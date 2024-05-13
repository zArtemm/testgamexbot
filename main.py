# Тебе нужно перейти на https://github.com/vladislavkovalskyi/mubble
# прочитать документацию о Dispatch, после чего переделать структуру проекта под этот Dispatch
from mubble import Token, API, Mubble, Dispatch
from tortoise import Tortoise

from commands import dps

api = API(Token.from_env(path_to_envfile=".env"))
dispatch = Dispatch()

for dp in dps:
    dispatch.load(dp)

bot = Mubble(api, dispatch=dispatch)


async def setup_database():
    await Tortoise.init(
        db_url="sqlite://database.sqlite3", modules={"models": ["database.user", "database.balance", "database.casino"]}
    )
    await Tortoise.generate_schemas()
    Tortoise.init_models(["database.user", "database.balance", "database.casino"], "models")

bot.loop_wrapper.on_startup.append(setup_database())
bot.run_forever()
