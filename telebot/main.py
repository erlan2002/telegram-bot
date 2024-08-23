import telebot


TOKEN = '7337830271:AAEsRLvMBlNziR2_F9GwRplUGX9dqbVRaes'
bot = telebot.TeleBot(TOKEN)



# /start

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # coздание клавиатуры с кнопками
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Dior')
    button2 = telebot.types.KeyboardButton('Video-Dior')
    button3 = telebot.types.KeyboardButton('Help')
    button4 = telebot.types.KeyboardButton('Audio')

    keyboard.add(button1, button2, button3, button4)



    bot.send_message(message.chat.id, "Welcome to my store! Choose your choice!:", reply_markup=keyboard)

# Оброботчик кнопку диор.

@bot.message_handler(func=lambda message:message.text == 'Dior')
def send_dior(message):
     with open('img.1659980249_19-kartinkin-net-p-oboi-dior-krasivo-21dd-копия.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first shirt. Nice!")





# Обработчик нажатия на кнопку "Video-Nike"
@bot.message_handler(func=lambda message: message.text == '')
def send_video_dior(message):



    # Отправка видео
    with open('', 'rb') as vid:
        bot.send_location(message.chat.id, vid, caption="https://www.google.com/search?sca_esv=2fefa95070cab5a0&rlz=1C1IXYC_ruKG1104KG1104&sxsrf=ADLYWIIkp1JX0W7DClE1zIrRriesMiDKSA:1724391073545&q=christian+dior+paris+location&npsic=0&rflfq=1&rldoc=1&rllag=48869709,2311899,1095&tbm=lcl&sa=X&ved=2ahUKEwix2ZGrsYqIAxW1IhAIHRJpLF8QtgN6BAgcEAE&biw=1536&bih=730&dpr=1.25 .")




# Обработчик нажатия на кнопку "Help"
@bot.message_handler(func=lambda message: message.text == 'Help')
def send_help(message):





    # Отправка сообщения со справкой
    bot.send_message(message.chat.id, "Это справочное сообщение. Введите /start для начала работы с ботом.")

# Обработчик нажатия на кнопку "Audio"
    with open('Ирина - Айдахар .mp3', 'rb') as audio:
        bot.send_voice(message.chat.id, audio, caption="Это аудиосообщение.")




# Запуск бота
bot.polling()