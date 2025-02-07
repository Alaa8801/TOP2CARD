import telebot

TOKEN = "8001843912:AAGFfa_cr9EA8pWW0j4mRVHc5rofBbG7Ax0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك في ORDER STORE! اختر الخدمة التي تريدها.")

bot.polling()
