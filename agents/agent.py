"""ADK-compliant root agent definition.

This file exposes the top-level variable `root_agent` which ADK expects to
discover when loading the `agents` package. We try to import the real
`Agent` class from `google.adk` but provide a lightweight local stub so the
project remains testable without the ADK CLI.

The `root_agent` lists sub-agents (also ADK-style Agent instances) so the
ADK runtime can display and orchestrate them. For local testing the
`run` function delegates to the sub-agents in sequence.
"""

from typing import Any, Dict

try:
    from google.adk import Agent  # type: ignore
    ADK_AVAILABLE = True
except Exception:
    ADK_AVAILABLE = False

    # Minimal local stub used when ADK is not installed. It stores
    # metadata and optionally a run function for local testing.
    class Agent:
        def __init__(self, name: str, system_prompt: str = "", tools=None, sub_agents=None, run_fn=None):
            self.name = name
            self.system_prompt = system_prompt
            self.tools = tools or []
            self.sub_agents = sub_agents or []
            self._run_fn = run_fn

        def run(self, *args, **kwargs):
            if self._run_fn:
                return self._run_fn(*args, **kwargs)
            # default no-op
            return {}


from agents.resume_parsing_agent import resume_parsing_agent
from agents.job_analysis_agent import job_analysis_agent
from agents.skill_matching_agent import skill_matching_agent
from agents.recommendation_agent import recommendation_agent


def _local_orchestrator(resume_path: str, job_description: str) -> Dict[str, Any]:
    """Simple sequential orchestration used for local testing.

    It calls each sub-agent's `run` method and assembles results in the same
    shape used across the project.
    """
    # 1. parse resume
    resume_text = resume_parsing_agent.run(resume_path)

    # 2. analyze job description
    jd_info = job_analysis_agent.run(job_description)

    # 3. match skills
    match_info = skill_matching_agent.run(resume_text, jd_info)

    # 4. recommendations + report
    rec_info = recommendation_agent.run(resume_text, jd_info, match_info)

    return {
        "resume_text": resume_text,
        "jd_info": jd_info,
        "match_info": match_info,
        "recommendation": rec_info,
    }


if ADK_AVAILABLE:
    # Pass only minimal fields to avoid ADK validation errors; prompts are
    # managed by ADK tooling or the UI. Keep sub_agents and tools visible.
    root_agent = Agent(
        name="smart_resume_analyzer_root",
        sub_agents=[
            resume_parsing_agent,
            job_analysis_agent,
            skill_matching_agent,
            recommendation_agent,
        ],
    )
else:
    root_agent = Agent(
        name="smart_resume_analyzer_root",
        system_prompt=(
            "You are the root orchestrator. Coordinate resume parsing, job analysis (using google_search), "
            "skill matching, and recommendation generation. Delegate tasks to the sub-agents."
        ),
        sub_agents=[
            resume_parsing_agent,
            job_analysis_agent,
            skill_matching_agent,
            recommendation_agent,
        ],
        run_fn=_local_orchestrator,
    )
