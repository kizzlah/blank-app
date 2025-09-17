

import streamlit as st

st.set_page_config(
    page_title="tech portfolio|k.b. clements",
    page_icon="💻",
    layout="centered"
)

# Inject custom CSS for dark neumorphism and Mono Nerd Font
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400;700&display=swap');
    body, .stApp {
        background: #18181b;
        color: #f8fafc;
        font-family: 'Fira Mono', 'Monospace', 'Nerd Font', monospace;
    }
    .stTitle, .stHeader, .stMarkdown, .stText, .stDownloadButton, .stRadio, .stSidebar, .stButton {
        font-family: 'Fira Mono', 'Monospace', 'Nerd Font', monospace !important;
    }
    .stApp {
        background: linear-gradient(135deg, #18181b 0%, #23234a 100%);
    }
    .block-container {
        background: #23234a;
        border-radius: 24px;
        box-shadow: 8px 8px 24px #10101a, -8px -8px 24px #23234a;
        padding: 2rem;
    }
    .stSidebar {
        background: #18181b;
        color: #f8fafc;
        border-radius: 24px;
        box-shadow: 4px 4px 16px #10101a, -4px -4px 16px #23234a;
    }
    h1, h2, h3, h4 {
        color: #f8fafc;
        text-shadow: 0 2px 8px #23234a;
    }
    a {
        color: #a5b4fc;
    }
    .stDownloadButton>button {
        background: linear-gradient(135deg, #f8fafc 0%, #a5b4fc 100%);
        color: #23234a;
        border-radius: 12px;
        box-shadow: 2px 2px 8px #23234a, -2px -2px 8px #f8fafc;
        font-family: 'Fira Mono', 'Monospace', 'Nerd Font', monospace;
    }
    .stRadio>div {
        background: #23234a;
        border-radius: 12px;
        box-shadow: 2px 2px 8px #10101a, -2px -2px 8px #23234a;
    }
    .stMarkdown {
        color: #f8fafc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("portfolio|k.b. clements")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["About", "Projects", "Skills", "Resume & Contact"],
    index=0
)


if section.lower() == "about":
    st.header("about")
    st.markdown(
        """
        <div style='padding:1.5rem;background:linear-gradient(135deg,#23234a 0%,#a5b4fc 100%);border-radius:32px;box-shadow:0 8px 32px #10101a33;'>
        welcome to my digital portfolio made with streamlit and python.<br>
        here you can find information about my projects, skills, and how to contact me.<br>
        if you get lost just use the arrow at the top left to open the menu bar.
        </div>
        """,
        unsafe_allow_html=True
    )

elif section.lower() == "projects":
    st.header("projects")
    st.markdown(
        """
        <div style='padding:1.5rem;background:linear-gradient(135deg,#23234a 0%,#f8fafc 100%);border-radius:32px;box-shadow:0 8px 32px #10101a22;'>
        <ul style='list-style:none;padding-left:0;'>
        <li style='margin-bottom:1rem;'><span style='color:#f472b6;font-weight:bold;'>Project One</span>: Description of your first project.</li>
        <li style='margin-bottom:1rem;'><span style='color:#a5b4fc;font-weight:bold;'>Project Two</span>: Description of your second project.</li>
        <li><span style='color:#fca5a5;font-weight:bold;'>Project Three</span>: Description of your third project.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

elif section.lower() == "skills":
    st.header("skills")
    st.markdown(
        """
        <div style='padding:1.5rem;background:linear-gradient(135deg,#23234a 0%,#f8fafc 100%);border-radius:32px;box-shadow:0 8px 32px #10101a22;'>
        <ul style='list-style:none;padding-left:0;'>
        <li style='color:#f8fafc;margin-bottom:1rem;'>Python, JavaScript, HTML/CSS</li>
        <li style='color:#a5b4fc;margin-bottom:1rem;'>Streamlit, Flask, React</li>
        <li style='color:#fca5a5;'>Git, Docker, Linux</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

elif section.lower() == "resume & contact":
    st.header("resume & contact")
    st.markdown(
        """
        <div style='padding:1.5rem;background:linear-gradient(135deg,#23234a 0%,#f8fafc 100%);border-radius:32px;box-shadow:0 8px 32px #10101a22;'>
        <div style='margin-bottom:2rem;'>
        <b>Download my resume:</b><br>
        <span style='color:#a5b4fc;'>click the button below to download a PDF of my resume.</span>
        </div>
        <div style='margin-bottom:2rem;'>
        <b>Contact</b><br>
        <span style='color:#f472b6;'>email:</span> www.kizzlah@icloud.com<br>
        <span style='color:#a5b4fc;'>github:</span> <a href='https://github.com/kizzlah' style='color:#a5b4fc;'>github.com/kizzlah</a>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.download_button("Download Resume (PDF)", data=b"", file_name="resume.pdf")
