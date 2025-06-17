from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Market Pulse API is running."})

def run_agent(name):
    try:
        result = subprocess.run(["python", f"agents/{name}/agent.py"], capture_output=True, text=True)
        return {"status": "done", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "error": str(e)}

@app.route("/run-<agent>", methods=["POST"])
def run_agent_endpoint(agent):
    agent_map = {
        "scraper": "ScraperAgent",
        "bigquery": "BigQueryAgent",
        "analyzer": "AnalyzerAgent",
        "reporter": "ReporterAgent",
        "notifier": "NotifierAgent"
    }
    if agent not in agent_map:
        return jsonify({"error": "Invalid agent name"}), 400
    return jsonify(run_agent(agent_map[agent]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
