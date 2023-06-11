import telebot

bot = telebot.TeleBot("6297181611:AAEQLUusY-4ojVrCkhsp-dPUdTR8A9rfTcY")


@bot.message_handler()
def info(message):
    if message.text == "game":
        bot.send_message(message.chat.id, "Хочешь поиграть в игру?")
        if message.text == "Да":
            bot.send_message(message.chat.id, "ok")


@bot.message_handler(commands=["start"])
def main(message):
    last_name = message.from_user.last_name
    if message.from_user.last_name:
        bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}")
    if not message.from_user.last_name:
        bot.send_message(message.chat.id, f"Привет")


bot.polling(none_stop=True)
