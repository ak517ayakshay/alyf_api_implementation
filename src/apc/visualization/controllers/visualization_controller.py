"""
APC Visualization Controllers

This module contains FastAPI route handlers for visualization endpoints.
It defines endpoints for managing dashboards and panel configurations.

Endpoints:
    GET /adaptive_visualization/get_current_config: adaptive_visualization_get_config
    POST /adaptive_visualization/validate_panel_config: adaptive_visualization_validate_panel_config
    GET /adaptive_visualization/member_dashboards: adaptive_visualization_member_dashboards
    POST /adaptive_visualization/get_panel_config_proposal: adaptive_visualization_get_panel_config_proposal
    GET /adaptive_visualization/get_panel_config_proposal: adaptive_visualization_get_panel_config_proposal
    GET /adaptive_visualization/raw_llm_query: adaptive_visualization_raw_llm_query
    POST /generate_n_vitals_panel_url: generate_n_vitals_panel_url
    POST /get_vitals: get_vitals_detail
""" 