import streamlit as st
from auth import login, logout
from pdf_processing import extract_text_from_pdf
from utils import suggest_skills, match_skills, get_companies, send_selection_email
from report import generate_report
# ---------------- LOGIN SYSTEM ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    login()
    st.stop()
else:
    st.sidebar.success("Logged in")
    if st.sidebar.button("Logout"):
        logout()

if "show_apply_form" not in st.session_state:
    st.session_state.show_apply_form = False

if "selected_company" not in st.session_state:
    st.session_state.selected_company = ""

if "qualified" not in st.session_state:
    st.session_state.qualified = False

if "qualified_companies" not in st.session_state:
    st.session_state.qualified_companies = []

if "qualified_role" not in st.session_state:
    st.session_state.qualified_role = ""

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = []

# ---------------- CSS DESIGN ----------------
st.markdown("""
<style>
/* App background - premium dark gradient */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}
/* Title */
h1 {
    color: #f1f5f9 !important;
    font-weight: 700;
    letter-spacing: -0.5px;
}
/* Headings */
h2, h3, h4, h5, h6 {
    color: #e2e8f0 !important;
    font-weight: 600;
}
/* All normal text - strong light contrast */
label, p, span, div, li, td, th {
    color: #e2e8f0 !important;
}
/* Inputs, textarea */
input, textarea {
    background-color: #1e293b !important;
    color: #f1f5f9 !important;
    border: 1px solid #475569 !important;
    border-radius: 8px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;
}
input::placeholder, textarea::placeholder {
    color: #94a3b8 !important;
}
input:focus, textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25) !important;
}
/* SELECTBOX / DROPDOWN - FIXED FOR VISIBILITY */
div[data-baseweb="select"],
div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    color: #f1f5f9 !important;
    border: 1px solid #475569 !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] span,
div[data-baseweb="select"] div {
    color: #f1f5f9 !important;
}
/* Dropdown arrow icon */
div[data-baseweb="select"] svg {
    fill: #f1f5f9 !important;
}
/* DROPDOWN LIST - HIGHLY VISIBLE */
ul[role="listbox"],
div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="menu"] {
    background-color: #1e293b !important;
    border: 1px solid #475569 !important;
    border-radius: 8px !important;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5) !important;
    z-index: 9999 !important;
}
ul[role="listbox"] li,
div[data-baseweb="menu"] li,
li[role="option"] {
    background-color: #1e293b !important;
    color: #f1f5f9 !important;
}
ul[role="listbox"] li:hover,
div[data-baseweb="menu"] li:hover,
li[role="option"]:hover {
    background-color: #334155 !important;
    color: #ffffff !important;
}
li[aria-selected="true"] {
    background-color: #1e40af !important;
    color: #ffffff !important;
}
ul[role="listbox"] li span,
ul[role="listbox"] li div,
li[role="option"] span,
li[role="option"] div {
    color: #f1f5f9 !important;
}
/* FILE UPLOADER - UPLOAD RESUME */
section[data-testid="stFileUploader"],
div[data-testid="stFileUploader"] {
    background-color: #1e293b !important;
    border: 2px dashed #475569 !important;
    border-radius: 12px !important;
    padding: 20px !important;
}
section[data-testid="stFileUploader"] *,
div[data-testid="stFileUploader"] *,
section[data-testid="stFileUploader"] label,
section[data-testid="stFileUploader"] span,
section[data-testid="stFileUploader"] p,
section[data-testid="stFileUploader"] div,
section[data-testid="stFileUploader"] small {
    color: #e2e8f0 !important;
}
/* Uploaded file name */
div[data-testid="stFileUploaderFile"] {
    background-color: #334155 !important;
    border-radius: 8px !important;
}
div[data-testid="stFileUploaderFile"] span,
div[data-testid="stFileUploaderFile"] div {
    color: #f1f5f9 !important;
}
/* EXPANDER - MATCH SKILLS / AI SUGGESTIONS - ATTRACTIVE BUBBLE STYLE */
div[data-testid="stExpander"],
details {
    background: linear-gradient(145deg, #1e1e2e 0%, #2d2d44 50%, #1e1e2e 100%) !important;
    border: 2px solid transparent !important;
    border-radius: 20px !important;
    box-shadow: 
        0 8px 32px rgba(139, 92, 246, 0.15),
        0 0 0 1px rgba(139, 92, 246, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
    padding: 4px !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stExpander"]:hover,
details:hover {
    box-shadow: 
        0 12px 40px rgba(139, 92, 246, 0.25),
        0 0 0 2px rgba(139, 92, 246, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    transform: translateY(-2px) !important;
}
div[data-testid="stExpander"]::before,
details::before {
    content: "" !important;
    position: absolute !important;
    top: -50% !important;
    left: -50% !important;
    width: 200% !important;
    height: 200% !important;
    background: conic-gradient(
        from 0deg,
        transparent,
        rgba(139, 92, 246, 0.1),
        transparent,
        rgba(236, 72, 153, 0.1),
        transparent
    ) !important;
    animation: rotate-gradient 6s linear infinite !important;
    z-index: -1 !important;
}
@keyframes rotate-gradient {
    100% { transform: rotate(360deg); }
}
div[data-testid="stExpander"] *,
details *,
summary,
summary span {
    color: #f1f5f9 !important;
}
div[data-testid="stExpander"] summary,
details summary {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(236, 72, 153, 0.15) 100%) !important;
    border-radius: 16px !important;
    padding: 16px 20px !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stExpander"] summary:hover,
details summary:hover {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.3) 0%, rgba(236, 72, 153, 0.25) 100%) !important;
}
/* MARKDOWN / TEXT BLOCKS - AI SUGGESTIONS - BUBBLE STYLE */
div[data-testid="stMarkdown"] {
    background: linear-gradient(145deg, rgba(6, 182, 212, 0.08) 0%, rgba(34, 211, 238, 0.05) 100%) !important;
    border: 1px solid rgba(6, 182, 212, 0.2) !important;
    border-radius: 16px !important;
    padding: 16px 20px !important;
    margin: 8px 0 !important;
    box-shadow: 
        0 4px 20px rgba(6, 182, 212, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
    position: relative !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stMarkdown"]:hover {
    border-color: rgba(6, 182, 212, 0.4) !important;
    box-shadow: 
        0 6px 28px rgba(6, 182, 212, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
}
div[data-testid="stMarkdown"]::before {
    content: "" !important;
    position: absolute !important;
    top: 10px !important;
    left: 10px !important;
    width: 8px !important;
    height: 8px !important;
    background: linear-gradient(135deg, #06b6d4, #22d3ee) !important;
    border-radius: 50% !important;
    box-shadow: 0 0 10px rgba(6, 182, 212, 0.5) !important;
}
div[data-testid="stMarkdown"] p,
div[data-testid="stMarkdown"] span,
div[data-testid="stMarkdown"] li {
    color: #e2e8f0 !important;
    line-height: 1.7 !important;
}
div[data-testid="stMarkdown"] code {
    color: #22d3ee !important;
    background-color: rgba(6, 182, 212, 0.15) !important;
    padding: 2px 8px !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
}
/* Code blocks */
div[data-testid="stMarkdown"] pre,
pre, code {
    background: linear-gradient(135deg, #0c1222 0%, #162032 100%) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(6, 182, 212, 0.2) !important;
    border-radius: 12px !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
}
/* TEXT AREA - Skills input */
div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    background-color: #1e293b !important;
    color: #f1f5f9 !important;
    border: 1px solid #475569 !important;
    border-radius: 8px !important;
}
div[data-testid="stTextArea"] label,
div[data-testid="stTextInput"] label {
    color: #e2e8f0 !important;
}
/* CONTAINER / CARD BLOCKS */
div[data-testid="stVerticalBlock"] > div,
div[data-testid="stHorizontalBlock"] > div {
    color: #e2e8f0 !important;
}
/* METRIC DISPLAY */
div[data-testid="stMetric"],
div[data-testid="stMetric"] label,
div[data-testid="stMetric"] div {
    color: #e2e8f0 !important;
}
div[data-testid="stMetricValue"] {
    color: #f1f5f9 !important;
}
/* DATAFRAME / TABLE */
div[data-testid="stDataFrame"],
div[data-testid="stTable"] {
    background-color: #1e293b !important;
}
div[data-testid="stDataFrame"] *,
div[data-testid="stTable"] * {
    color: #e2e8f0 !important;
}
/* JSON display */
div[data-testid="stJson"] {
    background-color: #1e293b !important;
}
div[data-testid="stJson"] * {
    color: #e2e8f0 !important;
}
/* MULTISELECT - MATCH SKILLS - ATTRACTIVE BUBBLE TAGS */
div[data-baseweb="tag"] {
    background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 50%, #ec4899 100%) !important;
    color: #ffffff !important;
    border-radius: 20px !important;
    padding: 6px 14px !important;
    font-weight: 600 !important;
    box-shadow: 
        0 4px 14px rgba(139, 92, 246, 0.4),
        inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    border: none !important;
    transition: all 0.2s ease !important;
}
div[data-baseweb="tag"]:hover {
    transform: scale(1.05) !important;
    box-shadow: 
        0 6px 20px rgba(139, 92, 246, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
}
div[data-baseweb="tag"] span {
    color: #ffffff !important;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) !important;
}
/* Tag close button */
div[data-baseweb="tag"] svg {
    fill: #ffffff !important;
    opacity: 0.8 !important;
    transition: opacity 0.2s ease !important;
}
div[data-baseweb="tag"] svg:hover {
    opacity: 1 !important;
}
/* Multiselect dropdown container */
div[data-baseweb="select"] input {
    background-color: #1e293b !important;
    color: #f1f5f9 !important;
}
/* Buttons - elegant premium dark style */
div.stButton > button,
button[kind="primary"],
button[kind="secondary"] {
    background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
    color: #ffffff !important;
    border-radius: 8px;
    padding: 12px 28px;
    font-weight: 600;
    border: none;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    transition: all 0.2s ease;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
    transform: translateY(-1px);
}
/* Download button */
div.stDownloadButton > button {
    background: linear-gradient(135deg, #059669 0%, #10b981 100%);
    color: #ffffff !important;
}
/* Progress bar */
div[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    border-radius: 4px;
}
/* Spinner */
div[data-testid="stSpinner"] * {
    color: #e2e8f0 !important;
}
/* Sidebar - refined premium dark look */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    border-right: 1px solid #334155;
}
section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}
/* Success alert */
div[data-testid="stAlert"][data-baseweb="notification"],
div.stAlert-success,
div[role="alert"] {
    background-color: #064e3b !important;
    color: #a7f3d0 !important;
    border: 1px solid #10b981 !important;
    border-radius: 8px !important;
}
/* Error alert */
div.stAlert-error {
    background-color: #7f1d1d !important;
    color: #fecaca !important;
    border: 1px solid #ef4444 !important;
    border-radius: 8px !important;
}
/* Info alert */
div.stAlert-info {
    background-color: #1e3a5f !important;
    color: #bfdbfe !important;
    border: 1px solid #3b82f6 !important;
    border-radius: 8px !important;
}
/* Warning alert */
div.stAlert-warning {
    background-color: #78350f !important;
    color: #fde68a !important;
    border: 1px solid #f59e0b !important;
    border-radius: 8px !important;
}
/* Tabs */
div[data-baseweb="tab-list"] {
    background-color: #0f172a !important;
    border-radius: 8px !important;
}
button[data-baseweb="tab"] {
    color: #e2e8f0 !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #1e293b !important;
    color: #3b82f6 !important;
}
/* Checkbox and Radio */
div[data-testid="stCheckbox"] label,
div[data-testid="stRadio"] label {
    color: #e2e8f0 !important;
}
/* Slider */
div[data-testid="stSlider"] label,
div[data-testid="stSlider"] div {
    color: #e2e8f0 !important;
}
/* Caption and small text */
small, .caption, figcaption {
    color: #94a3b8 !important;
}
            
/* Apply Form Box */
.apply-box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    border: 2px solid #3b82f6;
    margin-top: 20px;
}

/* Apply title */
.apply-title {
    font-size: 22px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 10px;
}

/* Apply success text */
.apply-success {
    color: lightgreen;
    font-weight: bold;
}

            
</style>
""", unsafe_allow_html=True)

# ---------------- APP UI ----------------
st.title("Resume Screening & Skill Matching")
job_skills_dict = {
    "Data Analyst": ["python", "sql", "excel", "communication", "machine learning"],
    "Full Stack Developer": ["python", "javascript", "html", "css", "react"],
    "Machine Learning Engineer": ["python", "machine learning", "tensorflow", "sql"],
    "Web Developer": ["html", "css", "javascript", "react", "python"],
    "Python Developer": ["python", "sql", "machine learning", "data science"]
}
skills_list = [
    "python", "java", "c++", "machine learning", "data science",
    "html", "css", "javascript", "sql", "mongodb", "react",
    "excel", "communication", "tensorflow"
]
selected_role = st.selectbox("Select Job Role", list(job_skills_dict.keys()))
companies = get_companies(selected_role)
st.subheader("Companies Hiring")
for company in companies:
    st.write(f"• {company}")
uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)
user_email = st.text_input("Enter your Email (to receive selection mail)")
if st.button("Analyze Resumes"):
    if not uploaded_files:
        st.warning("Please upload at least one resume")
    else:
        st.session_state.analysis_results = []
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            found, matched, percent = match_skills(
                text,
                skills_list,
                job_skills_dict[selected_role]
            )
            # Store results in session state
            result = {
                "file_name": file.name,
                "percent": percent,
                "matched": matched,
                "found": found,
                "suggestions": suggest_skills(selected_role),
                "companies": companies,
                "role": selected_role
            }
            st.session_state.analysis_results.append(result)
            
            # Send mail if selected
            if percent >= 50 and user_email:
                try:
                    send_selection_email(user_email, selected_role)
                except Exception as e:
                    pass
            
            # Store qualification info
            if percent >= 50:
                st.session_state.qualified = True
                st.session_state.qualified_companies = companies
                st.session_state.qualified_role = selected_role
        
        st.session_state.analysis_done = True
        st.rerun()

# ============== DISPLAY ANALYSIS RESULTS ==============
if st.session_state.analysis_done and st.session_state.analysis_results:
    for result in st.session_state.analysis_results:
        st.subheader(f"{result['file_name']} → {result['percent']:.1f}% Match")
        st.progress(int(result['percent']))
        
        st.subheader("Matched Skills")
        for skill in result['matched']:
            st.write(f"• {skill}")

        st.subheader("Missing Skills")
        for skill in [s for s in result['found'] if s not in result['matched']]:
            st.write(f"• {skill}")

        st.subheader("Suggestions")
        for s in result['suggestions']:
            st.write(f"- {s}")
        
        report_text = generate_report(
            result['file_name'],
            result['role'],
            result['percent'],
            result['matched'],
            [s for s in result['found'] if s not in result['matched']],
            result['suggestions'],
            result['companies']
        )
        
        st.subheader("Recommended Companies")
        for c in result['companies']:
            st.markdown(
                f'<span style="background: linear-gradient(to right, #2193b0, #6dd5ed); color:black; padding:5px 8px; margin:2px; border-radius:8px;">{c}</span>',
                unsafe_allow_html=True
            )
        
        st.download_button(
            "Download Report",
            report_text,
            file_name=f"{result['file_name']}_report.txt",
            key=f"download_{result['file_name']}"
        )
        
        st.markdown("---")
        
        # ============== APPLY NOW BUTTON (ONLY IF >= 50% MATCH) ==============
        if result['percent'] >= 50:
            st.success(f"Great match! You qualify to apply for {result['role']} positions.")
            
            st.subheader("Apply Now")
            cols = st.columns(len(result['companies']))
            for idx, company in enumerate(result['companies']):
                with cols[idx]:
                    if st.button(f"Apply - {company}", key=f"apply_{result['file_name']}_{company}"):
                        st.session_state.show_apply_form = True
                        st.session_state.selected_company = company
                        st.rerun()
        
        st.markdown("---")


# ============== APPLICATION FORM (SHOWS WHEN APPLY BUTTON CLICKED) ==============
if st.session_state.show_apply_form:
    st.markdown(f'<div class="apply-title">Apply to {st.session_state.selected_company}</div>', unsafe_allow_html=True)

    with st.form("application_form", clear_on_submit=True):
        st.markdown('<div class="apply-box">', unsafe_allow_html=True)

        full_name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        phone = st.text_input("Phone Number *")
        experience = st.text_input("Years of Experience *")
        current_company = st.text_input("Current Company (Optional)")
        linkedin = st.text_input("LinkedIn Profile (Optional)")
        cover_letter = st.text_area("Cover Letter (Optional)")

        st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button("Submit Application")
        with col2:
            cancel = st.form_submit_button("Cancel")

        if submit:
            if full_name and email and phone and experience:
                st.success(f"Application submitted successfully to {st.session_state.selected_company}!")
                st.session_state.show_apply_form = False
                st.session_state.selected_company = ""
                st.rerun()
            else:
                st.warning("Please fill all required fields marked with *")

        if cancel:
            st.session_state.show_apply_form = False
            st.session_state.selected_company = ""
            st.rerun()
