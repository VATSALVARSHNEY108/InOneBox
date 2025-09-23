import streamlit as st
import os
import json
from datetime import datetime
from PIL import Image
import base64
import psycopg2
from psycopg2.extras import RealDictCursor


def display_connect_page():
    """Display the Connect page with profile and feedback"""
    # Profile page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1>👨‍💻 About Me & Connect</h1>
        <div style="background: linear-gradient(45deg, #a8c8ff, #c4a7ff); 
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                    background-clip: text; font-size: 1.2rem; font-weight: 500;">
            ✨ Learn about me, my work, and let's connect ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Profile Section
    st.markdown("---")
    st.subheader("👨‍💻 My Profile")

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["👤 About Me", "📤 Upload Your Work", "💬 Connect & Feedback"])

    with tab1:
        display_profile_section()

    with tab2:
        display_upload_section()

    with tab3:
        display_contact_section()


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
        - **Languages**: Python, C++ , SQL
        - **ML/AI**: TensorFlow, PyTorch, Scikit-learn, LangChain , LangGraph
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

    # Upload form
    uploaded_files = st.file_uploader(
        "Choose files to upload",
        type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'],
        accept_multiple_files=True,
        help="Upload images in PNG, JPG, JPEG, GIF, BMP, or WebP format"
    )

    if uploaded_files:
        st.subheader(f"📋 {len(uploaded_files)} file(s) ready to upload")

        # Project details
        col1, col2 = st.columns(2)

        with col1:
            project_title = st.text_input("Project Title", placeholder="My Amazing Project")
            project_category = st.selectbox("Category", [
                "Photography", "Digital Art", "UI/UX Design",
                "Web Development", "Graphics", "Other"
            ])

        with col2:
            artist_name = st.text_input("Artist/Creator Name", placeholder="Your Name")
            project_description = st.text_area("Description",
                                               placeholder="Tell us about your project...",
                                               height=100)

        # Preview uploaded files
        st.subheader("🖼️ Preview")
        preview_cols = st.columns(min(len(uploaded_files), 4))

        for i, uploaded_file in enumerate(uploaded_files):
            with preview_cols[i % 4]:
                try:
                    image = Image.open(uploaded_file)
                    st.image(image, caption=uploaded_file.name, use_column_width=True)
                    st.write(f"**Size:** {image.size}")
                    st.write(f"**Format:** {image.format}")
                except Exception as e:
                    st.error(f"Error previewing {uploaded_file.name}: {e}")

        # Upload button
        if st.button("🚀 Add to Portfolio", type="primary"):
            try:
                # Create portfolio directory if it doesn't exist
                portfolio_dir = "attached_assets"
                os.makedirs(portfolio_dir, exist_ok=True)

                uploaded_count = 0
                for uploaded_file in uploaded_files:
                    # Save file
                    file_path = os.path.join(portfolio_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    uploaded_count += 1

                # Create metadata file
                metadata = {
                    "upload_date": datetime.now().isoformat(),
                    "project_title": project_title,
                    "category": project_category,
                    "artist_name": artist_name,
                    "description": project_description,
                    "files": [f.name for f in uploaded_files]
                }

                metadata_path = os.path.join(portfolio_dir, f"metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                with open(metadata_path, 'w') as f:
                    json.dump(metadata, f, indent=2)

                st.success(f"✅ Successfully uploaded {uploaded_count} file(s) to portfolio!")
                st.balloons()

                # Show upload summary
                with st.expander("📋 Upload Summary"):
                    st.json(metadata)

            except Exception as e:
                st.error(f"Error uploading files: {e}")

    else:
        st.info("👆 Choose files above to get started")

        # Upload guidelines
        st.markdown("### 📝 Upload Guidelines")
        st.markdown("""
        - **File Format:** PNG, JPG, JPEG, GIF, BMP, WebP
        - **File Size:** Maximum 10MB per file
        - **Quality:** High resolution images work best
        - **Content:** Original work or properly attributed content only
        - **Categories:** Choose the most appropriate category for your work
        """)


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


