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
print(accounts)
