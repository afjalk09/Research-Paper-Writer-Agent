
from crewai import Agent
from crewai.tools import tool
from model import gemini_llm
from langchain_tavily import TavilySearch

@tool("Tavily Search Tool")
def search_tool(query: str) -> str:
    """Search the web for research papers, methodologies, and technical context."""
    tavily_instance = TavilySearch(max_results=5)
    return str(tavily_instance.run(query))


# 1. LITERATURE RESEARCHER
researcher = Agent(
    role='Literature Researcher',
    goal='Find and ingest relevant research papers or thorough data on a given topic.',
    backstory='An expert academic librarian capable of finding hidden correlations in literature.',
    tools=[search_tool],
    verbose=True,
    llm=gemini_llm
)
