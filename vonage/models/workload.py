from odoo import fields, models


class Workload(models.Model):
    _name = "vcc.workload"
    _description = "VCC Workload. Records workload metrics, such as calls and semi-live/non-live interactions."

    agent_id = fields.Many2one(
        "vcc.agent",
        string="Agent",
        ondelete="cascade",
        readonly=True,
        copy=False,
    )
    since = fields.Datetime(
        string="Workload Since",
        readonly=True,
        copy=False,
    )
    calls = fields.Integer(
        string="Calls",
        default=0,
        readonly=True,
        copy=False,
    )
    semi_live = fields.Integer(
        string="Semi-Live Interactions",
        default=0,
        readonly=True,
        copy=False,
    )
    non_live = fields.Integer(
        string="Non-Live Interactions",
        default=0,
        readonly=True,
        copy=False,
    )
