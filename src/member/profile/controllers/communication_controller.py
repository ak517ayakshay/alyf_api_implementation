"""
Member Communication Controllers

This module contains FastAPI route handlers for member communication endpoints.
It defines endpoints for OTP verification and notification management.

Endpoints:
    POST /v1/member/send_otp: send_otp
    POST /v1/member/verify_otp: verify_otp
    GET /v1/member/notifications: get_notifications
    POST /v1/member/notifications/mark_read: mark_notifications_read
""" 