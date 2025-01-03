from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from aiogram.fsm.context import FSMContext

from typing import Callable, Dict, Any, Awaitable



class CancelMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message) and event.text == '/cancel':
            state: FSMContext = data.get('state')
            if state:
                await state.clear()
                await event.answer('The action has been canceled')
                return
        return await handler(event, data)
