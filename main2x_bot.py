from pyrogram import Client
from  pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton ,ReplyKeyboardRemove
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery


app = Client("my_bot")

data =[]
MAIN_KEYBOARD = ReplyKeyboardMarkup([['setname','setage'],['my profile']],resize_keyboard=True)
class MyUser:
    def __init__(self, user_id):
        self.id = user_id
        self.state = 0
        self.name = None
        self.age = None

def check_user(user_id): # check if user exists ,if not user will added to data
    for user in data:
        if user_id == user.id:
            return user
    new_user = MyUser(user_id)
    data.append(new_user)

@app.on_message()
def handle_message(bot: Client , msg: Message):


    user = check_user(msg.from_user.id)
    if (msg.chat.type != 'private'): #
        return

    if msg.text:
        if (msg.text == '/start' ):
            user.state = 0
            bot.send_message(user.id, 'welcome' , reply_markup=MAIN_KEYBOARD )

        elif(user.state == 0 and msg.text == 'set name' ) :
            user.state = 1
            bot.send_message(user.id,'enter your name: ', reply_markup=ReplyKeyboardRemove)
                            
        elif (user.state == 1 and msg.text == 'set age') :    
            user.state = 2
            bot.send_message(user.id,'enter your age: ', reply_markup=ReplyKeyboardRemove)
        
        elif (user.state == 2 and msg.text == 'my profile'):    
            bot.send_message(user.id,f'Name: {user.name}\nAge: {user.age}')

        elif user.state == 1:
            user.name = msg.text
            user.state = 0
            bot.send_message(user.id,'your name saved: ', reply_markup=MAIN_KEYBOARD)
        
        elif user.state == 2:
            user.age = msg.text
            user.state = 0
            bot.send_message(user.id,'your age saved: ', reply_markup=MAIN_KEYBOARD)

teachers = ["dr hamze","dr kesht", "dr sami" ] #database simulator

@app.on_callback_query()
def handle_callback(bot: Client, query: CallbackQuery):
    bot.answer_callback_query(query.id, f"got {query.data}!!", show_alert=True) # show alert is for POP message
    




    

app.run()