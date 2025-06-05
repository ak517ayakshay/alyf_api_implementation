"""
Member Communication Services

This module contains business logic for member communication operations.
It handles OTP verification and notification management.

Functions:
    send_otp(member_id, phone_number, is_new_member)
    verify_otp(member_id, otp)
    get_notifications(member_id)
    mark_notifications_read(member_id, notification_ids)
""" 