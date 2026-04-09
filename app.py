from flask import Flask, request, jsonify
from crowd_simulator import get_crowd_data
from assistant import suggest_path

app = Flask(__name__)

@app.route("/")
def home():
    return "CrowdFlow AI is running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")

    crowd_data = get_crowd_data()
    response = suggest_path(query, crowd_data)

    return jsonify({
        "query": query,
        "response": response,
        "crowd_data": crowd_data
    })

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)