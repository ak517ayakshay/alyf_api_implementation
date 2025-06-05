"""
APC Authentication Controllers

This module contains FastAPI route handlers for provider authentication endpoints.
It defines endpoints for login, 2FA validation, and password reset functionality.

Endpoints:
    POST /login: authenticate
    POST /login/validate_2fa: validate_2fa
    POST /login/resend_2fa: resend_2fa
    POST /forget_password: forget_password
""" 