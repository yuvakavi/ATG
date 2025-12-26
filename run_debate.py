import yaml
import json
from datetime import datetime

from nodes.user_input_node import user_input_node
from nodes.coordinator_node import coordinator_node
from nodes.memory_node import memory_node
from nodes.agent_node import agent_node
from nodes.judge_node import judge_node

# Load config
config = yaml.safe_load(open("config.yaml"))

# Initial state
state = {
    "topic": input("Enter topic for debate: "),
    "current_round": 0,
    "next_agent": "AgentA",
    "turns": [],
    "config": config,
    "done": False
}

# Load personas
personaA = open(config["agents"]["AgentA"]["persona_file"]).read()
personaB = open(config["agents"]["AgentB"]["persona_file"]).read()

# Run debate
state = user_input_node(state)

print("\n" + "="*80)
print("DEBATE IN PROGRESS")
print("="*80 + "\n")

while not state["done"]:
    state = coordinator_node(state)
    if state.get("done"):
        break

    state = memory_node(state)

    if state["next_agent"] == "AgentA":
        state = agent_node(state, "AgentA", personaA)
        # Get the latest turn that was just added
        latest_turn = state["turns"][-1]
        agent_name = config["agents"]["AgentA"]["name"]
        print(f"[Round {latest_turn['round']}]")
        print(f"Speaker: {agent_name}")
        print(f"Argument:")
        print(f"{latest_turn['text']}")
        print()  # Blank line between rounds
    else:
        state = agent_node(state, "AgentB", personaB)
        # Get the latest turn that was just added
        latest_turn = state["turns"][-1]
        agent_name = config["agents"]["AgentB"]["name"]
        print(f"[Round {latest_turn['round']}]")
        print(f"Speaker: {agent_name}")
        print(f"Argument:")
        print(f"{latest_turn['text']}")
        print()  # Blank line between rounds

# Judge
state = judge_node(state)

print("\n" + "="*80)
print("JUDGE DECISION")
print("="*80)

print("\nSummary:")
print(f"  {state['final_summary']}")

print("\nScores:")
print(f"  AgentA (Scientist): {state['scores']['AgentA']}")
print(f"  AgentB (Philosopher): {state['scores']['AgentB']}")

print("\nWinner:")
print(f"  {state['winner']} ({config['agents'][state['winner']]['name']})")

print("\nJustification:")
print(f"  {state['justification']}")

print("\n" + "="*80)

# Logging - prepare enhanced log with agent names
log_data = {
    "topic": state["topic"],
    "total_rounds": state["current_round"],
    "max_rounds": config["max_rounds"],
    "turns": [
        {
            "round": turn["round"],
            "agent": turn["agent"],
            "agent_name": config["agents"][turn["agent"]]["name"],
            "text": turn["text"]
        }
        for turn in state["turns"]
    ],
    "judge": {
        "summary": state["final_summary"],
        "winner": state["winner"],
        "winner_name": config["agents"][state["winner"]]["name"],
        "justification": state["justification"],
        "scores": state["scores"]
    },
    "timestamp": datetime.now().isoformat()
}

log_file = config["logging"]["log_path"]
with open(log_file, "w") as f:
    json.dump(log_data, f, indent=2)

print(f"\nDebate log saved to {log_file}")
