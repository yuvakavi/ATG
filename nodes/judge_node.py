def judge_node(state: dict) -> dict:
    """Evaluate debate and determine winner based on argument quality."""
    turns = state["turns"]
    topic = state["topic"].lower()
    
    # Analyze arguments from both agents
    agentA_turns = [t for t in turns if t["agent"] == "AgentA"]
    agentB_turns = [t for t in turns if t["agent"] == "AgentB"]
    
    # Score based on multiple criteria
    scoreA = 0
    scoreB = 0
    
    # 1. Argument diversity and depth
    agentA_keywords = set()
    agentB_keywords = set()
    
    for turn in agentA_turns:
        text = turn["text"].lower()
        # Scientific keywords
        if any(word in text for word in ["evidence", "research", "data", "studies", "scientific", "empirical", "analysis"]):
            scoreA += 2
        # Extract unique concepts
        agentA_keywords.update(text.split())
    
    for turn in agentB_turns:
        text = turn["text"].lower()
        # Philosophical keywords
        if any(word in text for word in ["ethical", "moral", "philosophical", "values", "dignity", "justice", "wisdom"]):
            scoreB += 2
        # Extract unique concepts
        agentB_keywords.update(text.split())
    
    # 2. Vocabulary richness
    scoreA += min(len(agentA_keywords) // 10, 5)
    scoreB += min(len(agentB_keywords) // 10, 5)
    
    # 3. Relevance to topic
    topic_words = set(topic.split())
    for turn in agentA_turns:
        if any(word in turn["text"].lower() for word in topic_words):
            scoreA += 1
    
    for turn in agentB_turns:
        if any(word in turn["text"].lower() for word in topic_words):
            scoreB += 1
    
    # 4. Consistency (all agents participated equally)
    if len(agentA_turns) == len(agentB_turns):
        scoreA += 3
        scoreB += 3
    
    # 5. Topic-specific scoring (regulation/policy topics favor different approaches)
    regulation_terms = ["regulate", "regulation", "government", "approval", "legally", "law", "policy"]
    ethical_terms = ["ethical", "moral", "human", "dignity", "rights", "values", "society"]
    
    if any(term in topic for term in regulation_terms):
        # For regulation topics, balanced scientific + ethical arguments are stronger
        if scoreA > 0 and scoreB > 0:
            # Slight edge to philosopher for regulation questions
            scoreB += 2
    
    if any(term in topic for term in ethical_terms):
        # For ethical topics, philosophical arguments are stronger
        scoreB += 3
    
    # Determine winner
    if scoreA > scoreB:
        winner = "AgentA"
        margin = scoreA - scoreB
    elif scoreB > scoreA:
        winner = "AgentB"
        margin = scoreB - scoreA
    else:
        # Tie-breaker: last speaker advantage
        winner = turns[-1]["agent"]
        margin = 0
    
    # Generate summary
    summary = f"Debate on '{state['topic']}' covered {len(turns)} rounds with arguments from both scientific and philosophical perspectives."
    
    # Generate detailed justification
    if margin > 5:
        strength = "significantly stronger"
    elif margin > 2:
        strength = "stronger"
    else:
        strength = "slightly better"
    
    agent_name = "Scientist" if winner == "AgentA" else "Philosopher"
    
    justification = (
        f"{winner} ({agent_name}) provided {strength} arguments (Score: {scoreA if winner == 'AgentA' else scoreB} vs {scoreB if winner == 'AgentA' else scoreA}). "
        f"Their perspective offered more comprehensive coverage of the topic with "
        f"{'evidence-based reasoning and empirical analysis' if winner == 'AgentA' else 'ethical considerations and philosophical depth'}."
    )
    
    state["final_summary"] = summary
    state["winner"] = winner
    state["justification"] = justification
    state["scores"] = {"AgentA": scoreA, "AgentB": scoreB}
    
    return state

