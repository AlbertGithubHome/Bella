import backtrader as bt
import pandas as pd
import skdata as skd
import datetime
import sys

'''
加载数据
'''
def load_data(code):
    try:
        df = pd.read_csv(f'data/{code}.csv')
    except FileNotFoundError:
        raise FileNotFoundError(f"未找到文件：{code}.csv")

    try:
        df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
        df.set_index('trade_date', inplace=True)
        df = df[['open', 'high', 'low', 'close', 'vol']]
        df.rename(columns={'vol': 'volume'}, inplace=True)
        df.sort_index(inplace=True)
    except Exception as e:
        raise ValueError(f'处理数据时出错: {e}')

    return df

def zprint(*args, **kwargs):
    # 打印到文件
    with open(".testing.log", "a", encoding="utf-8") as f: print(*args, **kwargs, file=f)
    # 打印到控制台
    print(*args, **kwargs)

def zprint_init(*args, **kwargs):
    with open(".testing.log", "w", encoding="utf-8") as f: print(*args, **kwargs, file=f)

'''
策略类
买入信号：股价在20日线上方，上穿5日线；股价在5日线上方，上穿20日线
卖出信号：跌破5日线第二日收盘依旧在5日线之下卖出
'''
class CrossMA5Strategy(bt.Strategy):
    def __init__(self):
        bt.indicators.MACDHisto(self.datas[0])
        self.ma5 = bt.ind.SMA(self.data.close, period=5)
        self.ma20 = bt.ind.SMA(self.data.close, period=20)
        self.buy_price = None  # 记录买入价格
        self.order = None # 存在订单
        self.buy_count = 0 # 买入次数

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        zprint(f'{dt.isoformat()}, {txt}')

    def notify_order(self, order):
        if order.status in [order.Completed]:
            dt = bt.num2date(order.executed.dt).date()  # 成交时间
            price = order.executed.price
            size = order.executed.size
            if order.isbuy():
                self.buy_price = price
                self.buy_count += 1
                self.log(f'买入 成交价: {price:.2f} 数量: {size:.0f}（成交时间: {dt}，买入次数：{self.buy_count}）')
            elif order.issell():
                sell_price = price
                if self.buy_price:
                    gain = (sell_price - self.buy_price) / self.buy_price * 100
                    self.log(f'卖出 成交价: {sell_price:.2f} 数量: {size:.0f}（成交时间: {dt}），本次收益: {gain:.2f}%\n')
                else:
                    self.log(f'卖出 成交价: {sell_price:.2f} 数量: {size:.0f}（成交时间: {dt}），但未记录买入价\n')
                self.buy_price = None  # 重置买入价
            self.order = None
        elif order.status in [order.Canceled, order.Rejected]:
            self.log(f'订单未成交：状态 {order.Status[order.status]}')
            self.order = None

    def next(self):
        if len(self.data) < 6:
            return

        if self.order:  # 有挂单还没完成，跳过
            return

        close = self.data.close[0]
        prev_close = self.data.close[-1]
        ma5 = self.ma5[0]
        prev_ma5 = self.ma5[-1]
        ma20 = self.ma20[0]
        prev_ma20 = self.ma20[-1]

        # 当日直接买入
        if not self.position:
            if (prev_close < prev_ma5 and close > ma5 and close >= ma20) or (prev_close < prev_ma20 and close > ma20 and close >= ma5):
                self.log(f'满足买入条件：昨收 {prev_close:.2f} < 昨MA5 {prev_ma5:.2f} 且 今收 {close:.2f} > 今MA5 {ma5:.2f}')
                #self.buy()
                self.order = self.order_target_percent(target=0.99)
        else:
            if prev_close < prev_ma5 and close < ma5:
                self.log(f'满足卖出条件：昨收 {prev_close:.2f} < 昨MA5 {prev_ma5:.2f} 且 今收 {close:.2f} < 今MA5 {ma5:.2f}')
                #self.sell()
                self.order = self.order_target_percent(target=0.0)

'''
订单观察类
记录已经完成的订单
'''
class TradeObserver(bt.Analyzer):
    def __init__(self):
        self.trades = []

    def notify_trade(self, trade):
        if trade.isclosed:
            self.trades.append({
                'open_dt': trade.open_datetime(),
                'close_dt': trade.close_datetime(),
                'pnl': trade.pnl
            })

    def get_analysis(self):
        return self.trades



def run(code, show_plot, save_lot):
    # Cerebro设置
    cerebro = bt.Cerebro()
    cerebro.addstrategy(CrossMA5Strategy)

    # 启用 Cheat-on-Close 模式
    cerebro.broker.set_coc(True)

    # 加载数据
    df = load_data(code)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    # 初始资金与手续费
    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.001)

    # 添加分析器（可选）
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(TradeObserver, _name='trades')

    # 执行回测
    initial_cash = cerebro.broker.getvalue()  # 初始资金
    zprint('初始资金: %.2f' % initial_cash)
    results = cerebro.run()
    final_cash = cerebro.broker.getvalue()
    zprint('结束资金: %.2f' % final_cash)

    # 回测区间
    bt_start = df.index[0].strftime('%Y-%m-%d')
    bt_end = df.index[-1].strftime('%Y-%m-%d')
    zprint(f'\n+++++++++++++++++++++++++++++++++\n回测区间: {bt_start} ~ {bt_end}')

    # 计算盈亏百分比
    profit_percent = (final_cash - initial_cash) / initial_cash * 100
    zprint('总计收益: %.2f%%' % profit_percent)

    # 输出分析器结果
    strat = results[0]
    zprint("夏普比率:", strat.analyzers.sharpe.get_analysis())
    zprint("最大回撤:", strat.analyzers.drawdown.get_analysis())

    # 绘图：蜡烛图 + 买卖点箭头
    if show_plot or save_lot:
        # cerebro.plot(style='candlestick', barup='lightcoral', bardown='lightgreen', volup='lightcoral', voldown='lightgreen')
        # cerebro.plot(style='candlestick')
        from backtrader import plot
        import matplotlib.dates as mdates
        plotter = plot.Plot(style='candlestick')
        original_show = plotter.show

        def new_show(self, *args, **kwargs):
            figs = self.plot(strat, **kwargs)
            trade_analysis = strat.analyzers.trades.get_analysis()
            for fig in figs:
                sharpe = strat.analyzers.sharpe.get_analysis().get('sharperatio', None)
                drawdown = strat.analyzers.drawdown.get_analysis().max.drawdown  # 最大回撤 %
                title_text = (
                    f"Code: {code} | Date Range: {bt_start} ~ {bt_end} | "
                    f"Initial Cash: {initial_cash:.2f} | Final Cash: {final_cash:.2f} | Total Return: {profit_percent:.2f}% | "
                    f"Sharpe Ratio: {sharpe:.2f} | Max Drawdown: {drawdown:.2f}% | Buy Count: {strat.buy_count}"
                )
                zprint(title_text)
                fig.suptitle(title_text, fontsize=10, y=0.04)

                # 保存图像到本地
                if save_lot:
                    fig.set_size_inches(19.2, 10.8)  # 1080P = 1920 * 1080
                    fig.savefig('pic/{0}-{1}.png'.format(datetime.datetime.now().strftime('%Y%m%d'), code), dpi=100, bbox_inches='tight')
            if show_plot:
                original_show()
            return figs
        plotter.show = new_show.__get__(plotter)
        cerebro.plot(plotter=plotter)


def normalize_code(code):
    if len(code) == 6: code = code + ".SZ" if code[0] < '6' else code + '.SH'
    return code

if __name__ == '__main__':
    code = '000678' if len(sys.argv) <= 1 else sys.argv[1]
    code = normalize_code(code)
    skd.download_last_year_data(code)
    # skd.download_data_from_date(code, '20241201')
    zprint_init()
    run(code, True, False)
