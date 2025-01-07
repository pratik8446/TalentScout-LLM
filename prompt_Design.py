
def generate_prompt(user_input, context):
    """
    Create a structured prompt for the LLM.
    """
    if context.get("stage") == "gathering_details":
        return f"Create a question to gather details about {user_input}."
    elif context.get("stage") == "tech_stack":
        return f"Generate 3 technical interview questions for someone proficient in {user_input}."
    else:
        return f"Continue the conversation based on this input: {user_input}"
