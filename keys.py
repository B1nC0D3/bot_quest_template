from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


REMOVE_KEYBOARD = ReplyKeyboardRemove()


def create_keyboard(buttons_text):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for button_text in buttons_text:
        markup.add(KeyboardButton(button_text))
    return markup
