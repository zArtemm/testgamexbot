from mubble import InlineKeyboard, InlineButton


class Keyboard:
    # Главное меню
    menu = (
        InlineKeyboard()
        .add(InlineButton("🎰 Казино", callback_data="casino_menu"))
        .row()
        .add(InlineButton("🍪 Кликер", callback_data="clicker_menu"))
        .add(InlineButton("🎁 Бонус", callback_data="bonus_menu"))
        .row()
        .add(InlineButton("🏦 Бизнесы", callback_data="business_menu"))
    ).get_markup()

    # Кликер меню
    clicker_menu = (
        InlineKeyboard()
        .add(InlineButton("🍪 Кликнуть", callback_data="clicker_click"))
        .row()
        .add(InlineButton("🛒 Магазин", callback_data="clicker_shop"))
        .add(InlineButton("🏆 Топ кликеров", callback_data="clicker_top"))
        .row()
        .add(InlineButton("⬅️ Назад", callback_data="back_to_main_menu"))
    ).get_markup()

    # Меню магазина
    clicker_shop = (
        InlineKeyboard()
        .add(InlineButton("🍪50  +5 кликов", callback_data="clicks_5"))
        .add(InlineButton("🍪950  +100 кликов", callback_data="clicks_100"))
        .row()
        .add(InlineButton("🍪9250  +1000 кликов", callback_data="clicks_1000"))
        .row()
        .add(InlineButton("⬅️ Назад", callback_data="clicker_menu"))
    ).get_markup()

    # Топ кликеров
    clicker_top = (
        InlineKeyboard().add(InlineButton("⬅️ Назад", callback_data="clicker_menu"))
    ).get_markup()

    # Казино меню
    casino_menu = (
        InlineKeyboard()
        .add(InlineButton("🎲 Выбрать игру", callback_data="choose_casino_game"))
        .row()
        .add(InlineButton("👤 Моя статистика", callback_data="casino_statistics"))
        .add(InlineButton("🏆 Топ выигрышей", callback_data="top_casino_victories"))
        .row()
        .add(InlineButton("💳 Пополнить баланс", callback_data="topup_balance_menu"))
        .row()
        .add(InlineButton("⬅️ Назад", callback_data="back_to_main_menu"))
    ).get_markup()

    # Выбрать игру казино
    choose_casino_game = (
        InlineKeyboard()
        .add(InlineButton("🪙 Орел и Решка", callback_data="heads_tails_menu"))
        .row()
        .add(InlineButton("✨ Звездная охота", callback_data="star_hunt_bet"))
        .add(InlineButton("🎫 Лотерея", callback_data="lottery_bet"))
        .row()
        .add(InlineButton("⬅️ Назад", callback_data="casino_menu"))
    ).get_markup()

    # Орел и Решка ставка
    heads_tails_bet_menu = (
        InlineKeyboard()
        .add(InlineButton("50💲", callback_data="heads_tails_bet_50"))
        .add(InlineButton("100💲", callback_data="heads_tails_bet_100"))
        .add(InlineButton("500💲", callback_data="heads_tails_bet_500"))
        .row()
        .add(InlineButton("1k💲", callback_data="heads_tails_bet_1000"))
        .add(InlineButton("5k💲", callback_data="heads_tails_bet_5000"))
        .add(InlineButton("10k💲", callback_data="heads_tails_bet_10000"))
        .row()
        .add(InlineButton("⬅️ Назад", callback_data="choose_casino_game"))
    ).get_markup()

    # Орел и Решка выбор
    head_or_tail = (
        InlineKeyboard()
        .add(InlineButton("🟡 Орел", callback_data="head"))
        .add(InlineButton("⚫ Решка", callback_data="tail"))
    ).get_markup()

    # Казино статистика
    casino_statistics = (
        InlineKeyboard().add(InlineButton("⬅️ Назад", callback_data="casino_menu"))
    ).get_markup()

    # Топ выигрышей в казино
    top_casino_victories = (
        InlineKeyboard().add(InlineButton("⬅️ Назад", callback_data="casino_menu"))
    ).get_markup()

    # Пополнить баланс казино
    topup_balance_menu = (
        InlineKeyboard()
        .add(InlineButton("10💲", callback_data="topup_10"))
        .add(InlineButton("100💲", callback_data="topup_100"))
        .add(InlineButton("1k💲", callback_data="topup_1000"))
        .row()
        .add(InlineButton("10k💲", callback_data="topup_10000"))
        .add(InlineButton("100k💲", callback_data="topup_100000"))
        .add(InlineButton("1kk💲", callback_data="topup_1000000"))
        .row()
        .add(InlineButton("⬅️ Назад", callback_data="casino_menu"))
    ).get_markup()
