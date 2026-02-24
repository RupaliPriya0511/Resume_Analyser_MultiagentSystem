"""Custom tool implementations required by the assessment.
These functions simulate or wrap functionality that agents will rely upon.

Each tool is typed and contains a clear docstring so that it can be
referenced directly by agents or by the ADK tool registry.
"""

import re
import os
from typing import List, Dict

# NOTE: In a real ADK environment, `google_search` would be a built-in tool provided by the
# framework. Here we provide a stub that demonstrates its intended use.

def google_search(query: str) -> List[str]:
    """Simulated built-in Google search tool.

    Args:
        query: search query string.

    Returns:
        A list of result snippets (mocked for assessment).
    """
    # For assessment purposes, return static keywords related to typical job descriptions
    return [
        "Skills: Python, Machine Learning, Data Analysis",
        "Requirements: experience with Git, teamwork, communication",
    ]


def extract_pdf_text(filepath: str) -> str:
    """Read a PDF file and return its text content.

    Uses PyPDF2 if installed; otherwise returns a placeholder string.

    Args:
        filepath: path to the resume PDF.

    Returns:
        Full text extracted from the PDF (or a mock string).
    """
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(filepath)
        text: List[str] = []
        for page in reader.pages:
            text.append(page.extract_text() or "")
        return "\n".join(text)
    except Exception:
        # fallback mock
        return f"[Text from {os.path.basename(filepath)}]"


def extract_keywords(text: str) -> List[str]:
    """Extract simple keywords/skills from a block of text.

    This naive implementation splits on commas, semicolons, and newlines and
    trims whitespace. It is sufficient for demonstration purposes.

    Args:
        text: the input text to analyze.

    Returns:
        List of keyword strings.
    """
    tokens = re.split(r"[,;\n]", text)
    keywords: List[str] = [tok.strip() for tok in tokens if tok.strip()]
    return keywords


def match_resume_to_jd(resume_text: str, jd_text: str) -> Dict[str, List[str]]:
    """Compare resume and job description texts to identify matches and gaps.

    Args:
        resume_text: raw text from candidate's resume.
        jd_text: raw text of the job description.

    Returns:
        A dictionary with keys 'matched', 'missing', and 'extra'.
    """
    resume_skills = set(extract_keywords(resume_text.lower()))
    jd_skills = set(extract_keywords(jd_text.lower()))
    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    extra = resume_skills - jd_skills
    return {
        "matched": sorted(matched),
        "missing": sorted(missing),
        "extra": sorted(extra),
    }


def generate_markdown_report(data: Dict, output_path: str = "report.md") -> str:
    """Create a markdown report from the analysis data and save to disk.

    Args:
        data: dictionary containing resume text, jd text, match results, etc.
        output_path: file path where markdown will be written.

    Returns:
        The path to the generated report file.
    """
    lines: List[str] = []
    lines.append("# Resume Analysis Report\n")
    if "resume_text" in data:
        lines.append("## Resume Excerpt")
        lines.append(data["resume_text"][:500] + "\n")
    if "jd_text" in data:
        lines.append("## Job Description Excerpt")
        lines.append(data["jd_text"][:500] + "\n")
    if "match" in data:
        match = data["match"]
        lines.append("## Skill Matching")
        lines.append(f"- Matched: {', '.join(match.get('matched', []))}")
        lines.append(f"- Missing: {', '.join(match.get('missing', []))}")
        lines.append(f"- Extra: {', '.join(match.get('extra', []))}")
    if "recommendations" in data:
        lines.append("## Recommendations")
        for rec in data["recommendations"]:
            lines.append(f"- {rec}")
    report = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    return output_path
