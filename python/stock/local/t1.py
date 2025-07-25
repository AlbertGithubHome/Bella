import backtrader as bt
import pandas as pd

# === 1. 读取CSV文件 ===
df = pd.read_csv('000002.csv')

# 转换日期格式并设为索引
df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
df.set_index('trade_date', inplace=True)

# 重命名列以适应 backtrader
df.rename(columns={
    'open': 'open',
    'high': 'high',
    'low': 'low',
    'close': 'close',
    'vol': 'volume'
}, inplace=True)

# 保留所需字段并按时间升序
df = df[['open', 'high', 'low', 'close', 'volume']]
df.sort_index(inplace=True)

# === 2. 策略类 ===
class CrossMA5Strategy(bt.Strategy):
    def __init__(self):
        self.ma5 = bt.ind.SMA(self.data.close, period=5)
        self.buy_signal = False
        self.sell_pending = False

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'买入 成交价: {order.executed.price:.2f}')
            elif order.issell():
                self.log(f'卖出 成交价: {order.executed.price:.2f}')

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
                self.buy_signal = True
        else:
            # 卖出条件：昨日收盘<MA5 且 今日收盘<MA5
            if prev_close < prev_ma5 and close < ma5:
                self.sell_pending = True

    def next_open(self):
        if self.buy_signal:
            self.buy()
            self.buy_signal = False
        elif self.sell_pending:
            self.sell()
            self.sell_pending = False

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

# === 4. 绘图（包含买卖点箭头）===
cerebro.plot(style='candlestick')
