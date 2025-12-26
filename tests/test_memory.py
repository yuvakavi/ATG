from nodes.memory_node import memory_node


def test_memory_created():
    """Test memory node creation."""
    state = {
        "topic": "AI regulation",
        "turns": [{"agent": "AgentA", "text": "Test"}]
    }
    state = memory_node(state)
    assert "agent_memory" in state

