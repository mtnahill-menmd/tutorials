from odoo import http

class VonageController(odoo.http.Controller):
    @route('/example_url', auth='public')