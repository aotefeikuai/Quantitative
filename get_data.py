import QUANTAXIS as QA
start = '2017-01-01'
end = '2017-07-31'
index_code = '000001'
benchmark = QA.QA_fetch_index_day_adv(index_code,start,end)

block = QA.QA_fetch_stock_block_adv(blockname='通达信88')
select_code = block.data.index.levels[1].values
data = QA.QA_fetch_stock_day_adv(list(select_code), start, end)
data_price = data.pivot('close')
period_return = ((data_price.iloc[-1]-data_price.iloc[0])/data_price.iloc[0]).dropna()
benchmark_return = (benchmark.data.iloc[-1]-benchmark.data.iloc[0])/benchmark.data.iloc[0]
# data_price

print(benchmark_return)
selrcted_code = period_return.sort_values()[-10:].index.values
print(selrcted_code)
financial = QA.QA_fetch_financial_report_adv(list(selrcted_code),'2016-01-01','2017-07-31')
financial.data.to_csv('financial_over_period.csv')
data_price[selrcted_code].to_csv('stock_price.csv')
print(financial.data)