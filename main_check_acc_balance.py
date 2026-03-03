import shioaji as sj
import os
from dotenv import load_dotenv

load_dotenv()

api = sj.Shioaji(simulation=False) 

accounts = api.login(
    api_key=os.getenv('API_KEY'),
    secret_key=os.getenv('SECRET_KEY')  
)
api.activate_ca(
        ca_path=os.getenv("CA_CERT_PATH"),
        ca_passwd=os.getenv("CA_PASSWORD"),
    )

print("login and activate ca success")

tmp=api.account_balance()

print(tmp)
