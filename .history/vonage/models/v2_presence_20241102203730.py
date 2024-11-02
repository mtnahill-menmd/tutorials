from odoo import models, fields


class Presence(models.Model):
    _name = "vcc.presence"
    _description = "VCC Presence"

    agent_id = fields.Many2one(
        "vcc.agent",
        string="Agent",
        ondelete="cascade",
    )
    presence_id = fields.Char(string="Presence ID")
    name = fields.Char(string="Presence Name")
    description = fields.Char(string="Description")
    since = fields.Datetime(string="Presence Since")
    eligible_for_routing = fields.Boolean(string="Eligible for Routing")
