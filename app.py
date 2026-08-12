import os

import time

import streamlit as st

import google.generativeai as genai

from duckduckgo_search import DDGS



# ----------------------------------------------------

# 1. PAGE CONFIGURATION

# ----------------------------------------------------

st.set_page_config(

    page_title="Autonomous Browsing AI Agent", page_icon="🤖", layout="wide"

)



st.title("🤖 Autonomous Web Browsing AI Agent")

st.markdown("An AI Agent capable of searching the web live to answer real-time queries.")



# Sidebar

with st.sidebar:

    st.header("⚙️ Configuration")

    api_key = st.text_input("Enter Gemini API Key", type="password")

    st.divider()

    st.info(

        "💡 **Tip:** Get your free API key from [Google AI Studio](https://aistudio.google.com/)."

    )



# ----------------------------------------------------

# 2. HELPER FUNCTIONS

# ----------------------------------------------------

def search_web(query: str):

    try:

        results = []

        with DDGS() as ddgs:

            search_gen = ddgs.text(query, max_results=3)

            if search_gen:

                for r in search_gen:

                    title = r.get("title", "No Title")

                    snippet = r.get("body", "No Snippet")

                    url = r.get("href", "#")

                    results.append(

                        f"**Title:** {title}\n**Snippet:** {snippet}\n**URL:** {url}"

                    )



        if not results:

            return "No web results found for this query."



        return "\n\n".join(results)

    except Exception as e:

        return f"Search Error: {str(e)}"





def get_gemini_response(prompt: str):

    """Helper to safely call models with fallback to avoid 429 quota errors."""

    models_to_try = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-flash-latest"]

   

    last_error = None

    for model_name in models_to_try:

        try:

            model = genai.GenerativeModel(model_name)

            response = model.generate_content(prompt)

            return response.text

        except Exception as e:

            last_error = e

            continue  # Direct fallback to next model if quota/error hits

           

    raise last_error





def run_agent(user_query: str, api_key: str):

    genai.configure(api_key=api_key)



    planner_prompt = f"""

    You are an AI Search Planner.

    User Question: "{user_query}"

   

    Formulate a short, effective web search query to find accurate and latest information.

    Return ONLY the search query text, no quotes or extra text.

    """



    try:

        search_query = get_gemini_response(planner_prompt).strip()

    except Exception as e:

        if "429" in str(e):

            return "⚠️ All models hit rate limits. Please wait about 30 seconds before typing next query."

        return f"Model Planning Error: {str(e)}"



    with st.status("🤖 Agent actively browsing...", expanded=True) as status:

        st.write(f"🔍 **Optimized Query:** `{search_query}`")

        st.write("🌐 Fetching live context from the web...")



        search_results = search_web(search_query)



        if "Search Error" in search_results:

            status.update(label="Search Failed!", state="error", expanded=True)

        else:

            st.write("✅ Web Search Complete!")

            status.update(

                label="Information Gathered!", state="complete", expanded=False

            )



    # Short delay to prevent hitting RPM limits

    time.sleep(2)



    final_prompt = f"""

    You are an intelligent Autonomous AI Assistant with web access.

    Answer the user's query comprehensively using the live search data below.

    Include relevant source URLs from the search context where helpful.

   

    User Query: {user_query}

   

    Live Web Search Context:

    {search_results}

    """



    try:

        return get_gemini_response(final_prompt)

    except Exception as e:

        if "429" in str(e):

            return "⚠️ Rate limit reached on final synthesis. Please wait 30 seconds and try again."

        return f"Error generating answer: {str(e)}"





# ----------------------------------------------------

# 3. CHAT INTERFACE & APP LOGIC

# ----------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []



# Display previous conversation

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])



# User Input

if user_input := st.chat_input("Ask anything (e.g., Latest AI trends, Stock updates)..."):

    if not api_key:

        st.error("⚠️ Please enter your Gemini API Key in the sidebar first!")

    else:

        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):

            st.markdown(user_input)



        with st.chat_message("assistant"):

            response = run_agent(user_input, api_key)

            st.markdown(response)



        st.session_state.messages.append({"role": "assistant", "content": response})