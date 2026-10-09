# 🤖 AI Customer Support Agent

A responsive, web-based customer support chatbot built using **LangChain**, **Streamlit**, and **OpenAI's GPT models**. This application implements conversational memory to maintain context throughout multi-turn interactions, providing a smooth human-like support experience.

## 🚀 Features
- **Contextual Memory:** Tracks and remembers previous messages within the chat session using LangChain's `ConversationBufferMemory`.
- **Streamlit Interface:** Offers a clean, minimal UI tailored for immediate user engagement.
- **Secure API Integration:** Prompts users dynamically for their OpenAI API key in a secured sidebar input.

## 🛠️ Tech Stack
- **Language:** Python
- **LLM Orchestration:** LangChain
- **LLM Provider:** OpenAI (`gpt-4o-mini`)
- **Frontend Framework:** Streamlit

## ⚙️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd AI-Support-Agent
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📝 How to Use
1. Open the local Streamlit URL generated in your terminal (usually `http://localhost:8501`).
2. Enter your personal OpenAI API Key in the secured password field within the sidebar.
3. Start typing your customer service queries in the bottom chat bar!
