import requests
import telebot
from textblob import TextBlob
import os
from deep_translator import GoogleTranslator


# Создаем экземпляр бота
bot = telebot.TeleBot('7002831072:AAE8SchZO1vPkpfjQBcyt2dy7xThjmGKaxI')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи) Пришли сообщение, которое надо проанализировать')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    polarity = polar(message.text)
    #print(type(response))

    if polarity < 0:
      pol = 'Негативное'
    elif polarity == 0:
      pol = 'Отсутствует'
    else:
      pol = 'Текст в целом позитивен '

    subjectivity = subject(message.text)
    subjectivity = subjectivity * 100

    bot.send_message(message.chat.id, 'Влияние: ' + str(pol) + '\n\nCтепень (от -1 до +1): ' + str(polarity))



def polar(message):
    #text = TextBlob(message)

    translated = GoogleTranslator(source='auto', target='en').translate(message)
    print(translated)
    text = TextBlob(translated)
    analysis = text.sentiment.polarity
    print(analysis)

    return analysis


def subject(message):
    #text = TextBlob(message)

    translated = GoogleTranslator(source='auto', target='en').translate(message)
    print(translated)
    text = TextBlob(translated)
    analysis = text.sentiment.subjectivity
    print(analysis)

    return analysis


# Запускаем бота
