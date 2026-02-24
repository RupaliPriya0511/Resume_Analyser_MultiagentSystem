"""Simple CLI wrapper around RootAgent to demonstrate end-to-end run.
Usage:
    python main.py <resume-pdf-path> "<job description text>"
"""

import sys
from agents.root_agent import RootAgent


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <resume-pdf-path> \"<job description text>\"")
        sys.exit(1)

    resume_path = sys.argv[1]
    job_description = sys.argv[2]

    orchestrator = RootAgent()
    result = orchestrator.run(resume_path, job_description)

    print("Analysis complete. Report at:", result["recommendation"]["report_path"])
    print("Recommendations:\n", "\n".join(result["recommendation"]["recommendations"]))


if __name__ == "__main__":
    main()
