"""
APC Dashboard Services

This module contains business logic for visualization and dashboard operations.
It handles creating and managing dashboards and panel configurations.

Functions:
    get_visualization_config(provider_id)
    validate_panel_config(provider_id, panel_config)
    get_member_dashboards(provider_id, member_id, start_time, end_time)
    get_panel_config_proposal(provider_id, specialities, vitals_of_interest, member_id, current_panel_config, additional_instructions)
    raw_llm_query(provider_id, prompt, member_id)
    generate_n_vitals_panel(member_id, vital_ids, start_time, end_time, vis_type)
    get_vitals_detail(provider_id, member_ids, vitals, start_time, end_time)
""" 