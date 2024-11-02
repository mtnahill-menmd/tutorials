from odoo import fields, models


class PresenceDefinition(models.Model):
    _name = "vcc.presence.definition"
    _description = "VCC Presence Definition"

    presence_id = fields.Char(string="Presence ID", required=True)
    name = fields.Char()
    description = fields.Char()
    selectable = fields.Boolean()
    category = fields.Selection()
