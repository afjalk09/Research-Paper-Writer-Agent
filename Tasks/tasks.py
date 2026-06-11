
from crewai import  Task

from Agents.criticAgent import critic
from Agents.innovatorAgent import innovator
from Agents.researcherAgent import researcher
from Agents.writerAgent import writer
from Agents.verifierAgent import verifier
from Agents.publisherAgent import publisher

# Define the Sequential Tasks mapping agent outputs to inputs
tasks = [
    Task(
        description='Gather comprehensive research papers and technical notes on the topic: {topic}.',
        expected_output='A structured summary of existing literature and methodologies.',
        agent=researcher
    ),
    Task(
        description='Analyze the gathered literature summary and extract 3-5 key limitations or gaps.',
        expected_output='A categorized list of methodology or data limitations.',
        agent=critic
    ),
    Task(
        description='Provide a concrete, actionable technical solution or hypothesis to overcome each limitation found.',
        expected_output='A conceptual framework explaining how to resolve the limitations.',
        agent=innovator
    ),
    Task(
        description='Write a full academic research paper draft. Include Abstract, Introduction, Limitations, Proposed Solution, and Conclusion.',
        expected_output='A beautifully formatted research paper draft in Markdown syntax.',
        agent=writer
    ),
    Task(
        description='Review the drafted paper. Verify that the solutions logically solve the limitations and check for clarity.',
        expected_output='A verified, polished version of the research paper with referee notes applied.',
        agent=verifier
    ),
    Task(
        description='Take the verified paper and write it out to a permanent local file named "final_research_paper.md".',
        expected_output='File successfully written notification.',
        output_file='final_research_paper.txt',
        agent=publisher
    )
]
