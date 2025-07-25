import backtrader as bt
import pandas as pd

# === 1. 读取CVS文件（实为CSV格式）===
df = pd.read_csv('600644.csv')

# 转换日期格式并设为索引
df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
df.set_index('trade_date', inplace=True)

# 保留所需字段并按时间升序
df = df[['open', 'high', 'low', 'close', 'vol']]
df.rename(columns={'vol': 'volume'}, inplace=True)
df.sort_index(inplace=True)

# === 2. 策略类 ===
class CrossMA5Strategy(bt.Strategy):
    def __init__(self):
        self.ma5 = bt.ind.SMA(self.data.close, period=5)
        self.buy_price = None  # 记录买入价格

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                self.buy_price = order.executed.price
                self.log(f'买入 成交价: {self.buy_price:.2f}, 数量: {order.executed.size}')
            elif order.issell():
                sell_price = order.executed.price
                gain = (sell_price - self.buy_price) / self.buy_price * 100
                self.log(f'卖出 成交价: {sell_price:.2f}, 数量: {order.executed.size}，本次收益: {gain:.2f}%')

    def next(self):
        if len(self.data) < 6:
            return

        close = self.data.close[0]
        prev_close = self.data.close[-1]
        ma5 = self.ma5[0]
        prev_ma5 = self.ma5[-1]

        # 买入条件：昨日收盘<MA5 且 今日收盘>MA5
        if not self.position:
            if prev_close < prev_ma5 and close > ma5:
                self.log(f'满足买入条件：昨收 {prev_close:.2f} < 昨MA5 {prev_ma5:.2f} 且 今收 {close:.2f} > 今MA5 {ma5:.2f}')

                # 全仓买入（向下取整）
                cash = self.broker.get_cash()
                size = int(cash // close)
                if size > 0:
                    self.buy(size=size)

        # 卖出条件：昨日收盘<MA5 且 今日收盘<MA5
        else:
            if prev_close < prev_ma5 and close < ma5:
                self.log(f'满足卖出条件：昨收 {prev_close:.2f} < 昨MA5 {prev_ma5:.2f} 且 今收 {close:.2f} < 今MA5 {ma5:.2f}')
                self.sell()

# === 3. Cerebro设置 ===
cerebro = bt.Cerebro()
cerebro.addstrategy(CrossMA5Strategy)

# 加载数据
data = bt.feeds.PandasData(dataname=df)
cerebro.adddata(data)

# 初始资金与手续费
cerebro.broker.setcash(100000)
cerebro.broker.setcommission(commission=0.001)

# 添加分析器（可选）
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')

# 执行回测
print('初始资金: %.2f' % cerebro.broker.getvalue())
results = cerebro.run()
print('结束资金: %.2f' % cerebro.broker.getvalue())

# 输出分析器结果
strat = results[0]
print("夏普比率:", strat.analyzers.sharpe.get_analysis())
print("最大回撤:", strat.analyzers.drawdown.get_analysis())

# === 4. 绘图（蜡烛图 + 买卖点）===
cerebro.plot(style='candlestick')
