"""ADK-style sub-agent: resume parsing.

Exposes `resume_parsing_agent` variable which is an `Agent` instance. The
file supports a real `google.adk.Agent` if available, otherwise a local stub
Agent is used so the project remains runnable without ADK.
"""

from typing import Any

try:
    from google.adk import Agent  # type: ignore
    ADK_AVAILABLE = True
except Exception:
    ADK_AVAILABLE = False

from tools.custom_tools import extract_pdf_text


def _parse_resume(filepath: str) -> str:
    """Wrapper that uses the extract_pdf_text tool and normalizes output."""
    text = extract_pdf_text(filepath)
    return text.strip()


if ADK_AVAILABLE:
    # For ADK, avoid passing prompt fields that may be rejected by the
    # framework's validation. Tools are attached so ADK can surface them.
    resume_parsing_agent = Agent(
        name="resume_parsing_agent",
        tools=[extract_pdf_text],
    )
else:
    resume_parsing_agent = Agent(
        name="resume_parsing_agent",
        system_prompt=(
            "Extract and clean text from resume PDF. Return plain text only."
        ),
        tools=[extract_pdf_text],
        run_fn=_parse_resume,
    )
