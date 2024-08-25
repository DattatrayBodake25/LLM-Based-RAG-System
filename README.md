# LLM-Based-RAG-System

### Overview
This project implements a Retrieval-Augmented Generation (RAG) system using a Large Language Model (LLM). The system integrates a front-end interface with a backend service to scrape, process, and generate responses based on user queries. The architecture includes:

- **Streamlit Frontend**: Provides an interface for user interaction.
- **Flask Backend**: Handles API requests, content scraping, and LLM integration.
- **Large Language Model (LLM)**: Generates responses based on processed content.

### Features
- **User Interaction**: Users can input queries through a Streamlit-based frontend.
- **Content Retrieval**: Queries are used to fetch relevant articles from the internet.
- **Content Processing**: Scraped content is processed for LLM input.
- **Response Generation**: LLM generates answers based on the processed content.
- **Conversational Memory (Bonus)**: Integration of tools like LangChain for conversational memory.

### Prerequisites
- **Python 3.8 or above**
- **API Keys**: For scraping and LLM integration (provide in `.env` file)

### Setup Instructions

#### Step 1: Clone the Repository
```bash
git clone https://github.com/DattatrayBodake25/LLM-Based-RAG-System.git
cd LLM-Based-RAG-System


Step 2: Set Up a Virtual Environment
You can use venv or conda to create an isolated environment for this project.
Using venv
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Using conda
conda create --name project_env python=3.8
conda activate project_env

Step 3: Install Dependencies
Install the required packages listed in requirements.txt.
pip install -r requirements.txt

Step 4: Configure Environment Variables
Create a .env file in the root directory and add your API keys:
# Example .env file
GEMINI_API_KEY=your_gemini_api_key

Step 5: Run the Flask Backend
Navigate to the flask_app directory and start the Flask server:
cd flask_app
python app.py

Step 6: Run the Streamlit Frontend
In a new terminal, navigate to the streamlit_app directory and run the Streamlit app:
cd streamlit_app
streamlit run app.py

Step 7: Open the Application
Open your web browser and go to http://localhost:8501. You can now interact with the system by entering your queries.

Project Structure
flask_app/: Contains the backend Flask API and utility functions.
streamlit_app/: Contains the Streamlit front-end code.
.env: Stores API keys (ensure this file is not included in version control).
requirements.txt: Lists the project dependencies.
README.md: This file.


How It Works
User Input: Users submit queries through the Streamlit interface.
Query Handling: The query is sent to the Flask backend via API call.
Content Retrieval: The Flask backend uses an API to search the internet and scrape relevant articles.
Content Processing: The scraped content is processed and sent to the LLM.
Response Generation: The LLM generates a response based on the processed content.
Response Display: The response is sent back to the Streamlit interface for user viewing.
Contributing
Feel free to contribute to this project by submitting issues or pull requests. Follow the guidelines in the CONTRIBUTING.md file if available.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Streamlit for the frontend framework.
Flask for the backend framework.
Your LLM Provider for the language model.
