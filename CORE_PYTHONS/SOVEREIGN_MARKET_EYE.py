import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import os
import json

class SovereignMarketEye:
    def __init__(self, starting_capital=10000.0):
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.ledger_path = os.path.join(self.brain_path, "SOVEREIGN_TRADES.json")
        self.starting_capital = starting_capital
        
        self.ledger = self.load_ledger()

    def load_ledger(self):
        if os.path.exists(self.ledger_path):
            with open(self.ledger_path, "r") as f:
                return json.load(f)
        else:
            return {
                "available_cash": self.starting_capital,
                "positions": {}, 
                "trade_history": []
            }

    def save_ledger(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.ledger, f, indent=4)

    def calculate_rsi(self, data, window=14):
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).fillna(0)
        loss = (-delta.where(delta < 0, 0)).fillna(0)
        
        avg_gain = gain.rolling(window=window, min_periods=1).mean()
        avg_loss = loss.rolling(window=window, min_periods=1).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi.iloc[-1]

    def scan_market(self, ticker="SPY", days="60d"):
        print(f"\n[AEON MARKET EYE]: Scanning {ticker}...")
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period=days)
            if df.empty:
                return "ERROR", 0

            current_price = df['Close'].iloc[-1]
            
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            df['SMA_50'] = df['Close'].rolling(window=50).mean()
            
            current_sma20 = df['SMA_20'].iloc[-1]
            current_sma50 = df['SMA_50'].iloc[-1]
            current_rsi = self.calculate_rsi(df)

            print(f"[{ticker}] Price: ${current_price:.2f} | SMA20: ${current_sma20:.2f} | RSI: {current_rsi:.1f}")

            signal = "HOLD"
            if current_rsi < 30 or (current_sma20 > current_sma50 and current_rsi < 60):
                signal = "BUY"
            elif current_rsi > 70 or (current_sma20 < current_sma50 and current_rsi > 50):
                signal = "SELL"
                
            return signal, current_price
            
        except Exception as e:
            print(f"[ERROR]: Market Eye blinded: {e}")
            return "ERROR", 0

    def execute_paper_trade(self, ticker, signal, price):
        cash = self.ledger["available_cash"]
        positions = self.ledger["positions"]
        
        if signal == "BUY":
            investment_amount = cash * 0.20
            if investment_amount < price:
                print(f"[AEON]: Insufficient capital to buy {ticker}.")
                return

            shares_to_buy = int(investment_amount // price)
            if shares_to_buy == 0:
                return

            cost = shares_to_buy * price
            self.ledger["available_cash"] -= cost
            
            if ticker in positions:
                old_shares = positions[ticker]["shares"]
                old_avg = positions[ticker]["avg_price"]
                new_shares = old_shares + shares_to_buy
                new_avg = ((old_shares * old_avg) + cost) / new_shares
                positions[ticker]["shares"] = new_shares
                positions[ticker]["avg_price"] = new_avg
            else:
                positions[ticker] = {"shares": shares_to_buy, "avg_price": price}

            trade_record = f"[{datetime.datetime.now()}] BOUGHT {shares_to_buy} shares of {ticker} at ${price:.2f}"
            self.ledger["trade_history"].append(trade_record)
            print(f"[EXECUTE]: {trade_record}")
            print(f"[CASH REMAINING]: ${self.ledger['available_cash']:.2f}")
            self.save_ledger()

        elif signal == "SELL":
            if ticker in positions and positions[ticker]["shares"] > 0:
                shares_to_sell = positions[ticker]["shares"]
                revenue = shares_to_sell * price
                self.ledger["available_cash"] += revenue
                profit = revenue - (shares_to_sell * positions[ticker]["avg_price"])
                trade_record = f"[{datetime.datetime.now()}] SOLD {shares_to_sell} shares of {ticker} at ${price:.2f} (PROFIT: ${profit:.2f})"
                self.ledger["trade_history"].append(trade_record)
                print(f"[EXECUTE]: {trade_record}")
                del positions[ticker]
                print(f"[CASH REMAINING]: ${self.ledger['available_cash']:.2f}")
                self.save_ledger()

    def run_daily_scan(self, watch_list=["SPY", "AAPL", "TSLA", "MSFT"]):
        print(f"\n=====================================================")
        print(f"--- [AEON]: INITIALIZING MARKET PAPER TRADER ---")
        print(f"=====================================================")
        print(f"Starting Cash: ${self.ledger['available_cash']:.2f}")
        for ticker in watch_list:
            signal, price = self.scan_market(ticker)
            if signal in ["BUY", "SELL"]:
                print(f"[SIGNAL DETECTED]: {signal} on {ticker}")
                self.execute_paper_trade(ticker, signal, price)
            else:
                print(f"[AEON]: Maintaining discipline. Holding position on {ticker}.")
                
        total_value = self.ledger['available_cash']
        for t, data in self.ledger['positions'].items():
            _, current_price = self.scan_market(t, days="5d")
            total_value += (data['shares'] * current_price)
            
        print(f"\n[AEON PORTFOLIO]: Estimated Net Worth: ${total_value:.2f}")

if __name__ == "__main__":
    eye = SovereignMarketEye()
    eye.run_daily_scan()