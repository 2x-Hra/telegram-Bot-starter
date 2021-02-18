from pyrogram import Client
from  pyrogram.types import Message

app = Client("my_bot")

@app.on_message()

def send_message(bot: Client , msg: Message):
    user_id = msg.from_user.id
    bot_text = msg.text
    
    if msg.text:
        bot.send_message(user_id, bot_text)
    elif msg.voice:

        print(msg.voice.file_id)
        bot.send_voice(user_id, msg.voice.file_id)
    elif msg.photo:
        bot.send_message(user_id, msg.photo.file_id)



    

app.run()