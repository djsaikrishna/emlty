# Project tg_bot_with_ChatGPT

tg_bot_with_ChatGPT - A simple telegram bot that answers on text questions with answers from chatGPT

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies 'pip install -r requirements.txt'
4. Go to telebram bot 'BotFather' and create your bot. Save your Api key
5. Register on openai.com - now it's not so easy from Russia, but it's possible
6. Go to https://platform.openai.com/account/api-keys and create 'API_KEY'
7. Create .env, write there your 'API_KEY="your_key"' and 'BOT_KEY="your_bot_key"'

## To start

Start main.py and go ask something your new bot

## Deploy

! If there is no docker/docker-compose on the server, install it. Instructions https://docs.docker.com/

### Creating folder for bot and go in "bot"
mkdir bot
cd bot

### Clone the repository to the current folder
git clone https://github.com/se-andrey/tg_bot_with_ChatGPT.git .

### Creating a file .env for key storage API_KEY=... и BOT_KEY=...
nano .env

### launch
docker-compose up -d