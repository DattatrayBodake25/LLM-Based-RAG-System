from flask import Flask, request, jsonify
# import utils
import os
# from utils import search_articles, concatenate_content, generate_answer
from . import utils
from .utils import search_articles, concatenate_content, generate_answer


app = Flask(__name__)

# Default route for checking if the API is running
@app.route('/', methods=['GET'])
def index():
    return "Flask API is running! Use POST /query to interact."

# Main route for handling queries
@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer.
    """
    # Extract the query from the request
    data = request.json
    user_query = data.get('query')
    if not user_query:
        return jsonify({"error": "Query not provided"}), 400

    # Debugging: Print the user query
    print(f"Received query: {user_query}")

    # Step 1: Search and scrape articles based on the query
    try:
        articles = search_articles(user_query)
        # Debugging: Print the articles found
        print(f"Articles found: {articles}")
    except Exception as e:
        print(f"Error searching articles: {str(e)}")
        return jsonify({"error": f"Error searching articles: {str(e)}"}), 500

    # Step 2: Concatenate content from the scraped articles
    concatenated_content = concatenate_content(articles)
    # Debugging: Print the concatenated content
    print(f"Concatenated content: {concatenated_content}")

    # Step 3: Generate an answer using the LLM
    try:
        generated_answer = generate_answer(concatenated_content, user_query)
        # Debugging: Print the generated answer
        print(f"Generated answer: {generated_answer}")
    except Exception as e:
        print(f"Error generating answer: {str(e)}")
        return jsonify({"error": f"Error generating answer: {str(e)}"}), 500

    # Return the jsonified text back to Streamlit
    return jsonify({"response": generated_answer})

if __name__ == '__main__':
    app.run(host='localhost', port=5001)