from odoo import models, fields


class AgentStatus(models.Model):
    _name = "agent_status"
    _description = "Agent Status"

    agent_id = fields.Char(
        string="Agent ID", required=True, help="The unique ID of the agent"
    )
    # presence_id = fields.Many2one(
    #    "agent_presence", string="Presence", ondelete="cascade"
    # )
    # workload_id = fields.Many2one(
    #    "agent_workload", string="Workload", ondelete="cascade"
    # )
    type = fields.Selection(
        [
            ("Workload", "Workload"),
            ("Presence", "Presence"),
        ],
        string="Type",
        required=True,
    )
    category = fields.Char(string="Category")
    name = fields.Char(string="Name")
    eligible_for_routing = fields.Boolean(string="Eligible for Routing")
    start = fields.Datetime(string="Start Time", help="start time of the status change")
    duration = fields.Integer(
        string="Duration", help="Duration in seconds or milliseconds"
    )
    status = fields.Char(string="Status")
    reason = fields.Char(string="Reason")
    interaction = fields.Char(string="Interaction")
    channel = fields.Char(string="Channel")

    # presence_id = fields.Many2one(
    #    "agent_presence", string="presence", ondelete="cascade"
    # )
    # workload_id = fields.Many2one(
    #    "agent_workload", string="Workload", ondelete="cascade"
    # )


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
