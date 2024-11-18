from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This module describes all the property info about each estate sale"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False,
        default=(fields.Date.today() + relativedelta(months=3)),
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(
        readonly=True,
        copy=False,
        compute="compute_accepted_offer_details",
        store=True,
    )
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[
            ("north", "North"),
            ("east", "East"),
            ("south", "South"),
            ("west", "West"),
        ],
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("new", "New"),
            ("offer received", "Offer Received"),
            ("offer accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        required=True,
        copy=False,
        default="new",
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Buyer",
        copy=False,
        compute="compute_accepted_offer_details",
    )
    user_id = fields.Many2one(
        "res.users", string="Salesperson", default=lambda self: self.env.user
    )
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    # Chapter 8 Computed fields
    total_area = fields.Integer(
        compute="_compute_total_area", inverse="_inverse_total_area", readonly=True
    )

    best_price = fields.Float(compute="_compute_best_price")
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")

    # Chapter 10 validation
    _sql_constraints = [
        (
            "positive_expected_price",
            "CHECK(expected_price > 0)",
            "Expected price must be positive",
        ),
        (
            "positive_selling_price",
            "CHECK(selling_price >= 0)",
            "Selling price must be positive",
        ),
        (
            "unique_name",
            "UNIQUE(name)",
            "Property name must be unique",
        ),
    ]

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    # Best Price

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.mapped("offer_ids.price"), default=0)

    # Garden Onchange
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden is True:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = None

    # Ch 9 Cancel Button
    def cancel_property(self):
        for record in self:
            if record.state == "sold":
                raise UserError("Sold properties can not be canceled.")
            else:
                record.state = "cancelled"
        return True

    # Ch 9 Sold Button
    def sold_property(self):
        for record in self:
            if record.state == "cancelled":
                raise UserError("Canceled properties can not be sold.")
            else:
                record.state = "sold"
        return True

    # Ch 9 Set Buyer and Sold when Accepted
    def compute_accepted_offer_details(self):
        for record in self:
            self.check_selling_price_high_enough()
            accepted_offers = record.offer_ids.filtered(
                lambda o: o.status == "accepted"
            )

            if len(accepted_offers) > 1:
                # more than 1 offer accepted
                raise UserError("Only one offer can be accepted!")
            elif not len(accepted_offers):
                # no offers accepted
                record.partner_id = None
                record.selling_price = None
            else:
                # set the selling price to the one
                record.partner_id = accepted_offers[0].partner_id
                record.selling_price = accepted_offers[0].price
        return True

    # Ch 10 Check exception error
    @api.constrains("selling_price", "expected_price")
    def check_selling_price_high_enough(self):
        for record in self:
            # check if selling price is not 0
            if not float_is_zero(record.selling_price, precision_digits=2):
                # check if it is greater than 90% of selling price
                if (
                    float_compare(
                        record.selling_price,
                        0.9 * record.expected_price,
                        precision_digits=2,
                    )
                    == -1
                ):
                    raise ValidationError(
                        "Selling price must be at least 90 percent of expected price"
                    )
