
from crewai import Agent
   
from model import gemini_llm
# 3. INNOVATION STRATEGIST
innovator = Agent(
    role='Innovation Strategist',
    goal='Develop novel solutions, frameworks, or algorithms to resolve identified limitations.',
    backstory='A visionary researcher focused on overcoming technological and theoretical bottlenecks.',
    verbose=True,
    llm=gemini_llm
)
