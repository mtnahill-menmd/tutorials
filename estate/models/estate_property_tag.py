from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tags for type of property such as house, condo"

    name = fields.Char(required=True)

    _sql_constraints = [
        (
            "unique_name",
            "UNIQUE(name)",
            "property tag must be unique",
        )
    ]
