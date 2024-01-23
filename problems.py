from telebot import TeleBot
from config import TOKEN
from keys import create_keyboard

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'start message')


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, 'help message')


@bot.message_handler(commands=['start_quest'])
def start_quest_handler(message):
    bot.send_message(message.chat.id, 'started quest')
    bot.register_next_step_handler(message, second_question)


def second_question(message):
    correct_answers = ['1', '2', '3']
    if message.text not in correct_answers:
        bot.register_next_step_handler(message, second_question)
        return
    markup = create_keyboard(correct_answers)
    bot.send_message(message.chat.id, 'message', reply_markup=markup)


bot.polling()
