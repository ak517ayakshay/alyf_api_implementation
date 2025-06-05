"""
APC Configuration Controllers

This module contains FastAPI route handlers for provider configuration endpoints.
It defines endpoints for managing provider configuration and actions.

Endpoints:
    POST /actions/provider: apc_actions_provider
    POST /v2/actions/provider: v2_apc_actions_provider
    POST /v1/apc/provider/config_update: provider_config_update
    GET /meta_info: get_meta_info
    GET /provider/generate_signup_link: generate_signup_link
""" 