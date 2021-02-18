from pyrogram import Client
from  pyrogram.types import Message

app = Client(
    session_name="my_bot",
    bot_token='1597619460:AAHSfzUFrAcjlqe7SpKK-PEUzN5lfo9bon4',
    api_id= 3477634,
    api_hash= "b892572907ad5fbce8a89a3ea947ed62"
)

@app.on_message()

def send_message(bot: Client , msg: Message):
    user_id = msg.from_user.id
    bot_text = msg.text
    
    if msg.text:
        bot.send_message(user_id, bot_text)
    elif msg.voice:
        print(msg.voice)


    

app.run()