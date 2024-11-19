import requests

from odoo import http, models, fields


class VonageIntegration(models.Model):
    _name = "vonage.auth.integration"

    token_response = fields.Char(string="Token Response")

    def get_vonage_token(self):
        # credentials - should live somewhere more secure
        client_id = "06489f4e-8530-4e93-80a4-5344f9ba1b07"
        client_secret = "x1pHeh5tMXg1feUonhwRTwMJ229s7vPpNJBahD1j"
        region = "nam"

        # Endpoint URL
        url = f"https://{region}.cc.vonage.com/Auth/connect/token"

        # Body parameters
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "users:read users:write stats interaction-content:read interactions:write agents-availability:read",
        }

        # Headers
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        # POST request
        response = requests.post(url, headers=headers, data=data)

        # Write to field
        self.token_response = response

        # Check response
        if response.status_code == 200:
            token_data = response.json()
            return token_data
        else:
            # Handle errors
            return {
                "error": response.text,
                "status_code": response.status_code,
            }
