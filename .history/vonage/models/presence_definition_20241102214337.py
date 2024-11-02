from odoo import fields, models


class PresenceDefinition(models.Model):
    _name = "vcc.presence.definition"
    _description = "VCC Presence Definition"

    presence_id = fields.Char(string="Presence ID", required=True)
    name = fields.Char(string="Presence Name", required=True)
    description = fields.Char(string="Description")
    selectable = fields.Boolean(string="Selectable", default=True)
    category = fields.Selection()
