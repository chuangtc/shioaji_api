import shioaji as sj
import os
from dotenv import load_dotenv

load_dotenv()

api = sj.Shioaji(simulation=False) 
accounts = api.login(
    api_key=os.getenv('API_KEY'),
    secret_key=os.getenv('SECRET_KEY')  
)

tmp = api.quote.subscribe(
    api.Contracts.Stocks["0050"], 
    quote_type = sj.constant.QuoteType.Tick,
    version = sj.constant.QuoteVersion.v1
)

print(tmp)
