import yfinance as yf

nifty = yf.download("^NSEI", start="2005-01-01")
nifty.to_csv("nifty50_data.csv")

gold = yf.download("GC=F", start="2005-01-01")
gold.to_csv("gold_usd_per_oz.csv")
