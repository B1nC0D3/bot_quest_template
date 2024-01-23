from telebot import TeleBot
from config import TOKEN
from quest_data import QUESTIONS
from keys import create_keyboard, REMOVE_KEYBOARD

bot = TeleBot(TOKEN)

STATE = {}


def check_state(message):
    return STATE.get(message.chat.id)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'start message')


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, 'help message')


@bot.message_handler(commands=['start_quest'])
def start_quest_handler(message):
    bot.send_message(message.chat.id, 'started quest')
    STATE[message.chat.id] = 'start'
    send_question(message)


@bot.message_handler(func=check_state)
def questions_handler(message):
    if not validate_user_answer(message):
        return
    send_question(message)
    check_win_condition(message)


@bot.message_handler(content_types=['text'])
def start_quest_handler(message):
    bot.send_message(message.chat.id, 'i dont get it!')


def check_win_condition(message):
    current_state = STATE[message.chat.id]
    current_question = QUESTIONS[current_state]
    current_answers = current_question.get('answers')
    if current_answers:
        return True
    message_text = 'You lose!'
    if current_question['win']:
        message_text = 'You win!'
    bot.send_message(message.chat.id, message_text)
    STATE.pop(message.chat.id)
    return False


def validate_user_answer(message):
    current_state = STATE[message.chat.id]
    current_question = QUESTIONS[current_state]
    current_answers = current_question['answers']
    next_question_key = current_answers.get(message.text)
    if not next_question_key:
        bot.send_message(message.chat.id, 'use buttons!')
        return False
    STATE[message.chat.id] = next_question_key
    return True


def send_question(message):
    current_question = QUESTIONS[STATE[message.chat.id]]
    current_answers = current_question.get('answers')
    markup = REMOVE_KEYBOARD
    if current_answers:
        markup = create_keyboard(current_answers.keys())
    bot.send_message(message.chat.id, current_question['text'], reply_markup=markup)


bot.polling()
