from odoo import models, fields


class AgentPresence(models.Model):
    _name = "agent_presence"
    _description = "Agent Presence"

    # agent_status_id = fields.Many2one(
    #   "agent.status", string="Agent Status", ondelete="cascade"
    # )
    category = fields.Char(string="Category")
    since = fields.Datetime(string="Presence Since")
    name = fields.Char(string="Presence Name")
    description = fields.Char(string="Description")
    eligible_for_routing = fields.Boolean(string="Eligible For Routing")
