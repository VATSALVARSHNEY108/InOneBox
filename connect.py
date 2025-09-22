import streamlit as st
import os
import json
from datetime import datetime
from PIL import Image
import base64
from tools import ai_tools


def display_connect_page():
    """Display the Connect page as a portfolio with photo gallery"""
    # Portfolio page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1>🎨 My Portfolio & Connect</h1>
        <div style="background: linear-gradient(45deg, #a8c8ff, #c4a7ff); 
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                    background-clip: text; font-size: 1.2rem; font-weight: 500;">
            ✨ Explore my work, share your creations, and let's connect ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Portfolio Gallery Section
    st.markdown("---")
    st.subheader("📸 Portfolio Gallery")

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["🖼️ Photo Gallery", "📤 Upload Your Work", "💬 Connect & Feedback"])

    with tab1:
        display_contact_section()
        
    with tab2:
        display_portfolio_gallery()

    with tab3:
        display_upload_section()


def display_portfolio_gallery():
    """Display the portfolio gallery with uploaded photos"""
    st.markdown("### 🎨 Featured Work & Gallery")

    # Portfolio categories
    category = st.selectbox("Browse by category:", [
        "All Works", "Photography", "Digital Art", "UI/UX Design",
        "Web Development", "Graphics", "User Submissions"
    ])

    # Check for uploaded images in attached_assets
    portfolio_dir = "attached_assets"
    if os.path.exists(portfolio_dir):
        image_files = [f for f in os.listdir(portfolio_dir)
                       if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))]

        if image_files:
            st.success(f"📸 Found {len(image_files)} images in portfolio")

            # Display images in a grid
            cols = st.columns(3)
            for i, image_file in enumerate(image_files):
                with cols[i % 3]:
                    try:
                        image_path = os.path.join(portfolio_dir, image_file)
                        image = Image.open(image_path)

                        # Create thumbnail
                        thumbnail = image.copy()
                        thumbnail.thumbnail((300, 300))

                        st.image(thumbnail, caption=image_file, use_column_width=True)

                        # Image details
                        with st.expander(f"Details: {image_file}"):
                            st.write(f"**Filename:** {image_file}")
                            st.write(f"**Size:** {image.size}")
                            st.write(f"**Format:** {image.format}")

                            # Download option
                            with open(image_path, "rb") as file:
                                st.download_button(
                                    f"⬇️ Download {image_file}",
                                    file.read(),
                                    file_name=image_file,
                                    mime="image/png"
                                )
                    except Exception as e:
                        st.error(f"Error loading {image_file}: {e}")
        else:
            st.info("📷 No portfolio images found. Upload some images in the 'Upload Your Work' tab!")
    else:
        st.info("📁 Portfolio directory not found. Upload some images to get started!")

    # Portfolio stats
    if os.path.exists(portfolio_dir):
        total_files = len([f for f in os.listdir(portfolio_dir) if os.path.isfile(os.path.join(portfolio_dir, f))])
        image_count = len([f for f in os.listdir(portfolio_dir)
                           if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Files", total_files)
        with col2:
            st.metric("Images", image_count)
        with col3:
            st.metric("Categories", "6")


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
                # Store feedback (in a real app, you'd send this to a backend)
                st.success("✅ Thank you for your feedback! I'll review it and get back to you if needed.")
                st.balloons()

                # Display what was submitted (for demo purposes)
                with st.expander("📋 Feedback Submitted"):
                    st.write(f"**Type:** {feedback_type}")
                    if name: st.write(f"**Name:** {name}")
                    if email: st.write(f"**Email:** {email}")
                    st.write(f"**Subject:** {subject}")
                    st.write(f"**Message:** {message}")
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
            ("💼 LinkedIn", "https://www.linkedin.com/in/vatsal-varshney108/", "Connect professionally"),
            ("🐦 Twitter", "https://twitter.com/username", "Follow me for updates"),
            ("📧 Email", "vatsalworkingat19@gmail.com", "Send me a direct email"),
            ("📱Mobile Number","9068633298","Contact Me"),
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


