import requests

from odoo import models, fields


class VonageIntegration(models.Model):
    _name = "vonage.auth.integration"
    _description = "Vonage Authentication Integration"

    token_response = fields.Char(string="Token Response")

    def generate_vonage_token(self):
        """Generate a new token for Vonage"""
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
        # self.token_response = response

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

    def call_vonage_api(self, endpoint, payload):
        """Make an authenticated call to a Vonage API endpoint"""
        token = self.env["api_token"].sudo().get_valid_token().token
        if not token:
            return {"error": "No valid token available"}
        url = f"https://api.vonage.com/{endpoint}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text, "status_code": response.status_code}
