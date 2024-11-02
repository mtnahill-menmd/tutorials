from odoo import fields, models


class VCCAgent(models.Model):
    _name = "vcc.agent"
    _description = "VCC Agent. Tracks agent information and provides relationships to presence, workload, and interaction records"

    agent_id = fields.Char(
        string="Agent ID",
        required=True,
        readonly=True,
        copy=False,
    )
    name = fields.Char(
        string="Agent Name",
        readonly=True,
        copy=False,
    )
    presence_ids = fields.One2many(
        "vcc.presence",
        "agent_id",
        string="Presence Records",
        readonly=True,
    )
    workload_ids = fields.One2many(
        "vcc.workload",
        "agent_id",
        string="Workload Records",
        readonly=True,
    )
    interaction_ids = fields.One2many(
        "vcc.interaction",
        "agent_id",
        string="Interactions",
        readonly=True,
    )
