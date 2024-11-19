import requests
from odoo import fields, models


class VCCAgent(models.Model):
    _name = "vcc.agent"
    _description = "VCC Agent. Tracks agent information and provides relationships to presence, workload, and interaction records"

    agent_id = fields.Char(
        string="Agent ID",
        required=True,
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
        url = "https://{region}.api.cc.vonage.com/useradmin/users?include=All"

        data = {

        }

        headers = {"Authorization": "Bearer" {token}}

    def parse_users(self):
        {
            "userId": "21bf9827-190e-4865-b1a5-f84b6d12533c",
            "lastLoginTime": "2024-11-16T14:11:52Z",
            "username": "adaly@menmd.com",
            "active": true,
            "name": "Adrian Daly",
            "email": "adaly@menmd.com",
            "ssoExternalId": "8149",
            "locked": false,
            "userAccountConfiguration": {
                "role": "Agent",
                "chargeable": true,
                "actAsAgent": true,
                "agentConfiguration": {
                    "agentDisplayId": "8149",
                    "webrtc": true,
                    "agentControlWebrtc": true,
                    "handleMultipleInteractions": false,
                    "enforcedDispositionCodes": true,
                    "nativeCallLogging": false,
                    "srStartRecOnAlerting": false,
                    "callParking": false,
                    "salesCadence": false,
                    "outboundAutoanswer": false,
                    "inboundAutoanswer": false,
                    "video": false,
                    "transcribeCallsRealTime": false,
                    "callRecordingControls": false,
                    "location": "US",
                    "telephonyAddress": {
                        "telephoneAddress": "8572335837",
                        "outboundTelephonyRegion": "be969939-22cd-a9d2-eb66-90dbafb506d6",
                        "nationalDisplay": true,
                        "virtualLocation": "US",
                        "preventAutoCallbackNumber": true,
                        "selectedCallbackNumberId": "",
                    },
                    "capacity": {
                        "isAgentLevel": false,
                        "live": 100,
                        "nonLive": 100,
                        "semiLive": 100,
                    },
                    "associatedUsers": [],
                },
            },
        },
