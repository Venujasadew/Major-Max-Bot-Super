import os
import telebot


bot = telebot.TeleBot("1963767783:AAFBCjD3hFRWepgsSAITnrnQqM_5zdG_X8M")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm MajorMax Chat Bot")


@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")



bot.polling()