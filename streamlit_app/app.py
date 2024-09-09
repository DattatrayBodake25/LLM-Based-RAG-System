import streamlit as st
import requests

# Set the URL for the Flask API (replace with your API endpoint)
FLASK_API_URL = "https://your-flask-api-url.onrender.com/query"

# Initialize session state
if "show_main" not in st.session_state:
    st.session_state.show_main = False

def show_main():
    st.session_state.show_main = True

# Display the welcome screen if show_main is False
if not st.session_state.show_main:
    st.markdown(
        """
        <style>
        .welcome {{
            text-align: center;
            padding: 50px;
        }}
        .welcome h1 {{
            font-size: 3em;
            color: #ffffff;
        }}
        .welcome p {{
            font-size: 1.5em;
            color: #e0e0e0;
        }}
        .button {{
            display: block;
            width: 200px;
            margin: 30px auto;
            padding: 10px;
            background-color: #0056b3;
            color: white;
            text-align: center;
            font-size: 1.2em;
            border-radius: 5px;
            cursor: pointer;
        }}
        .button:hover {{
            background-color: #004494;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="welcome">
            <h1>Welcome to My AI-Powered System</h1>
            <p>Your AI assistant for quick and insightful information retrieval.</p>
            <div class="button" onclick="window.location.href = 'http://localhost:8501/?show_main=true';">Let's Start</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Show main content if show_main is True
if st.session_state.show_main:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(to right, rgba(0,0,0,0.6), rgba(0,0,0,0.6));
            color: white;
            font-family: 'Roboto', sans-serif;
        }}
        .chatbox {{
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 20px;
            margin: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }}
        .user-message {{
            color: #0056b3;
            font-weight: bold;
        }}
        .bot-message {{
            color: #333333;
            font-weight: normal;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state to store chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Input for user query
    query = st.text_input("Enter your query:")

    if st.button("Send"):
        if query:
            try:
                response = requests.post(FLASK_API_URL, json={"query": query})
                if response.status_code == 200:
                    answer = response.json().get('response', "No answer received.")
                    st.session_state.history.append({"query": query, "response": answer})
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.RequestException as e:
                st.error(f"Request failed: {e}")

    # Display the chat history
    for chat in reversed(st.session_state.history):
        st.markdown(f"<div class='chatbox user-message'>You: {chat['query']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chatbox bot-message'>Bot: {chat['response']}</div>", unsafe_allow_html=True)




# import streamlit as st
# import requests

# # Set the URL for the Flask API (with the /query endpoint)
# FLASK_API_URL = "https://llm-based-rag-system.onrender.com/query"

# # Load the CSS style
# st.markdown(
#     f"""
#     <style>

#     /* Background Gradient */
#     .stApp {{
#         background: linear-gradient(to right, rgba(0,0,0,0.6), rgba(0,0,0,0.6));
#         color: white;
#         font-family: 'Roboto', sans-serif;
#     }}

#     /* Welcome message styling */
#     .welcome {{
#         text-align: center;
#         padding: 50px;
#     }}
#     .welcome h1 {{
#         font-size: 3em;
#         color: #ffffff;
#     }}
#     .welcome p {{
#         font-size: 1.5em;
#         color: #e0e0e0;
#     }}
#     .welcome p.smaller {{
#         font-size: 1.2em;
#         color: #b0b0b0;
#     }}

#     /* Chatbox styling */
#     .chatbox {{
#         background-color: rgba(255, 255, 255, 0.8);
#         border-radius: 15px;
#         padding: 20px;
#         margin: 20px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#     }}
#     .user-message {{
#         color: #0056b3;
#         font-weight: bold;
#     }}
#     .bot-message {{
#         color: #333333;
#         font-weight: normal;
#     }}

#     /* Custom fonts */
#     @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
#     body, p, h1, h2, h3, h4, h5, h6 {{
#         font-family: 'Roboto', sans-serif;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Welcome message
# st.markdown(
#     """
#     <div class="welcome">
#         <h1>Welcome to the LLM-based RAG Search Chatbot</h1>
#         <p>Your AI assistant for quick and insightful information retrieval.</p>
#         <p class="smaller">Type your query below and let the chatbot do the rest!</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Initialize session state to store chat history as pairs of queries and responses
# if "history" not in st.session_state:
#     st.session_state.history = []

# # Input for user query
# query = st.text_input("Enter your query:")

# if st.button("Send"):
#     if query:
#         # Send the query to the Flask API
#         try:
#             response = requests.post(FLASK_API_URL, json={"query": query})
#             if response.status_code == 200:
#                 answer = response.json().get('response', "No answer received.")
                
#                 # Add the query and response as a pair to chat history
#                 st.session_state.history.append({"query": query, "response": answer})
#             else:
#                 st.error(f"Error: {response.status_code} - {response.text}")
#         except requests.RequestException as e:
#             st.error(f"Request failed: {e}")

# # Display the chat history in reverse order (newest at the top)
# for chat in reversed(st.session_state.history):
#     st.markdown(f"<div class='chatbox user-message'>You: {chat['query']}</div>", unsafe_allow_html=True)
#     st.markdown(f"<div class='chatbox bot-message'>Bot: {chat['response']}</div>", unsafe_allow_html=True)
