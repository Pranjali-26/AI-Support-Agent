import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Configure the Streamlit page layout
st.set_page_config(page_title="AI Support Agent", page_icon="🤖")
st.title("🤖 AI Customer Support Agent")
st.write("Welcome! How can I assist you today?")

# Initialize OpenAI API Key (using Streamlit secrets or user input for safety)
openai_api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if not openai_api_key:
    st.info("Please add your OpenAI API key in the sidebar to start the chat.")
    st.stop()

# Set up LangChain conversational memory so the bot remembers context
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize the LLM framework and conversation chain
llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key, model_name="gpt-4o-mini")
conversation = ConversationChain(llm=llm, memory=st.session_state.memory, verbose=False)

# Display prior chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input interactions
if user_input := st.chat_input("Type your support request here..."):
    # Display user query
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Generate agent response using conversational history
    with st.chat_message("assistant"):
        response = conversation.predict(input=user_input)
        st.markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
