from odoo import fields, models


class AgentAvailability(models.Model):
    _name = "vonage.agent.availability"

    def call_agent_availability(self):

        region = "nam"
        skill_name = "Account Manager"
        url = f"https://{region}.api.cc.vonage.com/agents-availability?skillNames={skill_name}"
