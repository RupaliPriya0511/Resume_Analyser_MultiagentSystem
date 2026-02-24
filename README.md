# Smart Resume Analyzer (Shorthills)

This repository implements a simple multi-agent system using Python, following the Google
ADK architecture. The system reads a candidate resume (PDF) and a job description,
compares skills, and generates a markdown report with recommendations.

## Agents
1. **RootAgent** – orchestrator that sequences tasks
2. **ResumeParsingAgent** – extracts text from PDF using `extract_pdf_text`
3. **JobAnalysisAgent** – analyzes job description and enriches via `google_search`
4. **SkillMatchingAgent** – compares resume vs. JD using `match_resume_to_jd`
5. **RecommendationAgent** – suggests improvements and generates a report

## Tools
- `extract_pdf_text(filepath)`
- `extract_keywords(text)`
- `match_resume_to_jd(resume_text, jd_text)`
- `generate_markdown_report(data)`
- Built-in `google_search` (stubbed)

## Setup & Usage
1. **Clone** the repository and `cd` into `shorthills`.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate   # Windows
   # or: source .venv/bin/activate  # Unix
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the API key:
   ```bash
   cp .env.example .env  # then edit .env with your Gemini key
   ```
   (`.env`, `.venv/`, and `__pycache__/` are gitignored.)

**Running the system**
- With ADK installed locally:
   ```bash
   adk run smart_resume_analyzer    # command-line chat
   adk web                         # browser UI
   ```
- Without ADK, use the bundled alternatives:
   ```bash
   python ui.py                    # simple Flask form
   python main.py resume.pdf "Job description text"
   ```
A `report.md` file is produced containing the analysis.

---
## Architecture and Approach
The implementation follows the specified ADK architecture with a single
**RootAgent** orchestrating a sequence of four focused sub-agents:
1. **ResumeParsingAgent** – uses `extract_pdf_text` to pull text from a PDF.
2. **JobAnalysisAgent** – extracts keywords from the job description and
   enriches them using the built‑in `google_search` tool.
3. **SkillMatchingAgent** – compares resume and JD skills with
   `match_resume_to_jd`.
4. **RecommendationAgent** – creates suggestions and generates the final
   markdown report via `generate_markdown_report`.

Agents communicate through explicit return values; no hidden state or global
variables are used. Custom tools are plain, typed Python functions, making it
straightforward to replace or test them independently. The flow is primarily
sequential, satisfying the assessment’s orchestration requirement while
keeping the system simple and deterministic.

### Submission Notes
To complete the assessment submission, ensure that:

1. `adk run smart_resume_analyzer` and `adk web` execute successfully
   (ADK must be installed locally).  
2. This README, plus `problem_statement.md`, is included in the repo.  
3. The repository is pushed to a public GitHub URL.  
4. Provide a 5–6 sentence explanation of the overall approach and agent
   architecture (see below for a suggested text).  

Below is a sample explanation.
> I designed a sequential multi-agent pipeline using Google ADK. A RootAgent
> orchestrates four specialized sub-agents—resume parsing, job analysis,
> skill matching, and recommendation—each backed by clear, typed custom tools.
> The built-in `google_search` tool enriches job keywords, and results are
> compiled into a markdown report. The architecture is deterministic with
> explicit data flow, making it easy to understand and demonstrate when
> running via `adk run` or in the provided Flask UI. The system meets the
> requirement for root/sub-agent orchestration, tool usage, and end-to-end
> functionality while remaining simple and interview-friendly.

## Notes
- Designed for clarity and ease of explanation in interviews.
- Follows sequential orchestration with explicit data passing.
- Minimum number of agents and tools as per assessment constraints.
# Smart Resume Analyzer (Shorthills)

This repository implements a simple multi-agent system using Python, following the Google
ADK architecture. The system reads a candidate resume (PDF) and a job description,
compares skills, and generates a markdown report with recommendations.

## Agents

1. **RootAgent** – orchestrator that sequences tasks
2. **ResumeParsingAgent** – extracts text from PDF using `extract_pdf_text`
3. **JobAnalysisAgent** – analyzes job description and enriches via `google_search`
4. **SkillMatchingAgent** – compares resume vs. JD using `match_resume_to_jd`
5. **RecommendationAgent** – suggests improvements and generates a report

## Tools

- `extract_pdf_text(filepath)`
- `extract_keywords(text)`
- `match_resume_to_jd(resume_text, jd_text)`
- `generate_markdown_report(data)`
- Built-in `google_search` (stubbed)

## Setup & Usage

1. **Clone** the repository and `cd` into `shorthills`.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate   # Windows
   # or: source .venv/bin/activate  # Unix
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the API key:
   ```bash
   cp .env.example .env  # then edit .env with your Gemini key
   ```
   (`.env`, `.venv/`, and `__pycache__/` are gitignored.)

**Running the system**

- With ADK installed locally:
  ```bash
  adk run smart_resume_analyzer    # command-line chat
  adk web                         # browser UI
  ```
- Without ADK, use the bundled alternatives:
  ```bash
  python ui.py                    # simple Flask form
  python main.py resume.pdf "Job description text"
  ```
A `report.md` file is produced containing the analysis.

---

## Architecture and Approach
The implementation follows the specified ADK architecture with a single
**RootAgent** orchestrating a sequence of four focused sub-agents:

1. **ResumeParsingAgent** – uses `extract_pdf_text` to pull text from a PDF.
2. **JobAnalysisAgent** – extracts keywords from the job description and
   enriches them using the built‑in `google_search` tool.
3. **SkillMatchingAgent** – compares resume and JD skills with
   `match_resume_to_jd`.
4. **RecommendationAgent** – creates suggestions and generates the final
   markdown report via `generate_markdown_report`.

Agents communicate through explicit return values; no hidden state or global
variables are used. Custom tools are plain, typed Python functions, making it
straightforward to replace or test them independently. The flow is primarily
sequential, satisfying the assessment’s orchestration requirement while
keeping the system simple and deterministic.

### Submission Notes
To complete the assessment submission, ensure that:

1. `adk run smart_resume_analyzer` and `adk web` execute successfully
   (ADK must be installed locally).  
2. This README, plus `problem_statement.md`, is included in the repo.  
3. The repository is pushed to a public GitHub URL.  
4. Provide a 5–6 sentence explanation of the overall approach and agent
   architecture (see below for a suggested text).  

Below is a sample explanation.

> I designed a sequential multi-agent pipeline using Google ADK. A RootAgent
> orchestrates four specialized sub-agents—resume parsing, job analysis,
> skill matching, and recommendation—each backed by clear, typed custom tools.
> The built-in `google_search` tool enriches job keywords, and results are
> compiled into a markdown report. The architecture is deterministic with
> explicit data flow, making it easy to understand and demonstrate when
> running via `adk run` or in the provided Flask UI. The system meets the
> requirement for root/sub-agent orchestration, tool usage, and end-to-end
> functionality while remaining simple and interview-friendly.

## Notes

- Designed for clarity and ease of explanation in interviews.
- Follows sequential orchestration with explicit data passing.
- Minimum number of agents and tools as per assessment constraints.