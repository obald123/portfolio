import streamlit as st

# Set page title and icon
st.set_page_config(page_title="My Portfolio", page_icon="🎓")

# Custom CSS for animations and effects
st.markdown("""
    <style>
    .fade-in {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .hover-effect:hover {
        transform: scale(1.05);
        transition: transform 0.2s;
    }
    .scroll-animation {
        animation: scrollIn 1s ease-in-out;
    }
    @keyframes scrollIn {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Settings", "Contact"])

# Home section
if page == "Home":
    st.title("🎓 Student Portfolio")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    # Profile image
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="Uploaded image")
    else:
        st.image("person.png", width=150, caption="Default image")

    # Student details (Editable!)
    name = st.text_input("Name: ", "simugomwa obald")
    location = st.text_input("Location: ", "kigali, gasabo, kimihurura,Rwanda")
    field_of_study = st.text_input("Field of Study: ", "BSc Computer Science, SWE")
    university = st.text_input("University: ", "INES - Ruhengeri")

    st.write(f"📍{location}")
    st.write(f"📚{field_of_study}")
    st.write(f"🎓{university}")

    # Resume download button
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")

    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area("GET TO KNOW ME better:", "my name are simugomwa obald a finalist in BCs in computer science in INES Ruhengeri and i love technology where we come to AI one of the best technologies to be achieved that is why im studying python right now GO # TEAM PYTHON !")
    st.write(about_me)

    st.markdown('</div>', unsafe_allow_html=True)

# Projects section
elif page == "Projects":
    st.title("💻 My Projects")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    with st.expander("📊 Chatting App Project"):
        st.write("A project to build a chatting app using Python and Flask framework where everyone can chat with each other either in a group or individually and can send voice messages as well as images. GIT")

    with st.expander("🤖 Finance Bot"):
        st.write("Developed an AI-Powered finance bot to help users manage their finances and investments. The bot provides real-time stock prices, investment advice, and taxes calculations and payroll.")

    with st.expander("🌐 E-commerce Website"):
        st.write("Designed and Developed a website for an e-commerce business using PHP, JavaScript, HTML, and CSS. The website has features like product search, user authentication, and payment gateway integration.")

    st.markdown('</div>', unsafe_allow_html=True)

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    skill_machinelearning = st.slider("Machine learning & Data science", 0, 100, 90)
    st.progress(skill_machinelearning)
    skill_webdevelop = st.slider("Web development (CSS, HTML, React, Flask)", 0, 100, 90)
    st.progress(skill_webdevelop)
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)
    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    st.subheader("Certifications & Achievements")
    st.write("✔️ Completed Front-end program in ALX")
    st.write("✔️ Completed Machine learning course in Coursera")
    st.write("✔️ Completed Python course in SoloLearn")
    st.write("✔️ Completed Flask course in Udemy")
    st.write("✔️ Certified in debate (2016, iDebate Rwanda)")
    st.write("✔️ Certified in computer hardware repair and maintenance (2021-2023, Projection Technology)")

    st.markdown('</div>', unsafe_allow_html=True)

# Settings section
elif page == "Settings":
    st.title("🎨 Customize your profile")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    st.subheader("Upload a Profile Picture")
    uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150)

    st.subheader("✍️ Edit Personal Info")

    st.markdown('</div>', unsafe_allow_html=True)

# Contact section
elif page == "Contact":
    st.title("📬 Contact Me")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your message")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully")

    st.write("📧 Email: simugomwaobald@gmail.com")
    st.write("[🔗LinkedIn](https://www.linkedin.com/in/simugomwa-obald-4a4402216/)")
    st.write("[📂GitHub](https://github.com/obald123/portfolio.git)")

    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.write("© 2025 Obald Simugomwa")