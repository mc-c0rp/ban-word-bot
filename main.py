# лёша иди нахуй пидор
import telebot
import sys

TOKEN = '7221171441:AAGaeYU_9zIJT9ss6IEWbs8QaJ5hm12DQIA'

bot = telebot.TeleBot(TOKEN)

ban_words = ['https://vm.tiktok.com/ZMr2qdHbH', 'https://vm.tiktok.com/zmr2qdhbh', 'носатый', 'sukaebalrot']

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "idi nahui")

@bot.message_handler(commands=['link'])
def link(message):
    bot.reply_to(message, "вот оно:\n`https://vm.tiktok.com/ZMr2qdHbH`", parse_mode="Markdown")

@bot.message_handler(commands=['destroy'])
def destroy(message):
    if message.chat.type in ['group', 'supergroup']:
        chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)

        if chat_member.status == 'creator':
            bot.reply_to(message, 'пизда мэсэй...')
            sys.exit()
        else:
            bot.reply_to(message, 'ага, соси жуй пидар')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if any(ban_word in message.text.lower() for ban_word in ban_words):
        bot.reply_to(message, 'футе он ниште шлангул нахуй')
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

bot.polling(none_stop=True)
