"""
APC Authentication Services

This module contains business logic for provider authentication operations.
It handles authentication, 2FA validation, and password reset functionality.

Functions:
    authenticate_provider(username, password)
    validate_2fa_login(pid, otp)
    resend_2fa_token(pid)
    send_password_reset_email(username)
""" 