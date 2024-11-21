from datetime import datetime
import requests
from odoo import fields, models
from odoo.fields import Datetime


class VCCAgent(models.Model):
    _name = "vcc.agent"
    _description = "VCC Agent. Tracks agent information and provides relationships to presence, workload, and interaction records"

    username = fields.Char(
        string="Username",
        # required=True,
        readonly=True,
        copy=False,
    )
    name = fields.Char(
        string="Agent Name",
        readonly=True,
        copy=False,
    )
    email = fields.Char(
        string="Agent Email",
        readonly=True,
        copy=False,
    )
    last_login_time = fields.Datetime(
        string="Last Login Time",
        readonly=True,
        copy=False,
    )
    sso_external_id = fields.Char(
        string="sso ID",
        readonly=True,
        copy=False,
    )
    chargeable = fields.Boolean(
        string="chargeable",
        readonly=True,
        copy=False,
    )
    role = fields.Char(
        string="role",
        readonly=True,
        copy=False,
    )
    presence_ids = fields.One2many(
        "vcc.presence",
        "username",
        string="Presence Records",
        readonly=True,
        copy=False,
    )
    workload_ids = fields.One2many(
        "vcc.workload",
        "username",
        string="Workload Records",
        readonly=True,
        copy=False,
    )
    interaction_ids = fields.One2many(
        "vcc.interaction",
        "username",
        string="Interactions",
        readonly=True,
        copy=False,
    )

    def query_agent(self):
        region = "nam"
        url = f"https://{region}.api.cc.vonage.com/useradmin/users?include=All"

        # get valid token
        token_record = self.env["api.token"].sudo().get_valid_token_record()
        token = token_record.token
        if not token:
            raise ValueError("No valid token available. Please refresh token.")

        # prep headers for query
        headers = {"Authorization": f"Bearer {token}"}

        # Make get request
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            users = response.json()

            self.parse_users(users)  # process and store users
        else:
            raise ValueError(
                f"Failed to fetch agents: {response.status_code} - {response.text}"
            )

        # Reload the tree view
        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }

    def parse_users(self, users):
        """Parse and store user data in vcc.agent"""

        for user in users:
            username = user.get("username")
            name = user.get("name", "Unknown Name")
            email = user.get("email", "No Email Provided")
            sso_external_id = user.get("ssoExternalId")
            chargeable = user.get("chargeable")

            last_login_time_iso = user.get("userLastLogin")
            parsed_date = datetime.strptime(last_login_time_iso, "%Y-%m-%dT%H:%M:%SZ")
            last_login_time = Datetime.to_string(parsed_date)

            # Skip if username is missing
            if not username:
                continue

            # Search for an existing agent
            agent_record = self.env["vcc.agent"].search(
                [("username", "=", username)], limit=1
            )

            updated_agent_record = {
                "username": username,
                "name": name,
                "email": email,
                "last_login_time": last_login_time,
                "sso_external_id": sso_external_id,
                "chargeable": chargeable,
            }

            if agent_record:
                agent_record.write(updated_agent_record)
            else:
                self.env["vcc.agent"].create(updated_agent_record)
