from mubble import Dispatch, Message, CallbackQuery
from mubble.rules import CallbackData, CallbackDataMarkup

from database import User, Casino
from keyboards import Keyboard
from tools.randomizer import get_random_emoji, random_money_emoji, random_casino_emoji

import random

dp = Dispatch()


@dp.callback_query(CallbackData("heads_tails_menu"))
async def heads_tails_bet_menu_handler(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    await cq.edit_text(
        f"{get_random_emoji()} <b>{user.nickname}</b>, вы выбрали игру <b>«Орел и Решка»</b>\n"
        f"{random_money_emoji()} Поставьте сумму на которую хотите сыграть",
        parse_mode="HTML",
        reply_markup=Keyboard.heads_tails_bet_menu,
    )


@dp.callback_query(CallbackDataMarkup("heads_tails_bet_<bet:int>"))
async def head_tails_bet_handler(cq: CallbackQuery, bet: int):
    user = await User.get_or_none(uid=cq.from_user.id)
    casino: Casino = await user.casino.first()
    if bet > casino.balance:
        await cq.answer(
            f"{random_casino_emoji()} Казино\n"
            f"Недостаточно денег на балансе!\n"
            f"Текущий баланс: {casino.balance}\n",
            show_alert=False,
        )
        return

    casino.bet = bet
    await casino.save()

    await cq.answer(
        f"{random_casino_emoji()} Казино\n"
        f"Ставка поставлена успешно!\n"
        f"Текущий баланс: {casino.balance}\n",
        show_alert=False,
    )
    await cq.edit_text(
        f"{random_casino_emoji()} <b>{user.nickname}</b>, выберите <b>«Орел»</b> или <b>«Решка»</b>\n\n",
        parse_mode="HTML",
        reply_markup=Keyboard.head_or_tail,
    )


async def check_top_win_lose(bet: int, is_win: bool, casino: Casino):
    if is_win:
        if casino.top_victory < bet:
            casino.top_victory = bet
    else:
        if casino.top_loss < bet:
            casino.top_loss = bet
    await casino.save()


@dp.callback_query(CallbackData("head") | CallbackData("tail"))
async def head_or_tail_handler(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    casino: Casino = await user.casino.first()

    result = random.choice(("head", "tail"))
    if cq.data.unwrap() == result:
        casino.balance += round(casino.bet * 1.2)
        casino.victories_count += 1
        text = (
            f"{random_money_emoji()} <b>{user.nickname}</b>, вы победили!\n"
            f"{random_casino_emoji()} <b>Вы выиграли: ${round(casino.bet * 1.2)}</b>"
        )
        is_win = True
    else:
        casino.balance -= casino.bet
        casino.losses_count += 1
        text = (
            f"{random_money_emoji()} <b>{user.nickname}</b>, вы проиграли!\n"
            f"{random_casino_emoji()} <b>Ваша ставка анулирована</b>"
        )
        is_win = False

    await check_top_win_lose(casino.bet, is_win, casino)
    await casino.save()
    await cq.edit_text(text, parse_mode="HTML", reply_markup=Keyboard.heads_tails_bet_menu)
