import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import openai
from jira import JIRA

# Load environment variables
load_dotenv()

# Set up OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set up Jira API
jira_options = {"server": "https://caddiscap.atlassian.net"}
jira = JIRA(options=jira_options, basic_auth=(os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"]))

app = Flask(__name__)

# Your existing routes and logic
@app.route("/")
def index():
    return render_template("index.html")

from flask import request

@app.route("/api/query", methods=["POST"])
def process_query():
    data = request.json
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Empty query"}), 400

    # Interact with ChatGPT API
    chatgpt_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=query,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )

    chatgpt_answer = chatgpt_response.choices[0].text.strip()

    # Parse the ChatGPT answer and interact with Jira API
    # Depending on the answer, create new stories, subtasks, or update existing stories
    # You may need to implement custom logic to parse the answer and perform actions in Jira

    response_data = {
        "chatgpt_answer": chatgpt_answer,
        # Add any other relevant data from Jira interactions
    }

    return jsonify(response_data)
