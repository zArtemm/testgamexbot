from mubble import Dispatch, Message
from mubble.rules import Command

from database import User, Balance

dp = Dispatch()


@dp.message(Command("bal"))
async def bal_handler(message: Message):
    user = await User.get(uid=message.from_user.id)
    balance: Balance = await user.balance.first()

    await message.answer(f"Clicker: {balance.clicker}\nCasino: {balance.casino}\n")


@dp.message(Command("addbal"))
async def bal_handler(message: Message):
    user = await User.get(uid=message.from_user.id)
    balance: Balance = await user.balance.first()
    balance.clicker += 100
    balance.casino += 100

    await balance.save()

    await message.answer(f"Successfully added!\n/bal")
