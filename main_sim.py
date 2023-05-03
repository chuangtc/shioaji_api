import shioaji as sj
import os
from dotenv import load_dotenv

load_dotenv()

api = sj.Shioaji(simulation=True) # 模擬模式
accounts = api.login(
    api_key=os.getenv('API_KEY'),
    secret_key=os.getenv('SECRET_KEY')  
)
accounts

# 商品檔 - 請修改此處
contract = api.Contracts.Stocks.TSE["0050"]

# 證券委託單 - 請修改此處
order = api.Order(
    price=18,                                       # 價格
    quantity=1,                                     # 數量
    action=sj.constant.Action.Buy,                  # 買賣別
    price_type=sj.constant.StockPriceType.LMT,      # 委託價格類別
    order_type=sj.constant.OrderType.ROD,           # 委託條件
    account=api.stock_account                       # 下單帳號
)

# 下單
trade = api.place_order(contract, order)
trade

# 商品檔 - 近月台指期貨, 請修改此處
contract = min(
    [
        x for x in api.Contracts.Futures.TXF 
        if x.code[-2:] not in ["R1", "R2"]
    ],
    key=lambda x: x.delivery_date
)

# 期貨委託單 - 請修改此處
order = api.Order(
    action=sj.constant.Action.Buy,                   # 買賣別
    price=15000,                                     # 價格
    quantity=1,                                      # 數量
    price_type=sj.constant.FuturesPriceType.LMT,     # 委託價格類別
    order_type=sj.constant.OrderType.ROD,            # 委託條件
    octype=sj.constant.FuturesOCType.Auto,           # 倉別
    account=api.futopt_account                       # 下單帳號
)

# 下單
trade = api.place_order(contract, order)


