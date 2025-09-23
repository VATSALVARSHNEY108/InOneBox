__author__ = "VATSAL VARSHNEY"
import streamlit as st
import sys
from pathlib import Path

from connect import display_connect_page

# Add project root to Python path for local development
project_root = Path(__file__).parent.absolute()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.common import init_session_state, display_tool_grid, search_tools, navigate_to_tool, get_search_suggestions
from tools import (
    text_tools, image_tools, security_tools, css_tools, coding_tools,
    audio_video_tools, file_tools, ai_tools, social_media_tools,
    color_tools, web_dev_tools, seo_marketing_tools, data_tools,
    science_math_tools
)

# Configure page
st.set_page_config(
    page_title="Ultimate All-in-One Digital Toolkit",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Initialize session state
init_session_state()

# Tool categories configuration
TOOL_CATEGORIES = {
    "AI Tools": {
        "icon": "🤖",
        "description": "Artificial intelligence and machine learning tools",
        "module": ai_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Audio/Video Tools": {
        "icon": "🎵",
        "description": "Media processing and editing tools",
        "module": audio_video_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Coding Tools": {
        "icon": "💻",
        "description": "Programming utilities and development tools",
        "module": coding_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Color Tools": {
        "icon": "🌈",
        "description": "Color palettes, converters, and design tools",
        "module": color_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "CSS Tools": {
        "icon": "🎨",
        "description": "CSS generators, validators, and design tools",
        "module": css_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Data Tools": {
        "icon": "📊",
        "description": "Data analysis and visualization tools",
        "module": data_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "File Tools": {
        "icon": "📁",
        "description": "File management and conversion utilities",
        "module": file_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Image Tools": {
        "icon": "🖼️",
        "description": "Image editing, conversion, and analysis tools",
        "module": image_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Science/Math Tools": {
        "icon": "🧮",
        "description": "Scientific calculators and mathematical tools",
        "module": science_math_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Security/Privacy Tools": {
        "icon": "🔒",
        "description": "Cybersecurity, privacy, and encryption tools",
        "module": security_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Social Media Tools": {
        "icon": "📱",
        "description": "Social media management and analytics",
        "module": social_media_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "SEO/Marketing Tools": {
        "icon": "📈",
        "description": "Search optimization and marketing analytics",
        "module": seo_marketing_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Text Tools": {
        "icon": "📝",
        "description": "Text processing, analysis, and manipulation tools",
        "module": text_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Web Developer Tools": {
        "icon": "🌐",
        "description": "Web development and testing utilities",
        "module": web_dev_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    },
    "Connect":{
        "icon": "🤪",
        "description": "Web development and testing utilities",
        "module": web_dev_tools,
        "color": "#FFFFFF",
        "background-color": "#000000"
    }
}




def main():
    # Beautiful header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1>🛠️ In One Box </h1>
        <p>वत्सल वार्ष्णेय</p>
        <div style="background: linear-gradient(45deg, #a8c8ff, #c4a7ff); 
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                    background-clip: text; font-size: 1.2rem; font-weight: 500;">
            ✨ 500+ Professional Tools  ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Top Navigation Bar
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(168, 200, 255, 0.1), rgba(196, 167, 255, 0.1)); 
                padding: 1rem; border-radius: 10px; margin-bottom: 2rem;
                border: 1px solid rgba(255, 255, 255, 0.2);">
    """, unsafe_allow_html=True)

    # Top navigation columns
    nav_col1, nav_col2 = st.columns([3,4])

    with nav_col1:
        # Search functionality with advanced features
        search_query = st.text_input("🔍 Search Tools", placeholder="Type to search...", key="search_tools")
    with nav_col2:
        # Category selection
        selected_category = st.selectbox(
            "🎯 Select Category",
            ["Dashboard", "Connect"] + list(TOOL_CATEGORIES.keys()),
            index=0 if 'selected_category' not in st.session_state else
            (["Dashboard", "Connect"] + list(TOOL_CATEGORIES.keys())).index(
                st.session_state.selected_category) if st.session_state.selected_category in (
                    ["Dashboard", "Connect"] + list(TOOL_CATEGORIES.keys())) else 0
        )

    # Display search suggestions and results
    if search_query:
        # Show search suggestions
        if len(search_query) >= 1:
            suggestions = get_search_suggestions(search_query)
            if suggestions and len(search_query) < 4:  # Show suggestions for short queries
                st.caption("💡 Suggestions: " + " • ".join([f"`{s}`" for s in suggestions]))

        # Get search results with filter
        search_results = search_tools(search_query, TOOL_CATEGORIES, search_filter)

        if search_results:
            total_results = sum(len(tools) for tools in search_results.values())
            st.markdown(f"### 🔍 Search Results ({total_results} tools found)")

            if search_filter != "All":
                st.info(f"🔍 Filtered by: **{search_filter}**")

            # Display results in a more interactive format
            for category, tools in search_results.items():
                with st.expander(f"📂 {category} ({len(tools)} tools found)", expanded=True):
                    # Create columns for better layout
                    cols = st.columns(2)
                    for i, tool in enumerate(tools):
                        with cols[i % 2]:
                            st.markdown(f"**{tool['name']}**")
                            st.caption(f"📁 {tool.get('subcategory', 'General')} • Score: {tool.get('score', 0):.2f}")

                            # Navigation button
                            if st.button(f"Open {tool['name']}", key=f"search_{tool['id']}", type="secondary"):
                                navigate_to_tool(category, tool['name'])

                            st.markdown("---")
        else:
            if len(search_query) >= 2:
                st.warning(f"🔍 No tools found for '{search_query}'" + (
                    f" in {search_filter}" if search_filter != "All" else ""))
                st.info("💡 Try using different keywords or remove the category filter")

        st.markdown("---")

    if selected_category != "Dashboard":
        st.session_state.selected_category = selected_category

    st.markdown("</div>", unsafe_allow_html=True)

    # Main content area
    if selected_category == "Connect":
        display_connect_page()
    elif selected_category == "Dashboard" or 'selected_category' not in st.session_state:
        # Dashboard view
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(168, 200, 255, 0.2), rgba(196, 167, 255, 0.2)); 
                    color: white; padding: 1.5rem; border-radius: 15px; 
                    margin: 1rem 0; text-align: center;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);">
            <h3 style="margin: 0; color: white;">✨ Welcome to the Ultimate Digital Toolkit! ✨</h3>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Select a category from the sidebar or click on any tool category below to get started.</p>
        </div>
        """, unsafe_allow_html=True)

        # Tool category grid
        display_tool_grid(TOOL_CATEGORIES)





    else:
        # Category-specific tool view
        category_info = TOOL_CATEGORIES[st.session_state.selected_category]

        # Category header
        st.header(f"{category_info['icon']} {st.session_state.selected_category}")

        # Load and display category tools
        try:
            category_info['module'].display_tools()
        except Exception as e:
            st.error(f"Error loading {st.session_state.selected_category}: {str(e)}")
            st.info("Please try refreshing the page or selecting a different category.")


if __name__ == "__main__":

    main()



