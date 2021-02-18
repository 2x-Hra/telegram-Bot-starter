from pyrogram import Client
from  pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton 


app = Client("my_bot")

class MyUser:
    def __init__(self, user_id):
        self.id = user_id
        self.state = 0

@app.on_message()
def send_message(bot: Client , msg: Message):
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


    

app.run()