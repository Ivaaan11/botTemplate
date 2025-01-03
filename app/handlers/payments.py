import app.keyboards as k

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.filters.command import Command

router = Router()



# donation

@router.message(Command('donate_5'))
async def donate(message: Message):
    amount = 5

    prices = [LabeledPrice(label='XTR', amount=amount)]
    await message.answer_invoice(
        title = 'voluntary donation',
        description = 'donating',
        prices = prices,
        provider_token = '',
        payload = f'{amount}_stars',
        currency='XTR',
        reply_markup = k.payment_kb(amount)
    )


@router.pre_checkout_query()
async def on_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=False, error_message='There in not enough space for money 😭')
