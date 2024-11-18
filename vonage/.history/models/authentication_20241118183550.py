import requests

from odoo import http, models, fields


class VonageIntegration(models.Model):
    _name = "vonage.integration"

    def get_vonage_token(self):
        # credentials - should live somewhere more secure
        client_id = "06489f4e-8530-4e93-80a4-5344f9ba1b07"
        client_secret = "x1pHeh5tMXg1feUonhwRTwMJ229s7vPpNJBahD1j"
        region = "nam"
