import streamlit as st
import re
import requests
from urllib.parse import urlparse, urljoin
import json
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler


def display_tools():
    """Display all SEO and marketing tools"""

    tool_categories = {
        "SEO Analysis": [
            "Page SEO Analyzer", "Meta Tag Checker", "Keyword Density", "Heading Structure", "Internal Link Checker"
        ],
        "Content Marketing": [
            "Content Planner", "Keyword Research", "Competitor Analysis", "Content Calendar", "Topic Generator"
        ],
        "Social Media": [
            "Hashtag Generator", "Post Scheduler", "Engagement Calculator", "Handle Checker", "Bio Generator"
        ],
        "Email Marketing": [
            "Subject Line Tester", "Email Template", "List Segmentation", "A/B Test Calculator",
            "Deliverability Checker"
        ],
        "Analytics Tools": [
            "UTM Builder", "Click Tracker", "Conversion Calculator", "ROI Calculator", "Traffic Estimator"
        ],
        "Local SEO": [
            "Local Citation Checker", "GMB Optimizer", "Local Keyword Tool", "Review Generator", "NAP Consistency"
        ],
        "Technical SEO": [
            "Robots.txt Generator", "Sitemap Validator", "Schema Markup", "Canonical URL Checker", "Redirect Checker"
        ],
        "Link Building": [
            "Backlink Analyzer", "Anchor Text Analyzer", "Link Prospecting", "Outreach Templates",
            "Link Quality Checker"
        ],
        "PPC Tools": [
            "Ad Copy Generator", "Keyword Bid Calculator", "Quality Score Estimator", "Ad Preview",
            "Landing Page Analyzer"
        ],
        "Conversion Optimization": [
            "A/B Test Calculator", "Heatmap Analyzer", "Funnel Analyzer", "CRO Checklist", "Form Optimizer"
        ]
    }

    selected_category = st.selectbox("Select SEO/Marketing Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"SEO/Marketing Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Page SEO Analyzer":
        page_seo_analyzer()
    elif selected_tool == "Meta Tag Checker":
        meta_tag_checker()
    elif selected_tool == "Keyword Density":
        keyword_density()
    elif selected_tool == "UTM Builder":
        utm_builder()
    elif selected_tool == "Hashtag Generator":
        hashtag_generator()
    elif selected_tool == "Subject Line Tester":
        subject_line_tester()
    elif selected_tool == "Robots.txt Generator":
        robots_txt_generator()
    elif selected_tool == "Schema Markup":
        schema_markup_generator()
    elif selected_tool == "A/B Test Calculator":
        ab_test_calculator()
    elif selected_tool == "Heading Structure":
        heading_structure()
    elif selected_tool == "Internal Link Checker":
        internal_link_checker()
    elif selected_tool == "Content Planner":
        content_planner()
    elif selected_tool == "Keyword Research":
        keyword_research()
    elif selected_tool == "Competitor Analysis":
        competitor_analysis()
    elif selected_tool == "Content Calendar":
        content_calendar()
    elif selected_tool == "Topic Generator":
        topic_generator()
    elif selected_tool == "Post Scheduler":
        post_scheduler()
    elif selected_tool == "Engagement Calculator":
        engagement_calculator()
    elif selected_tool == "Handle Checker":
        handle_checker()
    elif selected_tool == "Bio Generator":
        bio_generator()
    # Email Marketing tools
    elif selected_tool == "Email Template":
        email_template()
    elif selected_tool == "List Segmentation":
        list_segmentation()
    elif selected_tool == "Deliverability Checker":
        deliverability_checker()
    # Analytics tools
    elif selected_tool == "Click Tracker":
        click_tracker()
    elif selected_tool == "Conversion Calculator":
        conversion_calculator()
    elif selected_tool == "ROI Calculator":
        roi_calculator()
    elif selected_tool == "Traffic Estimator":
        traffic_estimator()
    # Local SEO tools
    elif selected_tool == "Local Citation Checker":
        local_citation_checker()
    elif selected_tool == "GMB Optimizer":
        gmb_optimizer()
    elif selected_tool == "Local Keyword Tool":
        local_keyword_tool()
    elif selected_tool == "Review Generator":
        review_generator()
    elif selected_tool == "NAP Consistency":
        nap_consistency()
    # Technical SEO tools
    elif selected_tool == "Sitemap Validator":
        sitemap_validator()
    elif selected_tool == "Canonical URL Checker":
        canonical_url_checker()
    elif selected_tool == "Redirect Checker":
        redirect_checker()
    # Link Building tools
    elif selected_tool == "Backlink Analyzer":
        backlink_analyzer()
    elif selected_tool == "Anchor Text Analyzer":
        anchor_text_analyzer()
    elif selected_tool == "Link Prospecting":
        link_prospecting()
    elif selected_tool == "Outreach Templates":
        outreach_templates()
    elif selected_tool == "Link Quality Checker":
        link_quality_checker()
    # PPC tools
    elif selected_tool == "Ad Copy Generator":
        ad_copy_generator()
    elif selected_tool == "Keyword Bid Calculator":
        keyword_bid_calculator()
    elif selected_tool == "Quality Score Estimator":
        quality_score_estimator()
    elif selected_tool == "Ad Preview":
        ad_preview()
    elif selected_tool == "Landing Page Analyzer":
        landing_page_analyzer()
    # Conversion Optimization tools
    elif selected_tool == "Heatmap Analyzer":
        heatmap_analyzer()
    elif selected_tool == "Funnel Analyzer":
        funnel_analyzer()
    elif selected_tool == "CRO Checklist":
        cro_checklist()
    elif selected_tool == "Form Optimizer":
        form_optimizer()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def page_seo_analyzer():
    """Analyze page SEO"""
    create_tool_header("Page SEO Analyzer", "Analyze your webpage for SEO optimization", "🔍")

    url = st.text_input("Enter webpage URL:", placeholder="https://example.com/page")

    if url and st.button("Analyze SEO"):
        if url.startswith(('http://', 'https://')):
            with st.spinner("Analyzing page..."):
                analysis = analyze_page_seo(url)
                display_seo_analysis(analysis)
        else:
            st.error("Please enter a valid URL starting with http:// or https://")


def analyze_page_seo(url):
    """Analyze webpage for SEO factors"""
    try:
        response = requests.get(url, timeout=30)
        html_content = response.text

        analysis = {
            'title': extract_title(html_content),
            'meta_description': extract_meta_description(html_content),
            'headings': extract_headings(html_content),
            'images': analyze_images(html_content),
            'links': analyze_links(html_content, url),
            'word_count': count_words(html_content),
            'success': True
        }

        return analysis
    except Exception as e:
        return {'error': str(e), 'success': False}


def extract_title(html):
    """Extract page title"""
    match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else None


def extract_meta_description(html):
    """Extract meta description"""
    match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if not match:
        match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', html, re.IGNORECASE)
    return match.group(1).strip() if match else None


def extract_headings(html):
    """Extract heading tags"""
    headings = {}
    for i in range(1, 7):
        pattern = f'<h{i}[^>]*>(.*?)</h{i}>'
        matches = re.findall(pattern, html, re.IGNORECASE | re.DOTALL)
        headings[f'h{i}'] = [re.sub(r'<[^>]+>', '', match).strip() for match in matches]
    return headings


def analyze_images(html):
    """Analyze images for alt text"""
    img_pattern = r'<img[^>]*>'
    images = re.findall(img_pattern, html, re.IGNORECASE)

    total_images = len(images)
    images_with_alt = 0

    for img in images:
        if re.search(r'alt=["\'][^"\']*["\']', img, re.IGNORECASE):
            images_with_alt += 1

    return {
        'total': total_images,
        'with_alt': images_with_alt,
        'without_alt': total_images - images_with_alt
    }


def analyze_links(html, base_url):
    """Analyze internal and external links"""
    link_pattern = r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>'
    links = re.findall(link_pattern, html, re.IGNORECASE)

    internal_links = 0
    external_links = 0

    domain = urlparse(base_url).netloc

    for link in links:
        if link.startswith(('http://', 'https://')):
            if urlparse(link).netloc == domain:
                internal_links += 1
            else:
                external_links += 1
        elif link.startswith('/') or not link.startswith(('mailto:', 'tel:')):
            internal_links += 1

    return {
        'total': len(links),
        'internal': internal_links,
        'external': external_links
    }


def count_words(html):
    """Count words in page content"""
    # Remove script and style elements
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Count words
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def display_seo_analysis(analysis):
    """Display SEO analysis results"""
    if not analysis['success']:
        st.error(f"❌ Analysis failed: {analysis['error']}")
        return

    # Title analysis
    st.markdown("### 📝 Title Tag")
    if analysis['title']:
        title_length = len(analysis['title'])
        if 30 <= title_length <= 60:
            st.success(f"✅ Title length: {title_length} characters (optimal)")
        elif title_length < 30:
            st.warning(f"⚠️ Title length: {title_length} characters (too short)")
        else:
            st.error(f"❌ Title length: {title_length} characters (too long)")
        st.code(analysis['title'])
    else:
        st.error("❌ No title tag found")

    # Meta description analysis
    st.markdown("### 📄 Meta Description")
    if analysis['meta_description']:
        desc_length = len(analysis['meta_description'])
        if 150 <= desc_length <= 160:
            st.success(f"✅ Description length: {desc_length} characters (optimal)")
        elif desc_length < 150:
            st.warning(f"⚠️ Description length: {desc_length} characters (too short)")
        else:
            st.error(f"❌ Description length: {desc_length} characters (too long)")
        st.code(analysis['meta_description'])
    else:
        st.error("❌ No meta description found")

    # Headings analysis
    st.markdown("### 📋 Heading Structure")
    for heading, content in analysis['headings'].items():
        if content:
            st.write(f"**{heading.upper()}:** {len(content)} found")
            for i, text in enumerate(content[:3], 1):  # Show first 3
                st.write(f"  {i}. {text[:100]}...")

    # Images analysis
    st.markdown("### 🖼️ Images")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Images", analysis['images']['total'])
    with col2:
        st.metric("With Alt Text", analysis['images']['with_alt'])
    with col3:
        st.metric("Missing Alt Text", analysis['images']['without_alt'])

    if analysis['images']['without_alt'] > 0:
        st.warning(f"⚠️ {analysis['images']['without_alt']} images are missing alt text")
    else:
        st.success("✅ All images have alt text")

    # Links analysis
    st.markdown("### 🔗 Links")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Links", analysis['links']['total'])
    with col2:
        st.metric("Internal Links", analysis['links']['internal'])
    with col3:
        st.metric("External Links", analysis['links']['external'])

    # Content analysis
    st.markdown("### 📊 Content")
    st.metric("Word Count", analysis['word_count'])

    if analysis['word_count'] < 300:
        st.warning("⚠️ Content is quite short. Consider adding more valuable content.")
    elif analysis['word_count'] > 2000:
        st.info("ℹ️ Long content. Make sure it's well-structured with headings.")
    else:
        st.success("✅ Good content length")


def meta_tag_checker():
    """Check meta tags"""
    create_tool_header("Meta Tag Checker", "Check and validate meta tags", "🏷️")

    url = st.text_input("Enter webpage URL:", placeholder="https://example.com")

    if url and st.button("Check Meta Tags"):
        if url.startswith(('http://', 'https://')):
            meta_tags = check_meta_tags(url)
            display_meta_tags(meta_tags)
        else:
            st.error("Please enter a valid URL starting with http:// or https://")


def check_meta_tags(url):
    """Check meta tags of a webpage"""
    try:
        response = requests.get(url, timeout=30)
        html = response.text

        meta_tags = {
            'title': extract_title(html),
            'description': extract_meta_description(html),
            'keywords': extract_meta_keywords(html),
            'og_tags': extract_og_tags(html),
            'twitter_tags': extract_twitter_tags(html),
            'success': True
        }

        return meta_tags
    except Exception as e:
        return {'error': str(e), 'success': False}


def extract_meta_keywords(html):
    """Extract meta keywords"""
    match = re.search(r'<meta[^>]*name=["\']keywords["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    return match.group(1).strip() if match else None


def extract_og_tags(html):
    """Extract Open Graph tags"""
    og_tags = {}
    og_pattern = r'<meta[^>]*property=["\']og:([^"\']*)["\'][^>]*content=["\']([^"\']*)["\']'
    matches = re.findall(og_pattern, html, re.IGNORECASE)

    for prop, content in matches:
        og_tags[prop] = content

    return og_tags


def extract_twitter_tags(html):
    """Extract Twitter Card tags"""
    twitter_tags = {}
    twitter_pattern = r'<meta[^>]*name=["\']twitter:([^"\']*)["\'][^>]*content=["\']([^"\']*)["\']'
    matches = re.findall(twitter_pattern, html, re.IGNORECASE)

    for prop, content in matches:
        twitter_tags[prop] = content

    return twitter_tags


def display_meta_tags(meta_tags):
    """Display meta tags analysis"""
    if not meta_tags['success']:
        st.error(f"❌ Failed to check meta tags: {meta_tags['error']}")
        return

    # Basic meta tags
    st.markdown("### 📝 Basic Meta Tags")

    if meta_tags['title']:
        st.success(f"✅ Title: {meta_tags['title']}")
    else:
        st.error("❌ Title tag missing")

    if meta_tags['description']:
        st.success(f"✅ Description: {meta_tags['description']}")
    else:
        st.error("❌ Meta description missing")

    if meta_tags['keywords']:
        st.info(f"ℹ️ Keywords: {meta_tags['keywords']}")
    else:
        st.warning("⚠️ Meta keywords not found (not critical)")

    # Open Graph tags
    st.markdown("### 📱 Open Graph Tags")
    if meta_tags['og_tags']:
        for prop, content in meta_tags['og_tags'].items():
            st.write(f"**og:{prop}:** {content}")
    else:
        st.warning("⚠️ No Open Graph tags found")

    # Twitter tags
    st.markdown("### 🐦 Twitter Card Tags")
    if meta_tags['twitter_tags']:
        for prop, content in meta_tags['twitter_tags'].items():
            st.write(f"**twitter:{prop}:** {content}")
    else:
        st.warning("⚠️ No Twitter Card tags found")


def keyword_density():
    """Calculate keyword density"""
    create_tool_header("Keyword Density Analyzer", "Analyze keyword density in your content", "🔍")

    uploaded_file = FileHandler.upload_files(['txt', 'html'], accept_multiple=False)

    if uploaded_file:
        content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Content:", content[:500] + "...", height=100, disabled=True)
    else:
        content = st.text_area("Enter content to analyze:", height=200)

    if content and st.button("Analyze Keyword Density"):
        density = calculate_keyword_density(content)
        display_keyword_density(density)


def calculate_keyword_density(content):
    """Calculate keyword density"""
    # Remove HTML tags if present
    text = re.sub(r'<[^>]+>', '', content)

    # Convert to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)

    # Count word frequency
    word_count = {}
    for word in words:
        if len(word) > 2:  # Ignore very short words
            word_count[word] = word_count.get(word, 0) + 1

    # Calculate density percentages
    density = {}
    for word, count in word_count.items():
        density[word] = {
            'count': count,
            'density': (count / total_words) * 100
        }

    # Sort by density
    sorted_density = dict(sorted(density.items(), key=lambda x: x[1]['density'], reverse=True))

    return {
        'total_words': total_words,
        'unique_words': len(word_count),
        'density': sorted_density
    }


def display_keyword_density(density):
    """Display keyword density results"""
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Words", density['total_words'])

    with col2:
        st.metric("Unique Words", density['unique_words'])

    st.markdown("### 📊 Top Keywords by Density")

    # Show top 20 keywords
    top_keywords = list(density['density'].items())[:20]

    for word, stats in top_keywords:
        col1, col2, col3 = st.columns([3, 1, 1])

        with col1:
            st.write(word)
        with col2:
            st.write(f"{stats['count']} times")
        with col3:
            st.write(f"{stats['density']:.2f}%")


def utm_builder():
    """Build UTM parameters"""
    create_tool_header("UTM Builder", "Create trackable campaign URLs", "📊")

    base_url = st.text_input("Website URL:", placeholder="https://example.com/page")
    source = st.text_input("Campaign Source:", placeholder="google, newsletter, social")
    medium = st.text_input("Campaign Medium:", placeholder="cpc, email, social")
    campaign = st.text_input("Campaign Name:", placeholder="spring_sale, product_launch")

    st.markdown("### Optional Parameters")
    term = st.text_input("Campaign Term (keywords):", placeholder="running shoes")
    content = st.text_input("Campaign Content:", placeholder="banner_ad, text_link")

    if base_url and source and medium and campaign:
        utm_url = build_utm_url(base_url, source, medium, campaign, term, content)

        st.markdown("### 🔗 Generated UTM URL")
        st.code(utm_url)

        # QR Code option
        if st.button("Generate QR Code"):
            import qrcode
            from io import BytesIO

            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(utm_url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Convert to bytes
            img_buffer = BytesIO()
            img.save(img_buffer, format='PNG')
            img_bytes = img_buffer.getvalue()

            st.image(img_bytes, caption="QR Code for UTM URL")
            FileHandler.create_download_link(img_bytes, "utm_qr_code.png", "image/png")


def build_utm_url(base_url, source, medium, campaign, term="", content=""):
    """Build UTM URL with parameters"""
    from urllib.parse import quote

    # Ensure base URL has proper format
    if not base_url.startswith(('http://', 'https://')):
        base_url = 'https://' + base_url

    # Build UTM parameters
    params = [
        f"utm_source={quote(source)}",
        f"utm_medium={quote(medium)}",
        f"utm_campaign={quote(campaign)}"
    ]

    if term:
        params.append(f"utm_term={quote(term)}")

    if content:
        params.append(f"utm_content={quote(content)}")

    # Add parameters to URL
    separator = "&" if "?" in base_url else "?"
    utm_url = base_url + separator + "&".join(params)

    return utm_url


def hashtag_generator():
    """Generate hashtags for social media"""
    create_tool_header("Hashtag Generator", "Generate relevant hashtags for social media", "#️⃣")

    topic = st.text_input("Enter topic or keywords:", placeholder="fitness, workout, health")
    platform = st.selectbox("Social Media Platform:", ["Instagram", "Twitter", "LinkedIn", "TikTok"])

    if topic and st.button("Generate Hashtags"):
        hashtags = generate_hashtags(topic, platform)
        display_hashtags(hashtags, platform)


def generate_hashtags(topic, platform):
    """Generate hashtags based on topic and platform"""
    # Basic hashtag generation (in a real app, you might use an API)
    keywords = [word.strip().lower() for word in topic.split(',')]

    base_hashtags = []
    for keyword in keywords:
        base_hashtags.extend([
            f"#{keyword}",
            f"#{keyword}life",
            f"#{keyword}community",
            f"#{keyword}lover",
            f"#{keyword}daily"
        ])

    # Platform-specific hashtags
    platform_hashtags = {
        "Instagram": ["#instagood", "#photooftheday", "#instadaily", "#like4like", "#followme"],
        "Twitter": ["#trending", "#follow", "#retweet", "#engage", "#discussion"],
        "LinkedIn": ["#professional", "#networking", "#career", "#business", "#industry"],
        "TikTok": ["#fyp", "#viral", "#trending", "#foryou", "#tiktok"]
    }

    # Combine hashtags
    all_hashtags = base_hashtags + platform_hashtags.get(platform, [])

    return list(set(all_hashtags))  # Remove duplicates


def display_hashtags(hashtags, platform):
    """Display generated hashtags"""
    st.markdown(f"### #{platform} Hashtags")

    # Character limits by platform
    limits = {
        "Instagram": 30,
        "Twitter": 2,
        "LinkedIn": 3,
        "TikTok": 20
    }

    limit = limits.get(platform, 10)
    selected_hashtags = hashtags[:limit]

    # Display hashtags
    hashtag_text = " ".join(selected_hashtags)
    st.code(hashtag_text)

    # Copy button simulation
    st.success(f"✅ Generated {len(selected_hashtags)} hashtags")
    st.info(f"ℹ️ Recommended limit for {platform}: {limit} hashtags")

    # Show all hashtags in expandable section
    with st.expander("View All Generated Hashtags"):
        for hashtag in hashtags:
            st.write(hashtag)


def subject_line_tester():
    """Test email subject lines"""
    create_tool_header("Subject Line Tester", "Test and optimize email subject lines", "📧")

    subject_line = st.text_input("Enter subject line:", placeholder="Don't miss out on our amazing sale!")

    if subject_line and st.button("Test Subject Line"):
        analysis = analyze_subject_line(subject_line)
        display_subject_analysis(analysis)


def analyze_subject_line(subject_line):
    """Analyze email subject line"""
    length = len(subject_line)
    word_count = len(subject_line.split())

    # Check for spam words
    spam_words = ['free', 'urgent', 'limited time', 'act now', 'buy now', 'click here']
    spam_score = sum(1 for word in spam_words if word.lower() in subject_line.lower())

    # Check for personalization
    personalization = any(word in subject_line.lower() for word in ['you', 'your', 'name'])

    # Check for emojis
    emoji_count = len(re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF]', subject_line))

    # Check for urgency words
    urgency_words = ['urgent', 'hurry', 'fast', 'quick', 'limited', 'expires', 'deadline']
    urgency_score = sum(1 for word in urgency_words if word.lower() in subject_line.lower())

    return {
        'length': length,
        'word_count': word_count,
        'spam_score': spam_score,
        'personalization': personalization,
        'emoji_count': emoji_count,
        'urgency_score': urgency_score
    }


def display_subject_analysis(analysis):
    """Display subject line analysis"""
    # Length analysis
    st.markdown("### 📏 Length Analysis")
    col1, col2 = st.columns(2)

    with col1:
        if 30 <= analysis['length'] <= 50:
            st.success(f"✅ Character count: {analysis['length']} (optimal)")
        elif analysis['length'] < 30:
            st.warning(f"⚠️ Character count: {analysis['length']} (too short)")
        else:
            st.error(f"❌ Character count: {analysis['length']} (too long)")

    with col2:
        if 3 <= analysis['word_count'] <= 7:
            st.success(f"✅ Word count: {analysis['word_count']} (optimal)")
        else:
            st.warning(f"⚠️ Word count: {analysis['word_count']}")

    # Spam analysis
    st.markdown("### 🚫 Spam Risk")
    if analysis['spam_score'] == 0:
        st.success("✅ Low spam risk")
    elif analysis['spam_score'] <= 2:
        st.warning(f"⚠️ Medium spam risk ({analysis['spam_score']} spam words)")
    else:
        st.error(f"❌ High spam risk ({analysis['spam_score']} spam words)")

    # Other factors
    st.markdown("### 📊 Other Factors")

    if analysis['personalization']:
        st.success("✅ Contains personalization")
    else:
        st.info("ℹ️ Consider adding personalization (you, your)")

    if analysis['emoji_count'] > 0:
        st.info(f"📱 Contains {analysis['emoji_count']} emoji(s)")

    if analysis['urgency_score'] > 0:
        st.warning(f"⏰ Contains urgency words ({analysis['urgency_score']})")


def robots_txt_generator():
    """Generate robots.txt file"""
    create_tool_header("Robots.txt Generator", "Generate robots.txt file for your website", "🤖")

    st.markdown("### User-Agent Rules")

    user_agent = st.selectbox("User-Agent:", ["*", "Googlebot", "Bingbot", "Custom"])
    if user_agent == "Custom":
        user_agent = st.text_input("Custom User-Agent:")

    disallow_paths = st.text_area("Disallow paths (one per line):", placeholder="/admin/\n/private/\n/temp/")
    allow_paths = st.text_area("Allow paths (one per line):", placeholder="/public/\n/images/")

    sitemap_url = st.text_input("Sitemap URL:", placeholder="https://example.com/sitemap.xml")

    if st.button("Generate robots.txt"):
        robots_content = generate_robots_txt(user_agent, disallow_paths, allow_paths, sitemap_url)

        st.markdown("### 📄 Generated robots.txt")
        st.code(robots_content)
        FileHandler.create_download_link(robots_content.encode(), "robots.txt", "text/plain")


def generate_robots_txt(user_agent, disallow_paths, allow_paths, sitemap_url):
    """Generate robots.txt content"""
    lines = [f"User-agent: {user_agent}"]

    # Add disallow rules
    if disallow_paths:
        for path in disallow_paths.strip().split('\n'):
            if path.strip():
                lines.append(f"Disallow: {path.strip()}")

    # Add allow rules
    if allow_paths:
        for path in allow_paths.strip().split('\n'):
            if path.strip():
                lines.append(f"Allow: {path.strip()}")

    # Add empty line
    lines.append("")

    # Add sitemap
    if sitemap_url:
        lines.append(f"Sitemap: {sitemap_url}")

    return '\n'.join(lines)


def schema_markup_generator():
    """Generate Schema.org markup"""
    create_tool_header("Schema Markup Generator", "Generate structured data markup", "🏗️")

    schema_type = st.selectbox("Schema Type:", [
        "Organization", "Person", "LocalBusiness", "Product", "Article", "Event"
    ])

    if schema_type == "Organization":
        generate_organization_schema()
    elif schema_type == "Person":
        generate_person_schema()
    elif schema_type == "LocalBusiness":
        generate_local_business_schema()
    elif schema_type == "Product":
        generate_product_schema()
    elif schema_type == "Article":
        generate_article_schema()
    elif schema_type == "Event":
        generate_event_schema()


def generate_organization_schema():
    """Generate Organization schema"""
    name = st.text_input("Organization Name:", placeholder="Your Company")
    url = st.text_input("Website URL:", placeholder="https://yourcompany.com")
    logo = st.text_input("Logo URL:", placeholder="https://yourcompany.com/logo.png")
    description = st.text_area("Description:", placeholder="Company description")

    if name and st.button("Generate Schema"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": name,
            "url": url,
            "logo": logo,
            "description": description
        }

        schema_json = json.dumps(schema, indent=2)
        st.code(schema_json, language='json')
        FileHandler.create_download_link(schema_json.encode(), "organization_schema.json", "application/json")


def generate_person_schema():
    """Generate Person schema"""
    name = st.text_input("Full Name:", placeholder="John Doe")
    job_title = st.text_input("Job Title:", placeholder="Software Engineer")
    company = st.text_input("Company:", placeholder="Tech Company")
    email = st.text_input("Email:", placeholder="john@example.com")

    if name and st.button("Generate Schema"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": name,
            "jobTitle": job_title,
            "worksFor": {
                "@type": "Organization",
                "name": company
            },
            "email": email
        }

        schema_json = json.dumps(schema, indent=2)
        st.code(schema_json, language='json')
        FileHandler.create_download_link(schema_json.encode(), "person_schema.json", "application/json")


def generate_local_business_schema():
    """Generate LocalBusiness schema"""
    st.info("LocalBusiness schema generation - implement based on needs")


def generate_product_schema():
    """Generate Product schema"""
    st.info("Product schema generation - implement based on needs")


def generate_article_schema():
    """Generate Article schema"""
    st.info("Article schema generation - implement based on needs")


def generate_event_schema():
    """Generate Event schema"""
    st.info("Event schema generation - implement based on needs")


def ab_test_calculator():
    """Calculate A/B test significance"""
    create_tool_header("A/B Test Calculator", "Calculate statistical significance of A/B tests", "📊")

    st.markdown("### Control Group (A)")
    visitors_a = st.number_input("Visitors:", min_value=1, value=1000, key="visitors_a")
    conversions_a = st.number_input("Conversions:", min_value=0, value=50, key="conversions_a")

    st.markdown("### Variant Group (B)")
    visitors_b = st.number_input("Visitors:", min_value=1, value=1000, key="visitors_b")
    conversions_b = st.number_input("Conversions:", min_value=0, value=60, key="conversions_b")

    if st.button("Calculate Results"):
        results = calculate_ab_test(visitors_a, conversions_a, visitors_b, conversions_b)
        display_ab_results(results)


def calculate_ab_test(visitors_a, conversions_a, visitors_b, conversions_b):
    """Calculate A/B test results"""
    import math

    # Conversion rates
    cr_a = conversions_a / visitors_a
    cr_b = conversions_b / visitors_b

    # Improvement
    improvement = ((cr_b - cr_a) / cr_a) * 100 if cr_a > 0 else 0

    # Standard error
    se_a = math.sqrt((cr_a * (1 - cr_a)) / visitors_a)
    se_b = math.sqrt((cr_b * (1 - cr_b)) / visitors_b)
    se_diff = math.sqrt(se_a ** 2 + se_b ** 2)

    # Z-score
    z_score = (cr_b - cr_a) / se_diff if se_diff > 0 else 0

    # Statistical significance (approximation)
    significant = abs(z_score) > 1.96  # 95% confidence

    return {
        'cr_a': cr_a,
        'cr_b': cr_b,
        'improvement': improvement,
        'z_score': z_score,
        'significant': significant
    }


def display_ab_results(results):
    """Display A/B test results"""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Control Rate", f"{results['cr_a']:.2%}")

    with col2:
        st.metric("Variant Rate", f"{results['cr_b']:.2%}")

    with col3:
        improvement_color = "normal" if results['improvement'] >= 0 else "inverse"
        st.metric("Improvement", f"{results['improvement']:.2f}%")

    st.markdown("### 📊 Statistical Significance")

    if results['significant']:
        st.success(f"✅ Statistically significant (Z-score: {results['z_score']:.2f})")
        if results['improvement'] > 0:
            st.success("🎉 Variant B is performing better!")
        else:
            st.error("📉 Variant B is performing worse")
    else:
        st.warning(f"⚠️ Not statistically significant (Z-score: {results['z_score']:.2f})")
        st.info("Consider running the test longer or increasing sample size")


def heading_structure():
    """Analyze heading structure of a webpage"""
    create_tool_header("Heading Structure Analyzer", "Analyze the heading hierarchy and structure", "🔢")

    url = st.text_input("Enter webpage URL:", placeholder="https://example.com/page")

    if url and st.button("Analyze Heading Structure"):
        if url.startswith(('http://', 'https://')):
            with st.spinner("Analyzing heading structure..."):
                headings_analysis = analyze_heading_structure(url)
                display_heading_structure(headings_analysis)
        else:
            st.error("Please enter a valid URL starting with http:// or https://")


def analyze_heading_structure(url):
    """Analyze heading structure of webpage"""
    try:
        response = requests.get(url, timeout=30)
        html_content = response.text

        # Extract all headings with their positions
        headings = []
        for level in range(1, 7):
            pattern = f'<h{level}[^>]*>(.*?)</h{level}>'
            matches = re.finditer(pattern, html_content, re.IGNORECASE | re.DOTALL)
            for match in matches:
                text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
                headings.append({
                    'level': level,
                    'text': text,
                    'position': match.start()
                })

        # Sort by position to maintain document order
        headings.sort(key=lambda x: x['position'])

        # Analyze structure issues
        issues = analyze_heading_issues(headings)

        return {
            'headings': headings,
            'issues': issues,
            'success': True
        }
    except Exception as e:
        return {'error': str(e), 'success': False}


def analyze_heading_issues(headings):
    """Analyze heading structure for SEO issues"""
    issues = []

    if not headings:
        issues.append("No headings found on the page")
        return issues

    # Check if first heading is H1
    if headings[0]['level'] != 1:
        issues.append("Page doesn't start with an H1 tag")

    # Check for multiple H1s
    h1_count = sum(1 for h in headings if h['level'] == 1)
    if h1_count > 1:
        issues.append(f"Multiple H1 tags found ({h1_count}). Should have only one H1.")
    elif h1_count == 0:
        issues.append("No H1 tag found. Every page should have exactly one H1.")

    # Check for skipped heading levels
    for i in range(1, len(headings)):
        current_level = headings[i]['level']
        prev_level = headings[i - 1]['level']

        if current_level > prev_level + 1:
            issues.append(f"Skipped heading level: H{prev_level} followed by H{current_level}")

    # Check for empty headings
    empty_headings = [h for h in headings if not h['text'].strip()]
    if empty_headings:
        issues.append(f"{len(empty_headings)} empty heading(s) found")

    return issues


def display_heading_structure(analysis):
    """Display heading structure analysis"""
    if not analysis['success']:
        st.error(f"❌ Analysis failed: {analysis['error']}")
        return

    headings = analysis['headings']
    issues = analysis['issues']

    # Overview metrics
    st.markdown("### 📊 Heading Overview")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Headings", len(headings))

    with col2:
        h1_count = sum(1 for h in headings if h['level'] == 1)
        st.metric("H1 Tags", h1_count)

    with col3:
        max_level = max([h['level'] for h in headings]) if headings else 0
        st.metric("Deepest Level", f"H{max_level}")

    # Issues
    st.markdown("### ⚠️ Structure Issues")
    if issues:
        for issue in issues:
            st.error(f"❌ {issue}")
    else:
        st.success("✅ No structural issues found!")

    # Heading hierarchy
    st.markdown("### 🔢 Heading Hierarchy")
    if headings:
        for heading in headings:
            indent = "  " * (heading['level'] - 1)
            level_color = {1: "🔴", 2: "🟠", 3: "🟡", 4: "🟢", 5: "🔵", 6: "🟣"}
            color = level_color.get(heading['level'], "⚪")
            st.write(
                f"{indent}{color} H{heading['level']}: {heading['text'][:100]}{'...' if len(heading['text']) > 100 else ''}")
    else:
        st.info("No headings found on this page")

    # Level distribution
    st.markdown("### 📈 Level Distribution")
    level_counts = {}
    for heading in headings:
        level = f"H{heading['level']}"
        level_counts[level] = level_counts.get(level, 0) + 1

    if level_counts:
        for level, count in sorted(level_counts.items()):
            st.write(f"**{level}:** {count} occurrences")


def internal_link_checker():
    """Check internal links on a webpage"""
    create_tool_header("Internal Link Checker", "Check and validate internal links", "🔗")

    url = st.text_input("Enter webpage URL:", placeholder="https://example.com/page")

    if url and st.button("Check Internal Links"):
        if url.startswith(('http://', 'https://')):
            with st.spinner("Checking internal links..."):
                link_analysis = check_internal_links(url)
                display_link_analysis(link_analysis)
        else:
            st.error("Please enter a valid URL starting with http:// or https://")


def check_internal_links(url):
    """Check internal links on webpage"""
    try:
        response = requests.get(url, timeout=30)
        html_content = response.text
        base_domain = urlparse(url).netloc

        # Extract all links
        link_pattern = r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>'
        links = re.findall(link_pattern, html_content, re.IGNORECASE | re.DOTALL)

        internal_links = []
        for href, anchor_text in links:
            # Clean anchor text
            anchor_text = re.sub(r'<[^>]+>', '', anchor_text).strip()

            # Check if it's an internal link
            if href.startswith('/'):
                # Relative URL
                full_url = urljoin(url, href)
                internal_links.append({
                    'url': full_url,
                    'href': href,
                    'anchor_text': anchor_text,
                    'type': 'relative'
                })
            elif href.startswith(('http://', 'https://')):
                # Absolute URL
                link_domain = urlparse(href).netloc
                if link_domain == base_domain:
                    internal_links.append({
                        'url': href,
                        'href': href,
                        'anchor_text': anchor_text,
                        'type': 'absolute'
                    })

        # Check link status (sample first 10 to avoid overloading)
        checked_links = []
        for link in internal_links[:10]:
            try:
                link_response = requests.head(link['url'], timeout=10, allow_redirects=True)
                status = link_response.status_code
                link['status'] = status
                link['status_text'] = 'Working' if status < 400 else 'Broken'
            except:
                link['status'] = 0
                link['status_text'] = 'Error'
            checked_links.append(link)

        # Add unchecked links
        if len(internal_links) > 10:
            for link in internal_links[10:]:
                link['status'] = None
                link['status_text'] = 'Not checked'
                checked_links.append(link)

        return {
            'links': checked_links,
            'total_internal': len(internal_links),
            'checked_count': min(10, len(internal_links)),
            'success': True
        }
    except Exception as e:
        return {'error': str(e), 'success': False}


def display_link_analysis(analysis):
    """Display internal link analysis"""
    if not analysis['success']:
        st.error(f"❌ Analysis failed: {analysis['error']}")
        return

    links = analysis['links']

    # Overview
    st.markdown("### 📊 Internal Links Overview")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Internal Links", analysis['total_internal'])

    with col2:
        working_links = sum(1 for link in links if link.get('status_text') == 'Working')
        st.metric("Working Links", working_links)

    with col3:
        broken_links = sum(1 for link in links if link.get('status_text') == 'Broken')
        st.metric("Broken Links", broken_links)

    if analysis['checked_count'] < analysis['total_internal']:
        st.info(f"ℹ️ Status checked for first {analysis['checked_count']} links only")

    # Link details
    st.markdown("### 🔗 Link Details")

    if links:
        for i, link in enumerate(links, 1):
            with st.expander(f"Link {i}: {link['anchor_text'][:50]}{'...' if len(link['anchor_text']) > 50 else ''}"):
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**URL:** {link['url']}")
                    st.write(f"**Anchor Text:** {link['anchor_text']}")
                    st.write(f"**Type:** {link['type']}")

                with col2:
                    if link.get('status'):
                        if link['status_text'] == 'Working':
                            st.success(f"✅ {link['status_text']} ({link['status']})")
                        elif link['status_text'] == 'Broken':
                            st.error(f"❌ {link['status_text']} ({link['status']})")
                        else:
                            st.warning(f"⚠️ {link['status_text']}")
                    else:
                        st.info("ℹ️ Status not checked")
    else:
        st.info("No internal links found on this page")


def content_planner():
    """Content planning and strategy tool"""
    create_tool_header("Content Planner", "Plan your content strategy and goals", "📋")

    st.markdown("### Content Strategy Planning")

    # Business information
    st.markdown("#### Business Details")
    business_type = st.selectbox("Business Type:",
                                 ["E-commerce", "SaaS", "Blog/Media", "Service Business", "Local Business",
                                  "Non-profit", "Other"])
    target_audience = st.text_input("Target Audience:", placeholder="Young professionals, small business owners, etc.")
    business_goals = st.multiselect("Content Goals:",
                                    ["Brand Awareness", "Lead Generation", "Sales", "Customer Education",
                                     "Community Building", "SEO Traffic"])

    # Content preferences
    st.markdown("#### Content Preferences")
    content_types = st.multiselect("Content Types:",
                                   ["Blog Posts", "Social Media Posts", "Videos", "Podcasts", "Infographics",
                                    "Email Newsletters", "Case Studies", "White Papers"])
    posting_frequency = st.selectbox("Desired Posting Frequency:",
                                     ["Daily", "3-4 times/week", "2-3 times/week", "Weekly", "Bi-weekly", "Monthly"])
    content_pillars = st.text_area("Content Pillars/Themes:",
                                   placeholder="Educational content, industry news, product updates, customer stories...")

    if st.button("Generate Content Plan"):
        if target_audience and business_goals and content_types:
            plan = generate_content_plan(business_type, target_audience, business_goals, content_types,
                                         posting_frequency, content_pillars)
            display_content_plan(plan)
        else:
            st.error("Please fill in the required fields: Target Audience, Content Goals, and Content Types")


def generate_content_plan(business_type, target_audience, goals, content_types, frequency, pillars):
    """Generate a content strategy plan"""
    plan = {
        'strategy_overview': f"Content strategy for {business_type} targeting {target_audience}",
        'goals': goals,
        'content_mix': {},
        'content_calendar_template': [],
        'kpis': []
    }

    # Content mix recommendations
    if "Blog Posts" in content_types:
        plan['content_mix'][
            'Blog Posts'] = "2-3 educational posts per week focusing on industry insights and how-to guides"
    if "Social Media Posts" in content_types:
        plan['content_mix'][
            'Social Media Posts'] = "Daily engagement with mix of educational, promotional, and community content"
    if "Videos" in content_types:
        plan['content_mix'][
            'Videos'] = "Weekly video content including tutorials, behind-the-scenes, and customer testimonials"
    if "Email Newsletters" in content_types:
        plan['content_mix']['Email Newsletters'] = "Weekly newsletter with curated content and exclusive insights"

    # Sample content calendar
    content_ideas = [
        "Industry trend analysis",
        "How-to tutorial",
        "Customer success story",
        "Behind-the-scenes content",
        "Product/service spotlight",
        "Expert interview",
        "FAQ post",
        "Seasonal/timely content"
    ]

    for i, idea in enumerate(content_ideas[:4]):
        plan['content_calendar_template'].append({
            'week': i + 1,
            'content_idea': idea,
            'content_type': content_types[0] if content_types else "Blog Post",
            'goal': goals[0] if goals else "Brand Awareness"
        })

    # KPIs based on goals
    if "Brand Awareness" in goals:
        plan['kpis'].extend(["Reach", "Impressions", "Social Media Followers"])
    if "Lead Generation" in goals:
        plan['kpis'].extend(["Email Signups", "Download Conversions", "Contact Form Submissions"])
    if "Sales" in goals:
        plan['kpis'].extend(["Conversion Rate", "Revenue Attribution", "Sales Qualified Leads"])
    if "SEO Traffic" in goals:
        plan['kpis'].extend(["Organic Traffic", "Keyword Rankings", "Backlinks"])

    return plan


def display_content_plan(plan):
    """Display the generated content plan"""
    st.markdown("### 📊 Your Content Strategy Plan")

    # Strategy Overview
    st.markdown("#### Strategy Overview")
    st.write(plan['strategy_overview'])

    # Goals
    st.markdown("#### Content Goals")
    for goal in plan['goals']:
        st.write(f"• {goal}")

    # Content Mix
    st.markdown("#### Recommended Content Mix")
    for content_type, recommendation in plan['content_mix'].items():
        st.write(f"**{content_type}:** {recommendation}")

    # Sample Calendar
    st.markdown("#### Sample 4-Week Content Calendar")
    for item in plan['content_calendar_template']:
        with st.expander(f"Week {item['week']}: {item['content_idea']}"):
            st.write(f"**Content Type:** {item['content_type']}")
            st.write(f"**Primary Goal:** {item['goal']}")

    # KPIs
    st.markdown("#### Key Performance Indicators (KPIs)")
    kpi_cols = st.columns(3)
    for i, kpi in enumerate(plan['kpis']):
        with kpi_cols[i % 3]:
            st.metric(kpi, "Track")


def keyword_research():
    """Keyword research tool"""
    create_tool_header("Keyword Research", "Research keywords for your content", "🔍")

    seed_keyword = st.text_input("Enter seed keyword:", placeholder="digital marketing")
    industry = st.selectbox("Industry/Niche:",
                            ["Technology", "Health & Fitness", "Finance", "Education", "E-commerce", "Real Estate",
                             "Food & Beverage", "Travel", "Other"])

    if seed_keyword and st.button("Research Keywords"):
        keywords = generate_keyword_suggestions(seed_keyword, industry)
        display_keyword_research(keywords, seed_keyword)


def generate_keyword_suggestions(seed_keyword, industry):
    """Generate keyword suggestions"""
    # In a real application, you would use APIs like Google Keyword Planner, SEMrush, etc.
    base_keywords = seed_keyword.lower().split()

    keyword_variations = []

    # Long-tail variations
    modifiers = ["how to", "best", "top", "guide", "tips", "strategy", "tools", "services", "examples", "benefits"]
    for modifier in modifiers:
        keyword_variations.append({
            'keyword': f"{modifier} {seed_keyword}",
            'search_volume': "1K-10K",
            'difficulty': "Medium",
            'intent': "Informational"
        })

    # Question-based keywords
    question_words = ["what is", "how to", "why", "when", "where"]
    for question in question_words:
        keyword_variations.append({
            'keyword': f"{question} {seed_keyword}",
            'search_volume': "100-1K",
            'difficulty': "Low",
            'intent': "Informational"
        })

    # Commercial keywords
    commercial_modifiers = ["buy", "price", "cost", "review", "comparison", "vs"]
    for modifier in commercial_modifiers:
        keyword_variations.append({
            'keyword': f"{seed_keyword} {modifier}",
            'search_volume': "500-5K",
            'difficulty': "High",
            'intent': "Commercial"
        })

    return keyword_variations[:15]  # Return top 15 suggestions


def display_keyword_research(keywords, seed_keyword):
    """Display keyword research results"""
    st.markdown(f"### 🎯 Keyword Suggestions for '{seed_keyword}'")

    # Group by intent
    informational = [k for k in keywords if k['intent'] == 'Informational']
    commercial = [k for k in keywords if k['intent'] == 'Commercial']

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📚 Informational Keywords")
        for keyword in informational:
            with st.expander(keyword['keyword']):
                st.write(f"**Search Volume:** {keyword['search_volume']}")
                st.write(f"**Difficulty:** {keyword['difficulty']}")
                st.write(f"**Intent:** {keyword['intent']}")

    with col2:
        st.markdown("#### 💰 Commercial Keywords")
        for keyword in commercial:
            with st.expander(keyword['keyword']):
                st.write(f"**Search Volume:** {keyword['search_volume']}")
                st.write(f"**Difficulty:** {keyword['difficulty']}")
                st.write(f"**Intent:** {keyword['intent']}")

    # Export option
    st.markdown("### 📥 Export Keywords")
    if st.button("Generate Keyword List"):
        keyword_list = "\n".join(
            [f"{k['keyword']}, {k['search_volume']}, {k['difficulty']}, {k['intent']}" for k in keywords])
        st.text_area("Copy this keyword list:", f"Keyword, Search Volume, Difficulty, Intent\n{keyword_list}",
                     height=200)


def competitor_analysis():
    """Competitor analysis tool"""
    create_tool_header("Competitor Analysis", "Analyze your competitors' content strategy", "🔍")

    st.markdown("### Competitor Research")

    competitor_url = st.text_input("Competitor Website URL:", placeholder="https://competitor.com")
    analysis_type = st.selectbox("Analysis Type:",
                                 ["Content Audit", "Social Media Presence", "SEO Analysis", "Content Topics"])

    if competitor_url and st.button("Analyze Competitor"):
        if competitor_url.startswith(('http://', 'https://')):
            with st.spinner("Analyzing competitor..."):
                analysis = analyze_competitor(competitor_url, analysis_type)
                display_competitor_analysis(analysis, analysis_type)
        else:
            st.error("Please enter a valid URL starting with http:// or https://")


def analyze_competitor(url, analysis_type):
    """Analyze competitor website"""
    try:
        response = requests.get(url, timeout=30)
        html_content = response.text

        analysis = {
            'domain': urlparse(url).netloc,
            'title': extract_title(html_content),
            'meta_description': extract_meta_description(html_content),
            'headings': extract_headings(html_content),
            'word_count': count_words(html_content),
            'social_links': extract_social_links(html_content),
            'blog_links': find_blog_section(html_content, url),
            'success': True
        }

        return analysis
    except Exception as e:
        return {'error': str(e), 'success': False}


def extract_social_links(html):
    """Extract social media links"""
    social_platforms = ['facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'tiktok']
    social_links = {}

    for platform in social_platforms:
        pattern = f'href=["\'][^"\']*{platform}[^"\']*["\']'
        matches = re.findall(pattern, html, re.IGNORECASE)
        if matches:
            social_links[platform] = True

    return social_links


def find_blog_section(html, base_url):
    """Find blog or content section"""
    blog_keywords = ['blog', 'news', 'articles', 'insights', 'resources']
    blog_links = []

    for keyword in blog_keywords:
        pattern = f'href=["\']([^"\']*{keyword}[^"\']*)["\']'
        matches = re.findall(pattern, html, re.IGNORECASE)
        for match in matches:
            if not match.startswith('http'):
                match = urljoin(base_url, match)
            blog_links.append(match)

    return blog_links[:5]  # Return first 5 blog links


def display_competitor_analysis(analysis, analysis_type):
    """Display competitor analysis results"""
    if not analysis['success']:
        st.error(f"❌ Analysis failed: {analysis['error']}")
        return

    st.markdown(f"### 📊 Analysis Results for {analysis['domain']}")

    # Basic info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Page Title Length", len(analysis['title']) if analysis['title'] else 0)
    with col2:
        st.metric("Meta Description Length", len(analysis['meta_description']) if analysis['meta_description'] else 0)
    with col3:
        st.metric("Word Count", analysis['word_count'])

    # Title and description
    if analysis['title']:
        st.markdown("#### 📝 Page Title")
        st.code(analysis['title'])

    if analysis['meta_description']:
        st.markdown("#### 📄 Meta Description")
        st.code(analysis['meta_description'])

    # Social presence
    st.markdown("#### 📱 Social Media Presence")
    if analysis['social_links']:
        for platform, present in analysis['social_links'].items():
            if present:
                st.success(f"✅ {platform.title()}")
    else:
        st.info("No social media links found")

    # Content sections
    if analysis['blog_links']:
        st.markdown("#### 📚 Content Sections Found")
        for link in analysis['blog_links']:
            st.write(f"• {link}")

    # Heading structure
    st.markdown("#### 🔢 Heading Structure")
    for heading_level, headings in analysis['headings'].items():
        if headings:
            st.write(f"**{heading_level.upper()}:** {len(headings)} found")


def content_calendar():
    """Content calendar generator"""
    create_tool_header("Content Calendar", "Create a content publishing calendar", "📅")

    st.markdown("### Content Calendar Generator")

    # Calendar settings
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
        content_types = st.multiselect("Content Types:",
                                       ["Blog Post", "Social Media", "Video", "Email Newsletter", "Infographic",
                                        "Podcast"])

    with col2:
        duration_weeks = st.slider("Calendar Duration (weeks)", 1, 12, 4)
        posting_frequency = st.selectbox("Posting Frequency:",
                                         ["Daily", "3x per week", "2x per week", "Weekly", "Bi-weekly"])

    content_themes = st.text_area("Content Themes/Topics:",
                                  placeholder="Educational content, product updates, industry news, customer stories...")

    if st.button("Generate Calendar"):
        if content_types and content_themes:
            calendar = generate_content_calendar(start_date, duration_weeks, content_types, posting_frequency,
                                                 content_themes)
            display_content_calendar(calendar)
        else:
            st.error("Please select content types and provide content themes")


def generate_content_calendar(start_date, duration_weeks, content_types, frequency, themes):
    """Generate content calendar"""
    import datetime

    calendar_items = []
    current_date = start_date
    theme_list = [theme.strip() for theme in themes.split(',')]

    # Determine posting schedule
    posts_per_week = {
        "Daily": 7,
        "3x per week": 3,
        "2x per week": 2,
        "Weekly": 1,
        "Bi-weekly": 0.5
    }.get(frequency, 1)

    total_posts = int(duration_weeks * posts_per_week)

    for i in range(total_posts):
        # Calculate posting date
        if frequency == "Daily":
            post_date = current_date + datetime.timedelta(days=i)
        elif frequency == "3x per week":
            week_num = i // 3
            day_in_week = [0, 2, 4][i % 3]  # Monday, Wednesday, Friday
            post_date = current_date + datetime.timedelta(weeks=week_num, days=day_in_week)
        elif frequency == "2x per week":
            week_num = i // 2
            day_in_week = [0, 3][i % 2]  # Monday, Thursday
            post_date = current_date + datetime.timedelta(weeks=week_num, days=day_in_week)
        else:  # Weekly or bi-weekly
            post_date = current_date + datetime.timedelta(weeks=i)

        # Select content type and theme
        content_type = content_types[i % len(content_types)]
        theme = theme_list[i % len(theme_list)]

        calendar_items.append({
            'date': post_date,
            'content_type': content_type,
            'theme': theme,
            'status': 'Planned'
        })

    return calendar_items


def display_content_calendar(calendar):
    """Display content calendar"""
    st.markdown("### 📅 Your Content Calendar")

    # Calendar overview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Posts", len(calendar))
    with col2:
        content_types_count = len(set(item['content_type'] for item in calendar))
        st.metric("Content Types", content_types_count)
    with col3:
        duration = (calendar[-1]['date'] - calendar[0]['date']).days + 1
        st.metric("Duration (days)", duration)

    # Calendar items
    st.markdown("#### 📋 Calendar Schedule")
    for item in calendar:
        with st.expander(f"{item['date'].strftime('%B %d, %Y')} - {item['content_type']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**Type:** {item['content_type']}")
            with col2:
                st.write(f"**Theme:** {item['theme']}")
            with col3:
                st.write(f"**Status:** {item['status']}")

    # Export option
    st.markdown("### 📥 Export Calendar")
    if st.button("Generate CSV"):
        import io
        output = io.StringIO()
        output.write("Date,Content Type,Theme,Status\n")
        for item in calendar:
            output.write(f"{item['date']},{item['content_type']},{item['theme']},{item['status']}\n")
        st.text_area("Copy this CSV data:", output.getvalue(), height=200)


def topic_generator():
    """Content topic generator"""
    create_tool_header("Topic Generator", "Generate content topic ideas", "💡")

    st.markdown("### Content Topic Generator")

    # Input parameters
    industry = st.selectbox("Industry:",
                            ["Technology", "Health & Fitness", "Finance", "Education", "E-commerce", "Real Estate",
                             "Food & Beverage", "Travel", "Marketing", "Business", "Lifestyle", "Other"])

    content_type = st.selectbox("Content Type:",
                                ["Blog Post", "Social Media Post", "Video", "Podcast", "Email Newsletter",
                                 "Infographic"])

    audience = st.selectbox("Target Audience:",
                            ["Beginners", "Intermediate", "Advanced", "Business Owners", "Professionals", "Students",
                             "General Public"])

    tone = st.selectbox("Content Tone:",
                        ["Educational", "Entertaining", "Inspirational", "Professional", "Casual", "Technical"])

    keywords = st.text_input("Keywords/Themes:", placeholder="AI, automation, productivity")

    if st.button("Generate Topics"):
        if industry and content_type:
            topics = generate_content_topics(industry, content_type, audience, tone, keywords)
            display_topic_suggestions(topics, content_type)
        else:
            st.error("Please select industry and content type")


def generate_content_topics(industry, content_type, audience, tone, keywords):
    """Generate content topic suggestions"""
    topic_templates = {
        "Blog Post": [
            "The Ultimate Guide to {keyword} for {audience}",
            "10 {keyword} Mistakes {audience} Should Avoid",
            "How to {keyword}: A Step-by-Step Guide",
            "{keyword} Trends to Watch in 2024",
            "The Future of {keyword} in {industry}",
            "Common {keyword} Myths Debunked",
            "Best {keyword} Tools for {audience}",
            "{keyword} Case Study: Real Results",
            "Beginner's Guide to {keyword}",
            "Advanced {keyword} Strategies"
        ],
        "Social Media Post": [
            "Quick tip: {keyword}",
            "Did you know? {keyword} fact",
            "{keyword} Monday motivation",
            "Behind the scenes: {keyword}",
            "This week in {keyword}",
            "{keyword} wins this week",
            "Ask me anything about {keyword}",
            "{keyword} before and after",
            "My favorite {keyword} tools",
            "{keyword} challenge"
        ],
        "Video": [
            "{keyword} Tutorial for {audience}",
            "Day in the life: {keyword}",
            "{keyword} Review and Demo",
            "React to {keyword} trends",
            "{keyword} Q&A Session",
            "How I learned {keyword}",
            "{keyword} Mistakes I Made",
            "Budget {keyword} Setup",
            "{keyword} Time-lapse",
            "Interviewing {keyword} Expert"
        ]
    }

    # Get templates for content type
    templates = topic_templates.get(content_type, topic_templates["Blog Post"])

    # Generate topics
    topics = []
    keyword_list = [kw.strip() for kw in keywords.split(',')] if keywords else [industry.lower()]

    for template in templates:
        for keyword in keyword_list:
            topic = template.replace("{keyword}", keyword).replace("{audience}", audience.lower()).replace("{industry}",
                                                                                                           industry.lower())
            topics.append({
                'title': topic,
                'content_type': content_type,
                'tone': tone,
                'audience': audience,
                'estimated_length': get_estimated_length(content_type)
            })

    return topics[:20]  # Return top 20 topics


def get_estimated_length(content_type):
    """Get estimated content length"""
    lengths = {
        "Blog Post": "1500-2500 words",
        "Social Media Post": "50-280 characters",
        "Video": "5-15 minutes",
        "Podcast": "20-60 minutes",
        "Email Newsletter": "200-500 words",
        "Infographic": "5-10 data points"
    }
    return lengths.get(content_type, "Varies")


def display_topic_suggestions(topics, content_type):
    """Display topic suggestions"""
    st.markdown(f"### 💡 {content_type} Topic Ideas")

    # Topic cards
    for i, topic in enumerate(topics, 1):
        with st.expander(f"Topic {i}: {topic['title']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Audience:** {topic['audience']}")
                st.write(f"**Tone:** {topic['tone']}")
            with col2:
                st.write(f"**Type:** {topic['content_type']}")
                st.write(f"**Length:** {topic['estimated_length']}")

    # Export topics
    st.markdown("### 📥 Export Topics")
    if st.button("Generate Topic List"):
        topic_list = "\n".join([f"{i + 1}. {topic['title']}" for i, topic in enumerate(topics)])
        st.text_area("Copy this topic list:", topic_list, height=300)


def post_scheduler():
    """Social media post scheduler"""
    create_tool_header("Post Scheduler", "Schedule and plan your social media posts", "📅")

    st.markdown("### Social Media Post Scheduler")

    # Platform selection
    platform = st.selectbox("Social Media Platform:",
                            ["Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok", "YouTube", "Pinterest"])

    # Post details
    st.markdown("#### Post Details")
    post_content = st.text_area("Post Content:", placeholder="Write your engaging post content here...")

    # Character counter
    if post_content:
        char_limits = {
            "Instagram": 2200,
            "Twitter": 280,
            "Facebook": 63206,
            "LinkedIn": 3000,
            "TikTok": 150,
            "YouTube": 5000,
            "Pinterest": 500
        }
        char_count = len(post_content)
        char_limit = char_limits.get(platform, 1000)

        if char_count <= char_limit:
            st.success(f"✅ Character count: {char_count}/{char_limit}")
        else:
            st.error(f"❌ Character count: {char_count}/{char_limit} (too long)")

    # Scheduling options
    col1, col2 = st.columns(2)
    with col1:
        schedule_date = st.date_input("Schedule Date")
        schedule_time = st.time_input("Schedule Time")

    with col2:
        frequency = st.selectbox("Posting Frequency:",
                                 ["One-time", "Daily", "Weekly", "Bi-weekly", "Monthly"])
        auto_hashtags = st.checkbox("Auto-generate hashtags")

    # Media upload simulation
    st.markdown("#### Media Attachments")
    media_type = st.selectbox("Media Type:", ["None", "Image", "Video", "Carousel", "Story"])

    if media_type != "None":
        st.info(f"📎 {media_type} attachment selected (upload functionality would be implemented)")

    # Preview and schedule
    if st.button("Preview & Schedule Post"):
        if post_content:
            preview_post(platform, post_content, schedule_date, schedule_time, media_type, auto_hashtags)
        else:
            st.error("Please enter post content")


def preview_post(platform, content, date, time, media_type, auto_hashtags):
    """Preview the scheduled post"""
    st.markdown("### 📱 Post Preview")

    # Platform-specific preview
    st.markdown(f"#### {platform} Post Preview")

    # Post content with hashtags if enabled
    preview_content = content
    if auto_hashtags:
        # Simple hashtag generation based on content
        words = content.lower().split()
        hashtags = [f"#{word}" for word in words if len(word) > 3 and word.isalpha()][:5]
        if hashtags:
            preview_content += f"\n\n{' '.join(hashtags)}"

    st.code(preview_content, language=None)

    # Scheduling info
    st.markdown("#### 📅 Scheduling Details")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**Platform:** {platform}")
    with col2:
        st.write(f"**Date:** {date}")
    with col3:
        st.write(f"**Time:** {time}")

    if media_type != "None":
        st.write(f"**Media:** {media_type}")

    st.success("✅ Post scheduled successfully!")
    st.info("💡 In a real application, this would be added to your content calendar and posted automatically")


def engagement_calculator():
    """Calculate social media engagement rates"""
    create_tool_header("Engagement Calculator", "Calculate your social media engagement rates", "📊")

    st.markdown("### Social Media Engagement Calculator")

    # Platform selection
    platform = st.selectbox("Platform:",
                            ["Instagram", "Twitter", "Facebook", "LinkedIn", "TikTok", "YouTube"])

    # Metrics input
    st.markdown("#### Engagement Metrics")
    col1, col2 = st.columns(2)

    with col1:
        followers = st.number_input("Total Followers:", min_value=0, value=1000)
        likes = st.number_input("Total Likes:", min_value=0, value=100)
        comments = st.number_input("Total Comments:", min_value=0, value=10)

    with col2:
        shares = st.number_input("Total Shares/Retweets:", min_value=0, value=5)
        saves = st.number_input("Total Saves/Bookmarks:", min_value=0, value=8)
        reach = st.number_input("Post Reach (optional):", min_value=0, value=0)

    # Time period
    time_period = st.selectbox("Time Period:",
                               ["Single Post", "Last 7 days", "Last 30 days", "Last 90 days"])

    if st.button("Calculate Engagement"):
        engagement_data = calculate_engagement_rates(platform, followers, likes, comments, shares, saves, reach,
                                                     time_period)
        display_engagement_results(engagement_data, platform)


def calculate_engagement_rates(platform, followers, likes, comments, shares, saves, reach, time_period):
    """Calculate various engagement metrics"""
    total_engagement = likes + comments + shares + saves

    # Engagement rate calculations
    engagement_rate = (total_engagement / followers * 100) if followers > 0 else 0
    reach_engagement_rate = (total_engagement / reach * 100) if reach > 0 else 0

    # Platform-specific benchmarks
    benchmarks = {
        "Instagram": {"excellent": 6, "good": 3, "average": 1},
        "Twitter": {"excellent": 3, "good": 1.5, "average": 0.5},
        "Facebook": {"excellent": 5, "good": 2.5, "average": 1},
        "LinkedIn": {"excellent": 4, "good": 2, "average": 1},
        "TikTok": {"excellent": 10, "good": 5, "average": 2},
        "YouTube": {"excellent": 8, "good": 4, "average": 2}
    }

    platform_benchmark = benchmarks.get(platform, {"excellent": 5, "good": 2.5, "average": 1})

    # Performance assessment
    if engagement_rate >= platform_benchmark["excellent"]:
        performance = "Excellent"
        performance_color = "success"
    elif engagement_rate >= platform_benchmark["good"]:
        performance = "Good"
        performance_color = "success"
    elif engagement_rate >= platform_benchmark["average"]:
        performance = "Average"
        performance_color = "warning"
    else:
        performance = "Below Average"
        performance_color = "error"

    return {
        'total_engagement': total_engagement,
        'engagement_rate': engagement_rate,
        'reach_engagement_rate': reach_engagement_rate,
        'performance': performance,
        'performance_color': performance_color,
        'platform_benchmark': platform_benchmark,
        'breakdown': {
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'saves': saves
        }
    }


def display_engagement_results(data, platform):
    """Display engagement calculation results"""
    st.markdown("### 📊 Engagement Analysis Results")

    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Engagement", data['total_engagement'])
    with col2:
        st.metric("Engagement Rate", f"{data['engagement_rate']:.2f}%")
    with col3:
        if data['reach_engagement_rate'] > 0:
            st.metric("Reach Engagement Rate", f"{data['reach_engagement_rate']:.2f}%")
        else:
            st.metric("Performance", data['performance'])

    # Performance assessment
    st.markdown("### 🎯 Performance Assessment")
    if data['performance_color'] == "success":
        st.success(f"✅ {data['performance']} engagement rate for {platform}")
    elif data['performance_color'] == "warning":
        st.warning(f"⚠️ {data['performance']} engagement rate for {platform}")
    else:
        st.error(f"❌ {data['performance']} engagement rate for {platform}")

    # Benchmarks
    st.markdown(f"### 📈 {platform} Benchmarks")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Excellent", f"{data['platform_benchmark']['excellent']}%+")
    with col2:
        st.metric("Good", f"{data['platform_benchmark']['good']}%+")
    with col3:
        st.metric("Average", f"{data['platform_benchmark']['average']}%+")

    # Engagement breakdown
    st.markdown("### 📋 Engagement Breakdown")
    breakdown = data['breakdown']
    total = sum(breakdown.values())

    if total > 0:
        for metric, value in breakdown.items():
            percentage = (value / total * 100) if total > 0 else 0
            st.write(f"**{metric.title()}:** {value} ({percentage:.1f}%)")


def handle_checker():
    """Check social media handle availability"""
    create_tool_header("Handle Checker", "Check username availability across platforms", "🔍")

    st.markdown("### Social Media Handle Checker")

    desired_handle = st.text_input("Enter desired username/handle:", placeholder="your_username")

    if desired_handle:
        # Remove @ symbol if present
        clean_handle = desired_handle.replace("@", "").replace(" ", "").lower()

        st.markdown(f"### Checking availability for: **{clean_handle}**")

        # Platform URLs for checking
        platforms = {
            "Instagram": f"https://instagram.com/{clean_handle}",
            "Twitter": f"https://twitter.com/{clean_handle}",
            "Facebook": f"https://facebook.com/{clean_handle}",
            "LinkedIn": f"https://linkedin.com/in/{clean_handle}",
            "TikTok": f"https://tiktok.com/@{clean_handle}",
            "YouTube": f"https://youtube.com/c/{clean_handle}",
            "Pinterest": f"https://pinterest.com/{clean_handle}",
            "Snapchat": f"https://snapchat.com/add/{clean_handle}",
            "Twitch": f"https://twitch.tv/{clean_handle}",
            "Reddit": f"https://reddit.com/u/{clean_handle}"
        }

        if st.button("Check Availability"):
            with st.spinner("Checking handle availability..."):
                availability_results = check_handle_availability(clean_handle, platforms)
                display_handle_results(availability_results, clean_handle)


def check_handle_availability(handle, platforms):
    """Check if handle is available on different platforms"""
    results = {}

    # Simulate availability checking (in real app, you'd check actual APIs or scrape)
    import random

    for platform, url in platforms.items():
        # Simulate checking with random availability (for demo purposes)
        # In a real application, you would:
        # 1. Use platform APIs where available
        # 2. Make HTTP requests to check if profile exists
        # 3. Handle rate limiting and authentication

        is_available = random.choice([True, False, "Unknown"])

        results[platform] = {
            'url': url,
            'available': is_available,
            'status': 'Available' if is_available is True else 'Taken' if is_available is False else 'Unknown'
        }

    return results


def display_handle_results(results, handle):
    """Display handle availability results"""
    st.markdown("### 🔍 Availability Results")

    available_count = sum(1 for r in results.values() if r['available'] is True)
    taken_count = sum(1 for r in results.values() if r['available'] is False)
    unknown_count = sum(1 for r in results.values() if r['available'] == "Unknown")

    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Available", available_count)
    with col2:
        st.metric("Taken", taken_count)
    with col3:
        st.metric("Unknown", unknown_count)

    # Platform results
    st.markdown("### 📱 Platform Results")

    for platform, result in results.items():
        col1, col2, col3 = st.columns([2, 1, 2])

        with col1:
            st.write(f"**{platform}**")

        with col2:
            if result['available'] is True:
                st.success("✅ Available")
            elif result['available'] is False:
                st.error("❌ Taken")
            else:
                st.warning("❓ Unknown")

        with col3:
            st.write(f"[Check manually]({result['url']})")

    # Suggestions
    if taken_count > 0:
        st.markdown("### 💡 Alternative Suggestions")
        suggestions = [
            f"{handle}_official",
            f"the_{handle}",
            f"{handle}hq",
            f"{handle}_co",
            f"{handle}2024",
            f"real_{handle}"
        ]

        for suggestion in suggestions[:3]:
            st.write(f"• {suggestion}")


def bio_generator():
    """Generate social media bio/description"""
    create_tool_header("Bio Generator", "Generate engaging social media bios", "📝")

    st.markdown("### Social Media Bio Generator")

    # Profile information
    st.markdown("#### Profile Information")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name/Brand:", placeholder="John Doe")
        profession = st.text_input("Profession/Role:", placeholder="Digital Marketer")
        industry = st.selectbox("Industry:",
                                ["Technology", "Marketing", "Business", "Creative", "Health & Fitness",
                                 "Education", "Entertainment", "Food & Beverage", "Travel", "Fashion", "Other"])

    with col2:
        platform = st.selectbox("Primary Platform:",
                                ["Instagram", "Twitter", "LinkedIn", "TikTok", "YouTube"])
        tone = st.selectbox("Bio Tone:",
                            ["Professional", "Casual", "Funny", "Inspirational", "Quirky", "Minimalist"])
        include_emojis = st.checkbox("Include Emojis", value=True)

    # Additional details
    st.markdown("#### Additional Details")
    achievements = st.text_input("Key Achievements:", placeholder="Founder, Author, Speaker")
    interests = st.text_input("Interests/Hobbies:", placeholder="Coffee, Travel, Photography")
    call_to_action = st.text_input("Call to Action:", placeholder="DM for collaborations")
    website = st.text_input("Website/Link:", placeholder="www.example.com")

    if st.button("Generate Bio"):
        if name and profession:
            bio_options = generate_bio_options(name, profession, industry, platform, tone,
                                               include_emojis, achievements, interests, call_to_action, website)
            display_bio_options(bio_options, platform)
        else:
            st.error("Please fill in Name and Profession fields")


def generate_bio_options(name, profession, industry, platform, tone, include_emojis, achievements, interests, cta,
                         website):
    """Generate multiple bio options"""
    emoji_sets = {
        "Technology": ["💻", "🚀", "⚡", "🔧", "📱"],
        "Marketing": ["📈", "🎯", "💡", "📊", "🚀"],
        "Business": ["💼", "📈", "🎯", "💰", "🏆"],
        "Creative": ["🎨", "✨", "🎭", "📸", "🎬"],
        "Health & Fitness": ["💪", "🏃‍♂️", "🥗", "⚡", "🧘‍♀️"],
        "Education": ["📚", "🎓", "✏️", "🧠", "📖"],
        "Entertainment": ["🎬", "🎭", "🎪", "🎵", "✨"],
        "Food & Beverage": ["🍕", "☕", "👨‍🍳", "🥘", "🍷"],
        "Travel": ["✈️", "🌍", "📍", "🗺️", "🎒"],
        "Fashion": ["👗", "✨", "💄", "🛍️", "📸"]
    }

    emojis = emoji_sets.get(industry, ["✨", "🎯", "💡"])

    bio_templates = {
        "Professional": [
            f"{profession} | {achievements if achievements else 'Passionate about ' + industry.lower()}",
            f"{name} • {profession} • {interests if interests else 'Sharing insights about ' + industry.lower()}",
            f"Professional {profession.lower()} helping businesses grow"
        ],
        "Casual": [
            f"Hey! I'm {name} 👋 {profession} who loves {interests if interests else industry.lower()}",
            f"{profession} by day, {interests.split(',')[0] if interests else industry.lower() + ' enthusiast'} by night",
            f"Just a {profession.lower()} sharing my journey"
        ],
        "Funny": [
            f"{profession} with strong coffee opinions ☕",
            f"Professional {profession.lower()} • Amateur {interests.split(',')[0] if interests else 'human'}",
            f"{profession} who {interests if interests else 'takes life one day at a time'}"
        ],
        "Inspirational": [
            f"Empowering others through {profession.lower()} | {achievements if achievements else 'Making dreams reality'}",
            f"✨ {profession} on a mission to inspire",
            f"Turning passion into purpose • {profession}"
        ],
        "Quirky": [
            f"Professional {profession.lower()} & professional {interests.split(',')[0] if interests else 'daydreamer'}",
            f"{profession} with a side of {interests if interests else 'random facts'}",
            f"Plot twist: I'm a {profession.lower()}"
        ],
        "Minimalist": [
            f"{profession}",
            f"{name} • {profession}",
            f"{profession} • {achievements if achievements else industry}"
        ]
    }

    templates = bio_templates.get(tone, bio_templates["Professional"])
    bio_options = []

    for i, template in enumerate(templates):
        bio = template

        # Add emojis if requested
        if include_emojis and tone != "Minimalist":
            emoji_count = 2 if platform in ["Instagram", "TikTok"] else 1
            selected_emojis = emojis[:emoji_count]
            bio = f"{' '.join(selected_emojis)} {bio}"

        # Add call to action
        if cta:
            bio += f"\n{cta}"

        # Add website
        if website:
            bio += f"\n🔗 {website}"

        # Check character limits
        char_limits = {
            "Instagram": 150,
            "Twitter": 160,
            "LinkedIn": 120,
            "TikTok": 80,
            "YouTube": 1000
        }

        char_limit = char_limits.get(platform, 150)
        is_within_limit = len(bio) <= char_limit

        bio_options.append({
            'bio': bio,
            'char_count': len(bio),
            'char_limit': char_limit,
            'within_limit': is_within_limit,
            'style': tone
        })

    return bio_options


def display_bio_options(bio_options, platform):
    """Display generated bio options"""
    st.markdown("### 📝 Generated Bio Options")

    for i, option in enumerate(bio_options, 1):
        with st.expander(f"Option {i} - {option['style']} Style"):
            st.code(option['bio'], language=None)

            col1, col2 = st.columns(2)
            with col1:
                if option['within_limit']:
                    st.success(f"✅ {option['char_count']}/{option['char_limit']} characters")
                else:
                    st.error(f"❌ {option['char_count']}/{option['char_limit']} characters (too long)")

            with col2:
                if st.button(f"Copy Bio {i}", key=f"copy_bio_{i}"):
                    st.success("Bio copied to clipboard! (simulation)")

    # Tips
    st.markdown("### 💡 Bio Tips")
    tips = [
        f"Keep it under {bio_options[0]['char_limit']} characters for {platform}",
        "Use line breaks to make your bio easy to read",
        "Include a clear call-to-action",
        "Update your bio regularly to stay relevant",
        "Use keywords related to your industry for discoverability"
    ]

    for tip in tips:
        st.write(f"• {tip}")

    # Character limit info
    st.info(f"ℹ️ {platform} bio character limit: {bio_options[0]['char_limit']} characters")


# EMAIL MARKETING TOOLS

def email_template():
    """Email template generator"""
    create_tool_header("Email Template", "Generate professional email templates", "📧")

    st.markdown("### Email Template Generator")

    # Template type selection
    template_type = st.selectbox("Template Type:",
                                 ["Newsletter", "Welcome Series", "Promotional", "Abandoned Cart",
                                  "Product Launch", "Event Invitation", "Follow-up", "Re-engagement"])

    # Email details
    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("Company Name:", placeholder="Your Company")
        sender_name = st.text_input("Sender Name:", placeholder="John Doe")
        industry = st.selectbox("Industry:",
                                ["E-commerce", "SaaS", "Consulting", "Healthcare", "Education", "Other"])

    with col2:
        audience = st.selectbox("Target Audience:",
                                ["New Subscribers", "Existing Customers", "Prospects", "VIP Customers"])
        tone = st.selectbox("Email Tone:",
                            ["Professional", "Friendly", "Casual", "Urgent", "Informative"])
        include_images = st.checkbox("Include Image Placeholders")

    # Additional details
    main_message = st.text_area("Main Message/Content:",
                                placeholder="What's the key message you want to convey?")
    call_to_action = st.text_input("Call to Action:", placeholder="Shop Now, Learn More, etc.")

    if st.button("Generate Email Template"):
        if company_name and template_type:
            email_template_data = generate_email_template(template_type, company_name, sender_name,
                                                          industry, audience, tone, main_message,
                                                          call_to_action, include_images)
            display_email_template(email_template_data)
        else:
            st.error("Please fill in Company Name and select Template Type")


def generate_email_template(template_type, company, sender, industry, audience, tone, message, cta, images):
    """Generate email template based on parameters"""

    # Subject line templates
    subject_templates = {
        "Newsletter": f"📰 {company} Weekly Update - {message[:30]}..." if message else f"📰 Your {company} Weekly Update",
        "Welcome Series": f"Welcome to {company}! Here's what's next...",
        "Promotional": f"🔥 Special Offer from {company} - Don't Miss Out!",
        "Abandoned Cart": f"You left something behind at {company}",
        "Product Launch": f"🚀 Introducing Our Latest Product",
        "Event Invitation": f"You're Invited: {company} Event",
        "Follow-up": f"Following up on your interest in {company}",
        "Re-engagement": f"We miss you! Come back to {company}"
    }

    # Email body templates
    body_templates = {
        "Newsletter": f"""
Hi there!

Welcome to this week's {company} newsletter. Here's what's happening:

{message if message else ("• Industry insights and trends" + chr(10) + "• Product updates" + chr(10) + "• Customer success stories")}

[IMAGE PLACEHOLDER: Newsletter header image]

Best regards,
{sender}
{company} Team
        """,
        "Welcome Series": f"""
Welcome to {company}!

Hi there,

We're thrilled to have you join our community! Here's what you can expect:

{message if message else ("✓ Exclusive content and insights" + chr(10) + "✓ Special member-only offers" + chr(10) + "✓ Regular updates from our team")}

[IMAGE PLACEHOLDER: Welcome image]

Ready to get started?

Best,
{sender}
        """,
        "Promotional": f"""
Special Offer Just for You!

Hi there,

{message if message else f"We have an exclusive offer that we think you'll love:"}

🎯 [OFFER DETAILS]
⏰ Limited time only
💝 Exclusive for {company} subscribers

[IMAGE PLACEHOLDER: Product/offer image]

Don't wait - this offer expires soon!

Cheers,
{sender}
        """
    }

    # Get template or create generic one
    subject = subject_templates.get(template_type, f"{company} - {template_type}")
    body = body_templates.get(template_type, f"""
Hi there,

{message if message else f"Thank you for your interest in {company}."}

[MAIN CONTENT AREA]

{'[IMAGE PLACEHOLDER: Main content image]' if images else ''}

Best regards,
{sender}
{company}
    """)

    # Add CTA if provided
    if cta:
        body += f"\n\n[BUTTON: {cta}]\n"

    return {
        'subject': subject,
        'body': body,
        'template_type': template_type,
        'html_preview': generate_html_preview(subject, body, company)
    }


def generate_html_preview(subject, body, company):
    """Generate HTML preview of email"""
    html_template = f"""
    <div style="max-width: 600px; margin: 0 auto; font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
        <div style="background-color: white; padding: 30px; border-radius: 8px;">
            <h2 style="color: #333; margin-bottom: 20px;">{subject}</h2>
            <div style="line-height: 1.6; color: #555;">
                {body.replace('[IMAGE PLACEHOLDER:', '<p style="background-color: #e9e9e9; padding: 20px; text-align: center; border-radius: 4px;">[IMAGE PLACEHOLDER:').replace(']', ']</p>').replace(chr(10), '<br>')}
            </div>
            <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
            <p style="font-size: 12px; color: #888; text-align: center;">
                © {company}. All rights reserved.<br>
                You received this email because you subscribed to our newsletter.
            </p>
        </div>
    </div>
    """
    return html_template


def display_email_template(template_data):
    """Display the generated email template"""
    st.markdown("### 📧 Generated Email Template")

    # Subject line
    st.markdown("#### Subject Line")
    st.code(template_data['subject'])

    # Email body
    st.markdown("#### Email Body")
    st.code(template_data['body'], language=None)

    # HTML Preview
    st.markdown("#### HTML Preview")
    st.markdown(template_data['html_preview'], unsafe_allow_html=True)

    # Download options
    st.markdown("### 📥 Download Template")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Copy Plain Text"):
            st.success("Template copied! (simulation)")

    with col2:
        if st.button("Copy HTML"):
            st.success("HTML template copied! (simulation)")


def list_segmentation():
    """Email list segmentation tool"""
    create_tool_header("List Segmentation", "Segment your email list for better targeting", "🎯")

    st.markdown("### Email List Segmentation")

    # Upload or input data
    st.markdown("#### Customer Data")
    uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)

    if uploaded_file:
        st.success("✅ File uploaded successfully!")
        st.info("File processing simulation - analyzing customer data...")
    else:
        st.markdown("#### Sample Data Input")
        st.info("In a real application, you would upload a CSV file with customer data")

    # Segmentation criteria
    st.markdown("#### Segmentation Criteria")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Demographics**")
        age_segments = st.multiselect("Age Groups:",
                                      ["18-25", "26-35", "36-45", "46-55", "55+"])
        location_segments = st.multiselect("Locations:",
                                           ["North America", "Europe", "Asia", "Other"])

    with col2:
        st.markdown("**Behavior**")
        engagement_segments = st.multiselect("Engagement Level:",
                                             ["Highly Engaged", "Moderately Engaged", "Low Engagement", "Inactive"])
        purchase_segments = st.multiselect("Purchase Behavior:",
                                           ["Frequent Buyers", "Occasional Buyers", "One-time Buyers",
                                            "Never Purchased"])

    # Additional criteria
    st.markdown("#### Advanced Segmentation")
    interests = st.text_input("Interest Categories:", placeholder="technology, fitness, travel")
    lifecycle_stage = st.multiselect("Customer Lifecycle:",
                                     ["New Subscriber", "Active Customer", "At-Risk", "Win-Back"])

    if st.button("Create Segments"):
        segments = create_email_segments(age_segments, location_segments, engagement_segments,
                                         purchase_segments, interests, lifecycle_stage)
        display_segmentation_results(segments)


def create_email_segments(age_groups, locations, engagement, purchase, interests, lifecycle):
    """Create email segments based on criteria"""

    # Simulate segment creation
    segments = []

    # Demographic segments
    for age in age_groups:
        segments.append({
            'name': f"{age} Age Group",
            'criteria': f"Age: {age}",
            'estimated_size': f"{random.randint(500, 5000):,}",
            'engagement_rate': f"{random.uniform(15, 45):.1f}%",
            'recommended_content': "Age-appropriate content and messaging"
        })

    # Engagement segments
    for eng in engagement:
        segments.append({
            'name': eng,
            'criteria': f"Engagement: {eng}",
            'estimated_size': f"{random.randint(1000, 8000):,}",
            'engagement_rate': f"{random.uniform(10, 60):.1f}%",
            'recommended_content': "Tailored based on engagement patterns"
        })

    # Purchase behavior segments
    for purchase_type in purchase:
        segments.append({
            'name': purchase_type,
            'criteria': f"Purchase: {purchase_type}",
            'estimated_size': f"{random.randint(800, 6000):,}",
            'engagement_rate': f"{random.uniform(20, 50):.1f}%",
            'recommended_content': "Purchase-focused messaging"
        })

    return segments


def display_segmentation_results(segments):
    """Display segmentation results"""
    st.markdown("### 🎯 Email Segments Created")

    if not segments:
        st.info("Please select segmentation criteria to create segments")
        return

    # Overview metrics
    total_contacts = sum(int(segment['estimated_size'].replace(',', '')) for segment in segments)
    avg_engagement = sum(float(segment['engagement_rate'].replace('%', '')) for segment in segments) / len(segments)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Segments", len(segments))
    with col2:
        st.metric("Total Contacts", f"{total_contacts:,}")
    with col3:
        st.metric("Avg Engagement", f"{avg_engagement:.1f}%")

    # Segment details
    for i, segment in enumerate(segments, 1):
        with st.expander(f"Segment {i}: {segment['name']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Criteria:** {segment['criteria']}")
                st.write(f"**Size:** {segment['estimated_size']} contacts")
            with col2:
                st.write(f"**Engagement Rate:** {segment['engagement_rate']}")
                st.write(f"**Recommendation:** {segment['recommended_content']}")

    # Export option
    st.markdown("### 📥 Export Segments")
    if st.button("Generate Segment Report"):
        report = "\n".join([f"{seg['name']}: {seg['estimated_size']} contacts ({seg['engagement_rate']} engagement)"
                            for seg in segments])
        st.text_area("Copy this segment report:", f"Email Segmentation Report\n\n{report}", height=200)


def deliverability_checker():
    """Email deliverability checker"""
    create_tool_header("Deliverability Checker", "Check email deliverability factors", "✅")

    st.markdown("### Email Deliverability Checker")

    # Email content input
    st.markdown("#### Email Content Analysis")
    subject_line = st.text_input("Subject Line:", placeholder="Your email subject line")
    email_content = st.text_area("Email Content:", placeholder="Your email body content...", height=200)
    sender_email = st.text_input("Sender Email:", placeholder="sender@yourdomain.com")

    # Sender details
    col1, col2 = st.columns(2)
    with col1:
        sender_domain = st.text_input("Sender Domain:", placeholder="yourdomain.com")
        email_type = st.selectbox("Email Type:", ["Newsletter", "Promotional", "Transactional", "Welcome"])

    with col2:
        list_type = st.selectbox("List Type:", ["Opt-in", "Double Opt-in", "Purchased", "Scraped"])
        frequency = st.selectbox("Sending Frequency:", ["Daily", "Weekly", "Bi-weekly", "Monthly"])

    if st.button("Check Deliverability"):
        if subject_line and email_content and sender_email:
            deliverability_score = analyze_deliverability(subject_line, email_content, sender_email,
                                                          sender_domain, email_type, list_type, frequency)
            display_deliverability_results(deliverability_score)
        else:
            st.error("Please fill in all required fields")


def analyze_deliverability(subject, content, sender_email, domain, email_type, list_type, frequency):
    """Analyze email deliverability factors"""

    score = 100
    issues = []
    recommendations = []

    # Subject line analysis
    spam_words = ['free', 'urgent', 'act now', 'limited time', 'click here', 'buy now', '!!!', 'CAPS']
    subject_spam_count = sum(1 for word in spam_words if word.lower() in subject.lower())

    if subject_spam_count > 2:
        score -= 15
        issues.append(f"Subject line contains {subject_spam_count} potential spam words")
        recommendations.append("Reduce use of promotional language in subject line")

    if len(subject) > 50:
        score -= 5
        issues.append("Subject line is too long")
        recommendations.append("Keep subject line under 50 characters")

    # Content analysis
    content_spam_count = sum(1 for word in spam_words if word.lower() in content.lower())
    if content_spam_count > 5:
        score -= 20
        issues.append(f"Email content contains {content_spam_count} potential spam words")
        recommendations.append("Reduce promotional language in email content")

    # Check for HTML/text ratio
    if '<html>' in content.lower() or '<div>' in content.lower():
        # HTML email
        text_ratio = len(re.sub(r'<[^>]+>', '', content)) / len(content)
        if text_ratio < 0.3:
            score -= 10
            issues.append("Low text-to-HTML ratio")
            recommendations.append("Add more text content relative to HTML")

    # Sender reputation factors
    if not sender_email.endswith(domain) if domain else True:
        score -= 5
        issues.append("Sender email domain mismatch")
        recommendations.append("Use sender email from same domain")

    # List quality
    if list_type == "Purchased":
        score -= 25
        issues.append("Using purchased email list")
        recommendations.append("Use opt-in lists for better deliverability")
    elif list_type == "Scraped":
        score -= 40
        issues.append("Using scraped email list")
        recommendations.append("Never use scraped email lists")

    # Frequency issues
    if frequency == "Daily" and email_type == "Promotional":
        score -= 10
        issues.append("High promotional email frequency")
        recommendations.append("Reduce promotional email frequency")

    # Authentication simulation
    spf_status = random.choice([True, False])
    dkim_status = random.choice([True, False])
    dmarc_status = random.choice([True, False])

    if not spf_status:
        score -= 15
        issues.append("SPF record not configured")
        recommendations.append("Set up SPF record for your domain")

    if not dkim_status:
        score -= 15
        issues.append("DKIM not configured")
        recommendations.append("Configure DKIM signing")

    if not dmarc_status:
        score -= 10
        issues.append("DMARC policy not set")
        recommendations.append("Implement DMARC policy")

    # Ensure score doesn't go below 0
    score = max(0, score)

    return {
        'score': score,
        'grade': get_deliverability_grade(score),
        'issues': issues,
        'recommendations': recommendations,
        'authentication': {
            'spf': spf_status,
            'dkim': dkim_status,
            'dmarc': dmarc_status
        }
    }


def get_deliverability_grade(score):
    """Get letter grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def display_deliverability_results(results):
    """Display deliverability analysis results"""
    st.markdown("### 📊 Deliverability Analysis Results")

    # Overall score
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Deliverability Score", f"{results['score']}/100")
    with col2:
        st.metric("Grade", results['grade'])
    with col3:
        if results['score'] >= 80:
            st.success("✅ Good Deliverability")
        elif results['score'] >= 60:
            st.warning("⚠️ Moderate Deliverability")
        else:
            st.error("❌ Poor Deliverability")

    # Authentication status
    st.markdown("### 🔐 Authentication Status")
    auth_col1, auth_col2, auth_col3 = st.columns(3)

    with auth_col1:
        if results['authentication']['spf']:
            st.success("✅ SPF Configured")
        else:
            st.error("❌ SPF Missing")

    with auth_col2:
        if results['authentication']['dkim']:
            st.success("✅ DKIM Configured")
        else:
            st.error("❌ DKIM Missing")

    with auth_col3:
        if results['authentication']['dmarc']:
            st.success("✅ DMARC Configured")
        else:
            st.error("❌ DMARC Missing")

    # Issues found
    if results['issues']:
        st.markdown("### ⚠️ Issues Found")
        for issue in results['issues']:
            st.error(f"❌ {issue}")

    # Recommendations
    if results['recommendations']:
        st.markdown("### 💡 Recommendations")
        for rec in results['recommendations']:
            st.info(f"💡 {rec}")

    if not results['issues']:
        st.success("🎉 No major deliverability issues found!")


# ANALYTICS TOOLS

def click_tracker():
    """URL click tracking tool"""
    create_tool_header("Click Tracker", "Track clicks on your marketing links", "🖱️")

    st.markdown("### Click Tracking Setup")

    # URL input
    original_url = st.text_input("Original URL:", placeholder="https://example.com/product")
    campaign_name = st.text_input("Campaign Name:", placeholder="summer-sale-2024")

    # Tracking parameters
    col1, col2 = st.columns(2)
    with col1:
        source = st.text_input("Traffic Source:", placeholder="email, social, ads")
        medium = st.text_input("Traffic Medium:", placeholder="newsletter, post, banner")

    with col2:
        campaign_term = st.text_input("Campaign Term (optional):", placeholder="keywords")
        campaign_content = st.text_input("Campaign Content (optional):", placeholder="button, link")

    if original_url and campaign_name:
        tracked_url = generate_tracked_url(original_url, campaign_name, source, medium, campaign_term, campaign_content)

        st.markdown("### 🔗 Tracked URL")
        st.code(tracked_url)

        if st.button("Simulate Click Data"):
            click_data = simulate_click_tracking(campaign_name)
            display_click_analytics(click_data)


def generate_tracked_url(url, campaign, source, medium, term="", content=""):
    """Generate tracked URL with analytics parameters"""
    from urllib.parse import urlencode, urlparse, urlunparse

    # Parse original URL
    parsed = urlparse(url)

    # Build tracking parameters
    params = {
        'utm_source': source or 'direct',
        'utm_medium': medium or 'unknown',
        'utm_campaign': campaign,
        'track_id': f"track_{random.randint(1000, 9999)}"
    }

    if term:
        params['utm_term'] = term
    if content:
        params['utm_content'] = content

    # Add parameters to URL
    query = urlencode(params)
    existing_query = parsed.query
    if existing_query:
        query = f"{existing_query}&{query}"

    # Reconstruct URL
    tracked_url = urlunparse((
        parsed.scheme, parsed.netloc, parsed.path,
        parsed.params, query, parsed.fragment
    ))

    return tracked_url


def simulate_click_tracking(campaign_name):
    """Simulate click tracking data"""
    import datetime

    # Generate sample data for last 7 days
    days = []
    for i in range(7):
        date = datetime.date.today() - datetime.timedelta(days=i)
        clicks = random.randint(10, 100)
        unique_clicks = int(clicks * random.uniform(0.7, 0.9))

        days.append({
            'date': date.strftime('%Y-%m-%d'),
            'clicks': clicks,
            'unique_clicks': unique_clicks,
            'conversion_rate': random.uniform(2, 8)
        })

    return {
        'campaign': campaign_name,
        'total_clicks': sum(day['clicks'] for day in days),
        'unique_clicks': sum(day['unique_clicks'] for day in days),
        'avg_ctr': random.uniform(1.5, 4.2),
        'top_sources': [
            {'source': 'email', 'clicks': random.randint(50, 200)},
            {'source': 'social', 'clicks': random.randint(30, 150)},
            {'source': 'direct', 'clicks': random.randint(20, 100)}
        ],
        'daily_data': days
    }


def display_click_analytics(data):
    """Display click tracking analytics"""
    st.markdown("### 📊 Click Analytics Dashboard")

    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Clicks", data['total_clicks'])
    with col2:
        st.metric("Unique Clicks", data['unique_clicks'])
    with col3:
        st.metric("Avg CTR", f"{data['avg_ctr']:.2f}%")

    # Top sources
    st.markdown("### 🎯 Top Traffic Sources")
    for source in data['top_sources']:
        st.write(f"**{source['source'].title()}:** {source['clicks']} clicks")

    # Daily breakdown
    st.markdown("### 📈 Daily Click Data")
    for day in data['daily_data']:
        with st.expander(f"{day['date']} - {day['clicks']} clicks"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Total Clicks:** {day['clicks']}")
                st.write(f"**Unique Clicks:** {day['unique_clicks']}")
            with col2:
                st.write(f"**Conversion Rate:** {day['conversion_rate']:.1f}%")


def conversion_calculator():
    """Conversion rate calculator"""
    create_tool_header("Conversion Calculator", "Calculate conversion rates and metrics", "📈")

    st.markdown("### Conversion Rate Calculator")

    # Input metrics
    col1, col2 = st.columns(2)
    with col1:
        visitors = st.number_input("Total Visitors:", min_value=0, value=1000)
        conversions = st.number_input("Total Conversions:", min_value=0, value=50)
        revenue = st.number_input("Total Revenue ($):", min_value=0.0, value=2500.0, format="%.2f")

    with col2:
        cost = st.number_input("Total Cost ($):", min_value=0.0, value=500.0, format="%.2f")
        time_period = st.selectbox("Time Period:", ["Daily", "Weekly", "Monthly", "Quarterly"])
        goal_rate = st.number_input("Goal Conversion Rate (%):", min_value=0.0, value=5.0, format="%.2f")

    if visitors > 0:
        metrics = calculate_conversion_metrics(visitors, conversions, revenue, cost, goal_rate)
        display_conversion_metrics(metrics, time_period)


def calculate_conversion_metrics(visitors, conversions, revenue, cost, goal_rate):
    """Calculate various conversion metrics"""

    # Basic conversion rate
    conversion_rate = (conversions / visitors * 100) if visitors > 0 else 0

    # Revenue metrics
    avg_order_value = revenue / conversions if conversions > 0 else 0
    revenue_per_visitor = revenue / visitors if visitors > 0 else 0

    # Cost metrics
    cost_per_visitor = cost / visitors if visitors > 0 else 0
    cost_per_conversion = cost / conversions if conversions > 0 else 0

    # ROI metrics
    profit = revenue - cost
    roi = (profit / cost * 100) if cost > 0 else 0
    roas = (revenue / cost) if cost > 0 else 0

    # Goal analysis
    goal_gap = goal_rate - conversion_rate
    visitors_needed = (conversions / (goal_rate / 100)) if goal_rate > 0 else visitors

    return {
        'conversion_rate': conversion_rate,
        'avg_order_value': avg_order_value,
        'revenue_per_visitor': revenue_per_visitor,
        'cost_per_visitor': cost_per_visitor,
        'cost_per_conversion': cost_per_conversion,
        'profit': profit,
        'roi': roi,
        'roas': roas,
        'goal_gap': goal_gap,
        'visitors_needed': visitors_needed,
        'goal_rate': goal_rate
    }


def display_conversion_metrics(metrics, time_period):
    """Display conversion metrics"""
    st.markdown("### 📊 Conversion Metrics")

    # Conversion metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        if metrics['conversion_rate'] >= metrics['goal_rate']:
            st.success(f"Conversion Rate: {metrics['conversion_rate']:.2f}%")
        else:
            st.warning(f"Conversion Rate: {metrics['conversion_rate']:.2f}%")

    with col2:
        st.metric("Avg Order Value", f"${metrics['avg_order_value']:.2f}")

    with col3:
        st.metric("Revenue per Visitor", f"${metrics['revenue_per_visitor']:.2f}")

    # Cost metrics
    st.markdown("### 💰 Cost Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Cost per Visitor", f"${metrics['cost_per_visitor']:.2f}")
    with col2:
        st.metric("Cost per Conversion", f"${metrics['cost_per_conversion']:.2f}")
    with col3:
        if metrics['roi'] > 0:
            st.success(f"ROI: {metrics['roi']:.1f}%")
        else:
            st.error(f"ROI: {metrics['roi']:.1f}%")

    # Performance analysis
    st.markdown("### 🎯 Performance Analysis")

    if metrics['goal_gap'] > 0:
        st.warning(f"⚠️ You're {metrics['goal_gap']:.2f}% below your goal conversion rate")
        st.info(
            f"💡 You need {metrics['visitors_needed']:.0f} visitors to reach your goal (vs current {metrics['visitors_needed'] - (metrics['visitors_needed'] - metrics['conversion_rate'] / metrics['goal_rate'] * metrics['visitors_needed']):.0f})")
    else:
        st.success(f"✅ You've exceeded your goal conversion rate!")

    if metrics['roas'] >= 4:
        st.success(f"✅ Excellent ROAS: {metrics['roas']:.2f}x")
    elif metrics['roas'] >= 2:
        st.warning(f"⚠️ Good ROAS: {metrics['roas']:.2f}x")
    else:
        st.error(f"❌ Low ROAS: {metrics['roas']:.2f}x")


def roi_calculator():
    """ROI calculator for marketing campaigns"""
    create_tool_header("ROI Calculator", "Calculate return on investment for marketing campaigns", "💰")

    st.markdown("### ROI Calculator")

    # Campaign details
    campaign_type = st.selectbox("Campaign Type:",
                                 ["Google Ads", "Facebook Ads", "Email Marketing", "Content Marketing",
                                  "SEO", "Influencer Marketing", "Other"])

    # Investment inputs
    st.markdown("#### Investment Details")
    col1, col2 = st.columns(2)
    with col1:
        ad_spend = st.number_input("Ad Spend ($):", min_value=0.0, value=1000.0, format="%.2f")
        time_investment = st.number_input("Time Investment (hours):", min_value=0.0, value=20.0, format="%.1f")
        hourly_rate = st.number_input("Hourly Rate ($):", min_value=0.0, value=50.0, format="%.2f")

    with col2:
        tool_costs = st.number_input("Tool/Software Costs ($):", min_value=0.0, value=100.0, format="%.2f")
        other_costs = st.number_input("Other Costs ($):", min_value=0.0, value=0.0, format="%.2f")
        time_period = st.selectbox("Time Period:", ["Week", "Month", "Quarter", "Year"])

    # Results inputs
    st.markdown("#### Campaign Results")
    col1, col2 = st.columns(2)
    with col1:
        revenue = st.number_input("Revenue Generated ($):", min_value=0.0, value=3000.0, format="%.2f")
        conversions = st.number_input("Total Conversions:", min_value=0, value=30)

    with col2:
        new_customers = st.number_input("New Customers:", min_value=0, value=25)
        customer_lifetime_value = st.number_input("Avg Customer LTV ($):", min_value=0.0, value=500.0, format="%.2f")

    if st.button("Calculate ROI"):
        roi_data = calculate_roi_metrics(ad_spend, time_investment, hourly_rate, tool_costs,
                                         other_costs, revenue, conversions, new_customers,
                                         customer_lifetime_value, campaign_type)
        display_roi_analysis(roi_data, time_period)


def calculate_roi_metrics(ad_spend, time_hours, hourly_rate, tool_costs, other_costs,
                          revenue, conversions, new_customers, ltv, campaign_type):
    """Calculate comprehensive ROI metrics"""

    # Total investment calculation
    time_cost = time_hours * hourly_rate
    total_investment = ad_spend + time_cost + tool_costs + other_costs

    # Revenue calculations
    immediate_revenue = revenue
    ltv_revenue = new_customers * ltv
    total_revenue = immediate_revenue + ltv_revenue

    # ROI calculations
    immediate_roi = ((immediate_revenue - total_investment) / total_investment * 100) if total_investment > 0 else 0
    ltv_roi = ((total_revenue - total_investment) / total_investment * 100) if total_investment > 0 else 0

    # Additional metrics
    cost_per_conversion = total_investment / conversions if conversions > 0 else 0
    cost_per_customer = total_investment / new_customers if new_customers > 0 else 0
    roas = immediate_revenue / total_investment if total_investment > 0 else 0

    # Benchmarks by campaign type
    benchmarks = {
        "Google Ads": {"good_roi": 200, "excellent_roi": 400},
        "Facebook Ads": {"good_roi": 150, "excellent_roi": 300},
        "Email Marketing": {"good_roi": 300, "excellent_roi": 500},
        "Content Marketing": {"good_roi": 200, "excellent_roi": 400},
        "SEO": {"good_roi": 500, "excellent_roi": 1000},
        "Influencer Marketing": {"good_roi": 150, "excellent_roi": 300},
        "Other": {"good_roi": 200, "excellent_roi": 400}
    }

    benchmark = benchmarks.get(campaign_type, benchmarks["Other"])

    return {
        'total_investment': total_investment,
        'investment_breakdown': {
            'ad_spend': ad_spend,
            'time_cost': time_cost,
            'tool_costs': tool_costs,
            'other_costs': other_costs
        },
        'immediate_revenue': immediate_revenue,
        'ltv_revenue': ltv_revenue,
        'total_revenue': total_revenue,
        'immediate_roi': immediate_roi,
        'ltv_roi': ltv_roi,
        'cost_per_conversion': cost_per_conversion,
        'cost_per_customer': cost_per_customer,
        'roas': roas,
        'benchmark': benchmark,
        'campaign_type': campaign_type
    }


def display_roi_analysis(roi_data, time_period):
    """Display comprehensive ROI analysis"""
    st.markdown("### 💰 ROI Analysis Results")

    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        if roi_data['immediate_roi'] >= roi_data['benchmark']['excellent_roi']:
            st.success(f"Immediate ROI: {roi_data['immediate_roi']:.1f}%")
        elif roi_data['immediate_roi'] >= roi_data['benchmark']['good_roi']:
            st.warning(f"Immediate ROI: {roi_data['immediate_roi']:.1f}%")
        else:
            st.error(f"Immediate ROI: {roi_data['immediate_roi']:.1f}%")

    with col2:
        st.metric("LTV ROI", f"{roi_data['ltv_roi']:.1f}%")

    with col3:
        st.metric("ROAS", f"{roi_data['roas']:.2f}x")

    # Investment breakdown
    st.markdown("### 💸 Investment Breakdown")
    breakdown = roi_data['investment_breakdown']

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Ad Spend:** ${breakdown['ad_spend']:.2f}")
        st.write(f"**Time Cost:** ${breakdown['time_cost']:.2f}")
    with col2:
        st.write(f"**Tool Costs:** ${breakdown['tool_costs']:.2f}")
        st.write(f"**Other Costs:** ${breakdown['other_costs']:.2f}")

    st.write(f"**Total Investment:** ${roi_data['total_investment']:.2f}")

    # Revenue breakdown
    st.markdown("### 💵 Revenue Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Immediate Revenue", f"${roi_data['immediate_revenue']:.2f}")
        st.metric("Cost per Conversion", f"${roi_data['cost_per_conversion']:.2f}")

    with col2:
        st.metric("LTV Revenue", f"${roi_data['ltv_revenue']:.2f}")
        st.metric("Cost per Customer", f"${roi_data['cost_per_customer']:.2f}")

    # Benchmark comparison
    st.markdown(f"### 📊 {roi_data['campaign_type']} Benchmarks")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Good ROI", f"{roi_data['benchmark']['good_roi']}%+")
    with col2:
        st.metric("Excellent ROI", f"{roi_data['benchmark']['excellent_roi']}%+")

    # Recommendations
    st.markdown("### 💡 Recommendations")
    if roi_data['immediate_roi'] < 0:
        st.error("❌ Campaign is losing money. Consider pausing and optimizing.")
    elif roi_data['immediate_roi'] < roi_data['benchmark']['good_roi']:
        st.warning("⚠️ ROI is below industry benchmarks. Optimize targeting and content.")
    else:
        st.success("✅ Campaign is performing well. Consider scaling up.")


def traffic_estimator():
    """Website traffic estimator"""
    create_tool_header("Traffic Estimator", "Estimate website traffic and potential", "📊")

    st.markdown("### Traffic Estimation Tool")

    # Website details
    website_url = st.text_input("Website URL:", placeholder="https://example.com")
    industry = st.selectbox("Industry:",
                            ["Technology", "E-commerce", "Healthcare", "Finance", "Education",
                             "Travel", "Food & Beverage", "Real Estate", "Other"])

    # Current metrics
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Current Metrics")
        current_monthly_visitors = st.number_input("Current Monthly Visitors:", min_value=0, value=10000)
        current_pages = st.number_input("Total Pages on Site:", min_value=1, value=50)
        domain_age = st.selectbox("Domain Age:", ["Less than 1 year", "1-2 years", "2-5 years", "5+ years"])

    with col2:
        st.markdown("#### SEO Metrics")
        target_keywords = st.number_input("Target Keywords:", min_value=0, value=20)
        backlinks = st.number_input("Estimated Backlinks:", min_value=0, value=100)
        content_frequency = st.selectbox("Content Publishing:", ["Daily", "Weekly", "Bi-weekly", "Monthly", "Rarely"])

    # Goals and timeframe
    st.markdown("#### Goals")
    goal_timeframe = st.selectbox("Goal Timeframe:", ["3 months", "6 months", "1 year", "2 years"])
    marketing_budget = st.number_input("Monthly Marketing Budget ($):", min_value=0, value=1000)

    if st.button("Estimate Traffic Potential"):
        if website_url:
            traffic_estimate = calculate_traffic_potential(current_monthly_visitors, current_pages,
                                                           domain_age, target_keywords, backlinks,
                                                           content_frequency, goal_timeframe,
                                                           marketing_budget, industry)
            display_traffic_estimates(traffic_estimate)
        else:
            st.error("Please enter a website URL")


def calculate_traffic_potential(current_visitors, pages, domain_age, keywords, backlinks,
                                content_freq, timeframe, budget, industry):
    """Calculate traffic growth potential"""

    # Base growth factors
    domain_multiplier = {"Less than 1 year": 0.8, "1-2 years": 1.0, "2-5 years": 1.2, "5+ years": 1.5}
    content_multiplier = {"Daily": 2.0, "Weekly": 1.5, "Bi-weekly": 1.2, "Monthly": 1.0, "Rarely": 0.7}
    timeframe_multiplier = {"3 months": 0.3, "6 months": 0.6, "1 year": 1.0, "2 years": 1.8}

    # Industry benchmarks (average monthly visitors per $1000 marketing spend)
    industry_benchmarks = {
        "Technology": 2000,
        "E-commerce": 1500,
        "Healthcare": 1200,
        "Finance": 1000,
        "Education": 1800,
        "Travel": 2200,
        "Food & Beverage": 1600,
        "Real Estate": 1300,
        "Other": 1500
    }

    # Calculate potential factors
    domain_factor = domain_multiplier.get(domain_age, 1.0)
    content_factor = content_multiplier.get(content_freq, 1.0)
    time_factor = timeframe_multiplier.get(timeframe, 1.0)

    # SEO potential
    seo_potential = (keywords * 50) + (backlinks * 10)  # Rough estimate
    seo_growth = seo_potential * domain_factor * content_factor * time_factor

    # Paid traffic potential
    industry_benchmark = industry_benchmarks.get(industry, 1500)
    paid_potential = (budget / 1000) * industry_benchmark * time_factor

    # Content growth
    content_pages_growth = pages * content_factor * time_factor * 0.1

    # Total estimated growth
    total_potential_visitors = current_visitors + seo_growth + paid_potential + content_pages_growth

    # Conservative and optimistic scenarios
    conservative_estimate = total_potential_visitors * 0.7
    optimistic_estimate = total_potential_visitors * 1.3

    return {
        'current_visitors': current_visitors,
        'realistic_estimate': int(total_potential_visitors),
        'conservative_estimate': int(conservative_estimate),
        'optimistic_estimate': int(optimistic_estimate),
        'growth_factors': {
            'seo_growth': int(seo_growth),
            'paid_growth': int(paid_potential),
            'content_growth': int(content_pages_growth)
        },
        'timeframe': timeframe,
        'industry': industry
    }


def display_traffic_estimates(estimates):
    """Display traffic growth estimates"""
    st.markdown("### 📈 Traffic Growth Estimates")

    # Main estimates
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Conservative", f"{estimates['conservative_estimate']:,}")
    with col2:
        st.metric("Realistic", f"{estimates['realistic_estimate']:,}")
    with col3:
        st.metric("Optimistic", f"{estimates['optimistic_estimate']:,}")

    # Growth breakdown
    st.markdown("### 📊 Growth Factor Breakdown")

    growth_factors = estimates['growth_factors']
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("SEO Growth", f"+{growth_factors['seo_growth']:,}")
    with col2:
        st.metric("Paid Growth", f"+{growth_factors['paid_growth']:,}")
    with col3:
        st.metric("Content Growth", f"+{growth_factors['content_growth']:,}")

    # Growth percentage
    current_visitors = estimates['current_visitors']
    realistic_growth = estimates['realistic_estimate']

    if current_visitors > 0:
        growth_percentage = ((realistic_growth - current_visitors) / current_visitors) * 100
        st.markdown(f"### 🎯 Projected Growth: {growth_percentage:.1f}% over {estimates['timeframe']}")

    # Recommendations
    st.markdown("### 💡 Recommendations to Achieve These Numbers")

    recommendations = [
        "📝 Increase content publishing frequency",
        "🔍 Target more long-tail keywords",
        "🔗 Build high-quality backlinks",
        "📱 Optimize for mobile and page speed",
        "📊 Track and optimize conversion rates",
        "🎯 Improve targeting in paid campaigns"
    ]

    for rec in recommendations:
        st.write(f"• {rec}")

    # Disclaimer
    st.info(
        "ℹ️ These estimates are based on industry averages and may vary significantly based on execution quality, competition, and market conditions.")


# LOCAL SEO TOOLS

def local_citation_checker():
    """Local citation checker tool"""
    create_tool_header("Local Citation Checker", "Check business citations across the web", "📍")

    st.markdown("### Local Citation Checker")

    # Business information
    col1, col2 = st.columns(2)
    with col1:
        business_name = st.text_input("Business Name:", placeholder="Your Business Name")
        phone_number = st.text_input("Phone Number:", placeholder="+1-555-123-4567")
        website = st.text_input("Website:", placeholder="https://yourbusiness.com")

    with col2:
        address = st.text_area("Address:", placeholder="123 Main St, City, State 12345")
        category = st.selectbox("Business Category:",
                                ["Restaurant", "Retail", "Healthcare", "Professional Services",
                                 "Home Services", "Automotive", "Beauty & Spa", "Other"])

    if st.button("Check Citations"):
        if business_name and address:
            citation_data = simulate_citation_check(business_name, phone_number, address, website)
            display_citation_results(citation_data)
        else:
            st.error("Please fill in Business Name and Address")


def simulate_citation_check(business_name, phone, address, website):
    """Simulate citation checking across major platforms"""

    # Major citation platforms
    platforms = [
        {"name": "Google My Business", "priority": "High",
         "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Yelp", "priority": "High", "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Facebook", "priority": "High", "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Apple Maps", "priority": "High", "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Bing Places", "priority": "Medium", "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Yellow Pages", "priority": "Medium", "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Foursquare", "priority": "Medium", "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "BBB", "priority": "Low", "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Chamber of Commerce", "priority": "Low",
         "status": random.choice(["Found", "Not Found", "Inconsistent"])},
        {"name": "Angie's List", "priority": "Low", "status": random.choice(["Found", "Not Found", "Inconsistent"])}
    ]

    # Calculate metrics
    found_count = sum(1 for p in platforms if p["status"] == "Found")
    inconsistent_count = sum(1 for p in platforms if p["status"] == "Inconsistent")

    return {
        'business_name': business_name,
        'platforms': platforms,
        'found_count': found_count,
        'inconsistent_count': inconsistent_count,
        'total_platforms': len(platforms),
        'citation_score': (found_count / len(platforms)) * 100
    }


def display_citation_results(data):
    """Display citation check results"""
    st.markdown("### 📊 Citation Analysis Results")

    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Citation Score", f"{data['citation_score']:.1f}%")
    with col2:
        st.metric("Citations Found", f"{data['found_count']}/{data['total_platforms']}")
    with col3:
        st.metric("Inconsistent", data['inconsistent_count'])

    # Platform breakdown
    st.markdown("### 🏢 Platform Breakdown")

    for platform in data['platforms']:
        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:
            st.write(f"**{platform['name']}**")

        with col2:
            if platform['status'] == "Found":
                st.success("✅ Found")
            elif platform['status'] == "Inconsistent":
                st.warning("⚠️ Inconsistent")
            else:
                st.error("❌ Not Found")

        with col3:
            priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
            st.write(f"{priority_color[platform['priority']]} {platform['priority']}")

    # Recommendations
    st.markdown("### 💡 Recommendations")
    recommendations = []

    if data['inconsistent_count'] > 0:
        recommendations.append("🔧 Fix inconsistent citations to improve local SEO")

    missing_count = data['total_platforms'] - data['found_count'] - data['inconsistent_count']
    if missing_count > 0:
        recommendations.append(f"📝 Create {missing_count} missing citations")

    if data['citation_score'] < 70:
        recommendations.append("⚡ Focus on high-priority platforms first")

    recommendations.extend([
        "📞 Ensure NAP (Name, Address, Phone) consistency across all platforms",
        "🖼️ Add business photos and complete profiles",
        "⭐ Encourage customer reviews on major platforms"
    ])

    for rec in recommendations:
        st.write(f"• {rec}")


def gmb_optimizer():
    """Google My Business optimization tool"""
    create_tool_header("GMB Optimizer", "Optimize your Google My Business listing", "🏢")

    st.markdown("### Google My Business Optimization")

    # Current GMB status
    st.markdown("#### Current GMB Information")

    col1, col2 = st.columns(2)
    with col1:
        business_name = st.text_input("Business Name:", placeholder="Your Business Name")
        business_category = st.selectbox("Primary Category:",
                                         ["Restaurant", "Retail Store", "Professional Service",
                                          "Healthcare", "Home Services", "Automotive", "Other"])
        phone = st.text_input("Phone Number:", placeholder="+1-555-123-4567")
        website = st.text_input("Website URL:", placeholder="https://yourbusiness.com")

    with col2:
        address = st.text_area("Business Address:", placeholder="Full business address")
        hours = st.text_area("Business Hours:", placeholder="Mon-Fri: 9AM-5PM\nSat: 10AM-3PM\nSun: Closed")
        description = st.text_area("Business Description:", placeholder="Brief description of your business")

    # Additional details
    st.markdown("#### Additional Information")
    col1, col2 = st.columns(2)
    with col1:
        has_photos = st.checkbox("Has business photos uploaded")
        has_logo = st.checkbox("Has business logo")
        has_reviews = st.number_input("Number of reviews:", min_value=0, value=0)

    with col2:
        avg_rating = st.number_input("Average rating:", min_value=0.0, max_value=5.0, value=0.0, format="%.1f")
        posts_frequency = st.selectbox("GMB Posts Frequency:", ["Never", "Rarely", "Monthly", "Weekly", "Daily"])
        responds_to_reviews = st.checkbox("Responds to customer reviews")

    if st.button("Analyze GMB Optimization"):
        if business_name and business_category:
            optimization_score = analyze_gmb_optimization(business_name, business_category, phone,
                                                          website, address, hours, description,
                                                          has_photos, has_logo, has_reviews,
                                                          avg_rating, posts_frequency, responds_to_reviews)
            display_gmb_optimization(optimization_score)
        else:
            st.error("Please fill in Business Name and Category")


def analyze_gmb_optimization(name, category, phone, website, address, hours, description,
                             photos, logo, reviews, rating, posts_freq, responds):
    """Analyze GMB optimization level"""

    score = 0
    max_score = 100
    issues = []
    recommendations = []

    # Basic information completeness (40 points)
    if name:
        score += 5
    else:
        issues.append("Missing business name")

    if phone:
        score += 5
    else:
        issues.append("Missing phone number")
        recommendations.append("Add a local phone number")

    if website:
        score += 5
    else:
        recommendations.append("Add your website URL")

    if address:
        score += 10
    else:
        issues.append("Missing complete address")
        recommendations.append("Add complete business address")

    if hours:
        score += 10
    else:
        issues.append("Missing business hours")
        recommendations.append("Add detailed business hours")

    if description and len(description) > 50:
        score += 5
    else:
        issues.append("Missing or incomplete business description")
        recommendations.append("Write a detailed business description (150+ words)")

    # Visual content (25 points)
    if photos:
        score += 15
    else:
        issues.append("No business photos")
        recommendations.append("Upload high-quality business photos")

    if logo:
        score += 10
    else:
        recommendations.append("Upload your business logo")

    # Reviews and engagement (25 points)
    if reviews > 0:
        if reviews >= 50:
            score += 10
        elif reviews >= 20:
            score += 7
        elif reviews >= 5:
            score += 5
        else:
            score += 3
    else:
        issues.append("No customer reviews")
        recommendations.append("Encourage customers to leave reviews")

    if rating >= 4.0:
        score += 5
    elif rating >= 3.0:
        score += 3
    elif rating > 0:
        score += 1
        issues.append("Low average rating")
        recommendations.append("Focus on improving customer experience")

    if responds:
        score += 5
    else:
        recommendations.append("Respond to all customer reviews")

    if posts_freq not in ["Never", "Rarely"]:
        if posts_freq == "Daily":
            score += 5
        elif posts_freq == "Weekly":
            score += 4
        elif posts_freq == "Monthly":
            score += 2
    else:
        recommendations.append("Post regular updates and offers")

    # Additional optimization tips
    if score < 70:
        recommendations.extend([
            "Verify your business listing",
            "Add business attributes (wheelchair accessible, WiFi, etc.)",
            "Create GMB posts about products, events, and offers",
            "Add frequently asked questions",
            "Upload 360° photos if possible"
        ])

    return {
        'score': score,
        'grade': get_gmb_grade(score),
        'issues': issues,
        'recommendations': recommendations,
        'review_count': reviews,
        'avg_rating': rating
    }


def get_gmb_grade(score):
    """Get letter grade for GMB optimization"""
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


def display_gmb_optimization(data):
    """Display GMB optimization results"""
    st.markdown("### 📊 GMB Optimization Score")

    # Main score
    col1, col2, col3 = st.columns(3)
    with col1:
        if data['score'] >= 80:
            st.success(f"Score: {data['score']}/100")
        elif data['score'] >= 60:
            st.warning(f"Score: {data['score']}/100")
        else:
            st.error(f"Score: {data['score']}/100")

    with col2:
        st.metric("Grade", data['grade'])

    with col3:
        if data['avg_rating'] > 0:
            st.metric("Review Rating", f"{data['avg_rating']:.1f}/5.0")
        else:
            st.metric("Review Rating", "No reviews")

    # Issues found
    if data['issues']:
        st.markdown("### ⚠️ Issues Found")
        for issue in data['issues']:
            st.error(f"❌ {issue}")

    # Recommendations
    st.markdown("### 💡 Optimization Recommendations")
    for rec in data['recommendations']:
        st.info(f"💡 {rec}")

    # Success message
    if not data['issues']:
        st.success("🎉 Your GMB listing is well optimized!")


def local_keyword_tool():
    """Local keyword research tool"""
    create_tool_header("Local Keyword Tool", "Research local keywords for your business", "🔍")

    st.markdown("### Local Keyword Research")

    # Input parameters
    col1, col2 = st.columns(2)
    with col1:
        business_type = st.text_input("Business Type:", placeholder="restaurant, dentist, plumber")
        location = st.text_input("Location:", placeholder="New York, NY")
        additional_services = st.text_area("Additional Services:", placeholder="delivery, emergency, 24/7")

    with col2:
        target_radius = st.selectbox("Target Radius:", ["5 miles", "10 miles", "25 miles", "50 miles"])
        competition_level = st.selectbox("Competition Level:", ["Low", "Medium", "High"])
        business_size = st.selectbox("Business Size:", ["Local", "Regional", "National Chain"])

    if st.button("Generate Local Keywords"):
        if business_type and location:
            keywords = generate_local_keywords(business_type, location, additional_services,
                                               target_radius, competition_level, business_size)
            display_local_keywords(keywords)
        else:
            st.error("Please fill in Business Type and Location")


def generate_local_keywords(business_type, location, services, radius, competition, size):
    """Generate local keyword suggestions"""

    # Extract city and state from location
    location_parts = location.split(',')
    city = location_parts[0].strip() if location_parts else location
    state = location_parts[1].strip() if len(location_parts) > 1 else ""

    # Base keyword patterns
    base_patterns = [
        f"{business_type} in {city}",
        f"{business_type} near me",
        f"{city} {business_type}",
        f"best {business_type} {city}",
        f"{business_type} {city} {state}".strip(),
        f"local {business_type}",
        f"{business_type} nearby"
    ]

    # Service-specific keywords
    service_keywords = []
    if services:
        service_list = [s.strip() for s in services.split(',')]
        for service in service_list:
            service_keywords.extend([
                f"{service} {business_type} {city}",
                f"{business_type} {service} near me",
                f"{city} {business_type} {service}"
            ])

    # Long-tail local keywords
    long_tail = [
        f"top rated {business_type} in {city}",
        f"affordable {business_type} {city}",
        f"{business_type} reviews {city}",
        f"emergency {business_type} {city}",
        f"24 hour {business_type} near me",
        f"{business_type} phone number {city}",
        f"{business_type} directions {city}",
        f"open now {business_type} {city}"
    ]

    # Assign search volumes and difficulty
    all_keywords = base_patterns + service_keywords + long_tail
    keyword_data = []

    competition_multiplier = {"Low": 1.5, "Medium": 1.0, "High": 0.7}
    size_multiplier = {"Local": 0.8, "Regional": 1.0, "National Chain": 1.2}

    base_volume = competition_multiplier[competition] * size_multiplier[size]

    for keyword in all_keywords:
        # Simulate search volume and difficulty
        volume = int(random.randint(50, 2000) * base_volume)
        difficulty = random.randint(20, 80)

        # Adjust difficulty based on competition
        if competition == "High":
            difficulty += 20
        elif competition == "Low":
            difficulty -= 15

        difficulty = max(10, min(90, difficulty))  # Keep within bounds

        keyword_data.append({
            'keyword': keyword,
            'volume': volume,
            'difficulty': difficulty,
            'type': get_keyword_type(keyword)
        })

    # Sort by volume descending
    keyword_data.sort(key=lambda x: x['volume'], reverse=True)

    return {
        'keywords': keyword_data,
        'location': location,
        'business_type': business_type,
        'total_keywords': len(keyword_data)
    }


def get_keyword_type(keyword):
    """Categorize keyword type"""
    if 'near me' in keyword.lower() or 'nearby' in keyword.lower():
        return 'Near Me'
    elif 'best' in keyword.lower() or 'top' in keyword.lower():
        return 'Quality'
    elif 'phone' in keyword.lower() or 'directions' in keyword.lower():
        return 'Contact'
    elif 'emergency' in keyword.lower() or '24' in keyword.lower():
        return 'Urgent'
    elif 'reviews' in keyword.lower() or 'rating' in keyword.lower():
        return 'Reviews'
    else:
        return 'General'


def display_local_keywords(data):
    """Display local keyword research results"""
    st.markdown("### 🔍 Local Keyword Results")

    # Summary
    st.write(f"**Business:** {data['business_type'].title()}")
    st.write(f"**Location:** {data['location']}")
    st.write(f"**Total Keywords:** {data['total_keywords']}")

    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        volume_filter = st.selectbox("Minimum Search Volume:", [0, 100, 500, 1000])
    with col2:
        difficulty_filter = st.selectbox("Maximum Difficulty:", [90, 70, 50, 30])

    # Filter keywords
    filtered_keywords = [
        kw for kw in data['keywords']
        if kw['volume'] >= volume_filter and kw['difficulty'] <= difficulty_filter
    ]

    # Display keywords table
    st.markdown("### 📊 Keyword Opportunities")

    if filtered_keywords:
        for i, kw in enumerate(filtered_keywords[:20], 1):  # Show top 20
            with st.expander(f"{i}. {kw['keyword']} ({kw['volume']} searches)"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Search Volume", f"{kw['volume']:,}")
                with col2:
                    if kw['difficulty'] <= 30:
                        st.success(f"Difficulty: {kw['difficulty']}")
                    elif kw['difficulty'] <= 60:
                        st.warning(f"Difficulty: {kw['difficulty']}")
                    else:
                        st.error(f"Difficulty: {kw['difficulty']}")
                with col3:
                    st.info(f"Type: {kw['type']}")
    else:
        st.info("No keywords match your filters. Try adjusting the criteria.")

    # Keyword type breakdown
    st.markdown("### 📈 Keyword Type Distribution")
    type_counts = {}
    for kw in data['keywords']:
        type_counts[kw['type']] = type_counts.get(kw['type'], 0) + 1

    for kw_type, count in type_counts.items():
        st.write(f"**{kw_type}:** {count} keywords")


def review_generator():
    """Review response generator"""
    create_tool_header("Review Generator", "Generate responses to customer reviews", "⭐")

    st.markdown("### Review Response Generator")

    # Review details
    col1, col2 = st.columns(2)
    with col1:
        review_rating = st.selectbox("Review Rating:", ["5 stars", "4 stars", "3 stars", "2 stars", "1 star"])
        review_platform = st.selectbox("Platform:", ["Google", "Yelp", "Facebook", "TripAdvisor", "Other"])
        business_name = st.text_input("Business Name:", placeholder="Your Business Name")

    with col2:
        response_tone = st.selectbox("Response Tone:", ["Professional", "Friendly", "Apologetic", "Grateful"])
        customer_name = st.text_input("Customer Name (optional):", placeholder="John")
        include_offer = st.checkbox("Include special offer/discount")

    # Review content
    review_text = st.text_area("Customer Review:",
                               placeholder="Enter the customer's review text here...",
                               height=150)

    # Additional context
    issue_resolution = st.text_area("How was the issue resolved? (for negative reviews):",
                                    placeholder="Describe any steps taken to resolve the issue")

    if st.button("Generate Response"):
        if review_text and business_name:
            response = generate_review_response(review_rating, review_platform, business_name,
                                                response_tone, customer_name, include_offer,
                                                review_text, issue_resolution)
            display_review_response(response)
        else:
            st.error("Please fill in the review text and business name")


def generate_review_response(rating, platform, business_name, tone, customer_name,
                             include_offer, review_text, resolution):
    """Generate appropriate review response"""

    # Determine if positive or negative review
    stars = int(rating.split()[0])
    is_positive = stars >= 4

    # Greeting templates
    if customer_name:
        greeting = f"Hi {customer_name},"
    else:
        greeting = "Hello,"

    # Response templates based on rating and tone
    if is_positive:
        if tone == "Grateful":
            responses = [
                f"{greeting}\n\nThank you so much for taking the time to leave this wonderful review! We're thrilled to hear about your positive experience with {business_name}.",
                f"{greeting}\n\nWe're absolutely delighted by your {stars}-star review! Your feedback means the world to us at {business_name}.",
                f"{greeting}\n\nWhat a fantastic review! We're so grateful for customers like you who make our work at {business_name} so rewarding."
            ]
        elif tone == "Professional":
            responses = [
                f"{greeting}\n\nThank you for your {stars}-star review of {business_name}. We appreciate you taking the time to share your positive experience.",
                f"{greeting}\n\nWe're pleased to hear that you had a positive experience with {business_name}. Thank you for your feedback.",
                f"{greeting}\n\nThank you for choosing {business_name} and for sharing your experience. We value your business."
            ]
        else:  # Friendly
            responses = [
                f"{greeting}\n\nWow, thank you for this amazing review! We're so happy you loved your experience at {business_name}!",
                f"{greeting}\n\nThis review just made our day! Thanks for being such an awesome customer of {business_name}.",
                f"{greeting}\n\nYour review put a huge smile on our faces! We love serving customers like you at {business_name}."
            ]
    else:
        # Negative review responses
        if tone == "Apologetic":
            responses = [
                f"{greeting}\n\nWe sincerely apologize for the experience you had at {business_name}. This is not the level of service we strive to provide.",
                f"{greeting}\n\nThank you for bringing this to our attention. We're truly sorry that your experience with {business_name} didn't meet your expectations.",
                f"{greeting}\n\nWe're genuinely sorry to hear about your disappointing experience. Your feedback is valuable to {business_name}."
            ]
        elif tone == "Professional":
            responses = [
                f"{greeting}\n\nThank you for your feedback regarding your experience with {business_name}. We take all customer concerns seriously.",
                f"{greeting}\n\nWe appreciate you taking the time to share your experience with {business_name}. We'd like to address your concerns.",
                f"{greeting}\n\nThank you for your review. We value your feedback and would like the opportunity to improve your experience with {business_name}."
            ]
        else:  # Friendly
            responses = [
                f"{greeting}\n\nOh no! We're so sorry your experience with {business_name} wasn't what you hoped for. We'd love to make this right!",
                f"{greeting}\n\nYikes! This definitely isn't the experience we want our customers to have at {business_name}. Let us fix this!",
                f"{greeting}\n\nWe're bummed to hear about your experience! This isn't typical for {business_name}, and we want to turn this around."
            ]

    # Select a random response template
    base_response = random.choice(responses)

    # Add resolution information for negative reviews
    if not is_positive and resolution:
        base_response += f"\n\n{resolution}"

    # Add offer if requested
    if include_offer:
        offer_text = "\n\nWe'd love to invite you back with a special 15% discount on your next visit. Please contact us directly to redeem this offer."
        base_response += offer_text

    # Add closing
    if is_positive:
        closings = [
            f"\n\nWe look forward to serving you again soon!\n\nBest regards,\nThe {business_name} Team",
            f"\n\nThanks again for being such a valued customer!\n\nWarm regards,\n{business_name}",
            f"\n\nWe can't wait to see you again!\n\nSincerely,\nEveryone at {business_name}"
        ]
    else:
        closings = [
            f"\n\nPlease don't hesitate to contact us directly so we can make this right.\n\nSincerely,\nThe {business_name} Team",
            f"\n\nWe'd appreciate the chance to discuss this further and improve your experience.\n\nBest regards,\n{business_name}",
            f"\n\nYour satisfaction is our priority, and we hope to hear from you soon.\n\nRespectfully,\nThe {business_name} Team"
        ]

    base_response += random.choice(closings)

    return {
        'response': base_response,
        'rating': rating,
        'tone': tone,
        'is_positive': is_positive,
        'platform': platform
    }


def display_review_response(response_data):
    """Display generated review response"""
    st.markdown("### 💬 Generated Response")

    # Response preview
    st.text_area("Response:", response_data['response'], height=300)

    # Response details
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**Rating:** {response_data['rating']}")
    with col2:
        st.info(f"**Tone:** {response_data['tone']}")
    with col3:
        if response_data['is_positive']:
            st.success("**Type:** Positive")
        else:
            st.warning("**Type:** Negative")

    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Copy Response"):
            st.success("Response copied to clipboard! (simulation)")

    with col2:
        if st.button("Generate New Response"):
            st.info("Click 'Generate Response' above for a new version")

    # Tips
    st.markdown("### 💡 Response Tips")
    tips = [
        "Respond to reviews within 24-48 hours when possible",
        "Keep responses professional and on-brand",
        "Address specific points mentioned in the review",
        "For negative reviews, take the conversation offline when appropriate",
        "Thank customers for taking the time to leave feedback"
    ]

    for tip in tips:
        st.write(f"• {tip}")


def nap_consistency():
    """NAP consistency checker"""
    create_tool_header("NAP Consistency", "Check Name, Address, Phone consistency across platforms", "📋")

    st.markdown("### NAP Consistency Checker")
    st.info(
        "NAP (Name, Address, Phone) consistency is crucial for local SEO. Inconsistent information confuses search engines and customers.")

    # Master NAP information
    st.markdown("#### Master Business Information")
    col1, col2 = st.columns(2)
    with col1:
        master_name = st.text_input("Official Business Name:", placeholder="ABC Company LLC")
        master_phone = st.text_input("Official Phone Number:", placeholder="+1-555-123-4567")
    with col2:
        master_address = st.text_area("Official Address:",
                                      placeholder="123 Main Street\nSuite 100\nNew York, NY 10001")
        master_website = st.text_input("Official Website:", placeholder="https://abccompany.com")

    # Platform NAP variations
    st.markdown("#### Check NAP Across Platforms")

    platforms_to_check = st.multiselect("Select platforms to simulate checking:",
                                        ["Google My Business", "Yelp", "Facebook", "Yellow Pages",
                                         "Bing Places", "Apple Maps", "Foursquare", "BBB"])

    if st.button("Check NAP Consistency"):
        if master_name and master_phone and master_address and platforms_to_check:
            consistency_results = simulate_nap_check(master_name, master_phone, master_address,
                                                     master_website, platforms_to_check)
            display_nap_results(consistency_results)
        else:
            st.error("Please fill in all master information and select platforms to check")


def simulate_nap_check(name, phone, address, website, platforms):
    """Simulate NAP consistency check across platforms"""

    # Common variations for simulation
    name_variations = [name, name.replace("LLC", "").strip(), name.replace("Inc.", "").strip()]
    phone_variations = [phone, phone.replace("-", ""), phone.replace("+1-", ""), phone.replace(" ", "")]

    # Split address for variations
    address_lines = address.split('\n')
    address_variations = [
        address,
        address.replace("Street", "St").replace("Avenue", "Ave"),
        '\n'.join(address_lines[:2]),  # Without suite
        address.replace(",", "")
    ]

    results = []
    issues_found = []

    for platform in platforms:
        # Simulate finding variations
        platform_name = random.choice(name_variations)
        platform_phone = random.choice(phone_variations)
        platform_address = random.choice(address_variations)

        # Check for inconsistencies
        name_match = platform_name.strip().lower() == name.strip().lower()
        phone_match = ''.join(filter(str.isdigit, platform_phone)) == ''.join(filter(str.isdigit, phone))
        address_match = platform_address.replace(" ", "").lower() == address.replace(" ", "").lower()

        # Introduce some random inconsistencies for demo
        if random.random() < 0.3:  # 30% chance of inconsistency
            inconsistency_type = random.choice(['name', 'phone', 'address'])
            if inconsistency_type == 'name':
                name_match = False
                platform_name += " & Co"
            elif inconsistency_type == 'phone':
                phone_match = False
                platform_phone = platform_phone[:-1] + str(random.randint(0, 9))
            else:
                address_match = False
                platform_address = platform_address.replace("123", "124")

        platform_result = {
            'platform': platform,
            'name': platform_name,
            'phone': platform_phone,
            'address': platform_address,
            'name_match': name_match,
            'phone_match': phone_match,
            'address_match': address_match,
            'overall_match': name_match and phone_match and address_match
        }

        results.append(platform_result)

        # Collect issues
        if not name_match:
            issues_found.append(f"{platform}: Business name mismatch")
        if not phone_match:
            issues_found.append(f"{platform}: Phone number mismatch")
        if not address_match:
            issues_found.append(f"{platform}: Address mismatch")

    # Calculate consistency score
    total_checks = len(results) * 3  # 3 fields per platform
    consistent_checks = sum(1 for r in results for field in ['name_match', 'phone_match', 'address_match'] if r[field])
    consistency_score = (consistent_checks / total_checks * 100) if total_checks > 0 else 0

    return {
        'master_info': {'name': name, 'phone': phone, 'address': address, 'website': website},
        'results': results,
        'issues': issues_found,
        'consistency_score': consistency_score,
        'total_platforms': len(platforms)
    }


def display_nap_results(data):
    """Display NAP consistency results"""
    st.markdown("### 📊 NAP Consistency Results")

    # Overall score
    col1, col2, col3 = st.columns(3)
    with col1:
        if data['consistency_score'] >= 95:
            st.success(f"Consistency Score: {data['consistency_score']:.1f}%")
        elif data['consistency_score'] >= 80:
            st.warning(f"Consistency Score: {data['consistency_score']:.1f}%")
        else:
            st.error(f"Consistency Score: {data['consistency_score']:.1f}%")

    with col2:
        consistent_platforms = sum(1 for r in data['results'] if r['overall_match'])
        st.metric("Consistent Platforms", f"{consistent_platforms}/{data['total_platforms']}")

    with col3:
        st.metric("Issues Found", len(data['issues']))

    # Platform breakdown
    st.markdown("### 🏢 Platform Analysis")

    for result in data['results']:
        with st.expander(f"{result['platform']} - {'✅ Consistent' if result['overall_match'] else '❌ Issues Found'}"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Found Information:**")
                st.write(f"**Name:** {result['name']}")
                st.write(f"**Phone:** {result['phone']}")
                st.write(f"**Address:** {result['address']}")

            with col2:
                st.markdown("**Consistency Check:**")
                st.write(f"**Name:** {'✅' if result['name_match'] else '❌'}")
                st.write(f"**Phone:** {'✅' if result['phone_match'] else '❌'}")
                st.write(f"**Address:** {'✅' if result['address_match'] else '❌'}")

    # Issues summary
    if data['issues']:
        st.markdown("### ⚠️ Issues Found")
        for issue in data['issues']:
            st.error(f"❌ {issue}")

    # Recommendations
    st.markdown("### 💡 Recommendations")

    recommendations = []
    if data['consistency_score'] < 100:
        recommendations.extend([
            "📝 Update inconsistent listings to match your master NAP information",
            "🔍 Use exact same format across all platforms",
            "📞 Standardize phone number format (e.g., +1-555-123-4567)",
            "🏠 Use complete address including suite/unit numbers"
        ])

    if data['consistency_score'] < 80:
        recommendations.extend([
            "⚡ Prioritize fixing high-authority platforms first (Google, Yelp, Facebook)",
            "🔄 Set up monitoring to catch future inconsistencies",
            "📋 Create a master reference document for your team"
        ])

    if not recommendations:
        recommendations.append("🎉 Your NAP information is consistent across all checked platforms!")

    for rec in recommendations:
        st.write(f"• {rec}")


# TECHNICAL SEO TOOLS

def sitemap_validator():
    """XML sitemap validator tool"""
    create_tool_header("Sitemap Validator", "Validate and analyze XML sitemaps", "🗺️")

    st.markdown("### XML Sitemap Validator")

    # Input method selection
    input_method = st.radio("How would you like to provide the sitemap?",
                            ["URL", "Upload File", "Paste XML"])

    sitemap_content = ""
    sitemap_url = ""

    if input_method == "URL":
        sitemap_url = st.text_input("Sitemap URL:", placeholder="https://example.com/sitemap.xml")
        if sitemap_url and st.button("Fetch Sitemap"):
            # Simulate fetching sitemap
            st.info("Fetching sitemap... (simulation)")
            sitemap_content = simulate_sitemap_content(sitemap_url)

    elif input_method == "Upload File":
        uploaded_file = FileHandler.upload_files(['xml'], accept_multiple=False)
        if uploaded_file:
            st.success("✅ Sitemap file uploaded successfully!")
            sitemap_content = simulate_sitemap_content("uploaded file")

    else:  # Paste XML
        sitemap_content = st.text_area("Paste XML sitemap content:", height=200)

    if sitemap_content and st.button("Validate Sitemap"):
        validation_results = validate_sitemap(sitemap_content, sitemap_url)
        display_sitemap_validation(validation_results)


def simulate_sitemap_content(source):
    """Simulate sitemap content for demonstration"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://example.com/</loc>
        <lastmod>2024-01-15</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://example.com/about</loc>
        <lastmod>2024-01-10</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://example.com/contact</loc>
        <lastmod>2024-01-05</lastmod>
        <changefreq>yearly</changefreq>
        <priority>0.5</priority>
    </url>
</urlset>"""


def validate_sitemap(content, url=""):
    """Validate XML sitemap structure and content"""

    issues = []
    warnings = []
    stats = {
        'total_urls': 0,
        'valid_urls': 0,
        'unique_urls': 0,
        'has_lastmod': 0,
        'has_priority': 0,
        'has_changefreq': 0
    }

    # Simulate XML parsing and validation
    import re

    # Count URLs
    url_matches = re.findall(r'<url>', content)
    stats['total_urls'] = len(url_matches)

    # Check for valid XML structure
    if not content.strip().startswith('<?xml'):
        issues.append("Missing XML declaration")

    if 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"' not in content:
        issues.append("Missing or incorrect sitemap namespace")

    # Check URL structure
    loc_matches = re.findall(r'<loc>(.*?)</loc>', content)
    valid_urls = 0
    unique_urls = set()

    for loc in loc_matches:
        if loc.startswith('http'):
            valid_urls += 1
            unique_urls.add(loc)
        else:
            issues.append(f"Invalid URL format: {loc}")

    stats['valid_urls'] = valid_urls
    stats['unique_urls'] = len(unique_urls)

    # Check for duplicates
    if len(unique_urls) != len(loc_matches):
        warnings.append("Duplicate URLs found in sitemap")

    # Count optional elements
    stats['has_lastmod'] = len(re.findall(r'<lastmod>', content))
    stats['has_priority'] = len(re.findall(r'<priority>', content))
    stats['has_changefreq'] = len(re.findall(r'<changefreq>', content))

    # Check file size (simulate)
    estimated_size = len(content.encode('utf-8'))
    if estimated_size > 50 * 1024 * 1024:  # 50MB limit
        issues.append("Sitemap exceeds 50MB size limit")

    if stats['total_urls'] > 50000:
        issues.append("Sitemap contains more than 50,000 URLs")

    # Additional checks
    if stats['total_urls'] == 0:
        issues.append("No URLs found in sitemap")

    # Check for common issues
    if '/robots.txt' in content:
        warnings.append("Robots.txt URL found in sitemap (not recommended)")

    # Calculate score
    score = 100
    score -= len(issues) * 10
    score -= len(warnings) * 5
    score = max(0, score)

    return {
        'score': score,
        'issues': issues,
        'warnings': warnings,
        'stats': stats,
        'is_valid': len(issues) == 0
    }


def display_sitemap_validation(results):
    """Display sitemap validation results"""
    st.markdown("### 📊 Sitemap Validation Results")

    # Overall status
    col1, col2, col3 = st.columns(3)
    with col1:
        if results['is_valid']:
            st.success("✅ Valid Sitemap")
        else:
            st.error("❌ Invalid Sitemap")

    with col2:
        if results['score'] >= 80:
            st.success(f"Score: {results['score']}/100")
        elif results['score'] >= 60:
            st.warning(f"Score: {results['score']}/100")
        else:
            st.error(f"Score: {results['score']}/100")

    with col3:
        st.metric("Total URLs", results['stats']['total_urls'])

    # Statistics
    st.markdown("### 📈 Sitemap Statistics")
    stats = results['stats']

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Valid URLs", f"{stats['valid_urls']}/{stats['total_urls']}")
        st.metric("Unique URLs", stats['unique_urls'])

    with col2:
        st.metric("URLs with lastmod", stats['has_lastmod'])
        st.metric("URLs with priority", stats['has_priority'])

    # Issues
    if results['issues']:
        st.markdown("### ❌ Critical Issues")
        for issue in results['issues']:
            st.error(f"❌ {issue}")

    # Warnings
    if results['warnings']:
        st.markdown("### ⚠️ Warnings")
        for warning in results['warnings']:
            st.warning(f"⚠️ {warning}")

    # Recommendations
    st.markdown("### 💡 Recommendations")
    recommendations = []

    if stats['has_lastmod'] < stats['total_urls']:
        recommendations.append("Add <lastmod> dates to all URLs for better crawling")

    if stats['has_priority'] < stats['total_urls']:
        recommendations.append("Consider adding <priority> values to guide search engines")

    if not results['issues'] and not results['warnings']:
        recommendations.append("🎉 Your sitemap looks great! Submit it to Google Search Console")

    recommendations.extend([
        "Test sitemap accessibility in robots.txt",
        "Monitor sitemap in Google Search Console for errors",
        "Update sitemap regularly when adding new content"
    ])

    for rec in recommendations:
        st.write(f"• {rec}")


def canonical_url_checker():
    """Canonical URL checker tool"""
    create_tool_header("Canonical URL Checker", "Check canonical URL implementation", "🔗")

    st.markdown("### Canonical URL Checker")

    # Input URLs
    st.markdown("#### URLs to Check")
    url_input_method = st.radio("How would you like to input URLs?",
                                ["Single URL", "Multiple URLs", "Upload File"])

    urls_to_check = []

    if url_input_method == "Single URL":
        single_url = st.text_input("URL to check:", placeholder="https://example.com/page")
        if single_url:
            urls_to_check = [single_url]

    elif url_input_method == "Multiple URLs":
        multiple_urls = st.text_area("Enter URLs (one per line):",
                                     placeholder="https://example.com/page1\nhttps://example.com/page2",
                                     height=150)
        if multiple_urls:
            urls_to_check = [url.strip() for url in multiple_urls.split('\n') if url.strip()]

    else:  # Upload File
        uploaded_file = FileHandler.upload_files(['txt', 'csv'], accept_multiple=False)
        if uploaded_file:
            st.success("✅ File uploaded successfully!")
            urls_to_check = simulate_url_list()

    if urls_to_check and st.button("Check Canonical URLs"):
        canonical_results = check_canonical_urls(urls_to_check)
        display_canonical_results(canonical_results)


def simulate_url_list():
    """Simulate URL list for demonstration"""
    return [
        "https://example.com/",
        "https://example.com/about",
        "https://example.com/products",
        "https://example.com/contact",
        "https://example.com/blog"
    ]


def check_canonical_urls(urls):
    """Check canonical URL implementation for given URLs"""

    results = []
    issues = []

    for url in urls:
        # Simulate checking canonical URL
        has_canonical = random.choice([True, False])
        is_self_referencing = random.choice([True, False]) if has_canonical else False
        is_https = url.startswith('https://')

        # Generate canonical URL
        if has_canonical:
            if is_self_referencing:
                canonical_url = url
            else:
                # Simulate different canonical URL
                canonical_url = url.replace('http://', 'https://') if not is_https else url + '?ref=canonical'
        else:
            canonical_url = None

        # Check for issues
        url_issues = []
        if not has_canonical:
            url_issues.append("No canonical URL specified")
        elif not is_self_referencing:
            url_issues.append("Canonical URL differs from current URL")

        if not is_https and canonical_url and canonical_url.startswith('https://'):
            url_issues.append("HTTP page canonicalizes to HTTPS")

        # Simulate additional checks
        if random.random() < 0.1:  # 10% chance
            url_issues.append("Canonical URL returns 404")

        if random.random() < 0.05:  # 5% chance
            url_issues.append("Multiple canonical tags found")

        result = {
            'url': url,
            'has_canonical': has_canonical,
            'canonical_url': canonical_url,
            'is_self_referencing': is_self_referencing,
            'is_https': is_https,
            'issues': url_issues,
            'status': 'Good' if not url_issues else 'Issues Found'
        }

        results.append(result)
        issues.extend(url_issues)

    # Calculate summary stats
    total_urls = len(urls)
    urls_with_canonical = sum(1 for r in results if r['has_canonical'])
    self_referencing = sum(1 for r in results if r['is_self_referencing'])
    problematic_urls = sum(1 for r in results if r['issues'])

    return {
        'results': results,
        'summary': {
            'total_urls': total_urls,
            'with_canonical': urls_with_canonical,
            'self_referencing': self_referencing,
            'problematic': problematic_urls
        },
        'all_issues': list(set(issues))
    }


def display_canonical_results(data):
    """Display canonical URL check results"""
    st.markdown("### 📊 Canonical URL Analysis")

    # Summary metrics
    summary = data['summary']
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total URLs", summary['total_urls'])
    with col2:
        st.metric("With Canonical", f"{summary['with_canonical']}/{summary['total_urls']}")
    with col3:
        st.metric("Self-Referencing", summary['self_referencing'])
    with col4:
        if summary['problematic'] == 0:
            st.success(f"Issues: {summary['problematic']}")
        else:
            st.error(f"Issues: {summary['problematic']}")

    # URL-by-URL results
    st.markdown("### 🔍 Detailed Results")

    for i, result in enumerate(data['results'], 1):
        status_icon = "✅" if result['status'] == 'Good' else "❌"

        with st.expander(f"{i}. {status_icon} {result['url']}"):
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Has Canonical:** {'✅' if result['has_canonical'] else '❌'}")
                st.write(f"**Self-Referencing:** {'✅' if result['is_self_referencing'] else '❌'}")
                st.write(f"**HTTPS:** {'✅' if result['is_https'] else '❌'}")

            with col2:
                if result['canonical_url']:
                    st.write(f"**Canonical URL:** {result['canonical_url']}")
                else:
                    st.write("**Canonical URL:** Not specified")

            if result['issues']:
                st.markdown("**Issues Found:**")
                for issue in result['issues']:
                    st.error(f"❌ {issue}")

    # Common issues summary
    if data['all_issues']:
        st.markdown("### ⚠️ Common Issues Found")
        for issue in data['all_issues']:
            st.warning(f"⚠️ {issue}")

    # Recommendations
    st.markdown("### 💡 Recommendations")
    recommendations = [
        "Add canonical URLs to all pages to prevent duplicate content issues",
        "Use self-referencing canonical URLs for most pages",
        "Ensure canonical URLs use HTTPS when available",
        "Avoid chains of canonical redirects",
        "Test canonical URLs to ensure they return 200 status codes"
    ]

    if summary['problematic'] == 0:
        recommendations.insert(0, "🎉 All canonical URLs look good!")

    for rec in recommendations:
        st.write(f"• {rec}")


def redirect_checker():
    """Redirect checker tool"""
    create_tool_header("Redirect Checker", "Check URL redirects and redirect chains", "↪️")

    st.markdown("### Redirect Checker")

    # Input method
    check_type = st.selectbox("Check Type:",
                              ["Single URL", "Redirect Chain", "Bulk URLs", "Sitemap URLs"])

    urls_to_check = []

    if check_type == "Single URL":
        single_url = st.text_input("URL to check:", placeholder="https://example.com/old-page")
        if single_url:
            urls_to_check = [single_url]

    elif check_type == "Redirect Chain":
        chain_url = st.text_input("Starting URL:", placeholder="https://example.com/start")
        if chain_url:
            urls_to_check = [chain_url]

    elif check_type == "Bulk URLs":
        bulk_urls = st.text_area("Enter URLs (one per line):",
                                 placeholder="https://example.com/url1\nhttps://example.com/url2",
                                 height=150)
        if bulk_urls:
            urls_to_check = [url.strip() for url in bulk_urls.split('\n') if url.strip()]

    else:  # Sitemap URLs
        sitemap_url = st.text_input("Sitemap URL:", placeholder="https://example.com/sitemap.xml")
        if sitemap_url:
            st.info("Would extract URLs from sitemap for checking")
            urls_to_check = simulate_sitemap_urls()

    # Advanced options
    with st.expander("Advanced Options"):
        follow_redirects = st.checkbox("Follow redirect chains", value=True)
        max_redirects = st.number_input("Max redirects to follow:", min_value=1, max_value=10, value=5)
        check_internal_only = st.checkbox("Check internal redirects only")

    if urls_to_check and st.button("Check Redirects"):
        redirect_results = check_redirects(urls_to_check, follow_redirects, max_redirects)
        display_redirect_results(redirect_results)


def simulate_sitemap_urls():
    """Simulate URLs from sitemap"""
    return [
        "https://example.com/old-page",
        "https://example.com/moved-content",
        "https://example.com/redirected-post",
        "https://example.com/archived-page"
    ]


def check_redirects(urls, follow_chains=True, max_redirects=5):
    """Check redirects for given URLs"""

    results = []
    issues = []
    redirect_types = ['301', '302', '307', '308', '200', '404', '500']

    for url in urls:
        # Simulate redirect checking
        redirect_chain = []
        current_url = url

        # Simulate redirect chain
        chain_length = random.randint(0, 3) if follow_chains else random.randint(0, 1)

        for i in range(chain_length + 1):
            status_code = random.choice(redirect_types)

            if status_code in ['301', '302', '307', '308'] and i < max_redirects:
                # Simulate redirect
                if i == 0:
                    next_url = current_url.replace('old-', 'new-')
                else:
                    next_url = current_url + f'-final'

                redirect_chain.append({
                    'url': current_url,
                    'status_code': status_code,
                    'redirect_to': next_url,
                    'step': i + 1
                })
                current_url = next_url
            else:
                # Final destination
                redirect_chain.append({
                    'url': current_url,
                    'status_code': status_code,
                    'redirect_to': None,
                    'step': i + 1
                })
                break

        # Analyze chain
        chain_issues = []
        final_status = redirect_chain[-1]['status_code']
        chain_length = len([r for r in redirect_chain if r['redirect_to']])

        if chain_length > 3:
            chain_issues.append("Long redirect chain (>3 redirects)")

        if '302' in [r['status_code'] for r in redirect_chain]:
            chain_issues.append("Uses temporary redirect (302) - consider permanent (301)")

        if final_status == '404':
            chain_issues.append("Redirect leads to 404 page")
        elif final_status in ['500', '503']:
            chain_issues.append("Redirect leads to server error")

        # Check for redirect loops (simulation)
        if chain_length > 2 and random.random() < 0.1:
            chain_issues.append("Potential redirect loop detected")

        result = {
            'original_url': url,
            'redirect_chain': redirect_chain,
            'final_url': redirect_chain[-1]['url'],
            'final_status': final_status,
            'chain_length': chain_length,
            'issues': chain_issues,
            'status': 'Good' if not chain_issues and final_status == '200' else 'Issues Found'
        }

        results.append(result)
        issues.extend(chain_issues)

    # Summary statistics
    total_urls = len(urls)
    redirecting_urls = sum(1 for r in results if r['chain_length'] > 0)
    problematic_urls = sum(1 for r in results if r['issues'])
    broken_redirects = sum(1 for r in results if r['final_status'] in ['404', '500', '503'])

    return {
        'results': results,
        'summary': {
            'total_urls': total_urls,
            'redirecting': redirecting_urls,
            'problematic': problematic_urls,
            'broken': broken_redirects
        },
        'all_issues': list(set(issues))
    }


def display_redirect_results(data):
    """Display redirect check results"""
    st.markdown("### 📊 Redirect Analysis Results")

    # Summary metrics
    summary = data['summary']
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total URLs", summary['total_urls'])
    with col2:
        st.metric("Redirecting", summary['redirecting'])
    with col3:
        st.metric("Problematic", summary['problematic'])
    with col4:
        if summary['broken'] == 0:
            st.success(f"Broken: {summary['broken']}")
        else:
            st.error(f"Broken: {summary['broken']}")

    # Detailed results
    st.markdown("### 🔍 Redirect Details")

    for i, result in enumerate(data['results'], 1):
        status_icon = "✅" if result['status'] == 'Good' else "❌"
        chain_info = f"({result['chain_length']} redirects)" if result['chain_length'] > 0 else "(no redirects)"

        with st.expander(f"{i}. {status_icon} {result['original_url']} {chain_info}"):

            # Redirect chain visualization
            if result['redirect_chain']:
                st.markdown("**Redirect Chain:**")
                for step in result['redirect_chain']:
                    if step['redirect_to']:
                        st.write(
                            f"Step {step['step']}: {step['url']} → **{step['status_code']}** → {step['redirect_to']}")
                    else:
                        st.write(f"Step {step['step']}: {step['url']} → **{step['status_code']}** (Final)")

            # Summary info
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Final URL:** {result['final_url']}")
                st.write(f"**Final Status:** {result['final_status']}")
            with col2:
                st.write(f"**Chain Length:** {result['chain_length']}")
                st.write(f"**Status:** {result['status']}")

            # Issues
            if result['issues']:
                st.markdown("**Issues Found:**")
                for issue in result['issues']:
                    st.error(f"❌ {issue}")

    # Common issues
    if data['all_issues']:
        st.markdown("### ⚠️ Common Issues")
        for issue in data['all_issues']:
            st.warning(f"⚠️ {issue}")

    # Recommendations
    st.markdown("### 💡 Recommendations")
    recommendations = [
        "Use 301 redirects for permanent moves to preserve SEO value",
        "Minimize redirect chains - ideally direct redirects only",
        "Fix broken redirects that lead to 404 or error pages",
        "Update internal links to point directly to final destinations",
        "Monitor redirects regularly for performance impact"
    ]

    if summary['problematic'] == 0:
        recommendations.insert(0, "🎉 All redirects are working properly!")

    for rec in recommendations:
        st.write(f"• {rec}")


# LINK BUILDING TOOLS

def backlink_analyzer():
    """Backlink analysis tool"""
    create_tool_header("Backlink Analyzer", "Analyze backlink profile and quality", "🔗")

    st.markdown("### Backlink Analyzer")

    # Domain input
    domain_to_analyze = st.text_input("Domain to analyze:", placeholder="example.com")

    # Analysis options
    col1, col2 = st.columns(2)
    with col1:
        analysis_depth = st.selectbox("Analysis Depth:", ["Quick Scan", "Standard", "Deep Analysis"])
        include_competitors = st.checkbox("Include competitor comparison")

    with col2:
        date_range = st.selectbox("Date Range:", ["Last 30 days", "Last 3 months", "Last 6 months", "Last year"])
        min_domain_authority = st.slider("Minimum Domain Authority:", 0, 100, 10)

    if domain_to_analyze and st.button("Analyze Backlinks"):
        backlink_data = analyze_backlinks(domain_to_analyze, analysis_depth, include_competitors,
                                          date_range, min_domain_authority)
        display_backlink_analysis(backlink_data)


def analyze_backlinks(domain, depth, include_competitors, date_range, min_da):
    """Analyze backlink profile for domain"""

    # Simulate backlink data
    total_backlinks = random.randint(100, 10000)
    referring_domains = random.randint(50, 1000)

    # Generate sample backlinks
    backlinks = []
    domain_authorities = []
    anchor_texts = []

    for i in range(min(50, total_backlinks)):  # Show top 50
        da = random.randint(max(min_da, 10), 100)
        domain_authorities.append(da)

        referring_domain = f"domain{i + 1}.com"
        anchor_text = random.choice([
            domain.replace('.com', ''),
            'click here',
            'read more',
            'website',
            f'best {domain.split(".")[0]}',
            f'{domain.split(".")[0]} services',
            domain
        ])
        anchor_texts.append(anchor_text)

        backlink = {
            'referring_domain': referring_domain,
            'domain_authority': da,
            'page_authority': random.randint(20, 80),
            'anchor_text': anchor_text,
            'link_type': random.choice(['dofollow', 'nofollow']),
            'first_seen': f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            'status': random.choice(['active', 'lost', 'new'])
        }
        backlinks.append(backlink)

    # Calculate metrics
    avg_da = sum(domain_authorities) / len(domain_authorities) if domain_authorities else 0
    dofollow_percentage = sum(1 for bl in backlinks if bl['link_type'] == 'dofollow') / len(backlinks) * 100

    # Anchor text distribution
    anchor_distribution = {}
    for anchor in anchor_texts:
        anchor_distribution[anchor] = anchor_distribution.get(anchor, 0) + 1

    # Sort by frequency
    top_anchors = sorted(anchor_distribution.items(), key=lambda x: x[1], reverse=True)[:10]

    # Competitor data (if requested)
    competitors = []
    if include_competitors:
        for i in range(3):
            competitors.append({
                'domain': f'competitor{i + 1}.com',
                'backlinks': random.randint(200, 5000),
                'referring_domains': random.randint(100, 800),
                'avg_da': random.randint(30, 70)
            })

    return {
        'domain': domain,
        'total_backlinks': total_backlinks,
        'referring_domains': referring_domains,
        'avg_domain_authority': avg_da,
        'dofollow_percentage': dofollow_percentage,
        'backlinks': backlinks,
        'top_anchors': top_anchors,
        'competitors': competitors,
        'link_velocity': random.randint(5, 50)  # links per month
    }


def display_backlink_analysis(data):
    """Display backlink analysis results"""
    st.markdown("### 📊 Backlink Profile Overview")

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Backlinks", f"{data['total_backlinks']:,}")
    with col2:
        st.metric("Referring Domains", f"{data['referring_domains']:,}")
    with col3:
        st.metric("Avg Domain Authority", f"{data['avg_domain_authority']:.1f}")
    with col4:
        st.metric("Dofollow %", f"{data['dofollow_percentage']:.1f}%")

    # Link quality assessment
    st.markdown("### 🎯 Link Quality Assessment")

    high_quality = sum(1 for bl in data['backlinks'] if bl['domain_authority'] >= 70)
    medium_quality = sum(1 for bl in data['backlinks'] if 40 <= bl['domain_authority'] < 70)
    low_quality = sum(1 for bl in data['backlinks'] if bl['domain_authority'] < 40)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success(f"High Quality (DA 70+): {high_quality}")
    with col2:
        st.warning(f"Medium Quality (DA 40-69): {medium_quality}")
    with col3:
        st.error(f"Low Quality (DA <40): {low_quality}")

    # Top backlinks
    st.markdown("### 🔗 Top Backlinks")

    for i, backlink in enumerate(data['backlinks'][:10], 1):
        with st.expander(f"{i}. {backlink['referring_domain']} (DA: {backlink['domain_authority']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Domain Authority:** {backlink['domain_authority']}")
                st.write(f"**Page Authority:** {backlink['page_authority']}")
                st.write(f"**Link Type:** {backlink['link_type']}")
            with col2:
                st.write(f"**Anchor Text:** {backlink['anchor_text']}")
                st.write(f"**First Seen:** {backlink['first_seen']}")
                st.write(f"**Status:** {backlink['status']}")

    # Anchor text analysis
    st.markdown("### 📝 Top Anchor Texts")
    for anchor, count in data['top_anchors']:
        percentage = (count / len(data['backlinks'])) * 100
        st.write(f"**{anchor}:** {count} times ({percentage:.1f}%)")

    # Competitor comparison
    if data['competitors']:
        st.markdown("### 🏆 Competitor Comparison")
        for comp in data['competitors']:
            with st.expander(f"{comp['domain']}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Backlinks", f"{comp['backlinks']:,}")
                with col2:
                    st.metric("Referring Domains", f"{comp['referring_domains']:,}")
                with col3:
                    st.metric("Avg DA", f"{comp['avg_da']}")

    # Recommendations
    st.markdown("### 💡 Recommendations")
    recommendations = []

    if data['avg_domain_authority'] < 40:
        recommendations.append("🎯 Focus on acquiring high-authority backlinks (DA 50+)")

    if data['dofollow_percentage'] < 70:
        recommendations.append("⚡ Increase dofollow link percentage through quality content")

    recommendations.extend([
        "📈 Monitor link velocity and avoid sudden spikes",
        "🔍 Disavow toxic or spam backlinks",
        "📊 Track competitor backlink strategies",
        "🎨 Diversify anchor text distribution"
    ])

    for rec in recommendations:
        st.write(f"• {rec}")


def anchor_text_analyzer():
    """Anchor text distribution analyzer"""
    create_tool_header("Anchor Text Analyzer", "Analyze anchor text distribution and optimization", "⚓")

    st.markdown("### Anchor Text Analyzer")

    # Input method
    input_method = st.radio("Input Method:", ["Manual Entry", "Upload File", "Domain Analysis"])

    anchor_data = []

    if input_method == "Manual Entry":
        st.markdown("#### Enter Anchor Texts")
        num_anchors = st.number_input("Number of anchor texts to analyze:", min_value=1, max_value=50, value=5)

        for i in range(num_anchors):
            col1, col2 = st.columns(2)
            with col1:
                anchor = st.text_input(f"Anchor Text {i + 1}:", key=f"anchor_{i}")
            with col2:
                count = st.number_input(f"Count {i + 1}:", min_value=1, value=1, key=f"count_{i}")

            if anchor:
                anchor_data.append({'text': anchor, 'count': count})

    elif input_method == "Upload File":
        uploaded_file = FileHandler.upload_files(['csv', 'txt'], accept_multiple=False)
        if uploaded_file:
            st.success("✅ File uploaded successfully!")
            anchor_data = simulate_anchor_data()

    else:  # Domain Analysis
        domain = st.text_input("Domain to analyze:", placeholder="example.com")
        if domain:
            anchor_data = simulate_domain_anchors(domain)

    if anchor_data and st.button("Analyze Anchor Text Distribution"):
        analysis_results = analyze_anchor_distribution(anchor_data)
        display_anchor_analysis(analysis_results)


def simulate_anchor_data():
    """Simulate anchor text data for demonstration"""
    return [
        {'text': 'click here', 'count': 45},
        {'text': 'example.com', 'count': 38},
        {'text': 'website', 'count': 32},
        {'text': 'best services', 'count': 28},
        {'text': 'read more', 'count': 25},
        {'text': 'example', 'count': 22},
        {'text': 'visit site', 'count': 18},
        {'text': 'homepage', 'count': 15},
        {'text': 'learn more', 'count': 12},
        {'text': 'company', 'count': 10}
    ]


def simulate_domain_anchors(domain):
    """Simulate anchor text data for a domain"""
    domain_name = domain.split('.')[0]
    return [
        {'text': domain, 'count': random.randint(20, 50)},
        {'text': domain_name, 'count': random.randint(15, 40)},
        {'text': f'best {domain_name}', 'count': random.randint(10, 30)},
        {'text': 'click here', 'count': random.randint(25, 45)},
        {'text': 'website', 'count': random.randint(15, 35)},
        {'text': f'{domain_name} services', 'count': random.randint(8, 25)},
        {'text': 'read more', 'count': random.randint(10, 20)},
        {'text': 'visit site', 'count': random.randint(5, 15)}
    ]


def analyze_anchor_distribution(anchor_data):
    """Analyze anchor text distribution and provide recommendations"""

    # Calculate total links
    total_links = sum(item['count'] for item in anchor_data)

    # Calculate percentages and categorize
    analyzed_anchors = []
    categories = {
        'exact_match': 0,
        'partial_match': 0,
        'branded': 0,
        'generic': 0,
        'naked_url': 0
    }

    # Assume first domain for categorization (simplified)
    brand_name = "example"  # Would be extracted from actual domain

    for item in anchor_data:
        percentage = (item['count'] / total_links) * 100

        # Categorize anchor text
        text_lower = item['text'].lower()
        category = 'generic'  # default

        if brand_name in text_lower:
            category = 'branded'
            categories['branded'] += item['count']
        elif 'http' in text_lower or '.com' in text_lower:
            category = 'naked_url'
            categories['naked_url'] += item['count']
        elif any(word in text_lower for word in ['click', 'here', 'read', 'more', 'visit', 'website']):
            category = 'generic'
            categories['generic'] += item['count']
        else:
            # Assume keyword-rich
            if len(text_lower.split()) > 1:
                category = 'partial_match'
                categories['partial_match'] += item['count']
            else:
                category = 'exact_match'
                categories['exact_match'] += item['count']

        analyzed_anchors.append({
            'text': item['text'],
            'count': item['count'],
            'percentage': percentage,
            'category': category
        })

    # Calculate category percentages
    category_percentages = {k: (v / total_links) * 100 for k, v in categories.items()}

    # Risk assessment
    risk_factors = []
    risk_level = "Low"

    if category_percentages['exact_match'] > 15:
        risk_factors.append("High percentage of exact match anchors (>15%)")
        risk_level = "High"

    if category_percentages['partial_match'] > 25:
        risk_factors.append("High percentage of partial match anchors (>25%)")
        risk_level = "Medium" if risk_level == "Low" else "High"

    if category_percentages['generic'] < 30:
        risk_factors.append("Low percentage of generic anchors (<30%)")

    if category_percentages['branded'] < 20:
        risk_factors.append("Low percentage of branded anchors (<20%)")

    return {
        'anchors': analyzed_anchors,
        'total_links': total_links,
        'categories': category_percentages,
        'risk_level': risk_level,
        'risk_factors': risk_factors
    }


def display_anchor_analysis(data):
    """Display anchor text analysis results"""
    st.markdown("### 📊 Anchor Text Distribution Analysis")

    # Overview metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Links", data['total_links'])
    with col2:
        st.metric("Unique Anchors", len(data['anchors']))
    with col3:
        if data['risk_level'] == "Low":
            st.success(f"Risk Level: {data['risk_level']}")
        elif data['risk_level'] == "Medium":
            st.warning(f"Risk Level: {data['risk_level']}")
        else:
            st.error(f"Risk Level: {data['risk_level']}")

    # Category breakdown
    st.markdown("### 📈 Category Distribution")

    categories = data['categories']
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Exact Match:** {categories['exact_match']:.1f}%")
        st.write(f"**Partial Match:** {categories['partial_match']:.1f}%")
        st.write(f"**Branded:** {categories['branded']:.1f}%")

    with col2:
        st.write(f"**Generic:** {categories['generic']:.1f}%")
        st.write(f"**Naked URL:** {categories['naked_url']:.1f}%")

    # Detailed anchor breakdown
    st.markdown("### 📝 Anchor Text Breakdown")

    for anchor in sorted(data['anchors'], key=lambda x: x['count'], reverse=True):
        with st.expander(f"{anchor['text']} ({anchor['count']} times - {anchor['percentage']:.1f}%)"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**Count:** {anchor['count']}")
            with col2:
                st.write(f"**Percentage:** {anchor['percentage']:.1f}%")
            with col3:
                st.write(f"**Category:** {anchor['category'].replace('_', ' ').title()}")

    # Risk factors
    if data['risk_factors']:
        st.markdown("### ⚠️ Risk Factors")
        for risk in data['risk_factors']:
            st.warning(f"⚠️ {risk}")

    # Recommendations
    st.markdown("### 💡 Optimization Recommendations")

    recommendations = []

    if categories['exact_match'] > 15:
        recommendations.append("🎯 Reduce exact match anchor percentage to under 10%")

    if categories['branded'] < 20:
        recommendations.append("🏷️ Increase branded anchor text usage to 20-30%")

    if categories['generic'] < 30:
        recommendations.append("⚡ Add more generic anchors (click here, read more, etc.)")

    recommendations.extend([
        "🔄 Maintain natural anchor text variation",
        "📊 Monitor anchor distribution regularly",
        "🎨 Use long-tail keyword variations",
        "⚖️ Balance keyword-rich and natural anchors"
    ])

    for rec in recommendations:
        st.write(f"• {rec}")


def link_prospecting():
    """Link prospecting and opportunity finder"""
    create_tool_header("Link Prospecting", "Find link building opportunities", "🎯")

    st.markdown("### Link Prospecting Tool")

    # Target information
    col1, col2 = st.columns(2)
    with col1:
        target_domain = st.text_input("Your Domain:", placeholder="example.com")
        target_keywords = st.text_area("Target Keywords:",
                                       placeholder="digital marketing\nSEO services\ncontent marketing")

    with col2:
        industry = st.selectbox("Industry:",
                                ["Technology", "Marketing", "Healthcare", "Finance", "E-commerce",
                                 "Education", "Travel", "Food", "Real Estate", "Other"])
        prospect_types = st.multiselect("Prospect Types:",
                                        ["Resource Pages", "Guest Posting", "Broken Links",
                                         "Competitor Backlinks", "Directory Listings", "HARO"])

    # Search criteria
    st.markdown("#### Search Criteria")
    col1, col2 = st.columns(2)
    with col1:
        min_domain_authority = st.slider("Minimum Domain Authority:", 0, 100, 20)
        geographic_focus = st.selectbox("Geographic Focus:", ["Global", "US", "UK", "Canada", "Australia"])

    with col2:
        language = st.selectbox("Language:", ["English", "Spanish", "French", "German", "Other"])
        exclude_domains = st.text_area("Domains to Exclude:", placeholder="competitor1.com\ncompetitor2.com")

    if target_domain and prospect_types and st.button("Find Link Prospects"):
        prospects = find_link_prospects(target_domain, target_keywords, industry, prospect_types,
                                        min_domain_authority, geographic_focus)
        display_link_prospects(prospects)


def find_link_prospects(domain, keywords, industry, types, min_da, geo_focus):
    """Find link building prospects based on criteria"""

    prospects = []

    # Simulate different types of prospects
    for prospect_type in types:
        count = random.randint(5, 15)

        for i in range(count):
            da = random.randint(max(min_da, 20), 100)

            # Generate prospect based on type
            if prospect_type == "Resource Pages":
                prospect = {
                    'type': 'Resource Page',
                    'domain': f'resource-site-{i + 1}.com',
                    'url': f'https://resource-site-{i + 1}.com/resources',
                    'domain_authority': da,
                    'page_title': f'Best {industry} Resources',
                    'contact_info': f'contact@resource-site-{i + 1}.com',
                    'relevance_score': random.randint(60, 95),
                    'difficulty': random.choice(['Easy', 'Medium', 'Hard'])
                }

            elif prospect_type == "Guest Posting":
                prospect = {
                    'type': 'Guest Post',
                    'domain': f'blog-{i + 1}.com',
                    'url': f'https://blog-{i + 1}.com/write-for-us',
                    'domain_authority': da,
                    'page_title': 'Write for Us - Guest Posting Guidelines',
                    'contact_info': f'editor@blog-{i + 1}.com',
                    'relevance_score': random.randint(70, 90),
                    'difficulty': random.choice(['Medium', 'Hard'])
                }

            elif prospect_type == "Broken Links":
                prospect = {
                    'type': 'Broken Link',
                    'domain': f'authority-{i + 1}.com',
                    'url': f'https://authority-{i + 1}.com/broken-page',
                    'domain_authority': da,
                    'page_title': f'{industry} Tools and Resources',
                    'contact_info': f'webmaster@authority-{i + 1}.com',
                    'relevance_score': random.randint(80, 95),
                    'difficulty': 'Medium'
                }

            elif prospect_type == "Competitor Backlinks":
                prospect = {
                    'type': 'Competitor Link',
                    'domain': f'industry-site-{i + 1}.com',
                    'url': f'https://industry-site-{i + 1}.com/partners',
                    'domain_authority': da,
                    'page_title': f'{industry} Partners Directory',
                    'contact_info': f'partnerships@industry-site-{i + 1}.com',
                    'relevance_score': random.randint(75, 90),
                    'difficulty': random.choice(['Medium', 'Hard'])
                }

            else:  # Directory or HARO
                prospect = {
                    'type': prospect_type.replace(' Listings', '').replace('HARO', 'HARO Query'),
                    'domain': f'{prospect_type.lower().replace(" ", "-")}-{i + 1}.com',
                    'url': f'https://{prospect_type.lower().replace(" ", "-")}-{i + 1}.com',
                    'domain_authority': da,
                    'page_title': f'{industry} Directory Listing',
                    'contact_info': f'submit@{prospect_type.lower().replace(" ", "-")}-{i + 1}.com',
                    'relevance_score': random.randint(60, 85),
                    'difficulty': random.choice(['Easy', 'Medium'])
                }

            prospects.append(prospect)

    # Sort by relevance score
    prospects.sort(key=lambda x: x['relevance_score'], reverse=True)

    return {
        'prospects': prospects,
        'total_found': len(prospects),
        'avg_domain_authority': sum(p['domain_authority'] for p in prospects) / len(prospects),
        'difficulty_breakdown': {
            'easy': sum(1 for p in prospects if p['difficulty'] == 'Easy'),
            'medium': sum(1 for p in prospects if p['difficulty'] == 'Medium'),
            'hard': sum(1 for p in prospects if p['difficulty'] == 'Hard')
        }
    }


def display_link_prospects(data):
    """Display link prospecting results"""
    st.markdown("### 🎯 Link Prospects Found")

    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Prospects", data['total_found'])
    with col2:
        st.metric("Avg Domain Authority", f"{data['avg_domain_authority']:.1f}")
    with col3:
        st.metric("High Relevance (80+)",
                  sum(1 for p in data['prospects'] if p['relevance_score'] >= 80))

    # Difficulty breakdown
    st.markdown("### 📊 Difficulty Distribution")
    breakdown = data['difficulty_breakdown']
    col1, col2, col3 = st.columns(3)

    with col1:
        st.success(f"Easy: {breakdown['easy']}")
    with col2:
        st.warning(f"Medium: {breakdown['medium']}")
    with col3:
        st.error(f"Hard: {breakdown['hard']}")

    # Filter options
    st.markdown("### 🔍 Filter Prospects")
    col1, col2 = st.columns(2)
    with col1:
        min_relevance = st.slider("Minimum Relevance Score:", 0, 100, 60)
    with col2:
        difficulty_filter = st.multiselect("Difficulty Level:",
                                           ["Easy", "Medium", "Hard"],
                                           default=["Easy", "Medium", "Hard"])

    # Filter prospects
    filtered_prospects = [
        p for p in data['prospects']
        if p['relevance_score'] >= min_relevance and p['difficulty'] in difficulty_filter
    ]

    # Display prospects
    st.markdown(f"### 📋 Prospects ({len(filtered_prospects)} shown)")

    for i, prospect in enumerate(filtered_prospects[:20], 1):  # Show top 20
        relevance_color = "🟢" if prospect['relevance_score'] >= 80 else "🟡" if prospect[
                                                                                   'relevance_score'] >= 70 else "🔴"

        with st.expander(f"{i}. {relevance_color} {prospect['domain']} (DA: {prospect['domain_authority']})"):
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Type:** {prospect['type']}")
                st.write(f"**Domain Authority:** {prospect['domain_authority']}")
                st.write(f"**Relevance Score:** {prospect['relevance_score']}/100")
                st.write(f"**Difficulty:** {prospect['difficulty']}")

            with col2:
                st.write(f"**URL:** {prospect['url']}")
                st.write(f"**Page Title:** {prospect['page_title']}")
                st.write(f"**Contact:** {prospect['contact_info']}")

            # Action buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"Add to Outreach List", key=f"add_{i}"):
                    st.success("Added to outreach list!")
            with col2:
                if st.button(f"Mark as Contacted", key=f"contact_{i}"):
                    st.info("Marked as contacted")
            with col3:
                if st.button(f"Not Interested", key=f"skip_{i}"):
                    st.warning("Marked as not interested")

    # Export option
    st.markdown("### 📥 Export Prospects")
    if st.button("Export to CSV"):
        st.success("Prospects exported to CSV! (simulation)")


def outreach_templates():
    """Email outreach template generator"""
    create_tool_header("Outreach Templates", "Generate personalized outreach email templates", "📧")

    st.markdown("### Email Outreach Template Generator")

    # Template type and context
    col1, col2 = st.columns(2)
    with col1:
        template_type = st.selectbox("Template Type:",
                                     ["Guest Post Pitch", "Resource Page Request", "Broken Link Outreach",
                                      "General Link Request", "Partnership Proposal", "Follow-up Email"])

        outreach_tone = st.selectbox("Email Tone:",
                                     ["Professional", "Friendly", "Casual", "Formal"])

    with col2:
        personalization_level = st.selectbox("Personalization Level:",
                                             ["High", "Medium", "Low"])

        include_examples = st.checkbox("Include specific examples/value propositions")

    # Target information
    st.markdown("#### Target Information")
    col1, col2 = st.columns(2)
    with col1:
        target_name = st.text_input("Contact Name:", placeholder="John Smith")
        target_site = st.text_input("Target Website:", placeholder="example.com")
        target_page = st.text_input("Specific Page/Resource:", placeholder="https://example.com/resources")

    with col2:
        your_name = st.text_input("Your Name:", placeholder="Jane Doe")
        your_site = st.text_input("Your Website:", placeholder="yoursite.com")
        your_title = st.text_input("Your Title:", placeholder="Content Manager")

    # Content details
    st.markdown("#### Content/Proposal Details")
    content_topic = st.text_input("Content Topic/Subject:", placeholder="Digital Marketing Best Practices")
    value_proposition = st.text_area("Value Proposition:",
                                     placeholder="What value do you provide? Why should they link to you?")

    if st.button("Generate Outreach Template"):
        if target_site and your_name and template_type:
            template = generate_outreach_template(template_type, outreach_tone, personalization_level,
                                                  target_name, target_site, target_page, your_name,
                                                  your_site, your_title, content_topic, value_proposition,
                                                  include_examples)
            display_outreach_template(template)
        else:
            st.error("Please fill in the required fields")


def generate_outreach_template(template_type, tone, personalization, target_name, target_site,
                               target_page, your_name, your_site, your_title, topic, value_prop,
                               include_examples):
    """Generate personalized outreach email template"""

    # Subject line templates
    subject_templates = {
        "Guest Post Pitch": f"Guest post idea for {target_site}: {topic}",
        "Resource Page Request": f"Resource suggestion for {target_site}",
        "Broken Link Outreach": f"Broken link on {target_site} - quick fix suggestion",
        "General Link Request": f"Great content for {target_site} readers",
        "Partnership Proposal": f"Partnership opportunity with {your_site}",
        "Follow-up Email": f"Following up on my previous email"
    }

    # Greeting based on personalization level
    if personalization == "High" and target_name:
        greeting = f"Hi {target_name},"
    elif personalization == "Medium":
        greeting = f"Hello {target_site} team,"
    else:
        greeting = "Hello,"

    # Email body templates based on type and tone
    if template_type == "Guest Post Pitch":
        if tone == "Professional":
            body = f"""I hope this email finds you well.

I'm {your_name}, {your_title} at {your_site}. I've been following {target_site} and really appreciate your content on {topic if topic else 'industry topics'}.

I'd love to contribute a guest post to your site. I have an idea for an article titled "{topic if topic else 'Industry Best Practices'}" that I believe would provide significant value to your readers.

{value_prop if value_prop else 'The article would include practical tips, case studies, and actionable insights that your audience would find valuable.'}

I have experience writing for [mention relevant publications] and can provide samples of my previous work if you're interested.

Would you be open to discussing this opportunity? I'm happy to send over a detailed outline or answer any questions you might have."""

        else:  # Friendly/Casual tone
            body = f"""Hope you're having a great day!

I'm {your_name} from {your_site}, and I'm a big fan of what you're doing at {target_site}. Your content is always so insightful!

I was wondering if you'd be interested in a guest post from me? I have this great idea for an article about "{topic if topic else 'Industry Best Practices'}" that I think your readers would really love.

{value_prop if value_prop else "I'm thinking of including some real-world examples and practical tips that people can actually use."}

I've written for a few other sites before and always make sure to deliver high-quality, original content. Want to chat about it?"""

    elif template_type == "Resource Page Request":
        body = f"""I hope you're doing well.

I recently came across your excellent resource page at {target_page if target_page else target_site} and found it incredibly valuable.

I noticed you feature high-quality {topic if topic else 'industry'} resources, and I thought you might be interested in a resource I've created: {your_site}.

{value_prop if value_prop else "This resource provides comprehensive information and tools that complement the other resources you've listed."}

If you think it would be a good fit for your page, I'd be honored to have it included. I'm happy to provide any additional information you might need.

Thank you for curating such a valuable resource for the community!"""

    elif template_type == "Broken Link Outreach":
        body = f"""I hope this message finds you well.

I was browsing {target_site} today and found your {target_page if target_page else 'resource page'} to be incredibly helpful. However, I noticed that one of the links appears to be broken.

The link to [broken link URL] returns a 404 error. I thought you'd want to know so you can fix it.

As an alternative, I have a similar resource at {your_site} that covers {topic if topic else 'the same topic'}. {value_prop if value_prop else 'It provides comprehensive information on the subject and might be a suitable replacement.'}

Either way, I wanted to give you a heads up about the broken link. Keep up the great work!"""

    else:  # General templates
        body = f"""I hope you're having a great day.

I'm {your_name}, {your_title} at {your_site}. I've been following your work at {target_site} and really admire your content.

I wanted to reach out because I recently created a resource about {topic if topic else 'industry best practices'} that I think your audience would find valuable.

{value_prop if value_prop else 'The resource includes detailed insights, practical examples, and actionable tips.'}

If you think it would be useful to your readers, I'd be grateful if you considered mentioning it or linking to it in a future post.

Thanks for all the great content you create!"""

    # Closing
    if tone in ["Professional", "Formal"]:
        closing = f"""Best regards,
{your_name}
{your_title}
{your_site}"""
    else:
        closing = f"""Best,
{your_name}
{your_site}"""

    # Combine parts
    subject = subject_templates.get(template_type, f"Outreach from {your_site}")
    full_email = f"{greeting}\n\n{body}\n\n{closing}"

    return {
        'subject': subject,
        'body': full_email,
        'template_type': template_type,
        'tone': tone,
        'personalization': personalization
    }


def display_outreach_template(template):
    """Display generated outreach template"""
    st.markdown("### 📧 Generated Outreach Template")

    # Template info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**Type:** {template['template_type']}")
    with col2:
        st.info(f"**Tone:** {template['tone']}")
    with col3:
        st.info(f"**Personalization:** {template['personalization']}")

    # Subject line
    st.markdown("#### Subject Line")
    st.code(template['subject'])

    # Email body
    st.markdown("#### Email Body")
    st.text_area("Email Content:", template['body'], height=400)

    # Action buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Copy Template"):
            st.success("Template copied to clipboard! (simulation)")

    with col2:
        if st.button("Save to Templates"):
            st.success("Template saved! (simulation)")

    with col3:
        if st.button("Generate New Version"):
            st.info("Click 'Generate Outreach Template' above for a new version")

    # Tips
    st.markdown("### 💡 Outreach Tips")
    tips = [
        "📧 Personalize each email - mention specific content from their site",
        "⏰ Follow up after 1-2 weeks if no response",
        "📊 Track open rates and responses to optimize templates",
        "🎯 Keep initial emails short and focused",
        "📱 Make sure emails are mobile-friendly",
        "🔗 Include social proof or credentials when relevant"
    ]

    for tip in tips:
        st.write(f"• {tip}")


def link_quality_checker():
    """Link quality assessment tool"""
    create_tool_header("Link Quality Checker", "Assess the quality and value of potential links", "🏆")

    st.markdown("### Link Quality Checker")

    # Input methods
    input_method = st.radio("Input Method:", ["Single URL", "Bulk URLs", "Domain Analysis"])

    urls_to_check = []

    if input_method == "Single URL":
        single_url = st.text_input("URL to check:", placeholder="https://example.com/page")
        if single_url:
            urls_to_check = [single_url]

    elif input_method == "Bulk URLs":
        bulk_urls = st.text_area("Enter URLs (one per line):",
                                 placeholder="https://site1.com\nhttps://site2.com/page",
                                 height=150)
        if bulk_urls:
            urls_to_check = [url.strip() for url in bulk_urls.split('\n') if url.strip()]

    else:  # Domain Analysis
        domain = st.text_input("Domain to analyze:", placeholder="example.com")
        if domain:
            urls_to_check = [f"https://{domain}"]

    # Analysis criteria
    st.markdown("#### Analysis Criteria")
    col1, col2 = st.columns(2)

    with col1:
        check_spam_score = st.checkbox("Check spam score", value=True)
        check_content_quality = st.checkbox("Analyze content quality", value=True)
        check_link_profile = st.checkbox("Analyze link profile", value=True)

    with col2:
        check_technical_seo = st.checkbox("Check technical SEO", value=True)
        check_social_signals = st.checkbox("Check social signals")
        detailed_analysis = st.checkbox("Detailed analysis report")

    if urls_to_check and st.button("Analyze Link Quality"):
        quality_results = analyze_link_quality(urls_to_check, check_spam_score, check_content_quality,
                                               check_link_profile, check_technical_seo, check_social_signals)
        display_link_quality_results(quality_results, detailed_analysis)


def analyze_link_quality(urls, check_spam, check_content, check_links, check_technical, check_social):
    """Analyze the quality of potential link sources"""

    results = []

    for url in urls:
        # Simulate quality metrics
        domain = url.replace('https://', '').replace('http://', '').split('/')[0]

        # Basic metrics
        domain_authority = random.randint(20, 100)
        page_authority = random.randint(15, min(domain_authority + 10, 100))

        # Quality factors
        quality_score = 0
        max_score = 100
        factors = {}

        # Domain Authority (25 points)
        if domain_authority >= 70:
            da_score = 25
        elif domain_authority >= 50:
            da_score = 20
        elif domain_authority >= 30:
            da_score = 15
        else:
            da_score = 10

        quality_score += da_score
        factors['domain_authority'] = {'score': da_score, 'value': domain_authority}

        # Spam score (20 points)
        if check_spam:
            spam_score = random.randint(0, 30)
            if spam_score <= 5:
                spam_points = 20
            elif spam_score <= 15:
                spam_points = 15
            elif spam_score <= 25:
                spam_points = 10
            else:
                spam_points = 0

            quality_score += spam_points
            factors['spam_score'] = {'score': spam_points, 'value': spam_score}

        # Content quality (20 points)
        if check_content:
            content_score = random.randint(40, 95)
            content_points = int((content_score / 100) * 20)
            quality_score += content_points
            factors['content_quality'] = {'score': content_points, 'value': content_score}

        # Link profile (15 points)
        if check_links:
            referring_domains = random.randint(10, 1000)
            if referring_domains >= 500:
                link_points = 15
            elif referring_domains >= 100:
                link_points = 12
            elif referring_domains >= 50:
                link_points = 8
            else:
                link_points = 5

            quality_score += link_points
            factors['link_profile'] = {'score': link_points, 'value': referring_domains}

        # Technical SEO (10 points)
        if check_technical:
            tech_score = random.randint(60, 100)
            tech_points = int((tech_score / 100) * 10)
            quality_score += tech_points
            factors['technical_seo'] = {'score': tech_points, 'value': tech_score}

        # Social signals (10 points)
        if check_social:
            social_score = random.randint(20, 90)
            social_points = int((social_score / 100) * 10)
            quality_score += social_points
            factors['social_signals'] = {'score': social_points, 'value': social_score}

        # Calculate final percentage
        actual_max = sum(20 if check_spam else 0, 20 if check_content else 0, 15 if check_links else 0,
                         10 if check_technical else 0, 10 if check_social else 0) + 25  # DA always included

        final_percentage = (quality_score / actual_max) * 100

        # Overall grade
        if final_percentage >= 80:
            grade = "A"
            recommendation = "Excellent link opportunity"
        elif final_percentage >= 70:
            grade = "B"
            recommendation = "Good link opportunity"
        elif final_percentage >= 60:
            grade = "C"
            recommendation = "Average link opportunity"
        elif final_percentage >= 50:
            grade = "D"
            recommendation = "Below average - consider carefully"
        else:
            grade = "F"
            recommendation = "Poor link opportunity - avoid"

        result = {
            'url': url,
            'domain': domain,
            'quality_score': final_percentage,
            'grade': grade,
            'recommendation': recommendation,
            'factors': factors,
            'domain_authority': domain_authority,
            'page_authority': page_authority
        }

        results.append(result)

    return {
        'results': results,
        'avg_quality': sum(r['quality_score'] for r in results) / len(results),
        'high_quality_count': sum(1 for r in results if r['quality_score'] >= 70),
        'total_analyzed': len(results)
    }


def display_link_quality_results(data, detailed=False):
    """Display link quality analysis results"""
    st.markdown("### 🏆 Link Quality Analysis Results")

    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("URLs Analyzed", data['total_analyzed'])
    with col2:
        st.metric("Average Quality", f"{data['avg_quality']:.1f}%")
    with col3:
        st.metric("High Quality (70+%)", f"{data['high_quality_count']}/{data['total_analyzed']}")

    # Individual results
    st.markdown("### 📊 Quality Assessment Results")

    for i, result in enumerate(data['results'], 1):
        # Color coding based on grade
        if result['grade'] in ['A', 'B']:
            grade_color = "🟢"
        elif result['grade'] == 'C':
            grade_color = "🟡"
        else:
            grade_color = "🔴"

        with st.expander(
                f"{i}. {grade_color} {result['domain']} - Grade {result['grade']} ({result['quality_score']:.1f}%)"):

            # Basic metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Quality Score", f"{result['quality_score']:.1f}%")
            with col2:
                st.metric("Domain Authority", result['domain_authority'])
            with col3:
                st.metric("Page Authority", result['page_authority'])

            # Quality factors breakdown
            if detailed and result['factors']:
                st.markdown("**Quality Factors Breakdown:**")

                for factor, data_point in result['factors'].items():
                    factor_name = factor.replace('_', ' ').title()
                    st.write(f"**{factor_name}:** {data_point['value']} (Score: {data_point['score']})")

            # Recommendation
            st.markdown(f"**Recommendation:** {result['recommendation']}")

    # Quality distribution
    st.markdown("### 📈 Quality Distribution")

    grade_counts = {}
    for result in data['results']:
        grade_counts[result['grade']] = grade_counts.get(result['grade'], 0) + 1

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    grades = ['A', 'B', 'C', 'D', 'F']

    for i, grade in enumerate(grades):
        count = grade_counts.get(grade, 0)
        with cols[i]:
            if grade in ['A', 'B']:
                st.success(f"Grade {grade}: {count}")
            elif grade == 'C':
                st.warning(f"Grade {grade}: {count}")
            else:
                st.error(f"Grade {grade}: {count}")

    # Overall recommendations
    st.markdown("### 💡 Overall Recommendations")

    recommendations = []

    high_quality_percentage = (data['high_quality_count'] / data['total_analyzed']) * 100

    if high_quality_percentage >= 70:
        recommendations.append("✅ Excellent link opportunities - proceed with outreach")
    elif high_quality_percentage >= 50:
        recommendations.append("⚡ Good mix of opportunities - focus on highest quality")
    else:
        recommendations.append("⚠️ Limited high-quality opportunities - expand prospect list")

    recommendations.extend([
        "🎯 Prioritize sites with Grade A and B ratings",
        "🔍 Investigate Grade D and F sites before outreach",
        "📊 Monitor link quality metrics regularly",
        "🚫 Avoid sites with high spam scores (>15)"
    ])

    for rec in recommendations:
        st.write(f"• {rec}")


def heatmap_analyzer():
    """Analyze website heatmap data for optimization insights"""
    create_tool_header("Heatmap Analyzer", "Analyze user behavior patterns from heatmaps", "🔥")

    st.markdown("### 📊 Heatmap Data Input")

    # URL input
    url = st.text_input("Website Page URL:", placeholder="https://example.com/page")

    # Heatmap type
    heatmap_type = st.selectbox("Heatmap Type:", [
        "Click Heatmap", "Scroll Heatmap", "Movement Heatmap", "Attention Heatmap"
    ])

    # Device breakdown
    st.markdown("### 📱 Device Data")
    col1, col2, col3 = st.columns(3)
    with col1:
        desktop_users = st.number_input("Desktop Users:", min_value=0, value=1500)
    with col2:
        mobile_users = st.number_input("Mobile Users:", min_value=0, value=2000)
    with col3:
        tablet_users = st.number_input("Tablet Users:", min_value=0, value=500)

    # Key metrics
    st.markdown("### 🎯 Key Interaction Areas")
    col1, col2 = st.columns(2)
    with col1:
        above_fold_clicks = st.slider("Above-the-fold Click Rate %:", 0, 100, 65)
        cta_click_rate = st.slider("CTA Click Rate %:", 0, 100, 8)
    with col2:
        scroll_depth = st.slider("Average Scroll Depth %:", 0, 100, 75)
        exit_rate = st.slider("Page Exit Rate %:", 0, 100, 45)

    if st.button("Analyze Heatmap Data"):
        # Generate analysis
        total_users = desktop_users + mobile_users + tablet_users

        if total_users > 0:
            # Display summary metrics
            st.markdown("### 📈 Analysis Results")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Users", f"{total_users:,}")
            with col2:
                st.metric("Avg. Scroll Depth", f"{scroll_depth}%")
            with col3:
                st.metric("CTA Performance", f"{cta_click_rate}%")
            with col4:
                engagement_score = (above_fold_clicks + scroll_depth + (100 - exit_rate)) / 3
                st.metric("Engagement Score", f"{engagement_score:.1f}/100")

            # Device breakdown chart
            st.markdown("### 📊 Device Distribution")
            device_data = {
                'Desktop': desktop_users,
                'Mobile': mobile_users,
                'Tablet': tablet_users
            }
            st.bar_chart(device_data)

            # Recommendations
            st.markdown("### 💡 Optimization Recommendations")
            recommendations = []

            if above_fold_clicks < 50:
                recommendations.append("🔴 Low above-the-fold engagement - consider repositioning key elements")
            elif above_fold_clicks > 80:
                recommendations.append("🟢 Excellent above-the-fold engagement")

            if cta_click_rate < 5:
                recommendations.append("🔴 CTA needs optimization - test different colors, text, or positioning")
            elif cta_click_rate > 10:
                recommendations.append("🟢 Strong CTA performance")

            if scroll_depth < 50:
                recommendations.append("🔴 Poor scroll engagement - content may not be compelling enough")
            elif scroll_depth > 80:
                recommendations.append("🟢 Users are highly engaged with your content")

            if exit_rate > 60:
                recommendations.append("🔴 High exit rate - review page loading speed and content relevance")
            elif exit_rate < 30:
                recommendations.append("🟢 Low exit rate indicates good user retention")

            # Mobile-specific recommendations
            mobile_percentage = (mobile_users / total_users) * 100
            if mobile_percentage > 60:
                recommendations.append("📱 Mobile-first optimization critical - majority of users on mobile")

            for rec in recommendations:
                st.write(f"• {rec}")


def funnel_analyzer():
    """Analyze conversion funnel performance"""
    create_tool_header("Funnel Analyzer", "Analyze conversion funnel drop-off points", "🔄")

    st.markdown("### 🎯 Funnel Steps Configuration")

    # Number of funnel steps
    num_steps = st.slider("Number of Funnel Steps:", 2, 8, 4)

    # Funnel step data
    steps_data = []
    for i in range(num_steps):
        st.markdown(f"#### Step {i + 1}")
        col1, col2 = st.columns(2)
        with col1:
            step_name = st.text_input(f"Step Name:", key=f"step_name_{i}",
                                      value=f"Step {i + 1}")
        with col2:
            step_users = st.number_input(f"Users:", min_value=0, key=f"step_users_{i}",
                                         value=max(1000 - (i * 200), 100))
        steps_data.append({"name": step_name, "users": step_users})

    if st.button("Analyze Funnel"):
        st.markdown("### 📊 Funnel Analysis Results")

        # Calculate conversion rates and drop-offs
        funnel_metrics = []
        for i, step in enumerate(steps_data):
            if i == 0:
                conversion_rate = 100.0
                drop_off = 0.0
            else:
                conversion_rate = (step["users"] / steps_data[0]["users"]) * 100
                drop_off = ((steps_data[i - 1]["users"] - step["users"]) / steps_data[i - 1]["users"]) * 100

            funnel_metrics.append({
                "step": step["name"],
                "users": step["users"],
                "conversion_rate": conversion_rate,
                "drop_off": drop_off
            })

        # Display funnel visualization
        st.markdown("### 🔄 Funnel Visualization")
        for i, metric in enumerate(funnel_metrics):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"**{metric['step']}**")
            with col2:
                st.metric("Users", f"{metric['users']:,}")
            with col3:
                st.metric("Conversion Rate", f"{metric['conversion_rate']:.1f}%")
            with col4:
                if i > 0:
                    color = "🔴" if metric['drop_off'] > 30 else "🟡" if metric['drop_off'] > 15 else "🟢"
                    st.metric("Drop-off", f"{color} {metric['drop_off']:.1f}%")
                else:
                    st.metric("Drop-off", "N/A")

        # Overall funnel performance
        overall_conversion = (steps_data[-1]["users"] / steps_data[0]["users"]) * 100
        st.markdown(f"### 🎯 Overall Conversion Rate: {overall_conversion:.1f}%")

        # Recommendations
        st.markdown("### 💡 Optimization Recommendations")
        recommendations = []

        # Find biggest drop-off points
        max_drop_off = 0
        max_drop_step = ""
        for i, metric in enumerate(funnel_metrics[1:], 1):
            if metric['drop_off'] > max_drop_off:
                max_drop_off = metric['drop_off']
                max_drop_step = metric['step']

        if max_drop_off > 30:
            recommendations.append(f"🔴 Critical: Focus on '{max_drop_step}' - highest drop-off at {max_drop_off:.1f}%")

        if overall_conversion < 5:
            recommendations.append("🔴 Overall conversion is very low - consider fundamental UX changes")
        elif overall_conversion > 15:
            recommendations.append("🟢 Strong overall conversion rate")

        recommendations.extend([
            "🔍 A/B test the step with highest drop-off rate",
            "📱 Ensure mobile optimization for all funnel steps",
            "⚡ Test loading speed at each step",
            "📝 Simplify forms and reduce required fields",
            "🎯 Add progress indicators for multi-step processes"
        ])

        for rec in recommendations:
            st.write(f"• {rec}")


def cro_checklist():
    """Conversion Rate Optimization checklist tool"""
    create_tool_header("CRO Checklist", "Comprehensive conversion optimization checklist", "✅")

    st.markdown("### 🎯 Select Your Focus Area")

    focus_area = st.selectbox("Optimization Focus:", [
        "Landing Page", "E-commerce Product Page", "Checkout Process",
        "Lead Generation Form", "Homepage", "Blog/Content Page"
    ])

    if focus_area == "Landing Page":
        checklist_items = [
            "Clear, compelling headline that matches ad/email copy",
            "Single, focused call-to-action (CTA)",
            "Minimal navigation distractions",
            "Social proof (testimonials, reviews, logos)",
            "Mobile-responsive design",
            "Fast loading speed (< 3 seconds)",
            "Above-the-fold value proposition",
            "Trust signals (security badges, guarantees)",
            "Contact information clearly visible",
            "A/B test different variations"
        ]
    elif focus_area == "E-commerce Product Page":
        checklist_items = [
            "High-quality product images from multiple angles",
            "Detailed product descriptions",
            "Customer reviews and ratings",
            "Clear pricing and availability",
            "Multiple payment options",
            "Security badges and trust signals",
            "Related/recommended products",
            "Clear return/refund policy",
            "Mobile-optimized checkout",
            "Inventory level indicators"
        ]
    elif focus_area == "Checkout Process":
        checklist_items = [
            "Guest checkout option available",
            "Minimal form fields required",
            "Progress indicator for multi-step checkout",
            "Multiple payment methods",
            "Security badges prominently displayed",
            "Order summary clearly visible",
            "Shipping costs shown early",
            "Error messages are clear and helpful",
            "Auto-fill and validation features",
            "Mobile-optimized design"
        ]
    elif focus_area == "Lead Generation Form":
        checklist_items = [
            "Minimal required fields (name, email only if possible)",
            "Clear value proposition for form submission",
            "Compelling CTA button text",
            "Privacy policy link visible",
            "Form validation with helpful error messages",
            "Mobile-friendly form design",
            "Social proof near the form",
            "No CAPTCHA if possible",
            "Auto-focus on first field",
            "Thank you page or confirmation"
        ]
    elif focus_area == "Homepage":
        checklist_items = [
            "Clear value proposition in 5 seconds",
            "Primary CTA above the fold",
            "Navigation is intuitive and organized",
            "Social proof prominently displayed",
            "Mobile-responsive design",
            "Fast loading speed",
            "Search functionality if needed",
            "Contact information easily found",
            "Professional design and branding",
            "Clear next steps for visitors"
        ]
    else:  # Blog/Content Page
        checklist_items = [
            "Engaging headline and meta description",
            "Clear article structure with headers",
            "Related content suggestions",
            "Social sharing buttons",
            "Email subscription form",
            "Author bio and credibility indicators",
            "Fast loading speed",
            "Mobile-readable font sizes",
            "Internal linking to relevant content",
            "Clear CTA within or after content"
        ]

    st.markdown(f"### ✅ {focus_area} Optimization Checklist")

    # Create interactive checklist
    checked_items = 0
    total_items = len(checklist_items)

    for i, item in enumerate(checklist_items):
        if st.checkbox(item, key=f"checklist_{i}"):
            checked_items += 1

    # Progress tracking
    completion_rate = (checked_items / total_items) * 100
    st.markdown(f"### 📊 Completion Progress: {completion_rate:.0f}%")

    # Progress bar
    progress_bar = st.progress(completion_rate / 100)

    # Recommendations based on completion
    if completion_rate < 50:
        st.warning("🔴 Low completion rate - focus on implementing basic optimizations first")
    elif completion_rate < 80:
        st.info("🟡 Good progress - continue working through the remaining items")
    else:
        st.success("🟢 Excellent! You've covered most optimization areas")

    # Priority recommendations
    st.markdown("### 🎯 Priority Recommendations")
    priority_tips = [
        "Start with items that have the biggest impact on user experience",
        "A/B test one change at a time to measure impact",
        "Focus on mobile optimization - majority of traffic is mobile",
        "Use analytics to identify your biggest pain points",
        "Implement tracking to measure conversion improvements"
    ]

    for tip in priority_tips:
        st.write(f"• {tip}")


def form_optimizer():
    """Form optimization analysis tool"""
    create_tool_header("Form Optimizer", "Optimize forms for better conversions", "📝")

    st.markdown("### 📊 Form Performance Data")

    # Form metrics input
    col1, col2 = st.columns(2)
    with col1:
        form_views = st.number_input("Form Views:", min_value=1, value=1000)
        form_starts = st.number_input("Form Starts:", min_value=0, value=600)
        form_completions = st.number_input("Form Completions:", min_value=0, value=150)

    with col2:
        num_fields = st.number_input("Number of Form Fields:", min_value=1, value=8)
        required_fields = st.number_input("Required Fields:", min_value=1, value=5)
        avg_completion_time = st.number_input("Avg. Completion Time (seconds):", min_value=1, value=180)

    # Form type
    form_type = st.selectbox("Form Type:", [
        "Contact Form", "Lead Generation", "Registration", "Checkout",
        "Survey", "Newsletter Signup", "Quote Request"
    ])

    # Form features
    st.markdown("### ⚙️ Form Features")
    col1, col2 = st.columns(2)
    with col1:
        has_progress_bar = st.checkbox("Progress Indicator")
        has_validation = st.checkbox("Real-time Validation")
        has_autofill = st.checkbox("Auto-fill Enabled")
    with col2:
        mobile_optimized = st.checkbox("Mobile Optimized")
        has_social_login = st.checkbox("Social Login Options")
        has_security_badges = st.checkbox("Security Badges")

    if st.button("Analyze Form Performance"):
        # Calculate metrics
        start_rate = (form_starts / form_views) * 100 if form_views > 0 else 0
        completion_rate = (form_completions / form_starts) * 100 if form_starts > 0 else 0
        overall_conversion = (form_completions / form_views) * 100 if form_views > 0 else 0
        abandonment_rate = 100 - completion_rate

        # Display key metrics
        st.markdown("### 📈 Form Performance Metrics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            color = "🟢" if start_rate > 70 else "🟡" if start_rate > 50 else "🔴"
            st.metric("Start Rate", f"{color} {start_rate:.1f}%")
        with col2:
            color = "🟢" if completion_rate > 70 else "🟡" if completion_rate > 50 else "🔴"
            st.metric("Completion Rate", f"{color} {completion_rate:.1f}%")
        with col3:
            color = "🟢" if overall_conversion > 15 else "🟡" if overall_conversion > 8 else "🔴"
            st.metric("Overall Conversion", f"{color} {overall_conversion:.1f}%")
        with col4:
            color = "🔴" if abandonment_rate > 50 else "🟡" if abandonment_rate > 30 else "🟢"
            st.metric("Abandonment Rate", f"{color} {abandonment_rate:.1f}%")

        # Form complexity analysis
        st.markdown("### 🔍 Form Complexity Analysis")

        fields_per_completion = num_fields / (form_completions if form_completions > 0 else 1)
        time_per_field = avg_completion_time / num_fields

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Fields per Completion", f"{fields_per_completion:.1f}")
            st.metric("Time per Field", f"{time_per_field:.0f}s")
        with col2:
            required_percentage = (required_fields / num_fields) * 100
            st.metric("Required Fields %", f"{required_percentage:.0f}%")

            if avg_completion_time > 300:
                st.warning("⚠️ Long completion time may hurt conversions")
            else:
                st.success("✅ Reasonable completion time")

        # Optimization recommendations
        st.markdown("### 💡 Optimization Recommendations")
        recommendations = []

        # Field count recommendations
        if num_fields > 10:
            recommendations.append("🔴 Reduce form fields - consider multi-step form or remove non-essential fields")
        elif num_fields < 5:
            recommendations.append("🟢 Good field count - maintain current length")

        # Required fields
        if required_percentage > 80:
            recommendations.append("🔴 Too many required fields - make some optional to reduce friction")

        # Performance-based recommendations
        if start_rate < 50:
            recommendations.append("🔴 Low start rate - improve form headline and value proposition")

        if completion_rate < 50:
            recommendations.append("🔴 High abandonment - simplify form or add progress indicators")

        if avg_completion_time > 240:
            recommendations.append("🔴 Long completion time - reduce fields or improve UX")

        # Feature recommendations
        if not has_progress_bar and num_fields > 5:
            recommendations.append("📊 Add progress indicator for better user experience")

        if not has_validation:
            recommendations.append("✅ Add real-time validation to prevent errors")

        if not mobile_optimized:
            recommendations.append("📱 Critical: Optimize for mobile devices")

        if not has_autofill:
            recommendations.append("⚡ Enable auto-fill to speed up completion")

        # General recommendations
        recommendations.extend([
            "🎯 A/B test different field orders and labels",
            "🔒 Display security/privacy assurances",
            "📞 Offer alternative contact methods",
            "🎨 Use visual hierarchy to guide attention",
            "📝 Use clear, action-oriented button text"
        ])

        for rec in recommendations:
            st.write(f"• {rec}")

        # Form optimization score
        score = 0
        if start_rate > 60: score += 20
        if completion_rate > 60: score += 25
        if num_fields <= 8: score += 15
        if has_validation: score += 10
        if mobile_optimized: score += 15
        if has_progress_bar and num_fields > 5: score += 10
        if avg_completion_time <= 180: score += 5

        st.markdown(f"### 🎯 Form Optimization Score: {score}/100")

        if score >= 80:
            st.success("🟢 Excellent form optimization!")
        elif score >= 60:
            st.warning("🟡 Good form, but room for improvement")
        else:
            st.error("🔴 Form needs significant optimization")


import random