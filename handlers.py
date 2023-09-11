import telebot

from main import bot


@bot.message_handler(content_types=["photo"])
def echo(message: telebot.types.Message):
    print(message.photo)
    bot.reply_to(message, text=f'you wrote «{message.media_group_id}»')