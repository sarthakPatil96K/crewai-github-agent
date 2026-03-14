from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return LLM(
        model="groq/llama3-70b-8192",
        api_key=os.getenv("GROQ_API_KEY")
    )