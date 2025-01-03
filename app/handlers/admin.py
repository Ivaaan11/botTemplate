import app.keyboards as k

from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()



# stopping the bot

@router.message(F.text.casefold() == 'stop')
async def cmd_stop(message: Message):
    # if admin
    
    await message.answer('Bot stopped')
    exit()