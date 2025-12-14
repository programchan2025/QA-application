import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Apple AI Story Generator",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Apple AI Story Generator")
st.write("Generate a short story on any topic using Gemini + LangChain.")

# -----------------------------
# API Key Handling (Best Practice)
# -----------------------------
# Set your API key as an environment variable before running:
# export GOOGLE_API_KEY="your_api_key_here"
# or on Windows:
# setx GOOGLE_API_KEY "your_api_key_here"

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.warning("⚠️ Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

# -----------------------------
# LLM Initialization
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key=api_key
)

# -----------------------------
# Prompt Template
# -----------------------------
system_prompt = """
You are a helpful AI assistant. Your task is to tell a creative story on any topic.

Topic / User Input:
{user_input}
"""

template = ChatPromptTemplate.from_template(system_prompt)
chain = template | llm

# -----------------------------
# User Input UI
# -----------------------------
user_input = st.text_input(
    "Enter a topic or opening line for your story:",
    placeholder="e.g., I am Abdul who wants to explore the world"
)

# -----------------------------
# Generate Story
# -----------------------------
if st.button("✨ Generate Story"):
    if not user_input.strip():
        st.error("Please enter a topic or sentence.")
    else:
        with st.spinner("Generating your story..."):
            response = chain.invoke({"user_input": user_input})
            st.subheader("📚 Generated Story")
            st.write(response.content)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with Streamlit, LangChain, and Google Gemini")
