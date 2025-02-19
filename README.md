# shioaji_api
Shiaoji SinoPac 永豐金證券 Python API

## Git Source Code
* <https://github.com/chuangtc/shioaji_api>

## Requirements
* python >= 3.9
* Shioaji v1.2.5 (2025-02-19)

## Install required packages
```bash
pip install  -r requirements.txt
pip install shioaji[speed]
```

## Modify .env file
```bash
cp .env.template .env
```

## 欲開通正式環境API下單權限，客戶須於模擬環境完成登入及下單測試.
```bash
api = sj.Shioaji(simulation=True) # 模擬模式登入
accounts = api.login(
    api_key=os.getenv('API_KEY'),
    secret_key=os.getenv('SECRET_KEY')  
)
accounts
```

## 等正式開通後，會出現signed=True
```bash
Response Code: 0 | Event Code: 0 | Info: host '203.66.91.161:80', hostname '203.66.91.161:80' IP 203.66.91.161:80 (host 1 of 1) (host connection attempt 1 of 1) (total connection attempt 1 of 1) | Event: Session up[FutureAccount(person_id='F123456789', broker_id='F002000', account_id='1234567', signed=True, username='莊OO'), StockAccount(person_id='F123456789', broker_id='9A95', account_id='1234568', signed=True, username='莊OO')]
```


## 要正式下單時記得CA憑證路徑要用斜線(/)
```bash
CA_CERT_PATH="C:/ekey/1234/Sinopac.pfx"
```

## Reference
<https://github.com/Sinotrade/Shioaji>

## Totorial for Shioaji
[永豐金證券API](https://sinotrade.github.io/zh_TW/)
