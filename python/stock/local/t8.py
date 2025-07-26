import backtrader as bt
import pandas as pd
import skdata as sdt

'''
加载数据
'''
def load_data(code):
    try:
        df = pd.read_csv(f'{code}.csv')
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

'''
策略类
买入信号：上穿5日线买入
卖出信号：跌破5日线第二日收盘依旧在5日线之下卖出
'''
class CrossMA5Strategy(bt.Strategy):
    def __init__(self):
        self.ma5 = bt.ind.SMA(self.data.close, period=5)
        self.buy_price = None  # 记录买入价格
        self.order = None # 存在订单

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')

    def notify_order(self, order):
        if order.status in [order.Completed]:
            dt = bt.num2date(order.executed.dt).date()  # 成交时间
            price = order.executed.price
            size = order.executed.size
            if order.isbuy():
                self.buy_price = price
                self.log(f'买入 成交价: {price:.2f} 数量: {size:.0f}（成交时间: {dt}）')
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

        # 当日直接买入
        if not self.position:
            if prev_close < prev_ma5 and close > ma5:
                self.log(f'满足买入条件：昨收 {prev_close:.2f} < 昨MA5 {prev_ma5:.2f} 且 今收 {close:.2f} > 今MA5 {ma5:.2f}')
                #self.buy()
                self.order = self.order_target_percent(target=0.99)
        else:
            if prev_close < prev_ma5 and close < ma5:
                self.log(f'满足卖出条件：昨收 {prev_close:.2f} < 昨MA5 {prev_ma5:.2f} 且 今收 {close:.2f} < 今MA5 {ma5:.2f}')
                #self.sell()
                self.order = self.order_target_percent(target=0.0)

def run(code):
    # Cerebro设置 ===
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

    # 执行回测
    initial_cash = cerebro.broker.getvalue()  # 初始资金
    print('初始资金: %.2f' % initial_cash)
    results = cerebro.run()
    final_cash = cerebro.broker.getvalue()
    print('结束资金: %.2f' % final_cash)

    # 回测区间
    start = df.index[0].strftime('%Y-%m-%d')
    end = df.index[-1].strftime('%Y-%m-%d')
    print(f'\n+++++++++++++++++++++++++++++++++\n回测区间: {start} ~ {end}')

    # 计算盈亏百分比
    profit_percent = (final_cash - initial_cash) / initial_cash * 100
    print('总计收益: %.2f%%' % profit_percent)

    # 输出分析器结果
    strat = results[0]
    print("夏普比率:", strat.analyzers.sharpe.get_analysis())
    print("最大回撤:", strat.analyzers.drawdown.get_analysis())

    # 绘图：蜡烛图 + 买卖点箭头
    # cerebro.plot(style='candlestick')
    cerebro.plot(style='candlestick', barup='lightcoral', bardown='lightgreen', volup='lightcoral', voldown='lightgreen')

if __name__ == '__main__':
    code = '600644.SH'
    sdt.download_last_year_data(code)
    run(code)
