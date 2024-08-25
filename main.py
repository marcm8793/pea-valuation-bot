import json
import requests
from datetime import datetime
import telebot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query'

def load_portfolio():
    with open('portfolio.json', 'r') as f:
        return json.load(f)

def get_current_price(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_URL, params=params)
    data = response.json()

    if 'Global Quote' in data and '05. price' in data['Global Quote']:
        return float(data['Global Quote']['05. price'])
    else:
        raise Exception(f"Unable to fetch price for {symbol}")

def calculate_portfolio_value(portfolio):
    total_value = portfolio['cash'] # Cash as initial value
    for asset, data in portfolio['assets'].items():
        quantity = data['quantity']
        current_price = get_current_price(asset)
        total_value += quantity * current_price
    return total_value

def calculate_returns(portfolio, current_value):
    initial_investment = portfolio['initial_investment']
    investment_date = datetime.strptime(portfolio['investment_date'], '%Y-%m-%d')
    total_return = current_value - initial_investment
    total_return_percentage = (total_return / initial_investment) * 100

    years_passed = (datetime.now() - investment_date).days / 365.25
    annual_return = ((current_value / initial_investment) ** (1 / years_passed) - 1) * 100

    return total_return, total_return_percentage, annual_return

def send_telegram_message(message):
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
    bot.send_message(TELEGRAM_CHAT_ID, message)

def format_currency(value):
    return f"€{value:,.2f}"

def main():
    portfolio = load_portfolio()
    current_value = calculate_portfolio_value(portfolio)
    total_return, total_return_percentage, annual_return = calculate_returns(portfolio, current_value)

    message = f"""
Portfolio Valuation:
Current Value: {format_currency(current_value)}
Initial Investment: {format_currency(portfolio['initial_investment'])}
Total Return: {format_currency(total_return)} ({total_return_percentage:.2f}%)
Annual Average Return 📈: {annual_return:.2f}%
Unallocated Cash: {format_currency(portfolio['cash'])}
"""

    send_telegram_message(message)
    print("Message sent successfully!")

if __name__ == "__main__":
    main()
