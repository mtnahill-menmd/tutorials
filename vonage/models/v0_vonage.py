from odoo import fields, models


class Vonage(models.Model):
    _name = "vonage"
    _description = "This module integrates Vonage and Odoo"

    recording_end = fields.Datetime(
        readonly=True,
        copy=False,
        help="The time when the call recording ended",
    )
    recording_start = fields.Datetime(
        readonly=True,
        copy=False,
        help="The time when the call recording started",
    )
    recording_url = fields.Html(
        readonly=True,
        copy=False,
        help="The web link where the call recording can be accessed",
    )
    recording_uuid = fields.Char(
        readonly=True,
        copy=False,
        help="A unique identifier for the specific call recording",
    )
    conversation_uuid = fields.Char(
        readonly=True,
        copy=False,
        help="A unique identifier for the entire call conversation",
    )
    direction = fields.Selection(
        selection=[("received", "Received"), ("outbound", "Outbound")],
        readonly=True,
        copy=False,
        help="Indicates if the call was inbound (received) or outbound (made)",
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
        ],
        readonly=True,
        copy=False,
        help="Shows the current status of the call (started, ringing, answered, machine, completed, busy, cancelled, failed, rejected, timeout, unanswered )",
    )
    uuid = fields.Char(
        readonly=True,
        copy=False,
        help="Unique identifier for a specific call session",
    )
    call_type = fields.Selection(
        selection=[
            ("phone", "Phone"),
            ("app", "App"),
        ],
        readonly=True,
        copy=False,
        help="The type of call (e.g. phone, app)",
    )
    recording_url = fields.Html(
        readonly=True,
        copy=False,
        help="Call recording triggered and stored by Vonage",
    )
    duration = fields.Integer(
        readonly=True,
        copy=False,
        help="The total duration of the call",
    )
    total_state_time = fields.Float(
        readonly=True,
        copy=False,
        help="Total time the agent spent in various states (e.g. on hold, talking)",
    )
    number_of_logins = fields.Integer(
        readonly=True,
        copy=False,
        help="Tracks how many times the agent logged into the system",
    )
    number_of_logouts = fields.Integer(
        readonly=True,
        copy=False,
        help="Tracks how many times the agent logged out of the system",
    )
    first_activity_date_time = fields.Datetime(
        readonly=True,
        copy=False,
        help="The timestamp when the first activity of the call occurred",
    )
    ready_time = fields.Datetime(
        readonly=True,
        copy=False,
        help="The time when the agent was ready to take another call",
    )
    hold_time = fields.Float(
        readonly=True,
        copy=False,
        help="The amount of time the call was placed on hold",
    )
    inbound_call_count = fields.Integer(
        readonly=True,
        copy=False,
        help="The number of inbound calls received by the agent",
    )
    inbound_call_time = fields.Datetime(
        readonly=True,
        copy=False,
        help="The timestamp of when an inbound call was received",
    )
    outbound_call_count = fields.Integer(
        readonly=True,
        copy=False,
        help="The number of outbound calls made by the agent",
    )
    wrap_time = fields.Float(
        readonly=True,
        copy=False,
        help="The time spent by the agent after the call to finish up or wrap up",
    )
    utc_call_date = fields.Datetime(
        readonly=True,
        copy=False,
        help="The timestamp of the call in UTC (Coordinated Universal Time)",
    )
    away_time = fields.Float(
        readonly=True,
        copy=False,
        help="The amount of time the agent was away during the call",
    )
    line_busy_time = fields.Float(
        readonly=True,
        copy=False,
        help="Tracks the amount of time the line was busy during the call",
    )
    state_list = fields.Char(
        readonly=True,
        copy=False,
        help="A list of the various states (e.g. on call, idle) during the call session",
    )
    ready_for_outbound_time = fields.Char(
        readonly=True,
        copy=False,
        help="The amount of time the agent was ready for the next outbound call",
    )
    fault_time = fields.Float(
        readonly=True,
        copy=False,
        help="Tracks the amount of time a fault or error occurred during the call",
    )
    last_activity_time = fields.Datetime(
        readonly=True,
        copy=False,
        help="The timestamp of the last recorded activity during the call",
    )
    longest_state_time = fields.Float(
        readonly=True,
        copy=False,
        help="The longest time the agent spent in a particular state (e.g. on hold)",
    )
    agent_selected_count = fields.Integer(
        readonly=True,
        copy=False,
        help="Tracks how many times an agent was selected to take a call",
    )
    away_count = fields.Integer(
        readonly=True,
        copy=False,
        help="The number of times an agent was marked as away during a session",
    )
    hold_count = fields.Integer(
        readonly=True,
        copy=False,
        help="Tracks how many times the call was put on hold",
    )
    outbound_transfer_count = fields.Integer(
        readonly=True,
        copy=False,
        help="The number of times the call was transferred outbound",
    )
    vonage_wrap_count = fields.Integer(
        readonly=True,
        copy=False,
        help="The number of times the agent wrapped up after a call",
    )
    hangup_url = fields.Html(
        readonly=True,
        copy=False,
        help="Custom endpoint in Odoo to handle hang-up events",
    )
    answer_url = fields.Html(
        readonly=True,
        copy=False,
        help="Custom URL in Odoo to handle call answers",
    )
    event_url = fields.Html(
        readonly=True,
        copy=False,
        help="Custom URL in Odoo to handle call events and statuses",
    )
    # did not include "connect" or "talk" fields
    phone_number_to = fields.Char(
        required=True,
        help="The phone number of the customer or lead receiving the call",
    )
    phone_number_from = fields.Char(
        required=True,
        default="8572335837",
        help="The phone number of the agent making the call",
    )
    agent_id = fields.Char(
        help="The unique ID for the agent handling the call",
    )
    agent_name = fields.Char(
        help="The name of the agent handling the call",
    )
    agent_summary_owner_name = fields.Char(
        help="The name of the agent who owns the call summary",
    )
    call_timeout = fields.Float(
        help="The maximum time allowed before a call times out",
    )
    api_key = fields.Char(
        help="Authentication key used to connect Odoo with Vonage",
    )
    api_secret = fields.Char(
        help="Authentication secret key used for security between Odoo and Vonage",
    )
    application_id = fields.Char(
        help="Unique identifier for the Vonage application",
    )
    private_key = fields.Char(
        help="Private security key used for Vonage and Odoo integration",
    )
    region = fields.Char(help="Region of call, nam for North America")
