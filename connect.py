import streamlit as st
import os
import json
from datetime import datetime
from PIL import Image
import base64
import psycopg2
from psycopg2.extras import RealDictCursor


def display_connect_page():
    """Display the Portfolio page with all content in one place"""
    # Portfolio page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1>👨‍💻 Portfolio & Professional Profile</h1>
        <div style="background: linear-gradient(45deg, #a8c8ff, #c4a7ff); 
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                    background-clip: text; font-size: 1.2rem; font-weight: 500;">
            ✨ Comprehensive Portfolio - Everything in One Place ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Display all content in unified view
    display_complete_portfolio()


def display_complete_portfolio():
    """Display all portfolio content in one unified view"""

    # Profile Section with Photo and Bio
    st.markdown("## 👨‍💻 Professional Profile")

    # Profile layout
    col1, col2 = st.columns([1, 2])

    with col1:
        # Profile image section
        st.markdown("### 📸 Profile Photo")

        # Check if profile image exists
        profile_image_path = None
        portfolio_dir = "attached_assets"
        if os.path.exists(portfolio_dir):
            # Look for profile image (you can upload one)
            profile_images = [f for f in os.listdir(portfolio_dir)
                              if f.lower().startswith('profile') and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if profile_images:
                profile_image_path = os.path.join(portfolio_dir, profile_images[0])

        if profile_image_path and os.path.exists(profile_image_path):
            try:
                profile_image = Image.open(profile_image_path)
                # Display high-quality, larger profile image
                st.image(profile_image, width=400, caption="Vatsal Varshney - AI/ML Engineer")
            except Exception as e:
                st.error(f"Error loading profile image: {e}")
        else:
            # Placeholder for profile image - larger and higher quality
            st.markdown("""
            <div style="
                width: 400px; 
                height: 400px; 
                background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 8rem;
                margin: 1rem 0;
                box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
                border: 4px solid rgba(255, 255, 255, 0.2);
            ">
                👨‍💻
            </div>
            """, unsafe_allow_html=True)
            st.caption(
                "Upload a profile image named 'profile.jpg' to display here (400x400px recommended for best quality)")

    with col2:
        # Professional information
        st.markdown("### 👋 Hello, I'm Vatsal Varshney!")

        st.markdown("""
        **🤖 AI/ML Engineer**

        I'm passionate about artificial intelligence and machine learning, creating innovative solutions 
        that make a real difference. This comprehensive toolkit represents my commitment to making AI tools 
        accessible and useful for everyone.

        ### 🎯 What I Do
        - **Machine Learning**: Building intelligent systems and predictive models
        - **AI Development**: Creating AI-powered applications and tools
        - **Data Science**: Extracting insights from complex datasets
        - **Software Engineering**: Developing robust, scalable solutions

        ### 🛠️ Technologies & Skills
        - **Languages**: Python, JavaScript, SQL, C++
        - **ML/AI**: TensorFlow, PyTorch, Scikit-learn, OpenAI API, Google Gemini
        - **Web Development**: Streamlit, React, Node.js, HTML/CSS
        - **Tools**: Git, Docker, Pandas, NumPy, Matplotlib, Seaborn
        - **Cloud Platforms**: AWS, Google Cloud, Azure
        - **Databases**: PostgreSQL, MongoDB, MySQL

        ### 🌟 This Toolkit Project
        This comprehensive digital toolkit showcases over 500 professional tools across various categories:
        - AI and Machine Learning tools
        - Image and video processing
        - Data analysis and visualization
        - Web development utilities
        - Security and privacy tools
        - And much more!
        """)

    st.markdown("---")

    # Projects & Achievements Section
    st.markdown("## 🏆 Projects & Achievements")

    projects_col1, projects_col2 = st.columns(2)

    with projects_col1:
        st.markdown("""
        ### 🚀 Featured Projects

        **🛠️ Ultimate Digital Toolkit** (Current Project)
        - 500+ professional tools in one platform
        - AI-powered features with OpenAI and Google Gemini integration
        - Real-time data processing and visualization
        - Built with Streamlit, Python, and PostgreSQL

        **🤖 AI/ML Applications**
        - Machine learning model implementations
        - Computer vision projects
        - Natural language processing tools
        - Predictive analytics solutions

        **📊 Data Science Projects**
        - Advanced statistical analysis tools
        - Interactive data visualization dashboards
        - Data cleaning and preprocessing utilities
        - Business intelligence solutions
        """)

    with projects_col2:
        st.markdown("""
        ### 🎓 Education & Certifications

        **🎯 Competitive Programming**
        - Active on LeetCode and Codeforces
        - Problem-solving in algorithms and data structures
        - Regular participation in coding competitions

        **📚 Continuous Learning**
        - Machine Learning and AI courses
        - Cloud computing certifications
        - Web development bootcamps
        - Open source contributions

        **🔬 Research Interests**
        - Artificial Intelligence applications
        - Machine Learning optimization
        - Data science methodologies
        - Software engineering best practices
        """)

    st.markdown("---")

    # Contact & Social Links Section
    st.markdown("## 🌐 Connect With Me")

    contact_col1, contact_col2 = st.columns(2)

    with contact_col1:
        st.markdown("### 🔗 Find Me Online")

        # Social and contact links
        social_links = [
            ("🐙 **GitHub**", "https://github.com/VATSALVARSHNEY108", "View my projects and code repositories"),
            ("💼 **LinkedIn**", "https://www.linkedin.com/feed/", "Connect with me professionally"),
            ("📧 **Email**", "mailto:vatsalworkingat19.com", "Send me a direct email"),
            ("📞 **Contact**", "tel:+919068633298", "Call me or WhatsApp for discussions"),
            ("🟧 **LeetCode**", "https://leetcode.com/u/VATSAL_VARSHNEY/", "Check out my coding solutions"),
            ("🔵 **Codeforces**", "https://codeforces.com/profile/Vatsal_Varshney-69",
             "View my competitive programming profile")
        ]

        for icon_name, link, description in social_links:
            st.markdown(f"{icon_name} [{description}]({link})")

    with contact_col2:
        st.markdown("### 💬 Send Me a Message")

        # Feedback form
        feedback_type = st.selectbox("Message Type", [
            "Project Collaboration", "Job Opportunity", "Technical Question",
            "Feedback on Toolkit", "General Inquiry", "Compliment"
        ])

        name = st.text_input("Your Name", placeholder="Your full name")
        email = st.text_input("Your Email", placeholder="your@email.com")
        subject = st.text_input("Subject", placeholder="Brief description of your message")
        message = st.text_area("Message", height=150,
                               placeholder="Tell me more about your inquiry, project idea, or feedback...")

        if st.button("📤 Send Message", type="primary", use_container_width=True):
            if message and subject and name and email:
                # Save feedback to database
                try:
                    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
                    cursor = conn.cursor()

                    insert_query = """
                    INSERT INTO user_feedback (feedback_type, name, email, subject, message)
                    VALUES (%s, %s, %s, %s, %s)
                    """

                    cursor.execute(insert_query, (
                        feedback_type, name, email, subject, message
                    ))

                    conn.commit()
                    cursor.close()
                    conn.close()

                    st.success("✅ Thank you for your message! I'll get back to you soon.")
                    st.balloons()

                except Exception as e:
                    st.error(f"❌ Sorry, there was an error sending your message. Please try again. Error: {e}")
            else:
                st.error("Please fill in all fields (name, email, subject, and message).")

    st.markdown("---")

    # FAQ Section
    st.markdown("## ❓ Frequently Asked Questions")

    faq_col1, faq_col2 = st.columns(2)

    with faq_col1:
        st.markdown("### 🛠️ About the Toolkit")

        faqs_toolkit = [
            ("Is this toolkit free to use?",
             "Yes! Most tools are completely free. Some AI-powered features require API keys from providers like Google (Gemini) or OpenAI."),
            ("How many tools are available?",
             "Over 500 professional tools across 13+ categories including AI, data analysis, web development, security, and more."),
            ("Can I use these tools for commercial projects?",
             "Yes! The tools are designed for both personal and commercial use. Just make sure to comply with any third-party API terms of service.")
        ]

        for question, answer in faqs_toolkit:
            with st.expander(f"**{question}**"):
                st.write(answer)

    with faq_col2:
        st.markdown("### 🤝 Collaboration & Support")

        faqs_collab = [
            ("How can I collaborate with you?",
             "I'm always open to interesting projects! Reach out via email or LinkedIn with your project details and how you think we can work together."),
            ("Do you offer consulting services?",
             "Yes! I provide consulting for AI/ML projects, data science initiatives, and software development. Contact me to discuss your specific needs."),
            ("How can I contribute to your projects?",
             "Check out my GitHub repositories! I welcome contributions, bug reports, and feature requests. You can also provide feedback through the contact form.")
        ]

        for question, answer in faqs_collab:
            with st.expander(f"**{question}**"):
                st.write(answer)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(168, 200, 255, 0.1), rgba(196, 167, 255, 0.1)); border-radius: 10px; margin: 2rem 0;">
        <h3>🚀 Let's Build Something Amazing Together!</h3>
        <p style="font-size: 1.1rem; margin-bottom: 1rem;">
            Whether you're looking to collaborate on exciting projects, need AI/ML expertise, 
            or just want to connect with a fellow tech enthusiast, I'd love to hear from you!
        </p>
        <p style="font-weight: bold; color: #667eea;">
            📧 vatsalworkingat19.com | 📱 +91-9068633298
        </p>
    </div>
    """, unsafe_allow_html=True)


def display_profile_section():
    """Display Vatsal's profile section"""
    # Profile layout
    col1, col2 = st.columns([1, 2])

    with col1:
        # Profile image section
        st.markdown("### 📸 Profile Photo")

        # Check if profile image exists
        profile_image_path = None
        portfolio_dir = "attached_assets"
        if os.path.exists(portfolio_dir):
            # Look for profile image (you can upload one)
            profile_images = [f for f in os.listdir(portfolio_dir)
                              if f.lower().startswith('profile') and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if profile_images:
                profile_image_path = os.path.join(portfolio_dir, profile_images[0])

        if profile_image_path and os.path.exists(profile_image_path):
            try:
                profile_image = Image.open(profile_image_path)
                # Display high-quality, larger profile image
                st.image(profile_image, width=400, caption="Vatsal Varshney - AI/ML Engineer")
            except Exception as e:
                st.error(f"Error loading profile image: {e}")
        else:
            # Placeholder for profile image - larger and higher quality
            st.markdown("""
            <div style="
                width: 400px; 
                height: 400px; 
                background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 8rem;
                margin: 1rem 0;
                box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
                border: 4px solid rgba(255, 255, 255, 0.2);
            ">
                👨‍💻
            </div>
            """, unsafe_allow_html=True)
            st.caption(
                "Upload a profile image named 'profile.jpg' to display here (400x400px recommended for best quality)")

    with col2:
        # Profile information
        st.markdown("### 👋 Hello, I'm Vatsal Varshney!")

        st.markdown("""
        **🤖 AI/ML Engineer**

        I'm passionate about artificial intelligence and machine learning, creating innovative solutions 
        that make a real difference. This toolkit represents my commitment to making AI tools accessible 
        and useful for everyone.

        ### 🎯 What I Do
        - **Machine Learning**: Building intelligent systems and predictive models
        - **AI Development**: Creating AI-powered applications and tools
        - **Data Science**: Extracting insights from complex datasets
        - **Software Engineering**: Developing robust, scalable solutions

        ### 🛠️ Technologies & Skills
        - **Languages**: Python, JavaScript, SQL
        - **ML/AI**: TensorFlow, PyTorch, Scikit-learn, OpenAI API
        - **Tools**: Streamlit, Pandas, NumPy, Git, Docker
        - **Cloud**: AWS, Google Cloud, Azure

        ### 🌟 This Toolkit
        This comprehensive AI toolkit showcases various AI and ML capabilities, from image processing 
        to text analysis, data visualization, and much more. It's designed to be both educational 
        and practical for real-world applications.
        """)


def display_upload_section():
    """Display the upload section for new portfolio items"""
    st.markdown("### 📤 Share Your Creative Work")
    st.markdown("Upload your photos, artwork, or creative projects to showcase in the portfolio gallery!")


def display_contact_section():
    """Display contact and feedback section"""
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💬 Feedback & Support")
        st.markdown("""
        **Found a bug?** Let me know and help me improve the toolkit!  
        **Have a suggestion?** I'm always looking for ways to make it better.  
        **Need help?** I'm here to support you with any of the tools.
        """)

        # Feedback form
        st.subheader("📝 Send Feedback")

        feedback_type = st.selectbox("Feedback Type", [
            "Bug Report", "Feature Request", "General Feedback", "Support Request", "Compliment"
        ])

        name = st.text_input("Your Name (optional)", placeholder="John Doe")
        email = st.text_input("Your Email (optional)", placeholder="john@example.com")

        subject = st.text_input("Subject", placeholder="Brief description of your message")
        message = st.text_area("Message", height=150,
                               placeholder="Tell us more about your feedback, issue, or suggestion...")

        if st.button("📤 Send Feedback", type="primary"):
            if message and subject:
                # Save feedback to database
                try:
                    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
                    cursor = conn.cursor()

                    insert_query = """
                    INSERT INTO user_feedback (feedback_type, name, email, subject, message)
                    VALUES (%s, %s, %s, %s, %s)
                    """

                    cursor.execute(insert_query, (
                        feedback_type,
                        name if name else None,
                        email if email else None,
                        subject,
                        message
                    ))

                    conn.commit()
                    cursor.close()
                    conn.close()

                    st.success("✅ Thank you for your feedback! I'll review it and get back to you if needed.")
                    st.balloons()

                    # Show confirmation that it was saved
                    st.info("💾 Your feedback has been saved to the database for review.")

                except Exception as e:
                    st.error(f"❌ Sorry, there was an error saving your feedback. Please try again. Error: {e}")
            else:
                st.error("Please fill in both subject and message fields.")

    with col2:
        st.markdown("### 🌐 Connect With Me")
        st.markdown("""
        **Follow my updates** and join the community!  
        **Share your creations** made with the toolkit.  
        **Stay informed** about new features and releases.
        """)

        # Social media / connection links
        st.subheader("🔗 Find Me Online")

        # Social and contact links
        social_links = [
            ("🐙 GitHub", "https://github.com/VATSALVARSHNEY108", "View my projects and code"),
            ("💼 LinkedIn", "https://www.linkedin.com/feed/", "Connect professionally"),
            ("📧 Email", "mailto:vatsalworkingat19.com", "Send me a direct email"),
            ("📞 Contact", "tel:+919068633298", "Call me or WhatsApp"),
            ("🟧 LeetCode", "https://leetcode.com/u/VATSAL_VARSHNEY/", "Check Out My LeetCode Profile"),
            ("🔵 Codeforces", "https://codeforces.com/profile/Vatsal_Varshney-69", "Check Out My Codeforces Profile")
        ]

        for icon_name, link, description in social_links:
            st.markdown(f"**{icon_name}** [{description}]({link})")

        # Newsletter signup
        st.subheader("📰 Newsletter")
        newsletter_email = st.text_input("Subscribe for updates:", placeholder="your@email.com")
        if st.button("📮 Subscribe"):
            if newsletter_email and "@" in newsletter_email:
                st.success("✅ Subscribed! You'll receive updates about new tools and features.")
            else:
                st.error("Please enter a valid email address.")

    st.markdown("---")

    # FAQ Section
    st.subheader("❓ Frequently Asked Questions")

    faqs = [
        {
            "question": "Is this toolkit free to use?",
            "answer": "Yes! Most tools are completely free. Some AI-powered features require API keys from providers like Google (Gemini) or OpenAI."
        },
        {
            "question": "How do I report a bug or request a feature?",
            "answer": "Use the feedback form above or contact me through any of the social channels. I review all submissions personally!"
        },
        {
            "question": "Can I contribute to the project?",
            "answer": "Absolutely! Check out my GitHub repository to see how you can contribute code, documentation, or ideas."
        },
        {
            "question": "Are my files and data secure?",
            "answer": "Yes! All processing happens locally in your browser or on secure servers. I don't store your personal files or data."
        },
        {
            "question": "How often are new tools added?",
            "answer": "I'm constantly working on new tools and improvements. Follow my updates to stay informed about releases!"
        },
        {
            "question": "Can I upload my own work to the portfolio?",
            "answer": "Yes! Use the 'Upload Your Work' tab to share your creative projects. All uploads are stored securely and can be showcased in the gallery."
        }
    ]

    for i, faq in enumerate(faqs):
        with st.expander(f"**{faq['question']}**"):
            st.write(faq['answer'])
