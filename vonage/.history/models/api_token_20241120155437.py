from datetime import timedelta
from odoo import fields, models


class APIToken(models.Model):
    _name = "api.token"
    _description = "Vonage / Odoo API token management"

    token = fields.Text(string="Access Token", readonly=True)
    expiration = fields.Datetime(string="Expiration Time", readonly=True)

    def get_valid_token(self):
        """Retrieve a valid token or refresh it if expired"""
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
        # TODO add this to the relevant model
        # search through vonage auth model and get the generate token method
        token_data = integration.sudo().generate_vonage_token()

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
        """Test if token is valid"""
        print(f"MT TEST Call action_test_token")
        if self.expiration and self.expiration > fields.Datetime.now():
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": "Token Active",
                    "message": "The token is valid and active",
                    "type": "success",
                    "sticky": False,
                },
            }
        else:
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": "Token Active",
                    "message": "The token is valid and active",
                    "type": "danger",
                    "sticky": False,
                },
            }
