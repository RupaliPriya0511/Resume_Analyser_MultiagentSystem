# Problem Statement

## Smart Resume Analyzer

Design and build a functional multi-agent system using Google ADK to assist
candidates in optimizing their resumes for specific job descriptions.

### Objective
Accept a candidate's resume (PDF) and a job description as inputs, then
produce a concise, structured markdown report outlining:

- Matching skills between the resume and the job description
- Skills missing from the resume that appear in the job description
- Extra skills on the resume not required by the job description
- Keyword and content improvement suggestions for the resume

The system should be simple, deterministic, and easy to explain. It will
leverage Google ADK patterns with a Root Agent orchestrating at least three
sub-agents, and must use both built-in (`google_search`) and custom tools to
fulfill its responsibilities.