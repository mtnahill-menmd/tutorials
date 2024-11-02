from odoo import fields, models


class AgentAvailability(models.Model):
    _name = "agent_availability"

    logged_out = fields.Integer(readonly=True, copy=False)
    away = fields.Integer(readonly=True, copy=False)
    extended_away = fields.Integer(readonly=True, copy=False)
    ready = fields.Integer(readonly=True, copy=False)
