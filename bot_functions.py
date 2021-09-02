import praw
from animec import *
import os
from dotenv import load_dotenv

# load enviromental variables from .env file
load_dotenv()

def get_random_meme():
    """Get a random meme url from reddit

    Returns:
        str: meme url
    """
    reddit = praw.Reddit(client_id = os.getenv('CLIENT_ID'), 
                     client_secret = os.getenv('SECRET_KEY'), 
                     user_agent = os.getenv('USER_AGENT'))

    return reddit.subreddit("memes").random().url


def get_anime_news():
    """Get the latest three anime news

    Returns:
        list: list of news
    """
    articles = Aninews()
    [titles, links] = [articles.titles, articles.links]

    news = []
    for i in range(len(titles)):
        news.append(titles[i] + ': ' + links[i])

    return news


def give_me_a_waifu():
    """Get a random waifu gif url

    Returns:
        str: gif url
    """
    waifu = Waifu()
    return waifu.random_gif()


def get_image_character(character):
    """Get character image in url

    Args:
        character (str): anime character name

    Returns:
        str: image url
    """
    info_character = Charsearch(character)
    return info_character.image_url


def get_anime_info(title):
    """Get anime object

    Args:
        title (str): anime's title

    Returns:
        Anime: Object with anime information
    """
    return Anime(title)