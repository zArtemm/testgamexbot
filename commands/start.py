from mubble import Dispatch, Message, CallbackQuery
from mubble.rules import StartCommand, CallbackData

from database import User, Balance, Casino
from tools.randomizer import get_random_emoji
from keyboards import Keyboard


dp = Dispatch()


@dp.message(StartCommand())
async def start(message: Message):
    user = await User.get_or_none(uid=message.from_user.id)
    if user is None:
        balance = await Balance.create()
        casino = await Casino.create()
        await User.create(
            uid=message.from_user.id,
            nickname=message.from_user.first_name,
            balance=balance,
            casino=casino,
        )

    await message.answer(
        f"💸 <b>{message.from_user.first_name}</b>, приветствуем тебя!\n\n"
        "🎯 <b>Твои возможности:</b>\n"
        "<blockquote>• Ты можешь играть, зарабатывать деньги, строить свой бизнес!\n"
        "• Построй свой бизнес и будь Top-1 среди всех пользователей!\n"
        "• Ты можешь построить майнинг-ферму, которая будет делать тебе стабильный доход!</blockquote>\n\n"
        f"{get_random_emoji()} <b>Воспользуйся меню, чтобы играть!</b>",
        parse_mode="HTML",
        reply_markup=Keyboard.menu,
    )


# Назад в главное меню
@dp.callback_query(CallbackData("back_to_main_menu"))
async def back_to_main_menu(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    await cq.edit_text(
        f"💸 <b>{user.nickname}</b>, приветствуем тебя!\n\n"
        "🎯 <b>Твои возможности:</b>\n"
        "<blockquote>• Ты можешь играть, зарабатывать деньги, строить свой бизнес!\n"
        "• Построй свой бизнес и будь Top-1 среди всех пользователей!\n"
        "• Ты можешь построить майнинг-ферму, которая будет делать тебе стабильный доход!</blockquote>\n\n"
        f"{get_random_emoji()} <b>Воспользуйся меню, чтобы играть!</b>",
        parse_mode="HTML",
        reply_markup=Keyboard.menu,
    )
