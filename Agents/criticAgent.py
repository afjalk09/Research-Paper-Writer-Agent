from crewai import Agent
   
from model import gemini_llm
# 2. LIMITATION EXTRACTOR
critic = Agent(
    role='Limitation Extractor',
    goal='Identify implicit and explicit gaps, flaws, and limitations in the gathered research.',
    backstory='A meticulous peer reviewer specializing in methodology breakdowns and spotting constraints.',
    verbose=True,
    llm=gemini_llm
)
