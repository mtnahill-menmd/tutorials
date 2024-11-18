import requests
from odoo import http, models, fields


class VonageController(http.Controller):
    @route("/example_url", auth="public")
    def handler(self):
        return example()
