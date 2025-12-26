def agent_node(state: dict, agent_id: str, persona: str) -> dict:
    """Generate agent arguments based on persona and memory."""
    memory = state["agent_memory"]
    topic = memory["topic"]
    
    # Extract role from persona (e.g., "Scientist" or "Philosopher")
    role = persona.split('\n')[0].replace('You are a ', '').replace('.', '').strip()
    round_num = state["current_round"] + 1
    
    # Generate unique argument based on role, topic, and round
    if agent_id == "AgentA":
        # Scientist perspective
        perspectives = [
            f"From a scientific standpoint on '{topic}': We need empirical evidence and rigorous testing to ensure safety and efficacy.",
            f"Analyzing '{topic}' through data: Historical patterns show that premature adoption without proper validation leads to significant risks.",
            f"Research on '{topic}' indicates: Controlled studies and peer-reviewed findings must guide our policy decisions.",
            f"Evidence-based assessment of '{topic}': Statistical analysis reveals patterns that cannot be ignored in our approach.",
            f"Scientific consensus on '{topic}': Multiple independent studies converge on the need for systematic oversight.",
            f"Technical analysis of '{topic}': Risk-benefit calculations demonstrate the importance of measured implementation.",
            f"Data-driven perspective on '{topic}': Quantitative metrics show clear advantages of a cautious, methodical approach.",
            f"Empirical research on '{topic}': Longitudinal studies provide compelling evidence for structured governance."
        ]
    else:
        # Philosopher perspective
        perspectives = [
            f"Considering '{topic}' philosophically: We must examine the ethical implications and fundamental human values at stake.",
            f"Reflecting on '{topic}': Historical wisdom teaches us that human dignity and autonomy must be our guiding principles.",
            f"From an ethical standpoint on '{topic}': The question of what makes us human becomes central to this debate.",
            f"Philosophical analysis of '{topic}': We cannot separate technological advancement from moral responsibility.",
            f"Contemplating '{topic}': The long-term societal impact requires us to think beyond immediate gains.",
            f"Ethical framework for '{topic}': Justice, fairness, and equality must inform every decision we make.",
            f"Historical perspective on '{topic}': Past transformations remind us that progress without wisdom leads to unintended consequences.",
            f"Moral considerations on '{topic}': The intrinsic value of human agency demands careful deliberation."
        ]
    
    # Select argument based on round (cycling through perspectives)
    argument_index = (round_num - 1) % len(perspectives)
    argument = perspectives[argument_index]

    # Repetition check (should not occur with our design, but kept for safety)
    for t in state["turns"]:
        if argument.lower() == t["text"].lower():
            # Fallback to generic but unique argument
            argument = f"{role} presents perspective #{round_num} on '{topic}': {persona.split('.')[1].strip()}"
            break

    state["turns"].append({
        "round": state["current_round"] + 1,
        "agent": agent_id,
        "text": argument
    })

    state["current_round"] += 1
    state["next_agent"] = "AgentB" if agent_id == "AgentA" else "AgentA"

    return state

