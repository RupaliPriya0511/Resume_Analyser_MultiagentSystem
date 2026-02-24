"""Simple Flask-based web UI for the Smart Resume Analyzer.

This lightweight interface allows a user to upload a resume PDF and paste a job
description. The backend calls the RootAgent pipeline and displays the
markdown report on the page. Designed purely for demonstration; does not
require Google ADK.
"""

from flask import Flask, request, render_template_string
from agents.root_agent import RootAgent
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

FORM_HTML = """
<!doctype html>
<title>Smart Resume Analyzer</title>
<h1>Upload Resume and Job Description</h1>
<form method=post enctype=multipart/form-data>
  <label>Resume PDF: <input type=file name=resume></label><br><br>
  <label>Job Description:<br><textarea name=jd rows=6 cols=60></textarea></label><br><br>
  <input type=submit value='Analyze'>
</form>
{% if report %}
<h2>Analysis Report</h2>
<pre>{{ report }}</pre>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    report_text = None
    if request.method == 'POST':
        resume = request.files.get('resume')
        jd = request.form.get('jd', '')
        if resume and jd:
            path = os.path.join(UPLOAD_FOLDER, resume.filename)
            resume.save(path)
            agent = RootAgent()
            result = agent.run(path, jd)
            # read generated report file
            try:
                with open(result['recommendation']['report_path'], 'r', encoding='utf-8') as f:
                    report_text = f.read()
            except Exception as e:
                report_text = f"Failed to read report: {e}"
    return render_template_string(FORM_HTML, report=report_text)

if __name__ == '__main__':
    app.run(debug=True)
