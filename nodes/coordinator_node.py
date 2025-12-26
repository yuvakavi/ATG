def coordinator_node(state: dict) -> dict:
    """Coordinate debate flow and validate turn order."""
    max_rounds = state["config"]["max_rounds"]

    if state["current_round"] >= max_rounds:
        state["done"] = True
        return state

    expected_agent = "AgentA" if state["current_round"] % 2 == 0 else "AgentB"

    if state["next_agent"] != expected_agent:
        raise RuntimeError("Out-of-turn agent execution detected")

    return state

