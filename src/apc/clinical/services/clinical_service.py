"""
APC Clinical Services

This module contains business logic for clinical assessment operations.
It handles retrieving and processing clinical data.

Functions:
    get_clinical_assessments_ros_and_risk(provider_id, member_id, time_range, ros_scores, quality_scores)
    get_scores(member_id, ros_scores, quality_scores, start_time, end_time)
    get_clinical_assessments_daily_rounds(provider_id, assessment_range, verbose)
    get_vital_observations_timeseries(provider_id, vital_observations_request)
    get_vital_observations_aggregations(provider_id, vital_aggregations_request)
    get_schema(provider_id)
    secure_query(provider_id, table, query, limit, offset)
    get_daily_recording_report(provider_id, member_id, start_date, end_date)
""" 