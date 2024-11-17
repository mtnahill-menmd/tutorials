from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "property offers"

    price = fields.Float()
    status = fields.Selection(
        [("accepted", "Accepted"), ("refused", "Refused")],
        copy=False,
        string="Status",
    )
    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        string="Partner",
    )
    property_id = fields.Many2one(
        "estate.property",
        required=True,
        string="Property",
    )
    date_deadline = fields.Date(
        compute="_compute_validity_deadline",
        inverse="_inverse_compute_validity_deadline",
        string="Deadline",
    )
    validity = fields.Integer(
        default=7,
        string="Validity (days)",
    )

    @api.depends("validity")
    def _compute_validity_deadline(self):
        for record in self:
            origin_date = record.create_date or fields.Date.today()
            record.date_deadline = origin_date + relativedelta(days=record.validity)

    def _inverse_compute_validity_deadline(self):
        for record in self:
            create_datetime = record.create_date
            create_date = create_datetime.date()
            origin_date = create_date or fields.Date.today()
            datetime_difference = record.date_deadline - origin_date
            record.validity = datetime_difference.days
