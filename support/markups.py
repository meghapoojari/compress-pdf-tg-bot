from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Donate💫', url='t.me/MeDonate'),
            InlineKeyboardButton('More Bots🤖', url='t.me/BotsByBk')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Money Making Bot🥳', url='t.me/EasyMakeMoneyOnline_Bot'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
