import streamlit as st
from pdf_processing import extract_text_from_pdf
from utils import suggest_skills, match_skills, get_companies, send_selection_email
from report import generate_report

st.title("📄 Resume Screening & AI Suggestions App")

# Job skills dictionary
job_skills_dict = {
    "Data Analyst": ["python", "sql", "excel", "communication", "machine learning"],
    "Full Stack Developer": ["python", "javascript", "html", "css", "react"],
    "Machine Learning Engineer": ["python", "machine learning", "tensorflow", "sql"],
    "Web Developer": ["html", "css", "javascript", "react", "python"],
    "Python Developer": ["python", "sql", "machine learning", "data science"]
}

# List of skills to check in resumes
skills_list = [
    "python", "java", "c++", "machine learning", "data science",
    "html", "css", "javascript", "sql", "mongodb", "react",
    "excel", "communication", "tensorflow"
]

# 1️⃣ Select Job Role
selected_role = st.selectbox("Select Job Role", list(job_skills_dict.keys()))

# 2️⃣ Show Companies hiring for this role
companies = get_companies(selected_role)
st.subheader("🏢 Companies Hiring for this Role")
for company in companies:
    st.write(f"• {company}")

# 3️⃣ Upload Resumes
uploaded_files = st.file_uploader(
    "Upload Resume PDFs", type=["pdf"], accept_multiple_files=True
)

# 4️⃣ Analyze Resumes Button
if st.button("Analyze Resumes"):
    if not uploaded_files:
        st.warning("Please upload at least one resume")
    else:
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            found, matched, percent = match_skills(text, skills_list, job_skills_dict[selected_role])

            st.subheader(f"{file.name} → {percent:.1f}% Match")
            st.progress(int(percent))

            # Send email if match >= 50%
            if percent >= 50:
                user_email = "candidate@example.com"  # Replace or extract from resume
                try:
                    send_selection_email(user_email, selected_role)
                    st.success(f"📧 Selection email sent to {user_email}!")
                except Exception as e:
                    st.error(f"❌ Could not send email: {e}")

            # Skill badges
            st.write("✅ Matched Skills:")
            for skill in matched:
                st.markdown(f'<span style="background-color:#1e90ff;color:white;padding:5px 10px;margin:2px;border-radius:10px;">{skill}</span>', unsafe_allow_html=True)

            st.write("🔴 Missing/Other Skills:")
            for skill in [s for s in found if s not in matched]:
                st.markdown(f'<span style="background-color:#ff6f61;color:white;padding:5px 10px;margin:2px;border-radius:10px;">{skill}</span>', unsafe_allow_html=True)

            # AI Suggestions
            st.subheader("💡 AI Suggestions")
            suggestions = suggest_skills(selected_role)
            for s in suggestions:
                st.markdown(f'<span style="background-color:#87cefa;color:black;padding:5px 8px;margin:2px;border-radius:8px;">{s}</span>', unsafe_allow_html=True)

            # Recommended Companies
            st.subheader("🏢 Recommended Companies")
            for c in companies:
                st.markdown(f'<span style="background-color:#90ee90;color:black;padding:5px 8px;margin:2px;border-radius:8px;">{c}</span>', unsafe_allow_html=True)

            # Download report
            report_text = generate_report(
                file.name,
                selected_role,
                percent,
                matched,
                [s for s in found if s not in matched],
                suggestions,
                companies
            )
            st.download_button("⬇ Download Report", report_text, file_name=f"{file.name}_report.txt")
            st.markdown("---")
