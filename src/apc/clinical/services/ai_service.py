"""
APC AI Services

This module contains business logic for AI interaction operations.
It handles asking questions to Alyf AI and managing conversation history.

Functions:
    get_message_history(provider_id, member_id)
    clear_message_history(provider_id, member_id)
    get_thread_id(provider_id, member_id)
    write_message_to_db(message_text, thread_id, ai_generated, message_log)
    get_full_response(provider_id, prompt, member_id, title, timestamp, boost_with_knowledgebase)
    invoke_sql_agent(prompt, provider_id, member_id, title, timestamp, boost_with_knowledgebase)
""" 