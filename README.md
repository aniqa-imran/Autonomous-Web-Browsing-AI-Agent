# Autonomous-Web-Browsing-AI-Agent

An intelligent, autonomous AI agent built with **Streamlit**, **Google Gemini API**, and **DuckDuckGo Search**. This agent is capable of searching the live web in real time, gathering current information, and synthesizing comprehensive, accurate answers to user queries with source citations.

---

## 🌟 Key Features

- **🌐 Live Web Search Integration:** Uses DuckDuckGo Search API to query real-time information from the web.
- **🧠 Autonomous Query Planning:** Automatically converts user questions into concise, optimized web search queries using Google Gemini.
- **⚡ Rate-Limit Handling & Fallback:** Built-in multi-model fallback (`gemini-1.5-flash`, `gemini-1.5-pro`) to handle API rate limits smoothly.
- **🎨 Modern Dark UI:** Styled with sleek CSS glassmorphism, gradient accents, and responsive layout for a premium developer experience.
- **💬 Interactive Chat Experience:** Maintains conversation flow with status indicators showing live agent browsing steps.

---

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **LLM Engine:** [Google Gemini API](https://ai.google.dev/) (`google-generativeai`)
- **Web Search Engine:** [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) (`duckduckgo-search`)
- **Language:** Python 3.9+

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally:

### 1. Prerequisites
Ensure you have Python installed on your system. You can check by running:

python --version
cd Autonomous-Web-Browsing-AI-Agent
3. Install Dependencies
Install the required Python packages:

pip install streamlit google-generativeai duckduckgo-search
4. Run the Application
python -m streamlit run app.py
Start the Streamlit development server:

streamlit run app.py

# 🗝️ How to Get a Free Gemini API Key
Go to Google AI Studio.

Sign in with your Google Account.

Click on Get API Key and then Create API Key.

Copy the generated key and paste it into the Configuration Sidebar inside the app.

# 💡 Example Queries to Test
🌤️ "What is the current weather forecast for Lahore today?"

📰 "What are the top 3 latest tech or AI news stories from this week?"

🏏 "Who won the latest cricket match yesterday and what was the score?"

# 📝 License
This project is licensed under the MIT License - feel free to use and modify it.
