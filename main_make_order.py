import shioaji as sj
from shioaji.constant import Action, StockPriceType, OrderType
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
    ca_path=os.environ["CA_CERT_PATH"],
    ca_passwd=os.environ["CA_PASSWORD"],
)

print(result)

# 商品檔 - 請修改此處
# 準備下單的 Contract
# 使用 00878 國泰永續高股息
contract = api.Contracts.Stocks["00878"]
print(f"Contract: {contract}")

# 建立委託下單的 Order
order = sj.order.StockOrder(
    action=Action.Buy, # 買進
    price=contract.reference, # 以平盤價買進
    quantity=1, # 下單數量
    price_type=StockPriceType.LMT, # 限價單
    order_type=OrderType.ROD, # 當日有效單
    account=api.stock_account, # 使用預設的帳戶
)
print(f"Order: {order}")

# 送出委託單
trade = api.place_order(contract=contract, order=order)
print(f"Trade: {trade}")

# 更新狀態
api.update_status()
print(f"Status: {trade.status}")