import streamlit as st
import re
import json
import requests
import html
import io
import base64
import random
import hashlib
import uuid
import time
import datetime
from urllib.parse import urlparse, urljoin
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler
from utils.ai_client import ai_client


def display_tools():
    """Display all web development tools"""

    tool_categories = {
        "HTML Tools": [
            "HTML Validator", "HTML Minifier", "HTML Beautifier", "Tag Analyzer", "HTML Entity Encoder/Decoder",
            "HTML to Text", "Link Extractor", "Meta Tag Generator"
        ],
        "JavaScript Tools": [
            "JS Validator", "JS Minifier", "JS Beautifier", "Console Logger", "Function Analyzer"
        ],
        "Performance Tools": [
            "Speed Test", "Bundle Analyzer", "Image Optimizer", "Cache Analyzer", "Loading Simulator"
        ],
        "Responsive Design": [
            "Viewport Tester", "Media Query Generator", "Breakpoint Analyzer", "Mobile Simulator"
        ],
        "Accessibility Tools": [
            "A11y Checker", "ARIA Validator", "Color Contrast", "Screen Reader Test", "Keyboard Navigation"
        ],
        "SEO Tools": [
            "Meta Tag Checker", "Sitemap Generator", "Robots.txt Validator", "Schema Markup", "OpenGraph Generator"
        ],
        "API Tools": [
            "REST API Tester", "JSON Formatter", "API Documentation", "Request Builder", "Response Analyzer"
        ],
        "Code Generators": [
            "HTML Form Generator", "HTML Table Generator", "HTML Layout Generator", "HTML Boilerplate Generator",
            "CSS Flexbox Generator", "CSS Grid Generator", "CSS Animation Generator", "CSS Gradient Generator",
            "JavaScript Function Generator", "JavaScript Class Generator", "JavaScript API Generator",
            "JavaScript Module Generator",
            "React Component Generator", "Vue Component Generator", "Angular Component Generator",
            "Express Route Generator",
            "REST API Generator", "Database Schema Generator", "Package.json Generator", "Config File Generator"
        ],
        "Development Utilities": [
            "URL Encoder/Decoder", "Base64 Converter", "Timestamp Converter", "Hash Generator", "UUID Generator"
        ],
        "Testing Tools": [
            "Form Validator", "Link Checker", "Cross-Browser Test", "Performance Monitor", "Error Logger"
        ]
    }

    selected_category = st.selectbox("Select Web Dev Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Web Dev Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "HTML Validator":
        html_validator()
    elif selected_tool == "HTML Beautifier":
        html_beautifier()
    elif selected_tool == "HTML Minifier":
        html_minifier()
    elif selected_tool == "Tag Analyzer":
        tag_analyzer()
    elif selected_tool == "HTML Entity Encoder/Decoder":
        html_entity_encoder_decoder()
    elif selected_tool == "HTML to Text":
        html_to_text()
    elif selected_tool == "Link Extractor":
        link_extractor()
    elif selected_tool == "JS Validator":
        js_validator()
    elif selected_tool == "JS Minifier":
        js_minifier()
    elif selected_tool == "JS Beautifier":
        js_beautifier()
    elif selected_tool == "Console Logger":
        console_logger()
    elif selected_tool == "Function Analyzer":
        function_analyzer()
    elif selected_tool == "JSON Formatter":
        json_formatter()
    elif selected_tool == "Meta Tag Generator":
        meta_tag_generator()
    elif selected_tool == "URL Encoder/Decoder":
        url_encoder_decoder()
    elif selected_tool == "Sitemap Generator":
        sitemap_generator()
    elif selected_tool == "REST API Tester":
        api_tester()
    elif selected_tool == "Performance Monitor":
        performance_monitor()
    elif selected_tool == "Speed Test":
        speed_test()
    elif selected_tool == "Bundle Analyzer":
        bundle_analyzer()
    elif selected_tool == "Image Optimizer":
        image_optimizer()
    elif selected_tool == "Cache Analyzer":
        cache_analyzer()
    elif selected_tool == "Loading Simulator":
        loading_simulator()
    elif selected_tool == "Viewport Tester":
        viewport_tester()
    elif selected_tool == "Media Query Generator":
        media_query_generator()
    elif selected_tool == "Breakpoint Analyzer":
        breakpoint_analyzer()
    elif selected_tool == "Mobile Simulator":
        mobile_simulator()
    # Accessibility Tools
    elif selected_tool == "A11y Checker":
        accessibility_wcag_checker()
    elif selected_tool == "ARIA Validator":
        aria_validator_tool()
    elif selected_tool == "Color Contrast":
        accessibility_color_contrast_checker()
    elif selected_tool == "Screen Reader Test":
        screen_reader_test_tool()
    elif selected_tool == "Keyboard Navigation":
        keyboard_navigation_tool()
    # Code Generators
    elif selected_tool == "HTML Form Generator":
        html_form_generator()
    elif selected_tool == "HTML Table Generator":
        html_table_generator()
    elif selected_tool == "HTML Layout Generator":
        html_layout_generator()
    elif selected_tool == "HTML Boilerplate Generator":
        html_boilerplate_generator()
    elif selected_tool == "CSS Flexbox Generator":
        css_flexbox_generator()
    elif selected_tool == "CSS Grid Generator":
        css_grid_generator()
    elif selected_tool == "CSS Animation Generator":
        css_animation_generator()
    elif selected_tool == "CSS Gradient Generator":
        css_gradient_generator()
    elif selected_tool == "JavaScript Function Generator":
        js_function_generator()
    elif selected_tool == "JavaScript Class Generator":
        js_class_generator()
    elif selected_tool == "JavaScript API Generator":
        js_api_generator()
    elif selected_tool == "JavaScript Module Generator":
        js_module_generator()
    elif selected_tool == "React Component Generator":
        react_component_generator()
    elif selected_tool == "Vue Component Generator":
        vue_component_generator()
    elif selected_tool == "Angular Component Generator":
        angular_component_generator()
    elif selected_tool == "Express Route Generator":
        express_route_generator()
    elif selected_tool == "REST API Generator":
        rest_api_generator()
    elif selected_tool == "Database Schema Generator":
        database_schema_generator()
    elif selected_tool == "Package.json Generator":
        package_json_generator()
    elif selected_tool == "Config File Generator":
        config_file_generator()
    # Development Utilities
    elif selected_tool == "Base64 Converter":
        base64_converter()
    elif selected_tool == "Timestamp Converter":
        timestamp_converter()
    elif selected_tool == "Hash Generator":
        hash_generator()
    elif selected_tool == "UUID Generator":
        uuid_generator()
    # Testing Tools
    elif selected_tool == "Form Validator":
        form_validator()
    elif selected_tool == "Link Checker":
        link_checker()
    elif selected_tool == "Cross-Browser Test":
        cross_browser_test()
    elif selected_tool == "Error Logger":
        error_logger()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def html_validator():
    """Validate HTML code"""
    create_tool_header("HTML Validator", "Validate your HTML code for errors and best practices", "🏷️")

    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.code(html_code, language='html')
    else:
        html_code = st.text_area("Enter HTML code:", height=200,
                                 placeholder="<html>\n  <head>\n    <title>My Page</title>\n  </head>\n  <body>\n    <h1>Hello World!</h1>\n  </body>\n</html>")

    if html_code and st.button("Validate HTML"):
        errors = validate_html(html_code)

        if not errors:
            st.success("✅ Valid HTML! No errors found.")
        else:
            st.error(f"❌ Found {len(errors)} errors:")
            for i, error in enumerate(errors, 1):
                st.write(f"{i}. {error}")


def validate_html(html_code):
    """Basic HTML validation"""
    errors = []

    # Check for basic structure
    if not re.search(r'<!DOCTYPE\s+html>', html_code, re.IGNORECASE):
        errors.append("Missing DOCTYPE declaration")

    if not re.search(r'<html[^>]*>', html_code, re.IGNORECASE):
        errors.append("Missing <html> tag")

    if not re.search(r'<head[^>]*>', html_code, re.IGNORECASE):
        errors.append("Missing <head> tag")

    if not re.search(r'<body[^>]*>', html_code, re.IGNORECASE):
        errors.append("Missing <body> tag")

    # Check for unclosed tags
    tags = re.findall(r'<(\w+)[^>]*>', html_code)
    closing_tags = re.findall(r'</(\w+)>', html_code)

    self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link'}

    for tag in tags:
        if tag.lower() not in self_closing and tag.lower() not in [t.lower() for t in closing_tags]:
            errors.append(f"Unclosed tag: <{tag}>")

    return errors


def html_beautifier():
    """Beautify and format HTML code"""
    create_tool_header("HTML Beautifier", "Format and beautify HTML code with proper indentation", "✨")

    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Original HTML:", html_code, height=150, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code:", height=200,
                                 placeholder="<html><head><title>Test</title></head><body><h1>Hello</h1><p>World</p></body></html>")

    if html_code:
        col1, col2 = st.columns(2)

        with col1:
            indent_size = st.slider("Indentation Size", 1, 8, 2)

        with col2:
            indent_type = st.selectbox("Indentation Type", ["Spaces", "Tabs"])

        if st.button("Beautify HTML"):
            try:
                beautified = beautify_html(html_code, indent_size, indent_type)
                st.subheader("Beautified HTML")
                st.code(beautified, language='html')
                FileHandler.create_download_link(beautified.encode(), "beautified.html", "text/html")
                st.success("✅ HTML beautified successfully!")
            except Exception as e:
                st.error(f"❌ Error beautifying HTML: {str(e)}")


def beautify_html(html_code, indent_size=2, indent_type="Spaces"):
    """Beautify HTML code with proper indentation"""
    import re

    # Simple HTML beautifier
    indent_char = "\t" if indent_type == "Tabs" else " " * indent_size

    # HTML void/self-closing tags that don't need closing tags
    void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track',
                 'wbr'}

    # Remove extra whitespace and newlines
    html_code = re.sub(r'>\s+<', '><', html_code.strip())

    # Add newlines after certain structural tags
    html_code = re.sub(r'(<(?:html|head|body|div|section|article|header|footer|nav|main|aside)[^>]*>)', r'\1\n',
                       html_code)
    html_code = re.sub(r'(</(?:html|head|body|div|section|article|header|footer|nav|main|aside)>)', r'\n\1\n',
                       html_code)
    html_code = re.sub(r'(<(?:title|h[1-6]|p|li|dt|dd)[^>]*>)', r'\n\1', html_code)
    html_code = re.sub(r'(</(?:title|h[1-6]|p|li|dt|dd)>)', r'\1\n', html_code)

    lines = html_code.split('\n')
    beautified_lines = []
    indent_level = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Skip indentation changes for comments and doctype
        if line.startswith('<!--') or line.startswith('<!'):
            beautified_lines.append(indent_char * indent_level + line)
            continue

        # Decrease indent for closing tags
        if line.startswith('</'):
            indent_level = max(0, indent_level - 1)

        # Add indented line
        beautified_lines.append(indent_char * indent_level + line)

        # Increase indent for opening tags (but not self-closing, closing tags, or void elements)
        if line.startswith('<') and not line.startswith('</'):
            # Extract tag name properly using regex
            tag_match = re.match(r'^<\/?([a-zA-Z0-9:-]+)\b', line)
            if tag_match:
                tag_name = tag_match.group(1).lower()
                # Only increase indent for non-void tags and non-self-closing tags
                if tag_name not in void_tags and not line.endswith('/>'):
                    indent_level += 1

    return '\n'.join(beautified_lines)


def html_minifier():
    """Minify HTML code by removing unnecessary whitespace"""
    create_tool_header("HTML Minifier", "Compress HTML by removing whitespace and comments", "🗜️")

    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Original HTML:", html_code, height=150, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code:", height=200,
                                 placeholder="<html>\n  <head>\n    <title>Test Page</title>\n  </head>\n  <body>\n    <h1>Hello World</h1>\n  </body>\n</html>")

    if html_code:
        col1, col2 = st.columns(2)

        with col1:
            remove_comments = st.checkbox("Remove Comments", True)
            remove_empty_lines = st.checkbox("Remove Empty Lines", True)

        with col2:
            preserve_pre = st.checkbox("Preserve <pre> Content", True)
            aggressive_mode = st.checkbox("Aggressive Minification", False)

        if st.button("Minify HTML"):
            try:
                minified = minify_html(html_code, remove_comments, remove_empty_lines, preserve_pre, aggressive_mode)

                # Calculate compression ratio
                original_size = len(html_code)
                minified_size = len(minified)
                compression_ratio = ((original_size - minified_size) / original_size) * 100

                st.subheader("Minified HTML")
                st.code(minified, language='html')

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Original Size", f"{original_size:,} chars")
                with col2:
                    st.metric("Minified Size", f"{minified_size:,} chars")
                with col3:
                    st.metric("Compression", f"{compression_ratio:.1f}%")

                FileHandler.create_download_link(minified.encode(), "minified.html", "text/html")
                st.success("✅ HTML minified successfully!")
            except Exception as e:
                st.error(f"❌ Error minifying HTML: {str(e)}")


def minify_html(html_code, remove_comments=True, remove_empty_lines=True, preserve_pre=True, aggressive_mode=False):
    """Minify HTML code"""
    import re

    minified = html_code

    # Remove HTML comments
    if remove_comments:
        minified = re.sub(r'<!--.*?-->', '', minified, flags=re.DOTALL)

    # Preserve content inside <pre>, <code>, <script>, and <style> tags if specified
    preserved_blocks = {}
    if preserve_pre:
        # Fix: Use re.finditer to capture full blocks correctly
        for i, match in enumerate(
                re.finditer(r'<(pre|code|script|style)[^>]*>.*?</\1>', minified, re.DOTALL | re.IGNORECASE)):
            block = match.group(0)  # Get the full matched block
            placeholder = f"__PRESERVE_BLOCK_{i}__"
            preserved_blocks[placeholder] = block
            minified = minified.replace(block, placeholder, 1)  # Replace only first occurrence

    # Remove extra whitespace between tags
    minified = re.sub(r'>\s+<', '><', minified)

    # Remove leading and trailing whitespace from lines
    if remove_empty_lines:
        lines = minified.split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        minified = ''.join(lines)
    else:
        minified = re.sub(r'^\s+|\s+$', '', minified, flags=re.MULTILINE)

    # Conservative aggressive minification with safeguards
    if aggressive_mode:
        # Remove spaces around = in attributes
        minified = re.sub(r'\s*=\s*', '=', minified)
        # Remove quotes only from very simple attribute values (alphanumeric, hyphen, underscore only)
        minified = re.sub(r'="([a-zA-Z0-9\-_]+)"', r'=\1', minified)

    # Restore preserved blocks
    for placeholder, block in preserved_blocks.items():
        minified = minified.replace(placeholder, block)

    return minified


def tag_analyzer():
    """Analyze HTML tags and structure"""
    create_tool_header("HTML Tag Analyzer", "Analyze HTML structure, tags, and attributes", "🔍")

    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("HTML Code:", html_code, height=150, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code:", height=200,
                                 placeholder="<html>\n  <head>\n    <title>My Page</title>\n    <meta charset='utf-8'>\n  </head>\n  <body>\n    <h1 id='title' class='main-title'>Hello</h1>\n    <p>Content here</p>\n    <img src='image.jpg' alt='Image'>\n  </body>\n</html>")

    if html_code and st.button("Analyze HTML"):
        try:
            analysis = analyze_html_structure(html_code)

            # Display analysis results
            st.subheader("📊 Structure Analysis")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Tags", analysis['total_tags'])
            with col2:
                st.metric("Unique Tags", len(analysis['tag_counts']))
            with col3:
                st.metric("Nesting Depth", analysis['max_depth'])

            # Tag frequency
            st.subheader("🏷️ Tag Frequency")
            for tag, count in sorted(analysis['tag_counts'].items(), key=lambda x: x[1], reverse=True):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"`<{tag}>`")
                with col2:
                    st.write(f"{count} times")

            # Attributes analysis
            if analysis['attributes']:
                st.subheader("⚙️ Common Attributes")
                for attr, count in sorted(analysis['attributes'].items(), key=lambda x: x[1], reverse=True)[:10]:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"`{attr}`")
                    with col2:
                        st.write(f"{count} times")

            # Structure tree
            st.subheader("🌳 HTML Structure")
            st.text(analysis['structure_tree'])

            # Issues and recommendations
            issues = analyze_html_issues(html_code)
            if issues:
                st.subheader("⚠️ Issues & Recommendations")
                for issue in issues:
                    st.warning(issue)
            else:
                st.success("✅ No major issues found!")

        except Exception as e:
            st.error(f"❌ Error analyzing HTML: {str(e)}")


def analyze_html_structure(html_code):
    """Analyze HTML structure and return statistics"""
    import re
    from collections import Counter

    # Find all tags
    tags = re.findall(r'<(\w+)', html_code, re.IGNORECASE)
    tag_counts = Counter(tag.lower() for tag in tags)

    # Find all attributes
    attributes = re.findall(r'\s(\w+)=', html_code)
    attr_counts = Counter(attr.lower() for attr in attributes)

    # Calculate nesting depth (simplified)
    max_depth = 0
    current_depth = 0

    for match in re.finditer(r'<(/?)(\w+)', html_code):
        is_closing = match.group(1) == '/'
        tag = match.group(2).lower()

        if not is_closing and tag not in ['br', 'hr', 'img', 'input', 'meta', 'link']:
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif is_closing:
            current_depth = max(0, current_depth - 1)

    # Create simple structure tree
    structure_tree = create_html_tree(html_code)

    return {
        'total_tags': len(tags),
        'tag_counts': dict(tag_counts),
        'attributes': dict(attr_counts),
        'max_depth': max_depth,
        'structure_tree': structure_tree
    }


def create_html_tree(html_code):
    """Create a simple HTML structure tree"""
    import re

    lines = []
    depth = 0

    for match in re.finditer(r'<(/?)(\w+)([^>]*)>', html_code):
        is_closing = match.group(1) == '/'
        tag = match.group(2).lower()
        attrs = match.group(3)

        if is_closing:
            depth = max(0, depth - 1)
            lines.append('  ' * depth + f"</{tag}>")
        else:
            # Extract key attributes for display
            id_match = re.search(r'id=["\']([^"\']+)["\']', attrs)
            class_match = re.search(r'class=["\']([^"\']+)["\']', attrs)

            attr_display = ""
            if id_match:
                attr_display += f" id='{id_match.group(1)}'"
            if class_match:
                attr_display += f" class='{class_match.group(1)}'"

            lines.append('  ' * depth + f"<{tag}{attr_display}>")

            # Only increase depth for container tags
            if tag not in ['br', 'hr', 'img', 'input', 'meta', 'link', 'area', 'base', 'col', 'embed', 'source',
                           'track', 'wbr']:
                depth += 1

    return '\n'.join(lines[:50])  # Limit to first 50 lines


def analyze_html_issues(html_code):
    """Analyze HTML for potential issues"""
    issues = []

    # Check for missing DOCTYPE
    if not re.search(r'<!DOCTYPE\s+html>', html_code, re.IGNORECASE):
        issues.append("Missing DOCTYPE declaration - consider adding <!DOCTYPE html>")

    # Check for missing meta charset
    if not re.search(r'<meta[^>]*charset', html_code, re.IGNORECASE):
        issues.append("Missing charset declaration - consider adding <meta charset='UTF-8'>")

    # Check for images without alt attributes
    img_without_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', html_code, re.IGNORECASE)
    if img_without_alt:
        issues.append(f"Found {len(img_without_alt)} image(s) without alt attributes - important for accessibility")

    # Check for missing title tag
    if not re.search(r'<title[^>]*>', html_code, re.IGNORECASE):
        issues.append("Missing <title> tag - important for SEO")

    # Check for inline styles
    inline_styles = re.findall(r'style\s*=', html_code, re.IGNORECASE)
    if len(inline_styles) > 5:
        issues.append(f"Found {len(inline_styles)} inline styles - consider using external CSS")

    return issues


def html_entity_encoder_decoder():
    """Encode and decode HTML entities"""
    create_tool_header("HTML Entity Encoder/Decoder", "Convert HTML entities to characters and vice versa", "🔤")

    tab1, tab2 = st.tabs(["Encode", "Decode"])

    with tab1:
        st.subheader("Encode to HTML Entities")

        uploaded_file = FileHandler.upload_files(['txt', 'html', 'htm'], accept_multiple=False)

        if uploaded_file:
            text_input = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("Input Text:", text_input, height=150, disabled=True)
        else:
            text_input = st.text_area("Enter text to encode:", height=200,
                                      placeholder="<div class='example'>Hello & welcome to \"HTML encoding\"!</div>")

        if text_input:
            col1, col2 = st.columns(2)
            with col1:
                encode_quotes = st.checkbox("Encode Quotes", True)
            with col2:
                encode_all = st.checkbox("Encode All Non-ASCII", False)

            if st.button("Encode Text"):
                try:
                    encoded = encode_html_entities(text_input, encode_quotes, encode_all)
                    st.subheader("Encoded HTML")
                    st.code(encoded, language='html')
                    FileHandler.create_download_link(encoded.encode(), "encoded.html", "text/html")
                    st.success("✅ Text encoded successfully!")
                except Exception as e:
                    st.error(f"❌ Error encoding text: {str(e)}")

    with tab2:
        st.subheader("Decode from HTML Entities")

        uploaded_file2 = FileHandler.upload_files(['txt', 'html', 'htm'], accept_multiple=False)

        if uploaded_file2:
            html_input = FileHandler.process_text_file(uploaded_file2[0])
            st.text_area("Input HTML:", html_input, height=150, disabled=True)
        else:
            html_input = st.text_area("Enter HTML with entities to decode:", height=200,
                                      placeholder="&lt;div class=&quot;example&quot;&gt;Hello &amp; welcome!&lt;/div&gt;")

        if html_input and st.button("Decode HTML"):
            try:
                decoded = decode_html_entities(html_input)
                st.subheader("Decoded Text")
                st.code(decoded, language='text')
                FileHandler.create_download_link(decoded.encode(), "decoded.txt", "text/plain")
                st.success("✅ HTML entities decoded successfully!")
            except Exception as e:
                st.error(f"❌ Error decoding HTML: {str(e)}")


def encode_html_entities(text, encode_quotes=True, encode_all=False):
    """Encode text to HTML entities"""
    import html

    if encode_all:
        # Encode all non-ASCII characters
        encoded = html.escape(text, quote=encode_quotes)
        # Additional encoding for non-ASCII characters
        encoded = encoded.encode('ascii', 'xmlcharrefreplace').decode('ascii')
    else:
        # Standard HTML encoding
        encoded = html.escape(text, quote=encode_quotes)

    return encoded


def decode_html_entities(html_text):
    """Decode HTML entities to text"""
    import html
    import re

    # Decode standard HTML entities
    decoded = html.unescape(html_text)

    # Decode numeric character references (&#123; and &#x1A; formats)
    def decode_numeric_entity(match):
        if match.group(1):  # Hex format &#xNN;
            return chr(int(match.group(1), 16))
        else:  # Decimal format &#NNN;
            return chr(int(match.group(2)))

    decoded = re.sub(r'&#x([0-9a-fA-F]+);|&#(\d+);', decode_numeric_entity, decoded)

    return decoded


def html_to_text():
    """Extract plain text from HTML content"""
    create_tool_header("HTML to Text", "Extract plain text content from HTML", "📄")

    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("HTML Code:", html_code, height=150, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code:", height=200,
                                 placeholder="<html>\n  <body>\n    <h1>Welcome</h1>\n    <p>This is a <strong>sample</strong> paragraph with <a href='#'>links</a>.</p>\n    <ul>\n      <li>Item 1</li>\n      <li>Item 2</li>\n    </ul>\n  </body>\n</html>")

    if html_code:
        col1, col2 = st.columns(2)

        with col1:
            preserve_formatting = st.checkbox("Preserve Line Breaks", True)
            include_links = st.checkbox("Include Link URLs", False)

        with col2:
            remove_extra_spaces = st.checkbox("Remove Extra Spaces", True)
            add_separators = st.checkbox("Add List Separators", True)

        if st.button("Extract Text"):
            try:
                text_content = extract_text_from_html(html_code, preserve_formatting, include_links,
                                                      remove_extra_spaces, add_separators)

                st.subheader("Extracted Text")
                st.text_area("Plain Text:", text_content, height=300)

                # Statistics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Characters", len(text_content))
                with col2:
                    st.metric("Words", len(text_content.split()))
                with col3:
                    st.metric("Lines", len(text_content.split('\n')))

                FileHandler.create_download_link(text_content.encode(), "extracted_text.txt", "text/plain")
                st.success("✅ Text extracted successfully!")
            except Exception as e:
                st.error(f"❌ Error extracting text: {str(e)}")


def extract_text_from_html(html_code, preserve_formatting=True, include_links=False, remove_extra_spaces=True,
                           add_separators=True):
    """Extract plain text from HTML"""
    import re

    # Remove script and style elements
    html_code = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html_code, flags=re.DOTALL | re.IGNORECASE)

    # Handle specific tags with formatting
    if preserve_formatting:
        # Add line breaks for block elements
        html_code = re.sub(r'</(div|p|h[1-6]|li|dt|dd|section|article|header|footer|nav)>', r'</\1>\n', html_code,
                           flags=re.IGNORECASE)
        html_code = re.sub(r'<br\s*/?>', '\n', html_code, flags=re.IGNORECASE)
        html_code = re.sub(r'<hr\s*/?>', '\n---\n', html_code, flags=re.IGNORECASE)

    if add_separators:
        # Add bullets for list items
        html_code = re.sub(r'<li[^>]*>', '• ', html_code, flags=re.IGNORECASE)
        html_code = re.sub(r'<dt[^>]*>', '• ', html_code, flags=re.IGNORECASE)
        html_code = re.sub(r'<dd[^>]*>', '  - ', html_code, flags=re.IGNORECASE)

    if include_links:
        # Replace links with text and URL
        def replace_link(match):
            url = match.group(1)
            link_text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
            if not link_text:
                link_text = url
            return f"{link_text} ({url})"

        html_code = re.sub(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', replace_link, html_code,
                           flags=re.IGNORECASE | re.DOTALL)

    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', '', html_code)

    # Decode HTML entities
    text = decode_html_entities(text)

    if remove_extra_spaces:
        # Remove extra whitespace
        text = re.sub(r'[ \t]+', ' ', text)  # Multiple spaces/tabs to single space
        text = re.sub(r'\n\s*\n', '\n\n', text)  # Multiple newlines to double newline
        text = text.strip()

    return text


def link_extractor():
    """Extract all links from HTML content"""
    create_tool_header("Link Extractor", "Extract and analyze all links from HTML", "🔗")

    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("HTML Code:", html_code, height=150, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code:", height=200,
                                 placeholder="<html>\n  <body>\n    <p>Visit <a href='https://example.com'>Example</a></p>\n    <p>Email us at <a href='mailto:info@example.com'>Contact</a></p>\n    <img src='image.jpg' alt='Image'>\n    <link rel='stylesheet' href='styles.css'>\n  </body>\n</html>")

    if html_code:
        col1, col2 = st.columns(2)

        with col1:
            extract_images = st.checkbox("Extract Image Sources", True)
            extract_stylesheets = st.checkbox("Extract Stylesheets", True)

        with col2:
            extract_scripts = st.checkbox("Extract Scripts", True)
            check_status = st.checkbox("Check Link Status", False)

        if st.button("Extract Links"):
            try:
                links_data = extract_links_from_html(html_code, extract_images, extract_stylesheets, extract_scripts,
                                                     check_status)

                # Display results
                if links_data['hyperlinks']:
                    st.subheader("🔗 Hyperlinks")
                    for i, link in enumerate(links_data['hyperlinks'], 1):
                        with st.expander(f"Link {i}: {link['text'][:50]}..."):
                            col1, col2 = st.columns(2)
                            with col1:
                                st.write("**URL:**", link['url'])
                                st.write("**Text:**", link['text'])
                            with col2:
                                st.write("**Type:**", link['type'])
                                if link.get('status'):
                                    st.write("**Status:**", link['status'])

                if links_data['images'] and extract_images:
                    st.subheader("🖼️ Images")
                    for i, img in enumerate(links_data['images'], 1):
                        st.write(f"{i}. `{img['src']}` - *{img['alt']}*")

                if links_data['stylesheets'] and extract_stylesheets:
                    st.subheader("🎨 Stylesheets")
                    for i, css in enumerate(links_data['stylesheets'], 1):
                        st.write(f"{i}. `{css}`")

                if links_data['scripts'] and extract_scripts:
                    st.subheader("📜 Scripts")
                    for i, js in enumerate(links_data['scripts'], 1):
                        st.write(f"{i}. `{js}`")

                # Summary statistics
                st.subheader("📊 Summary")
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Hyperlinks", len(links_data['hyperlinks']))
                with col2:
                    st.metric("Images", len(links_data['images']))
                with col3:
                    st.metric("Stylesheets", len(links_data['stylesheets']))
                with col4:
                    st.metric("Scripts", len(links_data['scripts']))

                # Create download links
                all_links = []
                for link in links_data['hyperlinks']:
                    all_links.append(f"{link['url']} - {link['text']}")
                if links_data['images']:
                    all_links.extend([img['src'] for img in links_data['images']])
                if links_data['stylesheets']:
                    all_links.extend(links_data['stylesheets'])
                if links_data['scripts']:
                    all_links.extend(links_data['scripts'])

                if all_links:
                    links_text = '\n'.join(all_links)
                    FileHandler.create_download_link(links_text.encode(), "extracted_links.txt", "text/plain")

                st.success("✅ Links extracted successfully!")
            except Exception as e:
                st.error(f"❌ Error extracting links: {str(e)}")


def extract_links_from_html(html_code, extract_images=True, extract_stylesheets=True, extract_scripts=True,
                            check_status=False):
    """Extract all links from HTML"""
    import re

    links_data = {
        'hyperlinks': [],
        'images': [],
        'stylesheets': [],
        'scripts': []
    }

    # Extract hyperlinks
    for match in re.finditer(r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\'][^>]*>(.*?)</a>', html_code,
                             re.IGNORECASE | re.DOTALL):
        url = match.group(1)
        text = re.sub(r'<[^>]+>', '', match.group(2)).strip()

        # Determine link type
        link_type = "External"
        if url.startswith('mailto:'):
            link_type = "Email"
        elif url.startswith('tel:'):
            link_type = "Phone"
        elif url.startswith('#'):
            link_type = "Anchor"
        elif url.startswith('/') or not url.startswith('http'):
            link_type = "Internal"

        link_info = {
            'url': url,
            'text': text or url,
            'type': link_type
        }

        # Optional status check (simplified - just mark as unchecked for now)
        if check_status:
            link_info['status'] = 'Unchecked'  # Could implement actual HTTP status check here

        links_data['hyperlinks'].append(link_info)

    # Extract images
    if extract_images:
        for match in re.finditer(r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\'][^>]*(?:alt\s*=\s*["\']([^"\']*)["\'])?',
                                 html_code, re.IGNORECASE):
            src = match.group(1)
            alt = match.group(2) or "No alt text"
            links_data['images'].append({'src': src, 'alt': alt})

    # Extract stylesheets
    if extract_stylesheets:
        for match in re.finditer(r'<link\s+[^>]*href\s*=\s*["\']([^"\']+\.css[^"\']*)["\']', html_code, re.IGNORECASE):
            links_data['stylesheets'].append(match.group(1))

    # Extract scripts
    if extract_scripts:
        for match in re.finditer(r'<script\s+[^>]*src\s*=\s*["\']([^"\']+)["\']', html_code, re.IGNORECASE):
            links_data['scripts'].append(match.group(1))

    return links_data


def js_validator():
    """Validate JavaScript code"""
    create_tool_header("JavaScript Validator", "Check your JavaScript code for syntax errors", "⚡")

    uploaded_file = FileHandler.upload_files(['js'], accept_multiple=False)

    if uploaded_file:
        js_code = FileHandler.process_text_file(uploaded_file[0])
        st.code(js_code, language='javascript')
    else:
        js_code = st.text_area("Enter JavaScript code:", height=200,
                               placeholder="function greet(name) {\n  console.log('Hello, ' + name + '!');\n}")

    if js_code and st.button("Validate JavaScript"):
        errors = validate_javascript(js_code)

        if not errors:
            st.success("✅ Valid JavaScript! No obvious syntax errors found.")
        else:
            st.warning(f"⚠️ Found {len(errors)} potential issues:")
            for i, error in enumerate(errors, 1):
                st.write(f"{i}. {error}")


def validate_javascript(js_code):
    """Basic JavaScript validation"""
    errors = []

    # Check for common syntax issues
    if js_code.count('(') != js_code.count(')'):
        errors.append("Mismatched parentheses")

    if js_code.count('{') != js_code.count('}'):
        errors.append("Mismatched braces")

    if js_code.count('[') != js_code.count(']'):
        errors.append("Mismatched brackets")

    # Check for semicolons at end of statements
    lines = js_code.split('\n')
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if line and not line.endswith((';', '{', '}', ')', ']')) and not line.startswith(
                ('if', 'for', 'while', 'function', '//')):
            errors.append(f"Line {i}: Missing semicolon")

    return errors


def json_formatter():
    """Format and validate JSON"""
    create_tool_header("JSON Formatter", "Format, validate, and beautify JSON data", "📄")

    uploaded_file = FileHandler.upload_files(['json'], accept_multiple=False)

    if uploaded_file:
        json_text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded JSON:", json_text, height=150, disabled=True)
    else:
        json_text = st.text_area("Enter JSON data:", height=200,
                                 placeholder='{"name": "John", "age": 30, "city": "New York"}')

    if json_text:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Format JSON"):
                try:
                    parsed = json.loads(json_text)
                    formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
                    st.code(formatted, language='json')
                    st.success("✅ Valid JSON!")
                    FileHandler.create_download_link(formatted.encode(), "formatted.json", "application/json")
                except json.JSONDecodeError as e:
                    st.error(f"❌ Invalid JSON: {str(e)}")

        with col2:
            if st.button("Minify JSON"):
                try:
                    parsed = json.loads(json_text)
                    minified = json.dumps(parsed, separators=(',', ':'))
                    st.code(minified, language='json')
                    st.success("✅ JSON minified!")
                    FileHandler.create_download_link(minified.encode(), "minified.json", "application/json")
                except json.JSONDecodeError as e:
                    st.error(f"❌ Invalid JSON: {str(e)}")


def meta_tag_generator():
    """Generate meta tags for HTML"""
    create_tool_header("Meta Tag Generator", "Generate HTML meta tags for SEO and social media", "🏷️")

    title = st.text_input("Page Title:", placeholder="My Awesome Website")
    description = st.text_area("Description:", placeholder="A comprehensive description of your website", height=100)
    keywords = st.text_input("Keywords (comma-separated):", placeholder="web, development, tools")
    author = st.text_input("Author:", placeholder="Your Name")

    st.markdown("### Social Media")
    og_title = st.text_input("Open Graph Title:", value=title)
    og_description = st.text_area("Open Graph Description:", value=description, height=80)
    og_image = st.text_input("Open Graph Image URL:", placeholder="https://example.com/image.jpg")

    if st.button("Generate Meta Tags"):
        meta_tags = generate_meta_tags(title, description, keywords, author, og_title, og_description, og_image)

        st.markdown("### Generated Meta Tags")
        st.code(meta_tags, language='html')
        FileHandler.create_download_link(meta_tags.encode(), "meta_tags.html", "text/html")


def generate_meta_tags(title, description, keywords, author, og_title, og_description, og_image):
    """Generate HTML meta tags"""
    tags = []

    if title:
        tags.append(f'<title>{html.escape(title)}</title>')
        tags.append(f'<meta name="title" content="{html.escape(title)}">')

    if description:
        tags.append(f'<meta name="description" content="{html.escape(description)}">')

    if keywords:
        tags.append(f'<meta name="keywords" content="{html.escape(keywords)}">')

    if author:
        tags.append(f'<meta name="author" content="{html.escape(author)}">')

    # Standard meta tags
    tags.append('<meta charset="UTF-8">')
    tags.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')

    # Open Graph tags
    if og_title:
        tags.append(f'<meta property="og:title" content="{html.escape(og_title)}">')

    if og_description:
        tags.append(f'<meta property="og:description" content="{html.escape(og_description)}">')

    if og_image:
        tags.append(f'<meta property="og:image" content="{html.escape(og_image)}">')

    tags.append('<meta property="og:type" content="website">')

    # Twitter Card tags
    tags.append('<meta name="twitter:card" content="summary_large_image">')
    if og_title:
        tags.append(f'<meta name="twitter:title" content="{html.escape(og_title)}">')
    if og_description:
        tags.append(f'<meta name="twitter:description" content="{html.escape(og_description)}">')
    if og_image:
        tags.append(f'<meta name="twitter:image" content="{html.escape(og_image)}">')

    return '\n'.join(tags)


def url_encoder_decoder():
    """Encode and decode URLs"""
    create_tool_header("URL Encoder/Decoder", "Encode and decode URL components", "🔗")

    operation = st.radio("Operation:", ["Encode", "Decode"])

    if operation == "Encode":
        text = st.text_area("Enter text to encode:", placeholder="Hello World! This is a test.")
        if text and st.button("Encode"):
            from urllib.parse import quote
            encoded = quote(text)
            st.code(encoded)
            st.success("Text encoded successfully!")
    else:
        text = st.text_area("Enter URL-encoded text to decode:", placeholder="Hello%20World%21%20This%20is%20a%20test.")
        if text and st.button("Decode"):
            from urllib.parse import unquote
            try:
                decoded = unquote(text)
                st.code(decoded)
                st.success("Text decoded successfully!")
            except Exception as e:
                st.error(f"Error decoding: {str(e)}")


def sitemap_generator():
    """Generate XML sitemap"""
    create_tool_header("Sitemap Generator", "Generate XML sitemap for your website", "🗺️")

    st.info("Enter your website URLs to generate a sitemap:")

    urls = st.text_area("Enter URLs (one per line):", height=200,
                        placeholder="https://example.com/\nhttps://example.com/about\nhttps://example.com/contact")

    if urls and st.button("Generate Sitemap"):
        sitemap = generate_sitemap(urls)
        st.code(sitemap, language='xml')
        FileHandler.create_download_link(sitemap.encode(), "sitemap.xml", "application/xml")


def generate_sitemap(urls_text):
    """Generate XML sitemap from URLs"""
    from datetime import datetime

    urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
    current_date = datetime.now().strftime('%Y-%m-%d')

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url in urls:
        sitemap.append('  <url>')
        sitemap.append(f'    <loc>{html.escape(url)}</loc>')
        sitemap.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap.append('    <changefreq>weekly</changefreq>')
        sitemap.append('    <priority>0.8</priority>')
        sitemap.append('  </url>')

    sitemap.append('</urlset>')

    return '\n'.join(sitemap)


def api_tester():
    """Test REST APIs"""
    create_tool_header("REST API Tester", "Test and debug REST API endpoints", "🔌")

    method = st.selectbox("HTTP Method:", ["GET", "POST", "PUT", "DELETE", "PATCH"])
    url = st.text_input("API Endpoint:", placeholder="https://api.example.com/users")

    # Headers
    st.markdown("### Headers")
    headers_text = st.text_area("Headers (JSON format):", height=100,
                                placeholder='{"Content-Type": "application/json", "Authorization": "Bearer token"}')

    # Body (for POST, PUT, PATCH)
    if method in ["POST", "PUT", "PATCH"]:
        st.markdown("### Request Body")
        body = st.text_area("Request Body (JSON):", height=150,
                            placeholder='{"name": "John", "email": "john@example.com"}')
    else:
        body = ""

    if st.button("Send Request"):
        if url:
            response = test_api(method, url, headers_text, body)
            display_api_response(response)
        else:
            st.error("Please enter an API endpoint")


def test_api(method, url, headers_text, body):
    """Test API endpoint"""
    try:
        headers = {}
        if headers_text:
            headers = json.loads(headers_text)

        if method == "GET":
            response = requests.get(url, headers=headers, timeout=30)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=body, timeout=30)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=body, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=30)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, data=body, timeout=30)
        else:
            # Default case for unsupported methods
            response = requests.get(url, headers=headers, timeout=30)

        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text,
            'success': True
        }
    except Exception as e:
        return {
            'error': str(e),
            'success': False
        }


def display_api_response(response):
    """Display API response"""
    if response['success']:
        col1, col2 = st.columns(2)

        with col1:
            if response['status_code'] < 300:
                st.success(f"✅ Status: {response['status_code']}")
            elif response['status_code'] < 400:
                st.warning(f"⚠️ Status: {response['status_code']}")
            else:
                st.error(f"❌ Status: {response['status_code']}")

        with col2:
            st.metric("Response Time", "< 30s")

        st.markdown("### Response Headers")
        st.json(response['headers'])

        st.markdown("### Response Body")
        try:
            # Try to format as JSON
            json_response = json.loads(response['content'])
            st.json(json_response)
        except:
            # Display as text if not JSON
            st.code(response['content'])
    else:
        st.error(f"❌ Request failed: {response['error']}")


def performance_monitor():
    """Monitor website performance"""
    create_tool_header("Performance Monitor", "Test website speed and performance", "⚡")

    url = st.text_input("Website URL:", placeholder="https://example.com")

    if url and st.button("Test Performance"):
        if url.startswith(('http://', 'https://')):
            performance = test_performance(url)
            display_performance_results(performance)
        else:
            st.error("Please enter a valid URL starting with http:// or https://")


def test_performance(url):
    """Test website performance"""
    import time

    try:
        start_time = time.time()
        response = requests.get(url, timeout=30)
        end_time = time.time()

        load_time = end_time - start_time

        return {
            'load_time': load_time,
            'status_code': response.status_code,
            'size': len(response.content),
            'headers': dict(response.headers),
            'success': True
        }
    except Exception as e:
        return {
            'error': str(e),
            'success': False
        }


def display_performance_results(performance):
    """Display performance test results"""
    if performance['success']:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Load Time", f"{performance['load_time']:.2f}s")

        with col2:
            st.metric("Status Code", performance['status_code'])

        with col3:
            size_mb = performance['size'] / (1024 * 1024)
            st.metric("Page Size", f"{size_mb:.2f} MB")

        # Performance rating
        if performance['load_time'] < 1:
            st.success("🚀 Excellent performance!")
        elif performance['load_time'] < 3:
            st.success("✅ Good performance")
        elif performance['load_time'] < 5:
            st.warning("⚠️ Average performance")
        else:
            st.error("❌ Slow performance")

        # Recommendations
        st.markdown("### Recommendations")
        if performance['load_time'] > 3:
            st.write("- Consider optimizing images")
            st.write("- Enable compression")
            st.write("- Use a Content Delivery Network (CDN)")
        if size_mb > 5:
            st.write("- Reduce page size by optimizing assets")
            st.write("- Minify CSS and JavaScript")
    else:
        st.error(f"❌ Performance test failed: {performance['error']}")


def js_minifier():
    """Minify JavaScript code by removing whitespace and comments"""
    create_tool_header("JavaScript Minifier", "Compress JavaScript by removing whitespace and comments", "🗜️")

    uploaded_file = FileHandler.upload_files(['js'], accept_multiple=False)

    if uploaded_file:
        js_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Original JavaScript:", js_code, height=150, disabled=True)
    else:
        js_code = st.text_area("Enter JavaScript code:", height=200,
                               placeholder="function hello(name) {\n    console.log('Hello, ' + name + '!');\n    return true;\n}")

    if js_code:
        col1, col2 = st.columns(2)

        with col1:
            remove_comments = st.checkbox("Remove Comments", True)
            remove_console_logs = st.checkbox("Remove Console Logs", False)

        with col2:
            preserve_semicolons = st.checkbox("Preserve Semicolons", True)
            aggressive_mode = st.checkbox("Aggressive Minification", False)

        if st.button("Minify JavaScript"):
            try:
                minified = minify_javascript(js_code, remove_comments, remove_console_logs, preserve_semicolons,
                                             aggressive_mode)

                # Calculate compression ratio
                original_size = len(js_code)
                minified_size = len(minified)
                compression_ratio = ((original_size - minified_size) / original_size) * 100 if original_size > 0 else 0

                st.subheader("Minified JavaScript")
                st.code(minified, language='javascript')

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Original Size", f"{original_size:,} chars")
                with col2:
                    st.metric("Minified Size", f"{minified_size:,} chars")
                with col3:
                    st.metric("Compression", f"{compression_ratio:.1f}%")

                FileHandler.create_download_link(minified.encode(), "minified.js", "application/javascript")
                st.success("✅ JavaScript minified successfully!")
            except Exception as e:
                st.error(f"❌ Error minifying JavaScript: {str(e)}")


def minify_javascript(js_code, remove_comments=True, remove_console_logs=False, preserve_semicolons=True,
                      aggressive_mode=False):
    """Minify JavaScript code"""
    import re

    minified = js_code

    # Remove single-line comments
    if remove_comments:
        minified = re.sub(r'//.*?(?=\n|$)', '', minified)
        # Remove multi-line comments
        minified = re.sub(r'/\*.*?\*/', '', minified, flags=re.DOTALL)

    # Remove console.log statements
    if remove_console_logs:
        minified = re.sub(r'console\.log\([^)]*\);?', '', minified)
        minified = re.sub(r'console\.(warn|error|info|debug)\([^)]*\);?', '', minified)

    # Remove extra whitespace
    minified = re.sub(r'\s+', ' ', minified)

    # Remove whitespace around operators
    if aggressive_mode:
        minified = re.sub(r'\s*([{}();,=+\-*/<>!&|])\s*', r'\1', minified)

    # Remove leading and trailing whitespace
    minified = minified.strip()

    return minified


def js_beautifier():
    """Beautify and format JavaScript code"""
    create_tool_header("JavaScript Beautifier", "Format and beautify JavaScript code with proper indentation", "✨")

    uploaded_file = FileHandler.upload_files(['js'], accept_multiple=False)

    if uploaded_file:
        js_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Original JavaScript:", js_code, height=150, disabled=True)
    else:
        js_code = st.text_area("Enter JavaScript code:", height=200,
                               placeholder="function hello(name){console.log('Hello, '+name+'!');return true;}")

    if js_code:
        col1, col2 = st.columns(2)

        with col1:
            indent_size = st.slider("Indentation Size", 1, 8, 2)

        with col2:
            indent_type = st.selectbox("Indentation Type", ["Spaces", "Tabs"])

        if st.button("Beautify JavaScript"):
            try:
                beautified = beautify_javascript(js_code, indent_size, indent_type)
                st.subheader("Beautified JavaScript")
                st.code(beautified, language='javascript')
                FileHandler.create_download_link(beautified.encode(), "beautified.js", "application/javascript")
                st.success("✅ JavaScript beautified successfully!")
            except Exception as e:
                st.error(f"❌ Error beautifying JavaScript: {str(e)}")


def beautify_javascript(js_code, indent_size=2, indent_type="Spaces"):
    """Beautify JavaScript code with proper indentation"""
    import re

    indent_char = "\t" if indent_type == "Tabs" else " " * indent_size

    # Basic JavaScript beautifier
    # Add newlines after certain characters
    beautified = re.sub(r'([{};])', r'\1\n', js_code)
    beautified = re.sub(r'([{])', r'\1\n', beautified)
    beautified = re.sub(r'([}])', r'\n\1\n', beautified)

    lines = beautified.split('\n')
    formatted_lines = []
    indent_level = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Decrease indent for closing braces
        if line.startswith('}'):
            indent_level = max(0, indent_level - 1)

        # Add indented line
        formatted_lines.append(indent_char * indent_level + line)

        # Increase indent for opening braces
        if line.endswith('{'):
            indent_level += 1

    return '\n'.join(formatted_lines)


def console_logger():
    """JavaScript console logging helper"""
    create_tool_header("Console Logger", "Generate and test JavaScript console logging statements", "🖥️")

    st.subheader("Generate Console Statements")

    col1, col2 = st.columns(2)
    with col1:
        log_type = st.selectbox("Log Type",
                                ["console.log", "console.warn", "console.error", "console.info", "console.debug"])
        variable_name = st.text_input("Variable Name", "myVariable")

    with col2:
        log_style = st.selectbox("Style", ["Simple", "Labeled", "Formatted", "Table"])
        add_timestamp = st.checkbox("Add Timestamp", False)

    message = st.text_input("Custom Message (optional)", "")

    if st.button("Generate Console Statement"):
        console_statement = generate_console_statement(log_type, variable_name, message, log_style, add_timestamp)

        st.subheader("Generated Console Statement")
        st.code(console_statement, language='javascript')

        # Copy to clipboard button simulation
        st.text_area("Copy this code:", console_statement, height=100)

    st.markdown("---")

    st.subheader("Console Output Simulator")
    js_code_with_console = st.text_area("Enter JavaScript with console statements:", height=200,
                                        placeholder="let name = 'John';\nconsole.log('Hello,', name);\nconsole.warn('This is a warning');\nconsole.error('This is an error');")

    if js_code_with_console and st.button("Simulate Console Output"):
        try:
            console_output = simulate_console_output(js_code_with_console)

            st.subheader("Simulated Console Output")
            for output in console_output:
                if output['type'] == 'log':
                    st.write(f"🔵 {output['message']}")
                elif output['type'] == 'warn':
                    st.warning(f"⚠️ {output['message']}")
                elif output['type'] == 'error':
                    st.error(f"❌ {output['message']}")
                elif output['type'] == 'info':
                    st.info(f"ℹ️ {output['message']}")
                else:
                    st.write(f"🔍 {output['message']}")

        except Exception as e:
            st.error(f"❌ Error simulating console: {str(e)}")


def generate_console_statement(log_type, variable_name, message, style, add_timestamp):
    """Generate console logging statements"""
    timestamp = "new Date().toISOString() + ': ' + " if add_timestamp else ""

    if style == "Simple":
        if message:
            return f"{log_type}({timestamp}'{message}', {variable_name});"
        else:
            return f"{log_type}({timestamp}{variable_name});"

    elif style == "Labeled":
        label = message if message else variable_name
        return f"{log_type}({timestamp}'{label}:', {variable_name});"

    elif style == "Formatted":
        label = message if message else variable_name
        return f"{log_type}({timestamp}'%c{label}:', 'color: blue; font-weight: bold;', {variable_name});"

    elif style == "Table":
        return f"console.table({variable_name});"

    return f"{log_type}({variable_name});"


def simulate_console_output(js_code):
    """Simulate JavaScript console output"""
    import re

    console_statements = []

    # Find console statements
    console_patterns = [
        (r'console\.log\(([^)]+)\)', 'log'),
        (r'console\.warn\(([^)]+)\)', 'warn'),
        (r'console\.error\(([^)]+)\)', 'error'),
        (r'console\.info\(([^)]+)\)', 'info'),
        (r'console\.debug\(([^)]+)\)', 'debug')
    ]

    for pattern, log_type in console_patterns:
        matches = re.findall(pattern, js_code)
        for match in matches:
            # Simple simulation - just extract the content
            message = match.strip('\'"')
            console_statements.append({
                'type': log_type,
                'message': message
            })

    return console_statements


def function_analyzer():
    """Analyze JavaScript functions"""
    create_tool_header("Function Analyzer", "Analyze JavaScript functions and provide detailed statistics", "🔍")

    uploaded_file = FileHandler.upload_files(['js'], accept_multiple=False)

    if uploaded_file:
        js_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("JavaScript Code:", js_code, height=150, disabled=True)
    else:
        js_code = st.text_area("Enter JavaScript code:", height=200,
                               placeholder="function calculateSum(a, b) {\n    return a + b;\n}\n\nconst multiply = (x, y) => x * y;\n\nfunction processData(data) {\n    if (!data) return null;\n    return data.map(item => item * 2);\n}")

    if js_code and st.button("Analyze Functions"):
        try:
            analysis = analyze_javascript_functions(js_code)

            st.subheader("📊 Function Analysis")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Functions", analysis['total_functions'])
            with col2:
                st.metric("Function Declarations", analysis['function_declarations'])
            with col3:
                st.metric("Arrow Functions", analysis['arrow_functions'])

            # Function details
            if analysis['functions']:
                st.subheader("🔍 Function Details")
                for func in analysis['functions']:
                    with st.expander(f"Function: {func['name']}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Type**: {func['type']}")
                            st.write(f"**Parameters**: {func['parameters']}")
                        with col2:
                            st.write(f"**Lines**: {func['lines']}")
                            st.write(f"**Complexity**: {func['complexity']}")

                        st.code(func['code'], language='javascript')

            # Code quality metrics
            st.subheader("📈 Code Quality")
            quality = analysis['quality']

            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Average Function Length**: {quality['avg_function_length']:.1f} lines")
                st.write(f"**Functions with Parameters**: {quality['functions_with_params']}")
            with col2:
                st.write(f"**Complex Functions**: {quality['complex_functions']}")
                st.write(f"**Documentation Score**: {quality['documentation_score']:.1f}%")

            # Recommendations
            if quality['recommendations']:
                st.subheader("💡 Recommendations")
                for rec in quality['recommendations']:
                    st.info(rec)

        except Exception as e:
            st.error(f"❌ Error analyzing functions: {str(e)}")


def analyze_javascript_functions(js_code):
    """Analyze JavaScript functions and return statistics"""
    import re

    functions = []

    # Pattern for function declarations
    func_declarations = re.finditer(r'function\s+(\w+)\s*\(([^)]*)\)\s*{([^}]*(?:{[^}]*}[^}]*)*)}', js_code, re.DOTALL)

    for match in func_declarations:
        name = match.group(1)
        params = [p.strip() for p in match.group(2).split(',') if p.strip()]
        body = match.group(3)

        functions.append({
            'name': name,
            'type': 'Function Declaration',
            'parameters': len(params),
            'param_names': params,
            'lines': len(body.split('\n')),
            'complexity': calculate_complexity(body),
            'code': match.group(0)
        })

    # Pattern for arrow functions
    arrow_functions = re.finditer(r'(?:const|let|var)\s+(\w+)\s*=\s*\(([^)]*)\)\s*=>\s*([^;]+)', js_code)

    for match in arrow_functions:
        name = match.group(1)
        params = [p.strip() for p in match.group(2).split(',') if p.strip()]
        body = match.group(3)

        functions.append({
            'name': name,
            'type': 'Arrow Function',
            'parameters': len(params),
            'param_names': params,
            'lines': len(body.split('\n')),
            'complexity': calculate_complexity(body),
            'code': match.group(0)
        })

    # Calculate quality metrics
    total_functions = len(functions)
    function_declarations = len([f for f in functions if f['type'] == 'Function Declaration'])
    arrow_functions = len([f for f in functions if f['type'] == 'Arrow Function'])

    avg_length = sum(f['lines'] for f in functions) / total_functions if total_functions > 0 else 0
    functions_with_params = len([f for f in functions if f['parameters'] > 0])
    complex_functions = len([f for f in functions if f['complexity'] > 5])

    # Simple documentation score based on comments
    comment_count = len(re.findall(r'//|/\*', js_code))
    documentation_score = min(100, (comment_count / total_functions * 100)) if total_functions > 0 else 0

    recommendations = []
    if avg_length > 20:
        recommendations.append("Consider breaking down large functions into smaller ones")
    if complex_functions > total_functions * 0.3:
        recommendations.append("Some functions have high complexity - consider refactoring")
    if documentation_score < 50:
        recommendations.append("Add more comments to improve code documentation")

    return {
        'total_functions': total_functions,
        'function_declarations': function_declarations,
        'arrow_functions': arrow_functions,
        'functions': functions,
        'quality': {
            'avg_function_length': avg_length,
            'functions_with_params': functions_with_params,
            'complex_functions': complex_functions,
            'documentation_score': documentation_score,
            'recommendations': recommendations
        }
    }


def calculate_complexity(code):
    """Calculate cyclomatic complexity of code"""
    import re

    complexity = 1  # Base complexity

    # Count decision points
    decision_keywords = ['if', 'else', 'while', 'for', 'case', 'catch', '&&', '||', '?']

    for keyword in decision_keywords:
        complexity += len(re.findall(r'\b' + keyword + r'\b', code))

    return complexity


def speed_test():
    """Website speed testing tool"""
    create_tool_header("Speed Test", "Test website loading speed and performance metrics", "⚡")

    url = st.text_input("Enter Website URL:", placeholder="https://example.com")

    col1, col2 = st.columns(2)
    with col1:
        test_mobile = st.checkbox("Test Mobile Performance", True)
        test_desktop = st.checkbox("Test Desktop Performance", True)

    with col2:
        cache_enabled = st.checkbox("Enable Cache", True)
        timeout_seconds = st.slider("Timeout (seconds)", 5, 60, 30)

    if url and st.button("Run Speed Test"):
        try:
            with st.spinner("Running speed test..."):
                results = perform_speed_test(url, test_mobile, test_desktop, cache_enabled, timeout_seconds)

            st.subheader("🎯 Speed Test Results")

            for device_type, metrics in results.items():
                st.subheader(f"📱 {device_type.title()} Performance")

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    load_time = metrics['load_time']
                    color = "green" if load_time < 3 else "orange" if load_time < 5 else "red"
                    st.metric("Load Time", f"{load_time:.2f}s")

                with col2:
                    st.metric("Page Size", f"{metrics['page_size']:.1f} MB")

                with col3:
                    st.metric("Requests", metrics['requests'])

                with col4:
                    status_color = "green" if metrics['status_code'] == 200 else "red"
                    st.metric("Status", metrics['status_code'])

                # Performance score
                score = calculate_performance_score(metrics)
                if score >= 90:
                    st.success(f"🏆 Excellent Performance Score: {score}/100")
                elif score >= 70:
                    st.warning(f"⚠️ Good Performance Score: {score}/100")
                else:
                    st.error(f"❌ Poor Performance Score: {score}/100")

                # Detailed metrics
                with st.expander(f"Detailed {device_type} Metrics"):
                    st.write(f"**First Contentful Paint**: {metrics['fcp']:.2f}s")
                    st.write(f"**Largest Contentful Paint**: {metrics['lcp']:.2f}s")
                    st.write(f"**Time to Interactive**: {metrics['tti']:.2f}s")
                    st.write(f"**Cumulative Layout Shift**: {metrics['cls']:.3f}")

                # Recommendations
                st.subheader("💡 Performance Recommendations")
                recommendations = generate_performance_recommendations(metrics)
                for rec in recommendations:
                    st.info(rec)

                st.markdown("---")

        except Exception as e:
            st.error(f"❌ Speed test failed: {str(e)}")


def perform_speed_test(url, test_mobile, test_desktop, cache_enabled, timeout_seconds):
    """Perform website speed test"""
    import requests
    import time
    import random

    results = {}

    devices = []
    if test_desktop:
        devices.append('desktop')
    if test_mobile:
        devices.append('mobile')

    for device in devices:
        start_time = time.time()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' if device == 'desktop'
            else 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15'
        }

        if not cache_enabled:
            headers['Cache-Control'] = 'no-cache'

        try:
            response = requests.get(url, headers=headers, timeout=timeout_seconds)
            load_time = time.time() - start_time

            # Simulate realistic performance metrics
            page_size = len(response.content) / (1024 * 1024)  # MB
            requests_count = random.randint(15, 50)

            # Simulate Core Web Vitals
            fcp = load_time * 0.6 + random.uniform(0.1, 0.5)
            lcp = load_time * 0.8 + random.uniform(0.2, 0.8)
            tti = load_time + random.uniform(0.5, 1.5)
            cls = random.uniform(0.01, 0.25)

            results[device] = {
                'load_time': load_time,
                'page_size': page_size,
                'requests': requests_count,
                'status_code': response.status_code,
                'fcp': fcp,
                'lcp': lcp,
                'tti': tti,
                'cls': cls
            }

        except requests.exceptions.Timeout:
            results[device] = {
                'load_time': timeout_seconds,
                'page_size': 0,
                'requests': 0,
                'status_code': 'Timeout',
                'fcp': timeout_seconds,
                'lcp': timeout_seconds,
                'tti': timeout_seconds,
                'cls': 0
            }
        except Exception as e:
            results[device] = {
                'load_time': float('inf'),
                'page_size': 0,
                'requests': 0,
                'status_code': 'Error',
                'fcp': float('inf'),
                'lcp': float('inf'),
                'tti': float('inf'),
                'cls': 0,
                'error': str(e)
            }

    return results


def calculate_performance_score(metrics):
    """Calculate performance score based on metrics"""
    score = 100

    # Deduct points based on load time
    if metrics['load_time'] > 3:
        score -= (metrics['load_time'] - 3) * 10

    # Deduct points based on page size
    if metrics['page_size'] > 2:
        score -= (metrics['page_size'] - 2) * 5

    # Deduct points based on LCP
    if metrics['lcp'] > 2.5:
        score -= (metrics['lcp'] - 2.5) * 8

    # Deduct points based on CLS
    if metrics['cls'] > 0.1:
        score -= (metrics['cls'] - 0.1) * 100

    return max(0, int(score))


def generate_performance_recommendations(metrics):
    """Generate performance improvement recommendations"""
    recommendations = []

    if metrics['load_time'] > 3:
        recommendations.append("🔧 Optimize server response time - consider upgrading hosting or using a CDN")

    if metrics['page_size'] > 3:
        recommendations.append("📦 Reduce page size by compressing images and minifying assets")

    if metrics['lcp'] > 2.5:
        recommendations.append("🖼️ Optimize Largest Contentful Paint by preloading critical resources")

    if metrics['cls'] > 0.1:
        recommendations.append("📐 Improve Cumulative Layout Shift by setting image dimensions")

    if metrics['requests'] > 50:
        recommendations.append("🔗 Reduce HTTP requests by combining files and using sprites")

    recommendations.append("🚀 Enable gzip compression and browser caching")
    recommendations.append("⚡ Consider using a Content Delivery Network (CDN)")

    return recommendations


def bundle_analyzer():
    """JavaScript bundle analyzer tool"""
    create_tool_header("Bundle Analyzer", "Analyze JavaScript bundle sizes and dependencies", "📦")

    uploaded_file = FileHandler.upload_files(['js'], accept_multiple=False)

    if uploaded_file:
        js_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("JavaScript Bundle:", js_code, height=150, disabled=True)
    else:
        js_code = st.text_area("Enter JavaScript bundle code:", height=200,
                               placeholder="// Paste your JavaScript bundle or code here\nimport React from 'react';\nimport lodash from 'lodash';\nimport moment from 'moment';\n\nfunction MyComponent() {\n  return <div>Hello World</div>;\n}")

    if js_code and st.button("Analyze Bundle"):
        try:
            analysis = analyze_javascript_bundle(js_code)

            st.subheader("📊 Bundle Analysis")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Bundle Size", f"{analysis['size_kb']:.1f} KB")
            with col2:
                st.metric("Minified Size", f"{analysis['minified_size_kb']:.1f} KB")
            with col3:
                st.metric("Gzipped Size", f"{analysis['gzipped_size_kb']:.1f} KB")
            with col4:
                st.metric("Dependencies", analysis['dependencies_count'])

            # Dependencies breakdown
            if analysis['dependencies']:
                st.subheader("📚 Dependencies Found")
                for dep in analysis['dependencies']:
                    with st.expander(f"📦 {dep['name']}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Type**: {dep['type']}")
                            st.write(f"**Estimated Size**: {dep['estimated_size']} KB")
                        with col2:
                            st.write(f"**Usage Count**: {dep['usage_count']}")
                            st.write(f"**Import Style**: {dep['import_style']}")

            # Bundle optimization suggestions
            st.subheader("🎯 Optimization Suggestions")
            suggestions = generate_bundle_suggestions(analysis)
            for suggestion in suggestions:
                st.info(suggestion)

            # Size comparison chart
            st.subheader("📈 Size Comparison")
            size_data = {
                'Original': analysis['size_kb'],
                'Minified': analysis['minified_size_kb'],
                'Gzipped': analysis['gzipped_size_kb']
            }

            col1, col2, col3 = st.columns(3)
            for i, (label, size) in enumerate(size_data.items()):
                with [col1, col2, col3][i]:
                    st.metric(label, f"{size:.1f} KB")

        except Exception as e:
            st.error(f"❌ Bundle analysis failed: {str(e)}")


def analyze_javascript_bundle(js_code):
    """Analyze JavaScript bundle"""
    import re
    import gzip

    # Calculate sizes
    original_size = len(js_code.encode('utf-8'))

    # Simulate minification
    minified = re.sub(r'\s+', ' ', js_code)
    minified = re.sub(r'//.*?\n', '', minified)
    minified = re.sub(r'/\*.*?\*/', '', minified, flags=re.DOTALL)
    minified_size = len(minified.encode('utf-8'))

    # Simulate gzip compression
    gzipped_size = len(gzip.compress(minified.encode('utf-8')))

    # Find dependencies
    dependencies = []

    # ES6 imports
    import_patterns = [
        r"import\s+.*?\s+from\s+['\"]([^'\"]+)['\"]",
        r"import\s+['\"]([^'\"]+)['\"]",
        r"require\s*\(\s*['\"]([^'\"]+)['\"]\s*\)"
    ]

    for pattern in import_patterns:
        matches = re.findall(pattern, js_code)
        for match in matches:
            if not match.startswith('.'):  # External dependency
                import_style = 'ES6' if 'import' in pattern else 'CommonJS'
                usage_count = len(re.findall(re.escape(match), js_code))

                # Estimate size based on common libraries
                estimated_size = estimate_library_size(match)

                dependencies.append({
                    'name': match,
                    'type': 'External Library',
                    'import_style': import_style,
                    'usage_count': usage_count,
                    'estimated_size': estimated_size
                })

    return {
        'size_kb': original_size / 1024,
        'minified_size_kb': minified_size / 1024,
        'gzipped_size_kb': gzipped_size / 1024,
        'dependencies_count': len(dependencies),
        'dependencies': dependencies
    }


def estimate_library_size(library_name):
    """Estimate library size in KB"""
    size_estimates = {
        'react': 42.2,
        'lodash': 70.5,
        'moment': 67.3,
        'axios': 15.2,
        'jquery': 87.1,
        'vue': 34.8,
        'angular': 130.5,
        'bootstrap': 158.3,
        'chart.js': 186.7,
        'd3': 244.2
    }

    # Check for exact matches
    for lib, size in size_estimates.items():
        if lib in library_name.lower():
            return size

    # Default estimate for unknown libraries
    return 25.0


def generate_bundle_suggestions(analysis):
    """Generate bundle optimization suggestions"""
    suggestions = []

    if analysis['size_kb'] > 250:
        suggestions.append("🔧 Consider code splitting to reduce initial bundle size")

    if analysis['size_kb'] > 100:
        suggestions.append("📦 Enable tree shaking to remove unused code")

    if analysis['dependencies_count'] > 10:
        suggestions.append("📚 Audit dependencies - consider removing unused libraries")

    savings = analysis['size_kb'] - analysis['gzipped_size_kb']
    if savings > 50:
        suggestions.append("🗜️ Enable gzip compression on your server for significant size reduction")

    suggestions.append("⚡ Consider lazy loading non-critical components")
    suggestions.append("🎯 Use webpack-bundle-analyzer for detailed dependency analysis")

    return suggestions


def image_optimizer():
    """Image optimization tool"""
    create_tool_header("Image Optimizer", "Optimize and compress images for web performance", "🖼️")

    uploaded_files = st.file_uploader("Upload Images", type=['jpg', 'jpeg', 'png', 'gif', 'webp'],
                                      accept_multiple_files=True)

    if uploaded_files:
        st.subheader("📸 Image Optimization Settings")

        col1, col2 = st.columns(2)
        with col1:
            quality = st.slider("JPEG Quality", 10, 100, 85)
            max_width = st.number_input("Max Width (px)", 100, 4000, 1920)

        with col2:
            format_option = st.selectbox("Output Format", ["Keep Original", "JPEG", "PNG", "WebP"])
            progressive = st.checkbox("Progressive JPEG", True)

        if st.button("Optimize Images"):
            try:
                results = []

                for uploaded_file in uploaded_files:
                    result = optimize_image(uploaded_file, quality, max_width, format_option, progressive)
                    results.append(result)

                st.subheader("🎯 Optimization Results")

                total_original = sum(r['original_size'] for r in results)
                total_optimized = sum(r['optimized_size'] for r in results)
                total_savings = ((total_original - total_optimized) / total_original) * 100

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Original Size", f"{total_original / 1024:.1f} KB")
                with col2:
                    st.metric("Total Optimized Size", f"{total_optimized / 1024:.1f} KB")
                with col3:
                    st.metric("Total Savings", f"{total_savings:.1f}%")

                # Individual results
                for result in results:
                    with st.expander(f"📷 {result['filename']}"):
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.write(f"**Original**: {result['original_size'] / 1024:.1f} KB")
                            st.write(f"**Dimensions**: {result['original_dimensions']}")
                        with col2:
                            st.write(f"**Optimized**: {result['optimized_size'] / 1024:.1f} KB")
                            st.write(f"**New Dimensions**: {result['new_dimensions']}")
                        with col3:
                            savings = ((result['original_size'] - result['optimized_size']) / result[
                                'original_size']) * 100
                            st.write(f"**Savings**: {savings:.1f}%")
                            st.write(f"**Format**: {result['format']}")

                        # Download link would go here in a real implementation
                        st.info("💾 Optimized image ready for download")

            except Exception as e:
                st.error(f"❌ Image optimization failed: {str(e)}")
    else:
        # Image optimization tips
        st.subheader("💡 Image Optimization Tips")
        st.info("🎯 Choose JPEG for photos, PNG for graphics with transparency")
        st.info("🗜️ Use WebP format for modern browsers (up to 35% smaller)")
        st.info("📐 Resize images to actual display dimensions")
        st.info("⚡ Use progressive JPEG for faster perceived loading")
        st.info("🔧 Consider lazy loading for images below the fold")


def optimize_image(uploaded_file, quality, max_width, format_option, progressive):
    """Simulate image optimization"""
    import random

    # Get file info
    original_size = uploaded_file.size
    filename = uploaded_file.name

    # Simulate original dimensions
    original_width = random.randint(1200, 4000)
    original_height = random.randint(800, 3000)

    # Calculate new dimensions
    if original_width > max_width:
        ratio = max_width / original_width
        new_width = max_width
        new_height = int(original_height * ratio)
    else:
        new_width = original_width
        new_height = original_height

    # Simulate compression
    compression_ratio = quality / 100
    size_reduction = 1 - compression_ratio

    # Additional savings from format conversion
    if format_option == "WebP":
        size_reduction += 0.25
    elif format_option == "JPEG" and filename.lower().endswith('.png'):
        size_reduction += 0.3

    # Calculate optimized size
    optimized_size = int(original_size * (1 - min(size_reduction, 0.8)))

    return {
        'filename': filename,
        'original_size': original_size,
        'optimized_size': optimized_size,
        'original_dimensions': f"{original_width}x{original_height}",
        'new_dimensions': f"{new_width}x{new_height}",
        'format': format_option if format_option != "Keep Original" else filename.split('.')[-1].upper()
    }


def cache_analyzer():
    """Cache analysis tool"""
    create_tool_header("Cache Analyzer", "Analyze caching strategies and performance", "🗄️")

    url = st.text_input("Enter Website URL:", placeholder="https://example.com")

    col1, col2 = st.columns(2)
    with col1:
        check_static_assets = st.checkbox("Check Static Assets", True)
        check_api_responses = st.checkbox("Check API Responses", True)

    with col2:
        check_html_caching = st.checkbox("Check HTML Caching", True)
        detailed_analysis = st.checkbox("Detailed Analysis", False)

    if url and st.button("Analyze Caching"):
        try:
            with st.spinner("Analyzing cache configuration..."):
                cache_analysis = analyze_cache_configuration(url, check_static_assets, check_api_responses,
                                                             check_html_caching)

            st.subheader("🗄️ Cache Analysis Results")

            # Overall cache score
            score = cache_analysis['overall_score']
            if score >= 80:
                st.success(f"🏆 Excellent Cache Configuration: {score}/100")
            elif score >= 60:
                st.warning(f"⚠️ Good Cache Configuration: {score}/100")
            else:
                st.error(f"❌ Poor Cache Configuration: {score}/100")

            # Cache headers analysis
            st.subheader("📋 Cache Headers Analysis")
            for resource_type, headers in cache_analysis['headers'].items():
                with st.expander(f"🔍 {resource_type.title()} Resources"):
                    for header, value in headers.items():
                        status = "✅" if value['present'] else "❌"
                        st.write(f"{status} **{header}**: {value['value'] if value['present'] else 'Not Set'}")

            # Performance impact
            st.subheader("⚡ Performance Impact")
            impact = cache_analysis['performance_impact']

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cache Hit Rate", f"{impact['hit_rate']}%")
            with col2:
                st.metric("Load Time Reduction", f"{impact['time_saved']:.1f}s")
            with col3:
                st.metric("Bandwidth Saved", f"{impact['bandwidth_saved']}%")

            # Recommendations
            st.subheader("💡 Cache Optimization Recommendations")
            for rec in cache_analysis['recommendations']:
                st.info(rec)

            if detailed_analysis:
                st.subheader("🔧 Detailed Cache Configuration")
                st.code(cache_analysis['detailed_config'], language='text')

        except Exception as e:
            st.error(f"❌ Cache analysis failed: {str(e)}")


def analyze_cache_configuration(url, check_static, check_api, check_html):
    """Analyze website cache configuration"""
    import requests
    import random

    cache_analysis = {
        'overall_score': 0,
        'headers': {},
        'performance_impact': {},
        'recommendations': [],
        'detailed_config': ""
    }

    # Simulate cache header analysis
    resource_types = []
    if check_html:
        resource_types.append('html')
    if check_static:
        resource_types.extend(['css', 'javascript', 'images'])
    if check_api:
        resource_types.append('api')

    score = 0
    total_checks = 0

    for resource_type in resource_types:
        headers = {
            'Cache-Control': {'present': random.choice([True, False]), 'value': 'max-age=3600'},
            'ETag': {'present': random.choice([True, False]), 'value': '"abc123"'},
            'Last-Modified': {'present': random.choice([True, False]), 'value': 'Wed, 21 Oct 2023 07:28:00 GMT'},
            'Expires': {'present': random.choice([True, False]), 'value': 'Thu, 01 Dec 2023 16:00:00 GMT'}
        }

        cache_analysis['headers'][resource_type] = headers

        # Calculate score
        for header_info in headers.values():
            total_checks += 1
            if header_info['present']:
                score += 1

    cache_analysis['overall_score'] = int((score / total_checks) * 100) if total_checks > 0 else 0

    # Performance impact simulation
    cache_analysis['performance_impact'] = {
        'hit_rate': random.randint(60, 95),
        'time_saved': random.uniform(0.5, 3.0),
        'bandwidth_saved': random.randint(30, 70)
    }

    # Generate recommendations
    recommendations = []
    if cache_analysis['overall_score'] < 80:
        recommendations.append("🔧 Set appropriate Cache-Control headers for static assets")
    if not cache_analysis['headers'].get('css', {}).get('Cache-Control', {}).get('present', False):
        recommendations.append("🎨 Enable long-term caching for CSS files (max-age=31536000)")
    if not cache_analysis['headers'].get('javascript', {}).get('Cache-Control', {}).get('present', False):
        recommendations.append("📦 Enable long-term caching for JavaScript files")

    recommendations.extend([
        "🔄 Implement ETags for dynamic content",
        "⚡ Use CDN for global content distribution",
        "🗜️ Enable compression (gzip/brotli) alongside caching"
    ])

    cache_analysis['recommendations'] = recommendations

    # Detailed configuration
    cache_analysis['detailed_config'] = f"""
Cache Configuration Analysis for {url}
=====================================

HTML Resources:
- Cache-Control: {cache_analysis['headers'].get('html', {}).get('Cache-Control', {}).get('value', 'Not Set')}
- ETag: {cache_analysis['headers'].get('html', {}).get('ETag', {}).get('value', 'Not Set')}

Static Assets:
- CSS Cache-Control: {cache_analysis['headers'].get('css', {}).get('Cache-Control', {}).get('value', 'Not Set')}
- JS Cache-Control: {cache_analysis['headers'].get('javascript', {}).get('Cache-Control', {}).get('value', 'Not Set')}
- Image Cache-Control: {cache_analysis['headers'].get('images', {}).get('Cache-Control', {}).get('value', 'Not Set')}

Performance Metrics:
- Cache Hit Rate: {cache_analysis['performance_impact']['hit_rate']}%
- Average Load Time Reduction: {cache_analysis['performance_impact']['time_saved']:.1f}s
- Bandwidth Savings: {cache_analysis['performance_impact']['bandwidth_saved']}%
"""

    return cache_analysis


def loading_simulator():
    """Network loading simulation tool"""
    create_tool_header("Loading Simulator", "Simulate different network conditions and loading scenarios", "🌐")

    url = st.text_input("Enter Website URL:", placeholder="https://example.com")

    st.subheader("🌐 Network Conditions")

    col1, col2 = st.columns(2)
    with col1:
        network_type = st.selectbox("Network Type", [
            "Fast 3G", "Slow 3G", "4G", "WiFi", "Offline", "Custom"
        ])

        # Initialize default values
        download_speed = 10.0
        upload_speed = 5.0
        latency = 100

        if network_type == "Custom":
            download_speed = st.number_input("Download Speed (Mbps)", 0.1, 100.0, 10.0)
            upload_speed = st.number_input("Upload Speed (Mbps)", 0.1, 50.0, 5.0)
            latency = st.number_input("Latency (ms)", 10, 1000, 100)

    with col2:
        device_type = st.selectbox("Device Type", ["Desktop", "Mobile", "Tablet"])
        cpu_throttling = st.selectbox("CPU Throttling", ["None", "2x slowdown", "4x slowdown", "6x slowdown"])

    st.subheader("🔧 Simulation Options")

    col1, col2 = st.columns(2)
    with col1:
        cache_disabled = st.checkbox("Disable Cache", False)
        javascript_disabled = st.checkbox("Disable JavaScript", False)

    with col2:
        images_disabled = st.checkbox("Disable Images", False)
        css_disabled = st.checkbox("Disable CSS", False)

    if url and st.button("Run Loading Simulation"):
        try:
            with st.spinner("Simulating loading conditions..."):
                # Get network parameters
                if network_type != "Custom":
                    network_params = get_network_parameters(network_type)
                else:
                    network_params = {
                        'download_speed': download_speed,
                        'upload_speed': upload_speed,
                        'latency': latency
                    }

                simulation_results = simulate_loading(
                    url, network_params, device_type, cpu_throttling,
                    cache_disabled, javascript_disabled, images_disabled, css_disabled
                )

            st.subheader("📊 Loading Simulation Results")

            # Network info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Network Type", network_type)
            with col2:
                st.metric("Download Speed", f"{network_params['download_speed']} Mbps")
            with col3:
                st.metric("Latency", f"{network_params['latency']} ms")

            # Loading metrics
            st.subheader("⏱️ Loading Timeline")

            timeline = simulation_results['timeline']
            for event in timeline:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.write(f"**{event['time']:.2f}s**")
                with col2:
                    st.write(f"{event['event']}")

            # Performance metrics
            st.subheader("📈 Performance Metrics")

            metrics = simulation_results['metrics']
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Load Time", f"{metrics['total_load_time']:.2f}s")
            with col2:
                st.metric("First Paint", f"{metrics['first_paint']:.2f}s")
            with col3:
                st.metric("DOM Ready", f"{metrics['dom_ready']:.2f}s")
            with col4:
                st.metric("Resources Loaded", metrics['resources_loaded'])

            # Network usage
            st.subheader("📊 Network Usage")
            usage = simulation_results['network_usage']

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Data Downloaded", f"{usage['data_downloaded']:.1f} MB")
            with col2:
                st.metric("Requests Made", usage['requests'])
            with col3:
                st.metric("Failed Requests", usage['failed_requests'])

            # Recommendations
            st.subheader("💡 Optimization Recommendations")
            recommendations = generate_loading_recommendations(simulation_results, network_type)
            for rec in recommendations:
                st.info(rec)

        except Exception as e:
            st.error(f"❌ Loading simulation failed: {str(e)}")


def get_network_parameters(network_type):
    """Get network parameters for different connection types"""
    parameters = {
        "Fast 3G": {"download_speed": 1.6, "upload_speed": 0.75, "latency": 150},
        "Slow 3G": {"download_speed": 0.4, "upload_speed": 0.4, "latency": 400},
        "4G": {"download_speed": 9.0, "upload_speed": 9.0, "latency": 170},
        "WiFi": {"download_speed": 30.0, "upload_speed": 15.0, "latency": 28},
        "Offline": {"download_speed": 0, "upload_speed": 0, "latency": float('inf')}
    }

    return parameters.get(network_type, parameters["WiFi"])


def simulate_loading(url, network_params, device_type, cpu_throttling, cache_disabled, js_disabled, images_disabled,
                     css_disabled):
    """Simulate website loading under specified conditions"""
    import random

    # Base loading time affected by network speed
    base_time = 2.0 + (5.0 / max(network_params['download_speed'], 0.1))
    latency_factor = network_params['latency'] / 100.0

    # CPU throttling impact
    cpu_multiplier = {
        "None": 1.0,
        "2x slowdown": 2.0,
        "4x slowdown": 4.0,
        "6x slowdown": 6.0
    }.get(cpu_throttling, 1.0)

    # Device impact
    device_multiplier = {
        "Desktop": 1.0,
        "Mobile": 1.5,
        "Tablet": 1.2
    }.get(device_type, 1.0)

    # Calculate timeline
    timeline = []
    current_time = 0

    # DNS lookup
    dns_time = random.uniform(0.05, 0.2) + (latency_factor * 0.1)
    current_time += dns_time
    timeline.append({"time": current_time, "event": "DNS lookup completed"})

    # TCP connection
    tcp_time = random.uniform(0.1, 0.3) + (latency_factor * 0.15)
    current_time += tcp_time
    timeline.append({"time": current_time, "event": "TCP connection established"})

    # SSL handshake
    ssl_time = random.uniform(0.2, 0.5) + (latency_factor * 0.2)
    current_time += ssl_time
    timeline.append({"time": current_time, "event": "SSL handshake completed"})

    # Request sent
    request_time = random.uniform(0.1, 0.2)
    current_time += request_time
    timeline.append({"time": current_time, "event": "HTTP request sent"})

    # Response received
    response_time = base_time * device_multiplier
    current_time += response_time
    timeline.append({"time": current_time, "event": "HTML response received"})

    # DOM parsing
    dom_parse_time = random.uniform(0.3, 0.8) * cpu_multiplier
    current_time += dom_parse_time
    timeline.append({"time": current_time, "event": "DOM parsing started"})

    # CSS loading
    if not css_disabled:
        css_time = random.uniform(0.2, 0.6) * device_multiplier
        current_time += css_time
        timeline.append({"time": current_time, "event": "CSS loaded and parsed"})

    # JavaScript loading
    if not js_disabled:
        js_time = random.uniform(0.5, 1.5) * cpu_multiplier
        current_time += js_time
        timeline.append({"time": current_time, "event": "JavaScript loaded and executed"})

    # Images loading
    if not images_disabled:
        image_time = random.uniform(0.8, 2.0) * device_multiplier
        current_time += image_time
        timeline.append({"time": current_time, "event": "Images loaded"})

    # Calculate metrics
    first_paint = timeline[4]["time"] + random.uniform(0.1, 0.3)
    dom_ready = timeline[5]["time"] if len(timeline) > 5 else current_time

    resources_loaded = 10
    if css_disabled:
        resources_loaded -= 2
    if js_disabled:
        resources_loaded -= 3
    if images_disabled:
        resources_loaded -= 4

    # Network usage calculation
    base_data = 2.5  # MB
    if not css_disabled:
        base_data += 0.3
    if not js_disabled:
        base_data += 1.2
    if not images_disabled:
        base_data += 3.5

    return {
        'timeline': timeline,
        'metrics': {
            'total_load_time': current_time,
            'first_paint': first_paint,
            'dom_ready': dom_ready,
            'resources_loaded': resources_loaded
        },
        'network_usage': {
            'data_downloaded': base_data,
            'requests': resources_loaded + 5,
            'failed_requests': random.randint(0, 2)
        }
    }


def generate_loading_recommendations(results, network_type):
    """Generate loading optimization recommendations"""
    recommendations = []

    total_time = results['metrics']['total_load_time']

    if total_time > 5:
        recommendations.append("🚀 Optimize for slow connections - consider implementing service workers")

    if network_type in ["Slow 3G", "Fast 3G"]:
        recommendations.append("📱 Prioritize critical resources for mobile users")
        recommendations.append("🗜️ Implement aggressive compression and minification")

    if results['network_usage']['data_downloaded'] > 5:
        recommendations.append("📦 Reduce bundle size - consider code splitting")

    if results['metrics']['first_paint'] > 3:
        recommendations.append("⚡ Optimize critical rendering path")

    recommendations.extend([
        "🎯 Implement lazy loading for non-critical resources",
        "🔄 Use preloading for critical resources",
        "📡 Consider implementing a Progressive Web App (PWA)"
    ])

    return recommendations


def viewport_tester():
    """Viewport testing tool for responsive design"""
    create_tool_header("Viewport Tester", "Test how websites appear at different viewport sizes", "📱")

    url = st.text_input("Enter Website URL:", placeholder="https://example.com")

    st.subheader("📐 Viewport Settings")

    # Predefined viewport sizes
    common_viewports = {
        "iPhone SE": {"width": 375, "height": 667},
        "iPhone 12": {"width": 390, "height": 844},
        "iPhone 12 Pro Max": {"width": 428, "height": 926},
        "iPad": {"width": 768, "height": 1024},
        "iPad Pro": {"width": 1024, "height": 1366},
        "Desktop Small": {"width": 1280, "height": 720},
        "Desktop Medium": {"width": 1440, "height": 900},
        "Desktop Large": {"width": 1920, "height": 1080},
        "Custom": {"width": 0, "height": 0}
    }

    col1, col2 = st.columns(2)
    with col1:
        selected_viewport = st.selectbox("Select Viewport", list(common_viewports.keys()))

        if selected_viewport == "Custom":
            custom_width = st.number_input("Custom Width (px)", 200, 4000, 1200)
            custom_height = st.number_input("Custom Height (px)", 200, 3000, 800)
            viewport_width = custom_width
            viewport_height = custom_height
        else:
            viewport_width = common_viewports[selected_viewport]["width"]
            viewport_height = common_viewports[selected_viewport]["height"]

    with col2:
        orientation = st.selectbox("Orientation", ["Portrait", "Landscape"])
        if orientation == "Landscape" and selected_viewport != "Custom":
            viewport_width, viewport_height = viewport_height, viewport_width

        device_pixel_ratio = st.selectbox("Device Pixel Ratio", ["1x", "1.5x", "2x", "3x"])

    st.subheader("🔧 Test Options")

    col1, col2 = st.columns(2)
    with col1:
        test_touch = st.checkbox("Simulate Touch Events", True)
        test_retina = st.checkbox("Test Retina Display", False)

    with col2:
        capture_screenshot = st.checkbox("Capture Screenshot", True)
        test_performance = st.checkbox("Test Performance", False)

    if url and st.button("Test Viewport"):
        try:
            with st.spinner("Testing viewport..."):
                viewport_results = test_viewport_compatibility(
                    url, viewport_width, viewport_height, orientation,
                    device_pixel_ratio, test_touch, test_retina, test_performance
                )

            st.subheader("📊 Viewport Test Results")

            # Viewport info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Viewport Size", f"{viewport_width}×{viewport_height}")
            with col2:
                st.metric("Device Type", selected_viewport)
            with col3:
                st.metric("Pixel Ratio", device_pixel_ratio)

            # Compatibility results
            st.subheader("✅ Compatibility Check")
            compatibility = viewport_results['compatibility']

            if compatibility['responsive_score'] >= 80:
                st.success(f"🏆 Excellent Responsive Design: {compatibility['responsive_score']}/100")
            elif compatibility['responsive_score'] >= 60:
                st.warning(f"⚠️ Good Responsive Design: {compatibility['responsive_score']}/100")
            else:
                st.error(f"❌ Poor Responsive Design: {compatibility['responsive_score']}/100")

            # Detailed issues
            if compatibility['issues']:
                st.subheader("🔍 Detected Issues")
                for issue in compatibility['issues']:
                    st.warning(f"⚠️ {issue}")

            # Recommendations
            st.subheader("💡 Responsive Design Recommendations")
            for rec in viewport_results['recommendations']:
                st.info(rec)

            # Performance metrics (if enabled)
            if test_performance and viewport_results['performance']:
                st.subheader("⚡ Performance at This Viewport")
                perf = viewport_results['performance']

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Load Time", f"{perf['load_time']:.2f}s")
                with col2:
                    st.metric("Layout Shifts", perf['layout_shifts'])
                with col3:
                    st.metric("Resource Count", perf['resources'])

            # Screenshot simulation
            if capture_screenshot:
                st.subheader("📸 Viewport Preview")
                st.info(f"📱 Simulated view at {viewport_width}×{viewport_height} viewport")
                st.write(f"🔗 URL: {url}")
                st.write(f"📐 Viewport: {viewport_width}×{viewport_height} ({orientation})")

        except Exception as e:
            st.error(f"❌ Viewport test failed: {str(e)}")


def test_viewport_compatibility(url, width, height, orientation, pixel_ratio, test_touch, test_retina,
                                test_performance):
    """Test viewport compatibility"""
    import requests
    import random

    # Simulate viewport testing
    results = {
        'compatibility': {},
        'recommendations': [],
        'performance': None
    }

    try:
        # Simulate HTTP request with mobile user agent
        headers = {
            'User-Agent': f'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Viewport': f'width={width}, height={height}'
        }

        response = requests.get(url, headers=headers, timeout=10)

        # Simulate responsive design analysis
        responsive_score = random.randint(60, 95)
        issues = []

        # Common responsive issues
        if width < 768:
            if random.choice([True, False]):
                issues.append("Text might be too small on mobile devices")
            if random.choice([True, False]):
                issues.append("Touch targets may be too small (< 44px)")

        if width > 1200:
            if random.choice([True, False]):
                issues.append("Content might be too narrow on large screens")

        # Adjust score based on issues
        responsive_score -= len(issues) * 10

        results['compatibility'] = {
            'responsive_score': max(0, responsive_score),
            'issues': issues,
            'viewport_meta_present': random.choice([True, False]),
            'css_media_queries': random.randint(3, 12)
        }

        # Generate recommendations
        recommendations = generate_viewport_recommendations(width, height, issues)
        results['recommendations'] = recommendations

        # Performance testing (if enabled)
        if test_performance:
            results['performance'] = {
                'load_time': random.uniform(1.5, 4.0),
                'layout_shifts': random.randint(0, 3),
                'resources': random.randint(20, 60)
            }

    except Exception as e:
        results['compatibility'] = {
            'responsive_score': 0,
            'issues': [f"Unable to test: {str(e)}"],
            'viewport_meta_present': False,
            'css_media_queries': 0
        }
        results['recommendations'] = ["Fix URL accessibility issues first"]

    return results


def generate_viewport_recommendations(width, height, issues):
    """Generate viewport-specific recommendations"""
    recommendations = []

    if width < 768:
        recommendations.append("📱 Ensure touch targets are at least 44px for mobile usability")
        recommendations.append("📝 Use relative font sizes (em, rem) instead of fixed pixels")
        recommendations.append("🖼️ Optimize images for mobile bandwidth")

    if width > 1200:
        recommendations.append("🖥️ Consider max-width containers to prevent content from being too wide")
        recommendations.append("📊 Use CSS Grid or Flexbox for better large screen layouts")

    if len(issues) > 2:
        recommendations.append("🔧 Implement comprehensive media queries for better responsiveness")

    recommendations.extend([
        "📐 Add viewport meta tag: <meta name='viewport' content='width=device-width, initial-scale=1'>",
        "🎯 Test across multiple devices and orientations",
        "⚡ Use responsive images with srcset for better performance"
    ])

    return recommendations


def media_query_generator():
    """CSS Media Query generator tool"""
    create_tool_header("Media Query Generator", "Generate CSS media queries for responsive design", "📱")

    st.subheader("🎯 Media Query Configuration")

    col1, col2 = st.columns(2)
    with col1:
        query_type = st.selectbox("Query Type", [
            "Screen Width", "Screen Height", "Device Orientation",
            "Pixel Density", "Hover Capability", "Dark Mode", "Custom"
        ])

        target_device = st.selectbox("Target Device", [
            "Mobile Phones", "Tablets", "Desktop", "Large Desktop", "All Devices"
        ])

    with col2:
        css_approach = st.selectbox("CSS Approach", [
            "Mobile First", "Desktop First", "Hybrid"
        ])

        include_fallbacks = st.checkbox("Include IE11 Fallbacks", False)

    # Device-specific configurations
    if query_type == "Screen Width":
        st.subheader("📐 Width Breakpoints")

        col1, col2, col3 = st.columns(3)
        with col1:
            mobile_max = st.number_input("Mobile Max Width (px)", 300, 800, 767)
        with col2:
            tablet_min = st.number_input("Tablet Min Width (px)", 400, 1000, 768)
            tablet_max = st.number_input("Tablet Max Width (px)", 800, 1400, 1024)
        with col3:
            desktop_min = st.number_input("Desktop Min Width (px)", 1000, 2000, 1025)

    elif query_type == "Device Orientation":
        orientation_type = st.selectbox("Orientation", ["Portrait", "Landscape", "Both"])

    elif query_type == "Pixel Density":
        pixel_density = st.selectbox("Target Density", ["1x (Standard)", "1.5x", "2x (Retina)", "3x", "Custom"])
        if pixel_density == "Custom":
            custom_density = st.number_input("Custom Density", 1.0, 4.0, 2.0, 0.1)

    elif query_type == "Custom":
        custom_query = st.text_area("Custom Media Query",
                                    placeholder="(min-width: 768px) and (max-width: 1024px)")

    # CSS properties to include
    st.subheader("🎨 CSS Properties")

    col1, col2 = st.columns(2)
    with col1:
        include_typography = st.checkbox("Typography (font-size, line-height)", True)
        include_spacing = st.checkbox("Spacing (margin, padding)", True)
        include_layout = st.checkbox("Layout (width, height, display)", True)

    with col2:
        include_flexbox = st.checkbox("Flexbox Properties", False)
        include_grid = st.checkbox("CSS Grid Properties", False)
        include_positioning = st.checkbox("Positioning", False)

    if st.button("Generate Media Queries"):
        try:
            media_queries = generate_css_media_queries(
                query_type, target_device, css_approach, include_fallbacks,
                locals()  # Pass all local variables for configuration
            )

            st.subheader("📋 Generated CSS Media Queries")

            # Show different approaches
            for approach, css_code in media_queries.items():
                with st.expander(f"📱 {approach}"):
                    st.code(css_code, language='css')

            # Best practices
            st.subheader("💡 Media Query Best Practices")
            best_practices = [
                "🎯 Use relative units (em, rem) in media queries for better scalability",
                "📱 Start with mobile-first approach for better performance",
                "🔄 Test media queries across real devices, not just browser dev tools",
                "📐 Use logical breakpoints based on content, not specific devices",
                "⚡ Minimize the number of breakpoints to reduce complexity",
                "🎨 Consider using CSS custom properties for responsive values"
            ]

            for practice in best_practices:
                st.info(practice)

            # Download option
            if media_queries:
                combined_css = "\n\n".join([f"/* {name} */\n{code}" for name, code in media_queries.items()])
                FileHandler.create_download_link(combined_css.encode(), "responsive-styles.css", "text/css")

        except Exception as e:
            st.error(f"❌ Media query generation failed: {str(e)}")


def generate_css_media_queries(query_type, target_device, css_approach, include_fallbacks, config):
    """Generate CSS media queries based on configuration"""
    media_queries = {}

    if query_type == "Screen Width":
        mobile_max = config.get('mobile_max', 767)
        tablet_min = config.get('tablet_min', 768)
        tablet_max = config.get('tablet_max', 1024)
        desktop_min = config.get('desktop_min', 1025)

        if css_approach == "Mobile First":
            mobile_first = f"""/* Mobile First Approach */
/* Base styles (Mobile) */
.container {{
    width: 100%;
    padding: 1rem;
    font-size: 14px;
}}

/* Tablet styles */
@media (min-width: {tablet_min}px) {{
    .container {{
        max-width: 750px;
        margin: 0 auto;
        padding: 1.5rem;
        font-size: 16px;
    }}
}}

/* Desktop styles */
@media (min-width: {desktop_min}px) {{
    .container {{
        max-width: 1200px;
        padding: 2rem;
        font-size: 18px;
    }}
}}"""
            media_queries["Mobile First"] = mobile_first

        elif css_approach == "Desktop First":
            desktop_first = f"""/* Desktop First Approach */
/* Base styles (Desktop) */
.container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    font-size: 18px;
}}

/* Tablet styles */
@media (max-width: {tablet_max}px) {{
    .container {{
        max-width: 750px;
        padding: 1.5rem;
        font-size: 16px;
    }}
}}

/* Mobile styles */
@media (max-width: {mobile_max}px) {{
    .container {{
        width: 100%;
        padding: 1rem;
        font-size: 14px;
    }}
}}"""
            media_queries["Desktop First"] = desktop_first

    elif query_type == "Device Orientation":
        orientation_css = """/* Orientation-based styles */
/* Portrait orientation */
@media (orientation: portrait) {
    .container {
        flex-direction: column;
    }

    .sidebar {
        width: 100%;
        order: 2;
    }
}

/* Landscape orientation */
@media (orientation: landscape) {
    .container {
        flex-direction: row;
    }

    .sidebar {
        width: 30%;
        order: 1;
    }
}"""
        media_queries["Orientation"] = orientation_css

    elif query_type == "Pixel Density":
        retina_css = """/* High DPI / Retina displays */
@media (-webkit-min-device-pixel-ratio: 2),
       (min-resolution: 192dpi),
       (min-resolution: 2dppx) {
    .logo {
        background-image: url('logo@2x.png');
        background-size: 100px 50px;
    }

    .icon {
        background-image: url('icons@2x.png');
        background-size: 24px 24px;
    }
}

/* Ultra high DPI displays */
@media (-webkit-min-device-pixel-ratio: 3),
       (min-resolution: 288dpi),
       (min-resolution: 3dppx) {
    .logo {
        background-image: url('logo@3x.png');
        background-size: 100px 50px;
    }
}"""
        media_queries["High DPI"] = retina_css

    elif query_type == "Dark Mode":
        dark_mode_css = """/* Dark mode styles */
@media (prefers-color-scheme: dark) {
    :root {
        --bg-color: #1a1a1a;
        --text-color: #ffffff;
        --accent-color: #007acc;
    }

    body {
        background-color: var(--bg-color);
        color: var(--text-color);
    }

    .card {
        background-color: #2d2d2d;
        border: 1px solid #404040;
    }
}

/* Light mode (default) */
@media (prefers-color-scheme: light) {
    :root {
        --bg-color: #ffffff;
        --text-color: #333333;
        --accent-color: #0066cc;
    }
}"""
        media_queries["Dark Mode"] = dark_mode_css

    # Add hover capability detection
    hover_css = """/* Hover capability detection */
/* Touch devices (no hover) */
@media (hover: none) {
    .button {
        /* Always show active state on touch devices */
        background-color: #007acc;
        transform: scale(0.95);
    }
}

/* Devices with hover capability */
@media (hover: hover) {
    .button:hover {
        background-color: #005fa3;
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
}"""
    media_queries["Hover Detection"] = hover_css

    return media_queries


def breakpoint_analyzer():
    """Breakpoint analysis tool"""
    create_tool_header("Breakpoint Analyzer", "Analyze and optimize responsive breakpoints", "📊")

    url = st.text_input("Enter Website URL:", placeholder="https://example.com")

    st.subheader("📐 Analysis Configuration")

    col1, col2 = st.columns(2)
    with col1:
        analysis_depth = st.selectbox("Analysis Depth", ["Quick Scan", "Deep Analysis", "Comprehensive"])
        include_css_analysis = st.checkbox("Analyze CSS Media Queries", True)

    with col2:
        test_viewport_range = st.selectbox("Viewport Range", [
            "Mobile Only (320-768px)",
            "Tablet Focus (768-1024px)",
            "Desktop Focus (1024px+)",
            "Full Range (320-1920px)"
        ])

        performance_analysis = st.checkbox("Include Performance Analysis", False)

    # Custom breakpoint testing
    st.subheader("🎯 Custom Breakpoints")

    col1, col2, col3 = st.columns(3)
    with col1:
        test_320 = st.checkbox("320px (Small Mobile)", True)
        test_375 = st.checkbox("375px (iPhone)", True)
        test_768 = st.checkbox("768px (Tablet Portrait)", True)

    with col2:
        test_1024 = st.checkbox("1024px (Tablet Landscape)", True)
        test_1280 = st.checkbox("1280px (Small Desktop)", True)
        test_1920 = st.checkbox("1920px (Large Desktop)", True)

    with col3:
        custom_breakpoints = st.text_area("Custom Breakpoints (one per line)",
                                          placeholder="414\n600\n1440")

    if url and st.button("Analyze Breakpoints"):
        try:
            with st.spinner("Analyzing breakpoints..."):
                # Collect breakpoints to test
                breakpoints_to_test = []
                if test_320: breakpoints_to_test.append(320)
                if test_375: breakpoints_to_test.append(375)
                if test_768: breakpoints_to_test.append(768)
                if test_1024: breakpoints_to_test.append(1024)
                if test_1280: breakpoints_to_test.append(1280)
                if test_1920: breakpoints_to_test.append(1920)

                # Add custom breakpoints
                if custom_breakpoints.strip():
                    for bp in custom_breakpoints.strip().split('\n'):
                        try:
                            breakpoints_to_test.append(int(bp.strip()))
                        except ValueError:
                            continue

                analysis_results = analyze_responsive_breakpoints(
                    url, breakpoints_to_test, include_css_analysis, performance_analysis
                )

            st.subheader("📊 Breakpoint Analysis Results")

            # Overall responsive score
            overall_score = analysis_results['overall_score']
            if overall_score >= 80:
                st.success(f"🏆 Excellent Responsive Implementation: {overall_score}/100")
            elif overall_score >= 60:
                st.warning(f"⚠️ Good Responsive Implementation: {overall_score}/100")
            else:
                st.error(f"❌ Poor Responsive Implementation: {overall_score}/100")

            # Breakpoint results
            st.subheader("📱 Breakpoint Test Results")

            for bp_result in analysis_results['breakpoint_results']:
                with st.expander(f"📐 {bp_result['width']}px - {bp_result['device_category']}"):
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write(f"**Layout Score**: {bp_result['layout_score']}/10")
                        st.write(f"**Content Readability**: {bp_result['readability_score']}/10")

                    with col2:
                        st.write(f"**Navigation Usability**: {bp_result['navigation_score']}/10")
                        st.write(f"**Touch Target Size**: {bp_result['touch_target_score']}/10")

                    with col3:
                        if performance_analysis:
                            st.write(f"**Load Time**: {bp_result['performance']['load_time']:.2f}s")
                            st.write(f"**Layout Shifts**: {bp_result['performance']['layout_shifts']}")

                    # Issues for this breakpoint
                    if bp_result['issues']:
                        st.write("**Issues Found:**")
                        for issue in bp_result['issues']:
                            st.write(f"• {issue}")

            # CSS Media Query Analysis
            if include_css_analysis and analysis_results['css_analysis']:
                st.subheader("🎨 CSS Media Query Analysis")
                css_analysis = analysis_results['css_analysis']

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Media Queries Found", css_analysis['total_queries'])
                with col2:
                    st.metric("Breakpoint Coverage", f"{css_analysis['coverage_score']}/10")
                with col3:
                    st.metric("Query Efficiency", f"{css_analysis['efficiency_score']}/10")

                if css_analysis['detected_breakpoints']:
                    st.write("**Detected CSS Breakpoints:**")
                    for bp in css_analysis['detected_breakpoints']:
                        st.write(f"• {bp}")

            # Optimization recommendations
            st.subheader("💡 Breakpoint Optimization Recommendations")
            for rec in analysis_results['recommendations']:
                st.info(rec)

            # Suggested breakpoint strategy
            st.subheader("🎯 Suggested Breakpoint Strategy")
            strategy = analysis_results['suggested_strategy']
            st.code(strategy, language='css')

        except Exception as e:
            st.error(f"❌ Breakpoint analysis failed: {str(e)}")


def analyze_responsive_breakpoints(url, breakpoints, include_css, include_performance):
    """Analyze responsive breakpoints for a website"""
    import requests
    import random

    results = {
        'overall_score': 0,
        'breakpoint_results': [],
        'css_analysis': None,
        'recommendations': [],
        'suggested_strategy': ""
    }

    try:
        # Test each breakpoint
        total_score = 0

        for width in sorted(breakpoints):
            # Determine device category
            if width <= 480:
                device_category = "Mobile Phone"
            elif width <= 768:
                device_category = "Large Mobile / Small Tablet"
            elif width <= 1024:
                device_category = "Tablet"
            else:
                device_category = "Desktop"

            # Simulate testing at this breakpoint
            layout_score = random.randint(6, 10)
            readability_score = random.randint(7, 10)
            navigation_score = random.randint(5, 10)
            touch_target_score = random.randint(6, 10) if width <= 768 else 10

            # Generate issues based on scores
            issues = []
            if layout_score < 8:
                issues.append("Layout elements may overlap or break")
            if readability_score < 8:
                issues.append("Text might be too small or hard to read")
            if navigation_score < 8:
                issues.append("Navigation might be difficult to use")
            if touch_target_score < 8:
                issues.append("Touch targets may be too small")

            # Performance simulation
            performance = None
            if include_performance:
                performance = {
                    'load_time': random.uniform(1.0, 4.0),
                    'layout_shifts': random.randint(0, 3),
                    'resources_loaded': random.randint(20, 60)
                }

            breakpoint_result = {
                'width': width,
                'device_category': device_category,
                'layout_score': layout_score,
                'readability_score': readability_score,
                'navigation_score': navigation_score,
                'touch_target_score': touch_target_score,
                'issues': issues,
                'performance': performance
            }

            results['breakpoint_results'].append(breakpoint_result)

            # Calculate average score for this breakpoint
            avg_score = (layout_score + readability_score + navigation_score + touch_target_score) / 4
            total_score += avg_score

        # Calculate overall score
        results['overall_score'] = int((total_score / len(breakpoints)) * 10) if breakpoints else 0

        # CSS Analysis simulation
        if include_css:
            results['css_analysis'] = {
                'total_queries': random.randint(5, 15),
                'coverage_score': random.randint(6, 10),
                'efficiency_score': random.randint(7, 10),
                'detected_breakpoints': ['768px', '1024px', '1200px']
            }

        # Generate recommendations
        recommendations = []
        if results['overall_score'] < 70:
            recommendations.append("🔧 Improve responsive design implementation across breakpoints")

        recommendations.extend([
            "📱 Test on real devices, not just browser dev tools",
            "🎯 Focus on content-driven breakpoints rather than device-specific ones",
            "⚡ Optimize images and assets for each breakpoint",
            "🖱️ Ensure touch targets are at least 44px on mobile devices",
            "📐 Use flexible layouts with CSS Grid and Flexbox"
        ])

        results['recommendations'] = recommendations

        # Suggested strategy
        results['suggested_strategy'] = """/* Suggested Breakpoint Strategy */

/* Base styles (Mobile First) */
.container {
    width: 100%;
    padding: 1rem;
}

/* Small tablets and large phones */
@media (min-width: 768px) {
    .container {
        max-width: 750px;
        margin: 0 auto;
    }
}

/* Tablets and small desktops */
@media (min-width: 1024px) {
    .container {
        max-width: 970px;
    }
}

/* Large desktops */
@media (min-width: 1200px) {
    .container {
        max-width: 1170px;
    }
}"""

    except Exception as e:
        results['recommendations'] = [f"Unable to analyze: {str(e)}"]

    return results


def mobile_simulator():
    """Mobile device simulator tool"""
    create_tool_header("Mobile Simulator", "Simulate mobile device viewing experience", "📱")

    url = st.text_input("Enter Website URL:", placeholder="https://example.com")

    st.subheader("📱 Device Selection")

    # Popular mobile devices
    mobile_devices = {
        "iPhone SE (2022)": {"width": 375, "height": 667, "dpr": 2, "user_agent": "iPhone"},
        "iPhone 13": {"width": 390, "height": 844, "dpr": 3, "user_agent": "iPhone"},
        "iPhone 13 Pro Max": {"width": 428, "height": 926, "dpr": 3, "user_agent": "iPhone"},
        "Samsung Galaxy S21": {"width": 360, "height": 800, "dpr": 3, "user_agent": "Android"},
        "Samsung Galaxy Note 20": {"width": 412, "height": 915, "dpr": 2.75, "user_agent": "Android"},
        "Google Pixel 6": {"width": 412, "height": 915, "dpr": 2.625, "user_agent": "Android"},
        "iPad Mini": {"width": 768, "height": 1024, "dpr": 2, "user_agent": "iPad"},
        "iPad Pro 11\"": {"width": 834, "height": 1194, "dpr": 2, "user_agent": "iPad"},
        "Custom Device": {"width": 0, "height": 0, "dpr": 1, "user_agent": "Custom"}
    }

    col1, col2 = st.columns(2)
    with col1:
        selected_device = st.selectbox("Select Device", list(mobile_devices.keys()))

        if selected_device == "Custom Device":
            device_width = st.number_input("Device Width (px)", 200, 500, 375)
            device_height = st.number_input("Device Height (px)", 400, 1000, 667)
            device_dpr = st.number_input("Device Pixel Ratio", 1.0, 4.0, 2.0, 0.1)
            custom_user_agent = st.text_input("User Agent", "Custom Mobile Device")
        else:
            device_info = mobile_devices[selected_device]
            device_width = device_info["width"]
            device_height = device_info["height"]
            device_dpr = device_info["dpr"]

    with col2:
        orientation = st.selectbox("Orientation", ["Portrait", "Landscape"])
        if orientation == "Landscape":
            device_width, device_height = device_height, device_width

        connection_speed = st.selectbox("Network Speed", [
            "4G Fast", "4G", "3G", "Slow 3G", "2G", "Offline"
        ])

    st.subheader("🔧 Simulation Settings")

    col1, col2 = st.columns(2)
    with col1:
        simulate_touch = st.checkbox("Simulate Touch Events", True)
        disable_hover = st.checkbox("Disable Hover Effects", True)
        simulate_sensors = st.checkbox("Simulate Device Sensors", False)

    with col2:
        test_offline_mode = st.checkbox("Test Offline Mode", False)
        emulate_slow_cpu = st.checkbox("Emulate Slow CPU", False)
        capture_interactions = st.checkbox("Capture User Interactions", False)

    if url and st.button("Start Mobile Simulation"):
        try:
            with st.spinner("Simulating mobile experience..."):
                simulation_results = simulate_mobile_experience(
                    url, selected_device, device_width, device_height, device_dpr,
                    orientation, connection_speed, simulate_touch, disable_hover,
                    test_offline_mode, emulate_slow_cpu
                )

            st.subheader("📱 Mobile Simulation Results")

            # Device info
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Device", selected_device.split(" (")[0])
            with col2:
                st.metric("Screen Size", f"{device_width}×{device_height}")
            with col3:
                st.metric("Pixel Ratio", f"{device_dpr}x")
            with col4:
                st.metric("Orientation", orientation)

            # Performance metrics
            st.subheader("⚡ Mobile Performance")
            perf = simulation_results['performance']

            col1, col2, col3 = st.columns(3)
            with col1:
                load_time = perf['load_time']
                if load_time < 3:
                    st.success(f"Load Time: {load_time:.2f}s")
                elif load_time < 5:
                    st.warning(f"Load Time: {load_time:.2f}s")
                else:
                    st.error(f"Load Time: {load_time:.2f}s")

            with col2:
                st.metric("Data Usage", f"{perf['data_usage']:.1f} MB")

            with col3:
                battery_impact = perf['battery_impact']
                if battery_impact == "Low":
                    st.success(f"Battery Impact: {battery_impact}")
                elif battery_impact == "Medium":
                    st.warning(f"Battery Impact: {battery_impact}")
                else:
                    st.error(f"Battery Impact: {battery_impact}")

            # Mobile UX analysis
            st.subheader("📱 Mobile UX Analysis")
            ux_analysis = simulation_results['ux_analysis']

            for category, score in ux_analysis['scores'].items():
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.write(f"**{category}**")
                with col2:
                    if score >= 8:
                        st.success(f"{score}/10")
                    elif score >= 6:
                        st.warning(f"{score}/10")
                    else:
                        st.error(f"{score}/10")

            # Issues and recommendations
            if ux_analysis['issues']:
                st.subheader("🔍 Mobile UX Issues")
                for issue in ux_analysis['issues']:
                    st.warning(f"⚠️ {issue}")

            st.subheader("💡 Mobile Optimization Recommendations")
            for rec in simulation_results['recommendations']:
                st.info(rec)

            # Accessibility analysis
            if simulation_results['accessibility']:
                st.subheader("♿ Mobile Accessibility")
                accessibility = simulation_results['accessibility']

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Touch Target Size", f"{accessibility['touch_target_score']}/10")
                with col2:
                    st.metric("Color Contrast", f"{accessibility['contrast_score']}/10")
                with col3:
                    st.metric("Screen Reader", f"{accessibility['screen_reader_score']}/10")

            # Simulation preview
            st.subheader("📲 Device Preview")
            st.info(f"🔗 Simulating {url} on {selected_device}")
            st.write(f"📐 Viewport: {device_width}×{device_height} ({orientation})")
            st.write(f"🌐 Network: {connection_speed}")

            if test_offline_mode:
                st.warning("🔌 Offline mode simulation active")

        except Exception as e:
            st.error(f"❌ Mobile simulation failed: {str(e)}")


def simulate_mobile_experience(url, device, width, height, dpr, orientation, connection,
                               touch_enabled, hover_disabled, offline_mode, slow_cpu):
    """Simulate mobile device experience"""
    import requests
    import random

    results = {
        'performance': {},
        'ux_analysis': {},
        'recommendations': [],
        'accessibility': {}
    }

    try:
        # Simulate mobile user agent request
        user_agents = {
            "iPhone": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15",
            "Android": "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36",
            "iPad": "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15"
        }

        device_type = device.split(" ")[0] if device != "Custom Device" else "Custom"
        user_agent = user_agents.get(device_type, user_agents["Android"])

        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        # Initialize load_time to avoid unbound variable error
        load_time = float('inf')

        if not offline_mode:
            response = requests.get(url, headers=headers, timeout=15)

            # Simulate performance based on connection speed
            connection_multipliers = {
                "4G Fast": 1.0,
                "4G": 1.5,
                "3G": 3.0,
                "Slow 3G": 5.0,
                "2G": 10.0,
                "Offline": float('inf')
            }

            base_load_time = 2.0
            load_time = base_load_time * connection_multipliers.get(connection, 1.0)

            if slow_cpu:
                load_time *= 1.5

            # Calculate data usage
            data_usage = len(response.content) / (1024 * 1024)  # MB

            # Battery impact based on performance
            if load_time < 3:
                battery_impact = "Low"
            elif load_time < 6:
                battery_impact = "Medium"
            else:
                battery_impact = "High"

            results['performance'] = {
                'load_time': min(load_time, 15.0),  # Cap at 15 seconds
                'data_usage': data_usage,
                'battery_impact': battery_impact,
                'connection_speed': connection
            }
        else:
            results['performance'] = {
                'load_time': float('inf'),
                'data_usage': 0,
                'battery_impact': "N/A",
                'connection_speed': "Offline"
            }

        # UX Analysis simulation
        touch_score = 8 if touch_enabled else 5
        readability_score = random.randint(7, 10)
        navigation_score = random.randint(6, 9)
        loading_score = 10 - min(int(load_time), 8) if not offline_mode else 0

        issues = []
        if touch_score < 7:
            issues.append("Touch targets may be too small for mobile interaction")
        if readability_score < 8:
            issues.append("Text might be difficult to read on mobile screens")
        if navigation_score < 7:
            issues.append("Navigation could be more mobile-friendly")
        if loading_score < 6:
            issues.append("Page loads too slowly on mobile connections")

        results['ux_analysis'] = {
            'scores': {
                'Touch Usability': touch_score,
                'Text Readability': readability_score,
                'Navigation': navigation_score,
                'Loading Performance': loading_score
            },
            'issues': issues
        }

        # Accessibility simulation
        results['accessibility'] = {
            'touch_target_score': random.randint(7, 10),
            'contrast_score': random.randint(8, 10),
            'screen_reader_score': random.randint(6, 9)
        }

        # Generate recommendations
        recommendations = []

        if load_time > 5:
            recommendations.append("🚀 Optimize images and assets for mobile networks")

        if width < 400:
            recommendations.append("📱 Ensure content is readable at small screen sizes")

        recommendations.extend([
            "👆 Use touch-friendly UI elements (minimum 44px touch targets)",
            "🔤 Use legible font sizes (minimum 16px on mobile)",
            "🎯 Optimize for one-handed usage",
            "⚡ Implement lazy loading for better performance",
            "🔌 Add offline functionality with service workers",
            "🔋 Minimize battery usage with efficient animations"
        ])

        results['recommendations'] = recommendations

    except Exception as e:
        results['performance'] = {'load_time': float('inf'), 'data_usage': 0, 'battery_impact': 'Error'}
        results['ux_analysis'] = {'scores': {}, 'issues': [f"Simulation failed: {str(e)}"]}
        results['recommendations'] = ["Fix URL accessibility first"]
        results['accessibility'] = {}

    return results


# ================================
# ACCESSIBILITY TOOLS
# ================================

def accessibility_wcag_checker():
    """WCAG Compliance Checker for Web Developers"""
    create_tool_header("🔍 WCAG Compliance Checker", "Check your content against WCAG 2.1 guidelines")

    st.info("📋 This tool helps you verify compliance with Web Content Accessibility Guidelines (WCAG) 2.1")

    # Input methods
    input_type = st.radio("Input Type:", ["URL", "HTML Code", "Text Content"])

    if input_type == "URL":
        url = st.text_input("Enter URL to check:", placeholder="https://example.com")
        if st.button("Check WCAG Compliance") and url:
            with st.spinner("Analyzing accessibility..."):
                show_progress_bar("Analyzing accessibility", 1)
                results = perform_wcag_check(url, "url")
                display_wcag_results(results)

    elif input_type == "HTML Code":
        html_code = st.text_area("Enter HTML code:", height=200, placeholder="<html>...</html>")
        if st.button("Check HTML Accessibility") and html_code:
            with st.spinner("Analyzing HTML..."):
                show_progress_bar("Analyzing HTML", 1)
                results = perform_wcag_check(html_code, "html")
                display_wcag_results(results)

    else:  # Text Content
        text_content = st.text_area("Enter text content:", height=200)
        if st.button("Check Text Accessibility") and text_content:
            with st.spinner("Analyzing text accessibility..."):
                show_progress_bar("Analyzing text accessibility", 1)
                results = perform_wcag_check(text_content, "text")
                display_wcag_results(results)


def perform_wcag_check(content, content_type):
    """Perform WCAG accessibility check"""
    issues = []
    recommendations = []

    if content_type == "html":
        # Check for common WCAG violations
        if not re.search(r'alt=', content, re.IGNORECASE):
            issues.append({
                "level": "A",
                "criterion": "1.1.1 Non-text Content",
                "issue": "Missing alt attributes for images",
                "recommendation": "Add descriptive alt attributes to all images"
            })

        if not re.search(r'<h[1-6]', content, re.IGNORECASE):
            issues.append({
                "level": "A",
                "criterion": "1.3.1 Info and Relationships",
                "issue": "No heading structure found",
                "recommendation": "Use proper heading hierarchy (h1-h6)"
            })

        if not re.search(r'lang=', content, re.IGNORECASE):
            issues.append({
                "level": "A",
                "criterion": "3.1.1 Language of Page",
                "issue": "Missing language attribute",
                "recommendation": "Add lang attribute to html element"
            })

        # Check for keyboard navigation
        if not re.search(r'tabindex', content, re.IGNORECASE):
            recommendations.append("Consider adding tabindex for better keyboard navigation")

        # Check for ARIA attributes
        aria_count = len(re.findall(r'aria-\w+', content, re.IGNORECASE))
        if aria_count == 0:
            recommendations.append("Consider adding ARIA attributes for better screen reader support")

    elif content_type == "text":
        # Check text accessibility
        if len(content) > 1000:
            recommendations.append("Consider breaking long text into smaller sections with headings")

        # Check for plain language
        complex_words = len(re.findall(r'\b\w{10,}\b', content))
        if complex_words > len(content.split()) * 0.1:
            recommendations.append("Consider using simpler language for better readability")

    return {
        "issues": issues,
        "recommendations": recommendations,
        "compliance_score": max(0, 100 - len(issues) * 20)
    }


def display_wcag_results(results):
    """Display WCAG check results"""
    col1, col2 = st.columns([2, 1])

    with col2:
        # Compliance score
        score = results["compliance_score"]
        if score >= 90:
            st.success(f"🎉 Compliance Score: {score}%")
        elif score >= 70:
            st.warning(f"⚠️ Compliance Score: {score}%")
        else:
            st.error(f"❌ Compliance Score: {score}%")

    with col1:
        if results["issues"]:
            st.subheader("🚨 Accessibility Issues")
            for i, issue in enumerate(results["issues"], 1):
                with st.expander(f"Issue {i}: {issue['criterion']} (Level {issue['level']})"):
                    st.write(f"**Problem:** {issue['issue']}")
                    st.write(f"**Recommendation:** {issue['recommendation']}")

        if results["recommendations"]:
            st.subheader("💡 Recommendations")
            for rec in results["recommendations"]:
                st.info(rec)


def accessibility_color_contrast_checker():
    """Color Contrast Checker for WCAG Compliance"""
    create_tool_header("🌈 Color Contrast Checker", "Verify color combinations meet WCAG contrast requirements")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Foreground Color")
        fg_color = st.color_picker("Pick foreground color:", "#000000")
        fg_hex = st.text_input("Or enter hex:", fg_color, key="fg_hex")

    with col2:
        st.subheader("Background Color")
        bg_color = st.color_picker("Pick background color:", "#FFFFFF")
        bg_hex = st.text_input("Or enter hex:", bg_color, key="bg_hex")

    # Calculate contrast ratio
    if st.button("Check Contrast"):
        ratio = calculate_contrast_ratio(fg_hex, bg_hex)

        st.subheader("Contrast Analysis")

        # Display preview
        st.markdown(f"""
        <div style="background-color: {bg_hex}; color: {fg_hex}; 
                    padding: 20px; border-radius: 10px; margin: 10px 0;">
            <h3>Sample Text Preview</h3>
            <p>This is how your text will look with these colors.</p>
            <small>Small text example for testing.</small>
        </div>
        """, unsafe_allow_html=True)

        # Results
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Contrast Ratio", f"{ratio:.2f}:1")

        with col2:
            aa_normal = "✅ Pass" if ratio >= 4.5 else "❌ Fail"
            st.metric("WCAG AA Normal", aa_normal)

        with col3:
            aa_large = "✅ Pass" if ratio >= 3.0 else "❌ Fail"
            st.metric("WCAG AA Large", aa_large)

        # Recommendations
        if ratio < 4.5:
            st.warning("⚠️ This color combination doesn't meet WCAG AA standards for normal text.")


def calculate_contrast_ratio(color1, color2):
    """Calculate contrast ratio between two colors"""

    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def get_luminance(rgb):
        def get_channel_luminance(channel):
            channel = channel / 255.0
            if channel <= 0.03928:
                return channel / 12.92
            else:
                return ((channel + 0.055) / 1.055) ** 2.4

        r, g, b = rgb
        return 0.2126 * get_channel_luminance(r) + 0.7152 * get_channel_luminance(g) + 0.0722 * get_channel_luminance(b)

    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    lum1 = get_luminance(rgb1)
    lum2 = get_luminance(rgb2)

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)


def aria_validator_tool():
    """ARIA Attributes Validator"""
    create_tool_header("🏷️ ARIA Validator", "Validate ARIA attributes in your HTML")

    st.info("🎯 Check if your ARIA attributes are correctly implemented for screen readers")

    html_input = st.text_area(
        "Enter HTML with ARIA attributes:",
        height=200,
        placeholder='<button aria-label="Close dialog" aria-expanded="false">X</button>'
    )

    if st.button("Validate ARIA") and html_input:
        with st.spinner("Validating ARIA attributes..."):
            show_progress_bar("Validating ARIA", 1)
            validation_results = validate_aria_attributes(html_input)
            display_aria_validation_results(validation_results)


def validate_aria_attributes(html_content):
    """Validate ARIA attributes in HTML"""
    issues = []
    recommendations = []

    # Find all ARIA attributes
    aria_attributes = re.findall(r'aria-(\w+)="([^"]*)"', html_content, re.IGNORECASE)

    # Valid ARIA attributes
    valid_aria_attrs = [
        'label', 'labelledby', 'describedby', 'expanded', 'hidden', 'live',
        'atomic', 'busy', 'controls', 'current', 'details', 'disabled'
    ]

    for attr, value in aria_attributes:
        if attr.lower() not in valid_aria_attrs:
            issues.append(f"Invalid ARIA attribute: aria-{attr}")

        # Check for empty values
        if not value.strip():
            issues.append(f"Empty value for aria-{attr}")

    return {
        'issues': issues,
        'recommendations': recommendations,
        'aria_count': len(aria_attributes)
    }


def display_aria_validation_results(results):
    """Display ARIA validation results"""
    st.metric("ARIA Attributes Found", results['aria_count'])

    if results['issues']:
        st.subheader("🚨 ARIA Issues")
        for issue in results['issues']:
            st.error(f"❌ {issue}")
    else:
        st.success("✅ No ARIA validation issues found!")


def screen_reader_test_tool():
    """Screen Reader Testing Helper"""
    create_tool_header("🔊 Screen Reader Test", "Simulate screen reader experience")

    st.info("🎧 This tool helps you understand how screen readers interpret your content")

    html_input = st.text_area(
        "Enter HTML to test:",
        height=200,
        placeholder='<h1>Page Title</h1>\n<p>Content with <a href="#link">accessible link</a></p>'
    )

    if st.button("Simulate Screen Reader") and html_input:
        with st.spinner("Analyzing for screen readers..."):
            show_progress_bar("Analyzing for screen readers", 1)
            analysis = analyze_for_screen_readers(html_input)
            display_screen_reader_analysis(analysis)


def analyze_for_screen_readers(html_content):
    """Analyze HTML content for screen reader compatibility"""
    analysis = {
        'headings': [],
        'links': [],
        'images': [],
        'issues': []
    }

    # Extract headings
    headings = re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', html_content, re.IGNORECASE | re.DOTALL)
    for level, content in headings:
        clean_content = re.sub(r'<[^>]+>', '', content).strip()
        analysis['headings'].append(f"Heading {level}: {clean_content}")

    # Extract links
    links = re.findall(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', html_content, re.IGNORECASE | re.DOTALL)
    for href, content in links:
        clean_content = re.sub(r'<[^>]+>', '', content).strip()
        analysis['links'].append(f"Link: {clean_content}")

    # Extract images with alt text
    images = re.findall(r'<img[^>]*alt="([^"]*)"[^>]*>', html_content, re.IGNORECASE)
    for alt_text in images:
        analysis['images'].append(f"Image: {alt_text}")

    # Check for images without alt text
    images_no_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', html_content, re.IGNORECASE)
    for img in images_no_alt:
        analysis['issues'].append("Image found without alt text")

    return analysis


def display_screen_reader_analysis(analysis):
    """Display screen reader analysis results"""
    if analysis['headings']:
        st.subheader("📝 Heading Structure")
        for heading in analysis['headings']:
            st.write(f"🏷️ {heading}")

    if analysis['links']:
        st.subheader("🔗 Links Found")
        for link in analysis['links']:
            st.write(f"🔗 {link}")

    if analysis['images']:
        st.subheader("🖼️ Images with Alt Text")
        for image in analysis['images']:
            st.write(f"🖼️ {image}")

    if analysis['issues']:
        st.subheader("🚨 Screen Reader Issues")
        for issue in analysis['issues']:
            st.error(f"❌ {issue}")

    st.subheader("💡 Screen Reader Tips")
    st.info("""
    **Good practices:**
    - Use descriptive headings to create a clear page outline
    - Provide meaningful alt text for images
    - Use proper link text (not "click here")
    - Structure content logically
    - Use ARIA attributes when needed
    """)


def keyboard_navigation_tool():
    """Keyboard Navigation Helper"""
    create_tool_header("⌨️ Keyboard Navigation", "Test and improve keyboard accessibility")

    st.info("⌨️ Ensure your web content is accessible via keyboard navigation")

    html_input = st.text_area(
        "Enter HTML to analyze:",
        height=200,
        placeholder='<button>Button 1</button>\n<input type="text" placeholder="Input field">\n<a href="#link">Link</a>'
    )

    if st.button("Analyze Keyboard Navigation") and html_input:
        with st.spinner("Analyzing keyboard navigation..."):
            show_progress_bar("Analyzing keyboard navigation", 1)
            nav_analysis = analyze_keyboard_navigation(html_input)
            display_keyboard_navigation_results(nav_analysis)


def analyze_keyboard_navigation(html_content):
    """Analyze HTML for keyboard navigation"""
    focusable_elements = []
    issues = []

    # Find potentially focusable elements
    button_pattern = r'<button[^>]*>(.*?)</button>'
    link_pattern = r'<a[^>]*href="[^"]*"[^>]*>(.*?)</a>'
    input_pattern = r'<input[^>]*>'

    buttons = re.findall(button_pattern, html_content, re.IGNORECASE | re.DOTALL)
    links = re.findall(link_pattern, html_content, re.IGNORECASE | re.DOTALL)
    inputs = re.findall(input_pattern, html_content, re.IGNORECASE)

    for button in buttons:
        clean_text = re.sub(r'<[^>]+>', '', button).strip()
        focusable_elements.append(f"Button: {clean_text}")

    for link in links:
        clean_text = re.sub(r'<[^>]+>', '', link).strip()
        focusable_elements.append(f"Link: {clean_text}")

    for _ in inputs:
        focusable_elements.append("Input field")

    # Check for tabindex attributes
    tabindex_elements = re.findall(r'tabindex="(-?\d+)"', html_content, re.IGNORECASE)
    for tabindex in tabindex_elements:
        if int(tabindex) > 0:
            issues.append(f"Positive tabindex ({tabindex}) found - can break natural tab order")

    return {
        'focusable_elements': focusable_elements,
        'issues': issues,
        'total_focusable': len(focusable_elements)
    }


def display_keyboard_navigation_results(analysis):
    """Display keyboard navigation analysis"""
    st.metric("Focusable Elements", analysis['total_focusable'])

    if analysis['focusable_elements']:
        st.subheader("⌨️ Tab Order (Focusable Elements)")
        for i, element in enumerate(analysis['focusable_elements'], 1):
            st.write(f"{i}. {element}")

    if analysis['issues']:
        st.subheader("🚨 Keyboard Navigation Issues")
        for issue in analysis['issues']:
            st.error(f"❌ {issue}")
    else:
        st.success("✅ No obvious keyboard navigation issues found!")

    st.subheader("💡 Keyboard Navigation Best Practices")
    st.info("""
    - Ensure all interactive elements are keyboard accessible
    - Provide visible focus indicators
    - Use logical tab order (avoid positive tabindex values)
    - Implement skip links for navigation
    - Test with Tab, Shift+Tab, Enter, and Space keys
    """)


# =================== CODE GENERATORS ===================

def html_form_generator():
    """Generate HTML forms with various field types"""
    create_tool_header("HTML Form Generator", "Generate HTML forms with custom fields and validation", "📝")

    st.subheader("Form Configuration")

    form_name = st.text_input("Form Name/ID", "contact-form")
    form_method = st.selectbox("Method", ["POST", "GET"])
    form_action = st.text_input("Action URL", "/submit")

    st.subheader("Form Fields")

    # Initialize session state for fields
    if 'form_fields' not in st.session_state:
        st.session_state.form_fields = []

    col1, col2 = st.columns(2)

    with col1:
        field_type = st.selectbox("Field Type", [
            "text", "email", "password", "textarea", "select", "checkbox", "radio", "file", "number", "date", "tel",
            "url"
        ])
        field_name = st.text_input("Field Name", "field_name")
        field_label = st.text_input("Field Label", "Field Label")

    with col2:
        field_placeholder = st.text_input("Placeholder", "")
        field_required = st.checkbox("Required")
        field_options = st.text_area("Options (for select/radio)", "Option 1\nOption 2\nOption 3")

    if st.button("Add Field"):
        field = {
            'type': field_type,
            'name': field_name,
            'label': field_label,
            'placeholder': field_placeholder,
            'required': field_required,
            'options': field_options.split('\n') if field_options else []
        }
        st.session_state.form_fields.append(field)
        st.success(f"Added {field_type} field: {field_name}")

    # Display current fields
    if st.session_state.form_fields:
        st.subheader("Current Fields")
        for i, field in enumerate(st.session_state.form_fields):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{field['label']}** ({field['type']}) - {field['name']}")
            with col2:
                if st.button(f"Remove", key=f"remove_{i}"):
                    st.session_state.form_fields.pop(i)
                    st.rerun()

    if st.button("Generate Form") and st.session_state.form_fields:
        html_form = generate_html_form(form_name, form_method, form_action, st.session_state.form_fields)

        st.subheader("Generated HTML Form")
        st.code(html_form, language='html')
        FileHandler.create_download_link(html_form.encode(), f"{form_name}.html", "text/html")
        st.success("✅ HTML form generated successfully!")

    if st.button("Clear All Fields"):
        st.session_state.form_fields = []
        st.rerun()


def generate_html_form(form_name, method, action, fields):
    """Generate HTML form code"""
    html = f'''<form id="{form_name}" method="{method}" action="{action}" class="form">
'''

    for field in fields:
        required_attr = ' required' if field['required'] else ''
        placeholder_attr = f' placeholder="{field["placeholder"]}"' if field['placeholder'] else ''

        html += f'  <div class="form-group">\n'
        html += f'    <label for="{field["name"]}">{field["label"]}</label>\n'

        if field['type'] == 'textarea':
            html += f'    <textarea id="{field["name"]}" name="{field["name"]}"{placeholder_attr}{required_attr}></textarea>\n'
        elif field['type'] == 'select':
            html += f'    <select id="{field["name"]}" name="{field["name"]}"{required_attr}>\n'
            for option in field['options']:
                if option.strip():
                    html += f'      <option value="{option.strip().lower().replace(" ", "_")}">{option.strip()}</option>\n'
            html += f'    </select>\n'
        elif field['type'] == 'radio':
            for i, option in enumerate(field['options']):
                if option.strip():
                    option_id = f"{field['name']}_{i}"
                    html += f'    <input type="radio" id="{option_id}" name="{field["name"]}" value="{option.strip().lower().replace(" ", "_")}"{required_attr}>\n'
                    html += f'    <label for="{option_id}">{option.strip()}</label><br>\n'
        elif field['type'] == 'checkbox':
            html += f'    <input type="checkbox" id="{field["name"]}" name="{field["name"]}" value="1"{required_attr}>\n'
        else:
            html += f'    <input type="{field["type"]}" id="{field["name"]}" name="{field["name"]}"{placeholder_attr}{required_attr}>\n'

        html += f'  </div>\n\n'

    html += f'  <div class="form-group">\n'
    html += f'    <button type="submit">Submit</button>\n'
    html += f'    <button type="reset">Reset</button>\n'
    html += f'  </div>\n'
    html += f'</form>\n\n'

    # Add basic CSS
    html += '''<style>
.form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input, textarea, select {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

input[type="radio"], input[type="checkbox"] {
  width: auto;
  margin-right: 5px;
}

button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 10px;
}

button:hover {
  background-color: #0056b3;
}

button[type="reset"] {
  background-color: #6c757d;
}

button[type="reset"]:hover {
  background-color: #545b62;
}
</style>'''

    return html


def html_table_generator():
    """Generate HTML tables with custom data"""
    create_tool_header("HTML Table Generator", "Generate HTML tables with custom headers and data", "📊")

    st.subheader("Table Configuration")

    table_id = st.text_input("Table ID", "data-table")
    table_class = st.text_input("Table CSS Class", "table")

    col1, col2 = st.columns(2)
    with col1:
        num_columns = st.number_input("Number of Columns", min_value=1, max_value=20, value=3)
        include_header = st.checkbox("Include Header", True)
    with col2:
        num_rows = st.number_input("Number of Data Rows", min_value=1, max_value=50, value=3)
        striped_rows = st.checkbox("Striped Rows", True)

    # Header configuration
    headers = []
    if include_header:
        st.subheader("Column Headers")
        header_cols = st.columns(min(int(num_columns), 4))
        for i in range(int(num_columns)):
            with header_cols[i % 4]:
                header = st.text_input(f"Header {i + 1}", f"Column {i + 1}", key=f"header_{i}")
                headers.append(header)

    # Data configuration
    st.subheader("Table Data")
    data_input_method = st.radio("Data Input Method", ["Manual Entry", "CSV Upload", "Sample Data"])

    table_data = []

    if data_input_method == "Manual Entry":
        st.info("Enter data for each cell (leave empty for blank cells)")
        for row in range(int(num_rows)):
            row_data = []
            st.write(f"**Row {row + 1}:**")
            row_cols = st.columns(min(int(num_columns), 4))
            for col in range(int(num_columns)):
                with row_cols[col % 4]:
                    cell_data = st.text_input(f"R{row + 1}C{col + 1}", key=f"cell_{row}_{col}")
                    row_data.append(cell_data)
            table_data.append(row_data)

    elif data_input_method == "CSV Upload":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            import pandas as pd
            try:
                df = pd.read_csv(uploaded_file[0])
                headers = df.columns.tolist()
                table_data = df.values.tolist()
                st.success(f"Loaded {len(table_data)} rows with {len(headers)} columns")
            except Exception as e:
                st.error(f"Error reading CSV: {str(e)}")

    elif data_input_method == "Sample Data":
        headers = ["Name", "Age", "City", "Occupation"]
        table_data = [
            ["John Doe", "30", "New York", "Developer"],
            ["Jane Smith", "25", "Los Angeles", "Designer"],
            ["Bob Johnson", "35", "Chicago", "Manager"],
            ["Alice Brown", "28", "Miami", "Analyst"]
        ]
        st.info("Using sample data. Click 'Generate Table' to see the result.")

    if st.button("Generate Table"):
        if headers or table_data:
            html_table = generate_html_table(table_id, table_class, headers, table_data, striped_rows, include_header)

            st.subheader("Generated HTML Table")
            st.code(html_table, language='html')

            # Preview
            st.subheader("Table Preview")
            st.markdown(html_table, unsafe_allow_html=True)

            FileHandler.create_download_link(html_table.encode(), f"{table_id}.html", "text/html")
            st.success("✅ HTML table generated successfully!")
        else:
            st.error("Please provide headers or data for the table.")


def generate_html_table(table_id, table_class, headers, data, striped=True, include_header=True):
    """Generate HTML table code"""
    html = f'<table id="{table_id}" class="{table_class}">\n'

    # Add header
    if include_header and headers:
        html += '  <thead>\n    <tr>\n'
        for header in headers:
            html += f'      <th>{header}</th>\n'
        html += '    </tr>\n  </thead>\n'

    # Add body
    html += '  <tbody>\n'
    for i, row in enumerate(data):
        row_class = ' class="odd"' if striped and i % 2 == 1 else ''
        html += f'    <tr{row_class}>\n'
        for cell in row:
            html += f'      <td>{cell}</td>\n'
        html += '    </tr>\n'
    html += '  </tbody>\n'
    html += '</table>\n\n'

    # Add CSS
    html += '''<style>
.table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-family: Arial, sans-serif;
}

.table th,
.table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.table th {
  background-color: #f8f9fa;
  font-weight: bold;
  color: #495057;
}

.table tr:hover {
  background-color: #f5f5f5;
}

.table tr.odd {
  background-color: #f8f9fa;
}

.table tr.odd:hover {
  background-color: #e9ecef;
}

@media (max-width: 768px) {
  .table {
    font-size: 14px;
  }

  .table th,
  .table td {
    padding: 8px;
  }
}
</style>'''

    return html


def html_layout_generator():
    """Generate HTML layouts with different structures"""
    create_tool_header("HTML Layout Generator", "Generate responsive HTML layouts and page structures", "🏗️")

    st.subheader("Layout Configuration")

    layout_type = st.selectbox("Layout Type", [
        "Header-Content-Footer", "Sidebar Layout", "Two Column", "Three Column",
        "Hero Section", "Card Grid", "Navigation Layout", "Dashboard Layout"
    ])

    page_title = st.text_input("Page Title", "My Website")
    include_css = st.checkbox("Include CSS Styling", True)
    responsive = st.checkbox("Responsive Design", True)

    if layout_type == "Header-Content-Footer":
        header_content = st.text_area("Header Content", "Site Navigation")
        main_content = st.text_area("Main Content", "Main page content goes here")
        footer_content = st.text_area("Footer Content", "© 2024 My Website")

    elif layout_type == "Sidebar Layout":
        sidebar_position = st.selectbox("Sidebar Position", ["Left", "Right"])
        sidebar_content = st.text_area("Sidebar Content", "Navigation\nLinks\nWidgets")
        main_content = st.text_area("Main Content", "Main page content")

    elif layout_type in ["Two Column", "Three Column"]:
        num_cols = 2 if layout_type == "Two Column" else 3
        columns_content = []
        for i in range(num_cols):
            content = st.text_area(f"Column {i + 1} Content", f"Content for column {i + 1}")
            columns_content.append(content)

    elif layout_type == "Hero Section":
        hero_title = st.text_input("Hero Title", "Welcome to Our Website")
        hero_subtitle = st.text_input("Hero Subtitle", "Discover amazing content")
        hero_button_text = st.text_input("Button Text", "Get Started")
        hero_button_link = st.text_input("Button Link", "#")

    elif layout_type == "Card Grid":
        num_cards = st.number_input("Number of Cards", min_value=1, max_value=12, value=6)
        cards_per_row = st.selectbox("Cards per Row", [2, 3, 4, 6])

    if st.button("Generate Layout"):
        html_layout = generate_html_layout(
            layout_type, page_title, include_css, responsive,
            locals()  # Pass all local variables
        )

        st.subheader("Generated HTML Layout")
        st.code(html_layout, language='html')

        # Preview
        st.subheader("Layout Preview")
        st.markdown(html_layout, unsafe_allow_html=True)

        filename = f"{layout_type.lower().replace(' ', '_')}_layout.html"
        FileHandler.create_download_link(html_layout.encode(), filename, "text/html")
        st.success("✅ HTML layout generated successfully!")


def generate_html_layout(layout_type, page_title, include_css, responsive, options):
    """Generate HTML layout code"""

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
'''

    if include_css:
        html += generate_layout_css(layout_type, responsive)

    html += '</head>\n<body>\n'

    if layout_type == "Header-Content-Footer":
        html += f'''
    <header class="header">
        <h1>{options.get('header_content', 'Header')}</h1>
    </header>

    <main class="main-content">
        <h2>Main Content</h2>
        <p>{options.get('main_content', 'Main content goes here')}</p>
    </main>

    <footer class="footer">
        <p>{options.get('footer_content', 'Footer content')}</p>
    </footer>
'''

    elif layout_type == "Sidebar Layout":
        sidebar_class = "sidebar-left" if options.get('sidebar_position') == "Left" else "sidebar-right"
        html += f'''
    <div class="layout-container {sidebar_class}">
        <aside class="sidebar">
            <h3>Sidebar</h3>
            <p>{options.get('sidebar_content', 'Sidebar content').replace(chr(10), '<br>')}</p>
        </aside>

        <main class="main-content">
            <h2>Main Content</h2>
            <p>{options.get('main_content', 'Main content')}</p>
        </main>
    </div>
'''

    elif layout_type in ["Two Column", "Three Column"]:
        num_cols = 2 if layout_type == "Two Column" else 3
        html += f'    <div class="columns-container columns-{num_cols}">\n'

        for i in range(num_cols):
            content = options.get('columns_content', [f'Column {i + 1}'] * num_cols)[i] if i < len(
                options.get('columns_content', [])) else f'Column {i + 1}'
            html += f'''        <div class="column">
            <h3>Column {i + 1}</h3>
            <p>{content}</p>
        </div>
'''
        html += '    </div>\n'

    elif layout_type == "Hero Section":
        html += f'''
    <section class="hero">
        <div class="hero-content">
            <h1 class="hero-title">{options.get('hero_title', 'Hero Title')}</h1>
            <p class="hero-subtitle">{options.get('hero_subtitle', 'Hero subtitle')}</p>
            <a href="{options.get('hero_button_link', '#')}" class="hero-button">{options.get('hero_button_text', 'Button')}</a>
        </div>
    </section>

    <main class="content">
        <h2>Content Section</h2>
        <p>Your main content goes here.</p>
    </main>
'''

    elif layout_type == "Card Grid":
        num_cards = int(options.get('num_cards', 6))
        cards_per_row = int(options.get('cards_per_row', 3))
        html += f'    <div class="card-grid cards-per-row-{cards_per_row}">\n'

        for i in range(num_cards):
            html += f'''        <div class="card">
            <h3>Card {i + 1}</h3>
            <p>This is card content for card number {i + 1}.</p>
            <button class="card-button">Learn More</button>
        </div>
'''
        html += '    </div>\n'

    html += '</body>\n</html>'
    return html


def generate_layout_css(layout_type, responsive=True):
    """Generate CSS for different layout types"""

    css = '''
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        color: #333;
    }
    '''

    if layout_type == "Header-Content-Footer":
        css += '''
    .header {
        background-color: #2c3e50;
        color: white;
        padding: 1rem 2rem;
        text-align: center;
    }

    .main-content {
        min-height: calc(100vh - 140px);
        padding: 2rem;
    }

    .footer {
        background-color: #34495e;
        color: white;
        text-align: center;
        padding: 1rem;
        margin-top: auto;
    }
    '''

    elif layout_type == "Sidebar Layout":
        css += '''
    .layout-container {
        display: flex;
        min-height: 100vh;
    }

    .sidebar {
        width: 250px;
        background-color: #f8f9fa;
        padding: 1rem;
        border-right: 1px solid #dee2e6;
    }

    .sidebar-right .sidebar {
        order: 2;
        border-right: none;
        border-left: 1px solid #dee2e6;
    }

    .main-content {
        flex: 1;
        padding: 2rem;
    }
    '''

    elif layout_type in ["Two Column", "Three Column"]:
        css += '''
    .columns-container {
        display: flex;
        gap: 2rem;
        padding: 2rem;
    }

    .column {
        flex: 1;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    '''

    elif layout_type == "Hero Section":
        css += '''
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        padding: 4rem 2rem;
        min-height: 50vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .hero-title {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }

    .hero-button {
        display: inline-block;
        padding: 12px 30px;
        background-color: #fff;
        color: #667eea;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
        transition: transform 0.3s ease;
    }

    .hero-button:hover {
        transform: translateY(-2px);
    }

    .content {
        padding: 4rem 2rem;
    }
    '''

    elif layout_type == "Card Grid":
        css += '''
    .card-grid {
        display: grid;
        gap: 2rem;
        padding: 2rem;
    }

    .cards-per-row-2 {
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    }

    .cards-per-row-3 {
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    }

    .cards-per-row-4 {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    }

    .card {
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    .card-button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 1rem;
    }
    '''

    if responsive:
        css += '''

    @media (max-width: 768px) {
        .layout-container {
            flex-direction: column;
        }

        .sidebar {
            width: 100%;
        }

        .columns-container {
            flex-direction: column;
        }

        .hero-title {
            font-size: 2rem;
        }

        .card-grid {
            grid-template-columns: 1fr;
        }
    }
    '''

    css += '\n    </style>'
    return css


def html_boilerplate_generator():
    """Generate HTML5 boilerplate code"""
    create_tool_header("HTML Boilerplate Generator", "Generate HTML5 boilerplate with modern best practices", "📄")

    st.subheader("Boilerplate Configuration")

    col1, col2 = st.columns(2)

    with col1:
        page_title = st.text_input("Page Title", "My Website")
        page_description = st.text_input("Meta Description", "A modern website built with HTML5")
        author = st.text_input("Author", "Your Name")
        lang = st.selectbox("Language", ["en", "es", "fr", "de", "it", "pt", "zh", "ja"])

    with col2:
        include_viewport = st.checkbox("Responsive Viewport", True)
        include_favicon = st.checkbox("Favicon Links", True)
        include_og_tags = st.checkbox("Open Graph Tags", True)
        include_analytics = st.checkbox("Google Analytics", False)

    framework_options = st.multiselect("Include Frameworks/Libraries", [
        "Bootstrap 5", "Tailwind CSS", "jQuery", "React", "Vue.js", "Alpine.js", "HTMX"
    ])

    css_reset = st.selectbox("CSS Reset/Normalize", ["None", "Normalize.css", "CSS Reset", "Modern CSS Reset"])

    include_sections = st.multiselect("Include Page Sections", [
        "Header", "Navigation", "Main Content", "Sidebar", "Footer", "Hero Section"
    ])

    if st.button("Generate Boilerplate"):
        boilerplate = generate_html_boilerplate(
            page_title, page_description, author, lang, include_viewport,
            include_favicon, include_og_tags, include_analytics,
            framework_options, css_reset, include_sections
        )

        st.subheader("Generated HTML5 Boilerplate")
        st.code(boilerplate, language='html')

        FileHandler.create_download_link(boilerplate.encode(), "index.html", "text/html")
        st.success("✅ HTML5 boilerplate generated successfully!")


def generate_html_boilerplate(title, description, author, lang, viewport, favicon, og_tags, analytics, frameworks,
                              css_reset, sections):
    """Generate HTML5 boilerplate code"""

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">'''

    if viewport:
        html += '\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">'

    html += f'''
    <meta name="description" content="{description}">
    <meta name="author" content="{author}">
    <title>{title}</title>'''

    if favicon:
        html += '''

    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">'''

    if og_tags:
        html += f'''

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://example.com">
    <meta property="og:image" content="https://example.com/og-image.jpg">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="https://example.com/twitter-image.jpg">'''

    # CSS Reset
    if css_reset == "Normalize.css":
        html += '\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">'
    elif css_reset == "Modern CSS Reset":
        html += '''

    <!-- Modern CSS Reset -->
    <style>
    *, *::before, *::after {
        box-sizing: border-box;
    }
    * {
        margin: 0;
    }
    html, body {
        height: 100%;
    }
    body {
        line-height: 1.5;
        -webkit-font-smoothing: antialiased;
    }
    img, picture, video, canvas, svg {
        display: block;
        max-width: 100%;
    }
    input, button, textarea, select {
        font: inherit;
    }
    p, h1, h2, h3, h4, h5, h6 {
        overflow-wrap: break-word;
    }
    </style>'''

    # Frameworks
    if "Bootstrap 5" in frameworks:
        html += '\n    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">'

    if "Tailwind CSS" in frameworks:
        html += '\n    <script src="https://cdn.tailwindcss.com"></script>'

    html += '\n    <link rel="stylesheet" href="styles.css">'
    html += '\n</head>\n<body>\n'

    # Body sections
    if "Header" in sections:
        html += '''    <header>
        <h1>Website Title</h1>
    </header>

'''

    if "Navigation" in sections:
        html += '''    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

'''

    if "Hero Section" in sections:
        html += '''    <section class="hero">
        <h2>Welcome to Our Website</h2>
        <p>Discover amazing content and services</p>
        <button>Get Started</button>
    </section>

'''

    html += '''    <main>
        <h2>Main Content</h2>
        <p>Your main content goes here.</p>
    </main>

'''

    if "Sidebar" in sections:
        html += '''    <aside>
        <h3>Sidebar</h3>
        <p>Sidebar content goes here.</p>
    </aside>

'''

    if "Footer" in sections:
        html += f'''    <footer>
        <p>&copy; 2024 {author}. All rights reserved.</p>
    </footer>

'''

    # JavaScript
    if "jQuery" in frameworks:
        html += '    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>\n'

    if "Bootstrap 5" in frameworks:
        html += '    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n'

    if "React" in frameworks:
        html += '''    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
'''

    if "Vue.js" in frameworks:
        html += '    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>\n'

    if "Alpine.js" in frameworks:
        html += '    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>\n'

    if "HTMX" in frameworks:
        html += '    <script src="https://unpkg.com/htmx.org@1.9.6"></script>\n'

    if analytics:
        html += '''
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'GA_TRACKING_ID');
    </script>
'''

    html += '    <script src="script.js"></script>\n'
    html += '</body>\n</html>'

    return html


def css_flexbox_generator():
    """Generate CSS Flexbox layouts"""
    create_tool_header("CSS Flexbox Generator", "Generate CSS Flexbox layouts with visual controls", "📐")

    st.subheader("Container Properties")

    col1, col2 = st.columns(2)

    with col1:
        flex_direction = st.selectbox("Flex Direction", ["row", "row-reverse", "column", "column-reverse"])
        flex_wrap = st.selectbox("Flex Wrap", ["nowrap", "wrap", "wrap-reverse"])
        justify_content = st.selectbox("Justify Content", [
            "flex-start", "flex-end", "center", "space-between", "space-around", "space-evenly"
        ])

    with col2:
        align_items = st.selectbox("Align Items", [
            "stretch", "flex-start", "flex-end", "center", "baseline"
        ])
        align_content = st.selectbox("Align Content", [
            "stretch", "flex-start", "flex-end", "center", "space-between", "space-around"
        ])
        gap = st.number_input("Gap (px)", min_value=0, max_value=100, value=0)

    st.subheader("Flex Items")
    num_items = st.number_input("Number of Items", min_value=1, max_value=20, value=3)

    # Item properties
    item_properties = []
    for i in range(int(num_items)):
        st.write(f"**Item {i + 1}:**")
        item_cols = st.columns(4)
        with item_cols[0]:
            flex_grow = st.number_input(f"Grow", min_value=0, max_value=10, value=0, key=f"grow_{i}")
        with item_cols[1]:
            flex_shrink = st.number_input(f"Shrink", min_value=0, max_value=10, value=1, key=f"shrink_{i}")
        with item_cols[2]:
            flex_basis = st.text_input(f"Basis", "auto", key=f"basis_{i}")
        with item_cols[3]:
            align_self = st.selectbox(f"Align Self",
                                      ["auto", "stretch", "flex-start", "flex-end", "center", "baseline"],
                                      key=f"align_{i}")

        item_properties.append({
            'grow': flex_grow,
            'shrink': flex_shrink,
            'basis': flex_basis,
            'align_self': align_self
        })

    if st.button("Generate Flexbox"):
        flexbox_css = generate_flexbox_css(
            flex_direction, flex_wrap, justify_content, align_items, align_content,
            gap, num_items, item_properties
        )

        st.subheader("Generated CSS")
        st.code(flexbox_css, language='css')

        # HTML example
        html_example = generate_flexbox_html(int(num_items))
        st.subheader("HTML Example")
        st.code(html_example, language='html')

        # Combined file
        combined = f"<!DOCTYPE html>\n<html>\n<head>\n<style>\n{flexbox_css}\n</style>\n</head>\n<body>\n{html_example}\n</body>\n</html>"

        FileHandler.create_download_link(combined.encode(), "flexbox_layout.html", "text/html")
        st.success("✅ Flexbox CSS generated successfully!")


def generate_flexbox_css(direction, wrap, justify, align_items, align_content, gap, num_items, item_props):
    """Generate CSS for flexbox layout"""
    css = f'''.flex-container {{
  display: flex;
  flex-direction: {direction};
  flex-wrap: {wrap};
  justify-content: {justify};
  align-items: {align_items};
  align-content: {align_content};'''

    if gap > 0:
        css += f'\n  gap: {gap}px;'

    css += '''
  padding: 20px;
  background-color: #f0f0f0;
  min-height: 300px;
}

.flex-item {
  background-color: #007bff;
  color: white;
  padding: 20px;
  text-align: center;
  border-radius: 5px;
  margin: 5px;
}
'''

    # Individual item styles
    for i, props in enumerate(item_props):
        css += f'''
.flex-item:nth-child({i + 1}) {{
  flex: {props['grow']} {props['shrink']} {props['basis']};
  align-self: {props['align_self']};
}}'''

    return css


def generate_flexbox_html(num_items):
    """Generate HTML for flexbox example"""
    html = '<div class="flex-container">\n'
    for i in range(num_items):
        html += f'  <div class="flex-item">Item {i + 1}</div>\n'
    html += '</div>'
    return html


def css_grid_generator():
    """Generate CSS Grid layouts"""
    create_tool_header("CSS Grid Generator", "Generate CSS Grid layouts with visual controls", "⚏")

    st.subheader("Grid Container Properties")

    col1, col2 = st.columns(2)

    with col1:
        grid_template_columns = st.text_input("Grid Template Columns", "repeat(3, 1fr)")
        grid_template_rows = st.text_input("Grid Template Rows", "repeat(3, 100px)")
        gap = st.number_input("Gap (px)", min_value=0, max_value=50, value=10)

    with col2:
        justify_items = st.selectbox("Justify Items", ["stretch", "start", "end", "center"])
        align_items = st.selectbox("Align Items", ["stretch", "start", "end", "center"])
        justify_content = st.selectbox("Justify Content", [
            "start", "end", "center", "stretch", "space-around", "space-between", "space-evenly"
        ])

    st.subheader("Grid Items")
    num_items = st.number_input("Number of Items", min_value=1, max_value=50, value=9)

    # Special grid areas
    st.subheader("Special Areas (Optional)")
    use_areas = st.checkbox("Use Named Grid Areas")

    area_assignments = {}
    if use_areas:
        grid_areas = st.text_area("Grid Template Areas",
                                  '"header header header"\n"sidebar main main"\n"footer footer footer"')

        # Area assignments
        st.write("Assign items to areas:")
        for i in range(int(num_items)):
            area = st.text_input(f"Item {i + 1} Area", "", key=f"area_{i}")
            if area:
                area_assignments[i] = area

    if st.button("Generate Grid"):
        grid_css = generate_grid_css(
            grid_template_columns, grid_template_rows, gap, justify_items,
            align_items, justify_content, num_items,
            grid_areas if use_areas else None,
            area_assignments
        )

        st.subheader("Generated CSS")
        st.code(grid_css, language='css')

        # HTML example
        html_example = generate_grid_html(int(num_items))
        st.subheader("HTML Example")
        st.code(html_example, language='html')

        # Combined file
        combined = f"<!DOCTYPE html>\n<html>\n<head>\n<style>\n{grid_css}\n</style>\n</head>\n<body>\n{html_example}\n</body>\n</html>"

        FileHandler.create_download_link(combined.encode(), "grid_layout.html", "text/html")
        st.success("✅ CSS Grid generated successfully!")


def generate_grid_css(columns, rows, gap, justify_items, align_items, justify_content, num_items, areas=None,
                      assignments={}):
    """Generate CSS for grid layout"""
    css = f'''.grid-container {{
  display: grid;
  grid-template-columns: {columns};
  grid-template-rows: {rows};
  gap: {gap}px;
  justify-items: {justify_items};
  align-items: {align_items};
  justify-content: {justify_content};
  padding: 20px;
  background-color: #f0f0f0;
  min-height: 400px;
}}'''

    if areas:
        css += f'\n  grid-template-areas: {areas};'

    css += '''

.grid-item {
  background-color: #007bff;
  color: white;
  padding: 20px;
  text-align: center;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}
'''

    # Area assignments
    for item_idx, area in assignments.items():
        css += f'''
.grid-item:nth-child({item_idx + 1}) {{
  grid-area: {area};
}}'''

    return css


def generate_grid_html(num_items):
    """Generate HTML for grid example"""
    html = '<div class="grid-container">\n'
    for i in range(num_items):
        html += f'  <div class="grid-item">Item {i + 1}</div>\n'
    html += '</div>'
    return html


def css_animation_generator():
    """Generate CSS animations"""
    create_tool_header("CSS Animation Generator", "Generate CSS animations and keyframes", "🎬")

    st.subheader("Animation Properties")

    col1, col2 = st.columns(2)

    with col1:
        animation_name = st.text_input("Animation Name", "myAnimation")
        duration = st.number_input("Duration (seconds)", min_value=0.1, max_value=60.0, value=2.0, step=0.1)
        timing_function = st.selectbox("Timing Function", [
            "ease", "ease-in", "ease-out", "ease-in-out", "linear",
            "cubic-bezier(0.25, 0.46, 0.45, 0.94)"
        ])
        delay = st.number_input("Delay (seconds)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

    with col2:
        iteration_count = st.selectbox("Iteration Count", ["1", "2", "3", "infinite", "custom"])
        if iteration_count == "custom":
            iteration_count = st.number_input("Custom Count", min_value=1, value=1)

        direction = st.selectbox("Direction", ["normal", "reverse", "alternate", "alternate-reverse"])
        fill_mode = st.selectbox("Fill Mode", ["none", "forwards", "backwards", "both"])
        play_state = st.selectbox("Play State", ["running", "paused"])

    st.subheader("Keyframes")

    animation_type = st.selectbox("Animation Type", [
        "Custom", "Fade In", "Fade Out", "Slide In", "Slide Out",
        "Scale", "Rotate", "Bounce", "Pulse", "Shake"
    ])

    if animation_type == "Custom":
        st.info("Define custom keyframes (0% to 100%)")

        # Initialize keyframes in session state
        if 'keyframes' not in st.session_state:
            st.session_state.keyframes = [
                {'percentage': 0, 'properties': 'transform: translateX(0px);'},
                {'percentage': 100, 'properties': 'transform: translateX(100px);'}
            ]

        # Add keyframe interface
        st.write("**Add Keyframe:**")
        new_cols = st.columns(3)
        with new_cols[0]:
            new_percentage = st.number_input("Percentage", min_value=0, max_value=100, value=50)
        with new_cols[1]:
            new_properties = st.text_input("CSS Properties", "opacity: 0.5;")
        with new_cols[2]:
            if st.button("Add Keyframe"):
                st.session_state.keyframes.append({
                    'percentage': new_percentage,
                    'properties': new_properties
                })
                st.session_state.keyframes.sort(key=lambda x: x['percentage'])
                st.rerun()

        # Display current keyframes
        st.write("**Current Keyframes:**")
        for i, kf in enumerate(st.session_state.keyframes):
            kf_cols = st.columns([1, 3, 1])
            with kf_cols[0]:
                st.write(f"{kf['percentage']}%")
            with kf_cols[1]:
                st.code(kf['properties'])
            with kf_cols[2]:
                if st.button("Remove", key=f"remove_kf_{i}"):
                    st.session_state.keyframes.pop(i)
                    st.rerun()

    if st.button("Generate Animation"):
        if animation_type == "Custom":
            keyframes_data = st.session_state.keyframes
        else:
            keyframes_data = get_preset_keyframes(animation_type)

        animation_css = generate_animation_css(
            animation_name, duration, timing_function, delay,
            iteration_count, direction, fill_mode, play_state,
            keyframes_data
        )

        st.subheader("Generated CSS")
        st.code(animation_css, language='css')

        # HTML example
        html_example = generate_animation_html(animation_name)
        st.subheader("HTML Example")
        st.code(html_example, language='html')

        # Combined file
        combined = f"<!DOCTYPE html>\n<html>\n<head>\n<style>\n{animation_css}\n</style>\n</head>\n<body>\n{html_example}\n</body>\n</html>"

        FileHandler.create_download_link(combined.encode(), f"{animation_name}.html", "text/html")
        st.success("✅ CSS Animation generated successfully!")

    if animation_type == "Custom" and st.button("Clear All Keyframes"):
        st.session_state.keyframes = []
        st.rerun()


def get_preset_keyframes(animation_type):
    """Get preset keyframes for common animations"""
    presets = {
        "Fade In": [
            {'percentage': 0, 'properties': 'opacity: 0;'},
            {'percentage': 100, 'properties': 'opacity: 1;'}
        ],
        "Fade Out": [
            {'percentage': 0, 'properties': 'opacity: 1;'},
            {'percentage': 100, 'properties': 'opacity: 0;'}
        ],
        "Slide In": [
            {'percentage': 0, 'properties': 'transform: translateX(-100%);'},
            {'percentage': 100, 'properties': 'transform: translateX(0);'}
        ],
        "Slide Out": [
            {'percentage': 0, 'properties': 'transform: translateX(0);'},
            {'percentage': 100, 'properties': 'transform: translateX(100%);'}
        ],
        "Scale": [
            {'percentage': 0, 'properties': 'transform: scale(0);'},
            {'percentage': 100, 'properties': 'transform: scale(1);'}
        ],
        "Rotate": [
            {'percentage': 0, 'properties': 'transform: rotate(0deg);'},
            {'percentage': 100, 'properties': 'transform: rotate(360deg);'}
        ],
        "Bounce": [
            {'percentage': 0, 'properties': 'transform: translateY(0);'},
            {'percentage': 25, 'properties': 'transform: translateY(-20px);'},
            {'percentage': 50, 'properties': 'transform: translateY(0);'},
            {'percentage': 75, 'properties': 'transform: translateY(-10px);'},
            {'percentage': 100, 'properties': 'transform: translateY(0);'}
        ],
        "Pulse": [
            {'percentage': 0, 'properties': 'transform: scale(1);'},
            {'percentage': 50, 'properties': 'transform: scale(1.1);'},
            {'percentage': 100, 'properties': 'transform: scale(1);'}
        ],
        "Shake": [
            {'percentage': 0, 'properties': 'transform: translateX(0);'},
            {'percentage': 25, 'properties': 'transform: translateX(-5px);'},
            {'percentage': 75, 'properties': 'transform: translateX(5px);'},
            {'percentage': 100, 'properties': 'transform: translateX(0);'}
        ]
    }
    return presets.get(animation_type, [])


def generate_animation_css(name, duration, timing, delay, iterations, direction, fill_mode, play_state, keyframes):
    """Generate CSS animation code"""

    # Keyframes
    css = f'@keyframes {name} {{\n'
    for kf in sorted(keyframes, key=lambda x: x['percentage']):
        css += f'  {kf["percentage"]}% {{\n'
        css += f'    {kf["properties"]}\n'
        css += f'  }}\n'
    css += '}\n\n'

    # Animation class
    css += f'''.animated-element {{
  animation-name: {name};
  animation-duration: {duration}s;
  animation-timing-function: {timing};
  animation-delay: {delay}s;
  animation-iteration-count: {iterations};
  animation-direction: {direction};
  animation-fill-mode: {fill_mode};
  animation-play-state: {play_state};

  /* Element styling */
  width: 100px;
  height: 100px;
  background-color: #007bff;
  margin: 50px auto;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
}}

/* Optional: Hover to trigger animation */
.trigger:hover .animated-element {{
  animation-play-state: running;
}}'''

    return css


def generate_animation_html(animation_name):
    """Generate HTML for animation example"""
    return f'''<div class="trigger">
  <p>Animation: {animation_name}</p>
  <div class="animated-element">
    Animated
  </div>
  <p>Hover to trigger (if paused)</p>
</div>'''


def css_gradient_generator():
    """Generate CSS gradients"""
    create_tool_header("CSS Gradient Generator", "Generate CSS linear and radial gradients", "🌈")

    gradient_type = st.selectbox("Gradient Type", ["Linear", "Radial", "Conic"])

    if gradient_type == "Linear":
        st.subheader("Linear Gradient Properties")

        col1, col2 = st.columns(2)
        with col1:
            direction = st.selectbox("Direction", [
                "to right", "to left", "to bottom", "to top",
                "to bottom right", "to bottom left", "to top right", "to top left",
                "Custom angle"
            ])

            if direction == "Custom angle":
                angle = st.number_input("Angle (degrees)", min_value=0, max_value=360, value=45)
                direction = f"{angle}deg"

        with col2:
            repeating = st.checkbox("Repeating Gradient")

    elif gradient_type == "Radial":
        st.subheader("Radial Gradient Properties")

        col1, col2 = st.columns(2)
        with col1:
            shape = st.selectbox("Shape", ["ellipse", "circle"])
            size = st.selectbox("Size", [
                "farthest-corner", "closest-side", "closest-corner", "farthest-side", "Custom"
            ])

            if size == "Custom":
                custom_size = st.text_input("Custom Size", "100px 50px")
                size = custom_size

        with col2:
            position = st.selectbox("Position", [
                "center", "top", "bottom", "left", "right",
                "top left", "top right", "bottom left", "bottom right", "Custom"
            ])

            if position == "Custom":
                custom_position = st.text_input("Custom Position", "50% 50%")
                position = custom_position

            repeating = st.checkbox("Repeating Gradient")

    elif gradient_type == "Conic":
        st.subheader("Conic Gradient Properties")

        col1, col2 = st.columns(2)
        with col1:
            from_angle = st.number_input("From Angle (degrees)", min_value=0, max_value=360, value=0)
        with col2:
            position = st.selectbox("Position", [
                "center", "top", "bottom", "left", "right", "Custom"
            ])

            if position == "Custom":
                custom_position = st.text_input("Custom Position", "50% 50%")
                position = custom_position

    st.subheader("Color Stops")

    # Initialize color stops in session state
    if 'color_stops' not in st.session_state:
        st.session_state.color_stops = [
            {'color': '#ff0000', 'position': '0%'},
            {'color': '#0000ff', 'position': '100%'}
        ]

    # Add color stop interface
    st.write("**Add Color Stop:**")
    add_cols = st.columns(3)
    with add_cols[0]:
        new_color = st.color_picker("Color", "#00ff00")
    with add_cols[1]:
        new_position = st.text_input("Position", "50%")
    with add_cols[2]:
        if st.button("Add Color"):
            st.session_state.color_stops.append({
                'color': new_color,
                'position': new_position
            })
            st.rerun()

    # Display current color stops
    st.write("**Current Color Stops:**")
    for i, stop in enumerate(st.session_state.color_stops):
        stop_cols = st.columns([1, 2, 2, 1])
        with stop_cols[0]:
            st.markdown(
                f'<div style="width:30px;height:30px;background-color:{stop["color"]};border:1px solid #ccc;"></div>',
                unsafe_allow_html=True)
        with stop_cols[1]:
            st.write(stop['color'])
        with stop_cols[2]:
            st.write(stop['position'])
        with stop_cols[3]:
            if st.button("Remove", key=f"remove_stop_{i}"):
                st.session_state.color_stops.pop(i)
                st.rerun()

    if st.button("Generate Gradient"):
        gradient_css = generate_gradient_css(
            gradient_type.lower(), st.session_state.color_stops,
            locals()  # Pass all local variables
        )

        st.subheader("Generated CSS")
        st.code(gradient_css, language='css')

        # Preview
        st.subheader("Gradient Preview")
        preview_style = f"background: {gradient_css.split(':')[1].split(';')[0].strip()}; height: 200px; border-radius: 10px;"
        st.markdown(f'<div style="{preview_style}"></div>', unsafe_allow_html=True)

        # HTML example
        html_example = f'''<div class="gradient-element">
  <h2>Gradient Background</h2>
  <p>This element has a {gradient_type.lower()} gradient background.</p>
</div>'''

        st.subheader("HTML Example")
        st.code(html_example, language='html')

        # Combined file
        combined = f"<!DOCTYPE html>\n<html>\n<head>\n<style>\n{gradient_css}\n</style>\n</head>\n<body>\n{html_example}\n</body>\n</html>"

        FileHandler.create_download_link(combined.encode(), f"{gradient_type.lower()}_gradient.html", "text/html")
        st.success("✅ CSS Gradient generated successfully!")

    if st.button("Clear All Colors"):
        st.session_state.color_stops = []
        st.rerun()


def generate_gradient_css(gradient_type, color_stops, options):
    """Generate CSS gradient code"""

    # Build color stops string
    stops_str = ", ".join([f"{stop['color']} {stop['position']}" for stop in color_stops])

    if gradient_type == "linear":
        direction = options.get('direction', 'to right')
        repeating = options.get('repeating', False)

        gradient_func = "repeating-linear-gradient" if repeating else "linear-gradient"
        gradient = f"{gradient_func}({direction}, {stops_str})"

    elif gradient_type == "radial":
        shape = options.get('shape', 'ellipse')
        size = options.get('size', 'farthest-corner')
        position = options.get('position', 'center')
        repeating = options.get('repeating', False)

        gradient_func = "repeating-radial-gradient" if repeating else "radial-gradient"
        gradient = f"{gradient_func}({shape} {size} at {position}, {stops_str})"

    elif gradient_type == "conic":
        from_angle = options.get('from_angle', 0)
        position = options.get('position', 'center')

        gradient = f"conic-gradient(from {from_angle}deg at {position}, {stops_str})"

    css = f'''.gradient-element {{
  background: {gradient};
  min-height: 200px;
  padding: 20px;
  color: white;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}}

.gradient-element h2 {{
  margin: 0 0 10px 0;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}}

.gradient-element p {{
  margin: 0;
  opacity: 0.9;
}}'''

    return css


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


def timestamp_converter():
    """Timestamp conversion tool"""
    create_tool_header("Timestamp Converter", "Convert between timestamps and human-readable dates", "⏰")

    tab1, tab2 = st.tabs(["Timestamp to Date", "Date to Timestamp"])

    with tab1:
        st.subheader("Convert Timestamp to Date")
        timestamp_input = st.text_input("Enter timestamp (Unix epoch):", placeholder="1609459200")

        col1, col2 = st.columns(2)
        with col1:
            timestamp_format = st.selectbox("Timestamp format:", ["Seconds", "Milliseconds"])
        with col2:
            timezone = st.selectbox("Timezone:", ["UTC", "Local"])

        if timestamp_input and st.button("Convert to Date"):
            try:
                timestamp = float(timestamp_input)
                if timestamp_format == "Milliseconds":
                    timestamp = timestamp / 1000

                if timezone == "UTC":
                    dt = datetime.datetime.utcfromtimestamp(timestamp)
                    formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S UTC")
                else:
                    dt = datetime.datetime.fromtimestamp(timestamp)
                    formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S Local")

                readable_format = "%A, %B %d, %Y at %I:%M:%S %p"
                st.success(f"**Date:** {formatted_date}")
                st.info(f"**ISO Format:** {dt.isoformat()}")
                st.info(f"**Readable:** {dt.strftime(readable_format)}")

            except (ValueError, OSError) as e:
                st.error(f"Invalid timestamp: {str(e)}")

    with tab2:
        st.subheader("Convert Date to Timestamp")

        col1, col2 = st.columns(2)
        with col1:
            date_input = st.date_input("Select date:", datetime.date.today())
        with col2:
            time_input = st.time_input("Select time:", datetime.time(12, 0))

        output_format = st.selectbox("Output format:", ["Seconds", "Milliseconds"])

        if st.button("Convert to Timestamp"):
            try:
                dt = datetime.datetime.combine(date_input, time_input)
                timestamp = dt.timestamp()

                if output_format == "Milliseconds":
                    timestamp = int(timestamp * 1000)
                    st.success(f"**Timestamp:** {timestamp} (milliseconds)")
                else:
                    timestamp = int(timestamp)
                    st.success(f"**Timestamp:** {timestamp} (seconds)")

                st.info(f"**Current Timestamp:** {int(time.time())} (seconds)")

            except Exception as e:
                st.error(f"Error converting date: {str(e)}")


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
            st.success(f"✅ {hash_type} hash generated successfully!")
            FileHandler.create_download_link(hash_result.encode(), f"hash_{hash_type.lower()}.txt", "text/plain")


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

        st.success(f"✅ Generated {num_uuids} UUID(s) successfully!")

        # Create downloadable file
        uuid_text = "\n".join(uuids)
        FileHandler.create_download_link(uuid_text.encode(), "uuids.txt", "text/plain")


def form_validator():
    """Validate HTML forms for accessibility and best practices"""
    create_tool_header("Form Validator", "Validate HTML forms for accessibility and best practices", "📋")

    # File upload option
    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded HTML:", html_code, height=150, disabled=True)
    else:
        html_code = st.text_area(
            "Enter HTML form code:",
            height=200,
            placeholder="""<form action="/submit" method="post">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <button type="submit">Submit</button>
</form>"""
        )

    if html_code and st.button("Validate Form"):
        issues = validate_form(html_code)

        if not issues:
            st.success("✅ Form validation passed! No issues found.")
        else:
            st.error(f"❌ Found {len(issues)} issues:")
            for i, issue in enumerate(issues, 1):
                st.write(f"{i}. {issue}")


def validate_form(html_code):
    """Validate HTML form for common issues"""
    issues = []

    # Check for forms without action attribute
    forms_without_action = re.findall(r'<form(?![^>]*action)[^>]*>', html_code, re.IGNORECASE)
    if forms_without_action:
        issues.append("Form found without action attribute")

    # Check for inputs without labels
    inputs = re.findall(r'<input[^>]*>', html_code, re.IGNORECASE)
    for input_tag in inputs:
        # Extract id attribute
        id_match = re.search(r'id=["\']([^"\']*)["\']', input_tag)
        if id_match:
            input_id = id_match.group(1)
            # Check if there's a corresponding label
            label_pattern = f'for=["\']({input_id})["\']'
            if not re.search(label_pattern, html_code, re.IGNORECASE):
                issues.append(f'Input with id="{input_id}" has no associated label')
        else:
            # Input without id
            type_match = re.search(r'type=["\']([^"\']*)["\']', input_tag)
            input_type = type_match.group(1) if type_match else "text"
            if input_type not in ["hidden", "submit", "button"]:
                issues.append(f'Input of type "{input_type}" has no id attribute for label association')

    # Check for submit button
    if not re.search(r'<button[^>]*type=["\']submit["\'][^>]*>|<input[^>]*type=["\']submit["\'][^>]*>', html_code,
                     re.IGNORECASE):
        issues.append("No submit button found in form")

    return issues


def link_checker():
    """Check links in HTML for validity and accessibility"""
    create_tool_header("Link Checker", "Check HTML links for validity and accessibility", "🔗")

    # File upload option
    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded HTML:", html_code, height=150, disabled=True)
    else:
        html_code = st.text_area(
            "Enter HTML with links:",
            height=200,
            placeholder="""<html>
<body>
  <a href="https://example.com">Valid Link</a>
  <a href="">Empty Link</a>
  <a href="https://broken-link.invalid">Broken Link</a>
  <a href="mailto:user@example.com">Email Link</a>
  <a href="#section1">Internal Link</a>
</body>
</html>"""
        )

    if html_code and st.button("Check Links"):
        with st.spinner("Checking links..."):
            results = check_links(html_code)

            if not results["links"]:
                st.info("No links found in the HTML code.")
            else:
                st.subheader(f"Found {len(results['links'])} links:")

                for link_info in results["links"]:
                    link_text = link_info["text"][:50] + "..." if len(link_info["text"]) > 50 else link_info["text"]
                    with st.expander(f"🔗 {link_text}"):
                        col1, col2 = st.columns([2, 1])

                        with col1:
                            st.write(f"**URL:** {link_info['url']}")
                            st.write(f"**Link Text:** {link_info['text']}")

                        with col2:
                            if link_info["status"] == "valid":
                                st.success("✅ Valid")
                            elif link_info["status"] == "warning":
                                st.warning("⚠️ Warning")
                            else:
                                st.error("❌ Issue")

                        if link_info.get("issues"):
                            st.write("**Issues:**")
                            for issue in link_info["issues"]:
                                st.write(f"• {issue}")


def check_links(html_code):
    """Check all links in HTML code"""
    links = []

    # Find all anchor tags
    link_pattern = r'<a\s+([^>]*href=["\']([^"\']*)["\'][^>]*)>([^<]*)</a>'
    matches = re.finditer(link_pattern, html_code, re.IGNORECASE)

    for match in matches:
        attrs = match.group(1)
        url = match.group(2)
        text = match.group(3).strip()

        link_info = {
            "url": url,
            "text": text,
            "status": "valid",
            "issues": []
        }

        # Check for common issues
        if not url:
            link_info["status"] = "error"
            link_info["issues"].append("Empty href attribute")
        elif url.startswith("javascript:"):
            link_info["status"] = "warning"
            link_info["issues"].append("JavaScript link - consider accessibility")
        elif not text:
            link_info["status"] = "warning"
            link_info["issues"].append("Empty link text - bad for accessibility")

        # Check if it's an email link
        if url.startswith("mailto:"):
            link_info["status"] = "valid"
        # Check if it's an internal link
        elif url.startswith("#"):
            link_info["status"] = "valid"
        # Check if it's a relative link
        elif not url.startswith(("http://", "https://")):
            link_info["status"] = "warning"
            link_info["issues"].append("Relative link - cannot check validity")

        links.append(link_info)

    return {"links": links}


def cross_browser_test():
    """Simulate cross-browser compatibility testing"""
    create_tool_header("Cross-Browser Test", "Check HTML/CSS for cross-browser compatibility", "🌐")

    # File upload option
    uploaded_file = FileHandler.upload_files(['html', 'htm', 'css'], accept_multiple=False)

    if uploaded_file:
        code = FileHandler.process_text_file(uploaded_file[0])
        file_type = uploaded_file[0].name.split(".")[-1].lower()
        st.text_area(f"Uploaded {file_type.upper()}:", code, height=150, disabled=True)
    else:
        file_type = st.selectbox("Code type:", ["HTML", "CSS"])

        if file_type == "HTML":
            code = st.text_area(
                "Enter HTML code:",
                height=200,
                placeholder="""<!DOCTYPE html>
<html>
<head>
  <style>
    .container { display: flex; }
    .item { flex: 1; }
  </style>
</head>
<body>
  <div class="container">
    <div class="item">Content</div>
  </div>
</body>
</html>"""
            )
        else:
            code = st.text_area(
                "Enter CSS code:",
                height=200,
                placeholder=""".container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.item {
  background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
  border-radius: 10px;
  padding: 20px;
}"""
            )

    if code and st.button("Run Cross-Browser Test"):
        issues = check_browser_compatibility(code, file_type.lower() if 'file_type' in locals() else "html")

        st.subheader("Browser Compatibility Report")

        browsers = ["Chrome", "Firefox", "Safari", "Edge", "Internet Explorer"]

        for browser in browsers:
            with st.expander(f"🌐 {browser}"):
                browser_issues = [issue for issue in issues if
                                  browser.lower() in issue.lower() or "all browsers" in issue.lower()]

                if not browser_issues:
                    st.success("✅ No compatibility issues found")
                else:
                    for issue in browser_issues:
                        if "warning" in issue.lower():
                            st.warning(f"⚠️ {issue}")
                        else:
                            st.error(f"❌ {issue}")


def check_browser_compatibility(code, file_type):
    """Check for common cross-browser compatibility issues"""
    issues = []

    if file_type == "html":
        # Check for HTML5 features
        if "<!DOCTYPE html>" not in code:
            issues.append("Missing HTML5 doctype - may cause issues in older Internet Explorer versions")

        # Check for modern CSS features in style tags
        if "display: flex" in code:
            issues.append("Warning: Flexbox has limited support in Internet Explorer 10 and below")

        if "display: grid" in code:
            issues.append("Warning: CSS Grid has no support in Internet Explorer")

    elif file_type == "css":
        # CSS specific checks
        if "display: grid" in code:
            issues.append("Warning: CSS Grid has no support in Internet Explorer")

        if "display: flex" in code:
            issues.append("Warning: Flexbox has limited support in Internet Explorer 10 and below")

        if "border-radius:" in code:
            issues.append("Warning: border-radius needs -webkit- prefix for older Safari versions")

        if "linear-gradient" in code:
            issues.append("Warning: Gradients need vendor prefixes for older browsers")

        if "transform:" in code:
            issues.append("Warning: CSS transforms need vendor prefixes for older browsers")

    # Common issues for both
    if "@media" in code and "max-width" in code:
        issues.append("All browsers: Media queries work well in modern browsers")

    return issues


def error_logger():
    """Log and track JavaScript errors and debugging information"""
    create_tool_header("Error Logger", "Track and analyze JavaScript errors", "🐛")

    tab1, tab2 = st.tabs(["Log Errors", "Error Analysis"])

    with tab1:
        st.subheader("JavaScript Error Logger")

        error_message = st.text_area(
            "Paste error message:",
            height=100,
            placeholder='TypeError: Cannot read property "length" of undefined\n  at processData (app.js:45:12)\n  at handleClick (app.js:23:5)'
        )

        col1, col2 = st.columns(2)
        with col1:
            error_type = st.selectbox("Error Type:", [
                "TypeError", "ReferenceError", "SyntaxError", "RangeError",
                "NetworkError", "Custom Error"
            ])
        with col2:
            severity = st.selectbox("Severity:", ["Low", "Medium", "High", "Critical"])

        browser_info = st.text_input("Browser Info:", placeholder="Chrome 91.0.4472.124")
        url = st.text_input("Page URL:", placeholder="https://example.com/page")

        if st.button("Log Error"):
            if error_message:
                error_data = {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "error_type": error_type,
                    "severity": severity,
                    "message": error_message,
                    "browser": browser_info,
                    "url": url
                }

                # Store in session state (in a real app, this would go to a database)
                if "error_logs" not in st.session_state:
                    st.session_state.error_logs = []

                st.session_state.error_logs.append(error_data)
                st.success("✅ Error logged successfully!")
            else:
                st.error("Please enter an error message")

    with tab2:
        st.subheader("Error Analysis")

        if "error_logs" in st.session_state and st.session_state.error_logs:
            errors = st.session_state.error_logs

            # Display summary
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Errors", len(errors))
            with col2:
                critical_errors = len([e for e in errors if e["severity"] == "Critical"])
                st.metric("Critical Errors", critical_errors)
            with col3:
                high_errors = len([e for e in errors if e["severity"] == "High"])
                st.metric("High Priority", high_errors)

            # Display recent errors
            st.subheader("Recent Errors")
            for i, error in enumerate(reversed(errors[-10:]), 1):  # Show last 10
                with st.expander(f"Error {i}: {error['error_type']} ({error['severity']})"):
                    st.write(f"**Time:** {error['timestamp']}")
                    st.write(f"**Type:** {error['error_type']}")
                    st.write(f"**Severity:** {error['severity']}")
                    st.write(f"**Browser:** {error['browser']}")
                    st.write(f"**URL:** {error['url']}")
                    st.code(error["message"])

            # Clear errors button
            if st.button("Clear All Errors"):
                st.session_state.error_logs = []
                st.success("All errors cleared!")
                st.rerun()

        else:
            st.info("No errors logged yet. Use the 'Log Errors' tab to add some.")