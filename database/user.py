from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField(null=False)  # Telegram ID
    nickname = fields.CharField(max_length=255, null=True)

    # For clicker
    clicker_clicks_total = fields.IntField(default=0)
    clicker_click = fields.IntField(default=1)

    casino = fields.OneToOneField("models.Casino", related_name="user", null=False)

    # For casino
    # victories_count = fields.IntField(default=0)
    # losses_count = fields.IntField(default=0)
    # total_result = fields.IntField(default=0)
    # top_victory = fields.IntField(default=0)
    # top_loss = fields.IntField(default=0)
    # casino_balance = fields.IntField(default=10_000)

    balance = fields.OneToOneField("models.Balance", related_name="user", null=False)
