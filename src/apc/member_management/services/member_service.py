"""
APC Member Management Services

This module contains business logic for member management operations.
It handles adding, updating, and managing members.

Functions:
    add_member(provider_id, name, email, phone_number, synthetic)
    update_member(member_id, update_data)
    get_member_by_criteria(provider_id, member_id, email, phone_number)
    member_admin_summary(provider_id, member_id)
    create_auth_link(provider_id, member_id, source_name)
    reset_auth(provider_id, member_id, source_name)
    zoom_user(provider_id, member_id)
    reset_member(provider_id, member_id)
    email_members(provider_id, member_ids, email_type, subject, body)
    delete_members(provider_id, member_ids)
    icd_code_assignment(provider_id, member_ids, assign_list, unassign_list)
""" 