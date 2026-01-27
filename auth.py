import streamlit as st

# Simple users database (you can change usernames/passwords)
users = {
    "student": "stu123",
    "priya": "priya123"
}

def login():
    # LOGIN PAGE CSS - Clean, attractive, legible dark letters
    st.markdown("""
    <style>
    /* Clean light background for login page */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #f1f5f9 100%);
        min-height: 100vh;
    }
    
    /* Hide sidebar on login page */
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    /* Main title - dark, bold, legible */
    h1 {
        color: #1e293b !important;
        font-weight: 800 !important;
        font-size: 2.5rem !important;
        text-align: center !important;
        margin-bottom: 10px !important;
        letter-spacing: -0.5px !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Subheadings - dark and clear */
    h2, h3, h4, h5, h6 {
        color: #334155 !important;
        font-weight: 600 !important;
    }
    
    /* All text - dark, legible */
    label, p, span, div {
        color: #374151 !important;
        font-weight: 500 !important;
    }
    
    /* Input labels - prominent dark text */
    div[data-testid="stTextInput"] label {
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 8px !important;
    }
    
    /* Input fields - clean white with dark text */
    input, textarea {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border: 2px solid #cbd5e1 !important;
        border-radius: 12px !important;
        padding: 14px 16px !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
        transition: all 0.2s ease !important;
    }
    
    input::placeholder, textarea::placeholder {
        color: #9ca3af !important;
        font-weight: 400 !important;
    }
    
    input:focus, textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15), 0 2px 8px rgba(0, 0, 0, 0.08) !important;
        outline: none !important;
    }
    
    /* Login button - attractive blue gradient */
    div.stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 32px !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        width: 100% !important;
        margin-top: 12px !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35) !important;
        transition: all 0.25s ease !important;
        cursor: pointer !important;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%) !important;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.45) !important;
        transform: translateY(-2px) !important;
    }
    
    div.stButton > button:active {
        transform: translateY(0) !important;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3) !important;
    }
    
    /* Success message - clean green */
    div[data-testid="stAlert"][data-baseweb="notification"],
    div.stAlert {
        background-color: #ecfdf5 !important;
        color: #065f46 !important;
        border: 1px solid #10b981 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }
    
    /* Error message - clean red */
    div.stAlert-error,
    div[role="alert"] {
        background-color: #fef2f2 !important;
        color: #991b1b !important;
        border: 1px solid #ef4444 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }
    
    /* Form container styling */
    div[data-testid="stVerticalBlock"] {
        max-width: 420px !important;
        margin: 0 auto !important;
        padding: 40px 30px !important;
        background: #ffffff !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08), 0 0 0 1px rgba(0, 0, 0, 0.02) !important;
    }
    
    /* Add decorative header */
    div[data-testid="stVerticalBlock"]::before {
        content: "" !important;
        display: block !important;
        width: 60px !important;
        height: 60px !important;
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important;
        border-radius: 16px !important;
        margin: 0 auto 20px auto !important;
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.35) !important;
    }
    
    /* Password visibility toggle */
    button[data-testid="passwordVisibilityToggle"] {
        background: transparent !important;
        color: #64748b !important;
    }
    
    button[data-testid="passwordVisibilityToggle"]:hover {
        color: #3b82f6 !important;
    }
    
    /* Footer text styling */
    small, .caption {
        color: #64748b !important;
        font-weight: 400 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Welcome ")
    st.markdown("<p style='text-align: center; color: #64748b !important; margin-top: -10px; margin-bottom: 30px; font-size: 1rem;'>Sign in to access your account</p>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.success("Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid username or password")
    
    st.markdown("<p style='text-align: center; color: #94a3b8 !important; margin-top: 20px; font-size: 0.85rem;'>Demo: student / stu123</p>", unsafe_allow_html=True)


def logout():
    st.session_state["logged_in"] = False
    st.rerun()
