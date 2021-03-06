from pyrogram import Client
from pyrogram.types import Message
from  pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton ,ReplyKeyboardRemove




client = Client(session_name='mybot')


@client.on_message()
def handle_message(bot: Client, msg: Message):
    '''
        This function check if user exists return the user , 
        otherwise it will create a new user.
        In step1 it only figure out what is the message type and make some simpleButton
    '''
    chat_id = msg.chat.id
    bot_text = msg.text
    if msg.text:
        bot.send_message(chat_id, bot_text,
                        reply_markup=ReplyKeyboardMarkup([['salam','khodafez'],['back']],resize_keyboard=True)
                        )
    elif msg.voice:
        print(msg.voice.file_id)
        bot.send_voice(chat_id, msg.voice.file_id)
    elif msg.photo:
        bot.send_message(chat_id, msg.photo.file_id)
    elif msg.document:
        bot.send_message(chat_id, msg.document.file_id)

client.run()
