# AI GitHub Repository Auditor (CrewAI + MCP)

An **agentic AI system** that analyzes GitHub repositories using multiple collaborative AI agents. The system automatically reviews code, checks security issues, improves documentation, and generates GitHub issues.

This project uses **multi-agent orchestration with CrewAI and tool-based interaction via Model Context Protocol**.

The AI agents run using **LLMs served through Groq**.

---

# Project Overview

This system acts like an **AI software engineering assistant** for GitHub repositories.

Given a repository URL, the system:

* Analyzes the repository structure
* Reviews source code quality
* Detects potential security issues
* Improves documentation
* Automatically generates GitHub issues

Multiple AI agents collaborate to complete the workflow.

---

# Key Features

• Multi-agent AI system
• Autonomous repository analysis
• Automated code review
• Security vulnerability detection
• Documentation improvement
• GitHub issue generation
• Modular architecture for adding new agents

---

# System Architecture

```
User
 │
 ▼
CLI / API Interface
 │
 ▼
CrewAI Orchestrator
 │
 ├── Repository Analyzer Agent
 ├── Code Review Agent
 ├── Security Agent
 ├── Documentation Agent
 └── Issue Generator Agent
 │
 ▼
MCP Tool Layer
 │
 ▼
GitHub MCP Server
 │
 ▼
GitHub API
 │
 ▼
Target Repository
```

Agents collaborate through **CrewAI**, while tools interact with GitHub via MCP.

---

# Project Structure

```
crewai-github-agent
│
├── agents/          # AI agents
├── tasks/           # Agent tasks
├── tools/           # MCP tool integrations
├── crew/            # CrewAI configuration
├── workflows/       # Workflow pipelines
├── config/          # LLM and system config
├── utils/           # Helper utilities
├── tests/           # Unit tests
│
├── main.py          # Entry point
├── requirements.txt
├── .env
└── README.md
```

---

# Agents

### Repository Analyzer Agent

Analyzes repository structure, languages, and project organization.

### Code Review Agent

Reviews source code for best practices and potential improvements.

### Security Agent

Detects potential vulnerabilities or unsafe coding patterns.

### Documentation Agent

Improves README and generates documentation.

### Issue Generator Agent

Creates GitHub issues for identified problems.

---

# Tech Stack

Backend:

* Python
* CrewAI
* LangChain

LLM Provider:

* Groq

Tools & APIs:

* Model Context Protocol
* GitHub API

Optional Interface:

* FastAPI

---

# Installation

Clone the repository

```bash
git clone https://github.com/sarthakPatil96K/crewai-github-agent.git
cd crewai-github-agent
```

Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
MCP_SERVER_URL=http://localhost:3000
```

---

# Running the Project

Run the main script:

```
python main.py
```

Example input:

```
Enter GitHub repository URL:
https://github.com/example/project
```

Output:

* Repository analysis
* Code review report
* Security findings
* Documentation suggestions
* Generated GitHub issues

---

# Example Workflow

1. User enters repository URL
2. CrewAI orchestrator launches agents
3. Agents analyze repository collaboratively
4. MCP tools interact with GitHub
5. Results and issues are generated automatically

---

# Future Improvements

* Pull request generation
* Code refactoring suggestions
* CI/CD integration
* Web dashboard
* Multi-repository analysis

---

# Use Cases

• Automated code auditing
• AI developer assistants
• Software engineering analytics
• DevOps automation
• AI-powered code review systems

---

# Value

This project demonstrates:

* Multi-agent AI system design
* LLM tool integration
* GitHub automation
* AI workflow orchestration
* Applied generative AI engineering
