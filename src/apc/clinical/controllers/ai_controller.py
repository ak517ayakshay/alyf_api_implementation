"""
APC AI Controllers

This module contains FastAPI route handlers for AI interaction endpoints.
It defines endpoints for asking questions to Alyf AI and managing conversation history.

Endpoints:
    GET /v1/ask_alyf/get_message_history: get_message_history_endpoint
    DELETE /v1/apc/ask_alyf/clear_message_history: clear_message_history
    GET /ask_alyf/get_message_history: ask_alyf_get_message_history
    GET /ask_alyf/clear_message_history: ask_alyf_clear_message_history
    GET /ask_alyf/get_full_response: ask_alyf_get_full_response
""" 