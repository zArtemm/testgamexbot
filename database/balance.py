from tortoise import Model, fields


class Balance(Model):
    id = fields.IntField(pk=True)

    clicker = fields.IntField(default=0)
    casino = fields.IntField(default=10_000)
