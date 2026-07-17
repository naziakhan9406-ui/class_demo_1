import streamlit as st

# Setup page layout
st.set_page_config(
    page_title="Used Car Insights",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Route to pages inside the subfolders
intro_page = st.Page("introduction/introduction.py", title="Introduction", icon="📖", default=True)
eda_page = st.Page("eda/eda.py", title="Exploratory Data Analysis", icon="📊")
conclusion_page = st.Page("conclusion/conclusion.py", title="Conclusion & Insights", icon="🎯")

# Navigation setup
pg = st.navigation([intro_page, eda_page, conclusion_page])
pg.run()