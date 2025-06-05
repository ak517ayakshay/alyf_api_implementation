"""
APC Configuration Services

This module contains business logic for provider configuration operations.
It handles managing provider configuration and actions.

Functions:
    get_provider_config(provider_id)
    update_provider_config(provider_id, config)
    generate_self_signup_link(provider_record)
    get_meta_info(provider_id)
    provider_update_email(provider_id, magic_number, new_email)
    provider_send_email(provider_id, users, email_type, subject, body)
    provider_send_email_html(provider_id, subject, body, from_user, to_users, cc_users, bcc_users)
    provider_generate_brochure(provider_id)
    provider_generate_registration_url(provider_id, data_dict)
    provider_create_backfill_requests(provider_id, action_request)
""" 