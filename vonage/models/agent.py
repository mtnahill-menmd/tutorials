from odoo import models, fields


class Agent(models.Model):
    _name = "agent"
    _description = "Agent"

    agent_id = fields.Char(
        string="Agent ID",
        required=True,
        help="Unique identifier for the agent",
    )
    name = fields.Char(string="Agent Name")

    # presence_id = fields.Many2one(
    #    'agent.presence, string="Presence", ondelete="cascade"'
    # )
    # workload_id = fields.Many2one(
    #    "agent.workload", string="Workload", ondelete="cascade"
    # )
