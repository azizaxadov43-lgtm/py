import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram import Router
ky=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Tayyroman")]],resize_keyboard=True
)
iky=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Salom",callback_data="t")]])
Token="8885254803:AAG98lAQW2TBLJgNVKoNQOCEUT-xai3XLKg"
bot=Bot(token=Token)
dp=Dispatcher()
@dp.message(CommandStart())
async def yubor(message:Message):
    global i
    i=0
    #name=message.from_user.first_name
    global name
    name="Shaxrizoda"
    tsh=0
    chtid=message.chat.id
    if chtid==5297746319 or chtid==6126896201:
        if 1==1:
            us=message.from_user.username
            await bot.send_message(chat_id=5297746319,text=f"@{us} Tezroq yoz hal bo'ldi")
            await message.answer(f"Salom {name} men sizni anchadan bera kutgan edim .\n Sizga savolim bor edi ?.\nUni eshitishga tayyormisiz ?",reply_markup=ky)
    else:
        us=message.from_user.username
        await message.answer(f"Uzr men sizga xizmat ko'rsata olmayman !!!")
        await bot.send_message(chat_id=5297746319,text=f"@{us} yozdi sanga begona")
    #await message.answer("salom:",reply_markup=iky)
@dp.message(F.text=="Tayyroman")
async def qybor(message:Message):
    global i
    i+=1
    #name=message.from_user.first_name
    if i>=3:
        await message.answer("Eshitishga tayyor ekanligingizdan Xursand man siz Tez orada siz bilan bog'lanaman iltimos chatni to'liq tozlab yubormang !!!")
        us=message.from_user.username
        await bot.send_message(chat_id=5297746319,text=f"@{us} Tezroq yoz hal bo'ldi")
    else:
        await message.answer(f"{name}-Ishonch hosil qiling 3/{i}",reply_markup=ky)
"""@dp.message(F.data=="t")
async def yy(message:Message):
    await message.answer("salom",reply_markup=iky)"""
async def main():
    await dp.start_polling(bot)

asyncio.run(main())
