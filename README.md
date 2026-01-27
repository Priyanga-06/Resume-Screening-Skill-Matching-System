## RESUME SCREENING & AI SKILL MATCHING SYSTEM

❖ This project is an interactive Resume Screening and Skill Matching web application built using Python and Streamlit.
It helps recruiters and candidates analyze resumes, match skills against job roles, generate improvement suggestions, and receive automated email communication.

The system focuses on making resume evaluation simple, practical, and usable for real-world hiring scenarios.

## PROJECT OVERVIEW

❖Resume shortlisting is often manual, time-consuming, and inconsistent.
This project automates the process by answering key questions:

➛How well does a resume match a selected job role?

➛Which skills are missing for the selected role?

➛What improvements can the candidate make?

➛Which companies commonly hire for that role?

➛Can the candidate apply directly after qualification?

➛The application presents these insights in a clean and interactive interface.

## BUSINESS OBJECTIVE

The goal of this project is to simplify resume screening and improve hiring decisions.

It supports:

➛Students improving their resumes

➛Recruiters shortlisting candidates faster

➛Career guidance through role-based suggestions

➛This tool is designed for practical use in real hiring workflows.

## APPLICATION FEATURES
### CORE FEATURES

➛Secure login system

➛Upload multiple PDF resumes

➛Job role selection

➛Automatic skill extraction from resumes

➛Skill matching percentage

➛Missing skills identification

➛Role-based AI skill suggestions

➛Recommended companies for each role

➛Downloadable resume analysis report

➛Apply option enabled only when match exceeds 50%

➛Application form (name, email, phone) shown dynamically

➛Automatic email sent to the applicant



## TECHNOLOGY STACK

➛Python

➛Streamlit

➛Pandas

➛PDF Processing (PyPDF2 / pdfplumber)

➛SMTP for email automation

➛HTML & CSS for UI customization

➛Environment variables using .env

## PROJECT CAPABILITIES

➛Resume parsing from PDF files

➛Skill extraction using keyword matching

➛Role-based skill comparison

➛Intelligent feedback for improvement

➛User authentication (login/logout)

➛Dynamic application flow

➛Automated email notification system

➛Professional report generation

➛Clean UI with custom CSS


## PROJECT STRUCTURE

```text
resume-screening-project/
│
├── app.py
│   └── Main Streamlit application (UI + flow control)
│
├── auth.py
│   └── Login and session authentication logic
│
├── utils.py
│   └── Skill matching, suggestions, company logic
│
├── pdf_processing.py
│   └── Extracts text from uploaded PDF resumes
│
├── report.py
│   └── Generates downloadable resume report
│
├── email_utils.py
│   └── Sends automated email to applicants
│
├── .env
│   └── Stores secure email credentials
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```


## Work flow

<img width="1536" height="1024" alt="ChatGPT Image Jan 27, 2026, 08_28_08 PM" src="https://github.com/user-attachments/assets/46c7be0b-7cb1-41e2-9b74-90956bc8afc1" />

## How to Run the Application

### Run the Streamlit app using the following command:
       ➛ streamlit run app.py
After running the command, open the local URL shown in the terminal (usually http://localhost:8501) in your browser.

## Future Enhancements

 ➛Support for more resume formats (DOCX)

 ➛Improved NLP-based skill extraction

 ➛Database integration for storing candidate data

 ➛Advanced dashboard with analytics

 ➛Integration with job portals
