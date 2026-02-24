"""ADK-style sub-agent: job analysis.

Exposes `job_analysis_agent` as an Agent instance. Uses built-in
`google_search` (stubbed in tools) to enrich keywords extracted from the
job description.
"""

try:
    from google.adk import Agent  # type: ignore
    ADK_AVAILABLE = True
except Exception:
    ADK_AVAILABLE = False

from tools.custom_tools import google_search, extract_keywords


def _analyze_jd(jd_text: str) -> dict:
    keywords = extract_keywords(jd_text)
    search_results = google_search(jd_text)
    for res in search_results:
        keywords.extend(extract_keywords(res))
    return {
        "original": jd_text,
        "keywords": sorted(set(keywords)),
        "search_results": search_results,
    }


if ADK_AVAILABLE:
    job_analysis_agent = Agent(
        name="job_analysis_agent",
        tools=[google_search, extract_keywords],
    )
else:
    job_analysis_agent = Agent(
        name="job_analysis_agent",
        system_prompt=(
            "Analyze the job description and identify required skills. Use google_search to enrich keywords."
        ),
        tools=[google_search, extract_keywords],
        run_fn=_analyze_jd,
    )
