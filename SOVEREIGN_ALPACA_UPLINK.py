import os
import time
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from SOVEREIGN_MARKET_EYE import SovereignMarketEye

load_dotenv()

class AlpacaUplink:
    def __init__(self, paper_trading=True):
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.api_key = os.getenv("ALPACA_API_KEY")
        self.secret_key = os.getenv("ALPACA_SECRET_KEY")
        
        if not self.api_key or not self.secret_key:
            print("[CRITICAL ERROR]: Alpaca Keys not found in .env file.")
            self.api = None
            return

        self.base_url = "https://paper-api.alpaca.markets" if paper_trading else "https://api.alpaca.markets"
        mode = "PAPER TRADING (SIMULATED FUNDS)" if paper_trading else "LIVE TRADING (REAL MONEY ACTIVATED)"
        print(f"=====================================================")
        print(f"--- [AEON UPLINK]: INITIALIZING ALPACA CONNECTION ---")
        print(f"--- MODE: {mode} ---")
        print(f"=====================================================")

        try:
            self.api = tradeapi.REST(self.api_key, self.secret_key, self.base_url, api_version='v2')
            account = self.api.get_account()
            if account.trading_blocked:
                print('[CRITICAL ERROR]: Account is currently restricted from trading.')
            else:
                print(f"[STATUS]: Connection Verified. Buying Power: ${float(account.buying_power):.2f}")
        except Exception as e:
            print(f"[CRITICAL ERROR]: Failed to connect to Alpaca: {e}")
            self.api = None

        self.market_eye = SovereignMarketEye()

    def execute_live_trade(self, ticker, signal, price):
        if not self.api: return
        try:
            account = self.api.get_account()
            buying_power = float(account.buying_power)
            
            if signal == "BUY":
                allocation = buying_power * 0.20
                if allocation < price: return
                qty = int(allocation // price)
                if qty <= 0: return
                print(f"[AEON EXECUTING]: Submitting MARKET BUY for {qty} shares of {ticker}...")
                order = self.api.submit_order(symbol=ticker, qty=qty, side='buy', type='market', time_in_force='gtc')
                print(f"[SUCCESS]: Order Submitted. ID: {order.id}")
                
            elif signal == "SELL":
                try:
                    position = self.api.get_position(ticker)
                    qty = int(position.qty)
                except: return
                if qty > 0:
                    print(f"[AEON EXECUTING]: Submitting MARKET SELL for ALL {qty} shares of {ticker}...")
                    order = self.api.submit_order(symbol=ticker, qty=qty, side='sell', type='market', time_in_force='gtc')
                    print(f"[SUCCESS]: Liquidated position. ID: {order.id}")

        except Exception as e:
            print(f"[CRITICAL ERROR]: Execution failed on Alpaca Server: {e}")

    def run_market_loop(self, watch_list=["SPY", "AAPL", "TSLA", "MSFT", "NVDA"]):
        if not self.api: return
        print(f"\n[AEON UPLINK]: Commencing Autonomous Market Sweep...")
        clock = self.api.get_clock()
        if not clock.is_open:
            print("[AEON UPLINK]: The market is currently CLOSED. Waiting for the bell...")
            return

        for ticker in watch_list:
            signal, price = self.market_eye.scan_market(ticker)
            if signal in ["BUY", "SELL"]:
                print(f"[{ticker}]: ACTIONABLE SIGNAL DETECTED -> {signal}")
                self.execute_live_trade(ticker, signal, price)
            time.sleep(1) 

if __name__ == "__main__":
    uplink = AlpacaUplink(paper_trading=True)
    uplink.run_market_loop()