"""
Member Vitals Controllers

This module contains FastAPI route handlers for member vitals endpoints.
It defines endpoints for setting and retrieving vitals data.

Endpoints:
    POST /v1/member/set_vitals: set_member_vitals
    GET /v1/member/get_vitals: get_member_vitals
    POST /v1/member/{member_id}/set_vitals: set_vitals_v2
    GET /external_events/get_events: external_events_get_events
    POST /external_events/create_events: external_events_create_events
    GET /external_events/create_event_from_plain_description: external_events_create_event_from_plain_description
    GET /member/annotations/get: get_annotations
    POST /member/annotations/add: add_annotation
    POST /member/annotations/docs_for_smartplots: docs_for_smartplots
""" 