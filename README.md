 Market Pulse – Multi-Agent Market Intelligence System
Project for the Agent Development Kit Hackathon with Google Cloud

🌐 Live Demo
https://market-pulse-api-872651677730.us-central1.run.app

📂 GitHub Repository
https://github.com/lopsidedjudgement/market-pulse

🧠 What It Does
Market Pulse is an autonomous multi-agent system that collects, analyzes, and reports real-time market activity using Python and Google Cloud services. Each agent performs a specialized task, working together to provide intelligent business insights without manual effort.

🤖 Agents Overview
🔍 ScraperAgent
Gathers live data from public APIs (e.g., pricing, product trends).

📊 AnalyzerAgent
Applies sentiment analysis and identifies anomalies in market behavior.

🧠 BigQueryAgent
Pulls historical data from BigQuery to compare and forecast trends.

📝 ReporterAgent
Summarizes daily insights into visualized reports.

📣 NotifierAgent
Sends real-time alerts via Slack or email when thresholds are breached.

🛠️ Technologies Used
Python 3.13

Google Cloud Run

Google BigQuery

Flask REST API

NLP + Sentiment Analysis

GitHub + GitHub Actions

🧱 Architecture Diagram

![small](https://github.com/user-attachments/assets/18b5d80d-002a-44d1-ac1f-072ec533dd6e)


▶️ How to Run Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/lopsidedjudgement/market-pulse.git
cd market-pulse
Set environment variables:

bash
Copy
Edit
export GOOGLE_APPLICATION_CREDENTIALS="path/to/market-pulse-key.json"
export GCP_PROJECT_ID="market-pulse-quickdeploy"
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run each agent:

bash
Copy
Edit
python agents/ScraperAgent/agent.py
python agents/AnalyzerAgent/agent.py
python agents/BigQueryAgent/agent.py
python agents/ReporterAgent/agent.py
python agents/NotifierAgent/agent.py
🌍 Hosted API Endpoint
A public-facing REST API hosted on Google Cloud Run:
GET https://market-pulse-api-872651677730.us-central1.run.app
