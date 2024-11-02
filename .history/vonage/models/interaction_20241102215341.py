from odoo import models, fields


class Interaction(models.Model):
    _name = "vcc.interaction"
    _description = "VCC Interaction. Logs details about each interaction, such as start/end time, type and status"

    agent_id = fields.Many2one(
        "vcc.agent",
        string="Agent",
        ondelete="cascade",
    )
    interaction_id = fields.Char(string="Interaction ID")
    type = fields.Selection(
        [
            ("call", "Call"),
            ("chat", "Chat"),
        ],
        string="Interaction Type",
    )
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    duration = fields.duration(
        string="Duration",
        help="Duration in seconds",
    )
    status = fields.Selection(
        [
            ("completed", "Completed"),
            ("ongoing", "Ongoing"),
            ("missed", "Missed"),
        ],
        string="Status",
    )
    channel = fields.Char(string="Channel")
    reason = fields.Char(string="Reason")
