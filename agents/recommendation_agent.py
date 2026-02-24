"""ADK-style sub-agent: recommendations and report generation.

Exposes `recommendation_agent` as an Agent instance. It produces human-aimed
recommendations and writes a markdown report using the `generate_markdown_report` tool.
"""

try:
    from google.adk import Agent  # type: ignore
    ADK_AVAILABLE = True
except Exception:
    ADK_AVAILABLE = False

from tools.custom_tools import generate_markdown_report


def _recommend(resume_text: str, jd_info: dict, match_info: dict) -> dict:
    recs = []
    if match_info.get("missing"):
        recs.append(
            "Consider including the following skills in your resume: "
            + ", ".join(match_info["missing"])
        )
    jd_keywords = jd_info.get("keywords", [])
    if jd_keywords:
        recs.append("Use keywords such as: " + ", ".join(jd_keywords[:10]))
    recs.append("Ensure your contact information is easy to find.")

    report_data = {
        "resume_text": resume_text,
        "jd_text": jd_info.get("original"),
        "match": match_info,
        "recommendations": recs,
    }
    path = generate_markdown_report(report_data)
    return {"report_path": path, "recommendations": recs}


if ADK_AVAILABLE:
    recommendation_agent = Agent(
        name="recommendation_agent",
        tools=[generate_markdown_report],
    )
else:
    recommendation_agent = Agent(
        name="recommendation_agent",
        system_prompt=(
            "Suggest resume improvements and generate a concise markdown report."
        ),
        tools=[generate_markdown_report],
        run_fn=_recommend,
    )
