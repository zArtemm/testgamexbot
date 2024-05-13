from mubble import Dispatch, Message, CallbackQuery
from mubble.rules import CallbackData, CallbackDataMarkup

from database.user import User
from keyboards import Keyboard
from tools.randomizer import get_random_emoji

dp = Dispatch()


@dp.callback_query(CallbackData("clicker_menu"))
async def clicker_menu(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    await cq.edit_text(
        f"🍪 <b>{user.nickname}</b>, вы в меню кликера!\n"
        f"{get_random_emoji()} <b>Воспользуйся клавиатурой по полной!</b>",
        parse_mode="HTML",
        reply_markup=Keyboard.clicker_menu,
    )


# Магазин кликов
@dp.callback_query(CallbackData("clicker_shop"))
async def clicker_shop(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    await cq.edit_text(
        f"🛒 <b>{user.nickname}</b>, вы в меню магазина!\n"
        f"{get_random_emoji()} <b>Покупайте клики чтобы увеличить ваш доход!</b>",
        parse_mode="HTML",
        reply_markup=Keyboard.clicker_shop,
    )


# Топ кликеров
@dp.callback_query(CallbackData("clicker_top"))
async def clicker_top(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    top_clickers = await User.all().order_by("-clicker_clicks_total").limit(10)

    users = [
        f'<a href="tg://user?id={user.uid}">{user.nickname}</a> — {user.clicker_clicks_total:,d}🍪'
        for user in top_clickers
    ]

    await cq.edit_text(
        f"{get_random_emoji()} <b>{user.nickname}</b>, вы в меню топ кликеров!\n\n"
        f"🏆 <b>Топ кликеров: </b>\n" + "\n".join(users),
        parse_mode="HTML",
        reply_markup=Keyboard.clicker_top,
    )


# Кликер
@dp.callback_query(CallbackData("clicker_click"))
async def clicker_click(cq: CallbackQuery):
    user = await User.get_or_none(uid=cq.from_user.id)
    user.clicker_clicks_total += user.clicker_click
    await user.save()

    await cq.answer(
        "🍪 Кликер\n"
        f"+{user.clicker_click}\n"
        f"Всего: {user.clicker_clicks_total}\n",
        show_alert=False,
    )


# Доделать покупку
@dp.callback_query(CallbackDataMarkup("clicks_<amount>"))
async def clicker_buying(cq: CallbackQuery, amount: int):
    prices = {"5": 50, "100": 950, "1000": 9250}
    user = await User.get_or_none(uid=cq.from_user.id)

    if user.clicker_clicks_total >= prices[amount]:
        user.clicker_clicks_total -= prices[amount]
        user.clicker_click += int(amount)
        await cq.answer(
            "🍪 Кликер\n"
            f"Успешно!\n"
            f"Количество кликов за раз: {user.clicker_click}\n",
            show_alert=False,
        )
        await user.save()

    else:
        await cq.answer(
            "🍪 Кликер\n"
            f"Недостаточно кликов!\n"
            f"Всего: {user.clicker_clicks_total}\n",
            show_alert=False,
        )
        return
