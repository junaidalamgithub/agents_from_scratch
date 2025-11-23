# AI Agents from Scratch with Google Gemini (and other LLMs)

A lightweight, educational implementation of **tool-using AI Agents** built from scratch in Python. No LangChain, no LlamaIndex — just pure, readable code to understand how modern AI agents work under the hood.

This project demonstrates:
- How to build a ReAct-style agent (Reasoning + Acting)
- How to enable LLMs to call external tools
- How to support multiple LLM backends (currently Google Gemini, easily extensible)
- Tool calling with structured JSON output enforcement
- Uses **uv** as the fast Python package manager

Perfect for learning, prototyping, or as a minimal base for production agents.

## Features

- Two example tools:
  - `get_weather(location: str)` → fetches real-time weather using a free API
  - `calculate_sum(expression: str)` → safely evaluates mathematical expressions (e.g., "2 + 3 * (4 - 1)")
- Supports **Google Gemini** out of the box (`gemini-1.5-flash`, `gemini-1.5-pro`, etc.)
- Easy to swap in other LLMs (OpenAI, Anthropic, Groq, etc.) by modifying `agent.py`
- Clean separation of concerns: prompts, tools, and agent logic
- Uses **uv** for blazing-fast dependency management

## Project Structure
.
├── README.md
├── uv.lock
├── pyproject.toml
├── agent.py          # Core Agent class with ReAct loop
├── tools.py          # get_weather() and calculate_sum() tools
├── prompts.py        # System prompt and ReAct instruction templates
└── .env              # Your API keys (not tracked)


## Quick Start

### 1. Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

### 2. Clone and set up

```bash
git clone https://github.com/yourusername/ai-agents-from-scratch.git
cd ai-agents-from-scratch

# Install dependencies with uv
uv sync
```
### 3. Set up environment variables
create a .env file in your local workspace and set the following 2 API Keys:
```
GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
WEATHER_API_KEY=<YOUR_WEATHER_API_KEY>
```

### 4. Run the Agent

```bash
uv run main.py
```
### License
MIT License — feel free to use, modify, and learn from this code.