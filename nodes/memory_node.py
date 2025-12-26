def memory_node(state: dict) -> dict:
    """Manage debate memory and context."""
    turns = state["turns"]
    recent = turns[-2:] if len(turns) >= 2 else turns

    state["agent_memory"] = {
        "topic": state["topic"],
        "recent_turns": recent
    }
    return state

