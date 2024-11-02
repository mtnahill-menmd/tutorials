from odoo import fields, models


class PresenceDefinition(model.Model):
    _name = "PresenceDefinition"

    presence_id = fields.Char()
    name = fields.Char()
    description = fields.Char()
    selectable = fields.Boolean()
    category = fields.Selection()
