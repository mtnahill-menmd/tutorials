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

    # Chapter 10 validation
    _sql_constraints = [
        (
            "positive_offer",
            "CHECK(price > 0)",
            "Offer must be positive",
        )
    ]

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

    # Chapter 9 Accept and Refuse Buttons
    def accept_offer(self):
        for record in self:
            record.status = "accepted"
        return True

    def refuse_offer(self):
        for record in self:
            record.status = "refused"
        return True
