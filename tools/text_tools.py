import streamlit as st
import re
import base64
import hashlib
import html
import urllib.parse
import uuid
import random
import string
import unicodedata
import textwrap
from collections import Counter
import qrcode
from io import BytesIO
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler
from utils.ai_client import ai_client


def display_tools():
    """Display all text processing tools"""

    # Tool selection
    tool_categories = {
        "Text Conversion": [
            "Case Converter", "Base Converter", "Encoding Converter", "Format Converter"
        ],
        "Text Formatting": [
            "Whitespace Manager", "Line Break Handler", "Character Remover", "Text Normalizer"
        ],
        "Text Analysis": [
            "Word Counter", "Readability Analyzer", "Language Detector", "Sentiment Analyzer", "Content Moderator"
        ],
        "Encoding & Encryption": [
            "Base64 Encoder/Decoder", "URL Encoder/Decoder", "HTML Entity Converter", "Hash Generator"
        ],
        "Text Generation": [
            "Lorem Ipsum Generator", "Random Text Generator", "Password Generator", "UUID Generator"
        ],
        "Language Tools": [
            "Text Translator", "Spell Checker", "Grammar Analyzer", "Text-to-Speech"
        ],
        "Text Extraction": [
            "Email Extractor", "URL Extractor", "Phone Extractor", "Regex Matcher"
        ],
        "Text Editing": [
            "Find and Replace", "Text Merger", "Text Splitter", "Duplicate Remover"
        ],
        "Text Styling": [
            "Markdown Converter", "HTML Formatter", "Text Decorator", "Font Styler"
        ],
        "Miscellaneous": [
            "QR Code Generator", "Text to Image", "Word Cloud", "Text Comparison"
        ]
    }

    selected_category = st.selectbox("Select Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    # Add to recent tools
    add_to_recent(f"Text Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Case Converter":
        case_converter()
    elif selected_tool == "Base Converter":
        base_converter()
    elif selected_tool == "Word Counter":
        word_counter()
    elif selected_tool == "Base64 Encoder/Decoder":
        base64_converter()
    elif selected_tool == "Hash Generator":
        hash_generator()
    elif selected_tool == "Password Generator":
        password_generator()
    elif selected_tool == "QR Code Generator":
        qr_generator()
    elif selected_tool == "Find and Replace":
        find_replace()
    elif selected_tool == "Sentiment Analyzer":
        sentiment_analyzer()
    elif selected_tool == "Text Translator":
        text_translator()
    elif selected_tool == "Email Extractor":
        email_extractor()
    elif selected_tool == "URL Extractor":
        url_extractor()
    elif selected_tool == "Lorem Ipsum Generator":
        lorem_generator()
    elif selected_tool == "UUID Generator":
        uuid_generator()
    elif selected_tool == "Markdown Converter":
        markdown_converter()
    elif selected_tool == "Text Comparison":
        text_comparison()
    elif selected_tool == "Encoding Converter":
        encoding_converter()
    elif selected_tool == "Format Converter":
        format_converter()
    # Text Formatting
    elif selected_tool == "Whitespace Manager":
        whitespace_manager()
    elif selected_tool == "Line Break Handler":
        line_break_handler()
    elif selected_tool == "Character Remover":
        character_remover()
    elif selected_tool == "Text Normalizer":
        text_normalizer()
    # Text Analysis
    elif selected_tool == "Readability Analyzer":
        readability_analyzer()
    elif selected_tool == "Language Detector":
        language_detector()
    elif selected_tool == "Content Moderator":
        content_moderator()
    # Encoding & Encryption
    elif selected_tool == "URL Encoder/Decoder":
        url_encoder_decoder()
    elif selected_tool == "HTML Entity Converter":
        html_entity_converter()
    # Text Generation
    elif selected_tool == "Random Text Generator":
        random_text_generator()
    # Language Tools
    elif selected_tool == "Spell Checker":
        spell_checker()
    elif selected_tool == "Grammar Analyzer":
        grammar_analyzer()
    elif selected_tool == "Text-to-Speech":
        text_to_speech()
    # Text Extraction
    elif selected_tool == "Phone Extractor":
        phone_extractor()
    elif selected_tool == "Regex Matcher":
        regex_matcher()
    # Text Editing
    elif selected_tool == "Text Merger":
        text_merger()
    elif selected_tool == "Text Splitter":
        text_splitter()
    elif selected_tool == "Duplicate Remover":
        duplicate_remover()
    # Text Styling
    elif selected_tool == "HTML Formatter":
        html_formatter()
    elif selected_tool == "Text Decorator":
        text_decorator()
    elif selected_tool == "Font Styler":
        font_styler()
    # Miscellaneous
    elif selected_tool == "Text to Image":
        text_to_image()
    elif selected_tool == "Word Cloud":
        word_cloud()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def case_converter():
    """Text case conversion tool"""
    create_tool_header("Case Converter", "Convert text between different cases", "🔤")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text to convert:", height=150)

    if text:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("UPPERCASE"):
                result = text.upper()
                st.text_area("Result:", result, height=150)
                FileHandler.create_download_link(result.encode(), "uppercase.txt", "text/plain")

        with col2:
            if st.button("lowercase"):
                result = text.lower()
                st.text_area("Result:", result, height=150)
                FileHandler.create_download_link(result.encode(), "lowercase.txt", "text/plain")

        col3, col4 = st.columns(2)

        with col3:
            if st.button("Title Case"):
                result = text.title()
                st.text_area("Result:", result, height=150)
                FileHandler.create_download_link(result.encode(), "titlecase.txt", "text/plain")

        with col4:
            if st.button("Sentence case"):
                sentences = text.split('. ')
                result = '. '.join([s.capitalize() for s in sentences])
                st.text_area("Result:", result, height=150)
                FileHandler.create_download_link(result.encode(), "sentencecase.txt", "text/plain")


def base_converter():
    """Number base conversion tool"""
    create_tool_header("Base Converter", "Convert numbers between different bases", "🔢")

    number = st.text_input("Enter number:")
    from_base = st.selectbox("From base:", [2, 8, 10, 16], index=2)
    to_base = st.selectbox("To base:", [2, 8, 10, 16], index=0)

    if number and st.button("Convert"):
        try:
            # Convert to decimal first
            decimal_value = int(number, from_base)

            # Convert to target base
            result = ""
            if to_base == 2:
                result = bin(decimal_value)[2:]
            elif to_base == 8:
                result = oct(decimal_value)[2:]
            elif to_base == 10:
                result = str(decimal_value)
            elif to_base == 16:
                result = hex(decimal_value)[2:].upper()

            if result:
                st.success(f"Result: {result}")

        except ValueError:
            st.error("Invalid number for the selected base!")


def word_counter():
    """Word and character counting tool"""
    create_tool_header("Word Counter", "Count words, characters, and analyze text", "📊")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt', 'docx'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text to analyze:", height=200)

    if text:
        # Basic counts
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        word_count = len(text.split())
        sentence_count = len([s for s in text.split('.') if s.strip()])
        paragraph_count = len([p for p in text.split('\n\n') if p.strip()])

        # Display metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Characters", char_count)
        col2.metric("Characters (no spaces)", char_count_no_spaces)
        col3.metric("Words", word_count)
        col4.metric("Sentences", sentence_count)
        col5.metric("Paragraphs", paragraph_count)

        # Word frequency
        if st.checkbox("Show word frequency"):
            words = re.findall(r'\b\w+\b', text.lower())
            word_freq = Counter(words)
            most_common = word_freq.most_common(10)

            st.subheader("Most Common Words")
            for word, count in most_common:
                st.write(f"**{word}**: {count}")

        # Reading time estimate
        reading_speed = 200  # words per minute
        reading_time = word_count / reading_speed
        st.info(f"Estimated reading time: {reading_time:.1f} minutes")


def base64_converter():
    """Base64 encoding and decoding tool"""
    create_tool_header("Base64 Converter", "Encode and decode Base64 text", "🔐")

    operation = st.radio("Select operation:", ["Encode", "Decode"])

    if operation == "Encode":
        text = st.text_area("Enter text to encode:")
        if text and st.button("Encode"):
            encoded = base64.b64encode(text.encode()).decode()
            st.text_area("Encoded result:", encoded, height=100)
            FileHandler.create_download_link(encoded.encode(), "encoded.txt", "text/plain")

    else:  # Decode
        encoded_text = st.text_area("Enter Base64 text to decode:")
        if encoded_text and st.button("Decode"):
            try:
                decoded = base64.b64decode(encoded_text).decode()
                st.text_area("Decoded result:", decoded, height=100)
                FileHandler.create_download_link(decoded.encode(), "decoded.txt", "text/plain")
            except Exception as e:
                st.error(f"Invalid Base64 input: {str(e)}")


def hash_generator():
    """Hash generation tool"""
    create_tool_header("Hash Generator", "Generate various types of hashes", "🔒")

    text = st.text_area("Enter text to hash:")
    hash_type = st.selectbox("Select hash type:", ["MD5", "SHA1", "SHA256", "SHA512"])

    if text and st.button("Generate Hash"):
        text_bytes = text.encode()

        hash_result = ""
        if hash_type == "MD5":
            hash_result = hashlib.md5(text_bytes).hexdigest()
        elif hash_type == "SHA1":
            hash_result = hashlib.sha1(text_bytes).hexdigest()
        elif hash_type == "SHA256":
            hash_result = hashlib.sha256(text_bytes).hexdigest()
        elif hash_type == "SHA512":
            hash_result = hashlib.sha512(text_bytes).hexdigest()

        if hash_result:
            st.code(hash_result)
            FileHandler.create_download_link(hash_result.encode(), f"hash_{hash_type.lower()}.txt", "text/plain")


def password_generator():
    """Password generation tool"""
    create_tool_header("Password Generator", "Generate secure passwords", "🔑")

    col1, col2 = st.columns(2)

    with col1:
        length = st.slider("Password length:", 4, 128, 12)
        include_uppercase = st.checkbox("Include uppercase letters", True)
        include_lowercase = st.checkbox("Include lowercase letters", True)
        include_numbers = st.checkbox("Include numbers", True)
        include_symbols = st.checkbox("Include symbols", True)

    with col2:
        exclude_ambiguous = st.checkbox("Exclude ambiguous characters (0, O, l, I)", True)
        num_passwords = st.slider("Number of passwords:", 1, 20, 1)

    if st.button("Generate Passwords"):
        chars = ""
        if include_lowercase:
            chars += string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += "!@#$%^&*"

        if exclude_ambiguous:
            chars = chars.replace('0', '').replace('O', '').replace('l', '').replace('I', '')

        if not chars:
            st.error("Please select at least one character type!")
        else:
            passwords = []
            for _ in range(num_passwords):
                password = ''.join(random.choice(chars) for _ in range(length))
                passwords.append(password)
                st.code(password)

            # Create downloadable file
            password_text = '\n'.join(passwords)
            FileHandler.create_download_link(password_text.encode(), "passwords.txt", "text/plain")


def qr_generator():
    """QR code generation tool"""
    create_tool_header("QR Code Generator", "Generate QR codes from text", "📱")

    text = st.text_area("Enter text for QR code:")

    col1, col2 = st.columns(2)
    with col1:
        size = st.slider("Size (pixels):", 100, 1000, 300)
    with col2:
        border = st.slider("Border size:", 1, 10, 4)

    if text and st.button("Generate QR Code"):
        qr = qrcode.QRCode(version=1, box_size=10, border=border)
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((size, size))

        # Display QR code
        st.image(img, caption="Generated QR Code")

        # Prepare download
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        FileHandler.create_download_link(img_buffer.getvalue(), "qrcode.png", "image/png")


def find_replace():
    """Find and replace tool"""
    create_tool_header("Find and Replace", "Find and replace text patterns", "🔍")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200)

    find_text = st.text_input("Find:")
    replace_text = st.text_input("Replace with:")

    col1, col2, col3 = st.columns(3)
    with col1:
        case_sensitive = st.checkbox("Case sensitive")
    with col2:
        whole_words = st.checkbox("Whole words only")
    with col3:
        use_regex = st.checkbox("Use regular expressions")

    if text and find_text and st.button("Replace"):
        try:
            if use_regex:
                flags = 0 if case_sensitive else re.IGNORECASE
                if whole_words:
                    pattern = r'\b' + re.escape(find_text) + r'\b'
                else:
                    pattern = find_text
                result = re.sub(pattern, replace_text, text, flags=flags)
            else:
                if not case_sensitive:
                    # Case insensitive replacement
                    def replace_func(match):
                        return replace_text

                    pattern = re.escape(find_text)
                    if whole_words:
                        pattern = r'\b' + pattern + r'\b'
                    result = re.sub(pattern, replace_func, text, flags=re.IGNORECASE)
                else:
                    if whole_words:
                        pattern = r'\b' + re.escape(find_text) + r'\b'
                        result = re.sub(pattern, replace_text, text)
                    else:
                        result = text.replace(find_text, replace_text)

            st.text_area("Result:", result, height=200)

            # Count replacements
            original_count = len(re.findall(re.escape(find_text), text, re.IGNORECASE if not case_sensitive else 0))
            st.info(f"Replaced {original_count} occurrences")

            FileHandler.create_download_link(result.encode(), "replaced_text.txt", "text/plain")

        except re.error as e:
            st.error(f"Regular expression error: {str(e)}")


def sentiment_analyzer():
    """AI-powered sentiment analysis"""
    create_tool_header("Sentiment Analyzer", "Analyze text sentiment using AI", "😊")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text to analyze:", height=150)

    if text and st.button("Analyze Sentiment"):
        with st.spinner("Analyzing sentiment..."):
            result = ai_client.analyze_sentiment(text)

            if 'error' not in result:
                st.subheader("Sentiment Analysis Results")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Sentiment", result.get('sentiment', 'Unknown'))
                with col2:
                    confidence = result.get('confidence', 0)
                    st.metric("Confidence", f"{confidence:.2%}")

                if 'explanation' in result:
                    st.write("**Analysis:**", result['explanation'])

                if 'indicators' in result:
                    st.write("**Key Indicators:**", ', '.join(result['indicators']))
            else:
                st.error(result['error'])


def text_translator():
    """AI-powered text translation"""
    create_tool_header("Text Translator", "Translate text using AI", "🌍")

    text = st.text_area("Enter text to translate:", height=150)
    target_language = st.selectbox("Target language:", [
        "Spanish", "French", "German", "Italian", "Portuguese", "Russian",
        "Chinese", "Japanese", "Korean", "Arabic", "Hindi", "Dutch"
    ])

    if text and st.button("Translate"):
        with st.spinner("Translating..."):
            result = ai_client.translate_text(text, target_language)
            st.text_area("Translation:", result, height=150)
            FileHandler.create_download_link(result.encode(), f"translation_{target_language.lower()}.txt",
                                             "text/plain")


def email_extractor():
    """Extract email addresses from text"""
    create_tool_header("Email Extractor", "Extract email addresses from text", "📧")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text containing emails:", height=200)

    if text and st.button("Extract Emails"):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)

        if emails:
            st.success(f"Found {len(emails)} email(s):")
            for email in emails:
                st.write(f"• {email}")

            # Create downloadable list
            email_list = '\n'.join(emails)
            FileHandler.create_download_link(email_list.encode(), "extracted_emails.txt", "text/plain")
        else:
            st.info("No email addresses found.")


def url_extractor():
    """Extract URLs from text"""
    create_tool_header("URL Extractor", "Extract URLs from text", "🔗")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text containing URLs:", height=200)

    if text and st.button("Extract URLs"):
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)

        if urls:
            st.success(f"Found {len(urls)} URL(s):")
            for url in urls:
                st.write(f"• {url}")

            # Create downloadable list
            url_list = '\n'.join(urls)
            FileHandler.create_download_link(url_list.encode(), "extracted_urls.txt", "text/plain")
        else:
            st.info("No URLs found.")


def lorem_generator():
    """Lorem ipsum text generator"""
    create_tool_header("Lorem Ipsum Generator", "Generate placeholder text", "📄")

    col1, col2 = st.columns(2)
    with col1:
        num_paragraphs = st.slider("Number of paragraphs:", 1, 10, 3)
    with col2:
        start_with_lorem = st.checkbox("Start with 'Lorem ipsum...'", True)

    if st.button("Generate Text"):
        lorem_words = [
            "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
            "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
            "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud",
            "exercitation", "ullamco", "laboris", "nisi", "aliquip", "ex", "ea", "commodo",
            "consequat", "duis", "aute", "irure", "in", "reprehenderit", "voluptate",
            "velit", "esse", "cillum", "fugiat", "nulla", "pariatur", "excepteur", "sint",
            "occaecat", "cupidatat", "non", "proident", "sunt", "culpa", "qui", "officia",
            "deserunt", "mollit", "anim", "id", "est", "laborum"
        ]

        paragraphs = []

        for i in range(num_paragraphs):
            if i == 0 and start_with_lorem:
                paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                remaining_words = random.randint(30, 80)
            else:
                paragraph = ""
                remaining_words = random.randint(40, 100)

            words = []
            for _ in range(remaining_words):
                words.append(random.choice(lorem_words))

            paragraph += ' '.join(words) + '.'
            paragraph = paragraph.capitalize()
            paragraphs.append(paragraph)

        result = '\n\n'.join(paragraphs)
        st.text_area("Generated Lorem Ipsum:", result, height=300)
        FileHandler.create_download_link(result.encode(), "lorem_ipsum.txt", "text/plain")


def uuid_generator():
    """UUID generation tool"""
    create_tool_header("UUID Generator", "Generate universally unique identifiers", "🆔")

    col1, col2 = st.columns(2)
    with col1:
        num_uuids = st.slider("Number of UUIDs:", 1, 100, 1)
    with col2:
        uuid_version = st.selectbox("UUID Version:", [1, 4], index=1)

    if st.button("Generate UUIDs"):
        uuids = []
        for _ in range(num_uuids):
            if uuid_version == 1:
                new_uuid = str(uuid.uuid1())
            else:  # Version 4
                new_uuid = str(uuid.uuid4())
            uuids.append(new_uuid)
            st.code(new_uuid)

        # Create downloadable file
        uuid_text = '\n'.join(uuids)
        FileHandler.create_download_link(uuid_text.encode(), "uuids.txt", "text/plain")


def markdown_converter():
    """Markdown to HTML converter"""
    create_tool_header("Markdown Converter", "Convert Markdown to HTML", "📝")

    # File upload option
    uploaded_file = FileHandler.upload_files(['md', 'txt'], accept_multiple=False)

    if uploaded_file:
        markdown_text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Markdown", markdown_text, height=100, disabled=True)
    else:
        markdown_text = st.text_area("Enter Markdown text:", height=200)

    if markdown_text and st.button("Convert to HTML"):
        # Simple markdown to HTML conversion
        html_text = markdown_text

        # Headers
        html_text = re.sub(r'^### (.*)', r'<h3>\1</h3>', html_text, flags=re.MULTILINE)
        html_text = re.sub(r'^## (.*)', r'<h2>\1</h2>', html_text, flags=re.MULTILINE)
        html_text = re.sub(r'^# (.*)', r'<h1>\1</h1>', html_text, flags=re.MULTILINE)

        # Bold and italic
        html_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_text)
        html_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_text)

        # Links
        html_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_text)

        # Line breaks
        html_text = html_text.replace('\n', '<br>\n')

        st.text_area("HTML Output:", html_text, height=200)
        st.subheader("Preview:")
        st.markdown(html_text, unsafe_allow_html=True)

        FileHandler.create_download_link(html_text.encode(), "converted.html", "text/html")


def text_comparison():
    """Compare two texts"""
    create_tool_header("Text Comparison", "Compare two texts for differences", "🔍")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Text 1")
        text1 = st.text_area("Enter first text:", height=200, key="text1")

    with col2:
        st.subheader("Text 2")
        text2 = st.text_area("Enter second text:", height=200, key="text2")

    if text1 and text2 and st.button("Compare Texts"):
        # Basic comparison metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Length Difference", abs(len(text1) - len(text2)))
        with col2:
            similarity = calculate_similarity(text1, text2)
            st.metric("Similarity", f"{similarity:.1%}")
        with col3:
            word_diff = abs(len(text1.split()) - len(text2.split()))
            st.metric("Word Count Difference", word_diff)

        # Character-by-character comparison
        st.subheader("Detailed Comparison")

        if len(text1) == len(text2):
            differences = []
            for i, (c1, c2) in enumerate(zip(text1, text2)):
                if c1 != c2:
                    differences.append(f"Position {i}: '{c1}' vs '{c2}'")

            if differences:
                st.write(f"Found {len(differences)} character differences:")
                for diff in differences[:20]:  # Show first 20 differences
                    st.write(f"• {diff}")
                if len(differences) > 20:
                    st.write(f"... and {len(differences) - 20} more")
            else:
                st.success("Texts are identical!")
        else:
            st.info("Texts have different lengths. Exact character comparison not possible.")


def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate similarity between two texts"""
    # Simple similarity based on common words
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    if not words1 and not words2:
        return 1.0
    if not words1 or not words2:
        return 0.0

    common_words = words1.intersection(words2)
    total_words = words1.union(words2)

    return len(common_words) / len(total_words)


def encoding_converter():
    """Text encoding conversion tool"""
    create_tool_header("Encoding Converter", "Convert text between different character encodings", "🔄")

    # File upload option
    st.subheader("Input Text")
    input_method = st.radio("Choose input method:", ["Text Input", "File Upload"])

    text_content = ""
    if input_method == "File Upload":
        uploaded_file = FileHandler.upload_files(['txt', 'csv', 'json', 'xml'], accept_multiple=False)
        if uploaded_file:
            try:
                # Try to read with different encodings
                content = uploaded_file[0].read()
                detected_encoding = detect_encoding(content)
                st.info(f"Detected encoding: {detected_encoding}")
                text_content = content.decode(detected_encoding)
                st.text_area("File Content Preview",
                             text_content[:500] + "..." if len(text_content) > 500 else text_content, height=100,
                             disabled=True)
            except Exception as e:
                st.error(f"Error reading file: {e}")
    else:
        text_content = st.text_area("Enter text to convert:", height=150)

    if text_content:
        # Encoding options
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Source Encoding")
            source_encoding = st.selectbox("From encoding:", [
                "utf-8", "ascii", "latin-1", "cp1252", "utf-16", "utf-32",
                "iso-8859-1", "cp850", "cp1251", "big5", "shift_jis", "euc-jp"
            ])

        with col2:
            st.subheader("Target Encoding")
            target_encoding = st.selectbox("To encoding:", [
                "utf-8", "ascii", "latin-1", "cp1252", "utf-16", "utf-32",
                "iso-8859-1", "cp850", "cp1251", "big5", "shift_jis", "euc-jp"
            ], index=0)

        # Conversion options
        st.subheader("Conversion Options")
        error_handling = st.selectbox("Error Handling:", [
            "strict", "ignore", "replace", "xmlcharrefreplace", "backslashreplace"
        ], index=2)  # Default to 'replace'

        if st.button("Convert Encoding"):
            try:
                # Convert text encoding
                if source_encoding != target_encoding:
                    # First encode with source encoding, then decode with target
                    encoded_bytes = text_content.encode(source_encoding, errors=error_handling)
                    converted_text = encoded_bytes.decode(target_encoding, errors=error_handling)
                else:
                    converted_text = text_content
                    st.info("Source and target encodings are the same.")

                # Display results
                st.subheader("Conversion Results")

                # Show byte information
                col1, col2, col3 = st.columns(3)
                with col1:
                    original_bytes = len(text_content.encode(source_encoding, errors=error_handling))
                    st.metric("Original Size", f"{original_bytes} bytes")
                with col2:
                    converted_bytes = len(converted_text.encode(target_encoding, errors=error_handling))
                    st.metric("Converted Size", f"{converted_bytes} bytes")
                with col3:
                    size_diff = converted_bytes - original_bytes
                    st.metric("Size Difference", f"{size_diff:+d} bytes")

                # Display converted text
                st.text_area("Converted Text:", converted_text, height=200)

                # Download options
                st.subheader("Download Options")
                filename = f"converted_{target_encoding.replace('-', '_')}.txt"
                FileHandler.create_download_link(
                    converted_text.encode(target_encoding, errors=error_handling),
                    filename,
                    "text/plain"
                )

                # Show encoding details
                with st.expander("Encoding Details"):
                    st.write(f"**Source Encoding:** {source_encoding}")
                    st.write(f"**Target Encoding:** {target_encoding}")
                    st.write(f"**Error Handling:** {error_handling}")
                    st.write(f"**Character Count:** {len(converted_text)}")

                    # Show first few bytes in hex
                    hex_bytes = converted_text.encode(target_encoding, errors=error_handling)[:50].hex()
                    st.write(f"**First 50 bytes (hex):** {hex_bytes}")

            except Exception as e:
                st.error(f"Encoding conversion failed: {e}")


def format_converter():
    """Text format conversion tool"""
    create_tool_header("Format Converter", "Convert text between different data formats", "📋")

    # Input options
    st.subheader("Input Data")
    input_method = st.radio("Choose input method:", ["Text Input", "File Upload"])

    input_text = ""
    source_format = "text"

    if input_method == "File Upload":
        uploaded_file = FileHandler.upload_files(['txt', 'json', 'csv', 'xml', 'yaml'], accept_multiple=False)
        if uploaded_file:
            input_text = FileHandler.process_text_file(uploaded_file[0])
            file_extension = uploaded_file[0].name.split('.')[-1].lower()
            source_format = detect_format_from_extension(file_extension)
            st.text_area("File Content Preview", input_text[:1000] + "..." if len(input_text) > 1000 else input_text,
                         height=150, disabled=True)
    else:
        input_text = st.text_area("Enter data to convert:", height=200)

    if input_text:
        # Format selection
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Source Format")
            source_format = st.selectbox("From format:", [
                "json", "csv", "xml", "yaml", "text", "markdown", "html", "ini"
            ], index=get_format_index(source_format))

        with col2:
            st.subheader("Target Format")
            target_format = st.selectbox("To format:", [
                "json", "csv", "xml", "yaml", "text", "markdown", "html", "ini"
            ])

        # Conversion options
        st.subheader("Conversion Options")

        # Initialize default values
        csv_delimiter = ","
        csv_quote_char = '"'
        has_header = True
        pretty_json = True
        json_indent = 2
        xml_root_tag = "root"
        xml_item_tag = "item"

        # CSV specific options
        if source_format == "csv" or target_format == "csv":
            col1, col2, col3 = st.columns(3)
            with col1:
                csv_delimiter = st.text_input("CSV Delimiter:", ",")
            with col2:
                csv_quote_char = st.text_input("Quote Character:", '"')
            with col3:
                has_header = st.checkbox("Has Header Row", True)

        # JSON specific options
        if target_format == "json":
            pretty_json = st.checkbox("Pretty Print JSON", True)
            if pretty_json:
                json_indent = st.number_input("JSON Indent Spaces:", 1, 8, 2)
            else:
                json_indent = 0

        # XML specific options
        if target_format == "xml":
            xml_root_tag = st.text_input("XML Root Tag:", "root")
            xml_item_tag = st.text_input("XML Item Tag:", "item")

        if st.button("Convert Format"):
            try:
                # Parse source format
                parsed_data = parse_format(input_text, source_format, csv_delimiter, has_header)

                # Convert to target format
                converted_text = convert_to_format(parsed_data, target_format,
                                                   pretty_json, json_indent,
                                                   xml_root_tag, xml_item_tag,
                                                   csv_delimiter)

                # Display results
                st.subheader("Conversion Results")

                # Show conversion statistics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Original Size", f"{len(input_text)} chars")
                with col2:
                    st.metric("Converted Size", f"{len(converted_text)} chars")
                with col3:
                    size_change = len(converted_text) - len(input_text)
                    st.metric("Size Change", f"{size_change:+d} chars")

                # Display converted data
                st.text_area("Converted Data:", converted_text, height=300)

                # Download option
                file_extension = get_file_extension(target_format)
                filename = f"converted_data.{file_extension}"
                FileHandler.create_download_link(converted_text.encode(), filename, get_mime_type(target_format))

                # Show format details
                with st.expander("Conversion Details"):
                    st.write(f"**Source Format:** {source_format}")
                    st.write(f"**Target Format:** {target_format}")
                    if isinstance(parsed_data, list):
                        st.write(f"**Records Count:** {len(parsed_data)}")
                    elif isinstance(parsed_data, dict):
                        st.write(f"**Keys Count:** {len(parsed_data)}")
                    st.write(f"**Character Count:** {len(converted_text)}")

            except Exception as e:
                st.error(f"Format conversion failed: {e}")
                st.write("Please check your input data format and try again.")


# Helper functions for encoding converter
def detect_encoding(byte_content):
    """Simple encoding detection"""
    encodings_to_try = ['utf-8', 'ascii', 'latin-1', 'cp1252', 'utf-16']

    for encoding in encodings_to_try:
        try:
            byte_content.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue

    return 'utf-8'  # Default fallback


# Helper functions for format converter
def detect_format_from_extension(extension):
    """Detect format from file extension"""
    format_map = {
        'json': 'json',
        'csv': 'csv',
        'xml': 'xml',
        'yaml': 'yaml',
        'yml': 'yaml',
        'md': 'markdown',
        'html': 'html',
        'htm': 'html',
        'ini': 'ini',
        'txt': 'text'
    }
    return format_map.get(extension, 'text')


def get_format_index(format_name):
    """Get index for format selection"""
    formats = ["json", "csv", "xml", "yaml", "text", "markdown", "html", "ini"]
    try:
        return formats.index(format_name)
    except ValueError:
        return 4  # Default to 'text'


def parse_format(input_text, source_format, delimiter=',', has_header=True):
    """Parse input text based on source format"""
    import json
    import csv
    from io import StringIO

    if source_format == "json":
        return json.loads(input_text)

    elif source_format == "csv":
        csv_file = StringIO(input_text)
        reader = csv.DictReader(csv_file, delimiter=delimiter) if has_header else csv.reader(csv_file,
                                                                                             delimiter=delimiter)
        return list(reader)

    elif source_format == "xml":
        # Simple XML to dict conversion (basic implementation)
        import xml.etree.ElementTree as ET
        root = ET.fromstring(input_text)
        return xml_to_dict(root)

    elif source_format == "yaml":
        # Basic YAML parsing (simplified)
        lines = input_text.strip().split('\n')
        result = {}
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                result[key.strip()] = value.strip()
        return result

    else:  # text, markdown, html, ini
        return {"content": input_text, "format": source_format}


def convert_to_format(data, target_format, pretty_json=True, json_indent=2,
                      xml_root_tag='root', xml_item_tag='item', csv_delimiter=','):
    """Convert parsed data to target format"""
    import json
    import csv
    from io import StringIO

    if target_format == "json":
        if pretty_json:
            return json.dumps(data, indent=json_indent, ensure_ascii=False)
        else:
            return json.dumps(data, ensure_ascii=False)

    elif target_format == "csv":
        output = StringIO()
        if isinstance(data, list) and data:
            if isinstance(data[0], dict):
                # List of dictionaries
                fieldnames = data[0].keys()
                writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=csv_delimiter)
                writer.writeheader()
                writer.writerows(data)
            else:
                # List of lists
                writer = csv.writer(output, delimiter=csv_delimiter)
                writer.writerows(data)
        return output.getvalue()

    elif target_format == "xml":
        return dict_to_xml(data, xml_root_tag, xml_item_tag)

    elif target_format == "yaml":
        return dict_to_yaml(data)

    elif target_format == "markdown":
        return dict_to_markdown(data)

    elif target_format == "html":
        return dict_to_html(data)

    elif target_format == "ini":
        return dict_to_ini(data)

    else:  # text
        if isinstance(data, dict) and "content" in data:
            return data["content"]
        return str(data)


def xml_to_dict(element):
    """Convert XML element to dictionary"""
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result


def dict_to_xml(data, root_tag='root', item_tag='item'):
    """Convert dictionary to XML string"""

    def build_xml(obj, tag):
        if isinstance(obj, dict):
            xml = f"<{tag}>"
            for key, value in obj.items():
                xml += build_xml(value, key)
            xml += f"</{tag}>"
            return xml
        elif isinstance(obj, list):
            xml = ""
            for item in obj:
                xml += build_xml(item, item_tag)
            return xml
        else:
            return f"<{tag}>{str(obj)}</{tag}>"

    return f'<?xml version="1.0" encoding="UTF-8"?>\n{build_xml(data, root_tag)}'


def dict_to_yaml(data):
    """Convert dictionary to YAML string (simplified)"""

    def format_value(value, indent=0):
        spaces = "  " * indent
        if isinstance(value, dict):
            result = ""
            for k, v in value.items():
                result += f"\n{spaces}{k}:"
                if isinstance(v, (dict, list)):
                    result += format_value(v, indent + 1)
                else:
                    result += f" {v}"
            return result
        elif isinstance(value, list):
            result = ""
            for item in value:
                result += f"\n{spaces}- {item}"
            return result
        else:
            return f" {value}"

    return format_value(data).strip()


def dict_to_markdown(data):
    """Convert dictionary to Markdown string"""
    if isinstance(data, dict) and "content" in data:
        return data["content"]

    result = "# Data\n\n"
    if isinstance(data, dict):
        for key, value in data.items():
            result += f"## {key}\n\n{value}\n\n"
    elif isinstance(data, list):
        for i, item in enumerate(data, 1):
            result += f"{i}. {item}\n"
    else:
        result += str(data)

    return result


def dict_to_html(data):
    """Convert dictionary to HTML string"""
    if isinstance(data, dict) and "content" in data:
        return f"<html><body>{data['content']}</body></html>"

    html = "<html><head><title>Converted Data</title></head><body>"

    if isinstance(data, dict):
        html += "<dl>"
        for key, value in data.items():
            html += f"<dt>{key}</dt><dd>{value}</dd>"
        html += "</dl>"
    elif isinstance(data, list):
        html += "<ul>"
        for item in data:
            html += f"<li>{item}</li>"
        html += "</ul>"
    else:
        html += f"<p>{data}</p>"

    html += "</body></html>"
    return html


def dict_to_ini(data):
    """Convert dictionary to INI string"""
    if not isinstance(data, dict):
        return "[DEFAULT]\ndata = " + str(data)

    ini = ""
    for section, values in data.items():
        ini += f"[{section}]\n"
        if isinstance(values, dict):
            for key, value in values.items():
                ini += f"{key} = {value}\n"
        else:
            ini += f"value = {values}\n"
        ini += "\n"

    return ini


def get_file_extension(format_name):
    """Get file extension for format"""
    extensions = {
        'json': 'json',
        'csv': 'csv',
        'xml': 'xml',
        'yaml': 'yaml',
        'markdown': 'md',
        'html': 'html',
        'ini': 'ini',
        'text': 'txt'
    }
    return extensions.get(format_name, 'txt')


def get_mime_type(format_name):
    """Get MIME type for format"""
    mime_types = {
        'json': 'application/json',
        'csv': 'text/csv',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'markdown': 'text/markdown',
        'html': 'text/html',
        'ini': 'text/plain',
        'text': 'text/plain'
    }
    return mime_types.get(format_name, 'text/plain')


# Text Formatting Tools

def whitespace_manager():
    """Manage whitespace in text"""
    create_tool_header("Whitespace Manager", "Clean and manage whitespace in text", "🔧")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200,
                            placeholder="Text with    extra    spaces\nand\n\n\nmultiple\nline\nbreaks")

    if text:
        col1, col2 = st.columns(2)

        with col1:
            remove_extra_spaces = st.checkbox("Remove extra spaces", True)
            remove_tabs = st.checkbox("Remove tabs", False)

        with col2:
            remove_extra_newlines = st.checkbox("Remove extra newlines", True)
            normalize_spaces = st.checkbox("Normalize all whitespace", False)

        if st.button("Process Whitespace"):
            result = text

            if remove_extra_spaces:
                result = re.sub(r' +', ' ', result)

            if remove_tabs:
                result = result.replace('\t', ' ')

            if remove_extra_newlines:
                result = re.sub(r'\n+', '\n', result)

            if normalize_spaces:
                result = ' '.join(result.split())

            st.text_area("Result:", result, height=200)
            FileHandler.create_download_link(result.encode(), "whitespace_cleaned.txt", "text/plain")


def line_break_handler():
    """Handle line breaks in text"""
    create_tool_header("Line Break Handler", "Convert between different line break formats", "📄")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200, placeholder="Line 1\nLine 2\nLine 3\n\nParagraph 2")

    if text:
        operation = st.selectbox("Operation:", [
            "Convert to single line",
            "Add line breaks at character limit",
            "Convert to paragraph format",
            "Unix to Windows line endings",
            "Windows to Unix line endings"
        ])

        if operation == "Add line breaks at character limit":
            char_limit = st.slider("Character limit:", 20, 200, 80)

        if st.button("Process Line Breaks"):
            if operation == "Convert to single line":
                result = text.replace('\n', ' ').replace('\r', '')
            elif operation == "Add line breaks at character limit":
                result = textwrap.fill(text, width=char_limit)
            elif operation == "Convert to paragraph format":
                paragraphs = text.split('\n\n')
                result = '\n\n'.join([' '.join(p.split()) for p in paragraphs])
            elif operation == "Unix to Windows line endings":
                result = text.replace('\n', '\r\n')
            elif operation == "Windows to Unix line endings":
                result = text.replace('\r\n', '\n')

            st.text_area("Result:", result, height=200)
            FileHandler.create_download_link(result.encode(), "line_breaks_processed.txt", "text/plain")


def character_remover():
    """Remove specific characters from text"""
    create_tool_header("Character Remover", "Remove unwanted characters from text", "🗑️")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200, placeholder="Remove @#$% special characters!")

    if text:
        removal_type = st.selectbox("What to remove:", [
            "Custom characters",
            "All numbers",
            "All punctuation",
            "Non-ASCII characters",
            "Accents/diacritics",
            "All whitespace",
            "HTML tags"
        ])

        if removal_type == "Custom characters":
            chars_to_remove = st.text_input("Characters to remove:", placeholder="@#$%!?")

        if st.button("Remove Characters"):
            result = text

            if removal_type == "Custom characters" and chars_to_remove:
                for char in chars_to_remove:
                    result = result.replace(char, '')
            elif removal_type == "All numbers":
                result = re.sub(r'\d', '', result)
            elif removal_type == "All punctuation":
                result = re.sub(r'[^\w\s]', '', result)
            elif removal_type == "Non-ASCII characters":
                result = ''.join(char for char in result if ord(char) < 128)
            elif removal_type == "Accents/diacritics":
                result = ''.join(c for c in unicodedata.normalize('NFD', result)
                                 if unicodedata.category(c) != 'Mn')
            elif removal_type == "All whitespace":
                result = re.sub(r'\s', '', result)
            elif removal_type == "HTML tags":
                result = re.sub(r'<[^>]+>', '', result)

            st.text_area("Result:", result, height=200)
            FileHandler.create_download_link(result.encode(), "characters_removed.txt", "text/plain")


def text_normalizer():
    """Normalize text formatting"""
    create_tool_header("Text Normalizer", "Normalize text formatting and encoding", "📋")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200, placeholder="Ñormalize thîs tëxt wíth spéciàl charácters")

    if text:
        col1, col2 = st.columns(2)

        with col1:
            normalize_case = st.checkbox("Normalize case")
            case_option = st.selectbox("Case:", ["lowercase", "UPPERCASE", "Title Case"], disabled=not normalize_case)

        with col2:
            normalize_unicode = st.checkbox("Normalize Unicode", True)
            unicode_form = st.selectbox("Unicode form:", ["NFC", "NFD", "NFKC", "NFKD"], disabled=not normalize_unicode)

        normalize_quotes = st.checkbox("Normalize quotes")
        normalize_dashes = st.checkbox("Normalize dashes")

        if st.button("Normalize Text"):
            result = text

            if normalize_unicode:
                result = unicodedata.normalize(unicode_form, result)

            if normalize_case:
                if case_option == "lowercase":
                    result = result.lower()
                elif case_option == "UPPERCASE":
                    result = result.upper()
                elif case_option == "Title Case":
                    result = result.title()

            if normalize_quotes:
                # Convert various quote types to standard quotes
                result = result.replace('"', '"').replace('"', '"')
                result = result.replace(''', "'").replace(''', "'")

            if normalize_dashes:
                # Convert various dash types to standard hyphen
                result = result.replace('–', '-').replace('—', '-')

            st.text_area("Result:", result, height=200)
            FileHandler.create_download_link(result.encode(), "normalized_text.txt", "text/plain")


# Text Analysis Tools

def readability_analyzer():
    """Analyze text readability"""
    create_tool_header("Readability Analyzer", "Analyze text readability and complexity", "📊")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text to analyze:", height=200,
                            placeholder="The quick brown fox jumps over the lazy dog. This sentence is easy to read.")

    if text and st.button("Analyze Readability"):
        analysis = analyze_readability(text)

        st.subheader("📊 Readability Analysis")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Words", analysis['word_count'])
        with col2:
            st.metric("Sentences", analysis['sentence_count'])
        with col3:
            st.metric("Avg Words/Sentence", f"{analysis['avg_words_per_sentence']:.1f}")
        with col4:
            st.metric("Avg Syllables/Word", f"{analysis['avg_syllables_per_word']:.1f}")

        # Readability scores
        st.subheader("📈 Readability Scores")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Flesch Reading Ease", f"{analysis['flesch_reading_ease']:.1f}")
            if analysis['flesch_reading_ease'] >= 90:
                st.success("Very Easy to read")
            elif analysis['flesch_reading_ease'] >= 80:
                st.info("Easy to read")
            elif analysis['flesch_reading_ease'] >= 70:
                st.info("Fairly Easy to read")
            elif analysis['flesch_reading_ease'] >= 60:
                st.warning("Standard difficulty")
            else:
                st.error("Difficult to read")

        with col2:
            st.metric("Flesch-Kincaid Grade", f"{analysis['flesch_kincaid_grade']:.1f}")
            st.info(f"Grade {int(analysis['flesch_kincaid_grade'])} reading level")


def analyze_readability(text):
    """Calculate readability metrics"""
    # Count words
    words = len(text.split())

    # Count sentences
    sentences = len([s for s in re.split(r'[.!?]+', text) if s.strip()])

    # Count syllables (simplified)
    def count_syllables(word):
        word = word.lower()
        vowels = 'aeiouy'
        syllable_count = 0
        previous_was_vowel = False

        for i, char in enumerate(word):
            if char in vowels:
                if not previous_was_vowel:
                    syllable_count += 1
                previous_was_vowel = True
            else:
                previous_was_vowel = False

        # Handle silent e
        if word.endswith('e') and syllable_count > 1:
            syllable_count -= 1

        return max(1, syllable_count)

    syllables = sum(count_syllables(word) for word in re.findall(r'\b\w+\b', text))

    # Calculate metrics
    avg_words_per_sentence = words / max(sentences, 1)
    avg_syllables_per_word = syllables / max(words, 1)

    # Flesch Reading Ease Score
    flesch_reading_ease = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)

    # Flesch-Kincaid Grade Level
    flesch_kincaid_grade = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59

    return {
        'word_count': words,
        'sentence_count': sentences,
        'syllable_count': syllables,
        'avg_words_per_sentence': avg_words_per_sentence,
        'avg_syllables_per_word': avg_syllables_per_word,
        'flesch_reading_ease': max(0, flesch_reading_ease),
        'flesch_kincaid_grade': max(0, flesch_kincaid_grade)
    }


def language_detector():
    """Detect language of text"""
    create_tool_header("Language Detector", "Detect the language of text using AI", "🌍")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200,
                            placeholder="Hello world! How are you? / Hola mundo! ¿Cómo estás? / Bonjour le monde!")

    if text and st.button("Detect Language"):
        with st.spinner("Detecting language..."):
            result = ai_client.detect_language(text)

            if 'error' not in result:
                st.success(f"**Detected Language:** {result.get('language', 'Unknown')}")

                if 'confidence' in result:
                    st.metric("Confidence", f"{result['confidence']:.1%}")

                if 'explanation' in result:
                    st.info(f"**Explanation:** {result['explanation']}")
            else:
                st.error(result['error'])


# Encoding & Encryption Tools

def url_encoder_decoder():
    """Encode and decode URLs"""
    create_tool_header("URL Encoder/Decoder", "Encode and decode URL components", "🔗")

    operation = st.radio("Operation:", ["Encode", "Decode"])

    if operation == "Encode":
        text = st.text_area("Enter text to encode:", placeholder="Hello World! This is a test.")
        if text and st.button("Encode"):
            encoded = urllib.parse.quote(text)
            st.code(encoded)
            st.success("Text encoded successfully!")
            FileHandler.create_download_link(encoded.encode(), "encoded_url.txt", "text/plain")
    else:
        text = st.text_area("Enter URL-encoded text to decode:", placeholder="Hello%20World%21%20This%20is%20a%20test.")
        if text and st.button("Decode"):
            try:
                decoded = urllib.parse.unquote(text)
                st.code(decoded)
                st.success("Text decoded successfully!")
                FileHandler.create_download_link(decoded.encode(), "decoded_url.txt", "text/plain")
            except Exception as e:
                st.error(f"Error decoding: {str(e)}")


def html_entity_converter():
    """Convert HTML entities"""
    create_tool_header("HTML Entity Converter", "Convert between HTML entities and characters", "🔤")

    operation = st.radio("Operation:", ["Encode", "Decode"])

    if operation == "Encode":
        text = st.text_area("Enter text to encode:", placeholder="<script>alert('Hello & \"World\"');</script>")
        if text and st.button("Encode"):
            encoded = html.escape(text)
            st.code(encoded)
            st.success("Text encoded successfully!")
            FileHandler.create_download_link(encoded.encode(), "html_encoded.txt", "text/plain")
    else:
        text = st.text_area("Enter HTML entities to decode:",
                            placeholder="&lt;script&gt;alert(&#x27;Hello &amp; &quot;World&quot;&#x27;);&lt;/script&gt;")
        if text and st.button("Decode"):
            try:
                decoded = html.unescape(text)
                st.code(decoded)
                st.success("Text decoded successfully!")
                FileHandler.create_download_link(decoded.encode(), "html_decoded.txt", "text/plain")
            except Exception as e:
                st.error(f"Error decoding: {str(e)}")


# Text Generation Tools

def random_text_generator():
    """Generate random text"""
    create_tool_header("Random Text Generator", "Generate random text for testing", "🎲")

    text_type = st.selectbox("Text type:",
                             ["Random words", "Random sentences", "Random paragraphs", "Lorem ipsum style"])

    col1, col2 = st.columns(2)
    with col1:
        if text_type == "Random words":
            count = st.slider("Number of words:", 5, 100, 20)
        elif text_type == "Random sentences":
            count = st.slider("Number of sentences:", 1, 20, 5)
        elif text_type == "Random paragraphs":
            count = st.slider("Number of paragraphs:", 1, 10, 3)
        else:
            count = st.slider("Number of paragraphs:", 1, 10, 3)

    with col2:
        if text_type in ["Random sentences", "Random paragraphs"]:
            words_per_sentence = st.slider("Words per sentence:", 5, 20, 10)

    if st.button("Generate Text"):
        result = generate_random_text(text_type, count,
                                      words_per_sentence if text_type in ["Random sentences",
                                                                          "Random paragraphs"] else None)
        st.text_area("Generated text:", result, height=300)
        FileHandler.create_download_link(result.encode(), "random_text.txt", "text/plain")


def generate_random_text(text_type, count, words_per_sentence=None):
    """Generate random text based on type"""
    words = [
        "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", "cat", "mouse",
        "house", "car", "tree", "book", "computer", "phone", "table", "chair", "window", "door",
        "happy", "sad", "fast", "slow", "big", "small", "red", "blue", "green", "yellow",
        "run", "walk", "jump", "sit", "stand", "eat", "drink", "sleep", "work", "play"
    ]

    if text_type == "Random words":
        return " ".join(random.choices(words, k=count))

    elif text_type == "Random sentences":
        sentences = []
        for _ in range(count):
            sentence_words = random.choices(words, k=words_per_sentence or 10)
            sentence = " ".join(sentence_words).capitalize() + "."
            sentences.append(sentence)
        return " ".join(sentences)

    elif text_type == "Random paragraphs":
        paragraphs = []
        for _ in range(count):
            sentences = []
            for _ in range(random.randint(3, 6)):
                sentence_words = random.choices(words, k=words_per_sentence or 10)
                sentence = " ".join(sentence_words).capitalize() + "."
                sentences.append(sentence)
            paragraphs.append(" ".join(sentences))
        return "\n\n".join(paragraphs)

    else:  # Lorem ipsum style
        lorem_words = [
            "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
            "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
            "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud"
        ]

        paragraphs = []
        for _ in range(count):
            sentences = []
            for _ in range(random.randint(4, 8)):
                sentence_words = random.choices(lorem_words, k=random.randint(6, 12))
                sentence = " ".join(sentence_words).capitalize() + "."
                sentences.append(sentence)
            paragraphs.append(" ".join(sentences))
        return "\n\n".join(paragraphs)


# Language Tools

def spell_checker():
    """Check spelling using AI"""
    create_tool_header("Spell Checker", "Check and correct spelling using AI", "✏️")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text to check:", height=200,
                            placeholder="Ths sentnce has speling erors that ned to be fixd.")

    if text and st.button("Check Spelling"):
        with st.spinner("Checking spelling..."):
            result = ai_client.check_spelling(text)

            if 'error' not in result:
                st.subheader("Spell Check Results")

                if result.get('corrected_text'):
                    st.text_area("Corrected text:", result['corrected_text'], height=200)
                    FileHandler.create_download_link(result['corrected_text'].encode(), "corrected_text.txt",
                                                     "text/plain")

                if result.get('corrections'):
                    st.subheader("Corrections made:")
                    for correction in result['corrections']:
                        st.write(f"• **{correction.get('original', '')}** → **{correction.get('corrected', '')}**")

                if not result.get('corrections'):
                    st.success("✅ No spelling errors found!")
            else:
                st.error(result['error'])


def grammar_analyzer():
    """Analyze grammar using AI"""
    create_tool_header("Grammar Analyzer", "Analyze and improve grammar using AI", "📝")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text to analyze:", height=200,
                            placeholder="This sentence have grammar error that need fixing.")

    if text and st.button("Analyze Grammar"):
        with st.spinner("Analyzing grammar..."):
            result = ai_client.check_grammar(text)

            if 'error' not in result:
                st.subheader("Grammar Analysis Results")

                if result.get('corrected_text'):
                    st.text_area("Improved text:", result['corrected_text'], height=200)
                    FileHandler.create_download_link(result['corrected_text'].encode(), "grammar_corrected.txt",
                                                     "text/plain")

                if result.get('suggestions'):
                    st.subheader("Grammar suggestions:")
                    for suggestion in result['suggestions']:
                        st.write(f"• {suggestion}")

                if not result.get('suggestions'):
                    st.success("✅ No grammar issues found!")
            else:
                st.error(result['error'])


def text_to_speech():
    """Convert text to speech information"""
    create_tool_header("Text-to-Speech", "Generate text-to-speech information", "🔊")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200,
                            placeholder="Hello! This text will be converted to speech.")

    if text:
        col1, col2 = st.columns(2)
        with col1:
            voice_type = st.selectbox("Voice type:", ["Male", "Female", "Neutral"])
        with col2:
            speech_rate = st.selectbox("Speech rate:", ["Slow", "Normal", "Fast"])

        language = st.selectbox("Language:", ["English", "Spanish", "French", "German", "Italian"])

        if st.button("Generate Speech Info"):
            # Since we can't actually generate audio, provide information
            st.info("🎵 **Text-to-Speech Information**")
            st.write(f"**Text length:** {len(text)} characters")
            st.write(f"**Word count:** {len(text.split())} words")
            st.write(f"**Estimated duration:** {len(text.split()) * 0.6:.1f} seconds")
            st.write(f"**Voice:** {voice_type}")
            st.write(f"**Rate:** {speech_rate}")
            st.write(f"**Language:** {language}")

            # Provide phonetic breakdown for first few words
            words = text.split()[:5]
            st.subheader("Phonetic preview (first 5 words):")
            for word in words:
                st.write(f"• **{word}** → [Sample phonetic representation]")


# Text Extraction Tools

def phone_extractor():
    """Extract phone numbers from text"""
    create_tool_header("Phone Extractor", "Extract phone numbers from text", "📱")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text containing phone numbers:", height=200,
                            placeholder="Call me at (555) 123-4567 or +1-800-555-0199. My other number is 555.987.6543")

    if text and st.button("Extract Phone Numbers"):
        phones = extract_phone_numbers(text)

        if phones:
            st.success(f"Found {len(phones)} phone number(s):")
            for phone in phones:
                st.write(f"• {phone}")

            # Create downloadable list
            phone_list = '\n'.join(phones)
            FileHandler.create_download_link(phone_list.encode(), "extracted_phones.txt", "text/plain")
        else:
            st.info("No phone numbers found.")


def extract_phone_numbers(text):
    """Extract phone numbers using regex patterns"""
    patterns = [
        r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # (555) 123-4567, 555-123-4567, 555.123.4567
        r'\+\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}',  # +1-800-555-0199
        r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',  # 555-123-4567
    ]

    phones = set()
    for pattern in patterns:
        matches = re.findall(pattern, text)
        phones.update(matches)

    return list(phones)


def regex_matcher():
    """Match text using regular expressions"""
    create_tool_header("Regex Matcher", "Find patterns using regular expressions", "🔍")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text:", height=200,
                            placeholder="Find patterns in this text. Email: user@example.com, Phone: 555-123-4567")

    pattern = st.text_input("Regular expression pattern:",
                            placeholder=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    col1, col2 = st.columns(2)
    with col1:
        ignore_case = st.checkbox("Ignore case", True)
    with col2:
        multiline = st.checkbox("Multiline mode", False)

    if text and pattern and st.button("Find Matches"):
        try:
            flags = 0
            if ignore_case:
                flags |= re.IGNORECASE
            if multiline:
                flags |= re.MULTILINE

            matches = re.findall(pattern, text, flags=flags)

            if matches:
                st.success(f"Found {len(matches)} match(es):")
                for i, match in enumerate(matches, 1):
                    st.write(f"{i}. `{match}`")

                # Create downloadable list
                match_list = '\n'.join(matches)
                FileHandler.create_download_link(match_list.encode(), "regex_matches.txt", "text/plain")
            else:
                st.info("No matches found.")

        except re.error as e:
            st.error(f"Invalid regular expression: {str(e)}")


# Text Editing Tools

def text_merger():
    """Merge multiple texts"""
    create_tool_header("Text Merger", "Merge multiple text inputs", "🔗")

    num_texts = st.slider("Number of texts to merge:", 2, 10, 3)

    texts = []
    for i in range(num_texts):
        text = st.text_area(f"Text {i + 1}:", height=100, key=f"merge_text_{i}",
                            placeholder=f"Enter text {i + 1} here...")
        texts.append(text)

    separator = st.text_input("Separator:", value="\n\n", placeholder="\\n\\n")
    separator = separator.replace('\\n', '\n').replace('\\t', '\t')

    if any(texts) and st.button("Merge Texts"):
        non_empty_texts = [text for text in texts if text.strip()]

        if len(non_empty_texts) < 2:
            st.warning("Please provide at least 2 texts to merge.")
        else:
            merged = separator.join(non_empty_texts)
            st.text_area("Merged result:", merged, height=300)
            FileHandler.create_download_link(merged.encode(), "merged_text.txt", "text/plain")
            st.success(f"Merged {len(non_empty_texts)} texts successfully!")


def text_splitter():
    """Split text by various criteria"""
    create_tool_header("Text Splitter", "Split text into parts", "✂️")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text to split:", height=200,
                            placeholder="Split this text by lines, words, or custom separators.")

    if text:
        split_method = st.selectbox("Split by:", [
            "Lines", "Sentences", "Words", "Paragraphs", "Custom separator", "Character count"
        ])

        if split_method == "Custom separator":
            separator = st.text_input("Custom separator:", placeholder=",")
        elif split_method == "Character count":
            char_count = st.slider("Characters per part:", 50, 1000, 200)

        if st.button("Split Text"):
            if split_method == "Lines":
                parts = text.split('\n')
            elif split_method == "Sentences":
                parts = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
            elif split_method == "Words":
                parts = text.split()
            elif split_method == "Paragraphs":
                parts = [p.strip() for p in text.split('\n\n') if p.strip()]
            elif split_method == "Custom separator":
                parts = text.split(separator) if separator else [text]
            elif split_method == "Character count":
                parts = [text[i:i + char_count] for i in range(0, len(text), char_count)]

            st.success(f"Split into {len(parts)} part(s):")

            for i, part in enumerate(parts, 1):
                with st.expander(f"Part {i} ({len(part)} chars)"):
                    st.write(part)

            # Create downloadable files
            split_text = f"\n--- Part {i} ---\n".join(f"{i}: {part}" for i, part in enumerate(parts, 1))
            FileHandler.create_download_link(split_text.encode(), "split_text.txt", "text/plain")


def duplicate_remover():
    """Remove duplicate lines from text"""
    create_tool_header("Duplicate Remover", "Remove duplicate lines from text", "🗑️")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text with duplicates:", height=200,
                            placeholder="apple\nbanana\napple\ncherry\nbanana\ndate")

    if text:
        col1, col2 = st.columns(2)
        with col1:
            case_sensitive = st.checkbox("Case sensitive", True)
        with col2:
            preserve_order = st.checkbox("Preserve original order", True)

        trim_whitespace = st.checkbox("Trim whitespace before comparison", True)

        if st.button("Remove Duplicates"):
            lines = text.split('\n')

            if trim_whitespace:
                comparison_lines = [line.strip() for line in lines]
            else:
                comparison_lines = lines

            if not case_sensitive:
                comparison_lines = [line.lower() for line in comparison_lines]

            if preserve_order:
                seen = set()
                unique_lines = []
                for i, comp_line in enumerate(comparison_lines):
                    if comp_line not in seen:
                        seen.add(comp_line)
                        unique_lines.append(lines[i])
            else:
                unique_comparison = list(set(comparison_lines))
                # Map back to original case
                unique_lines = []
                for comp_line in unique_comparison:
                    for i, original_comp in enumerate(comparison_lines):
                        if comp_line == original_comp:
                            unique_lines.append(lines[i])
                            break

            result = '\n'.join(unique_lines)

            st.success(f"Removed {len(lines) - len(unique_lines)} duplicate(s)")
            st.text_area("Result:", result, height=200)
            FileHandler.create_download_link(result.encode(), "duplicates_removed.txt", "text/plain")


# Text Styling Tools

def html_formatter():
    """Format HTML code"""
    create_tool_header("HTML Formatter", "Format and beautify HTML code", "🌐")

    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded HTML", html_code, height=100, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code:", height=200,
                                 placeholder="<html><head><title>Test</title></head><body><h1>Hello</h1><p>World</p></body></html>")

    if html_code:
        col1, col2 = st.columns(2)
        with col1:
            indent_size = st.slider("Indentation size:", 1, 8, 2)
        with col2:
            indent_type = st.selectbox("Indentation type:", ["Spaces", "Tabs"])

        if st.button("Format HTML"):
            try:
                formatted = format_html_simple(html_code, indent_size, indent_type)
                st.code(formatted, language='html')
                FileHandler.create_download_link(formatted.encode(), "formatted.html", "text/html")
                st.success("HTML formatted successfully!")
            except Exception as e:
                st.error(f"Error formatting HTML: {str(e)}")


def format_html_simple(html_code, indent_size=2, indent_type="Spaces"):
    """Simple HTML formatter"""
    indent_char = "\t" if indent_type == "Tabs" else " " * indent_size

    # Remove extra whitespace
    html_code = re.sub(r'>\s+<', '><', html_code.strip())

    # Add newlines after tags
    html_code = re.sub(r'(<[^>]+>)', r'\1\n', html_code)

    lines = html_code.split('\n')
    formatted_lines = []
    indent_level = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith('</'):
            indent_level = max(0, indent_level - 1)

        formatted_lines.append(indent_char * indent_level + line)

        if line.startswith('<') and not line.startswith('</') and not line.endswith('/>'):
            indent_level += 1

    return '\n'.join(formatted_lines)


def text_decorator():
    """Add decorative formatting to text"""
    create_tool_header("Text Decorator", "Add decorative formatting to text", "✨")

    text = st.text_area("Enter text to decorate:", height=100, placeholder="Hello World")

    if text:
        decoration_type = st.selectbox("Decoration type:", [
            "ASCII Art Borders",
            "Unicode Decorations",
            "Markdown Formatting",
            "Bullet Points",
            "Numbered Lists",
            "Code Blocks"
        ])

        if decoration_type == "ASCII Art Borders":
            border_style = st.selectbox("Border style:", ["Simple", "Double", "Fancy"])
        elif decoration_type == "Unicode Decorations":
            unicode_style = st.selectbox("Unicode style:", ["Stars", "Hearts", "Arrows", "Symbols"])
        elif decoration_type == "Markdown Formatting":
            md_style = st.selectbox("Markdown style:", ["Headers", "Bold/Italic", "Blockquotes"])

        if st.button("Decorate Text"):
            result = decorate_text(text, decoration_type, locals())
            st.text_area("Decorated text:", result, height=300)
            FileHandler.create_download_link(result.encode(), "decorated_text.txt", "text/plain")


def decorate_text(text, decoration_type, options):
    """Apply decorative formatting to text"""
    lines = text.split('\n')

    if decoration_type == "ASCII Art Borders":
        border_style = options.get('border_style', 'Simple')
        max_length = max(len(line) for line in lines)

        if border_style == "Simple":
            border = '+' + '-' * (max_length + 2) + '+'
            result = [border]
            for line in lines:
                result.append(f'| {line:<{max_length}} |')
            result.append(border)
        elif border_style == "Double":
            border = '╔' + '═' * (max_length + 2) + '╗'
            bottom = '╚' + '═' * (max_length + 2) + '╝'
            result = [border]
            for line in lines:
                result.append(f'║ {line:<{max_length}} ║')
            result.append(bottom)
        else:  # Fancy
            border = '┌' + '─' * (max_length + 2) + '┐'
            bottom = '└' + '─' * (max_length + 2) + '┘'
            result = [border]
            for line in lines:
                result.append(f'│ {line:<{max_length}} │')
            result.append(bottom)

        return '\n'.join(result)

    elif decoration_type == "Unicode Decorations":
        unicode_style = options.get('unicode_style', 'Stars')
        decorations = {
            'Stars': ('✨ ', ' ✨'),
            'Hearts': ('💖 ', ' 💖'),
            'Arrows': ('→ ', ' ←'),
            'Symbols': ('🔸 ', ' 🔸')
        }
        prefix, suffix = decorations[unicode_style]
        return '\n'.join(f'{prefix}{line}{suffix}' for line in lines)

    elif decoration_type == "Markdown Formatting":
        md_style = options.get('md_style', 'Headers')
        if md_style == "Headers":
            return '\n'.join(f'## {line}' for line in lines)
        elif md_style == "Bold/Italic":
            return '\n'.join(f'**{line}**' for line in lines)
        else:  # Blockquotes
            return '\n'.join(f'> {line}' for line in lines)

    elif decoration_type == "Bullet Points":
        return '\n'.join(f'• {line}' for line in lines)

    elif decoration_type == "Numbered Lists":
        return '\n'.join(f'{i}. {line}' for i, line in enumerate(lines, 1))

    elif decoration_type == "Code Blocks":
        return f'```\n{text}\n```'

    return text


def font_styler():
    """Apply font-like styling to text"""
    create_tool_header("Font Styler", "Apply different font styles to text", "🎨")

    text = st.text_input("Enter text:", placeholder="Hello World")

    if text:
        style_type = st.selectbox("Font style:", [
            "Mathematical Bold",
            "Mathematical Italic",
            "Monospace",
            "Subscript Numbers",
            "Superscript Numbers",
            "Enclosed Characters"
        ])

        if st.button("Apply Style"):
            styled_text = apply_font_style(text, style_type)
            st.markdown(f"### Styled text:")
            st.code(styled_text)
            st.markdown(f"**Preview:** {styled_text}")
            FileHandler.create_download_link(styled_text.encode(), "styled_text.txt", "text/plain")


def apply_font_style(text, style_type):
    """Apply Unicode font styling"""
    if style_type == "Mathematical Bold":
        # Unicode Mathematical Bold
        bold_map = {
            'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆',
            'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
            'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔',
            'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
            'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠',
            'h': '𝐡', 'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧',
            'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮',
            'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳'
        }
        return ''.join(bold_map.get(char, char) for char in text)

    elif style_type == "Monospace":
        # Unicode Monospace
        mono_map = {
            'A': '𝙰', 'B': '𝙱', 'C': '𝙲', 'D': '𝙳', 'E': '𝙴', 'F': '𝙵', 'G': '𝙶',
            'H': '𝙷', 'I': '𝙸', 'J': '𝙹', 'K': '𝙺', 'L': '𝙻', 'M': '𝙼', 'N': '𝙽',
            'O': '𝙾', 'P': '𝙿', 'Q': '𝚀', 'R': '𝚁', 'S': '𝚂', 'T': '𝚃', 'U': '𝚄',
            'V': '𝚅', 'W': '𝚆', 'X': '𝚇', 'Y': '𝚈', 'Z': '𝚉',
            'a': '𝚊', 'b': '𝚋', 'c': '𝚌', 'd': '𝚍', 'e': '𝚎', 'f': '𝚏', 'g': '𝚐',
            'h': '𝚑', 'i': '𝚒', 'j': '𝚓', 'k': '𝚔', 'l': '𝚕', 'm': '𝚖', 'n': '𝚗',
            'o': '𝚘', 'p': '𝚙', 'q': '𝚚', 'r': '𝚛', 's': '𝚜', 't': '𝚝', 'u': '𝚞',
            'v': '𝚟', 'w': '𝚠', 'x': '𝚡', 'y': '𝚢', 'z': '𝚣'
        }
        return ''.join(mono_map.get(char, char) for char in text)

    elif style_type == "Subscript Numbers":
        sub_map = {'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'}
        return ''.join(sub_map.get(char, char) for char in text)

    elif style_type == "Superscript Numbers":
        sup_map = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
        return ''.join(sup_map.get(char, char) for char in text)

    else:  # Enclosed Characters
        enclosed_map = {
            'A': 'Ⓐ', 'B': 'Ⓑ', 'C': 'Ⓒ', 'D': 'Ⓓ', 'E': 'Ⓔ', 'F': 'Ⓕ', 'G': 'Ⓖ',
            'H': 'Ⓗ', 'I': 'Ⓘ', 'J': 'Ⓙ', 'K': 'Ⓚ', 'L': 'Ⓛ', 'M': 'Ⓜ', 'N': 'Ⓝ',
            'O': 'Ⓞ', 'P': 'Ⓟ', 'Q': 'Ⓠ', 'R': 'Ⓡ', 'S': 'Ⓢ', 'T': 'Ⓣ', 'U': 'Ⓤ',
            'V': 'Ⓥ', 'W': 'Ⓦ', 'X': 'Ⓧ', 'Y': 'Ⓨ', 'Z': 'Ⓩ',
            'a': 'ⓐ', 'b': 'ⓑ', 'c': 'ⓒ', 'd': 'ⓓ', 'e': 'ⓔ', 'f': 'ⓕ', 'g': 'ⓖ',
            'h': 'ⓗ', 'i': 'ⓘ', 'j': 'ⓙ', 'k': 'ⓚ', 'l': 'ⓛ', 'm': 'ⓜ', 'n': 'ⓝ',
            'o': 'ⓞ', 'p': 'ⓟ', 'q': 'ⓠ', 'r': 'ⓡ', 's': 'ⓢ', 't': 'ⓣ', 'u': 'ⓤ',
            'v': 'ⓥ', 'w': 'ⓦ', 'x': 'ⓧ', 'y': 'ⓨ', 'z': 'ⓩ',
            '1': '①', '2': '②', '3': '③', '4': '④', '5': '⑤', '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨', '0': '⓪'
        }
        return ''.join(enclosed_map.get(char, char) for char in text)


# Miscellaneous Tools

def text_to_image():
    """Generate text as image information"""
    create_tool_header("Text to Image", "Convert text to image format information", "🖼️")

    text = st.text_area("Enter text:", height=100, placeholder="Hello World!")

    if text:
        col1, col2 = st.columns(2)
        with col1:
            font_size = st.slider("Font size:", 12, 72, 24)
            text_color = st.selectbox("Text color:", ["Black", "White", "Red", "Blue", "Green"])

        with col2:
            bg_color = st.selectbox("Background color:", ["White", "Black", "Transparent", "Blue", "Green"])
            image_format = st.selectbox("Format:", ["PNG", "JPEG", "SVG"])

        if st.button("Generate Image Info"):
            st.info("🖼️ **Text to Image Information**")
            st.write(f"**Text:** {text}")
            st.write(f"**Font size:** {font_size}px")
            st.write(f"**Text color:** {text_color}")
            st.write(f"**Background:** {bg_color}")
            st.write(f"**Format:** {image_format}")
            st.write(f"**Estimated dimensions:** {len(text) * font_size * 0.6:.0f}x{font_size + 10}px")

            # Show preview as text art
            st.markdown("### Text Preview:")
            st.markdown(
                f'<div style="font-size: {font_size}px; color: {text_color.lower()}; background: {"transparent" if bg_color == "Transparent" else bg_color.lower()}; padding: 10px; border: 1px solid #ccc;">{text}</div>',
                unsafe_allow_html=True)


def word_cloud():
    """Generate word cloud information"""
    create_tool_header("Word Cloud", "Generate word cloud visualization info", "☁️")

    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter text for word cloud:", height=200,
                            placeholder="Enter a long text to analyze word frequency and generate a word cloud visualization.")

    if text:
        col1, col2 = st.columns(2)
        with col1:
            max_words = st.slider("Max words:", 10, 200, 50)
            min_word_length = st.slider("Min word length:", 1, 10, 3)

        with col2:
            color_scheme = st.selectbox("Color scheme:", ["Viridis", "Plasma", "Blues", "Reds"])
            background = st.selectbox("Background:", ["White", "Black", "Transparent"])

        if st.button("Generate Word Cloud Info"):
            word_freq = analyze_word_frequency(text, min_word_length)
            top_words = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:max_words])

            st.subheader("📊 Word Frequency Analysis")

            col1, col2 = st.columns([2, 1])
            with col1:
                st.write("**Top Words:**")
                for word, count in list(top_words.items())[:20]:
                    # Simple visual representation
                    bar_width = int((count / max(top_words.values())) * 20)
                    bar = "█" * bar_width
                    st.write(f"{word}: {bar} ({count})")

            with col2:
                st.metric("Total unique words", len(word_freq))
                st.metric("Total words", sum(word_freq.values()))
                st.metric("Most frequent word", max(word_freq.items(), key=lambda x: x[1])[0])

            st.subheader("☁️ Word Cloud Settings")
            st.write(f"**Max words:** {max_words}")
            st.write(f"**Min word length:** {min_word_length}")
            st.write(f"**Color scheme:** {color_scheme}")
            st.write(f"**Background:** {background}")


def analyze_word_frequency(text, min_length=3):
    """Analyze word frequency in text"""
    # Clean and split text
    words = re.findall(r'\b\w+\b', text.lower())

    # Filter by length and common stop words
    stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'a', 'an', 'is', 'are',
                  'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
                  'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those'}

    filtered_words = [word for word in words if len(word) >= min_length and word not in stop_words]

    return Counter(filtered_words)


def article_generator():
    """AI-powered article generation tool"""
    create_tool_header("Article Generator", "Generate comprehensive articles using AI", "📝")

    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("Article topic:", placeholder="e.g., 'Benefits of renewable energy'")
        article_type = st.selectbox("Article type:", [
            "Informational", "How-to Guide", "List Article", "Opinion Piece",
            "Review", "News Article", "Tutorial", "Research Summary"
        ])

    with col2:
        word_count = st.selectbox("Target word count:", ["500-750", "750-1000", "1000-1500", "1500-2000", "2000+"])
        tone = st.selectbox("Tone:", ["Professional", "Casual", "Academic", "Conversational", "Persuasive"])

    target_audience = st.text_input("Target audience:",
                                    placeholder="e.g., 'Small business owners', 'Students', 'General public'")
    key_points = st.text_area("Key points to include (optional):",
                              placeholder="• Point 1\n• Point 2\n• Point 3", height=100)

    if topic and st.button("Generate Article"):
        with st.spinner("Generating article..."):
            prompt = f"""Write a {article_type.lower()} about '{topic}' with the following specifications:

- Target word count: {word_count} words
- Tone: {tone}
- Target audience: {target_audience if target_audience else 'General audience'}
- Article type: {article_type}

{f'Key points to include: {key_points}' if key_points else ''}

Please create a well-structured article with:
1. An engaging title
2. Clear introduction
3. Well-organized body sections with headers
4. Conclusion
5. Proper formatting with headers and bullet points where appropriate

Make the content informative, engaging, and tailored to the specified audience."""

            result = ai_client.generate_text(prompt)

            if result and not result.startswith("Error"):
                st.text_area("Generated Article:", result, height=500)

                # Word count
                word_count_actual = len(result.split())
                st.info(f"Generated article length: {word_count_actual} words")

                FileHandler.create_download_link(result.encode(), f"article_{topic.replace(' ', '_')}.txt",
                                                 "text/plain")
            else:
                st.error(f"Error generating article: {result}")


def copywriting_assistant():
    """AI-powered copywriting assistant"""
    create_tool_header("Copywriting Assistant", "Create compelling marketing copy using AI", "✍️")

    copy_type = st.selectbox("Copy type:", [
        "Email Subject Lines", "Product Descriptions", "Ad Headlines", "Social Media Posts",
        "Landing Page Copy", "Sales Letters", "Email Marketing", "Press Releases",
        "Blog Headlines", "Call-to-Action Buttons", "Video Scripts", "Newsletter Content"
    ])

    col1, col2 = st.columns(2)
    with col1:
        product_service = st.text_input("Product/Service:", placeholder="What are you promoting?")
        target_audience = st.text_input("Target audience:", placeholder="Who is your ideal customer?")

    with col2:
        tone = st.selectbox("Tone:", ["Persuasive", "Friendly", "Professional", "Urgent", "Casual", "Luxurious"])
        length = st.selectbox("Length:", ["Short (1-2 sentences)", "Medium (paragraph)", "Long (multiple paragraphs)"])

    unique_selling_points = st.text_area("Key benefits/features:",
                                         placeholder="• Benefit 1\n• Benefit 2\n• Benefit 3", height=100)

    additional_context = st.text_area("Additional context (optional):",
                                      placeholder="Any specific requirements, competitor info, or special offers",
                                      height=80)

    if product_service and st.button("Generate Copy"):
        with st.spinner("Creating compelling copy..."):
            prompt = f"""Create {copy_type.lower()} for '{product_service}' with these specifications:

- Target audience: {target_audience if target_audience else 'General consumers'}
- Tone: {tone}
- Length: {length}
- Copy type: {copy_type}

Key benefits/features:
{unique_selling_points if unique_selling_points else 'Focus on general benefits'}

{f'Additional context: {additional_context}' if additional_context else ''}

Requirements:
- Make it compelling and action-oriented
- Focus on benefits over features
- Include emotional triggers where appropriate
- Use power words and persuasive language
- Ensure it's tailored to the target audience
- Generate multiple variations (3-5 options) when appropriate"""

            result = ai_client.generate_text(prompt)

            if result and not result.startswith("Error"):
                st.text_area("Generated Copy:", result, height=400)
                FileHandler.create_download_link(result.encode(), f"copy_{copy_type.replace(' ', '_').lower()}.txt",
                                                 "text/plain")
            else:
                st.error(f"Error generating copy: {result}")


def technical_writer():
    """AI-powered technical writing assistant"""
    create_tool_header("Technical Writer", "Create clear technical documentation using AI", "📋")

    doc_type = st.selectbox("Document type:", [
        "API Documentation", "User Manual", "Installation Guide", "Troubleshooting Guide",
        "Technical Specifications", "Process Documentation", "Code Documentation",
        "System Architecture", "Tutorial", "FAQ", "Release Notes", "White Paper"
    ])

    col1, col2 = st.columns(2)
    with col1:
        subject = st.text_input("Subject/Topic:", placeholder="What system, process, or technology?")
        audience_level = st.selectbox("Audience expertise:", ["Beginner", "Intermediate", "Advanced", "Expert"])

    with col2:
        format_style = st.selectbox("Format style:", ["Step-by-step", "Reference", "Conceptual", "Mixed"])
        include_examples = st.checkbox("Include code examples/screenshots references", True)

    key_topics = st.text_area("Key topics to cover:",
                              placeholder="• Topic 1\n• Topic 2\n• Topic 3", height=100)

    technical_context = st.text_area("Technical context (optional):",
                                     placeholder="Programming languages, platforms, versions, etc.", height=80)

    if subject and st.button("Generate Documentation"):
        with st.spinner("Creating technical documentation..."):
            prompt = f"""Create {doc_type.lower()} for '{subject}' with these specifications:

- Document type: {doc_type}
- Target audience: {audience_level} level users
- Format style: {format_style}
- Include examples: {'Yes' if include_examples else 'No'}

Key topics to cover:
{key_topics if key_topics else 'Cover essential aspects of the subject'}

{f'Technical context: {technical_context}' if technical_context else ''}

Requirements:
- Use clear, concise language appropriate for {audience_level} users
- Include proper headings and structure
- Provide step-by-step instructions where applicable
- Include prerequisites and assumptions
- Add troubleshooting sections when relevant
- Use consistent terminology throughout
- Include relevant warnings or important notes
- Format with proper markdown structure"""

            result = ai_client.generate_text(prompt)

            if result and not result.startswith("Error"):
                st.text_area("Generated Documentation:", result, height=500)
                FileHandler.create_download_link(result.encode(), f"docs_{subject.replace(' ', '_')}.txt", "text/plain")
            else:
                st.error(f"Error generating documentation: {result}")


def content_moderator():
    """AI-powered content moderation tool"""
    create_tool_header("Content Moderator", "Analyze content for safety and compliance using AI", "🛡️")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)

    if uploaded_file:
        text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text, height=100, disabled=True)
    else:
        text = st.text_area("Enter content to moderate:", height=200,
                            placeholder="Enter text content that you want to analyze for safety, toxicity, or policy violations...")

    col1, col2 = st.columns(2)
    with col1:
        moderation_level = st.selectbox("Moderation strictness:", ["Strict", "Moderate", "Lenient"])
        check_categories = st.multiselect("Check for:", [
            "Hate Speech", "Harassment", "Violence", "Adult Content",
            "Spam", "Misinformation", "Copyright Issues", "Personal Information"
        ], default=["Hate Speech", "Harassment", "Violence"])

    with col2:
        content_type = st.selectbox("Content type:", [
            "Social Media Post", "Comment", "Article", "Review",
            "Email", "Chat Message", "Forum Post", "General Text"
        ])
        provide_suggestions = st.checkbox("Provide improvement suggestions", True)

    if text and st.button("Moderate Content"):
        with st.spinner("Analyzing content for safety and compliance..."):
            categories_text = ", ".join(check_categories) if check_categories else "general safety issues"

            prompt = f"""Analyze the following content for moderation purposes:

Content Type: {content_type}
Moderation Level: {moderation_level}
Check for: {categories_text}

Content to analyze:
"{text}"

Please provide:
1. Overall Safety Score (1-10, where 10 is completely safe)
2. Risk Level (Low/Medium/High)
3. Specific Issues Found (if any)
4. Detailed Analysis of each concern
5. Recommendations for content improvement
6. Policy Compliance Assessment

Be thorough but fair in your assessment. Consider context and intent."""

            result = ai_client.generate_text(prompt)

            if result and not result.startswith("Error"):
                st.subheader("🛡️ Content Moderation Results")

                # Display results in a structured format
                st.text_area("Moderation Analysis:", result, height=400)

                # Quick actions section
                st.subheader("Quick Actions")
                col1, col2, col3 = st.columns(3)

                with col1:
                    if st.button("✅ Approve Content"):
                        st.success("Content approved for publication")

                with col2:
                    if st.button("⚠️ Flag for Review"):
                        st.warning("Content flagged for manual review")

                with col3:
                    if st.button("❌ Reject Content"):
                        st.error("Content rejected due to policy violations")

                # Additional analysis
                if st.checkbox("Show detailed breakdown"):
                    detailed_prompt = f"""Provide a detailed category-by-category breakdown of the content analysis:

Content: "{text}"

For each category ({categories_text}), provide:
- Score (1-10)
- Specific examples if violations found
- Confidence level
- Recommended action"""

                    detailed_result = ai_client.generate_text(detailed_prompt)
                    st.text_area("Detailed Category Analysis:", detailed_result, height=300)

                FileHandler.create_download_link(result.encode(), "moderation_report.txt", "text/plain")
            else:
                st.error(f"Error analyzing content: {result}")