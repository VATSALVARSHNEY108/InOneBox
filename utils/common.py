__author__ = "VATSAL VARSHNEY"
import streamlit as st
import time
import uuid
from typing import Dict, List, Any
import json
import importlib
import inspect
from difflib import SequenceMatcher


def init_session_state():
    if 'recent_tools' not in st.session_state:
        st.session_state.recent_tools = []
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'settings' not in st.session_state:
        st.session_state.settings = {
            'theme': 'light',
            'auto_save': True,
            'show_tips': True
        }


def add_to_recent(tool_name: str):
    if tool_name not in st.session_state.recent_tools:
        st.session_state.recent_tools.append(tool_name)
        if len(st.session_state.recent_tools) > 10:
            st.session_state.recent_tools.pop(0)


def add_to_history(operation: str, details: Dict[str, Any]):
    history_entry = {
        'id': str(uuid.uuid4()),
        'timestamp': time.time(),
        'operation': operation,
        'details': details
    }
    st.session_state.history.append(history_entry)
    if len(st.session_state.history) > 100:
        st.session_state.history.pop(0)


def display_tool_grid(categories: Dict[str, Any]):
    cols = st.columns(3)
    for i, (name, info) in enumerate(categories.items()):
        with cols[i % 3]:
            with st.container():
                st.markdown(f"""
                <div style="
                    border: 2px solid {info['color']};
                    border-radius: 10px;
                    padding: 20px;
                    margin: 10px 0;
                    text-align: center;
                    background-color: {info['color']}20;
                    cursor: pointer;
                ">
                    <h3 style="margin: 0; color: {info['color']};">
                        {info['icon']} {name}
                    </h3>
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"Open {name}", key=f"cat_{i}"):
                    st.session_state.selected_category = name
                    st.rerun()


def build_tool_index():
    if 'tool_index' not in st.session_state:
        tool_index = {}

        # List of all tool modules
        tool_modules = [
            'text_tools', 'image_tools', 'security_tools', 'css_tools', 'coding_tools',
            'audio_video_tools', 'file_tools', 'ai_tools', 'social_media_tools',
            'color_tools', 'web_dev_tools', 'seo_marketing_tools', 'data_tools',
            'science_math_tools'
        ]

        for module_name in tool_modules:
            try:
                # Import the module dynamically
                module = importlib.import_module(f'tools.{module_name}')

                # Get the display_tools function to extract tool_categories
                if hasattr(module, 'display_tools'):
                    # Get the source code to extract tool_categories
                    source = inspect.getsource(module.display_tools)

                    # Extract tool_categories dictionary using regex
                    import re
                    pattern = r'tool_categories\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}'
                    match = re.search(pattern, source, re.DOTALL)

                    if match:
                        try:
                            # Safely evaluate the dictionary
                            categories_str = '{' + match.group(1) + '}'
                            categories = eval(categories_str)

                            # Add tools to index
                            category_name = module_name.replace('_', ' ').title()
                            tool_index[category_name] = {
                                'module': module_name,
                                'categories': categories,
                                'tools': []
                            }

                            # Flatten all tools with their categories
                            for subcategory, tools in categories.items():
                                for tool in tools:
                                    tool_index[category_name]['tools'].append({
                                        'name': tool,
                                        'subcategory': subcategory,
                                        'module': module_name,
                                        'main_category': category_name
                                    })

                        except Exception as e:
                            st.error(f"Error parsing {module_name}: {e}")

            except ImportError:
                continue

        st.session_state.tool_index = tool_index

    return st.session_state.tool_index


def fuzzy_match_score(query: str, text: str) -> float:
    """Calculate fuzzy match score between query and text"""
    query = query.lower().strip()
    text = text.lower().strip()

    # Exact match gets highest score
    if query in text:
        return 1.0 if query == text else 0.8

    # Use sequence matcher for fuzzy matching
    return SequenceMatcher(None, query, text).ratio()


def search_tools(query: str, categories: Dict[str, Any], filter_category: str = "All") -> Dict[
    str, List[Dict[str, str]]]:
    """Enhanced search for tools across all categories with fuzzy matching and filtering"""
    if not query or len(query.strip()) < 2:
        return {}

    results = {}
    query = query.lower().strip()
    tool_index = build_tool_index()

    # Search through all tools
    all_matches = []

    for category_name, category_info in tool_index.items():
        # Apply category filter
        if filter_category != "All" and category_name != filter_category:
            continue

        for tool in category_info['tools']:
            # Calculate match scores
            name_score = fuzzy_match_score(query, tool['name'])
            subcategory_score = fuzzy_match_score(query, tool['subcategory'])
            category_score = fuzzy_match_score(query, category_name)

            # Combined score with weights
            total_score = (name_score * 0.6) + (subcategory_score * 0.3) + (category_score * 0.1)

            if total_score > 0.3:  # Minimum threshold
                all_matches.append({
                    'name': tool['name'],
                    'description': f"{tool['subcategory']} tool from {category_name}",
                    'category': category_name,
                    'subcategory': tool['subcategory'],
                    'module': tool['module'],
                    'score': total_score,
                    'id': f"{tool['module']}_{tool['name'].lower().replace(' ', '_')}"
                })

    # Sort by score (highest first)
    all_matches.sort(key=lambda x: x['score'], reverse=True)

    # Group results by category (top 20 results)
    for match in all_matches[:20]:
        category = match['category']
        if category not in results:
            results[category] = []
        results[category].append(match)

    return results


def get_search_suggestions(query: str) -> List[str]:
    if not query or len(query.strip()) < 1:
        return []

    suggestions = []
    tool_index = build_tool_index()

    # Common search terms
    common_terms = [
        "password", "generator", "converter", "validator", "formatter", "analyzer",
        "compressor", "editor", "calculator", "tester", "checker", "optimizer",
        "color", "image", "text", "code", "api", "database", "file", "security",
        "css", "html", "json", "email", "url", "qr code", "hash", "base64"
    ]

    # Add matching tool names and common terms
    query_lower = query.lower()
    for category_name, category_info in tool_index.items():
        for tool in category_info['tools']:
            tool_name_lower = tool['name'].lower()
            if query_lower in tool_name_lower and tool['name'] not in suggestions:
                suggestions.append(tool['name'])

    # Add matching common terms
    for term in common_terms:
        if query_lower in term and term not in suggestions:
            suggestions.append(term)

    return suggestions[:5]  # Return top 5 suggestions


def navigate_to_tool(category: str, tool_name: str):
    # Set the selected category in session state
    st.session_state.selected_category = category

    # Store the selected tool for the category
    st.session_state[f"selected_tool_{category.lower().replace(' ', '_')}"] = tool_name

    # Rerun to update the interface
    st.rerun()


def show_progress_bar(text: str, duration: int = 3):
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(duration * 10):
        progress = (i + 1) / (duration * 10)
        progress_bar.progress(progress)
        status_text.text(f"{text}... {int(progress * 100)}%")
        time.sleep(0.1)

    status_text.text(f"{text} completed!")
    return True


def create_download_button(data: bytes, filename: str, mime_type: str = "application/octet-stream"):
    return st.download_button(
        label=f"📥 Download {filename}",
        data=data,
        file_name=filename,
        mime=mime_type
    )


def display_comparison(original_data, processed_data, title: str = "Comparison"):
    st.subheader(title)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Before:**")
        if isinstance(original_data, str):
            st.text_area("Original", original_data, height=200, disabled=True)
        else:
            st.write(original_data)

    with col2:
        st.markdown("**After:**")
        if isinstance(processed_data, str):
            st.text_area("Processed", processed_data, height=200, disabled=True)
        else:
            st.write(processed_data)


def validate_file_type(uploaded_file, allowed_types: List[str]) -> bool:
    if uploaded_file is None:
        return False

    file_extension = uploaded_file.name.split('.')[-1].lower()
    return file_extension in allowed_types


def format_bytes(bytes_value: int) -> str:
    bytes_float = float(bytes_value)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_float < 1024.0:
            return f"{bytes_float:.1f} {unit}"
        bytes_float /= 1024.0
    return f"{bytes_float:.1f} TB"


def show_error_message(error: str, details: str = ""):
    st.error(f"❌ {error}")
    if details:
        st.write(f"Details: {details}")


def show_success_message(message: str):
    st.success(f"✅ {message}")


def show_info_message(message: str):
    st.info(f"ℹ️ {message}")


def create_tool_header(title: str, description: str = "", icon: str = "🛠️"):
    st.markdown(f"## {icon} {title}")
    st.markdown("---")


def save_to_favorites(tool_name: str, settings: Dict[str, Any]):
    favorite = {
        'id': str(uuid.uuid4()),
        'name': tool_name,
        'settings': settings,
        'timestamp': int(time.time())
    }
    st.session_state.favorites.append(favorite)
    show_success_message(f"Saved {tool_name} to favorites!")


def load_from_favorites():
    """Load and display favorite configurations"""
    if not st.session_state.favorites:
        st.info("No favorites saved yet.")
        return None

    favorite_names = [f"{fav['name']} ({time.strftime('%Y-%m-%d', time.localtime(fav['timestamp']))})"
                      for fav in st.session_state.favorites]

    selected = st.selectbox("Select favorite configuration:", favorite_names)
    if selected:
        index = favorite_names.index(selected)
        return st.session_state.favorites[index]
    return None

