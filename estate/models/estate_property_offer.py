from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate_property.offer"
    _description = "property offers"

    name = fields.Char(required=True)
    price = fields.Float()
    status = fields.Selection(
        [("accepted", "Accepted"), ("refused", "Refused")], copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate_property", required=True)
