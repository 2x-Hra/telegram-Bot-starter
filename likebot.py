from pyrogram import Client
from  pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton ,ReplyKeyboardRemove
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery
from pyrogram.types import InlineQuery, InlineQueryResultArticle,InputMessageContent

app = Client("my_bot")
data =[]

def IKM(data):
    '''
        Explanation : Create a inLine button with name: text and key: cbd

    '''
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])



@app.on_callback_query()
def handle_callback(bot: Client, query: CallbackQuery):
    '''
        this function for handling if user click on a INLINE BUTTON 
        and it will take care of it with changing the name of the Teacher in tlgram dynamically
    '''

@app.on_inline_query()
def handle_inline_query(bot: Client, query: InlineQuery):

    results = [InlineQueryResultArticle('title', InputMessageContent("Lets play a game"))]

    bot.answer_inline_query(query.id, results)
app.run()