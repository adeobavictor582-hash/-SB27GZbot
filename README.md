# SB27GZ Text Generator Bot

A simple Telegram bot that generates text for posts, captions, and quotes.

## Commands
- /start
- /generate
- /help

## Deploy on Railway

1. Push this repo to GitHub.
2. Create a new project on Railway → Deploy from GitHub.
3. Add environment variable:
   - `TELEGRAM_BOT_TOKEN` = your token from @BotFather
4. Railway runs the bot automatically.

## Run Locally

```bash
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=your_token
python main.py
