from config import BOT_TOKEN

import telebot

bot = telebot.TeleBot(token=BOT_TOKEN)

if __name__ == "__main__":
    from handlers import bot
    bot.polling(non_stop=True, interval=0)