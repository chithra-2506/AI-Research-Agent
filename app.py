from flask import Flask, render_template, request, jsonify
from agent.research_agent import ResearchAgent
import os

app = Flask(__name__)
agent = ResearchAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/research', methods=['POST'])
def research():
    data  = request.get_json()
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'error': 'Please enter a research query'}), 400
    api_key = data.get('api_key', '').strip()
    if not api_key:
        return jsonify({'error': 'Please enter your Gemini API key'}), 400
    result = agent.run(query, api_key)
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 AI Research Agent running at http://localhost:5000")
    app.run(debug=True, port=5000)
