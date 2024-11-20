from datetime import timedelta
from odoo import fields, models


class APIToken(models.Model):
    _name = "api.token"
    _description = "Vonage / Odoo API token management"

    token = fields.Text(string="Access Token", readonly=True)
    expiration = fields.Datetime(string="Expiration Time", readonly=True)

    def get_valid_token_record(self):
        """Retrieve a valid token or refresh it if expired"""
        print(f"inside get_valid_token_record")
        token_record = self.search([], limit=1)
        print(f"token_record {token_record}")
        if (
            token_record
            and token_record.expiration
            and token_record.expiration > fields.Datetime.now()
        ):
            # token = token_record.token
            return token_record
        return self.refresh_token()

    def refresh_token(self):
        """Generate and save new token"""

        # env has all models and methods, search for the relevant one
        integration = self.env["vonage.auth.integration"]
        # TODO add this to the relevant model
        # search through vonage auth model and get the generate token method
        # token_data = integration.sudo().generate_vonage_token()
        token_record = integration.generate_vonage_token()

        # check that the token data exists
        if token_record and "access_token" in token_record:
            # calculate the Datetime of the expiration
            expiration_time = fields.Datetime.now() + timedelta(
                seconds=token_record["expires_in"]
            )

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
            return token_data
        return None

    def action_test_token(self):
        """Test if the token is valid and populate expiration."""

        # Fetch the latest token and ensure it's valid
        token_record = self.get_valid_token_record()

        # If a valid token is found or refreshed, update the current record
        if token_record:
            self.write(
                {
                    "token": token_record.token,
                    "expiration": token_record.expiration,
                }
            )

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
