from odoo import models, fields


class AgentWorkload(models.Model):
    _name = "agent_workload"
    _description = "Agent Workload"

    # agent_status_id = fields.Many2one(
    #    "agent_status", string="Agent Status", ondelete="cascade"
    # )
    since = fields.Datetime(string="Workload Since")
    calls = fields.Integer(string="Calls", default=0)
    semi_live = fields.Integer(string="Semi-Live", default=0)
    non_live = fields.Integer(string="Non-Live", default=0)
