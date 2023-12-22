import streamlit as st

# Page titles and paths
pages = {
    "Dream Weaver": "pages/gpt.py",
    "Skill Spotlight": "pages/resume.py",
    "Contribution Compass": "pages/github_contributions.py",
}

# Title and instructions
st.title("Your Personal Exploration Toolkit")
st.markdown("Choose your adventure:")

# Buttons for each page
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Weave your Dream"):
        st.rerun()  # Updated for Streamlit compatibility
        st.session_state["page"] = "gpt"

with col2:
    if st.button("Shine your Skills"):
        st.rerun()
        st.session_state["page"] = "resume"

with col3:
    if st.button("Explore your Contributions"):
        st.rerun()
        st.session_state["page"] = "github"

# Page loading based on session state
if "page" in st.session_state:
    st.include(pages[st.session_state["page"]])
