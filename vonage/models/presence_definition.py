from odoo import fields, models


class PresenceDefinition(models.Model):
    _name = "presence_definition"
    _description = "Presence Definition"

    presence_id = fields.Char(string="Presence ID", required=True)
    selectable = fields.Boolean(string="Selectable")
    description = fields.Char(string="Description")
    is_custom_state = fields.Boolean(string="Is Custom State")
    # MTN 11/2/24 How to debug this?
    # category_id = fields.Many2one("presence_category", string="Category")
