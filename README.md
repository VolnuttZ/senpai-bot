# <p align="center">ohayouSenpaiBot for Telegram
<p align="center">A friki bot for anime, memes, and waifus. Just trust in Senpai.


<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## About The Project

This is a telegram bot that can be founded as @ohayouSenpaiBot, the features are mainly focused in anime world searching, but not limited to this. 
The goal of this project is to add new features and enhance the functionability of the bot. Feel free to add new commands and features :'3

### Built With

Just python, because python is love <3
* [python](https://www.python.org/)


## Getting Started

These are instructions to setup your own instance of this project locally. 

### Prerequisites

* Create your telegram bot with [BotFather](https://core.telegram.org/bots#6-botfather), save the API key
* Create your [reddit app](https://www.reddit.com/prefs/apps) , save the client-id, secret-key, and user-agent
* Install python 3, also a virtual environment is recommended to use

                                       
### Installation

* Clone the repository:
  ```sh
  $ git clone https://github.com/VolnuttZ/senpai-bot.git
  $ cd senpai-bot
  ```
* Install `requirements.txt` :
  ```sh
  $ python3 -m pip install -r requirements.txt
  ```
* Create `.env` file and add the environment variables of prerequisites, you could use your favorite text editor or command line:
  ```sh
  API_KEY = 'your api-key'
  CLIENT_ID = 'your client-id'
  SECRET_KEY = 'your secret-key'
  USER_AGENT = 'your user-agent'
  ```
* Run `main.py`:
  ```sh
  $ python3 main.py
  ```
  

## Usage

### List of commands
  * `/holi` say holi 
  * `/meme` random meme
  * `/waifu` random waifu gif
  * `/news` latest anime news
  * `/anime` anime description
  * `/character` character image
  * `/openings` anime openings
  * `/endings` anime endings
  * `/recommend` anime recommendations

                                       
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Cuauhtemoc Contreras - cm.cuauhtemoc@gmail.com

Project Link: [https://github.com/VolnuttZ/senpai-bot](https://github.com/VolnuttZ/senpai-bot)


## Acknowledgements

* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* [Animec](https://animec.readthedocs.io/en/latest/)
* [PRAW: The Python Reddit API Wrapper](https://github.com/praw-dev/praw)
* [MyAnimeList](https://myanimelist.net/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
