import requests

from odoo import http, models, fields


class VonageIntegration(models.Model):
    _name = "vonage.integration"

    def get_vonage_token(self):
        client_id = "06489f4e-8530-4e93-80a4-5344f9ba1b07"
