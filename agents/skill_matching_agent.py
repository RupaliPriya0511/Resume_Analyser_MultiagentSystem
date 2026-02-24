"""ADK-style sub-agent: skill matching.

Exposes `skill_matching_agent` variable which is an Agent instance. It uses
the `match_resume_to_jd` tool to compare resume and job description text.
"""

try:
    from google.adk import Agent  # type: ignore
    ADK_AVAILABLE = True
except Exception:
    ADK_AVAILABLE = False

from tools.custom_tools import match_resume_to_jd


def _match(resume_text: str, jd_info: dict) -> dict:
    jd_text = jd_info.get("original", "")
    return match_resume_to_jd(resume_text, jd_text)


if ADK_AVAILABLE:
    skill_matching_agent = Agent(
        name="skill_matching_agent",
        tools=[match_resume_to_jd],
    )
else:
    skill_matching_agent = Agent(
        name="skill_matching_agent",
        system_prompt=(
            "Compare resume skills with job requirements and return matched, missing, and extra skills."
        ),
        tools=[match_resume_to_jd],
        run_fn=_match,
    )
