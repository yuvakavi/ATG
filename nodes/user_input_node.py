def user_input_node(state: dict) -> dict:
    """Process and validate user input for debate topic."""
    topic = state.get("topic", "").strip()

    if len(topic) < 10:
        raise ValueError("Debate topic must be at least 10 characters")

    state["topic"] = topic
    return state

