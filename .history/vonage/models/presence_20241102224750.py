from odoo import models, fields


class Presence(models.Model):
    _name = "vcc.presence"
    _description = "VCC Presence. Captures the presence status details for an agent"

    agent_id = fields.Many2one(
        "vcc.agent",
        string="Agent",
        ondelete="cascade",
        readonly=True,
        copy=False,
    )
    presence_id = fields.Char(
        string="Presence ID",
        readonly=True,
        copy=False,
    )
    name = fields.Char(
        string="Presence Name",
        readonly=True,
        copy=False,
    )
    description = fields.Char(
        string="Description",
        readonly=True,
    )
    since = fields.Datetime(
        string="Presence Since",
        readonly=True,
    )
    eligible_for_routing = fields.Boolean(
        string="Eligible for Routing",
        readonly=True,
    )
