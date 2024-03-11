import telebot
import secret


bot = telebot.TeleBot(secret.token)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    count = 0
    text = message.text.lower()
    chat_id = message.chat.id
    len_txt = len(text)
    vowels = set("aeiouуеэоаыяиюё")
    for letter in text:
        if letter in vowels:
            count += 1
    print("Количество гласных равно:")
    bot.send_message(chat_id, f'Общее количество символов: {str(len_txt)}\n'
                              f'Количество гласных: {count}')


bot.polling()
