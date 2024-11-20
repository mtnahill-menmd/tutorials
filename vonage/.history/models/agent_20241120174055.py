import requests
from odoo import fields, models


class VCCAgent(models.Model):
    _name = "vcc.agent"
    _description = "VCC Agent. Tracks agent information and provides relationships to presence, workload, and interaction records"

    agent_id = fields.Char(
        string="Agent ID",
        # required=True,
        readonly=True,
        copy=False,
    )
    name = fields.Char(
        string="Agent Name",
        readonly=True,
        copy=False,
    )
    presence_ids = fields.One2many(
        "vcc.presence",
        "agent_id",
        string="Presence Records",
        readonly=True,
        copy=False,
    )
    workload_ids = fields.One2many(
        "vcc.workload",
        "agent_id",
        string="Workload Records",
        readonly=True,
        copy=False,
    )
    interaction_ids = fields.One2many(
        "vcc.interaction",
        "agent_id",
        string="Interactions",
        readonly=True,
        copy=False,
    )

    def query_agent(self):
        region = "nam"
        url = f"https://{region}.api.cc.vonage.com/useradmin/users?include=All"

        # get valid token
        token = self.env["api.token"].sudo().get_valid_token()

        print(f"inside query_agent")
        print(f"token {token}")
        if not token:
            raise ValueError("No valid token available. Please refresh token.")

        # prep headers for query
        headers = {"Authorization": f"Bearer {token}"}

        # Make get request
        response = requests.get(url, headers=headers)
        print(f"MT TEST agent_response {response}")

        if response.status_code == 200:
            print(f"inside 200 status code")
            print(f"respose.json {response.json()}")
            users = response.json()

            # users = response.json().get("users", [])
            print(f"users {users}")
            self.parse_users(users)  # process and store users
        else:
            raise ValueError(
                f"Failed to fetch agents: {response.status_code} - {response.text}"
            )

        # data = {}

    def parse_users(self, users):
        """Parse and store user data in vcc.agent"""
        print(f"inside parse_users")

        for user in users:
            print(f"users {users}")
            print(f"user {user}")
            agent_id = user.get("userId")
            name = user.get("name")
            print(f"name {name}")
            email = user.get("email")

            # check if the agent exists
            agent_record = self.search([("agent_id", "=", agent_id)], limit=1)
            if agent_record:
                # update the agent record
                agent_record.write({"name": name})
            else:
                # create a new agent record
                self.create(
                    {
                        "agent_id": agent_id,
                        "name": name,
                    }
                )

        # {
        #     "userId": "21bf9827-190e-4865-b1a5-f84b6d12533c",
        #     "lastLoginTime": "2024-11-16T14:11:52Z",
        #     "username": "adaly@menmd.com",
        #     "active": true,
        #     "name": "Adrian Daly",
        #     "email": "adaly@menmd.com",
        #     "ssoExternalId": "8149",
        #     "locked": false,
        #     "userAccountConfiguration": {
        #         "role": "Agent",
        #         "chargeable": true,
        #         "actAsAgent": true,
        #         "agentConfiguration": {
        #             "agentDisplayId": "8149",
        #             "webrtc": true,
        #             "agentControlWebrtc": true,
        #             "handleMultipleInteractions": false,
        #             "enforcedDispositionCodes": true,
        #             "nativeCallLogging": false,
        #             "srStartRecOnAlerting": false,
        #             "callParking": false,
        #             "salesCadence": false,
        #             "outboundAutoanswer": false,
        #             "inboundAutoanswer": false,
        #             "video": false,
        #             "transcribeCallsRealTime": false,
        #             "callRecordingControls": false,
        #             "location": "US",
        #             "telephonyAddress": {
        #                 "telephoneAddress": "8572335837",
        #                 "outboundTelephonyRegion": "be969939-22cd-a9d2-eb66-90dbafb506d6",
        #                 "nationalDisplay": true,
        #                 "virtualLocation": "US",
        #                 "preventAutoCallbackNumber": true,
        #                 "selectedCallbackNumberId": "",
        #             },
        #             "capacity": {
        #                 "isAgentLevel": false,
        #                 "live": 100,
        #                 "nonLive": 100,
        #                 "semiLive": 100,
        #             },
        #             "associatedUsers": [],
        #         },
        #     },
        # },
