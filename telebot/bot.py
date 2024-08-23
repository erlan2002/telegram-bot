# import telebot
# from time import sleep


# TOKEN = '7337830271:AAEsRLvMBlNziR2_F9GwRplUGX9dqbVRaes'


# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(comands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, я бот. Чем могу помочь?')

# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, 'Привет')
#     elif message.text == "Как дела":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Нормально.')

#     elif message.text == "Что делаешь?":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Данный момент обшаюсь с тобой.')
#     elif message.text == "Что ты хочешь от меня?":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Простите, я от вас ничего не хочу')
#     elif message.text == "Я от тебя хочу":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Что?')
#     elif message.text == "Помошь":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Какой')
#     elif message.text == "Забыл":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Ай-ай-ай чо за память!')
#     elif message.text == "А у тебя":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Хорошо тогда давай если вспомнишь напиши окей.')
#     else:
#         bot.send_message(message.from_user.id, 'Я тебя не поняла.')

# bot.infinity_polling()