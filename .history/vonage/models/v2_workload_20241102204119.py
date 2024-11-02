from odoo import fields, models


class Workload(models.Model):
    _name = "workload"
    _description = "VCC Workload"

    agent_id = fields.Many2one(
        "vcc.agent",
        string="Agent",
        ondelete="cascade",
    )
    since = fields.Datetime(string="Workload Since")
    calls = fields.Integer(string="Calls", default=0)
    semi_live = fields.Integer(string="Semi-Live Interactions", default=0)
    non_live = fields.Integer(string="Non-Live Interactions", default=0)
