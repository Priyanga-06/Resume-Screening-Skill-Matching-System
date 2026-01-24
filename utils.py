import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# STEP 1: Load .env file
load_dotenv()

# STEP 2: Read values from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")


# ------------------ Other functions ------------------

def suggest_skills(role):
    suggestions_dict = {
        "Data Analyst": ["Learn Power BI", "Improve SQL queries", "Try Tableau"],
        "Full Stack Developer": ["Learn Node.js", "Practice React projects"],
        "Machine Learning Engineer": ["Learn PyTorch", "Work on Kaggle"],
        "Web Developer": ["Practice responsive design", "Learn Bootstrap"],
        "Python Developer": ["Learn Django", "Build automation projects"]
    }
    return suggestions_dict.get(role, [])


def get_companies(role):
    companies_dict = {
        "Data Analyst": ["Google", "Amazon", "TCS"],
        "Full Stack Developer": ["Microsoft", "Infosys"],
        "Machine Learning Engineer": ["IBM", "Accenture"],
        "Web Developer": ["Zoho", "Wipro"],
        "Python Developer": ["Capgemini", "Cognizant"]
    }
    return companies_dict.get(role, [])


def match_skills(text, skills_list, job_required_skills):
    text_lower = text.lower()
    found = [s for s in skills_list if s in text_lower]
    matched = [s for s in job_required_skills if s in found]
    percent = (len(matched) / len(job_required_skills)) * 100 if job_required_skills else 0
    return found, matched, percent


# ------------------ STEP 4 IS HERE ------------------
# Email sending function

def send_selection_email(to_email, role):

    subject = f"Selected for {role}"
    body = f"""Dear Candidate,

Congratulations! You have been selected for the role of {role}.

Best wishes,
HR Team
"""

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        raise e
