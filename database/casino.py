from tortoise import Model, fields


class Casino(Model):
    id = fields.IntField(pk=True)

    victories_count = fields.IntField(default=0)
    losses_count = fields.IntField(default=0)
    
    total_result = fields.IntField(default=0)

    top_victory = fields.FloatField(default=0)
    top_loss = fields.FloatField(default=0)

    balance = fields.IntField(default=10_000)

    bet = fields.IntField(null=True)
