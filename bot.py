from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import tomsarkgh
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = TeleBot(token=TOKEN)



@bot.message_handler(commands=['start'])
def chat(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Concerts", callback_data="concerts"),
        InlineKeyboardButton("Theatre", callback_data="theatre"),
        InlineKeyboardButton("Opera and Ballet", callback_data="opera_ballet")
    )
    
    bot.send_message(message.chat.id, "Welcome! Choose a category", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["concerts", "theatre", "opera_ballet"])
def callback_query(call):
    message = call.message
    category = call.data
    concerts = tomsarkgh.parse(category)

    bot.send_message(message.chat.id, concerts)

bot.polling()


    