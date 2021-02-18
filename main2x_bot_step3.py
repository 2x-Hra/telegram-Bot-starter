from pyrogram import Client
from  pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton ,ReplyKeyboardRemove
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery


app = Client("my_bot")
data =[]

def IKM(data):
    '''
        Explanation : Create a inLine button with name :text and key : cbd
        
    '''
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])

MAIN_KEYBOARD = ReplyKeyboardMarkup([['setname','setage'],['my profile']],resize_keyboard=True)
TEACHERS_INLINEKB = IKM( [('Dr Keshtkaran', 'TCH0'), ('Dr Hamze', 'TCH1'), ('Dr Sami', 'TCH2')] )
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
    return new_user

@app.on_message()
def handle_message(bot: Client , msg: Message):
    user = check_user(msg.from_user.id)
    if (msg.chat.type != 'private'): #
        return

    if msg.text:
        if (msg.text == '/start' ):
            user.state = 0
            bot.send_message(user.id, 'welcome' , reply_markup=TEACHERS_INLINEKB )

 


teachers = ['دکتر کشتکاران', 'دکتر حمزه', 'دکتر سامی'] #database simulator
 

@app.on_callback_query()
def handle_callback(bot: Client, query: CallbackQuery):
    if query.data.startswith('TCH'):
        i = int(query.data[3:])
        bot.edit_message_text(query.message.chat.id, query.message.message_id, teachers[i],
                              reply_markup=TEACHERS_INLINEKB)


 

app.run()