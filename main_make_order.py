import shioaji as sj
import os
from dotenv import load_dotenv

load_dotenv()

api = sj.Shioaji(simulation=False) # 正式模式
accounts = api.login(
    api_key=os.getenv('API_KEY'),
    secret_key=os.getenv('SECRET_KEY')  
)
accounts

## Activate CA
result = api.activate_ca(
    ca_path=os.getenv('CA_PATH'),
    ca_passwd=os.getenv('CA_PASSWD'),
    person_id=os.getenv('PERSON_ID')
)

print(result)

# 商品檔 - 請修改此處
contract = api.Contracts.Stocks.TSE["00878"]

# 證券委託單 - 請修改此處
order = api.Order(
    price=17.67,                                    # 價格
    quantity=1,                                     # 數量
    action=sj.constant.Action.Buy,                  # 買賣別
    price_type=sj.constant.StockPriceType.LMT,      # 委託價格類別
    order_type=sj.constant.OrderType.ROD,           # 委託條件
    account=api.stock_account                       # 下單帳號
)

# 下單
trade = api.place_order(contract, order)
trade