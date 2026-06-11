from crewai import Agent
   
from model import gemini_llm
# 6. PUBLISHER
publisher = Agent(
    role='Publisher',
    goal='Finalize document formatting and compile the final paper into a publishable markdown file.',
    backstory='A technical publisher responsible for deploying finalized research assets.',
    verbose=True,
    llm=gemini_llm
)
