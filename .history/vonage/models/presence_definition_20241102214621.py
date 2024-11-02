from odoo import fields, models


class PresenceDefinition(models.Model):
    _name = "vcc.presence.definition"
    _description = "VCC Presence Definition"

    presence_id = fields.Char(
        string="Presence ID",
        required=True,
        help="A unique identifier for each presence status, often matching an ID from the external VCC system.",
    )
    name = fields.Char(
        string="Presence Name",
        required=True,
        help="The display name of the presence status such as Available or Logged Out",
    )
    description = fields.Char(
        string="Description",
        help="A descriptive field to provide additional information about the presence status",
    )
    selectable = fields.Boolean(string="Selectable", default=True)
    category = fields.Selection(
        [
            ("available", "Available"),
            ("away", "Away"),
            ("busy", "Busy"),
            ("logged_out", "Logged Out"),
            ("do_not_disturb", "Do Not Disturb"),
        ],
        string="Category",
        required=True,
    )