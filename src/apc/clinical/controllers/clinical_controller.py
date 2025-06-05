"""
APC Clinical Controllers

This module contains FastAPI route handlers for clinical assessment endpoints.
It defines endpoints for retrieving and managing clinical assessments.

Endpoints:
    GET /get_clinical_assessments/ros_and_risk: apc_get_clinical_assessments_ros_and_risk
    GET /get_scores: apc_get_scores
    POST /get_clinical_assessments/daily_rounds: apc_get_clinical_assessments_daily_rounds
    POST /vital_observations_timeseries: api_vital_observations_timeseries
    POST /vital_observations_aggregations: api_vital_observations_aggregations
    GET /apc/get_schema: get_schema
    GET /apc/secure_query: secure_query
    GET /member/get_daily_recording_report: apc_api_member_get_daily_recording_report
""" 