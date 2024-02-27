import time
import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

os.getenv("api_key")

#Use your Mexc Api credentials here
#apikey = 'mx0vgluqnh5ygVOgf0'
#secretkey = '0a9a5276aa5343bd8d6d3d1fbc4af4f4'

api_key = 'mx0vgluqnh5ygVOgf0'
secret_key = '0a9a5276aa5343bd8d6d3d1fbc4af4f4'

#Connect to Mexc exchange
exchange = ccxt.mexc ({
    'apiKey' : api_key,
    'secret' : secret_key,
})

#Define the trading pair and timeframe
symbol = 'ETH/USDT'
timeframe = '1h'
size = 0.0015

#Function to check if the price is above or below the VWAP
def is_price_above_vwap(
    symbol: str,
    timeframe: str
) -> bool:
    #Fetch OHLCV Data
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

    #Calculate VWAP
    total_volume = 0
    vwap = 0
    for candle in ohlcv:
        # volume = candle(5)
        # [1707019200000, 2302.96, 2303.36, 2294.14, 2297.33, 2104.8374]
        # because we're in a list hinted by the opening of our 'for' loop we need to access
        # the index of the candle we want to access, not treating the candle as a function
        # candle(5) would be a function call, which would throw an error passing 5 as an argument
        # candle[5] is the 6th element of the list, which is the volume
        # it is the 6th because in list index's we start at 0

        volume = candle[5]
        close_price = candle[4]
        total_volume += volume
        vwap += close_price * volume
    vwap /= total_volume
    

    #Check if current price is above the VWAP
    current_price = exchange.fetch_ticker(symbol)['last']
    print(f'this is the current price', current_price)
    def currentPrice(current_price, vwap):
        if current_price > vwap:

            long = True
            return long
        else:
            long = False
            return long

    position = currentPrice(current_price, vwap) # this is the variable that will be returned
    # however the function is not returning anything so it will return None

    return position # this is the return statement


position = is_price_above_vwap(symbol, timeframe)

#Main Trading function
def execute_trade(
    symbol: str,
    position: bool
) -> None:
        #Check is the currentprice is above the vwap
        if position == True:
            #Place a buy order
            time.sleep(2)
            order = exchange.create_market_buy_order(symbol, size)
            print("Buy order placed:", order)
        else:
            #Place a sell order
            order = exchange.create_market_sell_order(symbol, size)
            print("Sell order placed:", order)

def new_func(symbol):
        return is_price_above_vwap(symbol, timeframe)

#Run the trading function
execute_trade(symbol, position)