"""
APC Report Services

This module contains business logic for report generation operations.
It handles creating and retrieving various types of reports.

Functions:
    refresh_rpm_reports(provider_id, member_ids, time_range)
    get_rpm_reports(provider_id, member_ids, time_range)
    refresh_member_admin_reports(provider_id, member_ids, include_data_analytics)
    get_member_admin_reports(provider_id, member_ids)
    get_member_admin_html_report(member_ids)
    get_billing_reports(provider_id, member_ids, time_range)
    get_member_analytics_reports(provider_id, member_ids, time_range)
    get_provider_analytics_reports(provider_id, time_range)
""" 