import streamlit as st
import json
import csv
import io
from datetime import datetime, timedelta
import calendar
import random
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler
from utils.ai_client import ai_client


def display_tools():
    """Display all social media tools"""

    tool_categories = {
        "Content Schedulers": [
            "Multi-Platform Scheduler", "Content Calendar", "Post Optimizer", "Timing Analyzer", "Bulk Scheduler"
        ],
        "Analytics Dashboards": [
            "Engagement Analytics", "Reach Analysis", "Performance Tracker", "Competitor Analysis", "Growth Metrics"
        ],
        "Hashtag Generators": [
            "Hashtag Research", "Trending Hashtags", "Niche Discovery", "Hashtag Analytics", "Tag Optimizer"
        ],
        "Engagement Tools": [
            "Comment Manager", "Follower Analysis", "Interaction Tracker", "Community Builder", "Response Automation"
        ],
        "Multi-Platform Managers": [
            "Cross-Platform Posting", "Unified Dashboard", "Account Manager", "Content Distributor", "Platform Sync"
        ],
        "Content Creation": [
            "Post Generator", "Caption Writer", "Visual Content", "Story Creator", "Video Scripts"
        ],
        "Audience Analysis": [
            "Demographics Analyzer", "Behavior Insights", "Audience Segmentation", "Growth Tracking",
            "Engagement Patterns"
        ],
        "Campaign Management": [
            "Campaign Planner", "A/B Testing", "Performance Monitor", "ROI Tracker", "Campaign Analytics"
        ],
        "Social Listening": [
            "Mention Monitor", "Brand Tracking", "Sentiment Analysis", "Trend Detection", "Competitor Monitoring"
        ],
        "Influencer Tools": [
            "Influencer Finder", "Collaboration Manager", "Performance Tracker", "Outreach Automation", "ROI Calculator"
        ]
    }

    selected_category = st.selectbox("Select Social Media Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Social Media Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Multi-Platform Scheduler":
        multi_platform_scheduler()
    elif selected_tool == "Content Calendar":
        content_calendar()
    elif selected_tool == "Hashtag Research":
        hashtag_research()
    elif selected_tool == "Engagement Analytics":
        engagement_analytics()
    elif selected_tool == "Post Generator":
        post_generator()
    elif selected_tool == "Caption Writer":
        caption_writer()
    elif selected_tool == "Audience Segmentation":
        audience_segmentation()
    elif selected_tool == "Campaign Planner":
        campaign_planner()
    elif selected_tool == "Mention Monitor":
        mention_monitor()
    elif selected_tool == "Influencer Finder":
        influencer_finder()
    elif selected_tool == "Cross-Platform Posting":
        cross_platform_posting()
    elif selected_tool == "Trending Hashtags":
        trending_hashtags()
    elif selected_tool == "Performance Tracker":
        performance_tracker()
    elif selected_tool == "A/B Testing":
        ab_testing()
    elif selected_tool == "Brand Tracking":
        brand_tracking()
    elif selected_tool == "Competitor Monitoring":
        competitor_monitoring()
    elif selected_tool == "Post Optimizer":
        post_optimizer()
    elif selected_tool == "Reach Analysis":
        reach_analysis()
    elif selected_tool == "Comment Manager":
        comment_manager()
    elif selected_tool == "Visual Content":
        visual_content()
    elif selected_tool == "Sentiment Analysis":
        sentiment_analysis()
    elif selected_tool == "Growth Metrics":
        growth_metrics()
    elif selected_tool == "Follower Analysis":
        follower_analysis()
    elif selected_tool == "Timing Analyzer":
        timing_analyzer()
    elif selected_tool == "Bulk Scheduler":
        bulk_scheduler()
    elif selected_tool == "Competitor Analysis":
        competitor_analysis()
    elif selected_tool == "Niche Discovery":
        niche_discovery()
    elif selected_tool == "Hashtag Analytics":
        hashtag_analytics()
    elif selected_tool == "Tag Optimizer":
        tag_optimizer()
    elif selected_tool == "Interaction Tracker":
        interaction_tracker()
    elif selected_tool == "Community Builder":
        community_builder()
    elif selected_tool == "Response Automation":
        response_automation()
    elif selected_tool == "Unified Dashboard":
        unified_dashboard()
    elif selected_tool == "Account Manager":
        account_manager()
    elif selected_tool == "Content Distributor":
        content_distributor()
    elif selected_tool == "Platform Sync":
        platform_sync()
    elif selected_tool == "Story Creator":
        story_creator()
    elif selected_tool == "Video Scripts":
        video_scripts()
    elif selected_tool == "Demographics Analyzer":
        demographics_analyzer()
    elif selected_tool == "Behavior Insights":
        behavior_insights()
    elif selected_tool == "Growth Tracking":
        growth_tracking()
    elif selected_tool == "Engagement Patterns":
        engagement_patterns()
    elif selected_tool == "Performance Monitor":
        performance_monitor()
    elif selected_tool == "ROI Tracker":
        roi_tracker()
    elif selected_tool == "Campaign Analytics":
        campaign_analytics()
    elif selected_tool == "Trend Detection":
        trend_detection()
    elif selected_tool == "Collaboration Manager":
        collaboration_manager()
    elif selected_tool == "Outreach Automation":
        outreach_automation()
    elif selected_tool == "ROI Calculator":
        roi_calculator()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def multi_platform_scheduler():
    """Schedule posts across multiple social media platforms"""
    create_tool_header("Multi-Platform Scheduler", "Schedule posts across multiple social media platforms", "📅")

    # Platform selection
    st.subheader("Select Platforms")
    platforms = st.multiselect("Choose Platforms", [
        "Twitter", "Facebook", "Instagram", "LinkedIn", "TikTok", "YouTube", "Pinterest", "Reddit"
    ], default=["Twitter", "Facebook", "Instagram"])

    if not platforms:
        st.warning("Please select at least one platform.")
        return

    # Content creation
    st.subheader("Create Content")

    content_type = st.selectbox("Content Type", [
        "Text Post", "Image Post", "Video Post", "Link Post", "Story", "Carousel"
    ])

    # Main content
    main_content = st.text_area("Main Content", height=150,
                                placeholder="Write your post content here...")

    # Platform-specific customization
    st.subheader("Platform-Specific Content")
    platform_content = {}

    for platform in platforms:
        with st.expander(f"{platform} Customization"):
            custom_content = st.text_area(f"Custom content for {platform}",
                                          value=main_content,
                                          key=f"content_{platform}",
                                          help=f"Customize content specifically for {platform}")

            # Platform-specific settings
            if platform == "Twitter":
                thread_mode = st.checkbox("Create Thread", key=f"thread_{platform}")
                if thread_mode:
                    thread_count = st.number_input("Number of tweets", 1, 10, 1, key=f"thread_count_{platform}")

            elif platform == "Instagram":
                use_carousel = st.checkbox("Carousel Post", key=f"carousel_{platform}")
                story_post = st.checkbox("Also post to Story", key=f"story_{platform}")

            elif platform == "LinkedIn":
                professional_tone = st.checkbox("Use Professional Tone", True, key=f"prof_{platform}")

            # Hashtags for each platform
            hashtags = st.text_input(f"Hashtags for {platform}",
                                     placeholder="#hashtag1 #hashtag2",
                                     key=f"hashtags_{platform}")

            platform_content[platform] = {
                'content': custom_content,
                'hashtags': hashtags,
                'settings': {}
            }

    # Scheduling
    st.subheader("Schedule Settings")

    col1, col2 = st.columns(2)
    with col1:
        schedule_option = st.selectbox("Schedule Option", [
            "Post Now", "Schedule for Later", "Optimal Time", "Custom Schedule"
        ])

    # Initialize default values
    schedule_date = datetime.now().date()
    schedule_time = datetime.now().time()

    with col2:
        if schedule_option in ["Schedule for Later", "Custom Schedule"]:
            schedule_date = st.date_input("Schedule Date", datetime.now().date())
            schedule_time = st.time_input("Schedule Time", datetime.now().time())
        elif schedule_option == "Optimal Time":
            timezone = st.selectbox("Timezone", [
                "UTC", "EST", "PST", "GMT", "CET", "JST", "IST"
            ])

    # Media attachments
    if content_type in ["Image Post", "Video Post", "Carousel"]:
        st.subheader("Media Attachments")
        media_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mov'], accept_multiple=True)

        if media_files:
            st.success(f"Uploaded {len(media_files)} media file(s)")

    # Preview and schedule
    if st.button("Preview & Schedule Posts"):
        if main_content:
            preview_posts(platform_content, platforms, schedule_option)

            # Create scheduling data
            schedule_data = {
                'platforms': platforms,
                'content': platform_content,
                'schedule_option': schedule_option,
                'schedule_datetime': f"{schedule_date} {schedule_time}" if schedule_option != "Post Now" else "Immediate",
                'content_type': content_type,
                'created_at': datetime.now().isoformat()
            }

            # Export schedule
            if st.button("Export Schedule"):
                schedule_json = json.dumps(schedule_data, indent=2)
                FileHandler.create_download_link(
                    schedule_json.encode(),
                    f"social_media_schedule_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    "application/json"
                )
        else:
            st.error("Please enter some content for your post.")


def content_calendar():
    """Create and manage social media content calendar"""
    create_tool_header("Content Calendar", "Plan and organize your social media content", "📅")

    # Calendar view options
    view_type = st.selectbox("Calendar View", ["Monthly", "Weekly", "Daily"])

    if view_type == "Monthly":
        selected_date = st.date_input("Select Month", datetime.now().date())
        year = selected_date.year
        month = selected_date.month

        # Display monthly calendar
        st.subheader(f"Content Calendar - {calendar.month_name[month]} {year}")

        # Calendar grid
        cal = calendar.monthcalendar(year, month)

        # Create calendar layout
        for week in cal:
            cols = st.columns(7)
            for i, day in enumerate(week):
                with cols[i]:
                    if day == 0:
                        st.write("")
                    else:
                        date_obj = datetime(year, month, day).date()

                        # Check if content is scheduled for this day
                        has_content = check_scheduled_content(date_obj)

                        if has_content:
                            st.markdown(f"**{day}** 📝")
                            if st.button(f"View {day}", key=f"day_{day}"):
                                show_day_content(date_obj)
                        else:
                            st.write(f"{day}")
                            if st.button(f"+ {day}", key=f"add_{day}"):
                                add_content_to_day(date_obj)

    # Content planning
    st.subheader("Plan New Content")

    col1, col2 = st.columns(2)
    with col1:
        content_date = st.date_input("Content Date")
        content_time = st.time_input("Content Time")
        platform = st.selectbox("Platform", [
            "All Platforms", "Twitter", "Facebook", "Instagram", "LinkedIn", "TikTok"
        ])

    with col2:
        content_type = st.selectbox("Content Type", [
            "Promotional", "Educational", "Entertainment", "Behind-the-Scenes", "User-Generated", "News"
        ])
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])

    content_title = st.text_input("Content Title")
    content_description = st.text_area("Content Description", height=100)
    content_notes = st.text_area("Notes/Ideas", height=80)

    if st.button("Add to Calendar"):
        if content_title and content_description:
            calendar_entry = create_calendar_entry(
                content_date, content_time, platform, content_type,
                priority, content_title, content_description, content_notes
            )

            st.success(f"Content added to calendar for {content_date}")

            # Export calendar entry
            entry_json = json.dumps(calendar_entry, indent=2)
            FileHandler.create_download_link(
                entry_json.encode(),
                f"calendar_entry_{content_date}.json",
                "application/json"
            )


def hashtag_research():
    """Research and analyze hashtags"""
    create_tool_header("Hashtag Research", "Research hashtags for better reach", "#️⃣")

    # Research input
    st.subheader("Hashtag Research")

    col1, col2 = st.columns(2)
    with col1:
        research_method = st.selectbox("Research Method", [
            "Topic-Based", "Competitor Analysis", "Trending Discovery", "Niche Research"
        ])
        platform = st.selectbox("Target Platform", [
            "Instagram", "Twitter", "TikTok", "LinkedIn", "Facebook"
        ])

    with col2:
        topic = st.text_input("Topic/Keyword", placeholder="Enter your topic or keyword")
        industry = st.selectbox("Industry", [
            "Technology", "Fashion", "Food", "Travel", "Fitness", "Business",
            "Art", "Music", "Education", "Health", "Other"
        ])

    if st.button("Research Hashtags") and topic:
        with st.spinner("Researching hashtags..."):
            # Generate hashtag research using AI
            hashtag_data = research_hashtags_ai(topic, platform, industry, research_method)

            if hashtag_data:
                st.subheader("Hashtag Research Results")

                # Display recommended hashtags
                tabs = st.tabs(["Recommended", "Popular", "Niche", "Trending"])

                with tabs[0]:  # Recommended
                    st.write("**Recommended Hashtags:**")
                    recommended = hashtag_data.get('recommended', [])
                    display_hashtag_list(recommended, "recommended")

                with tabs[1]:  # Popular
                    st.write("**Popular Hashtags:**")
                    popular = hashtag_data.get('popular', [])
                    display_hashtag_list(popular, "popular")

                with tabs[2]:  # Niche
                    st.write("**Niche Hashtags:**")
                    niche = hashtag_data.get('niche', [])
                    display_hashtag_list(niche, "niche")

                with tabs[3]:  # Trending
                    st.write("**Trending Hashtags:**")
                    trending = hashtag_data.get('trending', [])
                    display_hashtag_list(trending, "trending")

                # Hashtag strategy
                st.subheader("Hashtag Strategy Recommendations")
                strategy = generate_hashtag_strategy(hashtag_data, platform)

                for recommendation in strategy:
                    st.write(f"• {recommendation}")

                # Export hashtags
                if st.button("Export Hashtag Research"):
                    export_data = {
                        'topic': topic,
                        'platform': platform,
                        'industry': industry,
                        'research_method': research_method,
                        'hashtags': hashtag_data,
                        'strategy': strategy,
                        'research_date': datetime.now().isoformat()
                    }

                    export_json = json.dumps(export_data, indent=2)
                    FileHandler.create_download_link(
                        export_json.encode(),
                        f"hashtag_research_{topic.replace(' ', '_')}.json",
                        "application/json"
                    )


def engagement_analytics():
    """Analyze social media engagement metrics"""
    create_tool_header("Engagement Analytics", "Analyze engagement metrics and performance", "📊")

    # Data input method
    data_method = st.selectbox("Data Input Method", [
        "Upload CSV Data", "Manual Entry", "Sample Data"
    ])

    # Initialize engagement_data
    engagement_data = None

    if data_method == "Upload CSV Data":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)

        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                st.subheader("Uploaded Data Preview")
                st.dataframe(df.head())

                engagement_data = df.to_dict('records')
        else:
            engagement_data = None

    elif data_method == "Sample Data":
        engagement_data = generate_sample_engagement_data()
        st.success("Using sample engagement data for demonstration")

    else:  # Manual Entry
        st.subheader("Enter Engagement Data")

        posts = []
        num_posts = st.number_input("Number of Posts to Analyze", 1, 20, 5)

        for i in range(num_posts):
            with st.expander(f"Post {i + 1}"):
                col1, col2 = st.columns(2)

                with col1:
                    post_type = st.selectbox(f"Post Type", ["Image", "Video", "Text", "Carousel"], key=f"type_{i}")
                    platform = st.selectbox(f"Platform", ["Instagram", "Twitter", "Facebook", "LinkedIn"],
                                            key=f"platform_{i}")
                    date = st.date_input(f"Post Date", key=f"date_{i}")

                with col2:
                    likes = st.number_input(f"Likes", 0, 100000, 0, key=f"likes_{i}")
                    comments = st.number_input(f"Comments", 0, 10000, 0, key=f"comments_{i}")
                    shares = st.number_input(f"Shares", 0, 10000, 0, key=f"shares_{i}")

                posts.append({
                    'post_type': post_type,
                    'platform': platform,
                    'date': date.isoformat(),
                    'likes': likes,
                    'comments': comments,
                    'shares': shares,
                    'engagement_rate': calculate_engagement_rate(likes, comments, shares)
                })

        engagement_data = posts

    # Analytics
    if engagement_data:
        st.subheader("Engagement Analytics")

        # Overall metrics
        total_posts = len(engagement_data)
        total_likes = sum(post.get('likes', 0) for post in engagement_data)
        total_comments = sum(post.get('comments', 0) for post in engagement_data)
        total_shares = sum(post.get('shares', 0) for post in engagement_data)
        avg_engagement = sum(
            post.get('engagement_rate', 0) for post in engagement_data) / total_posts if total_posts > 0 else 0

        # Display metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Total Posts", total_posts)
        with col2:
            st.metric("Total Likes", f"{total_likes:,}")
        with col3:
            st.metric("Total Comments", f"{total_comments:,}")
        with col4:
            st.metric("Total Shares", f"{total_shares:,}")
        with col5:
            st.metric("Avg Engagement", f"{avg_engagement:.2%}")

        # Performance by platform
        st.subheader("Performance by Platform")
        platform_stats = analyze_platform_performance(engagement_data)

        for platform, stats in platform_stats.items():
            with st.expander(f"{platform} Performance"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Posts", stats['posts'])
                with col2:
                    st.metric("Avg Likes", f"{stats['avg_likes']:.0f}")
                with col3:
                    st.metric("Engagement Rate", f"{stats['avg_engagement']:.2%}")

        # Best performing posts
        st.subheader("Top Performing Posts")
        top_posts = sorted(engagement_data, key=lambda x: x.get('engagement_rate', 0), reverse=True)[:5]

        for i, post in enumerate(top_posts, 1):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"**#{i}** {post.get('post_type', 'Unknown')}")
            with col2:
                st.write(f"Platform: {post.get('platform', 'Unknown')}")
            with col3:
                st.write(f"Date: {post.get('date', 'Unknown')}")
            with col4:
                st.write(f"Engagement: {post.get('engagement_rate', 0):.2%}")

        # Generate report
        if st.button("Generate Analytics Report"):
            report = generate_engagement_report(engagement_data, platform_stats)

            FileHandler.create_download_link(
                report.encode(),
                f"engagement_analytics_{datetime.now().strftime('%Y%m%d')}.txt",
                "text/plain"
            )


def post_generator():
    """Generate social media posts using AI"""
    create_tool_header("Post Generator", "Generate engaging social media posts with AI", "✍️")

    # Post parameters
    st.subheader("Post Configuration")

    col1, col2 = st.columns(2)
    with col1:
        platform = st.selectbox("Target Platform", [
            "Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok", "Pinterest"
        ])
        post_type = st.selectbox("Post Type", [
            "Promotional", "Educational", "Entertaining", "Inspirational", "Behind-the-Scenes", "Question/Poll"
        ])
        topic = st.text_input("Topic/Subject", placeholder="What should the post be about?")

    with col2:
        tone = st.selectbox("Tone", [
            "Professional", "Casual", "Friendly", "Humorous", "Inspirational", "Educational"
        ])
        target_audience = st.selectbox("Target Audience", [
            "General", "Young Adults", "Professionals", "Students", "Parents", "Entrepreneurs"
        ])
        include_hashtags = st.checkbox("Include Hashtags", True)

    # Additional options
    with st.expander("Advanced Options"):
        call_to_action = st.text_input("Call to Action", placeholder="e.g., Visit our website, Like and share")
        keywords = st.text_input("Keywords to Include", placeholder="keyword1, keyword2, keyword3")
        post_length = st.selectbox("Post Length", ["Short", "Medium", "Long"])
        emoji_style = st.selectbox("Emoji Usage", ["None", "Minimal", "Moderate", "Heavy"])

    if st.button("Generate Post") and topic:
        with st.spinner("Generating social media post..."):
            # Create prompt for AI
            prompt = create_post_generation_prompt(
                platform, post_type, topic, tone, target_audience,
                include_hashtags, call_to_action, keywords, post_length, emoji_style
            )

            generated_post = ai_client.generate_text(prompt, max_tokens=500)

            if generated_post:
                st.subheader("Generated Post")
                st.text_area("", generated_post, height=200, disabled=True)

                # Post analysis
                st.subheader("Post Analysis")
                analysis = analyze_generated_post(generated_post, platform)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Character Count", analysis['char_count'])
                with col2:
                    st.metric("Word Count", analysis['word_count'])
                with col3:
                    st.metric("Hashtag Count", analysis['hashtag_count'])

                # Platform-specific feedback
                feedback = get_platform_feedback(generated_post, platform)
                if feedback:
                    st.subheader("Platform Optimization Feedback")
                    for item in feedback:
                        st.write(f"• {item}")

                # Download post
                FileHandler.create_download_link(
                    generated_post.encode(),
                    f"social_post_{platform.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    "text/plain"
                )

                # Generate variations
                if st.button("Generate Variations"):
                    variations = generate_post_variations(generated_post, platform)

                    st.subheader("Post Variations")
                    for i, variation in enumerate(variations, 1):
                        with st.expander(f"Variation {i}"):
                            st.write(variation)


def caption_writer():
    """AI-powered caption writing tool"""
    create_tool_header("Caption Writer", "Write engaging captions for your content", "💬")

    # Content input
    st.subheader("Content Information")

    # Image upload for context
    uploaded_image = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_image:
        image = FileHandler.process_image_file(uploaded_image[0])
        if image:
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Analyze image for context
            if st.button("Analyze Image for Context"):
                with st.spinner("Analyzing image..."):
                    img_bytes = io.BytesIO()
                    image.save(img_bytes, format='PNG')
                    img_bytes.seek(0)

                    image_description = ai_client.analyze_image(
                        img_bytes.getvalue(),
                        "Describe this image in detail for social media caption writing."
                    )

                    if image_description:
                        st.text_area("Image Analysis", image_description, height=100, disabled=True)

    # Caption parameters
    col1, col2 = st.columns(2)
    with col1:
        content_theme = st.text_input("Content Theme/Topic")
        platform = st.selectbox("Platform", ["Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok"])
        caption_style = st.selectbox("Caption Style", [
            "Storytelling", "Question-based", "List-format", "Behind-the-scenes", "Motivational", "Humorous"
        ])

    with col2:
        brand_voice = st.selectbox("Brand Voice", [
            "Professional", "Casual", "Playful", "Inspirational", "Educational", "Luxury"
        ])
        target_mood = st.selectbox("Target Mood", [
            "Engaging", "Informative", "Entertaining", "Inspiring", "Promotional", "Community-building"
        ])
        caption_length = st.selectbox("Caption Length", ["Short", "Medium", "Long"])

    # Additional context
    brand_info = st.text_area("Brand/Business Information (optional)",
                              placeholder="Tell us about your brand, values, or business...")

    specific_message = st.text_area("Specific Message/CTA",
                                    placeholder="Any specific message or call-to-action you want to include...")

    if st.button("Generate Caption"):
        if content_theme:
            with st.spinner("Creating engaging caption..."):
                caption_prompt = create_caption_prompt(
                    content_theme, platform, caption_style, brand_voice,
                    target_mood, caption_length, brand_info, specific_message
                )

                generated_caption = ai_client.generate_text(caption_prompt, max_tokens=800)

                if generated_caption:
                    st.subheader("Generated Caption")
                    st.text_area("", generated_caption, height=250, disabled=True)

                    # Caption metrics
                    st.subheader("Caption Metrics")
                    metrics = analyze_caption_metrics(generated_caption, platform)

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Characters", metrics['characters'])
                    with col2:
                        st.metric("Words", metrics['words'])
                    with col3:
                        st.metric("Hashtags", metrics['hashtags'])
                    with col4:
                        st.metric("Mentions", metrics['mentions'])

                    # Platform optimization
                    optimization = get_caption_optimization(generated_caption, platform)
                    if optimization:
                        st.subheader("Optimization Tips")
                        for tip in optimization:
                            st.write(f"• {tip}")

                    # Export caption
                    FileHandler.create_download_link(
                        generated_caption.encode(),
                        f"caption_{platform.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        "text/plain"
                    )


# Helper Functions

def preview_posts(platform_content, platforms, schedule_option):
    """Preview posts for all platforms"""
    st.subheader("Post Preview")

    for platform in platforms:
        with st.expander(f"{platform} Post Preview"):
            content = platform_content[platform]['content']
            hashtags = platform_content[platform]['hashtags']

            # Show platform-specific preview
            st.write(f"**{platform} Post:**")
            st.write(content)
            if hashtags:
                st.write(f"**Hashtags:** {hashtags}")

            st.write(f"**Schedule:** {schedule_option}")


def check_scheduled_content(date):
    """Check if content is scheduled for a specific date"""
    # This would check against a database or storage
    # For demo, randomly return True/False
    return random.choice([True, False, False])  # 33% chance of having content


def show_day_content(date):
    """Show content scheduled for a specific day"""
    st.write(f"Content scheduled for {date}")
    # This would fetch actual content from storage


def add_content_to_day(date):
    """Add content to a specific day"""
    st.write(f"Add content for {date}")
    # This would open a form to add content


def create_calendar_entry(date, time, platform, content_type, priority, title, description, notes):
    """Create a calendar entry"""
    return {
        'date': date.isoformat(),
        'time': time.isoformat(),
        'platform': platform,
        'content_type': content_type,
        'priority': priority,
        'title': title,
        'description': description,
        'notes': notes,
        'created_at': datetime.now().isoformat()
    }


def research_hashtags_ai(topic, platform, industry, method):
    """Research hashtags using AI"""
    prompt = f"""
    Research hashtags for the topic "{topic}" on {platform} in the {industry} industry.
    Method: {method}

    Provide:
    1. 10 recommended hashtags (mix of popular and niche)
    2. 5 popular hashtags (high volume)
    3. 5 niche hashtags (specific to topic)
    4. 5 trending hashtags (currently popular)

    Format as JSON with categories: recommended, popular, niche, trending
    """

    try:
        response = ai_client.generate_text(prompt, max_tokens=1000)
        # Try to parse as JSON, fallback to text processing
        if response.strip().startswith('{'):
            return json.loads(response)
        else:
            # Parse text response into hashtag categories
            return parse_hashtag_response(response)
    except:
        # Fallback hashtag data
        return generate_fallback_hashtags(topic, platform, industry)


def display_hashtag_list(hashtags, category):
    """Display hashtag list with copy functionality"""
    if hashtags:
        hashtag_text = ' '.join([f"#{tag}" if not tag.startswith('#') else tag for tag in hashtags])
        st.code(hashtag_text)

        if st.button(f"Copy {category.title()} Hashtags", key=f"copy_{category}"):
            st.success(f"{category.title()} hashtags copied to clipboard!")


def generate_hashtag_strategy(hashtag_data, platform):
    """Generate hashtag strategy recommendations"""
    strategies = [
        f"Use a mix of popular and niche hashtags for optimal reach on {platform}",
        "Include 3-5 popular hashtags to increase discoverability",
        "Add 5-7 niche hashtags to target specific audiences",
        "Monitor trending hashtags and incorporate when relevant",
        "Create a branded hashtag for community building"
    ]

    if platform == "Instagram":
        strategies.append("Use up to 30 hashtags, but 11-15 often perform best")
    elif platform == "Twitter":
        strategies.append("Limit to 1-2 hashtags to maintain readability")
    elif platform == "TikTok":
        strategies.append("Use trending sounds and hashtags for algorithm boost")

    return strategies


def generate_sample_engagement_data():
    """Generate sample engagement data for analytics"""
    platforms = ["Instagram", "Twitter", "Facebook", "LinkedIn"]
    post_types = ["Image", "Video", "Text", "Carousel"]

    data = []
    for i in range(20):
        date = datetime.now() - timedelta(days=random.randint(1, 30))
        likes = random.randint(50, 1000)
        comments = random.randint(5, 100)
        shares = random.randint(1, 50)

        data.append({
            'post_type': random.choice(post_types),
            'platform': random.choice(platforms),
            'date': date.isoformat(),
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'engagement_rate': calculate_engagement_rate(likes, comments, shares)
        })

    return data


def calculate_engagement_rate(likes, comments, shares, followers=1000):
    """Calculate engagement rate"""
    total_engagement = likes + comments + shares
    return total_engagement / followers


def analyze_platform_performance(engagement_data):
    """Analyze performance by platform"""
    platform_stats = {}

    for post in engagement_data:
        platform = post.get('platform')
        if platform not in platform_stats:
            platform_stats[platform] = {
                'posts': 0,
                'total_likes': 0,
                'total_engagement': 0
            }

        platform_stats[platform]['posts'] += 1
        platform_stats[platform]['total_likes'] += post.get('likes', 0)
        platform_stats[platform]['total_engagement'] += post.get('engagement_rate', 0)

    # Calculate averages
    for platform, stats in platform_stats.items():
        stats['avg_likes'] = stats['total_likes'] / stats['posts'] if stats['posts'] > 0 else 0
        stats['avg_engagement'] = stats['total_engagement'] / stats['posts'] if stats['posts'] > 0 else 0

    return platform_stats


def generate_engagement_report(engagement_data, platform_stats):
    """Generate engagement analytics report"""
    report = "SOCIAL MEDIA ENGAGEMENT ANALYTICS REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Analysis Period: Last 30 days\n\n"

    # Overall stats
    total_posts = len(engagement_data)
    total_likes = sum(post.get('likes', 0) for post in engagement_data)
    total_comments = sum(post.get('comments', 0) for post in engagement_data)
    total_shares = sum(post.get('shares', 0) for post in engagement_data)

    report += "OVERALL PERFORMANCE:\n"
    report += f"Total Posts: {total_posts}\n"
    report += f"Total Likes: {total_likes:,}\n"
    report += f"Total Comments: {total_comments:,}\n"
    report += f"Total Shares: {total_shares:,}\n\n"

    # Platform breakdown
    report += "PLATFORM PERFORMANCE:\n"
    for platform, stats in platform_stats.items():
        report += f"\n{platform}:\n"
        report += f"  Posts: {stats['posts']}\n"
        report += f"  Avg Likes: {stats['avg_likes']:.0f}\n"
        report += f"  Avg Engagement Rate: {stats['avg_engagement']:.2%}\n"

    return report


def create_post_generation_prompt(platform, post_type, topic, tone, audience, hashtags, cta, keywords, length, emoji):
    """Create prompt for post generation"""
    prompt = f"""
    Create a {post_type.lower()} social media post for {platform} about "{topic}".

    Requirements:
    - Tone: {tone}
    - Target Audience: {audience}
    - Post Length: {length}
    - Emoji Usage: {emoji}
    """

    if hashtags:
        prompt += f"\n- Include relevant hashtags"

    if cta:
        prompt += f"\n- Include this call to action: {cta}"

    if keywords:
        prompt += f"\n- Include these keywords: {keywords}"

    prompt += f"\n\nMake it engaging and optimized for {platform}."

    return prompt


def analyze_generated_post(post, platform):
    """Analyze generated post metrics"""
    char_count = len(post)
    word_count = len(post.split())
    hashtag_count = post.count('#')

    return {
        'char_count': char_count,
        'word_count': word_count,
        'hashtag_count': hashtag_count
    }


def get_platform_feedback(post, platform):
    """Get platform-specific optimization feedback"""
    feedback = []
    char_count = len(post)

    if platform == "Twitter" and char_count > 280:
        feedback.append("Post exceeds Twitter's 280 character limit")
    elif platform == "Instagram" and char_count > 2200:
        feedback.append("Post exceeds Instagram's caption limit")

    if platform == "LinkedIn" and not any(word in post.lower() for word in ['professional', 'business', 'career']):
        feedback.append("Consider adding professional context for LinkedIn")

    return feedback


def generate_post_variations(original_post, platform):
    """Generate variations of the original post"""
    variations = []

    # This would use AI to create variations
    variations.append(f"Variation 1: {original_post[:100]}... (shortened)")
    variations.append(f"Variation 2: {original_post} (with different hashtags)")
    variations.append(f"Variation 3: Question format - What do you think about {original_post[:50]}?")

    return variations


def create_caption_prompt(theme, platform, style, voice, mood, length, brand_info, message):
    """Create prompt for caption generation"""
    prompt = f"""
    Write a {length.lower()} {style.lower()} caption for {platform} about "{theme}".

    Style Requirements:
    - Brand Voice: {voice}
    - Target Mood: {mood}
    - Caption Style: {style}
    """

    if brand_info:
        prompt += f"\n- Brand Context: {brand_info}"

    if message:
        prompt += f"\n- Include Message/CTA: {message}"

    prompt += f"\n\nMake it engaging and authentic for {platform}."

    return prompt


def analyze_caption_metrics(caption, platform):
    """Analyze caption metrics"""
    return {
        'characters': len(caption),
        'words': len(caption.split()),
        'hashtags': caption.count('#'),
        'mentions': caption.count('@')
    }


def get_caption_optimization(caption, platform):
    """Get caption optimization tips"""
    tips = []

    if platform == "Instagram":
        if caption.count('#') < 5:
            tips.append("Consider adding more hashtags (5-11 recommended for Instagram)")
        if len(caption) < 100:
            tips.append("Instagram captions can be longer - consider expanding your story")

    elif platform == "Twitter":
        if len(caption) > 240:
            tips.append("Consider shortening for Twitter (280 char limit)")
        if caption.count('#') > 2:
            tips.append("Twitter posts work better with 1-2 hashtags")

    return tips


# Placeholder functions for remaining tools
def parse_hashtag_response(response):
    """Parse text response into hashtag categories"""
    return {
        'recommended': ['example1', 'example2', 'example3'],
        'popular': ['popular1', 'popular2', 'popular3'],
        'niche': ['niche1', 'niche2', 'niche3'],
        'trending': ['trending1', 'trending2', 'trending3']
    }


def generate_fallback_hashtags(topic, platform, industry):
    """Generate fallback hashtag data"""
    return {
        'recommended': [f'{topic}', f'{industry}', f'{platform}content'],
        'popular': ['trending', 'viral', 'popular'],
        'niche': [f'{topic}community', f'{industry}life', 'niche'],
        'trending': ['trend1', 'trend2', 'trend3']
    }


def audience_segmentation():
    """Advanced audience segmentation and analysis tool"""
    create_tool_header("Audience Segmentation", "Analyze and segment your audience for targeted campaigns", "👥")

    # Data input method
    st.subheader("Audience Data Input")
    data_source = st.selectbox("Data Source", [
        "Upload CSV File", "Manual Entry", "Platform Analytics", "Sample Data"
    ])

    audience_data = None

    if data_source == "Upload CSV File":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                st.subheader("Data Preview")
                st.dataframe(df.head())
                audience_data = df.to_dict('records')

    elif data_source == "Sample Data":
        audience_data = generate_sample_audience_data()
        st.success("Using sample audience data for demonstration")

    elif data_source == "Manual Entry":
        st.subheader("Enter Audience Information")

        num_segments = st.number_input("Number of Audience Segments", 1, 10, 3)
        audience_data = []

        for i in range(num_segments):
            with st.expander(f"Segment {i + 1}"):
                col1, col2 = st.columns(2)

                with col1:
                    segment_name = st.text_input(f"Segment Name", f"Segment {i + 1}", key=f"seg_name_{i}")
                    age_range = st.selectbox(f"Age Range", ["18-24", "25-34", "35-44", "45-54", "55+"], key=f"age_{i}")
                    gender = st.selectbox(f"Gender", ["All", "Male", "Female", "Non-binary"], key=f"gender_{i}")
                    location = st.text_input(f"Primary Location", "United States", key=f"location_{i}")

                with col2:
                    interests = st.text_area(f"Interests", "technology, social media, marketing", key=f"interests_{i}")
                    platform_usage = st.multiselect(f"Platform Usage",
                                                    ["Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok",
                                                     "YouTube"],
                                                    default=["Instagram", "Facebook"], key=f"platforms_{i}")
                    engagement_level = st.selectbox(f"Engagement Level", ["High", "Medium", "Low"],
                                                    key=f"engagement_{i}")
                    spending_power = st.selectbox(f"Spending Power", ["High", "Medium", "Low"], key=f"spending_{i}")

                audience_data.append({
                    'segment_name': segment_name,
                    'age_range': age_range,
                    'gender': gender,
                    'location': location,
                    'interests': interests.split(', '),
                    'platforms': platform_usage,
                    'engagement_level': engagement_level,
                    'spending_power': spending_power
                })

    # Segmentation analysis
    if audience_data:
        st.subheader("Audience Segmentation Analysis")

        # Segmentation criteria
        col1, col2 = st.columns(2)
        with col1:
            primary_criteria = st.selectbox("Primary Segmentation Criteria", [
                "Demographics", "Behavior", "Interests", "Platform Usage", "Engagement Level"
            ])
        with col2:
            secondary_criteria = st.selectbox("Secondary Criteria", [
                "Location", "Spending Power", "Age", "Gender", "Activity Level"
            ])

        if st.button("Analyze Segments"):
            # Perform segmentation analysis
            analysis_results = analyze_audience_segments(audience_data, primary_criteria, secondary_criteria)

            # Display results
            tabs = st.tabs(["Overview", "Detailed Segments", "Recommendations", "Export"])

            with tabs[0]:  # Overview
                st.subheader("Segmentation Overview")

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Segments", len(analysis_results['segments']))
                with col2:
                    st.metric("Largest Segment", analysis_results['largest_segment']['name'])
                with col3:
                    st.metric("Most Engaged", analysis_results['most_engaged']['name'])
                with col4:
                    st.metric("High Value", analysis_results['high_value']['count'])

                # Segment distribution chart
                st.subheader("Segment Distribution")
                for segment in analysis_results['segments']:
                    percentage = segment['percentage']
                    st.progress(percentage / 100)
                    st.write(f"**{segment['name']}**: {percentage:.1f}%")

            with tabs[1]:  # Detailed Segments
                st.subheader("Detailed Segment Analysis")

                for segment in analysis_results['segments']:
                    with st.expander(f"📊 {segment['name']} ({segment['percentage']:.1f}%)"):
                        col1, col2 = st.columns(2)

                        with col1:
                            st.write("**Demographics:**")
                            st.write(f"• Age: {segment['demographics']['age']}")
                            st.write(f"• Gender: {segment['demographics']['gender']}")
                            st.write(f"• Location: {segment['demographics']['location']}")

                            st.write("**Behavior:**")
                            st.write(f"• Engagement: {segment['behavior']['engagement']}")
                            st.write(f"• Activity: {segment['behavior']['activity']}")

                        with col2:
                            st.write("**Platform Preferences:**")
                            for platform in segment['platforms']:
                                st.write(f"• {platform}")

                            st.write("**Key Interests:**")
                            for interest in segment['interests'][:5]:
                                st.write(f"• {interest}")

                        st.write("**Targeting Recommendations:**")
                        for rec in segment['recommendations']:
                            st.write(f"💡 {rec}")

            with tabs[2]:  # Recommendations
                st.subheader("Marketing Recommendations")

                for rec_category, recommendations in analysis_results['marketing_recommendations'].items():
                    st.write(f"**{rec_category.title()}:**")
                    for rec in recommendations:
                        st.write(f"• {rec}")
                    st.write("")

            with tabs[3]:  # Export
                st.subheader("Export Analysis")

                if st.button("Generate Segmentation Report"):
                    report = generate_segmentation_report(analysis_results, audience_data)

                    FileHandler.create_download_link(
                        report.encode(),
                        f"audience_segmentation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        "text/plain"
                    )

                if st.button("Export Segment Data"):
                    segment_json = json.dumps(analysis_results, indent=2)
                    FileHandler.create_download_link(
                        segment_json.encode(),
                        f"audience_segments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        "application/json"
                    )


def campaign_planner():
    """Comprehensive social media campaign planning tool"""
    create_tool_header("Campaign Planner", "Plan and manage your social media campaigns", "📋")

    # Campaign basics
    st.subheader("Campaign Setup")

    col1, col2 = st.columns(2)
    with col1:
        campaign_name = st.text_input("Campaign Name", placeholder="e.g., Summer Product Launch")
        campaign_type = st.selectbox("Campaign Type", [
            "Product Launch", "Brand Awareness", "Lead Generation", "Sales Promotion",
            "Event Marketing", "Engagement Drive", "Content Series", "Other"
        ])
        start_date = st.date_input("Start Date", datetime.now().date())
        end_date = st.date_input("End Date", datetime.now().date() + timedelta(days=30))

    with col2:
        target_audience = st.text_input("Target Audience", placeholder="e.g., Young professionals, tech enthusiasts")
        budget = st.number_input("Total Budget ($)", 0, 1000000, 5000)
        primary_goal = st.selectbox("Primary Goal", [
            "Increase Brand Awareness", "Drive Website Traffic", "Generate Leads",
            "Boost Sales", "Improve Engagement", "Build Community", "Launch Product"
        ])
        platforms = st.multiselect("Platforms", [
            "Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok", "YouTube", "Pinterest"
        ], default=["Instagram", "Facebook"])

    # Campaign objectives and KPIs
    st.subheader("Campaign Objectives & KPIs")

    objectives = []
    num_objectives = st.number_input("Number of Objectives", 1, 5, 2)

    for i in range(num_objectives):
        with st.expander(f"Objective {i + 1}"):
            col1, col2 = st.columns(2)

            with col1:
                objective_name = st.text_input(f"Objective", f"Objective {i + 1}", key=f"obj_name_{i}")
                metric = st.selectbox(f"Key Metric", [
                    "Reach", "Impressions", "Engagement Rate", "Click-through Rate",
                    "Conversions", "Leads", "Sales", "Followers", "Video Views"
                ], key=f"metric_{i}")

            with col2:
                target_value = st.number_input(f"Target Value", 0, 1000000, 1000, key=f"target_{i}")
                timeframe = st.selectbox(f"Timeframe", [
                    "Daily", "Weekly", "Monthly", "Campaign Total"
                ], key=f"timeframe_{i}")

            objectives.append({
                'name': objective_name,
                'metric': metric,
                'target': target_value,
                'timeframe': timeframe
            })

    # Content planning
    st.subheader("Content Planning")

    content_themes = st.text_area("Content Themes",
                                  placeholder="List the main themes/topics for your campaign content",
                                  height=100)

    content_types = st.multiselect("Content Types", [
        "Image Posts", "Video Posts", "Stories", "Reels/Short Videos",
        "Carousel Posts", "Live Videos", "User-Generated Content", "Polls/Questions"
    ], default=["Image Posts", "Video Posts"])

    posting_frequency = {}
    for platform in platforms:
        frequency = st.selectbox(f"{platform} Posting Frequency", [
            "Daily", "Every 2 days", "3 times per week", "Weekly", "Custom"
        ], key=f"freq_{platform}")
        posting_frequency[platform] = frequency

    # Budget allocation
    st.subheader("Budget Allocation")

    budget_allocation = {}
    remaining_budget = budget

    for platform in platforms:
        max_allocation = remaining_budget if platform == platforms[-1] else remaining_budget - (
                len(platforms) - platforms.index(platform) - 1)
        allocation = st.number_input(
            f"{platform} Budget ($)",
            0,
            max_allocation,
            min(max_allocation, budget // len(platforms)),
            key=f"budget_{platform}"
        )
        budget_allocation[platform] = allocation
        remaining_budget -= allocation

    st.write(f"Remaining Budget: ${remaining_budget}")

    # Timeline and milestones
    st.subheader("Campaign Timeline")

    milestones = []
    num_milestones = st.number_input("Number of Milestones", 1, 10, 3)

    for i in range(num_milestones):
        with st.expander(f"Milestone {i + 1}"):
            col1, col2 = st.columns(2)

            with col1:
                milestone_name = st.text_input(f"Milestone", f"Milestone {i + 1}", key=f"milestone_name_{i}")
                milestone_date = st.date_input(f"Date", start_date + timedelta(days=i * 7), key=f"milestone_date_{i}")

            with col2:
                milestone_desc = st.text_area(f"Description", key=f"milestone_desc_{i}")
                milestone_owner = st.text_input(f"Owner", "Team Member", key=f"milestone_owner_{i}")

            milestones.append({
                'name': milestone_name,
                'date': milestone_date.isoformat(),
                'description': milestone_desc,
                'owner': milestone_owner
            })

    # Generate campaign plan
    if st.button("Generate Campaign Plan") and campaign_name:
        campaign_data = {
            'campaign_name': campaign_name,
            'campaign_type': campaign_type,
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat(),
            'target_audience': target_audience,
            'budget': budget,
            'primary_goal': primary_goal,
            'platforms': platforms,
            'objectives': objectives,
            'content_themes': content_themes,
            'content_types': content_types,
            'posting_frequency': posting_frequency,
            'budget_allocation': budget_allocation,
            'milestones': milestones,
            'created_at': datetime.now().isoformat()
        }

        # Display campaign overview
        st.subheader("📊 Campaign Overview")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Duration", f"{(end_date - start_date).days} days")
        with col2:
            st.metric("Platforms", len(platforms))
        with col3:
            st.metric("Budget", f"${budget:,}")
        with col4:
            st.metric("Objectives", len(objectives))

        # Platform breakdown
        st.subheader("Platform Strategy")
        for platform in platforms:
            with st.expander(f"{platform} Strategy"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Budget:** ${budget_allocation.get(platform, 0):,}")
                    st.write(f"**Posting:** {posting_frequency.get(platform, 'Not set')}")
                with col2:
                    platform_recommendations = generate_platform_recommendations(platform, campaign_type,
                                                                                 target_audience)
                    st.write("**Recommendations:**")
                    for rec in platform_recommendations:
                        st.write(f"• {rec}")

        # Timeline visualization
        st.subheader("Campaign Timeline")
        timeline_days = (end_date - start_date).days

        for milestone in milestones:
            milestone_date_obj = datetime.fromisoformat(milestone['date']).date()
            days_from_start = (milestone_date_obj - start_date).days
            progress = days_from_start / timeline_days if timeline_days > 0 else 0

            st.write(f"**{milestone['name']}** - {milestone_date_obj}")
            st.progress(min(progress, 1.0))
            if milestone['description']:
                st.write(f"📝 {milestone['description']}")

        # Export options
        st.subheader("Export Campaign Plan")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Download Campaign Plan"):
                plan_text = generate_campaign_plan_report(campaign_data)
                FileHandler.create_download_link(
                    plan_text.encode(),
                    f"campaign_plan_{campaign_name.replace(' ', '_')}.txt",
                    "text/plain"
                )

        with col2:
            if st.button("Export as JSON"):
                plan_json = json.dumps(campaign_data, indent=2)
                FileHandler.create_download_link(
                    plan_json.encode(),
                    f"campaign_data_{campaign_name.replace(' ', '_')}.json",
                    "application/json"
                )


def mention_monitor():
    """Monitor brand mentions across social media platforms"""
    create_tool_header("Mention Monitor", "Track brand mentions and social conversations", "👂")

    # Search setup
    st.subheader("Mention Monitoring Setup")

    col1, col2 = st.columns(2)
    with col1:
        brand_terms = st.text_area("Brand Terms to Monitor",
                                   placeholder="Enter brand names, products, hashtags (one per line)")
        platforms = st.multiselect("Platforms to Monitor", [
            "Twitter", "Instagram", "Facebook", "LinkedIn", "TikTok", "Reddit", "YouTube"
        ], default=["Twitter", "Instagram"])

    with col2:
        monitoring_period = st.selectbox("Monitoring Period", [
            "Last 24 hours", "Last 7 days", "Last 30 days", "Custom Range"
        ])
        sentiment_filter = st.selectbox("Sentiment Filter", [
            "All Mentions", "Positive Only", "Negative Only", "Neutral Only"
        ])
        language = st.selectbox("Language", ["All", "English", "Spanish", "French", "German"])

    if brand_terms:
        brand_list = [term.strip() for term in brand_terms.split('\n') if term.strip()]

        if st.button("Start Monitoring"):
            with st.spinner("Searching for mentions..."):
                # Simulate mention monitoring
                mentions_data = simulate_mention_monitoring(brand_list, platforms, monitoring_period)

                # Display results
                st.subheader("📊 Monitoring Results")

                # Overview metrics
                total_mentions = len(mentions_data)
                positive = len([m for m in mentions_data if m['sentiment'] == 'positive'])
                negative = len([m for m in mentions_data if m['sentiment'] == 'negative'])
                neutral = len([m for m in mentions_data if m['sentiment'] == 'neutral'])

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Mentions", total_mentions)
                with col2:
                    st.metric("Positive", positive,
                              f"{positive / total_mentions * 100:.1f}%" if total_mentions > 0 else "0%")
                with col3:
                    st.metric("Negative", negative,
                              f"{negative / total_mentions * 100:.1f}%" if total_mentions > 0 else "0%")
                with col4:
                    st.metric("Neutral", neutral,
                              f"{neutral / total_mentions * 100:.1f}%" if total_mentions > 0 else "0%")

                # Platform breakdown
                st.subheader("Platform Breakdown")
                platform_counts = {}
                for mention in mentions_data:
                    platform = mention['platform']
                    platform_counts[platform] = platform_counts.get(platform, 0) + 1

                for platform, count in platform_counts.items():
                    percentage = count / total_mentions * 100 if total_mentions > 0 else 0
                    st.write(f"**{platform}**: {count} mentions ({percentage:.1f}%)")
                    st.progress(percentage / 100)

                # Recent mentions
                st.subheader("Recent Mentions")
                for mention in mentions_data[:10]:  # Show first 10
                    sentiment_color = {
                        'positive': '🟢',
                        'negative': '🔴',
                        'neutral': '🟡'
                    }.get(mention['sentiment'], '⚪')

                    with st.expander(f"{sentiment_color} {mention['platform']} - {mention['author']}"):
                        st.write(f"**Content:** {mention['content']}")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.write(f"**Date:** {mention['date']}")
                        with col2:
                            st.write(f"**Engagement:** {mention['engagement']}")
                        with col3:
                            st.write(f"**Reach:** {mention['reach']}")

                # Export mentions
                if st.button("Export Mentions Report"):
                    report = generate_mentions_report(mentions_data, brand_list)
                    FileHandler.create_download_link(
                        report.encode(),
                        f"mentions_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        "text/plain"
                    )


def influencer_finder():
    """Discover and analyze influencers in your niche"""
    create_tool_header("Influencer Finder", "Find and analyze influencers for collaborations", "⭐")

    # Search criteria
    st.subheader("Influencer Search Criteria")

    col1, col2 = st.columns(2)
    with col1:
        niche = st.selectbox("Niche/Industry", [
            "Technology", "Fashion", "Beauty", "Fitness", "Food", "Travel",
            "Gaming", "Business", "Lifestyle", "Education", "Music", "Art"
        ])
        platforms = st.multiselect("Platforms", [
            "Instagram", "TikTok", "YouTube", "Twitter", "LinkedIn"
        ], default=["Instagram"])
        location = st.text_input("Location (optional)", placeholder="e.g., United States, Global")

    with col2:
        follower_range = st.selectbox("Follower Range", [
            "Nano (1K-10K)", "Micro (10K-100K)", "Mid-tier (100K-1M)",
            "Macro (1M-10M)", "Mega (10M+)", "Any Size"
        ])
        engagement_rate = st.selectbox("Min Engagement Rate", [
            "Any", "1%+", "2%+", "3%+", "5%+", "10%+"
        ])
        budget_range = st.selectbox("Budget Range", [
            "Under $500", "$500-$2K", "$2K-$10K", "$10K-$50K", "$50K+", "Negotiable"
        ])

    # Additional filters
    with st.expander("Advanced Filters"):
        keywords = st.text_input("Keywords in Bio", placeholder="fitness, wellness, healthy")
        content_type = st.multiselect("Content Types", [
            "Photos", "Videos", "Stories", "Reels", "Live Streams", "Tutorials"
        ])
        collaboration_type = st.selectbox("Collaboration Type", [
            "Sponsored Posts", "Product Reviews", "Brand Ambassadorship",
            "Event Partnerships", "Content Creation", "Any"
        ])

    if st.button("Find Influencers"):
        with st.spinner("Searching for influencers..."):
            # Simulate influencer search
            influencers = simulate_influencer_search(niche, platforms, follower_range)

            st.subheader(f"🔍 Found {len(influencers)} Influencers")

            # Display influencers
            for i, influencer in enumerate(influencers):
                with st.expander(f"👤 {influencer['name']} (@{influencer['username']})"):
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write("**Profile Info:**")
                        st.write(f"• Platform: {influencer['platform']}")
                        st.write(f"• Followers: {influencer['followers']:,}")
                        st.write(f"• Location: {influencer['location']}")
                        st.write(f"• Category: {influencer['category']}")

                    with col2:
                        st.write("**Engagement Metrics:**")
                        st.write(f"• Engagement Rate: {influencer['engagement_rate']:.1f}%")
                        st.write(f"• Avg Likes: {influencer['avg_likes']:,}")
                        st.write(f"• Avg Comments: {influencer['avg_comments']:,}")
                        st.write(f"• Post Frequency: {influencer['post_frequency']}")

                    with col3:
                        st.write("**Collaboration Info:**")
                        st.write(f"• Est. Cost: {influencer['estimated_cost']}")
                        st.write(f"• Availability: {influencer['availability']}")
                        st.write(f"• Brand Safety: {influencer['brand_safety']}")

                        if st.button(f"Contact {influencer['name']}", key=f"contact_{i}"):
                            st.success(f"Contact info for {influencer['name']} saved to your outreach list!")

                    st.write(f"**Bio:** {influencer['bio']}")

                    # Audience insights
                    with st.expander("Audience Insights"):
                        audience = influencer['audience_insights']
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("**Demographics:**")
                            for demo, percentage in audience['demographics'].items():
                                st.write(f"• {demo}: {percentage}%")
                        with col2:
                            st.write("**Interests:**")
                            for interest in audience['interests']:
                                st.write(f"• {interest}")

            # Export influencer list
            if st.button("Export Influencer List"):
                export_data = generate_influencer_export(influencers, niche)
                FileHandler.create_download_link(
                    export_data.encode(),
                    f"influencers_{niche.lower()}_{datetime.now().strftime('%Y%m%d')}.csv",
                    "text/csv"
                )


def cross_platform_posting():
    """Post content across multiple social media platforms"""
    create_tool_header("Cross-Platform Posting", "Publish content to multiple platforms simultaneously", "📡")

    # Platform selection
    st.subheader("Select Platforms")
    platforms = st.multiselect("Choose Platforms", [
        "Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok", "Pinterest", "YouTube"
    ], default=["Instagram", "Facebook", "Twitter"])

    if not platforms:
        st.warning("Please select at least one platform to continue.")
        return

    # Content creation
    st.subheader("Create Your Content")

    content_type = st.selectbox("Content Type", [
        "Text Post", "Image Post", "Video Post", "Link Share", "Carousel"
    ])

    # Main content
    main_content = st.text_area("Main Content", height=150,
                                placeholder="Write your main post content here...")

    # Platform-specific customization
    st.subheader("Platform-Specific Customization")
    platform_content = {}

    for platform in platforms:
        with st.expander(f"{platform} Settings"):
            col1, col2 = st.columns(2)

            with col1:
                custom_content = st.text_area(f"Custom content for {platform}",
                                              value=main_content, key=f"content_{platform}",
                                              help=f"Customize content specifically for {platform}")

                hashtags = st.text_input(f"Hashtags for {platform}",
                                         placeholder="#hashtag1 #hashtag2", key=f"hashtags_{platform}")

            with col2:
                # Platform-specific options
                if platform == "Twitter":
                    thread_mode = st.checkbox("Create Thread", key=f"thread_{platform}")
                    if thread_mode:
                        thread_parts = st.number_input("Number of tweets", 1, 10, 1, key=f"thread_count_{platform}")

                elif platform == "Instagram":
                    story_post = st.checkbox("Also post to Story", key=f"story_{platform}")
                    use_carousel = st.checkbox("Carousel Post", key=f"carousel_{platform}")

                elif platform == "LinkedIn":
                    professional_tone = st.checkbox("Use Professional Tone", True, key=f"prof_{platform}")
                    article_format = st.checkbox("Format as Article", key=f"article_{platform}")

                elif platform == "TikTok":
                    trending_sounds = st.checkbox("Use Trending Audio", key=f"audio_{platform}")
                    duet_enabled = st.checkbox("Allow Duets", True, key=f"duet_{platform}")

                posting_time = st.selectbox(f"Posting Time for {platform}", [
                    "Post Now", "Optimal Time", "Custom Time"
                ], key=f"time_{platform}")

            platform_content[platform] = {
                'content': custom_content,
                'hashtags': hashtags,
                'posting_time': posting_time
            }

    # Media upload
    if content_type in ["Image Post", "Video Post", "Carousel"]:
        st.subheader("Upload Media")
        media_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mov'], accept_multiple=True)

        if media_files:
            st.success(f"Uploaded {len(media_files)} media file(s)")

            # Media preview
            for i, file in enumerate(media_files[:3]):  # Show first 3
                if file.type.startswith('image/'):
                    st.image(file, caption=f"Image {i + 1}", width=200)

    # Scheduling options
    st.subheader("Scheduling Options")

    col1, col2 = st.columns(2)
    with col1:
        schedule_option = st.selectbox("When to Post", [
            "Post Immediately", "Schedule for Later", "Save as Draft"
        ])

    with col2:
        if schedule_option == "Schedule for Later":
            schedule_date = st.date_input("Schedule Date")
            schedule_time = st.time_input("Schedule Time")

    # Preview and post
    if st.button("Preview Posts") and main_content:
        st.subheader("📱 Post Preview")

        for platform in platforms:
            content = platform_content[platform]
            with st.expander(f"{platform} Preview"):
                st.write(f"**Content:** {content['content']}")
                if content['hashtags']:
                    st.write(f"**Hashtags:** {content['hashtags']}")
                st.write(f"**Posting Time:** {content['posting_time']}")

                # Platform-specific preview styling
                if platform == "Twitter":
                    st.info("💙 Twitter post preview")
                elif platform == "Instagram":
                    st.info("📸 Instagram post preview")
                elif platform == "LinkedIn":
                    st.info("💼 LinkedIn post preview")

    # Post to platforms
    if st.button("🚀 Post to All Platforms") and main_content:
        posting_results = {}

        for platform in platforms:
            # Simulate posting
            success = simulate_cross_platform_post(platform, platform_content[platform])
            posting_results[platform] = success

        # Display results
        st.subheader("📊 Posting Results")

        successful_posts = sum(posting_results.values())
        failed_posts = len(platforms) - successful_posts

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Successful Posts", successful_posts)
        with col2:
            st.metric("Failed Posts", failed_posts)

        for platform, success in posting_results.items():
            status = "✅ Posted successfully" if success else "❌ Failed to post"
            st.write(f"**{platform}:** {status}")

        # Export posting report
        if st.button("Export Posting Report"):
            report = generate_posting_report(posting_results, platform_content)
            FileHandler.create_download_link(
                report.encode(),
                f"posting_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                "text/plain"
            )


def trending_hashtags():
    """Discover trending hashtags across platforms"""
    create_tool_header("Trending Hashtags", "Find the most popular hashtags for maximum reach", "#️⃣")

    # Search parameters
    st.subheader("Hashtag Discovery Settings")

    col1, col2 = st.columns(2)
    with col1:
        platform = st.selectbox("Platform", [
            "Instagram", "Twitter", "TikTok", "LinkedIn", "Pinterest", "All Platforms"
        ])
        category = st.selectbox("Category", [
            "All Categories", "Technology", "Fashion", "Food", "Travel", "Fitness",
            "Business", "Entertainment", "Sports", "News", "Art", "Music"
        ])

    with col2:
        time_period = st.selectbox("Time Period", [
            "Last 24 hours", "Last 7 days", "Last 30 days", "This month"
        ])
        hashtag_type = st.selectbox("Hashtag Type", [
            "All Types", "Trending", "Popular", "Emerging", "Seasonal"
        ])

    # Optional keyword input
    keywords = st.text_input("Keywords (optional)",
                             placeholder="Enter keywords to find related trending hashtags")

    if st.button("Find Trending Hashtags"):
        with st.spinner("Discovering trending hashtags..."):
            # Simulate hashtag discovery
            trending_data = simulate_trending_hashtags(platform, category, time_period, keywords)

            st.subheader(f"🔥 Trending Hashtags - {platform}")

            # Display trending hashtags in tabs
            tabs = st.tabs(["Top Trending", "Rising", "Category Specific", "Related"])

            with tabs[0]:  # Top Trending
                st.write("**Most Popular Right Now:**")
                for i, hashtag in enumerate(trending_data['top_trending'][:20], 1):
                    col1, col2, col3 = st.columns([2, 1, 1])
                    with col1:
                        st.write(f"**#{i}. #{hashtag['tag']}**")
                    with col2:
                        st.write(f"📊 {hashtag['posts']:,} posts")
                    with col3:
                        growth = hashtag['growth']
                        growth_color = "🟢" if growth > 0 else "🔴" if growth < 0 else "⚪"
                        st.write(f"{growth_color} {growth:+.1f}%")

            with tabs[1]:  # Rising
                st.write("**Rapidly Growing Hashtags:**")
                for hashtag in trending_data['rising'][:15]:
                    st.write(f"🚀 **#{hashtag['tag']}** - {hashtag['posts']:,} posts (+{hashtag['growth']:.1f}%)")

            with tabs[2]:  # Category Specific
                if category != "All Categories":
                    st.write(f"**{category} Hashtags:**")
                    for hashtag in trending_data['category_specific'][:15]:
                        st.write(f"📂 **#{hashtag['tag']}** - {hashtag['posts']:,} posts")
                else:
                    st.info("Select a specific category to see category-specific hashtags")

            with tabs[3]:  # Related
                if keywords:
                    st.write(f"**Related to '{keywords}':**")
                    for hashtag in trending_data['related'][:15]:
                        st.write(f"🔗 **#{hashtag['tag']}** - {hashtag['relevance']}% match")
                else:
                    st.info("Enter keywords to see related hashtags")

            # Hashtag strategy recommendations
            st.subheader("📈 Strategy Recommendations")
            recommendations = generate_hashtag_strategy_recommendations(trending_data, platform)

            for rec in recommendations:
                st.write(f"💡 {rec}")

            # Copy hashtags functionality
            st.subheader("📋 Quick Copy")
            all_trending = trending_data['top_trending'][:10]
            hashtag_string = ' '.join([f"#{h['tag']}" for h in all_trending])

            st.text_area("Copy these hashtags:", hashtag_string, height=100)

            # Export trending data
            if st.button("Export Trending Data"):
                export_text = generate_hashtag_export(trending_data, platform, category)
                FileHandler.create_download_link(
                    export_text.encode(),
                    f"trending_hashtags_{platform.lower()}_{datetime.now().strftime('%Y%m%d')}.txt",
                    "text/plain"
                )


def performance_tracker():
    """Track and analyze social media performance metrics"""
    create_tool_header("Performance Tracker", "Monitor your social media performance across platforms", "📊")

    # Data source selection
    st.subheader("Performance Data")

    data_source = st.selectbox("Data Source", [
        "Upload Analytics CSV", "Manual Entry", "Sample Data", "Platform Integration"
    ])

    performance_data = None

    if data_source == "Upload Analytics CSV":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                st.dataframe(df.head())
                performance_data = df.to_dict('records')

    elif data_source == "Sample Data":
        performance_data = generate_sample_performance_data()
        st.success("Using sample performance data")

    elif data_source == "Manual Entry":
        st.subheader("Enter Performance Data")

        num_posts = st.number_input("Number of Posts to Track", 1, 50, 10)
        performance_data = []

        for i in range(min(num_posts, 5)):  # Limit UI to 5 for demo
            with st.expander(f"Post {i + 1}"):
                col1, col2 = st.columns(2)

                with col1:
                    platform = st.selectbox(f"Platform", ["Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok"],
                                            key=f"perf_platform_{i}")
                    post_type = st.selectbox(f"Post Type", ["Image", "Video", "Carousel", "Text", "Story"],
                                             key=f"perf_type_{i}")
                    date = st.date_input(f"Post Date", key=f"perf_date_{i}")
                    time_posted = st.time_input(f"Time Posted", key=f"perf_time_{i}")

                with col2:
                    reach = st.number_input(f"Reach", 0, 10000000, 1000, key=f"perf_reach_{i}")
                    impressions = st.number_input(f"Impressions", 0, 10000000, 1500, key=f"perf_impressions_{i}")
                    likes = st.number_input(f"Likes", 0, 100000, 50, key=f"perf_likes_{i}")
                    comments = st.number_input(f"Comments", 0, 10000, 5, key=f"perf_comments_{i}")
                    shares = st.number_input(f"Shares", 0, 10000, 2, key=f"perf_shares_{i}")
                    clicks = st.number_input(f"Link Clicks", 0, 10000, 10, key=f"perf_clicks_{i}")

                engagement_rate = ((likes + comments + shares) / impressions * 100) if impressions > 0 else 0

                performance_data.append({
                    'platform': platform,
                    'post_type': post_type,
                    'date': date.isoformat(),
                    'time': time_posted.isoformat(),
                    'reach': reach,
                    'impressions': impressions,
                    'likes': likes,
                    'comments': comments,
                    'shares': shares,
                    'clicks': clicks,
                    'engagement_rate': engagement_rate
                })

    # Performance analysis
    if performance_data:
        st.subheader("📈 Performance Analysis")

        # Overall metrics
        total_posts = len(performance_data)
        total_reach = sum(post.get('reach', 0) for post in performance_data)
        total_impressions = sum(post.get('impressions', 0) for post in performance_data)
        total_engagement = sum(
            post.get('likes', 0) + post.get('comments', 0) + post.get('shares', 0) for post in performance_data)
        avg_engagement_rate = sum(
            post.get('engagement_rate', 0) for post in performance_data) / total_posts if total_posts > 0 else 0

        # Display key metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Total Posts", total_posts)
        with col2:
            st.metric("Total Reach", f"{total_reach:,}")
        with col3:
            st.metric("Total Impressions", f"{total_impressions:,}")
        with col4:
            st.metric("Total Engagement", f"{total_engagement:,}")
        with col5:
            st.metric("Avg Engagement Rate", f"{avg_engagement_rate:.2f}%")

        # Platform performance comparison
        st.subheader("Platform Comparison")
        platform_stats = analyze_platform_performance(performance_data)

        for platform, stats in platform_stats.items():
            with st.expander(f"{platform} Performance"):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Posts", stats['posts'])
                with col2:
                    st.metric("Avg Reach", f"{stats['avg_reach']:,.0f}")
                with col3:
                    st.metric("Avg Engagement", f"{stats['avg_engagement']:.2f}%")
                with col4:
                    st.metric("Best Performing", stats['best_post_type'])

        # Best performing content
        st.subheader("🏆 Top Performing Posts")
        top_posts = sorted(performance_data, key=lambda x: x.get('engagement_rate', 0), reverse=True)[:5]

        for i, post in enumerate(top_posts, 1):
            with st.expander(f"#{i} - {post.get('platform', 'Unknown')} {post.get('post_type', 'Post')}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Date:** {post.get('date', 'Unknown')}")
                    st.write(f"**Platform:** {post.get('platform', 'Unknown')}")
                    st.write(f"**Type:** {post.get('post_type', 'Unknown')}")
                with col2:
                    st.write(f"**Reach:** {post.get('reach', 0):,}")
                    st.write(f"**Impressions:** {post.get('impressions', 0):,}")
                    st.write(f"**Clicks:** {post.get('clicks', 0):,}")
                with col3:
                    st.write(f"**Likes:** {post.get('likes', 0):,}")
                    st.write(f"**Comments:** {post.get('comments', 0):,}")
                    st.write(f"**Engagement Rate:** {post.get('engagement_rate', 0):.2f}%")

        # Performance insights
        st.subheader("🔍 Performance Insights")
        insights = generate_performance_insights(performance_data)

        for insight in insights:
            st.write(f"💡 {insight}")

        # Export performance report
        if st.button("Export Performance Report"):
            report = generate_performance_report(performance_data, platform_stats)
            FileHandler.create_download_link(
                report.encode(),
                f"performance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                "text/plain"
            )


def ab_testing():
    """Set up and analyze A/B tests for social media content"""
    create_tool_header("A/B Testing", "Test different content variations to optimize performance", "🧪")

    # Test setup
    st.subheader("A/B Test Setup")

    col1, col2 = st.columns(2)
    with col1:
        test_name = st.text_input("Test Name", placeholder="e.g., Header Image Test")
        test_objective = st.selectbox("Primary Objective", [
            "Increase Engagement Rate", "Boost Click-through Rate", "Improve Reach",
            "Maximize Likes", "Increase Comments", "Drive Website Traffic"
        ])
        platform = st.selectbox("Platform", ["Instagram", "Facebook", "Twitter", "LinkedIn", "TikTok"])

    with col2:
        test_duration = st.number_input("Test Duration (days)", 1, 30, 7)
        audience_split = st.selectbox("Audience Split", ["50/50", "60/40", "70/30", "Custom"])
        confidence_level = st.selectbox("Confidence Level", ["90%", "95%", "99%"])

    # Content variations
    st.subheader("Content Variations")

    # Variation A
    st.write("**Variation A (Control)**")
    col1, col2 = st.columns(2)
    with col1:
        content_a = st.text_area("Content A", height=100, placeholder="Enter your control content...")
        hashtags_a = st.text_input("Hashtags A", placeholder="#hashtag1 #hashtag2")
    with col2:
        post_time_a = st.time_input("Posting Time A", key="time_a")
        cta_a = st.text_input("Call-to-Action A", placeholder="Learn more", key="cta_a")

    # Variation B
    st.write("**Variation B (Test)**")
    col1, col2 = st.columns(2)
    with col1:
        content_b = st.text_area("Content B", height=100, placeholder="Enter your test content...")
        hashtags_b = st.text_input("Hashtags B", placeholder="#hashtag1 #hashtag2")
    with col2:
        post_time_b = st.time_input("Posting Time B", key="time_b")
        cta_b = st.text_input("Call-to-Action B", placeholder="Discover now", key="cta_b")

    # Test variables
    st.subheader("What Are You Testing?")
    test_variables = st.multiselect("Test Variables", [
        "Content Copy", "Hashtags", "Posting Time", "Call-to-Action",
        "Image/Video", "Caption Length", "Emoji Usage", "Question vs Statement"
    ])

    # Hypothesis
    hypothesis = st.text_area("Hypothesis",
                              placeholder="I believe that [variation B] will perform better than [variation A] because...")

    # Launch test
    if st.button("Launch A/B Test") and test_name and content_a and content_b:
        # Create test configuration
        test_config = {
            'test_name': test_name,
            'objective': test_objective,
            'platform': platform,
            'duration': test_duration,
            'audience_split': audience_split,
            'confidence_level': confidence_level,
            'variation_a': {
                'content': content_a,
                'hashtags': hashtags_a,
                'post_time': post_time_a.isoformat(),
                'cta': cta_a
            },
            'variation_b': {
                'content': content_b,
                'hashtags': hashtags_b,
                'post_time': post_time_b.isoformat(),
                'cta': cta_b
            },
            'test_variables': test_variables,
            'hypothesis': hypothesis,
            'start_date': datetime.now().isoformat()
        }

        st.success(f"✅ A/B Test '{test_name}' has been launched!")

        # Simulate test results (in real implementation, this would track actual performance)
        with st.spinner("Simulating test results..."):
            test_results = simulate_ab_test_results(test_config)

            st.subheader("📊 Test Results")

            # Results overview
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Test Status", "Completed" if test_results['is_significant'] else "Ongoing")
            with col2:
                st.metric("Statistical Significance", "Yes" if test_results['is_significant'] else "No")
            with col3:
                winner = "Variation B" if test_results['winner'] == 'B' else "Variation A"
                st.metric("Winner", winner)

            # Detailed comparison
            st.subheader("Detailed Comparison")

            comparison_data = {
                'Metric': ['Impressions', 'Reach', 'Likes', 'Comments', 'Shares', 'Clicks', 'Engagement Rate'],
                'Variation A': [
                    f"{test_results['variation_a']['impressions']:,}",
                    f"{test_results['variation_a']['reach']:,}",
                    f"{test_results['variation_a']['likes']:,}",
                    f"{test_results['variation_a']['comments']:,}",
                    f"{test_results['variation_a']['shares']:,}",
                    f"{test_results['variation_a']['clicks']:,}",
                    f"{test_results['variation_a']['engagement_rate']:.2f}%"
                ],
                'Variation B': [
                    f"{test_results['variation_b']['impressions']:,}",
                    f"{test_results['variation_b']['reach']:,}",
                    f"{test_results['variation_b']['likes']:,}",
                    f"{test_results['variation_b']['comments']:,}",
                    f"{test_results['variation_b']['shares']:,}",
                    f"{test_results['variation_b']['clicks']:,}",
                    f"{test_results['variation_b']['engagement_rate']:.2f}%"
                ],
                'Improvement': [
                    f"{test_results['improvements']['impressions']:+.1f}%",
                    f"{test_results['improvements']['reach']:+.1f}%",
                    f"{test_results['improvements']['likes']:+.1f}%",
                    f"{test_results['improvements']['comments']:+.1f}%",
                    f"{test_results['improvements']['shares']:+.1f}%",
                    f"{test_results['improvements']['clicks']:+.1f}%",
                    f"{test_results['improvements']['engagement_rate']:+.1f}%"
                ]
            }

            st.table(comparison_data)

            # Key insights
            st.subheader("🔍 Key Insights")
            for insight in test_results['insights']:
                st.write(f"💡 {insight}")

            # Recommendations
            st.subheader("📋 Recommendations")
            for rec in test_results['recommendations']:
                st.write(f"✅ {rec}")

            # Export test results
            if st.button("Export Test Results"):
                report = generate_ab_test_report(test_config, test_results)
                FileHandler.create_download_link(
                    report.encode(),
                    f"ab_test_{test_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.txt",
                    "text/plain"
                )


def brand_tracking():
    """Track brand sentiment and performance across social media"""
    create_tool_header("Brand Tracking", "Monitor your brand's social media presence and sentiment", "🏷️")

    # Brand setup
    st.subheader("Brand Monitoring Setup")

    col1, col2 = st.columns(2)
    with col1:
        brand_name = st.text_input("Brand Name", placeholder="Enter your brand name")
        brand_handles = st.text_area("Social Media Handles",
                                     placeholder="@brandname (one per line)", height=100)
        competitors = st.text_area("Competitor Brands",
                                   placeholder="Enter competitor names (one per line)", height=100)

    with col2:
        tracking_period = st.selectbox("Tracking Period", [
            "Last 7 days", "Last 30 days", "Last 3 months", "Custom Range"
        ])
        platforms = st.multiselect("Platforms to Monitor", [
            "Twitter", "Instagram", "Facebook", "LinkedIn", "TikTok", "YouTube", "Reddit"
        ], default=["Twitter", "Instagram", "Facebook"])
        industries = st.multiselect("Industry Keywords", [
            "Technology", "Fashion", "Food", "Finance", "Healthcare", "Education", "Other"
        ])

    if brand_name and st.button("Start Brand Tracking"):
        with st.spinner("Analyzing brand presence..."):
            # Simulate brand tracking data
            brand_data = simulate_brand_tracking(brand_name, platforms, tracking_period)

            # Brand overview
            st.subheader(f"📊 {brand_name} Brand Overview")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Mentions", f"{brand_data['total_mentions']:,}")
            with col2:
                sentiment_score = brand_data['sentiment_score']
                sentiment_emoji = "😊" if sentiment_score > 0.6 else "😐" if sentiment_score > 0.3 else "😞"
                st.metric("Sentiment Score", f"{sentiment_score:.1f}/5.0 {sentiment_emoji}")
            with col3:
                st.metric("Reach", f"{brand_data['total_reach']:,}")
            with col4:
                st.metric("Share of Voice", f"{brand_data['share_of_voice']:.1f}%")

            # Sentiment breakdown
            st.subheader("Sentiment Analysis")

            col1, col2, col3 = st.columns(3)
            with col1:
                positive_pct = brand_data['sentiment_breakdown']['positive']
                st.metric("Positive", f"{positive_pct:.1f}%", f"+{positive_pct - 33.3:.1f}%")
                st.progress(positive_pct / 100)

            with col2:
                neutral_pct = brand_data['sentiment_breakdown']['neutral']
                st.metric("Neutral", f"{neutral_pct:.1f}%")
                st.progress(neutral_pct / 100)

            with col3:
                negative_pct = brand_data['sentiment_breakdown']['negative']
                st.metric("Negative", f"{negative_pct:.1f}%", f"{negative_pct - 33.3:.1f}%")
                st.progress(negative_pct / 100)

            # Platform performance
            st.subheader("Platform Performance")

            for platform_name, platform_data in brand_data['platform_breakdown'].items():
                with st.expander(f"{platform_name} Performance"):
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Mentions", f"{platform_data['mentions']:,}")
                    with col2:
                        st.metric("Engagement", f"{platform_data['engagement']:,}")
                    with col3:
                        st.metric("Reach", f"{platform_data['reach']:,}")
                    with col4:
                        st.metric("Sentiment", f"{platform_data['sentiment']:.1f}/5.0")

            # Recent mentions
            st.subheader("Recent Brand Mentions")

            for mention in brand_data['recent_mentions'][:10]:
                sentiment_color = {
                    'positive': '🟢',
                    'negative': '🔴',
                    'neutral': '🟡'
                }.get(mention['sentiment'], '⚪')

                with st.expander(f"{sentiment_color} {mention['platform']} - {mention['author']}"):
                    st.write(f"**Content:** {mention['content']}")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Date:** {mention['date']}")
                    with col2:
                        st.write(f"**Engagement:** {mention['engagement']}")
                    with col3:
                        st.write(f"**Reach:** {mention['reach']}")

            # Competitor comparison
            if competitors:
                st.subheader("Competitor Comparison")
                competitor_list = [c.strip() for c in competitors.split('\n') if c.strip()]

                comparison_data = simulate_competitor_comparison(brand_name, competitor_list)

                for competitor, data in comparison_data.items():
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.write(f"**{competitor}**")
                    with col2:
                        st.write(f"Mentions: {data['mentions']:,}")
                    with col3:
                        st.write(f"Sentiment: {data['sentiment']:.1f}/5.0")
                    with col4:
                        vs_brand = data['mentions'] - brand_data['total_mentions']
                        st.write(f"vs {brand_name}: {vs_brand:+,}")

            # Brand insights
            st.subheader("📈 Brand Insights")
            insights = generate_brand_insights(brand_data, brand_name)

            for insight in insights:
                st.write(f"💡 {insight}")

            # Action items
            st.subheader("🎯 Recommended Actions")
            actions = generate_brand_action_items(brand_data)

            for action in actions:
                st.write(f"✅ {action}")

            # Export brand report
            if st.button("Export Brand Report"):
                report = generate_brand_report(brand_data, brand_name)
                FileHandler.create_download_link(
                    report.encode(),
                    f"brand_report_{brand_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.txt",
                    "text/plain"
                )


# Helper Functions for Social Media Tools

def generate_sample_audience_data():
    """Generate sample audience data for demonstration"""
    return [
        {
            'segment_name': 'Tech Enthusiasts',
            'age_range': '25-34',
            'gender': 'All',
            'location': 'United States',
            'interests': ['technology', 'innovation', 'startups'],
            'platforms': ['LinkedIn', 'Twitter', 'Instagram'],
            'engagement_level': 'High',
            'spending_power': 'High'
        },
        {
            'segment_name': 'Young Professionals',
            'age_range': '25-34',
            'gender': 'All',
            'location': 'Global',
            'interests': ['career', 'networking', 'business'],
            'platforms': ['LinkedIn', 'Instagram'],
            'engagement_level': 'Medium',
            'spending_power': 'Medium'
        },
        {
            'segment_name': 'Creative Millennials',
            'age_range': '25-34',
            'gender': 'All',
            'location': 'Urban areas',
            'interests': ['design', 'art', 'creativity'],
            'platforms': ['Instagram', 'TikTok', 'Pinterest'],
            'engagement_level': 'High',
            'spending_power': 'Medium'
        }
    ]


def analyze_audience_segments(audience_data, primary_criteria, secondary_criteria):
    """Analyze audience segments based on criteria"""
    segments = []

    for i, segment in enumerate(audience_data):
        segment_analysis = {
            'name': segment.get('segment_name', f'Segment {i + 1}'),
            'percentage': random.uniform(15, 35),
            'demographics': {
                'age': segment.get('age_range', 'Unknown'),
                'gender': segment.get('gender', 'All'),
                'location': segment.get('location', 'Global')
            },
            'behavior': {
                'engagement': segment.get('engagement_level', 'Medium'),
                'activity': random.choice(['High', 'Medium', 'Low'])
            },
            'platforms': segment.get('platforms', []),
            'interests': segment.get('interests', []),
            'recommendations': [
                f"Target during peak {random.choice(['morning', 'afternoon', 'evening'])} hours",
                f"Use {random.choice(['visual', 'video', 'text'])} content for best engagement",
                f"Focus on {random.choice(['educational', 'entertaining', 'promotional'])} content"
            ]
        }
        segments.append(segment_analysis)

    # Sort by percentage
    segments.sort(key=lambda x: x['percentage'], reverse=True)

    return {
        'segments': segments,
        'largest_segment': segments[0] if segments else {'name': 'None'},
        'most_engaged': max(segments,
                            key=lambda x: 1 if x['behavior']['engagement'] == 'High' else 0) if segments else {
            'name': 'None'},
        'high_value': {'count': len([s for s in segments if s['demographics']['age'] in ['25-34', '35-44']])},
        'marketing_recommendations': {
            'content_strategy': [
                "Create platform-specific content for each segment",
                "Use data-driven insights to optimize posting times",
                "Develop personalized messaging for each segment"
            ],
            'targeting': [
                "Use lookalike audiences based on your best segments",
                "Implement retargeting campaigns for engaged users",
                "Test different ad formats for each segment"
            ],
            'engagement': [
                "Respond quickly to comments and messages",
                "Create interactive content like polls and Q&As",
                "Build community through user-generated content"
            ]
        }
    }


def generate_segmentation_report(analysis_results, audience_data):
    """Generate a text report of segmentation analysis"""
    report = f"AUDIENCE SEGMENTATION REPORT\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += "=" * 50 + "\n\n"

    report += "EXECUTIVE SUMMARY\n"
    report += f"Total Segments Analyzed: {len(analysis_results['segments'])}\n"
    report += f"Largest Segment: {analysis_results['largest_segment']['name']}\n"
    report += f"Most Engaged Segment: {analysis_results['most_engaged']['name']}\n\n"

    report += "DETAILED SEGMENT ANALYSIS\n"
    for segment in analysis_results['segments']:
        report += f"\n{segment['name']} ({segment['percentage']:.1f}%)\n"
        report += f"- Demographics: {segment['demographics']['age']}, {segment['demographics']['gender']}, {segment['demographics']['location']}\n"
        report += f"- Platforms: {', '.join(segment['platforms'])}\n"
        report += f"- Interests: {', '.join(segment['interests'])}\n"
        report += f"- Engagement: {segment['behavior']['engagement']}\n"

    return report


def generate_platform_recommendations(platform, campaign_type, target_audience):
    """Generate platform-specific recommendations"""
    recommendations = {
        'Instagram': [
            "Use high-quality visuals and Stories",
            "Post consistently with relevant hashtags",
            "Engage with user-generated content",
            "Utilize Instagram Shopping features"
        ],
        'Facebook': [
            "Create engaging video content",
            "Use Facebook Groups for community building",
            "Leverage Facebook Ads for precise targeting",
            "Share behind-the-scenes content"
        ],
        'Twitter': [
            "Join trending conversations",
            "Use relevant hashtags and mentions",
            "Share timely, news-worthy content",
            "Engage in real-time conversations"
        ],
        'LinkedIn': [
            "Share professional insights and thought leadership",
            "Use LinkedIn Articles for long-form content",
            "Engage in industry-specific groups",
            "Share company updates and achievements"
        ],
        'TikTok': [
            "Create short, entertaining videos",
            "Use trending sounds and effects",
            "Collaborate with TikTok creators",
            "Post consistently to maintain visibility"
        ]
    }

    return recommendations.get(platform,
                               ["Customize content for platform-specific audience", "Monitor engagement metrics",
                                "Test different content formats"])


def generate_campaign_plan_report(campaign_data):
    """Generate a comprehensive campaign plan report"""
    report = f"SOCIAL MEDIA CAMPAIGN PLAN: {campaign_data['campaign_name']}\n"
    report += "=" * 60 + "\n\n"

    report += f"Campaign Type: {campaign_data['campaign_type']}\n"
    report += f"Duration: {campaign_data['start_date']} to {campaign_data['end_date']}\n"
    report += f"Target Audience: {campaign_data['target_audience']}\n"
    report += f"Budget: ${campaign_data['budget']:,}\n"
    report += f"Primary Goal: {campaign_data['primary_goal']}\n"
    report += f"Platforms: {', '.join(campaign_data['platforms'])}\n\n"

    report += "OBJECTIVES\n"
    for obj in campaign_data['objectives']:
        report += f"- {obj['name']}: {obj['target']} {obj['metric']} ({obj['timeframe']})\n"

    report += f"\nCONTENT STRATEGY\n"
    report += f"Themes: {campaign_data['content_themes']}\n"
    report += f"Types: {', '.join(campaign_data['content_types'])}\n\n"

    report += "BUDGET ALLOCATION\n"
    for platform, budget in campaign_data['budget_allocation'].items():
        report += f"- {platform}: ${budget:,}\n"

    report += f"\nMILESTONES\n"
    for milestone in campaign_data['milestones']:
        report += f"- {milestone['date']}: {milestone['name']} ({milestone['owner']})\n"

    return report


def simulate_mention_monitoring(brand_list, platforms, monitoring_period):
    """Simulate mention monitoring results"""
    mentions = []

    for brand in brand_list:
        for platform in platforms:
            num_mentions = random.randint(5, 50)

            for i in range(num_mentions):
                mention = {
                    'brand': brand,
                    'platform': platform,
                    'author': f"user_{random.randint(1000, 9999)}",
                    'content': f"Just tried {brand}! {random.choice(['Amazing product!', 'Great service!', 'Could be better', 'Love it!', 'Not impressed'])}",
                    'date': (datetime.now() - timedelta(days=random.randint(0, 7))).strftime('%Y-%m-%d'),
                    'sentiment': random.choice(['positive', 'negative', 'neutral']),
                    'engagement': random.randint(10, 1000),
                    'reach': random.randint(100, 10000)
                }
                mentions.append(mention)

    return mentions


def generate_mentions_report(mentions_data, brand_list):
    """Generate mentions monitoring report"""
    report = f"BRAND MENTIONS REPORT\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Brands Monitored: {', '.join(brand_list)}\n"
    report += "=" * 50 + "\n\n"

    total_mentions = len(mentions_data)
    positive = len([m for m in mentions_data if m['sentiment'] == 'positive'])
    negative = len([m for m in mentions_data if m['sentiment'] == 'negative'])
    neutral = len([m for m in mentions_data if m['sentiment'] == 'neutral'])

    report += f"SUMMARY\n"
    report += f"Total Mentions: {total_mentions}\n"
    report += f"Positive: {positive} ({positive / total_mentions * 100:.1f}%)\n"
    report += f"Negative: {negative} ({negative / total_mentions * 100:.1f}%)\n"
    report += f"Neutral: {neutral} ({neutral / total_mentions * 100:.1f}%)\n\n"

    # Platform breakdown
    platform_counts = {}
    for mention in mentions_data:
        platform = mention['platform']
        platform_counts[platform] = platform_counts.get(platform, 0) + 1

    report += "PLATFORM BREAKDOWN\n"
    for platform, count in platform_counts.items():
        report += f"- {platform}: {count} mentions\n"

    return report


def simulate_influencer_search(niche, platforms, follower_range):
    """Simulate influencer search results"""
    influencers = []

    follower_ranges = {
        "Nano (1K-10K)": (1000, 10000),
        "Micro (10K-100K)": (10000, 100000),
        "Mid-tier (100K-1M)": (100000, 1000000),
        "Macro (1M-10M)": (1000000, 10000000),
        "Mega (10M+)": (10000000, 50000000),
        "Any Size": (1000, 50000000)
    }

    min_followers, max_followers = follower_ranges.get(follower_range, (1000, 100000))

    for i in range(10):  # Generate 10 influencers
        followers = random.randint(min_followers, max_followers)
        engagement_rate = random.uniform(1.5, 8.0)

        influencer = {
            'name': f"{random.choice(['Alex', 'Jordan', 'Taylor', 'Casey', 'Morgan'])} {random.choice(['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson'])}",
            'username': f"{niche.lower()}_guru_{random.randint(100, 999)}",
            'platform': random.choice(platforms),
            'followers': followers,
            'engagement_rate': engagement_rate,
            'avg_likes': int(followers * engagement_rate / 100 * 0.8),
            'avg_comments': int(followers * engagement_rate / 100 * 0.2),
            'location': random.choice(['United States', 'Canada', 'United Kingdom', 'Australia', 'Global']),
            'category': niche,
            'post_frequency': random.choice(['Daily', '3-4 times/week', 'Weekly', '2-3 times/week']),
            'estimated_cost': f"${random.randint(100, 5000)}",
            'availability': random.choice(['Available', 'Busy until next month', 'Selective collaborations']),
            'brand_safety': random.choice(['Excellent', 'Good', 'Fair']),
            'bio': f"Passionate {niche.lower()} enthusiast sharing tips and insights. Sponsored by various brands.",
            'audience_insights': {
                'demographics': {
                    '18-24': random.randint(20, 40),
                    '25-34': random.randint(30, 50),
                    '35-44': random.randint(15, 25),
                    '45+': random.randint(5, 15)
                },
                'interests': [f"{niche} trends", "Lifestyle", "Shopping", "Entertainment"]
            }
        }
        influencers.append(influencer)

    return sorted(influencers, key=lambda x: x['engagement_rate'], reverse=True)


def generate_influencer_export(influencers, niche):
    """Generate CSV export of influencer data"""
    csv_data = "Name,Username,Platform,Followers,Engagement Rate,Estimated Cost,Location,Availability\n"

    for influencer in influencers:
        csv_data += f"{influencer['name']},{influencer['username']},{influencer['platform']},{influencer['followers']},{influencer['engagement_rate']:.1f}%,{influencer['estimated_cost']},{influencer['location']},{influencer['availability']}\n"

    return csv_data


def simulate_cross_platform_post(platform, content_data):
    """Simulate posting to a platform"""
    # Simulate success/failure (90% success rate)
    return random.random() > 0.1


def generate_posting_report(posting_results, platform_content):
    """Generate cross-platform posting report"""
    report = f"CROSS-PLATFORM POSTING REPORT\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += "=" * 50 + "\n\n"

    successful = sum(posting_results.values())
    total = len(posting_results)

    report += f"POSTING SUMMARY\n"
    report += f"Total Platforms: {total}\n"
    report += f"Successful Posts: {successful}\n"
    report += f"Failed Posts: {total - successful}\n"
    report += f"Success Rate: {successful / total * 100:.1f}%\n\n"

    report += "PLATFORM RESULTS\n"
    for platform, success in posting_results.items():
        status = "SUCCESS" if success else "FAILED"
        report += f"- {platform}: {status}\n"

    return report


def simulate_trending_hashtags(platform, category, time_period, keywords):
    """Simulate trending hashtag discovery"""
    base_hashtags = {
        'Technology': ['tech', 'innovation', 'AI', 'startup', 'digital', 'coding', 'software'],
        'Fashion': ['fashion', 'style', 'outfit', 'trending', 'designer', 'streetstyle', 'ootd'],
        'Food': ['food', 'recipe', 'delicious', 'cooking', 'foodie', 'yummy', 'instafood'],
        'Travel': ['travel', 'wanderlust', 'vacation', 'explore', 'adventure', 'travelgram'],
        'Fitness': ['fitness', 'workout', 'gym', 'health', 'motivation', 'strong', 'fitlife']
    }

    category_tags = base_hashtags.get(category, ['trending', 'popular', 'viral'])

    trending_data = {
        'top_trending': [],
        'rising': [],
        'category_specific': [],
        'related': []
    }

    # Generate top trending
    for i, tag in enumerate(category_tags[:10]):
        trending_data['top_trending'].append({
            'tag': tag,
            'posts': random.randint(50000, 500000),
            'growth': random.uniform(-10, 50)
        })

    # Generate rising hashtags
    for i in range(15):
        trending_data['rising'].append({
            'tag': f"{random.choice(category_tags)}{random.randint(2024, 2025)}",
            'posts': random.randint(1000, 50000),
            'growth': random.uniform(20, 200)
        })

    # Category specific
    if category != "All Categories":
        for tag in category_tags:
            trending_data['category_specific'].append({
                'tag': f"{tag}{random.choice(['daily', 'tips', 'life', 'vibes'])}",
                'posts': random.randint(10000, 100000)
            })

    # Related to keywords
    if keywords:
        keyword_list = [k.strip() for k in keywords.split(',')]
        for keyword in keyword_list[:5]:
            trending_data['related'].append({
                'tag': f"{keyword}{random.choice(['love', 'life', 'daily', 'tips'])}",
                'relevance': random.randint(70, 95)
            })

    return trending_data


def generate_hashtag_strategy_recommendations(trending_data, platform):
    """Generate hashtag strategy recommendations"""
    recommendations = [
        f"Use 3-5 trending hashtags from the top list to maximize reach on {platform}",
        "Mix popular and niche hashtags for better engagement",
        "Monitor hashtag performance and adjust strategy weekly",
        "Create branded hashtags to build community",
        "Avoid overusing hashtags - quality over quantity"
    ]

    if platform == "Instagram":
        recommendations.append("Use up to 30 hashtags but focus on the most relevant ones")
    elif platform == "Twitter":
        recommendations.append("Limit to 2-3 hashtags per tweet for better engagement")
    elif platform == "LinkedIn":
        recommendations.append("Use 3-5 professional hashtags relevant to your industry")

    return recommendations


def generate_hashtag_export(trending_data, platform, category):
    """Generate hashtag export data"""
    export_text = f"TRENDING HASHTAGS REPORT - {platform}\n"
    export_text += f"Category: {category}\n"
    export_text += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    export_text += "=" * 50 + "\n\n"

    export_text += "TOP TRENDING HASHTAGS\n"
    for i, hashtag in enumerate(trending_data['top_trending'][:20], 1):
        export_text += f"{i}. #{hashtag['tag']} - {hashtag['posts']:,} posts\n"

    export_text += "\nRISING HASHTAGS\n"
    for hashtag in trending_data['rising'][:10]:
        export_text += f"#{hashtag['tag']} - {hashtag['posts']:,} posts (+{hashtag['growth']:.1f}%)\n"

    return export_text


def generate_sample_performance_data():
    """Generate sample performance data"""
    platforms = ['Instagram', 'Facebook', 'Twitter', 'LinkedIn', 'TikTok']
    post_types = ['Image', 'Video', 'Carousel', 'Text', 'Story']

    data = []
    for i in range(20):
        platform = random.choice(platforms)
        post_type = random.choice(post_types)
        impressions = random.randint(1000, 50000)
        reach = int(impressions * random.uniform(0.6, 0.9))
        likes = int(impressions * random.uniform(0.01, 0.05))
        comments = int(likes * random.uniform(0.05, 0.2))
        shares = int(likes * random.uniform(0.02, 0.1))
        clicks = int(impressions * random.uniform(0.005, 0.02))
        engagement_rate = (likes + comments + shares) / impressions * 100

        data.append({
            'platform': platform,
            'post_type': post_type,
            'date': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
            'reach': reach,
            'impressions': impressions,
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'clicks': clicks,
            'engagement_rate': engagement_rate
        })

    return data


def generate_performance_insights(performance_data):
    """Generate performance insights"""
    insights = []

    # Analyze best performing platform
    platform_performance = {}
    for post in performance_data:
        platform = post['platform']
        if platform not in platform_performance:
            platform_performance[platform] = []
        platform_performance[platform].append(post['engagement_rate'])

    best_platform = max(platform_performance.items(), key=lambda x: sum(x[1]) / len(x[1]))[0]
    insights.append(f"{best_platform} shows the highest average engagement rate")

    # Analyze best post type
    type_performance = {}
    for post in performance_data:
        post_type = post['post_type']
        if post_type not in type_performance:
            type_performance[post_type] = []
        type_performance[post_type].append(post['engagement_rate'])

    best_type = max(type_performance.items(), key=lambda x: sum(x[1]) / len(x[1]))[0]
    insights.append(f"{best_type} posts generate the best engagement")

    # General insights
    avg_engagement = sum(post['engagement_rate'] for post in performance_data) / len(performance_data)
    insights.append(f"Overall average engagement rate is {avg_engagement:.2f}%")

    insights.append("Post consistently during peak hours for better reach")
    insights.append("Focus on creating more interactive content to boost engagement")

    return insights


def generate_performance_report(performance_data, platform_stats):
    """Generate comprehensive performance report"""
    report = f"SOCIAL MEDIA PERFORMANCE REPORT\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += "=" * 50 + "\n\n"

    total_posts = len(performance_data)
    total_reach = sum(post.get('reach', 0) for post in performance_data)
    total_impressions = sum(post.get('impressions', 0) for post in performance_data)
    total_engagement = sum(
        post.get('likes', 0) + post.get('comments', 0) + post.get('shares', 0) for post in performance_data)

    report += f"OVERVIEW\n"
    report += f"Total Posts: {total_posts}\n"
    report += f"Total Reach: {total_reach:,}\n"
    report += f"Total Impressions: {total_impressions:,}\n"
    report += f"Total Engagement: {total_engagement:,}\n\n"

    report += "PLATFORM PERFORMANCE\n"
    for platform, stats in platform_stats.items():
        report += f"\n{platform}:\n"
        report += f"  Posts: {stats['posts']}\n"
        report += f"  Avg Reach: {stats['avg_reach']:,.0f}\n"
        report += f"  Avg Engagement: {stats['avg_engagement']:.2f}%\n"

    return report


def simulate_ab_test_results(test_config):
    """Simulate A/B test results"""
    # Generate realistic performance data
    variation_a_impressions = random.randint(5000, 15000)
    variation_b_impressions = random.randint(5000, 15000)

    variation_a_reach = int(variation_a_impressions * random.uniform(0.7, 0.9))
    variation_a_likes = int(variation_a_impressions * random.uniform(0.02, 0.04))
    variation_a_comments = int(variation_a_impressions * random.uniform(0.003, 0.008))
    variation_a_shares = int(variation_a_impressions * random.uniform(0.001, 0.005))
    variation_a_clicks = int(variation_a_impressions * random.uniform(0.01, 0.03))
    variation_a_engagement_rate = (
                                          variation_a_likes + variation_a_comments + variation_a_shares) / variation_a_impressions * 100

    variation_a = {
        'impressions': variation_a_impressions,
        'reach': variation_a_reach,
        'likes': variation_a_likes,
        'comments': variation_a_comments,
        'shares': variation_a_shares,
        'clicks': variation_a_clicks,
        'engagement_rate': variation_a_engagement_rate,
    }

    # Variation B performs slightly better (or worse)
    performance_multiplier = random.uniform(0.9, 1.3)
    variation_b_reach = int(variation_b_impressions * random.uniform(0.7, 0.9))
    variation_b_likes = int(variation_b_impressions * random.uniform(0.02, 0.04) * performance_multiplier)
    variation_b_comments = int(variation_b_impressions * random.uniform(0.003, 0.008) * performance_multiplier)
    variation_b_shares = int(variation_b_impressions * random.uniform(0.001, 0.005) * performance_multiplier)
    variation_b_clicks = int(variation_b_impressions * random.uniform(0.01, 0.03) * performance_multiplier)
    variation_b_engagement_rate = (
                                          variation_b_likes + variation_b_comments + variation_b_shares) / variation_b_impressions * 100

    variation_b = {
        'impressions': variation_b_impressions,
        'reach': variation_b_reach,
        'likes': variation_b_likes,
        'comments': variation_b_comments,
        'shares': variation_b_shares,
        'clicks': variation_b_clicks,
        'engagement_rate': variation_b_engagement_rate,
    }

    # Calculate improvements
    improvements = {}
    for metric in ['impressions', 'reach', 'likes', 'comments', 'shares', 'clicks', 'engagement_rate']:
        improvement = ((variation_b[metric] - variation_a[metric]) / variation_a[metric] * 100) if variation_a[
                                                                                                       metric] > 0 else 0
        improvements[metric] = improvement

    # Determine winner and significance
    winner = 'B' if variation_b['engagement_rate'] > variation_a['engagement_rate'] else 'A'
    is_significant = abs(improvements['engagement_rate']) > 5  # 5% threshold

    insights = [
        f"Variation {winner} performed better overall",
        f"Engagement rate improved by {abs(improvements['engagement_rate']):.1f}%",
        "Consider implementing the winning variation" if is_significant else "Results show no significant difference"
    ]

    recommendations = [
        f"Implement Variation {winner} for future campaigns" if is_significant else "Continue testing with larger sample size",
        "Monitor long-term performance to confirm results",
        "Test additional variables to further optimize performance"
    ]

    return {
        'variation_a': variation_a,
        'variation_b': variation_b,
        'improvements': improvements,
        'winner': winner,
        'is_significant': is_significant,
        'insights': insights,
        'recommendations': recommendations
    }


def generate_ab_test_report(test_config, test_results):
    """Generate A/B test report"""
    report = f"A/B TEST REPORT: {test_config['test_name']}\n"
    report += "=" * 50 + "\n\n"

    report += f"Test Objective: {test_config['objective']}\n"
    report += f"Platform: {test_config['platform']}\n"
    report += f"Duration: {test_config['duration']} days\n"
    report += f"Hypothesis: {test_config['hypothesis']}\n\n"

    report += "RESULTS SUMMARY\n"
    report += f"Winner: Variation {test_results['winner']}\n"
    report += f"Statistical Significance: {'Yes' if test_results['is_significant'] else 'No'}\n"
    report += f"Engagement Rate Improvement: {test_results['improvements']['engagement_rate']:+.1f}%\n\n"

    report += "DETAILED METRICS\n"
    metrics = ['impressions', 'reach', 'likes', 'comments', 'shares', 'clicks']
    for metric in metrics:
        report += f"{metric.title()}: {test_results['variation_a'][metric]:,} vs {test_results['variation_b'][metric]:,} ({test_results['improvements'][metric]:+.1f}%)\n"

    report += "\nRECOMMENDATIONS\n"
    for rec in test_results['recommendations']:
        report += f"- {rec}\n"

    return report


def simulate_brand_tracking(brand_name, platforms, tracking_period):
    """Simulate brand tracking data"""
    total_mentions = random.randint(500, 2000)
    sentiment_score = random.uniform(2.5, 4.5)

    # Generate sentiment breakdown
    positive_pct = random.uniform(30, 60)
    negative_pct = random.uniform(10, 25)
    neutral_pct = 100 - positive_pct - negative_pct

    # Platform breakdown
    platform_breakdown = {}
    remaining_mentions = total_mentions

    for i, platform in enumerate(platforms):
        if i == len(platforms) - 1:  # Last platform gets remaining mentions
            mentions = remaining_mentions
        else:
            mentions = random.randint(50, remaining_mentions // 2)
            remaining_mentions -= mentions

        platform_breakdown[platform] = {
            'mentions': mentions,
            'engagement': random.randint(mentions * 2, mentions * 5),
            'reach': random.randint(mentions * 10, mentions * 50),
            'sentiment': random.uniform(2.0, 5.0)
        }

    # Generate recent mentions
    recent_mentions = []
    for i in range(15):
        recent_mentions.append({
            'platform': random.choice(platforms),
            'author': f"user_{random.randint(1000, 9999)}",
            'content': f"Just tried {brand_name}! {random.choice(['Amazing experience!', 'Really impressed', 'Could be better', 'Love this brand!', 'Not what I expected'])}",
            'date': (datetime.now() - timedelta(days=random.randint(0, 7))).strftime('%Y-%m-%d'),
            'sentiment': random.choice(['positive', 'negative', 'neutral']),
            'engagement': random.randint(5, 100),
            'reach': random.randint(100, 5000)
        })

    return {
        'total_mentions': total_mentions,
        'sentiment_score': sentiment_score,
        'total_reach': sum(p['reach'] for p in platform_breakdown.values()),
        'share_of_voice': random.uniform(5, 25),
        'sentiment_breakdown': {
            'positive': positive_pct,
            'negative': negative_pct,
            'neutral': neutral_pct
        },
        'platform_breakdown': platform_breakdown,
        'recent_mentions': recent_mentions
    }


def simulate_competitor_comparison(brand_name, competitor_list):
    """Simulate competitor comparison data"""
    comparison_data = {}

    for competitor in competitor_list:
        comparison_data[competitor] = {
            'mentions': random.randint(300, 1500),
            'sentiment': random.uniform(2.0, 4.5),
            'reach': random.randint(5000, 50000)
        }

    return comparison_data


def generate_brand_insights(brand_data, brand_name):
    """Generate brand insights"""
    insights = []

    sentiment_score = brand_data['sentiment_score']
    if sentiment_score > 4.0:
        insights.append(f"{brand_name} has excellent brand sentiment")
    elif sentiment_score > 3.0:
        insights.append(f"{brand_name} maintains positive brand sentiment")
    else:
        insights.append(f"{brand_name} should focus on improving brand sentiment")

    # Platform insights
    best_platform = max(brand_data['platform_breakdown'].items(), key=lambda x: x[1]['mentions'])[0]
    insights.append(f"{best_platform} generates the most brand mentions")

    total_mentions = brand_data['total_mentions']
    if total_mentions > 1000:
        insights.append("Strong brand awareness and mention volume")
    else:
        insights.append("Opportunity to increase brand visibility")

    insights.append("Monitor sentiment trends to identify potential issues early")
    insights.append("Engage with positive mentions to build community")

    return insights


def generate_brand_action_items(brand_data):
    """Generate brand action items"""
    actions = []

    sentiment_breakdown = brand_data['sentiment_breakdown']

    if sentiment_breakdown['negative'] > 20:
        actions.append("Address negative sentiment by improving customer service response")

    if sentiment_breakdown['positive'] > 50:
        actions.append("Amplify positive mentions through social sharing and testimonials")

    actions.append("Create engaging content to increase positive brand mentions")
    actions.append("Set up automated alerts for brand mentions requiring immediate response")
    actions.append("Develop influencer partnerships to improve brand perception")

    return actions


def generate_brand_report(brand_data, brand_name):
    """Generate comprehensive brand report"""
    report = f"BRAND TRACKING REPORT: {brand_name}\n"
    report += "=" * 50 + "\n\n"

    report += f"BRAND OVERVIEW\n"
    report += f"Total Mentions: {brand_data['total_mentions']:,}\n"
    report += f"Sentiment Score: {brand_data['sentiment_score']:.1f}/5.0\n"
    report += f"Total Reach: {brand_data['total_reach']:,}\n"
    report += f"Share of Voice: {brand_data['share_of_voice']:.1f}%\n\n"

    report += f"SENTIMENT BREAKDOWN\n"
    report += f"Positive: {brand_data['sentiment_breakdown']['positive']:.1f}%\n"
    report += f"Negative: {brand_data['sentiment_breakdown']['negative']:.1f}%\n"
    report += f"Neutral: {brand_data['sentiment_breakdown']['neutral']:.1f}%\n\n"

    report += "PLATFORM PERFORMANCE\n"
    for platform, data in brand_data['platform_breakdown'].items():
        report += f"\n{platform}:\n"
        report += f"  Mentions: {data['mentions']:,}\n"
        report += f"  Engagement: {data['engagement']:,}\n"
        report += f"  Reach: {data['reach']:,}\n"
        report += f"  Sentiment: {data['sentiment']:.1f}/5.0\n"

    return report


def competitor_monitoring():
    """Monitor and analyze competitor social media activity"""
    create_tool_header("Competitor Monitoring", "Track and analyze competitor social media performance", "🕵️")

    # Competitor setup
    st.subheader("Competitor Setup")

    col1, col2 = st.columns(2)
    with col1:
        competitor_name = st.text_input("Competitor Name", placeholder="Enter competitor brand name")
        industry = st.selectbox("Industry", [
            "Technology", "Fashion", "Food & Beverage", "Travel", "Fitness", "Business Services",
            "E-commerce", "Entertainment", "Education", "Healthcare", "Finance", "Other"
        ])

    with col2:
        platforms = st.multiselect("Platforms to Monitor", [
            "Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok", "YouTube", "Pinterest"
        ], default=["Instagram", "Twitter", "LinkedIn"])

        monitoring_period = st.selectbox("Monitoring Period", [
            "Last 7 days", "Last 30 days", "Last 3 months", "Last 6 months"
        ])

    if not competitor_name or not platforms:
        st.warning("Please enter a competitor name and select at least one platform to monitor.")
        return

    # Analysis type
    analysis_type = st.selectbox("Analysis Type", [
        "Content Performance", "Engagement Analysis", "Hashtag Strategy", "Posting Frequency", "Comprehensive Analysis"
    ])

    # Advanced options
    with st.expander("Advanced Monitoring Options"):
        monitor_keywords = st.text_input("Keywords to Track", placeholder="product, campaign, hashtag")
        content_types = st.multiselect("Content Types to Analyze", [
            "Text Posts", "Images", "Videos", "Stories", "Reels", "Carousels", "Live Videos"
        ], default=["Images", "Videos", "Text Posts"])

        include_metrics = st.multiselect("Metrics to Track", [
            "Likes", "Comments", "Shares", "Views", "Engagement Rate", "Reach", "Impressions"
        ], default=["Likes", "Comments", "Shares", "Engagement Rate"])

    if st.button("Start Competitor Analysis"):
        if competitor_name and platforms:
            with st.spinner(f"Analyzing {competitor_name}'s social media presence..."):
                # Generate competitor analysis data
                competitor_data = generate_competitor_analysis_data(
                    competitor_name, platforms, monitoring_period, analysis_type,
                    monitor_keywords, content_types, include_metrics
                )

                if competitor_data:
                    st.subheader(f"Competitor Analysis: {competitor_name}")

                    # Overview metrics
                    st.subheader("📊 Performance Overview")
                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.metric("Total Posts", f"{competitor_data['total_posts']:,}")
                    with col2:
                        st.metric("Avg Engagement Rate", f"{competitor_data['avg_engagement_rate']:.2%}")
                    with col3:
                        st.metric("Total Followers", f"{competitor_data['total_followers']:,}")
                    with col4:
                        st.metric("Content Score", f"{competitor_data['content_score']:.1f}/10")

                    # Platform breakdown
                    st.subheader("🎯 Platform Performance")
                    tabs = st.tabs(platforms)

                    for i, platform in enumerate(platforms):
                        with tabs[i]:
                            platform_data = competitor_data['platform_data'][platform]

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Posts", platform_data['posts'])
                                st.metric("Avg Likes", f"{platform_data['avg_likes']:,}")
                            with col2:
                                st.metric("Followers", f"{platform_data['followers']:,}")
                                st.metric("Avg Comments", f"{platform_data['avg_comments']:,}")
                            with col3:
                                st.metric("Engagement Rate", f"{platform_data['engagement_rate']:.2%}")
                                st.metric("Post Frequency", f"{platform_data['post_frequency']}/day")

                    # Content analysis
                    st.subheader("📝 Content Strategy Analysis")

                    content_tabs = st.tabs(["Top Content", "Content Types", "Hashtag Strategy", "Posting Times"])

                    with content_tabs[0]:  # Top Content
                        st.write("**Best Performing Posts:**")
                        top_posts = competitor_data.get('top_posts', [])
                        for i, post in enumerate(top_posts[:5], 1):
                            with st.expander(f"#{i} - {post['platform']} ({post['engagement_rate']:.2%} engagement)"):
                                st.write(f"**Content:** {post['content'][:200]}...")
                                col1, col2, col3 = st.columns(3)
                                with col1:
                                    st.metric("Likes", f"{post['likes']:,}")
                                with col2:
                                    st.metric("Comments", f"{post['comments']:,}")
                                with col3:
                                    st.metric("Shares", f"{post['shares']:,}")

                    with content_tabs[1]:  # Content Types
                        content_breakdown = competitor_data.get('content_breakdown', {})
                        for content_type, stats in content_breakdown.items():
                            col1, col2 = st.columns([1, 2])
                            with col1:
                                st.write(f"**{content_type}**")
                            with col2:
                                st.write(
                                    f"{stats['percentage']:.1f}% ({stats['count']} posts) - Avg Engagement: {stats['avg_engagement']:.2%}")

                    with content_tabs[2]:  # Hashtag Strategy
                        st.write("**Top Hashtags Used:**")
                        top_hashtags = competitor_data.get('top_hashtags', [])
                        hashtag_cols = st.columns(3)
                        for i, hashtag in enumerate(top_hashtags[:15]):
                            with hashtag_cols[i % 3]:
                                st.write(f"#{hashtag['tag']} ({hashtag['count']} uses)")

                    with content_tabs[3]:  # Posting Times
                        posting_analysis = competitor_data.get('posting_analysis', {})
                        st.write("**Optimal Posting Times:**")
                        for day, times in posting_analysis.items():
                            st.write(f"**{day}:** {', '.join(times)}")

                    # Competitive insights
                    st.subheader("💡 Competitive Insights")
                    insights = generate_competitor_insights(competitor_data, competitor_name)
                    for insight in insights:
                        st.write(f"• {insight}")

                    # Recommendations
                    st.subheader("🚀 Strategic Recommendations")
                    recommendations = generate_competitor_recommendations(competitor_data, competitor_name)
                    for recommendation in recommendations:
                        st.write(f"• {recommendation}")

                    # Export options
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("📊 Export Analysis Report"):
                            report = generate_competitor_report(competitor_data, competitor_name, platforms)
                            FileHandler.create_download_link(
                                report.encode(),
                                f"competitor_analysis_{competitor_name.lower().replace(' ', '_')}.txt",
                                "text/plain"
                            )

                    with col2:
                        if st.button("📋 Export Competitor Data"):
                            data_json = json.dumps(competitor_data, indent=2)
                            FileHandler.create_download_link(
                                data_json.encode(),
                                f"competitor_data_{competitor_name.lower().replace(' ', '_')}.json",
                                "application/json"
                            )


def generate_competitor_analysis_data(competitor_name, platforms, monitoring_period, analysis_type, keywords,
                                      content_types, metrics):
    """Generate comprehensive competitor analysis data"""

    # Base metrics
    total_posts = random.randint(50, 500)
    total_followers = random.randint(10000, 1000000)
    avg_engagement_rate = random.uniform(0.01, 0.15)
    content_score = random.uniform(6.0, 9.5)

    # Platform data
    platform_data = {}
    for platform in platforms:
        platform_data[platform] = {
            'posts': random.randint(10, 100),
            'followers': random.randint(5000, 200000),
            'avg_likes': random.randint(100, 10000),
            'avg_comments': random.randint(10, 1000),
            'avg_shares': random.randint(5, 500),
            'engagement_rate': random.uniform(0.005, 0.20),
            'post_frequency': round(random.uniform(0.5, 3.0), 1)
        }

    # Top performing posts
    post_types = ["Product showcase", "Behind-the-scenes", "User testimonial", "Educational content",
                  "Promotional offer"]
    top_posts = []
    for i in range(10):
        likes = random.randint(500, 50000)
        comments = random.randint(20, 2000)
        shares = random.randint(10, 1000)
        total_engagement = likes + comments + shares

        top_posts.append({
            'platform': random.choice(platforms),
            'content': f"{random.choice(post_types)} content from {competitor_name}",
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'engagement_rate': total_engagement / random.randint(10000, 100000),
            'post_type': random.choice(post_types)
        })

    # Sort by engagement rate
    top_posts.sort(key=lambda x: x['engagement_rate'], reverse=True)

    # Content breakdown
    content_breakdown = {}
    for content_type in content_types:
        count = random.randint(5, 50)
        content_breakdown[content_type] = {
            'count': count,
            'percentage': (count / total_posts) * 100,
            'avg_engagement': random.uniform(0.01, 0.25)
        }

    # Hashtag analysis
    hashtag_samples = ["marketing", "business", "innovation", "technology", "growth", "success", "team", "quality",
                       "customer", "service", "digital", "future", "leadership", "strategy", "brand"]
    top_hashtags = []
    for hashtag in random.sample(hashtag_samples, 10):
        top_hashtags.append({
            'tag': hashtag,
            'count': random.randint(5, 50),
            'avg_engagement': random.uniform(0.01, 0.20)
        })

    # Posting times analysis
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    posting_analysis = {}
    for day in days:
        times = random.sample(["9:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM"], 2)
        posting_analysis[day] = times

    return {
        'competitor_name': competitor_name,
        'total_posts': total_posts,
        'total_followers': total_followers,
        'avg_engagement_rate': avg_engagement_rate,
        'content_score': content_score,
        'platform_data': platform_data,
        'top_posts': top_posts,
        'content_breakdown': content_breakdown,
        'top_hashtags': top_hashtags,
        'posting_analysis': posting_analysis,
        'analysis_period': monitoring_period,
        'monitored_platforms': platforms
    }


def generate_competitor_insights(competitor_data, competitor_name):
    """Generate strategic insights from competitor analysis"""
    insights = []

    avg_engagement = competitor_data['avg_engagement_rate']
    if avg_engagement > 0.10:
        insights.append(
            f"{competitor_name} has exceptionally high engagement rates, indicating strong audience connection")
    elif avg_engagement > 0.05:
        insights.append(f"{competitor_name} maintains good engagement levels with their audience")
    else:
        insights.append(f"{competitor_name} shows room for improvement in audience engagement")

    # Platform insights
    best_platform = max(competitor_data['platform_data'].items(), key=lambda x: x[1]['engagement_rate'])
    insights.append(
        f"{competitor_name} performs best on {best_platform[0]} with {best_platform[1]['engagement_rate']:.2%} engagement")

    # Content insights
    if 'content_breakdown' in competitor_data:
        top_content = max(competitor_data['content_breakdown'].items(), key=lambda x: x[1]['avg_engagement'])
        insights.append(f"{top_content[0]} content generates the highest engagement for {competitor_name}")

    # Posting frequency
    total_posts = competitor_data['total_posts']
    if total_posts > 200:
        insights.append(f"{competitor_name} maintains high posting frequency, keeping audience engaged")
    elif total_posts < 50:
        insights.append(f"{competitor_name} has low posting frequency, potential opportunity for increased visibility")

    insights.append(
        f"{competitor_name} has built a substantial following of {competitor_data['total_followers']:,} across platforms")

    return insights


def generate_competitor_recommendations(competitor_data, competitor_name):
    """Generate strategic recommendations based on competitor analysis"""
    recommendations = []

    best_platform = max(competitor_data['platform_data'].items(), key=lambda x: x[1]['engagement_rate'])
    recommendations.append(
        f"Consider increasing presence on {best_platform[0]} - {competitor_name}'s most successful platform")

    if 'top_hashtags' in competitor_data:
        top_hashtags = competitor_data['top_hashtags'][:5]
        hashtag_list = ', '.join([f"#{tag['tag']}" for tag in top_hashtags])
        recommendations.append(f"Explore using similar hashtags: {hashtag_list}")

    # Posting time recommendations
    if 'posting_analysis' in competitor_data:
        recommendations.append(f"Consider posting during {competitor_name}'s optimal times for better visibility")

    if 'content_breakdown' in competitor_data:
        top_content = max(competitor_data['content_breakdown'].items(), key=lambda x: x[1]['avg_engagement'])
        recommendations.append(f"Increase {top_content[0]} content - it shows highest engagement for {competitor_name}")

    recommendations.append(f"Monitor {competitor_name}'s campaign launches and promotional strategies")
    recommendations.append("Set up automated alerts for competitor mentions and brand comparisons")
    recommendations.append("Analyze competitor's audience demographics for targeting insights")

    return recommendations


def generate_competitor_report(competitor_data, competitor_name, platforms):
    """Generate comprehensive competitor monitoring report"""
    report = f"COMPETITOR MONITORING REPORT: {competitor_name}\n"
    report += "=" * 60 + "\n\n"

    report += f"EXECUTIVE SUMMARY\n"
    report += f"Competitor: {competitor_name}\n"
    report += f"Analysis Period: {competitor_data['analysis_period']}\n"
    report += f"Platforms Monitored: {', '.join(platforms)}\n"
    report += f"Total Posts Analyzed: {competitor_data['total_posts']:,}\n"
    report += f"Total Followers: {competitor_data['total_followers']:,}\n"
    report += f"Average Engagement Rate: {competitor_data['avg_engagement_rate']:.2%}\n"
    report += f"Content Quality Score: {competitor_data['content_score']:.1f}/10\n\n"

    report += "PLATFORM PERFORMANCE BREAKDOWN\n"
    report += "-" * 40 + "\n"
    for platform, data in competitor_data['platform_data'].items():
        report += f"\n{platform.upper()}:\n"
        report += f"  Posts: {data['posts']:,}\n"
        report += f"  Followers: {data['followers']:,}\n"
        report += f"  Average Likes: {data['avg_likes']:,}\n"
        report += f"  Average Comments: {data['avg_comments']:,}\n"
        report += f"  Engagement Rate: {data['engagement_rate']:.2%}\n"
        report += f"  Posting Frequency: {data['post_frequency']} posts/day\n"

    report += f"\nTOP PERFORMING CONTENT\n"
    report += "-" * 25 + "\n"
    for i, post in enumerate(competitor_data['top_posts'][:5], 1):
        report += f"\n#{i}. {post['platform']} Post\n"
        report += f"   Engagement Rate: {post['engagement_rate']:.2%}\n"
        report += f"   Likes: {post['likes']:,} | Comments: {post['comments']:,} | Shares: {post['shares']:,}\n"
        report += f"   Content: {post['content']}\n"

    report += f"\nHASHTAG STRATEGY\n"
    report += "-" * 16 + "\n"
    for hashtag in competitor_data['top_hashtags'][:10]:
        report += f"#{hashtag['tag']} - Used {hashtag['count']} times\n"

    report += f"\nSTRATEGIC INSIGHTS\n"
    report += "-" * 18 + "\n"
    insights = generate_competitor_insights(competitor_data, competitor_name)
    for insight in insights:
        report += f"• {insight}\n"

    report += f"\nRECOMMENDATIONS\n"
    report += "-" * 15 + "\n"
    recommendations = generate_competitor_recommendations(competitor_data, competitor_name)
    for recommendation in recommendations:
        report += f"• {recommendation}\n"

    report += f"\nReport generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    return report


def post_optimizer():
    """Optimize social media posts for better performance"""
    create_tool_header("Post Optimizer", "Optimize your posts for maximum engagement", "🚀")

    st.subheader("Post Content")
    original_post = st.text_area("Enter your post content", height=150,
                                 placeholder="Paste your post content here...")

    if not original_post:
        st.warning("Please enter some post content to optimize.")
        return

    col1, col2 = st.columns(2)
    with col1:
        platform = st.selectbox("Target Platform", [
            "Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok"
        ])
        optimization_goals = st.multiselect("Optimization Goals", [
            "Increase Engagement", "Improve Readability", "Add Trending Hashtags",
            "Better Call-to-Action", "Optimize Length", "Add Emojis"
        ])

    with col2:
        audience_type = st.selectbox("Target Audience", [
            "General", "Young Adults", "Professionals", "Families", "Entrepreneurs"
        ])
        tone = st.selectbox("Desired Tone", [
            "Keep Original", "More Professional", "More Casual", "More Engaging", "More Urgent"
        ])

    if st.button("Optimize Post"):
        with st.spinner("Optimizing your post..."):
            # Generate optimized versions
            optimized_posts = generate_optimized_posts(original_post, platform, optimization_goals, audience_type, tone)

            if optimized_posts:
                st.subheader("Optimized Versions")

                for i, optimized in enumerate(optimized_posts, 1):
                    with st.expander(f"Version {i} - {optimized['improvement_focus']}"):
                        st.text_area(f"Optimized Content {i}", optimized['content'], height=120, disabled=True)

                        # Show improvements made
                        st.write("**Improvements Made:**")
                        for improvement in optimized['improvements']:
                            st.write(f"• {improvement}")

                        # Show metrics comparison
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Character Count", optimized['char_count'],
                                      optimized['char_count'] - len(original_post))
                        with col2:
                            st.metric("Hashtags", optimized['hashtag_count'])
                        with col3:
                            st.metric("Engagement Score", f"{optimized['engagement_score']}/10")


def reach_analysis():
    """Analyze post reach and impressions"""
    create_tool_header("Reach Analysis", "Analyze your content reach and audience", "📈")

    st.subheader("Data Input")

    data_source = st.selectbox("Data Source", [
        "Upload CSV", "Manual Entry", "Sample Data"
    ])

    reach_data = None

    if data_source == "Sample Data":
        reach_data = generate_sample_reach_data()
        st.success("Using sample reach data for demonstration")
    elif data_source == "Manual Entry":
        st.subheader("Enter Reach Data")

        posts_data = []
        num_posts = st.number_input("Number of Posts", 1, 20, 5)

        for i in range(num_posts):
            with st.expander(f"Post {i + 1}"):
                col1, col2 = st.columns(2)
                with col1:
                    post_title = st.text_input(f"Post Title", key=f"title_{i}")
                    platform = st.selectbox("Platform", ["Instagram", "Twitter", "Facebook", "LinkedIn"],
                                            key=f"platform_{i}")
                    reach = st.number_input("Reach", 0, 10000000, key=f"reach_{i}")

                with col2:
                    impressions = st.number_input("Impressions", 0, 10000000, key=f"impressions_{i}")
                    engagement = st.number_input("Total Engagement", 0, 100000, key=f"engagement_{i}")
                    followers = st.number_input("Followers at Time", 1000, 10000000, key=f"followers_{i}")

                posts_data.append({
                    'title': post_title,
                    'platform': platform,
                    'reach': reach,
                    'impressions': impressions,
                    'engagement': engagement,
                    'followers': followers,
                    'reach_rate': (reach / followers) * 100 if followers > 0 else 0
                })

        reach_data = posts_data

    if reach_data:
        st.subheader("📊 Reach Analytics")

        # Overview metrics
        total_reach = sum(post['reach'] for post in reach_data)
        total_impressions = sum(post['impressions'] for post in reach_data)
        avg_reach_rate = sum(post['reach_rate'] for post in reach_data) / len(reach_data)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Reach", f"{total_reach:,}")
        with col2:
            st.metric("Total Impressions", f"{total_impressions:,}")
        with col3:
            st.metric("Avg Reach Rate", f"{avg_reach_rate:.1f}%")
        with col4:
            st.metric("Avg Frequency", f"{total_impressions / total_reach:.1f}" if total_reach > 0 else "0")

        # Platform breakdown
        st.subheader("Platform Performance")
        platform_stats = {}
        for post in reach_data:
            platform = post['platform']
            if platform not in platform_stats:
                platform_stats[platform] = {'reach': 0, 'impressions': 0, 'posts': 0}
            platform_stats[platform]['reach'] += post['reach']
            platform_stats[platform]['impressions'] += post['impressions']
            platform_stats[platform]['posts'] += 1

        for platform, stats in platform_stats.items():
            with st.expander(f"{platform} Performance"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Posts", stats['posts'])
                with col2:
                    st.metric("Total Reach", f"{stats['reach']:,}")
                with col3:
                    st.metric("Avg Reach/Post", f"{stats['reach'] // stats['posts']:,}")


def comment_manager():
    """Manage and analyze social media comments"""
    create_tool_header("Comment Manager", "Manage comments and interactions", "💬")

    st.subheader("Comment Management")

    management_type = st.selectbox("Management Type", [
        "View Comments", "Respond to Comments", "Comment Analytics", "Moderation"
    ])

    if management_type == "Comment Analytics":
        st.subheader("📊 Comment Analytics")

        # Sample comment data
        comments_data = generate_sample_comments_data()

        # Overview metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Comments", len(comments_data))
        with col2:
            positive = sum(1 for c in comments_data if c['sentiment'] == 'positive')
            st.metric("Positive Comments", positive)
        with col3:
            negative = sum(1 for c in comments_data if c['sentiment'] == 'negative')
            st.metric("Negative Comments", negative)
        with col4:
            avg_response_time = sum(c['response_time'] for c in comments_data) / len(comments_data)
            st.metric("Avg Response Time", f"{avg_response_time:.1f}h")

        # Recent comments
        st.subheader("Recent Comments")
        for comment in comments_data[:5]:
            with st.expander(f"{comment['platform']} - {comment['sentiment'].title()}"):
                st.write(f"**Comment:** {comment['text']}")
                st.write(f"**Author:** {comment['author']}")
                st.write(f"**Sentiment:** {comment['sentiment']}")
                if comment['needs_response']:
                    st.warning("⚠️ Requires response")

    elif management_type == "Respond to Comments":
        st.subheader("✍️ Comment Response Assistant")

        comment_text = st.text_area("Original Comment", placeholder="Paste the comment you want to respond to...")
        comment_sentiment = st.selectbox("Comment Sentiment", ["Positive", "Negative", "Neutral", "Question"])

        if comment_text:
            response_style = st.selectbox("Response Style", [
                "Professional", "Friendly", "Apologetic", "Informative", "Grateful"
            ])

            if st.button("Generate Response"):
                with st.spinner("Generating response..."):
                    response = generate_comment_response(comment_text, comment_sentiment, response_style)
                    st.text_area("Suggested Response", response, height=100)


def visual_content():
    """Create and optimize visual content for social media"""
    create_tool_header("Visual Content", "Create engaging visual content", "🎨")

    st.subheader("Visual Content Creation")

    content_type = st.selectbox("Content Type", [
        "Quote Graphics", "Infographics", "Story Templates", "Post Templates", "Brand Assets"
    ])

    if content_type == "Quote Graphics":
        quote_text = st.text_area("Quote Text", placeholder="Enter your quote here...")
        author = st.text_input("Author (optional)")

        col1, col2 = st.columns(2)
        with col1:
            theme = st.selectbox("Theme", [
                "Motivational", "Business", "Minimalist", "Bold", "Elegant"
            ])
            color_scheme = st.selectbox("Color Scheme", [
                "Blue & White", "Black & Gold", "Gradient", "Brand Colors", "Custom"
            ])

        with col2:
            format_size = st.selectbox("Format", [
                "Instagram Square (1080x1080)",
                "Instagram Story (1080x1920)",
                "Twitter (1200x675)",
                "LinkedIn (1200x628)",
                "Facebook (1200x630)"
            ])

        if quote_text and st.button("Generate Quote Graphic"):
            st.info("Quote graphic would be generated here with the specified parameters")
            st.write(f"**Quote:** {quote_text}")
            st.write(f"**Theme:** {theme}")
            st.write(f"**Size:** {format_size}")

    elif content_type == "Story Templates":
        st.subheader("📱 Story Template Creator")

        story_type = st.selectbox("Story Type", [
            "Behind the Scenes", "Product Showcase", "Tips & Tricks", "Quote", "Poll/Question"
        ])

        brand_colors = st.text_input("Brand Colors (hex codes)", placeholder="#FF5733, #33A1FF")

        if st.button("Create Story Template"):
            st.info(f"Creating {story_type} story template with your brand colors")


def sentiment_analysis():
    """Analyze sentiment of social media content and comments"""
    create_tool_header("Sentiment Analysis", "Analyze sentiment across your content", "😊")

    st.subheader("Sentiment Analysis")

    analysis_type = st.selectbox("Analysis Type", [
        "Single Post Analysis", "Bulk Content Analysis", "Comment Sentiment", "Brand Mention Analysis"
    ])

    if analysis_type == "Single Post Analysis":
        content = st.text_area("Post Content", placeholder="Paste your post content here...")

        if content and st.button("Analyze Sentiment"):
            with st.spinner("Analyzing sentiment..."):
                # Simulate sentiment analysis
                sentiment_score = random.uniform(-1, 1)

                if sentiment_score > 0.3:
                    sentiment = "Positive 😊"
                    color = "green"
                elif sentiment_score < -0.3:
                    sentiment = "Negative 😞"
                    color = "red"
                else:
                    sentiment = "Neutral 😐"
                    color = "gray"

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Sentiment", sentiment)
                with col2:
                    st.metric("Confidence", f"{abs(sentiment_score) * 100:.1f}%")
                with col3:
                    st.metric("Score", f"{sentiment_score:.2f}")

                # Detailed analysis
                st.subheader("Detailed Analysis")
                emotions = generate_emotion_analysis(content)

                for emotion, percentage in emotions.items():
                    st.write(f"**{emotion}:** {percentage:.1f}%")

    elif analysis_type == "Comment Sentiment":
        st.subheader("📝 Comment Sentiment Analysis")

        # Sample data
        comment_sentiments = generate_sample_comment_sentiments()

        col1, col2, col3 = st.columns(3)
        with col1:
            positive_pct = sum(1 for c in comment_sentiments if c['sentiment'] > 0.3) / len(comment_sentiments) * 100
            st.metric("Positive Comments", f"{positive_pct:.1f}%")
        with col2:
            negative_pct = sum(1 for c in comment_sentiments if c['sentiment'] < -0.3) / len(comment_sentiments) * 100
            st.metric("Negative Comments", f"{negative_pct:.1f}%")
        with col3:
            neutral_pct = 100 - positive_pct - negative_pct
            st.metric("Neutral Comments", f"{neutral_pct:.1f}%")

        # Show recent comments with sentiment
        st.subheader("Recent Comments")
        for comment in comment_sentiments[:10]:
            sentiment_emoji = "😊" if comment['sentiment'] > 0.3 else "😞" if comment['sentiment'] < -0.3 else "😐"
            st.write(f"{sentiment_emoji} {comment['text'][:100]}...")


def growth_metrics():
    """Track and analyze growth metrics"""
    create_tool_header("Growth Metrics", "Track your social media growth", "📈")

    st.subheader("Growth Analysis")

    time_period = st.selectbox("Time Period", [
        "Last 7 days", "Last 30 days", "Last 3 months", "Last 6 months", "Last year"
    ])

    # Generate sample growth data
    growth_data = generate_sample_growth_data(time_period)

    # Overview metrics
    st.subheader("📊 Growth Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("New Followers", f"{growth_data['new_followers']:,}",
                  f"+{growth_data['follower_growth_rate']:.1f}%")
    with col2:
        st.metric("Total Reach", f"{growth_data['total_reach']:,}",
                  f"+{growth_data['reach_growth']:.1f}%")
    with col3:
        st.metric("Engagement Rate", f"{growth_data['avg_engagement']:.2%}",
                  f"+{growth_data['engagement_growth']:.1f}%")
    with col4:
        st.metric("Posts Published", growth_data['posts_count'])

    # Platform growth
    st.subheader("Platform Growth")
    for platform, data in growth_data['platform_growth'].items():
        with st.expander(f"{platform} Growth"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Followers", f"{data['followers']:,}", f"+{data['growth']}")
            with col2:
                st.metric("Engagement", f"{data['engagement']:.2%}")
            with col3:
                st.metric("Posts", data['posts'])

    # Growth insights
    st.subheader("💡 Growth Insights")
    insights = generate_growth_insights(growth_data)
    for insight in insights:
        st.write(f"• {insight}")


def follower_analysis():
    """Analyze follower demographics and behavior"""
    create_tool_header("Follower Analysis", "Understand your audience better", "👥")

    st.subheader("Follower Analytics")

    # Generate sample follower data
    follower_data = generate_sample_follower_data()

    # Overview
    st.subheader("👥 Audience Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Followers", f"{follower_data['total_followers']:,}")
    with col2:
        st.metric("Active Followers", f"{follower_data['active_followers']:,}")
    with col3:
        st.metric("Engagement Rate", f"{follower_data['engagement_rate']:.2%}")
    with col4:
        st.metric("Growth Rate", f"+{follower_data['growth_rate']:.1f}%")

    # Demographics
    st.subheader("📊 Demographics")

    tabs = st.tabs(["Age Groups", "Gender", "Location", "Interests"])

    with tabs[0]:  # Age Groups
        st.write("**Age Distribution:**")
        for age_group, percentage in follower_data['age_groups'].items():
            st.write(f"**{age_group}:** {percentage:.1f}%")

    with tabs[1]:  # Gender
        st.write("**Gender Distribution:**")
        for gender, percentage in follower_data['gender'].items():
            st.write(f"**{gender}:** {percentage:.1f}%")

    with tabs[2]:  # Location
        st.write("**Top Locations:**")
        for location, percentage in follower_data['locations'].items():
            st.write(f"**{location}:** {percentage:.1f}%")

    with tabs[3]:  # Interests
        st.write("**Top Interests:**")
        for interest, percentage in follower_data['interests'].items():
            st.write(f"**{interest}:** {percentage:.1f}%")

    # Activity patterns
    st.subheader("⏰ Activity Patterns")
    st.write("**Most Active Times:**")
    for time, activity in follower_data['active_times'].items():
        st.write(f"**{time}:** {activity:.1f}% of daily activity")


# Helper functions for the new tools

def generate_optimized_posts(original, platform, goals, audience, tone):
    """Generate optimized versions of a post"""
    versions = []

    # Version 1: Engagement focused
    versions.append({
        'content': f"🚀 {original}\n\n#trending #viral #engagement",
        'improvement_focus': 'Engagement Boost',
        'improvements': ['Added engaging emoji', 'Included trending hashtags', 'Improved call-to-action'],
        'char_count': len(original) + 25,
        'hashtag_count': 3,
        'engagement_score': 8.5
    })

    # Version 2: Professional tone
    versions.append({
        'content': f"Professional insight: {original}\n\nShare your thoughts in the comments below.",
        'improvement_focus': 'Professional Tone',
        'improvements': ['Enhanced professional language', 'Added discussion prompt', 'Improved structure'],
        'char_count': len(original) + 35,
        'hashtag_count': 0,
        'engagement_score': 7.8
    })

    return versions


def generate_sample_reach_data():
    """Generate sample reach data"""
    return [
        {'title': 'Product Launch Post', 'platform': 'Instagram', 'reach': 15000, 'impressions': 18500,
         'engagement': 1200, 'followers': 25000, 'reach_rate': 60.0},
        {'title': 'Behind the Scenes', 'platform': 'Twitter', 'reach': 8500, 'impressions': 12000, 'engagement': 850,
         'followers': 20000, 'reach_rate': 42.5},
        {'title': 'Educational Content', 'platform': 'LinkedIn', 'reach': 12000, 'impressions': 15000,
         'engagement': 950, 'followers': 18000, 'reach_rate': 66.7}
    ]


def generate_sample_comments_data():
    """Generate sample comment data"""
    return [
        {'platform': 'Instagram', 'text': 'Love this product!', 'author': 'user123', 'sentiment': 'positive',
         'response_time': 2.5, 'needs_response': False},
        {'platform': 'Twitter', 'text': 'Having issues with delivery', 'author': 'customer456', 'sentiment': 'negative',
         'response_time': 0, 'needs_response': True},
        {'platform': 'Facebook', 'text': 'Great post, very informative', 'author': 'fan789', 'sentiment': 'positive',
         'response_time': 1.2, 'needs_response': False}
    ]


def generate_comment_response(comment, sentiment, style):
    """Generate a response to a comment"""
    responses = {
        'positive': f"Thank you so much for your kind words! We're thrilled you're happy with our content. 😊",
        'negative': f"We sincerely apologize for any inconvenience. Please send us a DM so we can resolve this immediately.",
        'neutral': f"Thank you for taking the time to engage with our content. We appreciate your feedback!"
    }
    return responses.get(sentiment.lower(), "Thank you for your comment! We appreciate your engagement.")


def generate_emotion_analysis(content):
    """Generate emotion analysis"""
    return {
        'Joy': random.uniform(20, 80),
        'Trust': random.uniform(15, 60),
        'Anticipation': random.uniform(10, 40),
        'Surprise': random.uniform(5, 30),
        'Fear': random.uniform(0, 20),
        'Sadness': random.uniform(0, 15)
    }


def generate_sample_comment_sentiments():
    """Generate sample comment sentiment data"""
    comments = [
        {'text': 'Amazing product, highly recommend!', 'sentiment': 0.8},
        {'text': 'Not satisfied with the service', 'sentiment': -0.6},
        {'text': 'Pretty good overall', 'sentiment': 0.2},
        {'text': 'Excellent customer support', 'sentiment': 0.9},
        {'text': 'Could be better', 'sentiment': -0.2}
    ]
    return comments * 2  # Duplicate for more sample data


def generate_sample_growth_data(period):
    """Generate sample growth metrics"""
    return {
        'new_followers': random.randint(500, 5000),
        'follower_growth_rate': random.uniform(5, 25),
        'total_reach': random.randint(50000, 500000),
        'reach_growth': random.uniform(10, 40),
        'avg_engagement': random.uniform(0.02, 0.08),
        'engagement_growth': random.uniform(5, 20),
        'posts_count': random.randint(10, 50),
        'platform_growth': {
            'Instagram': {'followers': random.randint(10000, 50000), 'growth': random.randint(200, 1000),
                          'engagement': random.uniform(0.03, 0.07), 'posts': random.randint(5, 20)},
            'Twitter': {'followers': random.randint(5000, 30000), 'growth': random.randint(100, 800),
                        'engagement': random.uniform(0.02, 0.05), 'posts': random.randint(10, 30)},
            'LinkedIn': {'followers': random.randint(3000, 20000), 'growth': random.randint(50, 500),
                         'engagement': random.uniform(0.04, 0.08), 'posts': random.randint(3, 15)}
        }
    }


def generate_growth_insights(data):
    """Generate growth insights"""
    insights = []

    if data['follower_growth_rate'] > 15:
        insights.append("Excellent follower growth rate - your content strategy is working well")
    elif data['follower_growth_rate'] > 8:
        insights.append("Good steady growth - consider boosting high-performing content")
    else:
        insights.append("Growth rate could be improved - try posting more consistently or engaging content")

    best_platform = max(data['platform_growth'].items(), key=lambda x: x[1]['engagement'])
    insights.append(f"{best_platform[0]} shows the highest engagement - focus more content there")

    insights.append("Continue monitoring growth trends to identify successful content patterns")

    return insights


def generate_sample_follower_data():
    """Generate sample follower demographic data"""
    return {
        'total_followers': random.randint(10000, 100000),
        'active_followers': random.randint(7000, 80000),
        'engagement_rate': random.uniform(0.03, 0.08),
        'growth_rate': random.uniform(5, 20),
        'age_groups': {
            '18-24': random.uniform(15, 25),
            '25-34': random.uniform(25, 40),
            '35-44': random.uniform(20, 30),
            '45-54': random.uniform(10, 20),
            '55+': random.uniform(5, 15)
        },
        'gender': {
            'Female': random.uniform(45, 65),
            'Male': random.uniform(35, 55),
            'Other': random.uniform(1, 5)
        },
        'locations': {
            'United States': random.uniform(30, 50),
            'Canada': random.uniform(8, 15),
            'United Kingdom': random.uniform(10, 18),
            'Australia': random.uniform(5, 12),
            'Other': random.uniform(15, 30)
        },
        'interests': {
            'Technology': random.uniform(20, 35),
            'Business': random.uniform(15, 30),
            'Lifestyle': random.uniform(25, 40),
            'Entertainment': random.uniform(20, 35),
            'Sports': random.uniform(10, 25)
        },
        'active_times': {
            'Morning (6-12 PM)': random.uniform(20, 35),
            'Afternoon (12-6 PM)': random.uniform(25, 40),
            'Evening (6-12 AM)': random.uniform(30, 45),
            'Late Night (12-6 AM)': random.uniform(5, 15)
        }
    }


def timing_analyzer():
    """Analyze optimal posting times for maximum engagement"""
    create_tool_header("Timing Analyzer", "Find the best times to post for maximum engagement", "⏰")

    st.subheader("Platform Selection")
    platform = st.selectbox("Select Platform", [
        "Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok", "YouTube"
    ])

    audience_location = st.selectbox("Primary Audience Location", [
        "United States", "Europe", "Asia", "Global", "Custom Timezone"
    ])

    if st.button("Analyze Optimal Times"):
        with st.spinner("Analyzing optimal posting times..."):
            optimal_times = generate_optimal_times_data(platform, audience_location)

            st.subheader(f"📊 Optimal Posting Times for {platform}")

            # Daily breakdown
            st.subheader("Best Times by Day")
            for day, times in optimal_times['daily_times'].items():
                with st.expander(f"{day}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Best Time", times['best_time'])
                    with col2:
                        st.metric("Engagement Score", f"{times['score']}/10")
                    with col3:
                        st.metric("Reach Potential", f"{times['reach_potential']:.1f}%")

            # Overall recommendations
            st.subheader("💡 Recommendations")
            for rec in optimal_times['recommendations']:
                st.write(f"• {rec}")


def bulk_scheduler():
    """Schedule multiple posts in bulk across platforms"""
    create_tool_header("Bulk Scheduler", "Schedule multiple posts efficiently", "📋")

    st.subheader("Bulk Post Upload")

    upload_method = st.selectbox("Upload Method", [
        "CSV File Upload", "Manual Entry", "Template Download"
    ])

    if upload_method == "Template Download":
        st.write("Download the template to prepare your posts:")
        template_data = generate_bulk_template()
        if st.button("Download Template"):
            FileHandler.create_download_link(
                template_data.encode(),
                "bulk_scheduler_template.csv",
                "text/csv"
            )

    elif upload_method == "Manual Entry":
        st.subheader("Enter Posts")
        num_posts = st.number_input("Number of Posts", 1, 50, 5)

        posts_data = []
        for i in range(num_posts):
            with st.expander(f"Post {i + 1}"):
                col1, col2 = st.columns(2)
                with col1:
                    content = st.text_area(f"Content", key=f"content_{i}")
                    platform = st.multiselect("Platforms",
                                              ["Instagram", "Twitter", "Facebook", "LinkedIn"], key=f"platforms_{i}")

                with col2:
                    schedule_date = st.date_input("Date", key=f"date_{i}")
                    schedule_time = st.time_input("Time", key=f"time_{i}")

                posts_data.append({
                    'content': content,
                    'platforms': platform,
                    'date': schedule_date,
                    'time': schedule_time
                })

        if st.button("Schedule All Posts"):
            scheduled_count = sum(1 for post in posts_data if post['content'] and post['platforms'])
            st.success(f"Successfully scheduled {scheduled_count} posts across multiple platforms!")


def competitor_analysis():
    """Comprehensive competitor analysis tool"""
    create_tool_header("Competitor Analysis", "Deep dive analysis of competitor performance", "🎯")

    # This is similar to competitor_monitoring but more comprehensive
    st.subheader("Competitor Research")

    competitor_name = st.text_input("Competitor Name")
    analysis_depth = st.selectbox("Analysis Depth", [
        "Quick Overview", "Detailed Analysis", "Comprehensive Report"
    ])

    if competitor_name and st.button("Start Analysis"):
        with st.spinner("Performing comprehensive competitor analysis..."):
            analysis_data = generate_comprehensive_competitor_analysis(competitor_name, analysis_depth)

            # Display results based on depth
            st.subheader(f"Analysis Results: {competitor_name}")

            # Key metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Overall Score", f"{analysis_data['overall_score']}/100")
            with col2:
                st.metric("Content Quality", f"{analysis_data['content_quality']}/10")
            with col3:
                st.metric("Engagement Rate", f"{analysis_data['engagement_rate']:.2%}")
            with col4:
                st.metric("Market Share", f"{analysis_data['market_share']:.1f}%")


def niche_discovery():
    """Discover niche hashtags and content opportunities"""
    create_tool_header("Niche Discovery", "Find untapped hashtags and content niches", "🔍")

    st.subheader("Niche Research")

    main_topic = st.text_input("Main Topic/Industry", placeholder="e.g., sustainable fashion")
    platform = st.selectbox("Target Platform", ["Instagram", "Twitter", "TikTok", "LinkedIn"])

    if main_topic and st.button("Discover Niches"):
        with st.spinner("Discovering niche opportunities..."):
            niche_data = generate_niche_data(main_topic, platform)

            st.subheader("🎯 Niche Opportunities")

            tabs = st.tabs(["Micro Niches", "Hashtag Opportunities", "Content Gaps", "Rising Trends"])

            with tabs[0]:
                st.write("**Micro Niches to Explore:**")
                for niche in niche_data['micro_niches']:
                    with st.expander(f"{niche['name']} (Competition: {niche['competition']})"):
                        st.write(f"**Description:** {niche['description']}")
                        st.write(f"**Potential:** {niche['potential']}/10")
                        st.write(f"**Suggested hashtags:** {', '.join(niche['hashtags'])}")


def hashtag_analytics():
    """Advanced hashtag performance analytics"""
    create_tool_header("Hashtag Analytics", "Deep analytics for hashtag performance", "#️⃣")

    st.subheader("Hashtag Performance Analysis")

    hashtags_input = st.text_area("Enter Hashtags (one per line)", placeholder="#marketing\n#socialmedia\n#branding")
    time_period = st.selectbox("Analysis Period", ["Last 30 days", "Last 90 days", "Last 6 months"])

    if hashtags_input and st.button("Analyze Hashtags"):
        hashtags = [tag.strip() for tag in hashtags_input.split('\n') if tag.strip()]

        with st.spinner("Analyzing hashtag performance..."):
            analytics_data = generate_hashtag_analytics_data(hashtags, time_period)

            st.subheader("📊 Hashtag Performance")

            for hashtag, data in analytics_data.items():
                with st.expander(f"{hashtag} Analytics"):
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Total Posts", f"{data['total_posts']:,}")
                    with col2:
                        st.metric("Avg Engagement", f"{data['avg_engagement']:,}")
                    with col3:
                        st.metric("Difficulty Score", f"{data['difficulty']}/10")
                    with col4:
                        st.metric("Trend", data['trend'])


def tag_optimizer():
    """Optimize hashtag combinations for maximum reach"""
    create_tool_header("Tag Optimizer", "Optimize your hashtag strategy", "🏷️")

    st.subheader("Hashtag Optimization")

    content_topic = st.text_input("Content Topic", placeholder="What's your post about?")
    platform = st.selectbox("Platform", ["Instagram", "Twitter", "TikTok", "LinkedIn"])
    goal = st.selectbox("Primary Goal", [
        "Maximum Reach", "High Engagement", "Niche Targeting", "Viral Potential"
    ])

    if content_topic and st.button("Optimize Hashtags"):
        with st.spinner("Optimizing hashtag combination..."):
            optimized_tags = generate_optimized_hashtags(content_topic, platform, goal)

            st.subheader("🎯 Optimized Hashtag Strategy")

            tabs = st.tabs(["Primary Tags", "Supporting Tags", "Niche Tags", "Strategy"])

            with tabs[0]:
                st.write("**Primary High-Impact Tags:**")
                for tag in optimized_tags['primary']:
                    st.write(f"#{tag['tag']} - Reach: {tag['reach']}, Competition: {tag['competition']}")


def interaction_tracker():
    """Track and analyze user interactions across platforms"""
    create_tool_header("Interaction Tracker", "Monitor all your social interactions", "👥")

    st.subheader("Interaction Overview")

    time_range = st.selectbox("Time Range", ["Today", "Last 7 days", "Last 30 days"])
    platform_filter = st.multiselect("Platforms", [
        "Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok"
    ], default=["Instagram", "Twitter"])

    if st.button("Load Interactions"):
        with st.spinner("Loading interaction data..."):
            interaction_data = generate_interaction_data(time_range, platform_filter)

            # Overview metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Interactions", f"{interaction_data['total']:,}")
            with col2:
                st.metric("Comments", f"{interaction_data['comments']:,}")
            with col3:
                st.metric("Mentions", f"{interaction_data['mentions']:,}")
            with col4:
                st.metric("DMs", f"{interaction_data['dms']:,}")

            # Recent interactions
            st.subheader("Recent Interactions")
            for interaction in interaction_data['recent'][:10]:
                with st.expander(f"{interaction['platform']} - {interaction['type']}"):
                    st.write(f"**User:** {interaction['user']}")
                    st.write(f"**Content:** {interaction['content'][:100]}...")
                    st.write(f"**Status:** {interaction['status']}")


def community_builder():
    """Tools to build and engage your social media community"""
    create_tool_header("Community Builder", "Grow and engage your community", "🏘️")

    st.subheader("Community Growth Strategy")

    current_followers = st.number_input("Current Followers", 0, 10000000, 1000)
    target_growth = st.selectbox("Target Growth", [
        "10% per month", "25% per month", "50% per month", "100% per month"
    ])

    community_type = st.selectbox("Community Type", [
        "Brand Community", "Niche Interest Group", "Professional Network", "Entertainment Community"
    ])

    if st.button("Generate Community Strategy"):
        with st.spinner("Creating community building strategy..."):
            strategy = generate_community_strategy(current_followers, target_growth, community_type)

            st.subheader("🎯 Community Building Strategy")

            tabs = st.tabs(["Growth Plan", "Engagement Tactics", "Content Ideas", "Milestones"])

            with tabs[0]:
                st.write("**Growth Strategy:**")
                for step in strategy['growth_plan']:
                    st.write(f"• {step}")


def response_automation():
    """Automate responses to common social media interactions"""
    create_tool_header("Response Automation", "Automate your social media responses", "🤖")

    st.subheader("Response Templates")

    template_type = st.selectbox("Template Type", [
        "Thank You Messages", "Customer Service", "FAQ Responses", "Welcome Messages"
    ])

    if template_type == "Thank You Messages":
        st.subheader("Thank You Templates")

        scenarios = [
            "General positive comment",
            "Product compliment",
            "Service praise",
            "Share/Repost thank you"
        ]

        for scenario in scenarios:
            with st.expander(f"Template: {scenario}"):
                template = generate_response_template(scenario)
                st.text_area(f"Template", template, key=scenario)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Save Template", key=f"save_{scenario}"):
                        st.success("Template saved!")
                with col2:
                    if st.button(f"Generate Variation", key=f"gen_{scenario}"):
                        variation = generate_response_template(scenario, variation=True)
                        st.write(f"**Variation:** {variation}")


def unified_dashboard():
    """Unified view of all social media accounts and metrics"""
    create_tool_header("Unified Dashboard", "All your social media metrics in one place", "📊")

    st.subheader("Social Media Overview")

    # Account connections
    st.subheader("Connected Accounts")
    platforms = ["Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok", "YouTube"]

    connected_platforms = []
    for platform in platforms:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{platform}**")
        with col2:
            if st.checkbox("Connected", key=platform):
                connected_platforms.append(platform)

    if connected_platforms:
        if st.button("Load Dashboard"):
            dashboard_data = generate_unified_dashboard_data(connected_platforms)

            # Overall metrics
            st.subheader("📈 Overall Performance")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Followers", f"{dashboard_data['total_followers']:,}")
            with col2:
                st.metric("Total Posts", f"{dashboard_data['total_posts']:,}")
            with col3:
                st.metric("Avg Engagement", f"{dashboard_data['avg_engagement']:.2%}")
            with col4:
                st.metric("Total Reach", f"{dashboard_data['total_reach']:,}")

            # Platform breakdown
            st.subheader("Platform Performance")
            for platform in connected_platforms:
                data = dashboard_data['platforms'][platform]
                with st.expander(f"{platform} Metrics"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Followers", f"{data['followers']:,}")
                    with col2:
                        st.metric("Engagement Rate", f"{data['engagement']:.2%}")
                    with col3:
                        st.metric("Recent Posts", data['recent_posts'])


def account_manager():
    """Manage multiple social media accounts efficiently"""
    create_tool_header("Account Manager", "Manage multiple social accounts", "👤")

    st.subheader("Account Management")

    # Account setup
    if 'accounts' not in st.session_state:
        st.session_state.accounts = []

    st.subheader("Add New Account")
    col1, col2, col3 = st.columns(3)
    with col1:
        platform = st.selectbox("Platform", ["Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok"])
    with col2:
        username = st.text_input("Username/Handle")
    with col3:
        account_type = st.selectbox("Type", ["Personal", "Business", "Brand"])

    if st.button("Add Account") and username:
        st.session_state.accounts.append({
            'platform': platform,
            'username': username,
            'type': account_type,
            'status': 'Active'
        })
        st.success(f"Added {platform} account: {username}")

    # Display accounts
    if st.session_state.accounts:
        st.subheader("Your Accounts")
        for i, account in enumerate(st.session_state.accounts):
            with st.expander(f"{account['platform']} - @{account['username']}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Type:** {account['type']}")
                with col2:
                    st.write(f"**Status:** {account['status']}")
                with col3:
                    if st.button("Remove", key=f"remove_{i}"):
                        st.session_state.accounts.pop(i)
                        st.rerun()


def content_distributor():
    """Distribute content efficiently across multiple platforms"""
    create_tool_header("Content Distributor", "Distribute content across all platforms", "📡")

    st.subheader("Content Distribution")

    # Content input
    main_content = st.text_area("Main Content", height=150)
    content_type = st.selectbox("Content Type", [
        "Text Post", "Image Post", "Video Post", "Link Post", "Story"
    ])

    # Platform customization
    st.subheader("Platform Customization")
    platforms = ["Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok"]

    customizations = {}
    for platform in platforms:
        if st.checkbox(f"Include {platform}"):
            with st.expander(f"{platform} Customization"):
                custom_content = st.text_area(f"Custom content for {platform}",
                                              value=main_content, key=f"content_{platform}")
                hashtags = st.text_input(f"Hashtags for {platform}", key=f"hashtags_{platform}")

                customizations[platform] = {
                    'content': custom_content,
                    'hashtags': hashtags
                }

    if st.button("Distribute Content") and customizations:
        st.success(f"Content distributed to {len(customizations)} platforms!")

        for platform, custom in customizations.items():
            with st.expander(f"Preview: {platform}"):
                st.write(f"**Content:** {custom['content'][:100]}...")
                st.write(f"**Hashtags:** {custom['hashtags']}")


def platform_sync():
    """Synchronize settings and content across platforms"""
    create_tool_header("Platform Sync", "Keep your platforms synchronized", "🔄")

    st.subheader("Sync Settings")

    sync_type = st.selectbox("Sync Type", [
        "Profile Information", "Bio/Description", "Contact Info", "Brand Colors", "Posting Schedule"
    ])

    source_platform = st.selectbox("Source Platform", [
        "Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok"
    ])

    target_platforms = st.multiselect("Target Platforms", [
        "Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok"
    ])

    if st.button("Sync Platforms") and target_platforms:
        with st.spinner("Synchronizing platforms..."):
            sync_results = perform_platform_sync(sync_type, source_platform, target_platforms)

            st.subheader("Sync Results")
            for platform, result in sync_results.items():
                status = "✅ Success" if result['success'] else "❌ Failed"
                st.write(f"**{platform}:** {status} - {result['message']}")


def story_creator():
    """Create engaging stories for social media"""
    create_tool_header("Story Creator", "Create compelling social media stories", "📱")

    st.subheader("Story Creation")

    story_type = st.selectbox("Story Type", [
        "Behind the Scenes", "Product Showcase", "Tutorial/Tips", "Poll/Question", "Announcement"
    ])

    platform = st.selectbox("Target Platform", [
        "Instagram Stories", "Facebook Stories", "LinkedIn Stories", "YouTube Shorts"
    ])

    if story_type == "Behind the Scenes":
        st.subheader("Behind the Scenes Story")

        scene_description = st.text_area("Describe the scene", placeholder="What's happening behind the scenes?")
        mood = st.selectbox("Mood", ["Professional", "Casual", "Fun", "Inspiring", "Educational"])

        if scene_description and st.button("Create Story"):
            story_content = generate_story_content(story_type, scene_description, mood, platform)

            st.subheader("📱 Generated Story")
            st.text_area("Story Text", story_content['text'], height=100)

            if story_content.get('stickers'):
                st.write("**Suggested Stickers/Elements:**")
                for sticker in story_content['stickers']:
                    st.write(f"• {sticker}")


def video_scripts():
    """Generate scripts for social media videos"""
    create_tool_header("Video Scripts", "Create engaging video scripts", "🎬")

    st.subheader("Video Script Generator")

    video_type = st.selectbox("Video Type", [
        "Product Demo", "Tutorial", "Behind the Scenes", "Testimonial", "Announcement", "Educational"
    ])

    duration = st.selectbox("Video Duration", [
        "15 seconds (TikTok/Instagram Reels)",
        "30 seconds (Instagram/Twitter)",
        "1 minute (Instagram/Facebook)",
        "2-3 minutes (YouTube Shorts)"
    ])

    topic = st.text_input("Video Topic", placeholder="What's your video about?")
    target_audience = st.selectbox("Target Audience", [
        "General", "Young Adults", "Professionals", "Entrepreneurs", "Students"
    ])

    if topic and st.button("Generate Script"):
        with st.spinner("Generating video script..."):
            script = generate_video_script(video_type, duration, topic, target_audience)

            st.subheader("🎬 Video Script")

            tabs = st.tabs(["Script", "Shot List", "Captions", "Music Suggestions"])

            with tabs[0]:
                st.text_area("Full Script", script['script'], height=300)

            with tabs[1]:
                st.write("**Shot List:**")
                for i, shot in enumerate(script['shots'], 1):
                    st.write(f"{i}. {shot}")


def demographics_analyzer():
    """Analyze audience demographics in detail"""
    create_tool_header("Demographics Analyzer", "Deep dive into audience demographics", "📊")

    st.subheader("Demographic Analysis")

    data_source = st.selectbox("Data Source", [
        "Instagram Insights", "Twitter Analytics", "Facebook Insights", "Sample Data"
    ])

    if st.button("Load Demographics"):
        demo_data = generate_detailed_demographics_data()

        st.subheader("👥 Audience Demographics")

        tabs = st.tabs(["Age & Gender", "Location", "Interests", "Behavior", "Device Usage"])

        with tabs[0]:
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Age Distribution:**")
                for age, pct in demo_data['age_groups'].items():
                    st.progress(pct / 100, text=f"{age}: {pct:.1f}%")

            with col2:
                st.write("**Gender Distribution:**")
                for gender, pct in demo_data['gender'].items():
                    st.progress(pct / 100, text=f"{gender}: {pct:.1f}%")

        with tabs[1]:
            st.write("**Geographic Distribution:**")
            for location, data in demo_data['locations'].items():
                with st.expander(f"{location} ({data['percentage']:.1f}%)"):
                    st.write(f"**Cities:** {', '.join(data['cities'])}")
                    st.write(f"**Activity Level:** {data['activity_level']}")


def behavior_insights():
    """Analyze audience behavior patterns"""
    create_tool_header("Behavior Insights", "Understand how your audience behaves", "🧠")

    st.subheader("Behavior Analysis")

    analysis_period = st.selectbox("Analysis Period", [
        "Last 7 days", "Last 30 days", "Last 3 months"
    ])

    if st.button("Analyze Behavior"):
        behavior_data = generate_behavior_insights_data(analysis_period)

        st.subheader("🧠 Behavior Insights")

        tabs = st.tabs(["Activity Patterns", "Content Preferences", "Engagement Behavior", "Shopping Behavior"])

        with tabs[0]:
            st.write("**Peak Activity Hours:**")
            for hour, activity in behavior_data['activity_hours'].items():
                st.write(f"**{hour}:** {activity:.1f}% of daily activity")

        with tabs[1]:
            st.write("**Content Type Preferences:**")
            for content_type, engagement in behavior_data['content_preferences'].items():
                st.write(f"**{content_type}:** {engagement:.2f}% avg engagement")


def growth_tracking():
    """Track detailed growth metrics over time"""
    create_tool_header("Growth Tracking", "Track your growth journey", "📈")

    st.subheader("Growth Metrics")

    metric_type = st.selectbox("Metric to Track", [
        "Follower Growth", "Engagement Growth", "Reach Growth", "Content Performance"
    ])

    time_period = st.selectbox("Time Period", [
        "Last 30 days", "Last 3 months", "Last 6 months", "Last year"
    ])

    if st.button("Load Growth Data"):
        growth_data = generate_growth_tracking_data(metric_type, time_period)

        st.subheader(f"📊 {metric_type} Tracking")

        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Current Value", f"{growth_data['current']:,}")
        with col2:
            st.metric("Growth Rate", f"+{growth_data['growth_rate']:.1f}%")
        with col3:
            st.metric("Best Period", growth_data['best_period'])
        with col4:
            st.metric("Projected", f"{growth_data['projected']:,}")

        # Growth insights
        st.subheader("📈 Growth Insights")
        for insight in growth_data['insights']:
            st.write(f"• {insight}")


def engagement_patterns():
    """Analyze engagement patterns and trends"""
    create_tool_header("Engagement Patterns", "Discover your engagement patterns", "💫")

    st.subheader("Pattern Analysis")

    pattern_type = st.selectbox("Pattern Type", [
        "Hourly Patterns", "Daily Patterns", "Content Type Patterns", "Seasonal Patterns"
    ])

    if st.button("Analyze Patterns"):
        pattern_data = generate_engagement_patterns_data(pattern_type)

        st.subheader(f"💫 {pattern_type}")

        if pattern_type == "Hourly Patterns" and 'hourly' in pattern_data:
            st.write("**Best Engagement Hours:**")
            hourly_data = pattern_data.get('hourly', {})
            for hour, engagement in hourly_data.items():
                if isinstance(engagement, (int, float)):
                    color = "green" if engagement > 5 else "orange" if engagement > 3 else "red"
                    st.write(f"**{hour}:** {engagement:.1f}% engagement")

        elif pattern_type == "Content Type Patterns" and 'content_types' in pattern_data:
            st.write("**Content Performance:**")
            content_data = pattern_data.get('content_types', {})
            for content_type, metrics in content_data.items():
                if isinstance(metrics, dict):
                    with st.expander(f"{content_type}"):
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            likes = metrics.get('likes', 0)
                            if isinstance(likes, (int, float)):
                                st.metric("Avg Likes", f"{likes:,}")
                        with col2:
                            comments = metrics.get('comments', 0)
                            if isinstance(comments, (int, float)):
                                st.metric("Avg Comments", f"{comments:,}")
                        with col3:
                            engagement = metrics.get('engagement', 0.0)
                            if isinstance(engagement, (int, float)):
                                st.metric("Engagement Rate", f"{engagement:.2%}")

        else:
            st.info(f"Pattern analysis for {pattern_type} is being processed...")


def performance_monitor():
    """Monitor performance across all campaigns and posts"""
    create_tool_header("Performance Monitor", "Monitor all your content performance", "📊")

    st.subheader("Performance Monitoring")

    monitor_type = st.selectbox("Monitor Type", [
        "Real-time Performance", "Campaign Performance", "Content Performance", "Overall Performance"
    ])

    if st.button("Load Performance Data"):
        perf_data = generate_performance_monitor_data(monitor_type)

        st.subheader("📊 Performance Dashboard")

        # Alert section
        if perf_data.get('alerts'):
            st.subheader("🚨 Performance Alerts")
            for alert in perf_data['alerts']:
                alert_type = "error" if alert['type'] == 'critical' else "warning"
                st.error(alert['message']) if alert_type == "error" else st.warning(alert['message'])

        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Reach", f"{perf_data['total_reach']:,}",
                      f"+{perf_data['reach_change']:.1f}%")
        with col2:
            st.metric("Engagement Rate", f"{perf_data['engagement_rate']:.2%}",
                      f"+{perf_data['engagement_change']:.1f}%")
        with col3:
            st.metric("Active Campaigns", perf_data['active_campaigns'])
        with col4:
            st.metric("Performance Score", f"{perf_data['performance_score']}/100")


def roi_tracker():
    """Track return on investment for social media activities"""
    create_tool_header("ROI Tracker", "Track your social media ROI", "💰")

    st.subheader("ROI Calculation")

    # Investment inputs
    st.subheader("Investment")
    col1, col2 = st.columns(2)
    with col1:
        ad_spend = st.number_input("Ad Spend ($)", 0.0, 100000.0, 0.0)
        content_cost = st.number_input("Content Creation Cost ($)", 0.0, 50000.0, 0.0)
    with col2:
        tool_costs = st.number_input("Tool/Software Costs ($)", 0.0, 10000.0, 0.0)
        time_investment = st.number_input("Time Investment (hours)", 0.0, 1000.0, 0.0)

    hourly_rate = st.number_input("Your Hourly Rate ($)", 0.0, 500.0, 50.0)

    # Returns
    st.subheader("Returns")
    sales_generated = st.number_input("Sales Generated ($)", 0.0, 1000000.0, 0.0)
    leads_generated = st.number_input("Leads Generated", 0, 10000, 0)
    lead_value = st.number_input("Average Lead Value ($)", 0.0, 10000.0, 0.0)

    if st.button("Calculate ROI"):
        roi_data = calculate_social_media_roi(
            ad_spend, content_cost, tool_costs, time_investment, hourly_rate,
            sales_generated, leads_generated, lead_value
        )

        st.subheader("💰 ROI Results")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Investment", f"${roi_data['total_investment']:,.2f}")
        with col2:
            st.metric("Total Return", f"${roi_data['total_return']:,.2f}")
        with col3:
            st.metric("ROI", f"{roi_data['roi']:.1f}%")
        with col4:
            color = "normal" if roi_data['roi'] > 0 else "inverse"
            st.metric("Profit/Loss", f"${roi_data['profit']:,.2f}")


def campaign_analytics():
    """Comprehensive campaign analytics"""
    create_tool_header("Campaign Analytics", "Deep dive into campaign performance", "📈")

    st.subheader("Campaign Analysis")

    campaign_name = st.text_input("Campaign Name", placeholder="Enter campaign name")
    campaign_type = st.selectbox("Campaign Type", [
        "Product Launch", "Brand Awareness", "Lead Generation", "Sales Campaign", "Event Promotion"
    ])

    date_range = st.selectbox("Date Range", [
        "Last 7 days", "Last 30 days", "Custom Range"
    ])

    if campaign_name and st.button("Analyze Campaign"):
        campaign_data = generate_campaign_analytics_data(campaign_name, campaign_type, date_range)

        st.subheader(f"📊 {campaign_name} Analytics")

        # Key performance indicators
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Reach", f"{campaign_data['total_reach']:,}")
        with col2:
            st.metric("Engagement Rate", f"{campaign_data['engagement_rate']:.2%}")
        with col3:
            st.metric("Conversion Rate", f"{campaign_data['conversion_rate']:.2%}")
        with col4:
            st.metric("Campaign Score", f"{campaign_data['score']}/100")

        # Platform breakdown
        st.subheader("Platform Performance")
        for platform, metrics in campaign_data['platforms'].items():
            with st.expander(f"{platform} Performance"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Reach", f"{metrics['reach']:,}")
                with col2:
                    st.metric("Engagement", f"{metrics['engagement']:.2%}")
                with col3:
                    st.metric("Conversions", metrics['conversions'])


def trend_detection():
    """Detect trending topics and hashtags"""
    create_tool_header("Trend Detection", "Spot trending topics before they explode", "🔥")

    st.subheader("Trend Analysis")

    trend_type = st.selectbox("Trend Type", [
        "Hashtag Trends", "Topic Trends", "Industry Trends", "Geographic Trends"
    ])

    platform = st.selectbox("Platform", [
        "All Platforms", "Twitter", "Instagram", "TikTok", "LinkedIn"
    ])

    if st.button("Detect Trends"):
        with st.spinner("Analyzing trending data..."):
            trend_data = generate_trend_detection_data(trend_type, platform)

            st.subheader("🔥 Trending Now")

            tabs = st.tabs(["Rising Trends", "Established Trends", "Declining Trends", "Predictions"])

            with tabs[0]:
                st.write("**Rising Trends (📈 Growth > 200%):**")
                for trend in trend_data['rising']:
                    col1, col2, col3 = st.columns([2, 1, 1])
                    with col1:
                        st.write(f"**{trend['name']}**")
                    with col2:
                        st.write(f"Growth: +{trend['growth']:.0f}%")
                    with col3:
                        st.write(f"Volume: {trend['volume']:,}")


def collaboration_manager():
    """Manage influencer and brand collaborations"""
    create_tool_header("Collaboration Manager", "Manage all your collaborations", "🤝")

    st.subheader("Collaboration Dashboard")

    if 'collaborations' not in st.session_state:
        st.session_state.collaborations = []

    # Add new collaboration
    st.subheader("New Collaboration")
    col1, col2, col3 = st.columns(3)
    with col1:
        partner_name = st.text_input("Partner/Influencer Name")
        collaboration_type = st.selectbox("Type", [
            "Sponsored Post", "Product Review", "Brand Partnership", "Event Collaboration"
        ])
    with col2:
        platform = st.selectbox("Platform", [
            "Instagram", "Twitter", "YouTube", "TikTok", "LinkedIn"
        ])
        status = st.selectbox("Status", [
            "Planning", "In Progress", "Content Created", "Published", "Completed"
        ])
    with col3:
        budget = st.number_input("Budget ($)", 0.0, 100000.0, 0.0)
        deadline = st.date_input("Deadline")

    if st.button("Add Collaboration") and partner_name:
        st.session_state.collaborations.append({
            'partner': partner_name,
            'type': collaboration_type,
            'platform': platform,
            'status': status,
            'budget': budget,
            'deadline': deadline
        })
        st.success(f"Added collaboration with {partner_name}")

    # Display collaborations
    if st.session_state.collaborations:
        st.subheader("Active Collaborations")
        for i, collab in enumerate(st.session_state.collaborations):
            with st.expander(f"{collab['partner']} - {collab['type']}"):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write(f"**Platform:** {collab['platform']}")
                with col2:
                    st.write(f"**Status:** {collab['status']}")
                with col3:
                    st.write(f"**Budget:** ${collab['budget']:,.2f}")
                with col4:
                    st.write(f"**Deadline:** {collab['deadline']}")


def outreach_automation():
    """Automate influencer and partner outreach"""
    create_tool_header("Outreach Automation", "Automate your outreach campaigns", "📧")

    st.subheader("Outreach Campaign")

    campaign_type = st.selectbox("Campaign Type", [
        "Influencer Outreach", "Brand Partnership", "Guest Posting", "Collaboration Request"
    ])

    # Target criteria
    st.subheader("Target Criteria")
    col1, col2 = st.columns(2)
    with col1:
        min_followers = st.number_input("Min Followers", 1000, 10000000, 10000)
        max_followers = st.number_input("Max Followers", 1000, 10000000, 100000)
        engagement_rate = st.slider("Min Engagement Rate", 0.0, 20.0, 2.0)

    with col2:
        niche = st.multiselect("Niche/Industry", [
            "Fashion", "Beauty", "Technology", "Food", "Travel", "Fitness", "Business"
        ])
        location = st.multiselect("Location", [
            "United States", "Canada", "United Kingdom", "Australia", "Global"
        ])

    # Message template
    st.subheader("Outreach Message")
    message_template = st.text_area("Message Template",
                                    placeholder="Hi [NAME], I love your content about [NICHE]...",
                                    height=150
                                    )

    if st.button("Start Outreach Campaign"):
        if message_template and niche:
            outreach_results = simulate_outreach_campaign(
                campaign_type, min_followers, max_followers,
                engagement_rate, niche, location, message_template
            )

            st.subheader("📧 Campaign Results")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Targets Found", outreach_results['targets_found'])
            with col2:
                st.metric("Messages Sent", outreach_results['messages_sent'])
            with col3:
                st.metric("Response Rate", f"{outreach_results['response_rate']:.1f}%")
            with col4:
                st.metric("Interested", outreach_results['interested'])


def roi_calculator():
    """Calculate ROI for different social media strategies"""
    create_tool_header("ROI Calculator", "Calculate social media ROI and projections", "🧮")

    st.subheader("ROI Calculator")

    calculation_type = st.selectbox("Calculation Type", [
        "Current ROI", "Projected ROI", "Campaign ROI", "Influencer ROI"
    ])

    if calculation_type == "Current ROI":
        st.subheader("Current Performance ROI")

        # Costs
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Costs:**")
            monthly_ad_spend = st.number_input("Monthly Ad Spend ($)", 0.0, 50000.0, 1000.0)
            content_costs = st.number_input("Content Creation ($)", 0.0, 10000.0, 500.0)
            tool_costs = st.number_input("Tools/Software ($)", 0.0, 1000.0, 100.0)
            time_hours = st.number_input("Time Investment (hours/month)", 0.0, 200.0, 40.0)
            hourly_rate = st.number_input("Your Hourly Rate ($)", 0.0, 200.0, 50.0)

        with col2:
            st.write("**Returns:**")
            direct_sales = st.number_input("Direct Sales ($)", 0.0, 100000.0, 5000.0)
            leads = st.number_input("Leads Generated", 0, 1000, 50)
            lead_value = st.number_input("Average Lead Value ($)", 0.0, 1000.0, 100.0)
            brand_value = st.number_input("Brand Value Increase ($)", 0.0, 50000.0, 1000.0)

        if st.button("Calculate ROI"):
            roi_results = calculate_comprehensive_roi(
                monthly_ad_spend, content_costs, tool_costs, time_hours, hourly_rate,
                direct_sales, leads, lead_value, brand_value
            )

            st.subheader("📊 ROI Results")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Investment", f"${roi_results['total_cost']:,.2f}")
            with col2:
                st.metric("Total Return", f"${roi_results['total_return']:,.2f}")
            with col3:
                roi_color = "green" if roi_results['roi_percentage'] > 0 else "red"
                st.metric("ROI", f"{roi_results['roi_percentage']:.1f}%")
            with col4:
                st.metric("Monthly Profit", f"${roi_results['monthly_profit']:,.2f}")

            # ROI breakdown
            st.subheader("ROI Breakdown")
            breakdown = roi_results['breakdown']
            for source, value in breakdown.items():
                st.write(f"**{source}:** ${value:,.2f}")


# Helper functions for the new tools

def generate_optimal_times_data(platform, location):
    """Generate optimal posting times data"""
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_times = {}

    for day in days:
        daily_times[day] = {
            'best_time': random.choice(['9:00 AM', '12:00 PM', '3:00 PM', '6:00 PM', '8:00 PM']),
            'score': random.uniform(7.0, 10.0),
            'reach_potential': random.uniform(60, 95)
        }

    recommendations = [
        f"Best overall time for {platform}: {random.choice(['12:00 PM', '6:00 PM', '8:00 PM'])}",
        "Weekends show 15% higher engagement for visual content",
        "Avoid posting during 2-4 PM for optimal visibility"
    ]

    return {
        'daily_times': daily_times,
        'recommendations': recommendations
    }


def generate_bulk_template():
    """Generate CSV template for bulk scheduling"""
    return "Content,Platform,Date,Time,Hashtags,Notes\nSample post content,Instagram,2024-01-15,12:00,#marketing #social,First post\n"


def generate_comprehensive_competitor_analysis(name, depth):
    """Generate comprehensive competitor analysis"""
    return {
        'overall_score': random.randint(65, 95),
        'content_quality': random.uniform(6.0, 9.5),
        'engagement_rate': random.uniform(0.02, 0.12),
        'market_share': random.uniform(5.0, 25.0)
    }


def generate_niche_data(topic, platform):
    """Generate niche discovery data"""
    return {
        'micro_niches': [
            {
                'name': f"Sustainable {topic}",
                'competition': 'Low',
                'description': f"Eco-friendly approach to {topic}",
                'potential': 8.5,
                'hashtags': ['#sustainable', f'#{topic}', '#eco']
            },
            {
                'name': f"DIY {topic}",
                'competition': 'Medium',
                'description': f"Do-it-yourself {topic} content",
                'potential': 7.2,
                'hashtags': ['#diy', f'#{topic}', '#handmade']
            }
        ]
    }


def generate_hashtag_analytics_data(hashtags, period):
    """Generate hashtag analytics data"""
    analytics = {}
    for hashtag in hashtags:
        analytics[hashtag] = {
            'total_posts': random.randint(10000, 1000000),
            'avg_engagement': random.randint(100, 50000),
            'difficulty': random.randint(3, 10),
            'trend': random.choice(['Rising', 'Stable', 'Declining'])
        }
    return analytics


def generate_optimized_hashtags(topic, platform, goal):
    """Generate optimized hashtag combinations"""
    return {
        'primary': [
            {'tag': f'{topic}', 'reach': 'High', 'competition': 'Medium'},
            {'tag': f'{topic}tips', 'reach': 'Medium', 'competition': 'Low'},
            {'tag': f'{topic}community', 'reach': 'Medium', 'competition': 'Low'}
        ]
    }


def generate_interaction_data(time_range, platforms):
    """Generate interaction tracking data"""
    return {
        'total': random.randint(500, 5000),
        'comments': random.randint(100, 1000),
        'mentions': random.randint(50, 500),
        'dms': random.randint(20, 200),
        'recent': [
            {
                'platform': random.choice(platforms),
                'type': random.choice(['Comment', 'Mention', 'DM']),
                'user': f'user{random.randint(1, 1000)}',
                'content': 'Great post! Love your content.',
                'status': random.choice(['Responded', 'Pending', 'Read'])
            } for _ in range(20)
        ]
    }


def generate_community_strategy(followers, growth, community_type):
    """Generate community building strategy"""
    return {
        'growth_plan': [
            'Post consistently 3-5 times per week',
            'Engage with comments within 2 hours',
            'Host weekly live sessions or Q&As',
            'Collaborate with micro-influencers',
            'Create user-generated content campaigns'
        ]
    }


def generate_response_template(scenario, variation=False):
    """Generate response templates"""
    templates = {
        "General positive comment": "Thank you so much for your kind words! 😊 We're thrilled you enjoyed our content!",
        "Product compliment": "We're so happy you love our product! Your support means everything to us! 💙",
        "Service praise": "Thank you for recognizing our efforts! We're always here to help! 🌟",
        "Share/Repost thank you": "Thanks for sharing! We appreciate you spreading the word! 🙏"
    }

    base = templates.get(scenario, "Thank you for your engagement!")

    if variation:
        return base.replace("Thank you", "Thanks").replace("😊", "🎉")

    return base


def generate_unified_dashboard_data(platforms):
    """Generate unified dashboard data"""
    return {
        'total_followers': sum(random.randint(5000, 100000) for _ in platforms),
        'total_posts': sum(random.randint(10, 100) for _ in platforms),
        'avg_engagement': random.uniform(0.02, 0.08),
        'total_reach': sum(random.randint(10000, 500000) for _ in platforms),
        'platforms': {
            platform: {
                'followers': random.randint(5000, 100000),
                'engagement': random.uniform(0.01, 0.12),
                'recent_posts': random.randint(5, 25)
            } for platform in platforms
        }
    }


def perform_platform_sync(sync_type, source, targets):
    """Simulate platform synchronization"""
    results = {}
    for target in targets:
        results[target] = {
            'success': random.choice([True, True, True, False]),  # 75% success rate
            'message': 'Successfully synced' if results.get(target, {}).get('success',
                                                                            True) else 'Sync failed - check permissions'
        }
    return results


def generate_story_content(story_type, description, mood, platform):
    """Generate story content"""
    return {
        'text': f"Behind the scenes: {description}\n\nWhat do you think? 🤔",
        'stickers': ['Poll sticker', 'Question sticker', 'Location tag', 'Hashtag sticker']
    }


def generate_video_script(video_type, duration, topic, audience):
    """Generate video script"""
    return {
        'script': f"""HOOK (0-3s): "Want to learn about {topic}? Here's what you need to know..."

INTRODUCTION (3-8s): Hi everyone! Today we're diving deep into {topic}.

MAIN CONTENT (8-25s): 
- Key point 1 about {topic}
- Key point 2 that {audience} should know
- Practical tip they can use immediately

CALL TO ACTION (25-30s): What's your experience with {topic}? Comment below!""",

        'shots': [
            'Close-up of speaker with engaging expression',
            'B-roll footage related to topic',
            'Text overlay with key points',
            'Final shot with clear CTA'
        ]
    }


def generate_detailed_demographics_data():
    """Generate detailed demographic data"""
    return {
        'age_groups': {
            '18-24': random.uniform(15, 30),
            '25-34': random.uniform(30, 45),
            '35-44': random.uniform(20, 35),
            '45-54': random.uniform(10, 20),
            '55+': random.uniform(5, 15)
        },
        'gender': {
            'Female': random.uniform(45, 65),
            'Male': random.uniform(35, 55),
            'Non-binary': random.uniform(1, 5)
        },
        'locations': {
            'United States': {
                'percentage': random.uniform(40, 60),
                'cities': ['New York', 'Los Angeles', 'Chicago'],
                'activity_level': 'High'
            },
            'Canada': {
                'percentage': random.uniform(10, 20),
                'cities': ['Toronto', 'Vancouver', 'Montreal'],
                'activity_level': 'Medium'
            }
        }
    }


def generate_behavior_insights_data(period):
    """Generate behavior insights data"""
    return {
        'activity_hours': {
            '9-12 AM': random.uniform(15, 25),
            '12-3 PM': random.uniform(20, 30),
            '3-6 PM': random.uniform(25, 35),
            '6-9 PM': random.uniform(30, 40),
            '9-12 AM': random.uniform(10, 20)
        },
        'content_preferences': {
            'Video Content': random.uniform(4, 8),
            'Image Posts': random.uniform(3, 6),
            'Text Posts': random.uniform(2, 4),
            'Stories': random.uniform(5, 9)
        }
    }


def generate_growth_tracking_data(metric_type, period):
    """Generate growth tracking data"""
    return {
        'current': random.randint(10000, 100000),
        'growth_rate': random.uniform(5, 30),
        'best_period': random.choice(['Week 2', 'Week 3', 'Month 2']),
        'projected': random.randint(15000, 150000),
        'insights': [
            f'{metric_type} is trending upward',
            'Best growth occurs on weekends',
            'Video content drives 40% more growth'
        ]
    }


def generate_engagement_patterns_data(pattern_type):
    """Generate engagement pattern data"""
    if pattern_type == "Hourly Patterns":
        return {
            'hourly': {f'{h}:00': random.uniform(2, 8) for h in range(0, 24)}
        }
    elif pattern_type == "Content Type Patterns":
        return {
            'content_types': {
                'Video': {'likes': random.randint(500, 5000), 'comments': random.randint(50, 500),
                          'engagement': random.uniform(0.04, 0.12)},
                'Image': {'likes': random.randint(300, 3000), 'comments': random.randint(30, 300),
                          'engagement': random.uniform(0.03, 0.08)},
                'Carousel': {'likes': random.randint(400, 4000), 'comments': random.randint(40, 400),
                             'engagement': random.uniform(0.035, 0.10)}
            }
        }
    return {}


def generate_performance_monitor_data(monitor_type):
    """Generate performance monitoring data"""
    return {
        'total_reach': random.randint(50000, 500000),
        'reach_change': random.uniform(-10, 30),
        'engagement_rate': random.uniform(0.02, 0.08),
        'engagement_change': random.uniform(-5, 15),
        'active_campaigns': random.randint(2, 8),
        'performance_score': random.randint(65, 95),
        'alerts': [
            {'type': 'warning', 'message': 'Engagement down 15% this week'},
            {'type': 'info', 'message': 'New follower milestone reached'}
        ] if random.choice([True, False]) else []
    }


def calculate_social_media_roi(ad_spend, content_cost, tool_costs, time_investment, hourly_rate, sales, leads,
                               lead_value):
    """Calculate social media ROI"""
    total_investment = ad_spend + content_cost + tool_costs + (time_investment * hourly_rate)
    total_return = sales + (leads * lead_value)
    profit = total_return - total_investment
    roi = (profit / total_investment * 100) if total_investment > 0 else 0

    return {
        'total_investment': total_investment,
        'total_return': total_return,
        'profit': profit,
        'roi': roi
    }


def generate_campaign_analytics_data(name, campaign_type, date_range):
    """Generate campaign analytics data"""
    return {
        'total_reach': random.randint(10000, 1000000),
        'engagement_rate': random.uniform(0.02, 0.15),
        'conversion_rate': random.uniform(0.5, 5.0),
        'score': random.randint(70, 95),
        'platforms': {
            'Instagram': {'reach': random.randint(5000, 500000), 'engagement': random.uniform(0.03, 0.12),
                          'conversions': random.randint(10, 100)},
            'Facebook': {'reach': random.randint(3000, 300000), 'engagement': random.uniform(0.02, 0.08),
                         'conversions': random.randint(5, 50)},
            'Twitter': {'reach': random.randint(2000, 200000), 'engagement': random.uniform(0.01, 0.06),
                        'conversions': random.randint(3, 30)}
        }
    }


def generate_trend_detection_data(trend_type, platform):
    """Generate trend detection data"""
    return {
        'rising': [
            {'name': f'#{random.choice(["AI", "sustainability", "wellness", "productivity"])}',
             'growth': random.uniform(200, 500), 'volume': random.randint(10000, 100000)},
            {'name': f'#{random.choice(["remote", "digital", "innovation", "future"])}',
             'growth': random.uniform(150, 400), 'volume': random.randint(8000, 80000)},
            {'name': f'#{random.choice(["startup", "entrepreneur", "growth", "success"])}',
             'growth': random.uniform(100, 300), 'volume': random.randint(5000, 50000)}
        ]
    }


def simulate_outreach_campaign(campaign_type, min_followers, max_followers, engagement_rate, niche, location, message):
    """Simulate outreach campaign results"""
    targets_found = random.randint(50, 500)
    messages_sent = int(targets_found * random.uniform(0.7, 0.9))
    response_rate = random.uniform(10, 30)
    interested = int(messages_sent * (response_rate / 100) * random.uniform(0.6, 0.8))

    return {
        'targets_found': targets_found,
        'messages_sent': messages_sent,
        'response_rate': response_rate,
        'interested': interested
    }


def calculate_comprehensive_roi(ad_spend, content_costs, tool_costs, time_hours, hourly_rate, direct_sales, leads,
                                lead_value, brand_value):
    """Calculate comprehensive ROI"""
    total_cost = ad_spend + content_costs + tool_costs + (time_hours * hourly_rate)
    total_return = direct_sales + (leads * lead_value) + brand_value
    monthly_profit = total_return - total_cost
    roi_percentage = (monthly_profit / total_cost * 100) if total_cost > 0 else 0

    return {
        'total_cost': total_cost,
        'total_return': total_return,
        'monthly_profit': monthly_profit,
        'roi_percentage': roi_percentage,
        'breakdown': {
            'Direct Sales': direct_sales,
            'Lead Value': leads * lead_value,
            'Brand Value': brand_value
        }
    }
