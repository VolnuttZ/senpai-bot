import telebot
import os
import bot_functions
from dotenv import load_dotenv

# load enviromental variables from .env file
load_dotenv()

# bot instance
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

"""
commands and their functions:
"""


@bot.message_handler(commands=['holi'])
def say_holi(message):

    bot.reply_to(message, "Holi uwu")


@bot.message_handler(commands=['love'])
def say_love(message):

    bot.reply_to(message, "Grecia & Temo U///U")


@bot.message_handler(commands=['meme'])
def send_meme(message):

    meme_url = bot_functions.get_random_meme()
    bot.send_photo(message.chat.id, meme_url)


@bot.message_handler(commands=['news'])
def send_anime_news(message):

    news = bot_functions.get_anime_news()
    for new in news:
        bot.send_message(message.chat.id, new)


@bot.message_handler(commands=['waifu'])
def send_waifu(message):

    gif_url = bot_functions.give_me_a_waifu()
    bot.send_document(message.chat.id, gif_url)


@bot.message_handler(commands=['character'])
def send_image_character(message):

    msg = bot.reply_to(message, "write character's name")
    bot.register_next_step_handler(msg, process_image_character)


def process_image_character(message):

    name = message.text
    img_url = bot_functions.get_image_character(name)
    bot.send_photo(message.chat.id, img_url)


@bot.message_handler(commands=['anime'])
def send_anime_description(message):

    msg = bot.reply_to(message, "write anime's title")
    bot.register_next_step_handler(msg, process_anime_description)


def process_anime_description(message):

    title = message.text
    info = bot_functions.get_anime_info(title)

    description = info.description
    url = info.url
    episodes = info.episodes

    bot.send_message(message.chat.id, url)
    bot.send_message(message.chat.id, description + '\n episodes: ' + episodes)


@bot.message_handler(commands=['recommend'])
def send_recommendations(message):

    msg = bot.reply_to(message,
                       "write an anime's title for based recommendations")
    bot.register_next_step_handler(msg, process_recommendations)


def process_recommendations(message):

    title = message.text
    info = bot_functions.get_anime_info(title)

    recommendations = ', '.join(info.recommend())
    bot.send_message(message.chat.id, recommendations)


@bot.message_handler(commands=['openings'])
def send_openings(message):

    msg = bot.reply_to(message, "write anime's title")
    bot.register_next_step_handler(msg, process_openings)


def process_openings(message):
    anime = message.text
    info = bot_functions.get_anime_info(anime)

    openings = ', '.join(info.opening_themes)
    bot.send_message(message.chat.id, openings)


@bot.message_handler(commands=['endings'])
def send_endings(message):

    msg = bot.reply_to(message, "write anime's title")
    bot.register_next_step_handler(msg, process_endings)


def process_endings(message):
    anime = message.text
    info = bot_functions.get_anime_info(anime)

    endings = ', '.join(info.ending_themes)
    bot.send_message(message.chat.id, endings)


if __name__ == '__main__':
    bot.polling()
