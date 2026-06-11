from crewai import Agent
   
from model import gemini_llm
# 4. ACADEMIC WRITER
writer = Agent(
    role='Academic Writer',
    goal='Draft a comprehensive, highly formal academic research paper in markdown format.',
    backstory='A seasoned academic writer skilled at structuring papers with clean definitions and prose.',
    verbose=True,
    llm=gemini_llm
)
