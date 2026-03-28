# Binance Futures Trading Bot (Testnet)

## 📌 Overview
This project is a Python-based CLI trading bot that interacts with Binance Futures Testnet (USDT-M) to place Market and Limit orders.


## 🚀 Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL sides
- CLI-based input using argparse
- Input validation and error handling
- Logging of API requests and responses


## 🛠️ Tech Stack
- Python 3.x
- python-binance
- dotenv


## ⚙️ Setup

1. Clone the repository:
   git clone <your-repo-link>

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file in the root directory:
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   BASE_URL=https://testnet.binancefuture.com/fapi


## ▶️ Usage

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 64000


## 📄 Output
- Displays order summary and response details
- Logs all API interactions in `trading_bot.log`


## 📊 Logs Included
- One successful MARKET order
- One successful LIMIT order


## ⚠️ Assumptions
- Binance Futures Testnet is used
- Minimum order value is 100 USDT


## 📌 Notes
- `.env` file is not included for security reasons
- Replace API keys before running


## 👨‍💻 Author
Mohammed Nayeem Uddin