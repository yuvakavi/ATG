# 🎭 ATG Multi-Agent Debate System

A sophisticated multi-agent debate framework that orchestrates intelligent conversations between AI agents with different personas and expertise.

## ✨ Features

- 🤖 **Multiple Agent Personas** - Philosophers, Scientists, and custom personas
- 🎯 **Coordinator Node** - Manages debate flow and turn-taking
- ⚖️ **Judge Node** - Evaluates arguments and determines winners
- 🧠 **Memory Node** - Maintains conversation history and context
- 📊 **DAG Generation** - Creates directed acyclic graphs for debate visualization
- 📝 **Comprehensive Logging** - Tracks all debate interactions

## 🏗️ Architecture

```
atg-multi-agent-debate/
├── 📁 nodes/              # Core agent implementations
│   ├── agent_node.py      # Base agent functionality
│   ├── coordinator_node.py # Debate orchestration
│   ├── judge_node.py      # Argument evaluation
│   ├── memory_node.py     # Context management
│   └── user_input_node.py # User interaction
├── 📁 personas/           # Agent personality definitions
│   ├── philosopher.txt    # Philosophical perspective
│   └── scientist.txt      # Scientific perspective
├── 📁 dag/                # Graph generation
├── 📁 tests/              # Unit tests
├── 📁 logs/               # Debate logs
├── 📁 sample_outputs/     # Example outputs
├── config.yaml            # Configuration settings
├── run_debate.py          # Main entry point
└── requirements.txt       # Dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd atg-multi-agent-debate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure settings**
Edit `config.yaml` to customize debate parameters

### 🎮 Usage

Run a debate session:
```bash
python run_debate.py
```

Generate debate visualization:
```bash
python dag/generate_dag.py
```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

Run specific tests:
```bash
python -m pytest tests/test_judge.py
python -m pytest tests/test_memory.py
python -m pytest tests/test_turn_control.py
```

## 📋 Configuration

Edit `config.yaml` to customize:
- 🎭 Agent personas and roles
- ⏱️ Debate duration and turn limits
- 🎯 Judging criteria
- 📊 Logging preferences
- 🧠 Memory management settings

## 🎯 Node Types

### 🤖 Agent Node
Represents individual debate participants with unique perspectives

### 🎪 Coordinator Node
Manages debate flow, turn-taking, and ensures fair participation

### ⚖️ Judge Node
Evaluates arguments based on:
- Logic and reasoning
- Evidence quality
- Persuasiveness
- Coherence

### 🧠 Memory Node
Maintains:
- Conversation history
- Context awareness
- Cross-reference tracking

### 👤 User Input Node
Handles human interaction and input during debates

## 📊 Output

Debate logs are saved in JSON format with:
- 💬 Complete conversation transcript
- ⏰ Timestamps
- 🏆 Evaluation scores
- 📈 Performance metrics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

Built with passion for advancing multi-agent AI systems and intelligent debate.

---

Made with ❤️ by the ATG Team
