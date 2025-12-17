import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="GenAI & ML Mastery", layout="wide")

# --- NAVIGATION MENU ---
with st.sidebar:
    choice = option_menu(
        menu_title="GenAI & ML Mastery", # required
        options=["Home", "About the Course", "About Us", "FAQs", "Contact Us"], # Updated to match your content
        icons=['house', 'book', 'info-circle', 'question-circle', 'telephone'], # Relevant icons
        menu_icon="cast", # optional
        default_index=0, # optional
        orientation="Horizontal",
    )

# --- HOME SECTION ---
if choice == "Home":
    st.title("🚀 Master Generative AI & Machine Learning")    
  
    st.subheader("Welcome to our Learning Hub")
    st.write("Welcome to the premier destination for mastering the future of technology. At our academy, we believe that Artificial Intelligence is not just a technical skill, but a fundamental shift in how the world operates. Led by industry experts Pramod Gupta (16+ years) and Sahil Pareek (8+ years), we offer an immersive, high-impact learning experience designed to take you from the core principles of Traditional Machine Learning to the cutting edge of Agentic AI and Generative media. Over the course of four intensive weeks, we bridge the gap between complex algorithms and real-world application, ensuring you don't just understand AI—you learn how to build with it.")    
        
    st.subheader("Our Mission")
    st.write("Our mission is to democratize high-end AI education by providing a structured, 4-week roadmap that simplifies the transition from 'Traditional' to 'Generative.' Under the mentorship of Sahil and Pramod, we aim to equip students, consultants, and tech enthusiasts with the practical tools—ranging from Looker Studio for data storytelling to Dialogflow for conversational agents—necessary to thrive in an AI-driven economy. We are committed to turning theoretical concepts into tangible career assets through 2-hour live sessions and hands-on case studies.")
    
    st.subheader("Our Vision")
    st.write("We envision a future where every student has the agency to harness Artificial Intelligence to solve global challenges. By blending the strategic expertise of management consulting with the technical prowess of LLMs and Image/Video Generation, we strive to create a community of innovators who are prepared for the 'Agentic' era of AI. Our goal is to be the global benchmark for practical AI training, fostering a new generation of leaders who lead with intelligence, creativity, and technical excellence.")
    st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995", width=600) 

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
    st.title("👥 Who We Are")
    st.markdown("""
    We are a collective of seasoned **AI practitioners and passionate educators** committed to demystifying the most complex technological frontiers. 
    
    Our core mission is to **bridge the gap** between abstract, theoretical AI frameworks and their practical, high-stakes applications in management consulting. We believe that true mastery of Machine Learning and Generative AI isn't just about understanding the code; it’s about knowing how to leverage these tools to drive strategic value and solve intricate business problems.
    """)

    st.title("Our Trainers")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pramod Gupta")
        st.write("Specialist in Generative AI and Technical Architecture.")
        st.write("16+ years experience in AI/ML, Data Science") 
        st.write("Worked for Google, JP Morgan Chase, Tata Consultancy Services, Aeries Technology, Edelweiss Tokio")  
    with col2:
        st.subheader("Sahil Pareek")
        st.write("Expert in AI Strategy and Management Consulting.")
        st.write("8+ years experience in Management and Consulting") 
        

    st.divider()

    st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c", width=600) # Image of a team/collaboration

# --- FAQ SECTION ---
elif choice == "FAQs":
    st.title("❓ Frequently Asked Questions")
    st.write("Everything you need to know about the GenAI & ML Mastery course.")

    # FAQ 1
    with st.expander("Do I need a technical background or coding skills?"):
        st.write("""
        While a basic understanding of computers is helpful, this course is designed 
        to be accessible. We cover BI tools and Generative AI platforms that 
        allow you to build powerful solutions without writing complex code.
        """)

    # FAQ 2
    with st.expander("What is the duration of the live sessions?"):
        st.write("""
        Every Saturday and Sunday, we host a **2-hour live session**. 
        These sessions are interactive and include both theory and practical demos.
        """)

    # FAQ 3
    with st.expander("Will I work on real-world projects?"):
        st.write("""
        Absolutely. You will build projects involving Sentiment Analysis, 
        Image/Video generation, and even a functional Chatbot using Dialogflow.
        """)

    # FAQ 4
    with st.expander("What are the system requirements?"):
        st.write("""
        All you need is a laptop with a stable internet connection. 
        Most of the tools we use (Looker Studio, Google Colab, Dialogflow) 
        are browser-based and do not require heavy software installation.
        """)

    # FAQ 5
    with st.expander("How do I access the assignments?"):
        st.write("""
        Assignments are shared via our dedicated student portal and WhatsApp group 
        following the Saturday sessions.
        """)

# --- CONTACT US SECTION ---
elif choice == "Contact Us":
    st.title("📩 Register / Contact Us")
    st.write("Please fill out the form below to enroll or ask a question.")
    
    # Using the Google Form URL provided
    google_form_url = "https://forms.gle/8AKAQcA2wxGtNVyc7"
    
    # Embedding the form using an iframe
    st.markdown(f'<iframe src="{google_form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html=True)
