from odoo import fields, models


class PresenceDefinition(models.Model):
    _name = "vcc.presence.definition"
    _description = "VCC Presence Definition"

    presence_id = fields.Char(
        string="Presence ID",
        required=True,
        help="A unique identifier for each presence status, often matching an ID from the external VCC system.",
        readonly=True,
        copy=False,
    )
    name = fields.Char(
        string="Presence Name",
        required=True,
        help="The display name of the presence status such as Available or Logged Out",
        readonly=True,
        copy=False,
    )
    description = fields.Char(
        string="Description",
        help="A descriptive field to provide additional information about the presence status",
        readonly=True,
        copy=False,
    )
    selectable = fields.Boolean(
        string="Selectable",
        default=True,
        help="A boolean indicating whether agents can select this status manually. For example, some statuses may be system-controlled.",
        readonly=True,
        copy=False,
    )
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
        help="The category of the presence status, which helps group statuses into categories like Available, Away or Busy. This is useful for filtering and categorizing presence types.",
        readonly=True,
    )
