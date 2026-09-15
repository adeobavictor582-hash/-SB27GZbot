import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Store user topics temporarily
user_topics = {}

# ---------- Templates ----------
TEMPLATES = {
    "quote": [
        "Small steps every day lead to big results.",
        "Focus on progress, not perfection.",
        "Discipline beats motivation.",
        "Learn something new today.",
    ],
    "caption": [
        "Simple moments, lasting memories.",
        "Living one day at a time.",
        "Good vibes only.",
        "Making today count.",
    ],
    "post": [
        "Here is something worth sharing today. Stay consistent and keep learning.",
        "A short thought: the best time to start was yesterday. The next best time is now.",
        "Sharing a simple idea that helps me stay focused every day.",
    ],
}

# ---------- Commands ----------
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Hi. I generate text for you.\n\nType /generate to begin.\nType /help for info."
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(
        message,
        "How it works:\n"
        "1. Type /generate\n"
        "2. Choose a type\n"
        "3. I send you text.\n\n"
        "Commands:\n"
        "/start - Start\n"
        "/generate - Create text\n"
        "/help - This message"
    )

@bot.message_handler(commands=['generate'])
def generate(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(
        types.InlineKeyboardButton("Quote", callback_data="quote"),
        types.InlineKeyboardButton("Caption", callback_data="caption"),
        types.InlineKeyboardButton("Post", callback_data="post"),
    )
    bot.reply_to(message, "Choose a text type:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_choice(call):
    import random
    kind = call.data
    if kind in TEMPLATES:
        text = random.choice(TEMPLATES[kind])
        bot.send_message(call.message.chat.id, f"Here is your text:\n\n{text}")
    else:
        bot.send_message(call.message.chat.id, "Unknown type. Try /generate again.")
    bot.answer_callback_query(call.id)

# ---------- Fallback ----------
@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.reply_to(message, "Type /generate to create text, or /help for info.")

# ---------- Run ----------
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
