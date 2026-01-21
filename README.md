# Resume-Screening-Skill-Matching-System

Project Overview:

A smart resume analysis system that allows users to upload resumes and automatically matches skills based on selected job roles.
The system provides match percentage, highlights strengths, and gives AI-based suggestions to improve the resume.

Features:

Upload multiple PDF resumes

Role-based skill matching

Match percentage with progress bar

Highlight matched and missing skills

AI-powered improvement suggestions

Downloadable resume analysis report

Modular Python project structure

Easy to use Streamlit web interface

Architecture:

Resume Analyzer Architecture

User → Streamlit UI → PDF Processing → Skill Matching Engine → AI Suggestions → Report Generation

Tech Stack:
Frontend

Streamlit (Python-based UI framework)

Backend

Python 3.x

PyPDF2 (PDF text extraction)

Modular Python files (utils, processing, reporting)

Quick Start:
Project Setup
git clone <your-github-repo-link>
cd Resumes
pip install -r requirements.txt

Run the Application
streamlit run app.py


App runs at:
http://localhost:8501

Project Structure:
Resumes/
├── app.py                
├── pdf_processing.py     
├── utils.py               
├── report.py             
├── uploads/              
├── requirements.txt      
├── resume-sample-1.pdf
├── resume-sample-2.pdf
├── ...
└── README.md
