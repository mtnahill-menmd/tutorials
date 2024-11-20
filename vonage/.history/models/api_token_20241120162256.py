from datetime import timedelta
from odoo import fields, models


class APIToken(models.Model):
    _name = "api.token"
    _description = "Vonage / Odoo API token management"

    token = fields.Text(string="Access Token", readonly=True)
    expiration = fields.Datetime(string="Expiration Time", readonly=True)

    def get_valid_token(self):
        """Retrieve a valid token or refresh it if expired"""
        print(f"MT TEST Call get_valid_token")
        token_record = self.search([], limit=1)
        if (
            token_record
            and token_record.expiration
            and token_record.expiration > fields.Datetime.now()
        ):
            return token_record
        return self.refresh_token()

    def refresh_token(self):
        """Generate and save new token"""
        print(f"MT TEST Call refresh_token")

        # env has all models and methods, search for the relevant one
        integration = self.env["vonage.auth.integration"]
        print(f"integration: {integration}")
        # TODO add this to the relevant model
        # search through vonage auth model and get the generate token method
        # token_data = integration.sudo().generate_vonage_token()
        token_data = integration.generate_vonage_token()
        print(f"token_data {token_data}")

        # check that the token data exists
        if token_data and "access_token" in token_data:
            # calculate the Datetime of the expiration
            expiration_time = fields.Datetime.now() + timedelta(
                seconds=token_data["expires_in"]
            )

            print(f"MT TEST Expiration Time: {expiration_time}")
            # search in this model whether the token exists
            token_record = self.search([], limit=1)
            # check whether it exists
            if token_record:
                token_record.write(
                    {"token": token_data["access_token"], "expiration": expiration_time}
                )
            else:
                self.create(
                    {"token": token_data["access_token"], "expiration": expiration_time}
                )
            return token_data["access_token"]
        return None

    def action_test_token(self):
        """Test if the token is valid and populate expiration."""
        print(f"MT TEST Call action_test_token")

        # Fetch the latest token and ensure it's valid
        token_record = self.get_valid_token()

        # If a valid token is found or refreshed, update the current record
        if token_record:
            self.write(
                {
                    "token": token_record.token,
                    "expiration": token_record.expiration,
                }
            )
            print(f"self.expiration after update: {self.expiration}")

            # Check if the token is still valid
            if (
                token_record.expiration
                and token_record.expiration > fields.Datetime.now()
            ):
                return {
                    "type": "ir.actions.client",
                    "tag": "display_notification",
                    "params": {
                        "title": "Token Active",
                        "message": f"The token is valid and active until {token_record.expiration}.",
                        "type": "success",
                        "sticky": False,
                    },
                }

        # If no valid token, display an error
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": "Token Expired",
                "message": "The token has expired or is missing. Please refresh it.",
                "type": "danger",
                "sticky": False,
            },
        }