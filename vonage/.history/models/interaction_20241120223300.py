from odoo import models, fields


class Interaction(models.Model):
    _name = "vcc.interaction"
    _description = "VCC Interaction. Logs details about each interaction, such as start/end time, type and status"

    username = fields.Many2one(
        "vcc.agent",
        string="Agent",
        ondelete="cascade",
        readonly=True,
        copy=False,
    )
    interaction_id = fields.Char(string="Interaction ID", readonly=True)
    type = fields.Selection(
        [
            ("call", "Call"),
            ("chat", "Chat"),
        ],
        string="Interaction Type",
        readonly=True,
        copy=False,
    )
    start_time = fields.Datetime(
        string="Start Time",
        readonly=True,
        copy=False,
    )
    end_time = fields.Datetime(
        string="End Time",
        readonly=True,
        copy=False,
    )
    duration = fields.Integer(
        string="Duration",
        help="Duration in seconds",
        readonly=True,
        copy=False,
    )
    status = fields.Selection(
        [
            ("completed", "Completed"),
            ("ongoing", "Ongoing"),
            ("missed", "Missed"),
        ],
        string="Status",
        readonly=True,
        copy=False,
    )
    channel = fields.Char(
        string="Channel",
        readonly=True,
        copy=False,
    )
    reason = fields.Char(
        string="Reason",
        readonly=True,
        copy=False,
    )