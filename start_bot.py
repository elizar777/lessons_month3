# from aiogram import Bot, Dispatcher, types, executor 
# from config import token

# bot = Bot(token=token)
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer("Привет Мир!Привет Geeks!")
    
    
# @dp.message_handler(commands='help')
# async def help(message:types.Message):
#     await message.answer("Чем я могу вам помочь?")
    
    
    
# @dp.message_handler(text='Geeks')
# async def geeks(message:types.Message):
#     await message.reply("Geeks - это айти курсы в Кыргызстане")
    
    
# @dp.message_handler(text='Привет')
# async def hello(message:types.Message):
#     await message.reply("Привет, как дела?")
    
# @dp.message_handler(commands='test')
# async def test(message:types.Message):
#     await message.answer_photo('https://prosettings.net/cdn-cgi/image/dpr=1%2Cf=auto%2Cfit=pad%2Cheight=675%2Cq=85%2Csharpen=2%2Cwidth=1200/wp-content/uploads/s1mple.png')
#     await message.answer_location(40.51931603792678, 72.80298388177104)
  

    


# executor.start_polling(dp)
    