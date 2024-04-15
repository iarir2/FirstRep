from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text="1")],
    [KeyboardButton(text="2")]
]

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    row_width=1
)
