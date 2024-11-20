# -*- coding: utf-8 -*-

{
    "name": "vonage",
    "depends": [
        "base",
    ],
    "application": True,
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "views/api_token_view.xml" "views/auth_integration_view.xml",
        "views/vonage_stats_views.xml",
        "views/vonage_menus.xml",
    ],
}
