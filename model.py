import os
from crewai import LLM

gemini_llm =LLM(
    model="gemini-2.5-flash",
    temperature=0.2,  # Low temperature makes academic writing more factual
    google_api_key=os.environ.get("GEMINI_API_KEY")
)
