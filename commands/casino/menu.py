from mubble import Dispatch, CallbackQuery
from mubble.rules import CallbackData

from database import User
from keyboards import Keyboard
from tools.randomizer import get_random_emoji, random_money_emoji


dp = Dispatch()


# Меню казино
@dp.callback_query(CallbackData("casino_menu"))
async def casino_menu(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    await cq.edit_text(
        f"🍒 <b>{user.nickname}</b>, вы в меню казино!\n"
        f"{random_money_emoji()} <b>Играй и зарабатывай!</b>",
        parse_mode="HTML",
        reply_markup=Keyboard.casino_menu,
    )


# Меню выбора игры
@dp.callback_query(CallbackData("choose_casino_game"))
async def choose_casino_game(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    await cq.edit_text(
        f"{get_random_emoji()} <b>{user.nickname}</b>, выберите игру!\n"
        f"{random_money_emoji()} <b>Удачи!</b>",
        parse_mode="HTML",
        reply_markup=Keyboard.choose_casino_game,
    )
