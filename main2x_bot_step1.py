from pyrogram import Client
from pyrogram.types import Message

api_id = 3477634
api_hash = 'b892572907ad5fbce8a89a3ea947ed62'
bot_token = '1597619460:AAHSfzUFrAcjlqe7SpKK-PEUzN5lfo9bon4'

client = Client(session_name='mybot', bot_token=bot_token, api_id=api_id, api_hash=api_hash)


@client.on_message()
def handle_message(bot: Client, message: Message):
    user_id = message.from_user.id
    if message.text:
        bot.send_message(user_id, message.text)
    elif message.voice:
        print(message.voice)
        # bot.send_voice(user_id, message.voice)


client.run()
