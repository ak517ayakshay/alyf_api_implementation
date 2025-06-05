"""
APC Report Controllers

This module contains FastAPI route handlers for report generation endpoints.
It defines endpoints for creating and retrieving various types of reports.

Endpoints:
    POST /reports/rpm/refresh_reports: reports_rpm_refresh_reports
    POST /reports/rpm/get_reports: reports_rpm_get_reports
    GET /reports/member_admin/refresh_reports: reports_member_admin_refresh_reports
    GET /reports/member_admin/get_reports: reports_member_admin_get_reports
    GET /reports/member_admin/get_html_report: reports_member_admin_get_reports
    POST /reports/billing/get_reports: reports_billing_get_reports
    POST /reports/member_data_analytics/get_reports: reports_member_analytics_get_reports
    POST /reports/provider_data_analytics/get_reports: reports_provider_analytics_get_reports
""" 