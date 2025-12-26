from langgraph.graph import StateGraph
from typing import TypedDict


class DebateState(TypedDict):
    """State for the debate workflow."""
    topic: str
    current_round: int
    next_agent: str
    turns: list
    done: bool


def generate():
    """Generate debate DAG visualization."""
    graph = StateGraph(DebateState)
    
    # Add nodes
    graph.add_node("UserInput", lambda x: x)
    graph.add_node("Coordinator", lambda x: x)
    graph.add_node("Memory", lambda x: x)
    graph.add_node("AgentA", lambda x: x)
    graph.add_node("AgentB", lambda x: x)
    graph.add_node("Judge", lambda x: x)

    # Set entry point
    graph.set_entry_point("UserInput")
    
    # Add edges
    graph.add_edge("UserInput", "Coordinator")
    graph.add_edge("Coordinator", "Memory")
    graph.add_edge("Memory", "AgentA")
    graph.add_edge("AgentA", "AgentB")
    graph.add_edge("AgentB", "Judge")
    graph.set_finish_point("Judge")
    
    # Compile and visualize
    compiled = graph.compile()
    
    try:
        # Try to generate visualization using mermaid
        png_data = compiled.get_graph().draw_mermaid_png()
        with open("dag/debate_dag.png", "wb") as f:
            f.write(png_data)
        print("DAG visualization saved to dag/debate_dag.png")
    except Exception as e:
        print(f"Could not generate PNG visualization: {e}")
        print("DAG structure created successfully (visualization requires graphviz)")
        # Print mermaid text representation as fallback
        try:
            mermaid_text = compiled.get_graph().draw_mermaid()
            print("\nMermaid diagram representation:")
            print(mermaid_text)
        except:
            pass


if __name__ == "__main__":
    generate()
