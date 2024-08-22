import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the Gemini API key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Check if the API key is loaded
if not GEMINI_API_KEY:
    raise ValueError("API key for Gemini is not set in the environment variables.")

# Set the API endpoint for Gemini
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

def search_articles(query):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{"parts": [{"text": query}]}]
    }

    try:
        response = requests.post(f"{API_ENDPOINT}?key={GEMINI_API_KEY}", json=data, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching articles: {str(e)}")

    results = response.json()
    
    # Debugging: Print the raw response
    print(f"Raw API response: {results}")

    articles = []

    # Extract content directly from the API response
    for item in results.get('candidates', []):
        article_content = item.get('content', {}).get('parts', [{}])[0].get('text', '')
        articles.append({"content": article_content})

    return articles

def fetch_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching content from {url}: {str(e)}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    content = ' '.join([p.get_text() for p in soup.find_all(['h1', 'h2', 'h3', 'p'])])
    return content.strip()

def concatenate_content(articles):
    full_text = ' '.join(article.get('content', '') for article in articles)
    return full_text

def generate_answer(content, query):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{"parts": [{"text": f"Based on the following content, answer the query: {query}\n\nContent: {content}"}]}]
    }

    try:
        response = requests.post(f"{API_ENDPOINT}?key={GEMINI_API_KEY}", json=data, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error generating answer: {str(e)}")

    results = response.json()

    # Extract the answer from the response
    if 'candidates' in results and len(results['candidates']) > 0:
        return results['candidates'][0].get('content', {}).get('parts', [{}])[0].get('text', '').strip()
    else:
        return "No answer generated."