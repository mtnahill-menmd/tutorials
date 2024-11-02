from odoo import models, fields  # type: ignore


class PresenceCategory(models.Model):
    _name = "presence_category"
    _description = "Presence Category"

    category_type = fields.Char(string="Category")
    description = fields.Char(string="Description")
    sub_category = fields.Char(string="Subcategory")
    # MTN 11/2/24 How to debug this?
    # presence_definition_ids = fields.One2many(
    #    "presence_definition", "category_id", string="Presence Definitions"
    # )
