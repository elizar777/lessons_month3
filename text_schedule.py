
from config import token
import schedule, time, requests

def main():
    print("Привет всем!", time.ctime())

    
def second_main():
    print("Пока!")

def get_btc_price():
    url = "https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    respons = requests.get(url=url).json()
    result_btc = round(float(respons.get('price')))
    print(result_btc)
    
def get_eth_price():
    url = "https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    respons = requests.get(url=url).json()
    result_eht = round(float(respons.get('price')))
    print(f"EHT: {result_eht}")
    
  
    
    


schedule.every(1).seconds.do(get_eth_price)




# schedule.every().seconds.do(main)
# schedule.every().minute.at(':37').do(main)
# schedule.every().minute.at(':55').do(second_main)

while True:
    schedule.run_pending()