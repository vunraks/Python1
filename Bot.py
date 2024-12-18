import asyncio
import subprocess
import logging
import random
import subprocess
import requests
import datetime
from aiogram import Bot, Dispatcher,types, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7786893238:AAHl5sld2FiimnNIEnM2p10dsrShO_WnFKY")
dp = Dispatcher()
WEATHER_API_KEY = "8396e7375c51bcb646be334d2d696fa5"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"



@dp.message(Command("start"))
async def cmd_name(message: Message):
    await message.answer("Привет, я тест бот")

@dp.message(Command("info"))
async def cmd_name(message: Message):
    await message.reply("У меня есть такие команды - \n/start, \n/info, \n/who, \n/weather, \n/time, \n/name")

@dp.message(Command("who"))
async def cmd_name(message: Message):
    await message.reply("Никита")  



btn_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Хоррор")],
        [KeyboardButton(text="Приключения")],
        [KeyboardButton(text="Комедии")],
        [KeyboardButton(text="Фантастика")],
        [KeyboardButton(text="Триллеры")]
    ],
    resize_keyboard=True
)

horror = ["https://www.kinopoisk.ru/film/977288/","https://www.kinopoisk.ru/series/915196/","https://www.kinopoisk.ru/film/195524/"]
adventure = ["https://www.kinopoisk.ru/film/5078983/","https://www.kinopoisk.ru/film/522941/","https://www.kinopoisk.ru/film/427076/"]
comedy = ["https://www.kinopoisk.ru/film/8124/","https://www.kinopoisk.ru/film/42664/","https://www.kinopoisk.ru/film/6039/"]
fantastic = ["https://www.kinopoisk.ru/film/251733/","https://www.kinopoisk.ru/film/258687/","https://www.kinopoisk.ru/film/447301/"]
triller = ["https://www.kinopoisk.ru/film/397667/","https://www.kinopoisk.ru/film/361/","https://www.kinopoisk.ru/series/838050/"]


@dp.message(Command("films"))
async def cmd_name(message: Message):
    await message.answer("Выберите жанр", reply_markup=btn_keyboard)

@dp.message(lambda message: message.text == "Хоррор")
async def show_horror(message: Message):
    await message.reply("123" + random.choice(horror))

@dp.message(lambda message: message.text == "Приключения")
async def show_adventure(message: Message):
    await message.reply("212314" + random.choice(adventure))

@dp.message(lambda message: message.text == "Комедии")
async def show_comedy(message: Message):
    await message.reply("2314" + random.choice(comedy))

@dp.message(lambda message: message.text == "Фантастика")
async def show_fantastic(message: Message):
    await message.reply("21234" + random.choice(fantastic))

@dp.message(lambda message: message.text == "Триллеры")
async def show_triller(message: Message):
    await message.reply("вот есть такие" + random.choice(triller))







@dp.message(Command("name"))
async def cmd_name(message: Message):  
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"Привет, <b>{args[1]}</b>", parse_mode="HTML") 
    else:
        await message.answer("Пожалуйста, укажи свое имя после команды /name.") 



@dp.message(Command("special_buttons"))
async def cmd_special_buttons(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Запросить контакт", request_contact=True)],
        [types.KeyboardButton(text="Запросить викторину", request_poll=types.KeyboardButtonPollType(type='quiz'))],
    ] 
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("Выберите действие", reply_markup=keyboard)


@dp.message(lambda message: message.text == "Запросить викторину")
async def send_quiz(message: types.Message):
    question = "Какой самы большой океан на Земле?"
    options = ["Атлантический", "Индийский", "Тихий", "Северно Ледовитый"]  
    correct_option_id = 2  

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type='quiz',
        correct_option_id=correct_option_id,
        is_anonymous=False
    )
    

@dp.message(Command("game"))
async def launch_game(message: Message):
    def run_game():
        try:
            subprocess.Popen(r'D:\qBittorrent\The Binding of Isaac Rebirth\isaac-ng.exe')
            return "Игра запущена"
        except FileExistsError:
            return "Путь к игре не найден"
        
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_game)

    await message.reply(response)    



# @dp.message(lambda message: message.text == "Погода") 
# async def start_command(message: Message):
#     await message.answer(
#         "Напиши название города, и я расскажу тебе о погоде!"
#     )
# @dp.message(F.text)
# async def get_weather(message: Message):
#     city = message.text.strip()
#     try:
#         response = requests.get(WEATHER_URL, params={
#             'q': city,
#             'appid': WEATHER_API_KEY,
#             'units': 'metric',
#             'lang': 'ru'
#         })
#         data = response.json()  
#         logging.info(f"API response: {data}")  
#         if data["cod"] == 200:  
#             city_name = data["name"]
#             temp = data["main"]["temp"]
#             weather_desc = data["weather"][0]["description"]
#             wind_speed = data["wind"]["speed"]
#             weather_info = (
#                 f"🌆 <b>Город:</b> {city_name}\n"
#                 f"🌡 <b>Температура:</b> {temp}°C\n"
#                 f"☁ <b>Описание:</b> {weather_desc.capitalize()}\n"
#                 f"💨 <b>Ветер:</b> {wind_speed} м/с"
#             )
#             await message.answer(weather_info, parse_mode="HTML")
#         else:
#             await message.answer("Не удалось найти город. Проверьте название и попробуйте снова.")
#     except Exception as e:
#         logging.error(f"Ошибка: {e}")
#         await message.answer("Произошла ошибка. Попробуйте снова позже.")
# async def main():
#     await dp.start_polling()


# @dp.message(Command("button"))
# async def cmd_name(message: Message):  
#     kb = [
#         [types.KeyboardButton(text="Старт")],
#         [types.KeyboardButton(text="Инфо")],
#         [types.KeyboardButton(text="Время")],
#         [types.KeyboardButton(text="Погода")],
#         [types.KeyboardButton(text="Стоп")]
#     ]         
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#     await message.answer("Какую кнопку вы выбрали?", reply_markup=keyboard )

# @dp.message(lambda message: message.text == "Старт")
# async def firs_btn(message: Message):
#     await message.reply("Привет, я тестовый бот, нажми на кнопку инфо и получи больше информации!")

# @dp.message(lambda message: message.text == "Инфо")  
# async def second_btn(message: Message):
#     await message.reply("У меня есть такие команды - \n/start \n/info \n/who \n/weather \n/time \n/name")

# @dp.message(lambda message: message.text == "Время")

# @dp.message(F.text == "/time")
# async def time_command(message: Message):
#     now = datetime.now().strftime('%H:%M:%S___%d:%m:%Y')
#     await message.answer(f"Текущее время и дата в Алматы: {now}")    
# async def main():
#     await bot.delete_webhook(drop_pending_updates=True)  
#     await dp.start_polling(bot)  












    



















async def main():
    await dp.start_polling(bot)

if __name__== "__main__" :
   asyncio.run(main())

# engine = pyttsx3.init()

# engine.setProperty("rate",150)
# engine.setProperty("volume",0.9)

# engine.say("Добро пожаловать")

# engine.runAndWait()





    


# @dp.message()
# async def echo_message(message: types.Message):
#     await message.answer(f"Привет {message.from_user.first_name}, твой текст: \n{message.text}")  



    





# @dp.message(F.content_type == "animation")
# async def echo_gif(message: Message):
#     await message.reply_animation(message.animation.file_id)













#Вариант 1
@dp.message(Command("nname"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>Nikita</b>!", parse_mode="HTML")
    await message.answer("Hello, *Nikita*\!", parse_mode="MardownV2")


# #Вариант 2
# @dp.message()
# async def echo_message(message: types.Message):
#     await message.answer(f"Привет {message.from_user.first_name}, <b>{message.text}</b>!", parse_mode="HTML")
#     await message.answer(f"Hello, {message.from_user.first_name}, *{message.text}*\!", parse_mode="MardownV2")





