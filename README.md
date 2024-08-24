# Portfolio Valuation Bot

This bot calculates the current value of your investment portfolio and sends the information via Telegram on the first day of each month.

## 1. Running locally

### Setup

1. Clone this repository.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your API keys:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   TELEGRAM_CHAT_ID=your_telegram_chat_id_here
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
   ```
4. Update the `portfolio.json` file with your investment details.

### Running the Bot

Run the bot using the following command:

```
python main.py
```

The bot will calculate your portfolio value and send a message to your specified Telegram chat.

## 2.Running on a VPS

### Setup

1. Clone this repository on your VPS:

   ```
   git clone https://github.com/your-username/portfolio-bot.git
   cd portfolio-bot
   ```

2. Create a virtual environment and activate it:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API keys:

   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   TELEGRAM_CHAT_ID=your_telegram_chat_id_here
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
   ```

5. Update the `portfolio.json` file with your investment details:
   ```json
   {
     "initial_investment": 10000,
     "investment_date": "2022-01-01",
     "cash": 1000,
     "assets": {
       "IWDA.AS": {
         "quantity": 100
       },
       "EMIM.AS": {
         "quantity": 50
       }
     }
   }
   ```

### Deployment on VPS

1. Ensure you have Python 3 installed on your VPS.

2. Navigate to the project directory:

   ```
   cd /path/to/portfolio-bot
   ```

3. Create a shell script to run the Python script:

   ```
   nano run_portfolio_bot.sh
   ```

4. Add the following content to the shell script:

   ```bash
   #!/bin/bash
   cd /path/to/portfolio-bot
   source venv/bin/activate
   python main.py
   deactivate
   ```

5. Make the shell script executable:

   ```
   chmod +x run_portfolio_bot.sh
   ```

6. Set up a cron job to run the script on the first of each month:

   ```
   crontab -e
   ```

7. Add the following line to the crontab file:

   ```
   0 9 1 * * /path/to/portfolio-bot/run_portfolio_bot.sh
   ```

   This will run the script at 9:00 AM on the first day of each month.

8. Save and exit the crontab editor.

### Manual Running

To run the bot manually:

```
./run_portfolio_bot.sh
```

The bot will calculate your portfolio value and send a message to your specified Telegram chat.

### Troubleshooting

- Check the cron job logs for any errors:

  ```
  grep CRON /var/log/syslog
  ```

- Ensure all paths in the shell script and cron job are absolute paths.

- If the script doesn't run, check the permissions of the script and the Python files.
