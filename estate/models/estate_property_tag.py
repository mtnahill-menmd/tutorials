from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate_property.tag"
    _description = "Tags for type of property such as house, condo"

    name = fields.Char(required=True)
    property = fields.Many2many("estate_property")
