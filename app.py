import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="GenAI & ML Mastery", layout="wide")

# --- NAVIGATION MENU ---
with st.sidebar:
    choice = option_menu(
        menu_title="Main Menu", # required
        options=["Home", "About the Course", "About Us", "Contact Us"], # Updated to match your content
        icons=['house', 'book', 'info-circle', 'telephone'], # Relevant icons
        menu_icon="cast", # optional
        default_index=0, # optional
        orientation="vertical",
    )

# --- HOME SECTION ---
if choice == "Home":
    st.title("🚀 Master Generative AI & Machine Learning")
    st.subheader("Empowering students to build the future with AI.")
    st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995", width=600) 
    st.write("""
    Welcome to the premier destination for learning AI. 
    From Traditional Machine Learning to the latest in Agentic AI and Image Generation, 
    we provide a comprehensive 4-week journey into the world of Intelligence.
    """)

# --- ABOUT THE COURSE SECTION ---
elif choice == "About the Course":
    st.title("📚 Course Syllabus")
    st.info("Each session is a 2-hour live session designed for hands-on learning.")

    # Week 1
    with st.expander("Week 1: Data Visualization & Foundations"):
        st.write("**Saturday:** Deep Dive into BI Tools like Looker Studio — *Master the art of transforming raw data into high-impact, interactive dashboards.*")
        st.write("**Sunday:** Practical Demo on BI Tools")

    # Week 2
    with st.expander("Week 2: AI in Consulting"):
        st.write("**Saturday:** Generative AI For Consulting along with AI Case Study")
        st.write("**Sunday:** Management Consulting along with Case Study")

    # Week 3
    with st.expander("Week 3: Deep Dive into Gen AI & Traditional ML"):
        st.markdown("""
        **Saturday:** * **Traditional AI:** Supervised/Unsupervised, ML, Clustering, Rule-Based.
        * **AI Strategy:** Where to use (and not use) AI Applications.
        * **Gen AI:** What is it? Different use cases and differences from Traditional AI.
        * **The Market:** Google, OpenAI and many more.
        * **Advanced Topics:** Agentic AI, LLMs, Sentiment Analysis.
        * **Assignment:** Image Generation & Projects.
        
        **Sunday:**
        * **Demo Day:** Showing you Real Gen AI Projects Built in the Industry.
        """)

    # Week 4
    with st.expander("Week 4: Conversational AI & Deployment"):
        st.write("**Saturday:** Introduction to Conversational Agents; How chatbots and voicebots are built; Dialogflow based chatbot and voicebot.")
        st.write("**Sunday:** Enjoy Conversation AI Chatbot Demo with Revision of all the learnings")

# --- ABOUT US SECTION ---
elif choice == "About Us":
    st.title("👥 About Us")
    st.write("""
    We are a team of AI practitioners and educators dedicated to making complex 
    technologies accessible. Our mission is to bridge the gap between theoretical 
    AI concepts and real-world management consulting applications.
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/3208/3208945.png", width=150)

# --- CONTACT US SECTION ---
elif choice == "Contact Us":
    st.title("📩 Register / Contact Us")
    st.write("Please fill out the form below to enroll or ask a question.")
    
    # Using the Google Form URL provided
    google_form_url = "https://forms.gle/8AKAQcA2wxGtNVyc7"
    
    # Embedding the form using an iframe
    st.markdown(f'<iframe src="{google_form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html=True)
