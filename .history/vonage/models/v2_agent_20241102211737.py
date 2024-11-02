from odoo import fields, models


class VCCAgent(models.Model):
    _name = "vcc.agent"
    _description = "VCC Agent. Tracks agent information and provides relationships to presence, workload, and interaction records"

    agent_id = fields.Char(string="Agent ID", required=True)
    name = fields.Char(string="Agent Name")
    presence_ids = fields.One2many(
        "vcc.presence",
        "agent_id",
        string="Presence Records",
    )
    workload_ids = fields.One2many(
        "vcc_workload",
        "agent_id",
        string="Workload Records",
    )
    interaction_ids = fields.One2many(
        "vcc.interaction",
        "agent_id",
        string="Interactions",
    )
