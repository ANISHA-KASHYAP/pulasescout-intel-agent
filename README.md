# PulseScout — Autonomous Multi-Agent Market & Competitor Intelligence Platform

PulseScout is an autonomous market and competitor intelligence platform engineered using Fetch.ai uAgents framework, Agentverse, and Streamlit. It deploys decentralized sub-agents that sweep tech ecosystems (GitHub, ArXiv, HackerNews) to aggregate, synthesize, and deliver real-time competitive insights.

---

## Key Features

- Autonomous Multi-Agent Architecture: Specialized sub-agents operating via communication protocols on the Fetch.ai uAgents ecosystem.
- Agentverse Hosted Integration: Live agent registration on the Fetch.ai Almanac registry for discovery and message routing.
- Real-Time Data Synthesis: Queries tech domain repositories, research papers, and discussions simultaneously.
- Minimalist Control Dashboard: Interactive Streamlit interface featuring active agent toggles and streaming protocol execution logs.

---

## Tech Stack

- Agent Infrastructure: Fetch.ai uAgents Framework, Agentverse Hosted Agent & Almanac Registry
- Asynchronous Networking: Python asyncio, httpx
- Frontend Dashboard: Streamlit
- Version Control: Git, GitHub

---

## System Architecture

+-----------------------+
| Streamlit UI / User   |
+-----------------------+
            |
            v
+-----------------------+
| PulseScout Gateway    |
+-----------------------+
            |
  +---------+---------+---------+
  |                   |         |
  v                   v         v
+--------------+ +----------+ +------------------+
| GitHub Scout | | ArXiv    | | HackerNews       |
| uAgent       | | Scholar  | | Tracker uAgent   |
+--------------+ +----------+ +------------------+
      |               |                 |
      v               v                 v
GitHub API      ArXiv API         HackerNews API

---

## Project Structure

PulseScout/
+-- app.py              # Streamlit dashboard application
+-- agent.py            # Agentverse hosted uAgent protocol & logic
+-- requirements.txt    # Python dependencies
+-- README.md           # Project documentation

---

## Getting Started

### 1. Prerequisites

Python 3.10+ and Git installed on your local environment.

### 2. Installation

Clone the repository and install required packages:

git clone https://github.com/ANISHA-KASHYAP/pulasescout-intel-agent.git
cd pulasescout-intel-agent
pip install -r requirements.txt

### 3. Running the Dashboard

Launch the Streamlit web application:

streamlit run app.py

Access the local interface at http://localhost:8501.

---

## Agentverse Deployment

The underlying intelligence agent (agent.py) is deployed on Agentverse and registered on the Almanac Service.

Testing in Agentverse:
1. Open the Agentverse Build tab.
2. Select agent.py and verify active protocol registration.
3. Query via the Chat with Agent interface (e.g., multi-agent systems or fastapi).

---

## License

Distributed under the MIT License.
