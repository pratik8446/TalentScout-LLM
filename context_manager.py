def handle_context(conversation_history):
    """
    Manage the conversation context based on the history.
    """
    if not conversation_history:
        # If there's no conversation history, initialize with gathering details
        return {"stage": "gathering_details"}
    
    last_interaction = conversation_history[-1]
    user_input = last_interaction["user"].lower()
    
    # Determine context stage based on user input
    if "tech stack" in user_input:
        return {"stage": "tech_stack"}
    elif "position" in user_input or "experience" in user_input:
        return {"stage": "gathering_details"}
    elif "exit" in user_input:
        return {"stage": "end_conversation"}
    else:
        return {"stage": "general_conversation"}

def update_context(conversation_history, new_stage):
    """
    Update the conversation context stage.
    """
    if conversation_history:
        conversation_history[-1]["context"] = new_stage
