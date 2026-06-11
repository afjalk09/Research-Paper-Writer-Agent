# Research Paper Writer using CrewAI & Gemini

An autonomous multi-agent research system built with CrewAI and Google Gemini that researches a scientific topic, identifies limitations in existing work, proposes innovations, drafts an academic paper, performs peer review, and exports the final manuscript to Markdown.

---

## Overview

This project simulates a complete academic research workflow using specialized AI agents collaborating sequentially.

Given a research topic, the system:

1. Searches and collects literature.
2. Extracts research limitations.
3. Proposes innovative solutions.
4. Writes a complete academic paper.
5. Performs peer review.
6. Exports the final paper as a Markdown document.

---

## Architecture

```text
Topic Input
    │
    ▼
Literature Researcher
    │
    ▼
Limitation Extractor
    │
    ▼
Innovation Strategist
    │
    ▼
Academic Writer
    │
    ▼
Peer Reviewer
    │
    ▼
Publisher
    │
    ▼
final_research_paper.md
```

---

## Agents

### Literature Researcher

**Role:** Literature Researcher

**Responsibilities**

* Search for relevant papers and resources
* Gather technical references
* Summarize existing methodologies

**Tools**

* Tavily Search

---

### Limitation Extractor

**Role:** Limitation Extractor

**Responsibilities**

* Identify weaknesses in current approaches
* Find research gaps
* Analyze methodological constraints

---

### Innovation Strategist

**Role:** Innovation Strategist

**Responsibilities**

* Generate novel ideas
* Propose technical solutions
* Create conceptual frameworks

---

### Academic Writer

**Role:** Academic Writer

**Responsibilities**

* Produce a formal academic manuscript
* Create structured sections
* Maintain scientific writing style

---

### Peer Reviewer

**Role:** Peer Reviewer

**Responsibilities**

* Verify logical consistency
* Validate conclusions
* Improve clarity and rigor

---

### Publisher

**Role:** Publisher

**Responsibilities**

* Finalize formatting
* Export final research paper
* Generate Markdown output

---

## Technology Stack

* Python 3.10+
* CrewAI
* Google Gemini
* Tavily Search API
* LangChain

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/research-paper-writer.git
cd research-paper-writer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```
---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```



Recommended models:

| Model            | Use Case              |
| ---------------- | --------------------- |
| gemini-1.5-pro   | Best quality          |
| gemini-1.5-flash | Faster and cheaper    |
| gemini-2.5-flash | Latest fast model     |
| gemini-2.5-pro   | Latest advanced model |

---

## Running the Project

```bash
python main.py
```

---

## Example Input

```python
result = research_crew.kickoff(
    inputs={
        "topic": "Impact of Multi-Agent LLMs on Scientific Peer Review Fatigue"
    }
)
```

---

## Workflow Tasks

### Task 1

Gather research papers and technical notes.

### Task 2

Identify limitations and gaps.

### Task 3

Generate innovative solutions.

### Task 4

Write a complete academic paper.

### Task 5

Review and validate the paper.

### Task 6

Publish the final version to:

```text
final_research_paper.md
```

---

## Output Example

```text
final_research_paper.md
```

Contents:

```markdown
# Impact of Multi-Agent LLMs on Scientific Peer Review Fatigue

Install missing packages:

```bash
pip install -r requirements.txt
```


## Future Enhancements

* ArXiv integration
* Semantic paper retrieval
* Citation generation
* PDF export
* Research paper ranking
* Knowledge graph generation
* Multi-paper comparison
* Automated bibliography creation

---

## License

MIT License

---

## Author

Afjal Khan

Built using CrewAI, Gemini, LangChain, and Tavily Search.
