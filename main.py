from settings import API_KEY, BOT_KEY
import openai
import telebot
import requests
openai.api_key = API_KEY
bot = telebot.TeleBot(BOT_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.from_user.id, text='Привет. Я отвечу практически на любой твой вопрос. Что ты хочешь узнать?')


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
         model='text-davinci-003',
         prompt=message.text,
         temperature=0.5,
         max_tokens=1000,
         top_p=1.0,
         frequency_penalty=0.5,
         presence_penalty=0.0,
     )
    bot.send_message(chat_id=message.from_user.id, reply_to_message_id=message.message_id, text=response['choices'][0]['text'])

bot.polling()
