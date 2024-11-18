import requests
from odoo import http, models, fields


class VonageController(http.Controller):

    @http.route("/get_vonage_data", type="http", auth="public")
    def get_vonage_data(self):
        token_data = (
            http.request.env["vonage.auth.integration"].sudo().get_vonage_token()
        )
        if "error" in token_data:
            return token_data["error"]
