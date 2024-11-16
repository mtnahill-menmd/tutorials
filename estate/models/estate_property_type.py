from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate_property.type"
    _description = "All property types"

    name = fields.Char(required=True)
