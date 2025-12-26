from nodes.judge_node import judge_node


def test_judge_output():
    """Test judge node output."""
    state = {
        "topic": "AI regulation",
        "turns": [
            {"agent": "AgentA", "text": "Scientific evidence shows risks"},
            {"agent": "AgentB", "text": "Ethical considerations matter"}
        ]
    }
    state = judge_node(state)
    assert "winner" in state
    assert "justification" in state
    assert "scores" in state
    assert "final_summary" in state

