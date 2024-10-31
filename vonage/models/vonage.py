from odoo import fields, models


class Vonage(models.Model):
    _name = "vonage"
    _description = "This module integrates vonage and Odoo"

    recording_end = fields.Datetime()
    recording_start = fields.Datetime()
    recording_url = fields.Html()
    recording_uuid = fields.Char()
    conversation_uuid = fields.Char()
    direction = fields.Selection(
        selection=[("received", "Received"), ("outbound", "Outbound")]
    )
    status = fields.Selection(
        selection=[
            ("started", "Started"),
            ("ringing", "Ringing"),
            ("answered", "Answered"),
            ("machine", "Machine"),
            ("completed", "Completed"),
            ("busy", "Busy"),
            ("cancelled", "Cancelled"),
            ("failed", "Failed"),
            ("rejected", "Rejected"),
            ("timeout", "Timeout"),
            ("unanswered", "Unanswered"),
        ]
    )
    uuid = fields.Char()
    call_type = fields.Selection(
        selection=[
            ("phone", "Phone"),
            ("app", "App"),
        ]
    )
    recording_url = fields.Html()
    duration = fields.Integer()
    total_state_time = fields.Float()
    number_of_logins = fields.Integer()
    number_of_logouts = fields.Integer()
    first_activity_date_time = fields.Datetime()
    ready_time = fields.Datetime()
    hold_time = fields.Float()
    inbound_call_count = fields.Integer()
    inbound_call_time = fields.Datetime()
    outbound_call_count = fields.Integer()
    wrap_time = fields.Float()
    utc_call_date = fields.Datetime()
    away_time = fields.Float()
    line_busy_time = fields.Float()
    state_list = fields.Char()
    ready_for_outbound_time = fields.Char()
    fault_time = fields.Float()
    last_activity_time = fields.Datetime()
    longest_state_time = fields.Float()
    agent_selected_count = fields.Integer()
    away_count = fields.Integer()
    hold_count = fields.Integer()
    outbound_transfer_count = fields.Integer()
    vonage_wrap_count = fields.Integer()
    hangup_url = fields.Html()
    answer_url = fields.Html()
    event_url = fields.Html()
    # did not include "connect" or "talk" fields
    phone_number_to = fields.Char()
    phone_number_from = fields.Char()
    agent_id = fields.Char()
    agent_name = fields.Char()
    agent_summary_owner_name = fields.Char()
    call_timeout = fields.Float()
    api_key = fields.Char()
    api_secret = fields.Char()
    application_id = fields.Char()
    private_key = fields.Char()
    region = fields.Char()
