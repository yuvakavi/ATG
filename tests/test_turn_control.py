import pytest
from nodes.coordinator_node import coordinator_node


def test_turn_violation():
    """Test turn violation detection."""
    state = {
        "current_round": 1,
        "next_agent": "AgentA",
        "config": {"max_rounds": 8}
    }
    with pytest.raises(RuntimeError):
        coordinator_node(state)

