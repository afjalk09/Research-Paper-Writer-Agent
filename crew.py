
from crewai import  Crew, Process
from dotenv import load_dotenv
load_dotenv()



from Agents.criticAgent import critic
from Agents.innovatorAgent import innovator
from Agents.researcherAgent import researcher
from Agents.writerAgent import writer
from Agents.verifierAgent import verifier
from Agents.publisherAgent import publisher

from Tasks.tasks import tasks


# Assemble the Multi-Agent System
research_crew = Crew(
    agents=[researcher, critic, innovator, writer, verifier, publisher],
    tasks=tasks,
    process=Process.sequential # Ensures linear flow from Agent 1 to Agent 6
)

# Kickoff the multi-agent system execution
result = research_crew.kickoff(inputs={'topic': 'Agentic Ai in Health Care'})
print("Workflow Complete!")
