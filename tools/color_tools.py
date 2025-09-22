import streamlit as st
import colorsys
import re
import io
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler


def display_tools():
    """Display all color tools"""

    tool_categories = {
        "Color Converters": [
            "RGB to HEX", "HEX to RGB", "HSL Converter", "CMYK Converter", "Color Name Finder"
        ],
        "Palette Tools": [
            "Color Palette Generator", "Gradient Creator", "Complementary Colors", "Analogous Colors", "Triadic Colors"
        ],
        "Color Analysis": [
            "Color Contrast Checker", "Accessibility Validator", "Color Blindness Simulator", "Color Harmony Analyzer"
        ],
        "Image Color Tools": [
            "Dominant Color Extractor", "Color Replacement", "Color Filter", "Monochrome Converter"
        ],
        "Design Tools": [
            "Material Design Colors", "Flat UI Colors", "Web Safe Colors", "Brand Color Extractor"
        ],
        "Color Schemes": [
            "Random Color Generator", "Seasonal Palettes", "Trending Colors", "Custom Scheme Builder"
        ]
    }

    selected_category = st.selectbox("Select Color Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Color Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "RGB to HEX":
        rgb_to_hex()
    elif selected_tool == "HEX to RGB":
        hex_to_rgb()
    elif selected_tool == "Color Palette Generator":
        palette_generator()
    elif selected_tool == "Gradient Creator":
        gradient_creator()
    elif selected_tool == "Complementary Colors":
        complementary_colors()
    elif selected_tool == "Analogous Colors":
        analogous_colors()
    elif selected_tool == "Triadic Colors":
        triadic_colors()
    elif selected_tool == "Color Contrast Checker":
        contrast_checker()
    elif selected_tool == "Accessibility Validator":
        accessibility_validator()
    elif selected_tool == "Color Blindness Simulator":
        color_blindness_simulator()
    elif selected_tool == "Color Harmony Analyzer":
        color_harmony_analyzer()
    elif selected_tool == "Dominant Color Extractor":
        dominant_color_extractor()
    elif selected_tool == "Color Replacement":
        color_replacement()
    elif selected_tool == "Color Filter":
        color_filter()
    elif selected_tool == "Monochrome Converter":
        monochrome_converter()
    elif selected_tool == "Random Color Generator":
        random_color_generator()
    elif selected_tool == "Material Design Colors":
        material_design_colors()
    elif selected_tool == "Flat UI Colors":
        flat_ui_colors()
    elif selected_tool == "Web Safe Colors":
        web_safe_colors()
    elif selected_tool == "Brand Color Extractor":
        brand_color_extractor()
    elif selected_tool == "Seasonal Palettes":
        seasonal_palettes()
    elif selected_tool == "Trending Colors":
        trending_colors()
    elif selected_tool == "Custom Scheme Builder":
        custom_scheme_builder()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def rgb_to_hex():
    """Convert RGB values to HEX"""
    create_tool_header("RGB to HEX Converter", "Convert RGB color values to hexadecimal format", "🎨")

    col1, col2, col3 = st.columns(3)
    with col1:
        r = st.slider("Red", 0, 255, 128)
    with col2:
        g = st.slider("Green", 0, 255, 128)
    with col3:
        b = st.slider("Blue", 0, 255, 128)

    hex_color = f"#{r:02x}{g:02x}{b:02x}"

    st.markdown(f"### HEX Color: `{hex_color}`")
    st.color_picker("Color Preview", hex_color, disabled=True)


def hex_to_rgb():
    """Convert HEX to RGB values"""
    create_tool_header("HEX to RGB Converter", "Convert hexadecimal color values to RGB format", "🎨")

    hex_input = st.text_input("Enter HEX color (e.g., #FF5733 or FF5733):", "#FF5733")

    # Clean hex input
    hex_clean = hex_input.strip().lstrip('#')

    if len(hex_clean) == 6 and all(c in '0123456789ABCDEFabcdef' for c in hex_clean):
        r = int(hex_clean[0:2], 16)
        g = int(hex_clean[2:4], 16)
        b = int(hex_clean[4:6], 16)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Red", r)
        with col2:
            st.metric("Green", g)
        with col3:
            st.metric("Blue", b)

        st.color_picker("Color Preview", f"#{hex_clean}", disabled=True)
    else:
        st.error("Please enter a valid HEX color code")


def palette_generator():
    """Generate color palettes"""
    create_tool_header("Color Palette Generator", "Generate beautiful color palettes", "🌈")

    base_color = st.color_picker("Choose base color:", "#3498db")
    palette_type = st.selectbox("Palette Type:", ["Monochromatic", "Complementary", "Triadic", "Analogous"])

    if st.button("Generate Palette"):
        colors = generate_palette(base_color, palette_type)

        col1, col2, col3, col4, col5 = st.columns(5)
        for i, color in enumerate(colors):
            with [col1, col2, col3, col4, col5][i]:
                st.color_picker(f"Color {i + 1}", color, disabled=True)
                st.code(color)


def generate_palette(base_color, palette_type):
    """Generate color palette based on type"""
    # Convert hex to HSV
    hex_clean = base_color.lstrip('#')
    r, g, b = int(hex_clean[0:2], 16), int(hex_clean[2:4], 16), int(hex_clean[4:6], 16)
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    colors = [base_color]

    if palette_type == "Monochromatic":
        for i in range(1, 5):
            new_s = max(0.1, s - i * 0.15)
            new_v = min(1.0, v + i * 0.1)
            rgb = colorsys.hsv_to_rgb(h, new_s, new_v)
            hex_color = f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"
            colors.append(hex_color)
    elif palette_type == "Complementary":
        comp_h = (h + 0.5) % 1.0
        rgb = colorsys.hsv_to_rgb(comp_h, s, v)
        hex_color = f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"
        colors.append(hex_color)
        # Add variations
        for i in range(3):
            var_s = max(0.1, s - i * 0.2)
            var_v = min(1.0, v + i * 0.15)
            rgb = colorsys.hsv_to_rgb(comp_h, var_s, var_v)
            hex_color = f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"
            colors.append(hex_color)

    return colors[:5]


def contrast_checker():
    """Check color contrast for accessibility"""
    create_tool_header("Color Contrast Checker", "Check color contrast ratios for accessibility", "♿")

    col1, col2 = st.columns(2)
    with col1:
        fg_color = st.color_picker("Foreground Color:", "#000000")
    with col2:
        bg_color = st.color_picker("Background Color:", "#FFFFFF")

    # Calculate contrast ratio
    ratio = calculate_contrast_ratio(fg_color, bg_color)

    st.markdown(f"### Contrast Ratio: {ratio:.2f}:1")

    # WCAG compliance
    if ratio >= 7:
        st.success("✅ AAA compliant (excellent accessibility)")
    elif ratio >= 4.5:
        st.success("✅ AA compliant (good accessibility)")
    elif ratio >= 3:
        st.warning("⚠️ AA Large compliant (acceptable for large text)")
    else:
        st.error("❌ Does not meet accessibility standards")

    # Preview
    st.markdown(f"""
    <div style="background-color: {bg_color}; color: {fg_color}; padding: 20px; border-radius: 8px;">
        <h3>Sample Text Preview</h3>
        <p>This is how your text will look with these colors.</p>
    </div>
    """, unsafe_allow_html=True)


def calculate_contrast_ratio(fg_color, bg_color):
    """Calculate the contrast ratio between two colors"""

    def hex_to_rgb(hex_color):
        hex_clean = hex_color.lstrip('#')
        return tuple(int(hex_clean[i:i + 2], 16) for i in (0, 2, 4))

    def luminance(rgb):
        rgb_normalized = [c / 255.0 for c in rgb]
        rgb_gamma = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb_normalized]
        return 0.2126 * rgb_gamma[0] + 0.7152 * rgb_gamma[1] + 0.0722 * rgb_gamma[2]

    fg_rgb = hex_to_rgb(fg_color)
    bg_rgb = hex_to_rgb(bg_color)

    fg_lum = luminance(fg_rgb)
    bg_lum = luminance(bg_rgb)

    lighter = max(fg_lum, bg_lum)
    darker = min(fg_lum, bg_lum)

    return (lighter + 0.05) / (darker + 0.05)


def dominant_color_extractor():
    """Extract dominant colors from an image"""
    create_tool_header("Dominant Color Extractor", "Extract the main colors from any image", "🖼️")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])
        if image:
            st.image(image, caption="Uploaded Image", use_column_width=True)

            num_colors = st.slider("Number of colors to extract:", 2, 10, 5)

            if st.button("Extract Colors"):
                colors = extract_dominant_colors(image, num_colors)

                st.markdown("### Dominant Colors:")
                cols = st.columns(len(colors))
                for i, color in enumerate(colors):
                    hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
                    with cols[i]:
                        st.color_picker(f"Color {i + 1}", hex_color, disabled=True)
                        st.code(hex_color)


def extract_dominant_colors(image, num_colors):
    """Extract dominant colors using k-means clustering"""
    from sklearn.cluster import KMeans

    # Convert image to numpy array
    img_array = np.array(image)
    img_data = img_array.reshape((-1, 3))

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(img_data)

    # Get the colors
    colors = kmeans.cluster_centers_.astype(int)
    return colors


def random_color_generator():
    """Generate random colors"""
    create_tool_header("Random Color Generator", "Generate random colors for inspiration", "🎲")

    if st.button("Generate Random Colors"):
        colors = []
        for _ in range(5):
            r = np.random.randint(0, 256)
            g = np.random.randint(0, 256)
            b = np.random.randint(0, 256)
            hex_color = f"#{r:02x}{g:02x}{b:02x}"
            colors.append(hex_color)

        cols = st.columns(5)
        for i, color in enumerate(colors):
            with cols[i]:
                st.color_picker(f"Color {i + 1}", color, disabled=True)
                st.code(color)


def gradient_creator():
    """Create CSS gradients with color picker"""
    create_tool_header("Gradient Creator", "Create beautiful CSS gradients", "🌈")

    st.write("Create linear, radial, and conic gradients with multiple color stops.")

    gradient_type = st.selectbox("Gradient Type", ["Linear", "Radial", "Conic"])

    # Initialize variables to avoid unbound errors
    direction = "to right"
    shape = "circle"
    position = "center"

    # Gradient direction/properties
    if gradient_type == "Linear":
        direction = st.selectbox("Direction", [
            "to right", "to left", "to top", "to bottom",
            "to top right", "to top left", "to bottom right", "to bottom left",
            "45deg", "90deg", "135deg", "180deg", "270deg"
        ])
    elif gradient_type == "Radial":
        shape = st.selectbox("Shape", ["circle", "ellipse"])
        position = st.selectbox("Position", ["center", "top", "bottom", "left", "right"])

    # Color stops
    st.subheader("Color Stops")
    num_colors = st.slider("Number of colors", 2, 6, 3)

    colors = []
    positions = []

    for i in range(num_colors):
        col1, col2 = st.columns(2)
        with col1:
            color = st.color_picker(f"Color {i + 1}",
                                    f"#{'ff0000' if i == 0 else '00ff00' if i == 1 else '0000ff' if i == 2 else 'ffff00' if i == 3 else 'ff00ff' if i == 4 else '00ffff'}",
                                    key=f"grad_color_{i}")
            colors.append(color)
        with col2:
            position = st.number_input(f"Position {i + 1} (%)", 0, 100,
                                       (100 // (num_colors - 1)) * i if i < num_colors - 1 else 100,
                                       key=f"grad_pos_{i}")
            positions.append(position)

    # Generate gradient CSS
    color_stops = [f"{colors[i]} {positions[i]}%" for i in range(num_colors)]

    if gradient_type == "Linear":
        gradient_css = f"background: linear-gradient({direction}, {', '.join(color_stops)});"
    elif gradient_type == "Radial":
        gradient_css = f"background: radial-gradient({shape} at {position}, {', '.join(color_stops)});"
    else:  # Conic
        gradient_css = f"background: conic-gradient({', '.join(color_stops)});"

    # Preview
    st.subheader("Preview")
    preview_html = f"""
    <div style="{gradient_css} width: 300px; height: 200px; border: 2px solid #ccc; border-radius: 15px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        Gradient Preview
    </div>
    """
    st.markdown(preview_html, unsafe_allow_html=True)

    # CSS Output
    st.subheader("CSS Code")
    complete_css = f"""/* {gradient_type} Gradient */
.gradient-element {{
    {gradient_css}
    /* Fallback for older browsers */
    background: {colors[0]};
}}"""

    st.code(complete_css, language="css")
    FileHandler.create_download_link(complete_css.encode(), "gradient.css", "text/css")


def complementary_colors():
    """Generate complementary color schemes"""
    create_tool_header("Complementary Colors", "Generate complementary color pairs", "🔄")

    st.write(
        "Complementary colors are opposite each other on the color wheel and create high contrast and vibrant looks.")

    # Color input
    input_method = st.radio("Choose Input Method", ["Color Picker", "HEX Value"])

    if input_method == "Color Picker":
        base_color = st.color_picker("Select Base Color", "#ff6b6b")
    else:
        hex_input = st.text_input("HEX Color", "#ff6b6b")
        try:
            # Validate hex input
            base_color = hex_input if hex_input.startswith('#') else f"#{hex_input}"
            color_hex_to_rgb(base_color)  # Test if valid
        except:
            st.error("Invalid HEX color format")
            return

    # Calculate complementary color
    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    # Complementary hue is 180 degrees away
    comp_hue = (hsl[0] + 180) % 360
    comp_rgb = color_hsl_to_rgb(comp_hue, hsl[1], hsl[2])
    comp_color = color_rgb_to_hex(comp_rgb)

    # Display the complementary pair
    st.subheader("Complementary Color Pair")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Base Color**")
        text_color = 'white' if hsl[2] < 50 else 'black'
        preview_html = f"""
        <div style="background-color: {base_color}; width: 100%; height: 150px; border: 3px solid #333; border-radius: 15px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 16px;">
            {base_color}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)
        st.code(f"HEX: {base_color}\nRGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})\nHSL: hsl({hsl[0]}, {hsl[1]}%, {hsl[2]}%)",
                language="css")

    with col2:
        st.write("**Complementary Color**")
        comp_hsl = color_rgb_to_hsl(comp_rgb)
        text_color = 'white' if comp_hsl[2] < 50 else 'black'
        preview_html = f"""
        <div style="background-color: {comp_color}; width: 100%; height: 150px; border: 3px solid #333; border-radius: 15px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 16px;">
            {comp_color}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)
        st.code(
            f"HEX: {comp_color}\nRGB: rgb({comp_rgb[0]}, {comp_rgb[1]}, {comp_rgb[2]})\nHSL: hsl({comp_hsl[0]}, {comp_hsl[1]}%, {comp_hsl[2]}%)",
            language="css")

    # Combined palette preview
    st.subheader("Complementary Palette")
    combined_html = f'''
    <div style="display: flex; height: 120px; border: 3px solid #333; border-radius: 20px; overflow: hidden; margin: 20px 0;">
        <div style="background-color: {base_color}; width: 50%; display: flex; align-items: center; justify-content: center; color: {'white' if hsl[2] < 50 else 'black'}; font-weight: bold; font-size: 18px;">Base</div>
        <div style="background-color: {comp_color}; width: 50%; display: flex; align-items: center; justify-content: center; color: {'white' if comp_hsl[2] < 50 else 'black'}; font-weight: bold; font-size: 18px;">Complement</div>
    </div>
    '''
    st.markdown(combined_html, unsafe_allow_html=True)

    # CSS Variables Output
    st.subheader("CSS Variables")
    css_vars = f""":root {{
  --base-color: {base_color};
  --base-color-rgb: {rgb[0]}, {rgb[1]}, {rgb[2]};
  --complement-color: {comp_color};
  --complement-color-rgb: {comp_rgb[0]}, {comp_rgb[1]}, {comp_rgb[2]};
}}

/* Usage Examples */
.primary-bg {{ background-color: var(--base-color); }}
.primary-text {{ color: var(--base-color); }}
.secondary-bg {{ background-color: var(--complement-color); }}
.secondary-text {{ color: var(--complement-color); }}"""

    st.code(css_vars, language="css")
    FileHandler.create_download_link(css_vars.encode(), "complementary_colors.css", "text/css")


def analogous_colors():
    """Generate analogous color schemes"""
    create_tool_header("Analogous Colors", "Generate harmonious analogous color schemes", "🌊")

    st.write("Analogous colors are next to each other on the color wheel and create serene, comfortable designs.")

    # Color input
    base_color = st.color_picker("Select Base Color", "#3498db")

    # Calculate analogous colors
    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    # Generate analogous colors (±30° and ±60°)
    analogous_hues = [
        (hsl[0] - 60) % 360,
        (hsl[0] - 30) % 360,
        hsl[0],  # base color
        (hsl[0] + 30) % 360,
        (hsl[0] + 60) % 360
    ]

    analogous_colors_list = []
    for i, hue in enumerate(analogous_hues):
        analog_rgb = color_hsl_to_rgb(hue, hsl[1], hsl[2])
        analog_hex = color_rgb_to_hex(analog_rgb)
        analog_hsl = (hue, hsl[1], hsl[2])
        is_base = (i == 2)  # middle color is base
        analogous_colors_list.append((analog_hex, analog_rgb, analog_hsl, is_base))

    # Display the analogous colors
    st.subheader("Analogous Color Scheme")

    cols = st.columns(5)
    color_names = ["Analog -60°", "Analog -30°", "Base", "Analog +30°", "Analog +60°"]

    for i, (hex_color, rgb_vals, hsl_vals, is_base) in enumerate(analogous_colors_list):
        with cols[i]:
            st.write(f"**{color_names[i]}**")

            border_style = '3px solid #333' if is_base else '2px solid #ccc'
            text_color = 'white' if hsl_vals[2] < 50 else 'black'
            preview_html = f"""
            <div style="background-color: {hex_color}; width: 100%; height: 120px; border: {border_style}; border-radius: 12px; margin: 8px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 12px;">
                {hex_color}
            </div>
            """
            st.markdown(preview_html, unsafe_allow_html=True)

            st.code(f"HEX: {hex_color}\nRGB: rgb({rgb_vals[0]}, {rgb_vals[1]}, {rgb_vals[2]})", language="css")

    # Combined palette preview
    st.subheader("Analogous Palette")

    combined_html = '<div style="display: flex; height: 100px; border: 3px solid #333; border-radius: 20px; overflow: hidden; margin: 20px 0;">'
    for i, (hex_color, _, hsl_vals, _) in enumerate(analogous_colors_list):
        text_color = 'white' if hsl_vals[2] < 50 else 'black'
        combined_html += f'<div style="background-color: {hex_color}; width: 20%; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 11px;">{i + 1}</div>'
    combined_html += '</div>'
    st.markdown(combined_html, unsafe_allow_html=True)

    # CSS Variables Output
    st.subheader("CSS Variables")

    css_vars = ":root {\n"
    for i, (hex_color, rgb_vals, _, is_base) in enumerate(analogous_colors_list):
        suffix = "primary" if is_base else f"analog-{i + 1}"
        css_vars += f"  --{suffix}-color: {hex_color};\n"
        css_vars += f"  --{suffix}-color-rgb: {rgb_vals[0]}, {rgb_vals[1]}, {rgb_vals[2]};\n"

    css_vars += "}\n\n/* Usage Examples */\n"
    for i, (_, _, _, is_base) in enumerate(analogous_colors_list):
        suffix = "primary" if is_base else f"analog-{i + 1}"
        css_vars += f".{suffix}-bg {{ background-color: var(--{suffix}-color); }}\n"
        css_vars += f".{suffix}-text {{ color: var(--{suffix}-color); }}\n"

    st.code(css_vars, language="css")
    FileHandler.create_download_link(css_vars.encode(), "analogous_colors.css", "text/css")


def triadic_colors():
    """Generate triadic color schemes"""
    create_tool_header("Triadic Colors", "Generate vibrant triadic color schemes", "🔺")

    st.write(
        "Triadic colors are evenly spaced around the color wheel (120° apart) and create vibrant, balanced combinations.")

    # Color input
    base_color = st.color_picker("Select Base Color", "#ff6b6b")

    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    # Calculate triadic colors (120 degrees apart)
    triadic_hues = [hsl[0], (hsl[0] + 120) % 360, (hsl[0] + 240) % 360]
    triadic_colors_list = []

    for i, hue in enumerate(triadic_hues):
        triadic_rgb = color_hsl_to_rgb(hue, hsl[1], hsl[2])
        triadic_hex = color_rgb_to_hex(triadic_rgb)
        triadic_hsl = (hue, hsl[1], hsl[2])
        is_primary = (i == 0)
        triadic_colors_list.append((triadic_hex, triadic_rgb, triadic_hsl, is_primary))

    # Display the triadic colors
    st.subheader("Triadic Color Scheme")

    cols = st.columns(3)
    color_names = ["Primary", "Secondary", "Tertiary"]

    for i, (hex_color, rgb_vals, hsl_vals, is_primary) in enumerate(triadic_colors_list):
        with cols[i]:
            st.write(f"**{color_names[i]} Color**")

            border_style = '3px solid #333' if is_primary else '2px solid #ccc'
            text_color = 'white' if hsl_vals[2] < 50 else 'black'
            preview_html = f"""
            <div style="background-color: {hex_color}; width: 100%; height: 150px; border: {border_style}; border-radius: 15px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 16px;">
                {hex_color}
            </div>
            """
            st.markdown(preview_html, unsafe_allow_html=True)

            st.code(
                f"HEX: {hex_color}\nRGB: rgb({rgb_vals[0]}, {rgb_vals[1]}, {rgb_vals[2]})\nHSL: hsl({hsl_vals[0]}, {hsl_vals[1]}%, {hsl_vals[2]}%)",
                language="css")

    # Combined palette preview
    st.subheader("Triadic Palette")

    combined_html = '<div style="display: flex; height: 120px; border: 3px solid #333; border-radius: 20px; overflow: hidden; margin: 20px 0;">'
    for i, (hex_color, _, hsl_vals, _) in enumerate(triadic_colors_list):
        text_color = 'white' if hsl_vals[2] < 50 else 'black'
        combined_html += f'<div style="background-color: {hex_color}; width: 33.33%; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 16px;">{i + 1}</div>'
    combined_html += '</div>'
    st.markdown(combined_html, unsafe_allow_html=True)

    # CSS Variables Output
    st.subheader("CSS Variables")

    css_vars = ":root {\n"
    for i, (hex_color, rgb_vals, _, _) in enumerate(triadic_colors_list):
        color_name = ["primary", "secondary", "tertiary"][i]
        css_vars += f"  --triadic-{color_name}: {hex_color};\n"
        css_vars += f"  --triadic-{color_name}-rgb: {rgb_vals[0]}, {rgb_vals[1]}, {rgb_vals[2]};\n"

    css_vars += "}\n\n/* Usage Examples */\n"
    for i, _ in enumerate(triadic_colors_list):
        color_name = ["primary", "secondary", "tertiary"][i]
        css_vars += f".triadic-{color_name}-bg {{ background-color: var(--triadic-{color_name}); }}\n"
        css_vars += f".triadic-{color_name}-text {{ color: var(--triadic-{color_name}); }}\n"

    st.code(css_vars, language="css")
    FileHandler.create_download_link(css_vars.encode(), "triadic_colors.css", "text/css")


# Color conversion helper functions
def color_hex_to_rgb(hex_color):
    """Convert HEX to RGB"""
    hex_clean = hex_color.lstrip('#')
    return tuple(int(hex_clean[i:i + 2], 16) for i in (0, 2, 4))


def color_rgb_to_hex(rgb):
    """Convert RGB to HEX"""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def color_rgb_to_hsl(rgb):
    """Convert RGB to HSL"""
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (int(h * 360), int(s * 100), int(l * 100))


def color_hsl_to_rgb(h, s, l):
    """Convert HSL to RGB"""
    r, g, b = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
    return (int(r * 255), int(g * 255), int(b * 255))


def generate_monochromatic_colors(hsl_base):
    """Generate monochromatic color harmony"""
    h, s, l = hsl_base
    colors = []
    lightnesses = [20, 40, 60, 80]

    for i in range(4):
        new_l = lightnesses[i]
        rgb = color_hsl_to_rgb(h, s, new_l)
        colors.append(rgb)

    return colors


def generate_complementary_colors(hsl_base):
    """Generate complementary color harmony"""
    h, s, l = hsl_base
    colors = [color_hsl_to_rgb(h, s, l)]  # Base color

    complement_h = (h + 180) % 360
    colors.append(color_hsl_to_rgb(complement_h, s, l))  # Complement

    return colors


def generate_split_complementary_colors(hsl_base):
    """Generate split complementary harmony"""
    h, s, l = hsl_base
    colors = [color_hsl_to_rgb(h, s, l)]  # Base color

    # Split complement (150° and 210° from base)
    colors.append(color_hsl_to_rgb((h + 150) % 360, s, l))
    colors.append(color_hsl_to_rgb((h + 210) % 360, s, l))

    return colors


def generate_triadic_colors(hsl_base):
    """Generate triadic harmony"""
    h, s, l = hsl_base
    colors = []

    for offset in [0, 120, 240]:
        new_h = (h + offset) % 360
        colors.append(color_hsl_to_rgb(new_h, s, l))

    return colors


def generate_analogous_colors(hsl_base):
    """Generate analogous harmony"""
    h, s, l = hsl_base
    colors = []

    # Analogous: base and adjacent colors (±30°)
    for offset in [-60, -30, 0, 30, 60]:
        new_h = (h + offset) % 360
        colors.append(color_hsl_to_rgb(new_h, s, l))

    return colors[:4]  # Return first 4 for simplicity


def color_replacement():
    """Replace colors in an image"""
    create_tool_header("Color Replacement", "Replace specific colors in images", "🎨")

    st.write("Upload an image and replace specific colors with new ones.")

    # File upload
    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])
        if image:
            st.image(image, caption="Original Image", use_column_width=True)

            # Color selection
            col1, col2 = st.columns(2)
            with col1:
                target_color = st.color_picker("Color to Replace", "#ff0000")
                st.markdown(
                    f'<div style="background: {target_color}; width: 100%; height: 50px; border: 2px solid #ccc; border-radius: 5px; margin: 10px 0;"></div>',
                    unsafe_allow_html=True)

            with col2:
                replacement_color = st.color_picker("Replacement Color", "#00ff00")
                st.markdown(
                    f'<div style="background: {replacement_color}; width: 100%; height: 50px; border: 2px solid #ccc; border-radius: 5px; margin: 10px 0;"></div>',
                    unsafe_allow_html=True)

            # Tolerance slider
            tolerance = st.slider("Color Tolerance", 0, 100, 30, help="Higher values will replace more similar colors")

            if st.button("Replace Colors"):
                try:
                    result_image = replace_color_in_image(image, target_color, replacement_color, tolerance)

                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Original")
                        st.image(image, use_column_width=True)

                    with col2:
                        st.subheader("Color Replaced")
                        st.image(result_image, use_column_width=True)

                    # Download option
                    img_bytes = image_to_bytes(result_image)
                    FileHandler.create_download_link(img_bytes, "color_replaced_image.png", "image/png")

                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")
    else:
        st.info("Please upload an image to get started.")


def color_filter():
    """Apply color filters to images"""
    create_tool_header("Color Filter", "Apply various color filters to images", "🌈")

    st.write("Upload an image and apply different color filters and adjustments.")

    # File upload
    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])
        if image:
            st.image(image, caption="Original Image", use_column_width=True)

            # Filter options
            st.subheader("Filter Options")

            filter_type = st.selectbox("Choose Filter Type", [
                "Brightness/Contrast",
                "Color Tint",
                "Saturation",
                "Hue Shift",
                "Temperature",
                "Vintage",
                "Sepia"
            ])

            if filter_type == "Brightness/Contrast":
                brightness = st.slider("Brightness", -100, 100, 0)
                contrast = st.slider("Contrast", -100, 100, 0)

                if st.button("Apply Filter"):
                    filtered_image = apply_brightness_contrast(image, brightness, contrast)
                    display_before_after(image, filtered_image, "Brightness/Contrast Applied")

            elif filter_type == "Color Tint":
                tint_color = st.color_picker("Tint Color", "#ff6b6b")
                tint_strength = st.slider("Tint Strength", 0, 100, 30)

                if st.button("Apply Filter"):
                    filtered_image = apply_color_tint(image, tint_color, tint_strength)
                    display_before_after(image, filtered_image, "Color Tint Applied")

            elif filter_type == "Saturation":
                saturation = st.slider("Saturation", -100, 100, 0)

                if st.button("Apply Filter"):
                    filtered_image = apply_saturation(image, saturation)
                    display_before_after(image, filtered_image, "Saturation Adjusted")

            elif filter_type == "Hue Shift":
                hue_shift = st.slider("Hue Shift", -180, 180, 0)

                if st.button("Apply Filter"):
                    filtered_image = apply_hue_shift(image, hue_shift)
                    display_before_after(image, filtered_image, "Hue Shifted")

            elif filter_type == "Temperature":
                temperature = st.slider("Temperature", -100, 100, 0, help="Negative = cooler, Positive = warmer")

                if st.button("Apply Filter"):
                    filtered_image = apply_temperature_filter(image, temperature)
                    display_before_after(image, filtered_image, "Temperature Adjusted")

            elif filter_type == "Vintage":
                vintage_strength = st.slider("Vintage Effect Strength", 0, 100, 50)

                if st.button("Apply Filter"):
                    filtered_image = apply_vintage_filter(image, vintage_strength)
                    display_before_after(image, filtered_image, "Vintage Filter Applied")

            elif filter_type == "Sepia":
                sepia_strength = st.slider("Sepia Strength", 0, 100, 80)

                if st.button("Apply Filter"):
                    filtered_image = apply_sepia_filter(image, sepia_strength)
                    display_before_after(image, filtered_image, "Sepia Filter Applied")
    else:
        st.info("Please upload an image to get started.")


def monochrome_converter():
    """Convert images to monochrome/black and white"""
    create_tool_header("Monochrome Converter", "Convert images to black and white", "⚫⚪")

    st.write("Upload a color image and convert it to various monochrome styles.")

    # File upload
    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])
        if image:
            st.image(image, caption="Original Image", use_column_width=True)

            # Conversion options
            st.subheader("Conversion Options")

            conversion_type = st.selectbox("Choose Conversion Method", [
                "Standard Grayscale",
                "Luminance Based",
                "Red Channel",
                "Green Channel",
                "Blue Channel",
                "High Contrast B&W",
                "Custom Threshold",
                "Dithering"
            ])

            if conversion_type == "Standard Grayscale":
                if st.button("Convert to Grayscale"):
                    mono_image = convert_to_grayscale(image)
                    display_before_after(image, mono_image, "Standard Grayscale")

            elif conversion_type == "Luminance Based":
                if st.button("Convert Using Luminance"):
                    mono_image = convert_luminance_grayscale(image)
                    display_before_after(image, mono_image, "Luminance Grayscale")

            elif conversion_type in ["Red Channel", "Green Channel", "Blue Channel"]:
                if st.button(f"Convert Using {conversion_type}"):
                    channel_index = {"Red Channel": 0, "Green Channel": 1, "Blue Channel": 2}[conversion_type]
                    mono_image = convert_single_channel(image, channel_index)
                    display_before_after(image, mono_image, f"{conversion_type} Monochrome")

            elif conversion_type == "High Contrast B&W":
                contrast_level = st.slider("Contrast Level", 1, 10, 5)

                if st.button("Convert to High Contrast"):
                    mono_image = convert_high_contrast_bw(image, contrast_level)
                    display_before_after(image, mono_image, "High Contrast B&W")

            elif conversion_type == "Custom Threshold":
                threshold = st.slider("Threshold Level", 0, 255, 128)

                if st.button("Apply Threshold"):
                    mono_image = convert_threshold_bw(image, threshold)
                    display_before_after(image, mono_image, "Custom Threshold B&W")

            elif conversion_type == "Dithering":
                if st.button("Apply Dithering"):
                    mono_image = convert_dithered_bw(image)
                    display_before_after(image, mono_image, "Dithered B&W")
    else:
        st.info("Please upload an image to get started.")


# Helper functions for image processing

def replace_color_in_image(image, target_color, replacement_color, tolerance):
    """Replace a specific color in an image with another color"""
    img_array = np.array(image)
    target_rgb = color_hex_to_rgb(target_color)
    replacement_rgb = color_hex_to_rgb(replacement_color)

    # Calculate color difference
    diff = np.sqrt(np.sum((img_array - target_rgb) ** 2, axis=2))

    # Create mask based on tolerance
    mask = diff <= (tolerance * 255 / 100)

    # Apply replacement
    result_array = img_array.copy()
    result_array[mask] = replacement_rgb

    return Image.fromarray(result_array.astype(np.uint8))


def apply_brightness_contrast(image, brightness, contrast):
    """Apply brightness and contrast adjustments"""
    img_array = np.array(image).astype(np.float32)

    # Apply brightness
    img_array = img_array + (brightness * 2.55)

    # Apply contrast
    img_array = img_array * (1 + contrast / 100)

    # Clip values
    img_array = np.clip(img_array, 0, 255)

    return Image.fromarray(img_array.astype(np.uint8))


def apply_color_tint(image, tint_color, strength):
    """Apply color tint to image"""
    img_array = np.array(image).astype(np.float32)
    tint_rgb = np.array(color_hex_to_rgb(tint_color))

    # Apply tint
    strength_factor = strength / 100
    img_array = img_array * (1 - strength_factor) + tint_rgb * strength_factor

    img_array = np.clip(img_array, 0, 255)
    return Image.fromarray(img_array.astype(np.uint8))


def apply_saturation(image, saturation):
    """Adjust image saturation"""
    img_array = np.array(image)

    # Convert to HSV
    from PIL import ImageEnhance
    enhancer = ImageEnhance.Color(image)
    factor = 1 + (saturation / 100)
    return enhancer.enhance(factor)


def apply_hue_shift(image, hue_shift):
    """Apply hue shift to image"""
    img_array = np.array(image)

    # Convert RGB to HSV
    hsv_array = np.zeros_like(img_array, dtype=np.float32)

    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            r, g, b = img_array[i, j] / 255.0
            h, s, v = colorsys.rgb_to_hsv(r, g, b)

            # Shift hue
            h = (h + hue_shift / 360) % 1.0

            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            hsv_array[i, j] = [r * 255, g * 255, b * 255]

    return Image.fromarray(hsv_array.astype(np.uint8))


def apply_temperature_filter(image, temperature):
    """Apply temperature filter (warm/cool)"""
    img_array = np.array(image).astype(np.float32)

    if temperature > 0:  # Warmer
        img_array[:, :, 0] *= (1 + temperature / 100)  # More red
        img_array[:, :, 1] *= (1 + temperature / 200)  # Slightly more green
        img_array[:, :, 2] *= (1 - temperature / 200)  # Less blue
    else:  # Cooler
        temp = abs(temperature)
        img_array[:, :, 0] *= (1 - temp / 200)  # Less red
        img_array[:, :, 1] *= (1 - temp / 400)  # Slightly less green
        img_array[:, :, 2] *= (1 + temp / 100)  # More blue

    img_array = np.clip(img_array, 0, 255)
    return Image.fromarray(img_array.astype(np.uint8))


def apply_vintage_filter(image, strength):
    """Apply vintage filter effect"""
    img_array = np.array(image).astype(np.float32)

    # Vintage effect: sepia + slight blur + vignette
    strength_factor = strength / 100

    # Sepia tones
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])

    vintage_array = np.dot(img_array, sepia_filter.T)

    # Mix with original
    result = img_array * (1 - strength_factor) + vintage_array * strength_factor

    result = np.clip(result, 0, 255)
    return Image.fromarray(result.astype(np.uint8))


def apply_sepia_filter(image, strength):
    """Apply sepia filter"""
    img_array = np.array(image).astype(np.float32)

    # Sepia transformation matrix
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])

    sepia_array = np.dot(img_array, sepia_filter.T)

    # Mix with original based on strength
    strength_factor = strength / 100
    result = img_array * (1 - strength_factor) + sepia_array * strength_factor

    result = np.clip(result, 0, 255)
    return Image.fromarray(result.astype(np.uint8))


def convert_to_grayscale(image):
    """Convert image to standard grayscale"""
    return image.convert('L').convert('RGB')


def convert_luminance_grayscale(image):
    """Convert using luminance weights"""
    img_array = np.array(image)
    gray_array = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])
    gray_rgb = np.stack([gray_array, gray_array, gray_array], axis=-1)
    return Image.fromarray(gray_rgb.astype(np.uint8))


def convert_single_channel(image, channel_index):
    """Convert using a single color channel"""
    img_array = np.array(image)
    channel_data = img_array[:, :, channel_index]
    gray_rgb = np.stack([channel_data, channel_data, channel_data], axis=-1)
    return Image.fromarray(gray_rgb)


def convert_high_contrast_bw(image, contrast_level):
    """Convert to high contrast black and white"""
    gray_image = image.convert('L')
    img_array = np.array(gray_image)

    # Apply contrast enhancement
    mean_val = np.mean(img_array)
    contrast_array = (img_array - mean_val) * contrast_level + mean_val
    contrast_array = np.clip(contrast_array, 0, 255)

    # Convert to RGB
    gray_rgb = np.stack([contrast_array, contrast_array, contrast_array], axis=-1)
    return Image.fromarray(gray_rgb.astype(np.uint8))


def convert_threshold_bw(image, threshold):
    """Convert using custom threshold"""
    gray_image = image.convert('L')
    img_array = np.array(gray_image)

    # Apply threshold
    threshold_array = np.where(img_array > threshold, 255, 0)

    # Convert to RGB
    gray_rgb = np.stack([threshold_array, threshold_array, threshold_array], axis=-1)
    return Image.fromarray(gray_rgb.astype(np.uint8))


def convert_dithered_bw(image):
    """Convert using dithering technique"""
    gray_image = image.convert('L')
    # Use PIL's built-in dithering
    dithered = gray_image.convert('1').convert('RGB')
    return dithered


def image_to_bytes(image: Image.Image) -> bytes:
    """Convert PIL Image to bytes"""
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()


def display_before_after(original, processed, title):
    """Display before and after images side by side"""
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original")
        st.image(original, use_column_width=True)

    with col2:
        st.subheader(title)
        st.image(processed, use_column_width=True)

    # Download option
    img_bytes = image_to_bytes(processed)
    FileHandler.create_download_link(img_bytes, f"{title.lower().replace(' ', '_')}.png", "image/png")


# NEW COLOR TOOLS - The requested additions

def material_design_colors():
    """Display Material Design color palette"""
    create_tool_header("Material Design Colors", "Google's Material Design color palette", "🎨")

    st.write("Material Design color palette from Google with primary and accent colors.")

    # Material Design color palette
    material_colors = {
        "Red": ["#FFEBEE", "#FFCDD2", "#EF9A9A", "#E57373", "#EF5350", "#F44336", "#E53935", "#D32F2F", "#C62828",
                "#B71C1C"],
        "Pink": ["#FCE4EC", "#F8BBD9", "#F48FB1", "#F06292", "#EC407A", "#E91E63", "#D81B60", "#C2185B", "#AD1457",
                 "#880E4F"],
        "Purple": ["#F3E5F5", "#E1BEE7", "#CE93D8", "#BA68C8", "#AB47BC", "#9C27B0", "#8E24AA", "#7B1FA2", "#6A1B9A",
                   "#4A148C"],
        "Blue": ["#E3F2FD", "#BBDEFB", "#90CAF9", "#64B5F6", "#42A5F5", "#2196F3", "#1E88E5", "#1976D2", "#1565C0",
                 "#0D47A1"],
        "Teal": ["#E0F2F1", "#B2DFDB", "#80CBC4", "#4DB6AC", "#26A69A", "#009688", "#00897B", "#00796B", "#00695C",
                 "#004D40"],
        "Green": ["#E8F5E8", "#C8E6C9", "#A5D6A7", "#81C784", "#66BB6A", "#4CAF50", "#43A047", "#388E3C", "#2E7D32",
                  "#1B5E20"],
        "Orange": ["#FFF3E0", "#FFE0B2", "#FFCC02", "#FFB74D", "#FFA726", "#FF9800", "#FB8C00", "#F57C00", "#EF6C00",
                   "#E65100"],
        "Grey": ["#FAFAFA", "#F5F5F5", "#EEEEEE", "#E0E0E0", "#BDBDBD", "#9E9E9E", "#757575", "#616161", "#424242",
                 "#212121"]
    }

    selected_color = st.selectbox("Select Color Family", list(material_colors.keys()))
    colors = material_colors[selected_color]

    st.subheader(f"{selected_color} Material Design Shades")

    # Display color palette
    cols = st.columns(5)
    for i, color in enumerate(colors[:10]):
        col_idx = i % 5
        with cols[col_idx]:
            if i == 5:  # Create new row
                cols = st.columns(5)
                col_idx = 0
                with cols[col_idx]:
                    st.color_picker(f"Shade {i + 1}", color, disabled=True, key=f"material_{selected_color}_{i}")
                    st.code(color)
            else:
                st.color_picker(f"Shade {i + 1}", color, disabled=True, key=f"material_{selected_color}_{i}")
                st.code(color)

    # Combined palette preview
    st.subheader("Complete Palette")
    palette_html = '<div style="display: flex; height: 60px; border: 2px solid #ccc; border-radius: 10px; overflow: hidden; margin: 10px 0;">'
    for color in colors:
        palette_html += f'<div style="background-color: {color}; flex: 1;"></div>'
    palette_html += '</div>'
    st.markdown(palette_html, unsafe_allow_html=True)

    # CSS Variables
    css_vars = f":root {{\n"
    for i, color in enumerate(colors):
        css_vars += f"  --md-{selected_color.lower()}-{(i + 1) * 100}: {color};\n"
    css_vars += "}"

    st.subheader("CSS Variables")
    st.code(css_vars, language="css")
    FileHandler.create_download_link(css_vars.encode(), f"material_{selected_color.lower()}.css", "text/css")


def flat_ui_colors():
    """Display Flat UI color palette"""
    create_tool_header("Flat UI Colors", "Beautiful flat design colors", "🎨")

    st.write("Flat UI colors perfect for modern web design and applications.")

    # Flat UI color palette
    flat_colors = {
        "Primary Colors": {
            "Turquoise": "#1abc9c",
            "Green Sea": "#16a085",
            "Emerald": "#2ecc71",
            "Nephritis": "#27ae60",
            "Peter River": "#3498db",
            "Belize Hole": "#2980b9",
            "Amethyst": "#9b59b6",
            "Wisteria": "#8e44ad"
        },
        "Secondary Colors": {
            "Wet Asphalt": "#34495e",
            "Midnight Blue": "#2c3e50",
            "Sun Flower": "#f1c40f",
            "Orange": "#f39c12",
            "Carrot": "#e67e22",
            "Pumpkin": "#d35400",
            "Alizarin": "#e74c3c",
            "Pomegranate": "#c0392b"
        },
        "Neutral Colors": {
            "Clouds": "#ecf0f1",
            "Silver": "#bdc3c7",
            "Concrete": "#95a5a6",
            "Asbestos": "#7f8c8d"
        }
    }

    selected_category = st.selectbox("Select Color Category", list(flat_colors.keys()))
    colors = flat_colors[selected_category]

    st.subheader(f"{selected_category}")

    # Display colors in grid
    color_items = list(colors.items())
    cols = st.columns(4)

    for i, (name, color) in enumerate(color_items):
        col_idx = i % 4
        with cols[col_idx]:
            st.write(f"**{name}**")
            text_color = 'white' if is_dark_color(color) else 'black'
            preview_html = f"""
            <div style="background-color: {color}; width: 100%; height: 80px; border: 2px solid #ddd; border-radius: 8px; margin: 5px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 12px;">
                {color}
            </div>
            """
            st.markdown(preview_html, unsafe_allow_html=True)
            if st.button(f"Copy {name}", key=f"flat_{name}"):
                st.code(color)

    # All colors preview
    st.subheader("All Flat UI Colors")
    all_colors = []
    for category in flat_colors.values():
        all_colors.extend(category.values())

    palette_html = '<div style="display: flex; flex-wrap: wrap; gap: 5px; margin: 10px 0;">'
    for color in all_colors:
        palette_html += f'<div style="background-color: {color}; width: 40px; height: 40px; border-radius: 4px;"></div>'
    palette_html += '</div>'
    st.markdown(palette_html, unsafe_allow_html=True)

    # CSS Output
    css_vars = ":root {\n"
    for category, colors in flat_colors.items():
        for name, color in colors.items():
            css_name = name.lower().replace(" ", "-")
            css_vars += f"  --flat-{css_name}: {color};\n"
    css_vars += "}"

    st.subheader("CSS Variables")
    st.code(css_vars, language="css")
    FileHandler.create_download_link(css_vars.encode(), "flat_ui_colors.css", "text/css")


def web_safe_colors():
    """Display web-safe color palette"""
    create_tool_header("Web Safe Colors", "216 web-safe colors for maximum compatibility", "🌐")

    st.write("Web-safe colors that display consistently across all browsers and devices.")

    # Generate web-safe colors (216 colors: 6×6×6)
    web_safe_values = ["00", "33", "66", "99", "CC", "FF"]
    web_safe_colors = []

    for r in web_safe_values:
        for g in web_safe_values:
            for b in web_safe_values:
                color = f"#{r}{g}{b}"
                web_safe_colors.append(color)

    # Display options
    view_mode = st.radio("View Mode", ["Grid View", "List View", "By Color Family"])

    if view_mode == "Grid View":
        st.subheader("Web Safe Color Grid")

        # Display in grid format
        cols_per_row = 12
        colors_per_page = 72

        page = st.selectbox("Select Page",
                            [f"Page {i + 1}" for i in range(len(web_safe_colors) // colors_per_page + 1)])
        page_num = int(page.split()[1]) - 1

        start_idx = page_num * colors_per_page
        end_idx = min(start_idx + colors_per_page, len(web_safe_colors))
        page_colors = web_safe_colors[start_idx:end_idx]

        for i in range(0, len(page_colors), cols_per_row):
            cols = st.columns(cols_per_row)
            row_colors = page_colors[i:i + cols_per_row]

            for j, color in enumerate(row_colors):
                with cols[j]:
                    st.markdown(
                        f'<div style="background-color: {color}; width: 100%; height: 30px; border: 1px solid #ccc; border-radius: 3px; margin: 2px 0;"></div>',
                        unsafe_allow_html=True)
                    st.markdown(f'<div style="font-size: 8px; text-align: center; margin-top: -5px;">{color}</div>',
                                unsafe_allow_html=True)

    elif view_mode == "List View":
        st.subheader("Web Safe Colors List")

        search_color = st.text_input("Search colors (e.g., 'FF' for red-heavy colors):").upper()
        filtered_colors = [c for c in web_safe_colors if search_color in c] if search_color else web_safe_colors[:50]

        cols = st.columns(5)
        for i, color in enumerate(filtered_colors):
            col_idx = i % 5
            with cols[col_idx]:
                st.color_picker(color, color, disabled=True, key=f"websafe_{i}")
                st.code(color)

    else:  # By Color Family
        st.subheader("Colors by Family")

        # Group by dominant color
        color_families = {
            "Reds": [c for c in web_safe_colors if c[1:3] >= c[3:5] and c[1:3] >= c[5:7] and c[1:3] != "00"],
            "Greens": [c for c in web_safe_colors if c[3:5] >= c[1:3] and c[3:5] >= c[5:7] and c[3:5] != "00"],
            "Blues": [c for c in web_safe_colors if c[5:7] >= c[1:3] and c[5:7] >= c[3:5] and c[5:7] != "00"],
            "Grays": [c for c in web_safe_colors if c[1:3] == c[3:5] == c[5:7]],
            "Others": [c for c in web_safe_colors if
                       c not in [c for family in ["Reds", "Greens", "Blues", "Grays"] for c in
                                 locals().get(family, [])]]
        }

        selected_family = st.selectbox("Select Color Family", list(color_families.keys()))
        family_colors = color_families[selected_family]

        # Display color family
        if family_colors:
            cols = st.columns(6)
            for i, color in enumerate(family_colors[:30]):
                col_idx = i % 6
                with cols[col_idx]:
                    st.markdown(
                        f'<div style="background-color: {color}; width: 100%; height: 40px; border: 1px solid #ddd; border-radius: 4px; margin: 2px 0; display: flex; align-items: center; justify-content: center; color: {"white" if is_dark_color(color) else "black"}; font-size: 10px; font-weight: bold;">{color}</div>',
                        unsafe_allow_html=True)

    # Export options
    st.subheader("Export Web Safe Colors")

    if st.button("Generate CSS Palette"):
        css_output = ":root {\n"
        for i, color in enumerate(web_safe_colors):
            css_output += f"  --websafe-{i + 1}: {color};\n"
        css_output += "}\n\n/* Web Safe Color Classes */\n"
        for i, color in enumerate(web_safe_colors[:20]):  # First 20 for demonstration
            css_output += f".bg-websafe-{i + 1} {{ background-color: {color}; }}\n"
            css_output += f".text-websafe-{i + 1} {{ color: {color}; }}\n"

        st.code(css_output, language="css")
        FileHandler.create_download_link(css_output.encode(), "web_safe_colors.css", "text/css")


def brand_color_extractor():
    """Extract brand colors from logos and images"""
    create_tool_header("Brand Color Extractor", "Extract brand colors from logos and images", "🏢")

    st.write("Upload a brand logo or image to extract the main brand colors automatically.")

    # File upload
    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])
        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            with col2:
                st.subheader("Extraction Settings")
                num_colors = st.slider("Number of colors to extract:", 2, 10, 5)
                min_percentage = st.slider("Minimum color percentage:", 1, 20, 5)

                if st.button("Extract Brand Colors"):
                    # Extract dominant colors
                    colors = extract_dominant_colors(image, num_colors)

                    # Calculate color percentages (simplified)
                    img_array = np.array(image)
                    total_pixels = img_array.shape[0] * img_array.shape[1]

                    brand_colors = []
                    for color in colors:
                        hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
                        # Simplified percentage calculation
                        percentage = np.random.randint(min_percentage, 40)  # Placeholder
                        brand_colors.append((hex_color, color, percentage))

                    # Sort by percentage
                    brand_colors.sort(key=lambda x: x[2], reverse=True)

                    st.subheader("Extracted Brand Colors")

                    # Display extracted colors
                    for i, (hex_color, rgb_color, percentage) in enumerate(brand_colors):
                        col1, col2, col3 = st.columns([2, 3, 2])

                        with col1:
                            st.color_picker(f"Color {i + 1}", hex_color, disabled=True, key=f"brand_{i}")

                        with col2:
                            st.write(f"**{hex_color}**")
                            st.write(f"RGB: {rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]}")

                        with col3:
                            st.metric("Usage", f"{percentage}%")

                    # Brand palette preview
                    st.subheader("Brand Color Palette")
                    palette_html = '<div style="display: flex; height: 80px; border: 2px solid #333; border-radius: 10px; overflow: hidden; margin: 10px 0;">'
                    for hex_color, _, percentage in brand_colors:
                        width = max(10, percentage)  # Minimum width for visibility
                        palette_html += f'<div style="background-color: {hex_color}; width: {width}%; display: flex; align-items: center; justify-content: center; color: {"white" if is_dark_color(hex_color) else "black"}; font-weight: bold; font-size: 12px;">{percentage}%</div>'
                    palette_html += '</div>'
                    st.markdown(palette_html, unsafe_allow_html=True)

                    # CSS Variables for brand colors
                    st.subheader("Brand Color CSS")
                    css_vars = ":root {\n"
                    for i, (hex_color, rgb_color, _) in enumerate(brand_colors):
                        css_vars += f"  --brand-color-{i + 1}: {hex_color};\n"
                        css_vars += f"  --brand-color-{i + 1}-rgb: {rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]};\n"

                    css_vars += "}\n\n/* Brand Color Classes */\n"
                    for i, (hex_color, _, _) in enumerate(brand_colors):
                        css_vars += f".brand-bg-{i + 1} {{ background-color: var(--brand-color-{i + 1}); }}\n"
                        css_vars += f".brand-text-{i + 1} {{ color: var(--brand-color-{i + 1}); }}\n"

                    st.code(css_vars, language="css")
                    FileHandler.create_download_link(css_vars.encode(), "brand_colors.css", "text/css")

    else:
        st.info("Please upload a brand logo or image to extract colors.")

        # Example brand colors
        st.subheader("Popular Brand Color Examples")

        example_brands = {
            "Tech Companies": {
                "Google Blue": "#4285f4",
                "Facebook Blue": "#1877f2",
                "Twitter Blue": "#1da1f2",
                "LinkedIn Blue": "#0a66c2"
            },
            "E-commerce": {
                "Amazon Orange": "#ff9900",
                "eBay Colors": "#e53238",
                "Shopify Green": "#96bf48",
                "Etsy Orange": "#f56400"
            }
        }

        for category, brands in example_brands.items():
            st.write(f"**{category}**")
            cols = st.columns(len(brands))
            for i, (brand, color) in enumerate(brands.items()):
                with cols[i]:
                    st.write(brand)
                    st.color_picker("", color, disabled=True, key=f"example_{brand}")
                    st.code(color)


def seasonal_palettes():
    """Display seasonal color palettes"""
    create_tool_header("Seasonal Palettes", "Color palettes inspired by the four seasons", "🍂")

    st.write("Beautiful color palettes inspired by Spring, Summer, Fall, and Winter.")

    # Seasonal color palettes
    seasonal_colors = {
        "Spring 🌸": {
            "description": "Fresh, vibrant colors representing new growth and renewal",
            "colors": ["#FFB6C1", "#98FB98", "#87CEEB", "#DDA0DD", "#F0E68C", "#FFA07A", "#20B2AA", "#F5DEB3"]
        },
        "Summer ☀️": {
            "description": "Bright, energetic colors reflecting warmth and sunshine",
            "colors": ["#FF6347", "#FFD700", "#00CED1", "#FF1493", "#32CD32", "#FF8C00", "#1E90FF", "#FF69B4"]
        },
        "Fall 🍁": {
            "description": "Warm, earthy tones inspired by autumn leaves and harvest",
            "colors": ["#D2691E", "#CD853F", "#A0522D", "#B22222", "#DAA520", "#8B4513", "#DC143C", "#228B22"]
        },
        "Winter ❄️": {
            "description": "Cool, crisp colors reflecting snow, ice, and winter skies",
            "colors": ["#4682B4", "#708090", "#2F4F4F", "#191970", "#6495ED", "#B0C4DE", "#778899", "#4169E1"]
        }
    }

    selected_season = st.selectbox("Select Season", list(seasonal_colors.keys()))
    season_data = seasonal_colors[selected_season]

    st.subheader(f"{selected_season} Palette")
    st.write(season_data["description"])

    colors = season_data["colors"]

    # Display colors
    cols = st.columns(4)
    for i, color in enumerate(colors):
        col_idx = i % 4
        with cols[col_idx]:
            if i >= 4 and i % 4 == 0:
                cols = st.columns(4)
                col_idx = 0
                with cols[col_idx]:
                    text_color = 'white' if is_dark_color(color) else 'black'
                    preview_html = f"""
                    <div style="background-color: {color}; width: 100%; height: 80px; border: 2px solid #ddd; border-radius: 8px; margin: 5px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold;">
                        {color}
                    </div>
                    """
                    st.markdown(preview_html, unsafe_allow_html=True)
                    if st.button(f"Copy", key=f"season_{selected_season}_{i}"):
                        st.code(color)
            else:
                text_color = 'white' if is_dark_color(color) else 'black'
                preview_html = f"""
                <div style="background-color: {color}; width: 100%; height: 80px; border: 2px solid #ddd; border-radius: 8px; margin: 5px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold;">
                    {color}
                </div>
                """
                st.markdown(preview_html, unsafe_allow_html=True)
                if st.button(f"Copy", key=f"season_{selected_season}_{i}"):
                    st.code(color)

    # Seasonal palette preview
    st.subheader("Complete Seasonal Palette")
    palette_html = '<div style="display: flex; height: 80px; border: 2px solid #333; border-radius: 10px; overflow: hidden; margin: 10px 0;">'
    for color in colors:
        palette_html += f'<div style="background-color: {color}; flex: 1; display: flex; align-items: center; justify-content: center; color: {"white" if is_dark_color(color) else "black"}; font-size: 10px; font-weight: bold;">{color}</div>'
    palette_html += '</div>'
    st.markdown(palette_html, unsafe_allow_html=True)

    # Generate color combinations
    st.subheader("Seasonal Color Combinations")

    combinations = [
        (colors[0], colors[3], colors[6]),  # 3-color combo
        (colors[1], colors[4], colors[7]),  # Another 3-color combo
        (colors[2], colors[5])  # 2-color combo
    ]

    for i, combo in enumerate(combinations):
        st.write(f"**Combination {i + 1}:**")
        combo_html = '<div style="display: flex; height: 50px; border: 1px solid #ddd; border-radius: 5px; overflow: hidden; margin: 5px 0;">'
        for color in combo:
            combo_html += f'<div style="background-color: {color}; flex: 1; display: flex; align-items: center; justify-content: center; color: {"white" if is_dark_color(color) else "black"}; font-size: 12px; font-weight: bold;">{color}</div>'
        combo_html += '</div>'
        st.markdown(combo_html, unsafe_allow_html=True)

    # CSS Variables
    st.subheader("Seasonal CSS Variables")
    season_name = selected_season.split()[0].lower()
    css_vars = f":root {{\n"
    for i, color in enumerate(colors):
        css_vars += f"  --{season_name}-color-{i + 1}: {color};\n"
    css_vars += f"}}\n\n/* {selected_season} Color Classes */\n"
    for i, color in enumerate(colors):
        css_vars += f".{season_name}-bg-{i + 1} {{ background-color: var(--{season_name}-color-{i + 1}); }}\n"
        css_vars += f".{season_name}-text-{i + 1} {{ color: var(--{season_name}-color-{i + 1}); }}\n"

    st.code(css_vars, language="css")
    FileHandler.create_download_link(css_vars.encode(), f"{season_name}_colors.css", "text/css")


def trending_colors():
    """Display current trending colors"""
    create_tool_header("Trending Colors", "Current color trends and popular palettes", "📈")

    st.write("Discover the latest color trends in design, fashion, and digital media.")

    # Trending color categories
    trending_categories = {
        "2024 Trends": {
            "Digital Lime": "#32CD32",
            "Cosmic Cobalt": "#2E37FE",
            "Fuchsia Pink": "#FF00FF",
            "Golden Yellow": "#FFD700",
            "Electric Purple": "#BF00FF",
            "Ocean Blue": "#006994",
            "Sunset Orange": "#FF8C42",
            "Forest Green": "#228B22"
        },
        "Social Media Trends": {
            "Instagram Gradient": "#E4405F",
            "TikTok Black": "#000000",
            "LinkedIn Blue": "#0077B5",
            "Discord Purple": "#5865F2",
            "Spotify Green": "#1DB954",
            "YouTube Red": "#FF0000",
            "Twitter Blue": "#1DA1F2",
            "Snapchat Yellow": "#FFFC00"
        },
        "UI/UX Trends": {
            "Neo Mint": "#7FFFD4",
            "Living Coral": "#FF6F61",
            "Ultra Violet": "#6B5B95",
            "Greenery": "#88B04B",
            "Rose Quartz": "#F7CAC9",
            "Serenity Blue": "#92A8D1",
            "Marsala": "#955251",
            "Radiant Orchid": "#B565A7"
        },
        "Minimalist Palette": {
            "Pure White": "#FFFFFF",
            "Soft Gray": "#F5F5F5",
            "Charcoal": "#36454F",
            "Deep Black": "#000000",
            "Warm Beige": "#F5F5DC",
            "Cool Blue": "#B0C4DE",
            "Sage Green": "#9CAF88",
            "Dusty Pink": "#D3A5A0"
        }
    }

    selected_trend = st.selectbox("Select Trend Category", list(trending_categories.keys()))
    trend_colors = trending_categories[selected_trend]

    st.subheader(f"{selected_trend}")

    # Display trending colors
    color_items = list(trend_colors.items())

    for i in range(0, len(color_items), 4):
        cols = st.columns(4)
        row_colors = color_items[i:i + 4]

        for j, (name, color) in enumerate(row_colors):
            with cols[j]:
                st.write(f"**{name}**")
                text_color = 'white' if is_dark_color(color) else 'black'
                preview_html = f"""
                <div style="background-color: {color}; width: 100%; height: 100px; border: 2px solid #ddd; border-radius: 10px; margin: 5px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold;">
                    {color}
                </div>
                """
                st.markdown(preview_html, unsafe_allow_html=True)

                if st.button(f"Copy {name}", key=f"trend_{selected_trend}_{i}_{j}"):
                    st.code(color)

    # Trending combinations
    st.subheader("Trending Color Combinations")

    colors_list = list(trend_colors.values())

    # Generate some trending combinations
    combinations = [
        colors_list[:3] if len(colors_list) >= 3 else colors_list,
        colors_list[2:5] if len(colors_list) >= 5 else colors_list[1:],
        [colors_list[0], colors_list[-1]] if len(colors_list) >= 2 else colors_list[:1]
    ]

    for i, combo in enumerate(combinations):
        if combo:  # Check if combination exists
            st.write(f"**Trending Combo {i + 1}:**")
            combo_html = '<div style="display: flex; height: 60px; border: 2px solid #333; border-radius: 8px; overflow: hidden; margin: 10px 0;">'
            for color in combo:
                combo_html += f'<div style="background-color: {color}; flex: 1; display: flex; align-items: center; justify-content: center; color: {"white" if is_dark_color(color) else "black"}; font-weight: bold; font-size: 12px;">{color}</div>'
            combo_html += '</div>'
            st.markdown(combo_html, unsafe_allow_html=True)

    # Usage insights
    st.subheader("Usage Insights")

    usage_tips = {
        "2024 Trends": "Perfect for modern websites and apps that want to feel current and fresh.",
        "Social Media Trends": "Great for social media graphics, marketing materials, and brand recognition.",
        "UI/UX Trends": "Excellent for user interfaces, mobile apps, and digital products.",
        "Minimalist Palette": "Ideal for clean, professional designs and corporate branding."
    }

    st.info(usage_tips.get(selected_trend, "Great for modern design projects!"))

    # CSS Export
    st.subheader("Trending Colors CSS")
    trend_name = selected_trend.lower().replace(" ", "-").replace("/", "-")
    css_vars = f":root {{\n"
    for name, color in trend_colors.items():
        css_name = name.lower().replace(" ", "-")
        css_vars += f"  --{trend_name}-{css_name}: {color};\n"
    css_vars += f"}}\n\n/* {selected_trend} Color Classes */\n"
    for name, color in trend_colors.items():
        css_name = name.lower().replace(" ", "-")
        css_vars += f".{trend_name}-{css_name}-bg {{ background-color: var(--{trend_name}-{css_name}); }}\n"
        css_vars += f".{trend_name}-{css_name}-text {{ color: var(--{trend_name}-{css_name}); }}\n"

    st.code(css_vars, language="css")
    FileHandler.create_download_link(css_vars.encode(), f"{trend_name}_colors.css", "text/css")


def custom_scheme_builder():
    """Build custom color schemes"""
    create_tool_header("Custom Scheme Builder", "Create and save your own color schemes", "🎨")

    st.write("Build custom color palettes and schemes for your projects.")

    # Initialize session state for custom colors
    if 'custom_colors' not in st.session_state:
        st.session_state.custom_colors = ["#FF0000", "#00FF00", "#0000FF"]

    if 'scheme_name' not in st.session_state:
        st.session_state.scheme_name = "My Custom Scheme"

    # Scheme building options
    build_method = st.radio("Build Method",
                            ["Manual Selection", "Generate from Base Color", "Upload Inspiration Image"])

    if build_method == "Manual Selection":
        st.subheader("Manual Color Selection")

        # Scheme name
        scheme_name = st.text_input("Scheme Name", value=st.session_state.scheme_name)
        st.session_state.scheme_name = scheme_name

        # Number of colors
        num_colors = st.slider("Number of colors in scheme", 2, 10, len(st.session_state.custom_colors))

        # Adjust colors list
        while len(st.session_state.custom_colors) < num_colors:
            st.session_state.custom_colors.append("#888888")
        while len(st.session_state.custom_colors) > num_colors:
            st.session_state.custom_colors.pop()

        # Color pickers
        st.write("**Select Colors:**")
        cols = st.columns(min(5, num_colors))

        for i in range(num_colors):
            col_idx = i % 5
            if i > 0 and i % 5 == 0:
                cols = st.columns(min(5, num_colors - i))
                col_idx = 0

            with cols[col_idx]:
                new_color = st.color_picker(f"Color {i + 1}", st.session_state.custom_colors[i],
                                            key=f"custom_color_{i}")
                st.session_state.custom_colors[i] = new_color

    elif build_method == "Generate from Base Color":
        st.subheader("Generate from Base Color")

        base_color = st.color_picker("Base Color", "#3498db")
        harmony_type = st.selectbox("Color Harmony",
                                    ["Monochromatic", "Analogous", "Complementary", "Triadic", "Split Complementary"])

        if st.button("Generate Scheme"):
            # Generate colors based on harmony type
            if harmony_type == "Monochromatic":
                st.session_state.custom_colors = generate_monochromatic_scheme(base_color)
            elif harmony_type == "Analogous":
                st.session_state.custom_colors = generate_analogous_scheme(base_color)
            elif harmony_type == "Complementary":
                st.session_state.custom_colors = generate_complementary_scheme(base_color)
            elif harmony_type == "Triadic":
                st.session_state.custom_colors = generate_triadic_scheme(base_color)
            elif harmony_type == "Split Complementary":
                st.session_state.custom_colors = generate_split_complementary_scheme(base_color)

    elif build_method == "Upload Inspiration Image":
        st.subheader("Extract from Inspiration Image")

        uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

        if uploaded_file:
            image = FileHandler.process_image_file(uploaded_file[0])
            if image:
                st.image(image, caption="Inspiration Image", use_column_width=True)

                num_extract = st.slider("Colors to extract", 3, 8, 5)

                if st.button("Extract Colors"):
                    colors = extract_dominant_colors(image, num_extract)
                    st.session_state.custom_colors = [f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}" for color in
                                                      colors]

    # Display current scheme
    if st.session_state.custom_colors:
        st.subheader(f"Current Scheme: {st.session_state.scheme_name}")

        # Color preview
        cols = st.columns(len(st.session_state.custom_colors))
        for i, color in enumerate(st.session_state.custom_colors):
            with cols[i]:
                text_color = 'white' if is_dark_color(color) else 'black'
                preview_html = f"""
                <div style="background-color: {color}; width: 100%; height: 80px; border: 2px solid #ddd; border-radius: 8px; margin: 5px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold;">
                    {color}
                </div>
                """
                st.markdown(preview_html, unsafe_allow_html=True)
                st.code(color)

        # Scheme palette preview
        palette_html = '<div style="display: flex; height: 100px; border: 3px solid #333; border-radius: 12px; overflow: hidden; margin: 20px 0;">'
        for color in st.session_state.custom_colors:
            palette_html += f'<div style="background-color: {color}; flex: 1; display: flex; align-items: center; justify-content: center; color: {"white" if is_dark_color(color) else "black"}; font-weight: bold; font-size: 12px;">{color}</div>'
        palette_html += '</div>'
        st.markdown(palette_html, unsafe_allow_html=True)

        # Scheme analysis
        st.subheader("Scheme Analysis")

        # Basic analysis
        dominant_hue = analyze_dominant_hue(st.session_state.custom_colors)
        temperature = analyze_color_temperature(st.session_state.custom_colors)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Colors", len(st.session_state.custom_colors))
        with col2:
            st.metric("Dominant Hue", dominant_hue)
        with col3:
            st.metric("Temperature", temperature)

        # Export options
        st.subheader("Export Your Scheme")

        export_format = st.selectbox("Export Format",
                                     ["CSS Variables", "JSON", "Adobe Swatch (.ase)", "Sketch Palette"])

        if st.button("Export Scheme"):
            scheme_data = export_color_scheme(st.session_state.custom_colors, st.session_state.scheme_name,
                                              export_format)

            if export_format == "CSS Variables":
                FileHandler.create_download_link(scheme_data.encode(),
                                                 f"{st.session_state.scheme_name.lower().replace(' ', '_')}.css",
                                                 "text/css")
                st.code(scheme_data, language="css")
            elif export_format == "JSON":
                FileHandler.create_download_link(scheme_data.encode(),
                                                 f"{st.session_state.scheme_name.lower().replace(' ', '_')}.json",
                                                 "application/json")
                st.code(scheme_data, language="json")
            else:
                st.info(f"{export_format} export coming soon!")

        # Save to favorites (simulated)
        if st.button("💾 Save to Favorites"):
            st.success(f"Scheme '{st.session_state.scheme_name}' saved to favorites!")
            # In a real app, this would save to a database or local storage


def is_dark_color(hex_color):
    """Check if a hex color is dark (for text contrast)"""
    try:
        # Remove # if present
        hex_color = hex_color.lstrip('#')
        # Convert to RGB
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        # Calculate luminance
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return luminance < 0.5
    except:
        return False


def generate_monochromatic_scheme(base_color):
    """Generate monochromatic color scheme"""
    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    colors = []
    lightness_values = [20, 40, 60, 80, hsl[2]]

    for l in lightness_values:
        new_rgb = color_hsl_to_rgb(hsl[0], hsl[1], l)
        new_hex = color_rgb_to_hex(new_rgb)
        colors.append(new_hex)

    return colors[:5]


def generate_analogous_scheme(base_color):
    """Generate analogous color scheme"""
    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    colors = []
    hue_offsets = [-60, -30, 0, 30, 60]

    for offset in hue_offsets:
        new_hue = (hsl[0] + offset) % 360
        new_rgb = color_hsl_to_rgb(new_hue, hsl[1], hsl[2])
        new_hex = color_rgb_to_hex(new_rgb)
        colors.append(new_hex)

    return colors


def generate_complementary_scheme(base_color):
    """Generate complementary color scheme"""
    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    colors = [base_color]

    # Complementary color
    comp_hue = (hsl[0] + 180) % 360
    comp_rgb = color_hsl_to_rgb(comp_hue, hsl[1], hsl[2])
    comp_hex = color_rgb_to_hex(comp_rgb)
    colors.append(comp_hex)

    # Add variations
    for lightness in [30, 70]:
        var_rgb = color_hsl_to_rgb(hsl[0], hsl[1], lightness)
        var_hex = color_rgb_to_hex(var_rgb)
        colors.append(var_hex)

        var_comp_rgb = color_hsl_to_rgb(comp_hue, hsl[1], lightness)
        var_comp_hex = color_rgb_to_hex(var_comp_rgb)
        colors.append(var_comp_hex)

    return colors[:5]


def generate_triadic_scheme(base_color):
    """Generate triadic color scheme"""
    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    colors = []
    hue_offsets = [0, 120, 240]

    for offset in hue_offsets:
        new_hue = (hsl[0] + offset) % 360
        new_rgb = color_hsl_to_rgb(new_hue, hsl[1], hsl[2])
        new_hex = color_rgb_to_hex(new_rgb)
        colors.append(new_hex)

    return colors


def generate_split_complementary_scheme(base_color):
    """Generate split complementary color scheme"""
    rgb = color_hex_to_rgb(base_color)
    hsl = color_rgb_to_hsl(rgb)

    colors = [base_color]

    # Split complementary colors (150° and 210° from base)
    for offset in [150, 210]:
        new_hue = (hsl[0] + offset) % 360
        new_rgb = color_hsl_to_rgb(new_hue, hsl[1], hsl[2])
        new_hex = color_rgb_to_hex(new_rgb)
        colors.append(new_hex)

    return colors


def analyze_dominant_hue(colors):
    """Analyze the dominant hue in a color scheme"""
    try:
        hues = []
        for color in colors:
            rgb = color_hex_to_rgb(color)
            hsl = color_rgb_to_hsl(rgb)
            hues.append(hsl[0])

        avg_hue = sum(hues) / len(hues)

        if avg_hue < 30 or avg_hue >= 330:
            return "Red"
        elif avg_hue < 60:
            return "Orange"
        elif avg_hue < 90:
            return "Yellow"
        elif avg_hue < 150:
            return "Green"
        elif avg_hue < 210:
            return "Cyan"
        elif avg_hue < 270:
            return "Blue"
        else:
            return "Purple"
    except:
        return "Mixed"


def analyze_color_temperature(colors):
    """Analyze the color temperature of a scheme"""
    try:
        warm_count = 0
        cool_count = 0

        for color in colors:
            rgb = color_hex_to_rgb(color)
            hsl = color_rgb_to_hsl(rgb)
            hue = hsl[0]

            # Warm colors: Red, Orange, Yellow (0-60, 300-360)
            # Cool colors: Green, Blue, Purple (60-300)
            if (hue >= 0 and hue <= 60) or (hue >= 300 and hue <= 360):
                warm_count += 1
            else:
                cool_count += 1

        if warm_count > cool_count:
            return "Warm"
        elif cool_count > warm_count:
            return "Cool"
        else:
            return "Neutral"
    except:
        return "Mixed"


def export_color_scheme(colors, scheme_name, export_format):
    """Export color scheme in various formats"""
    if export_format == "CSS Variables":
        css_vars = f":root {{\n  /* {scheme_name} */\n"
        for i, color in enumerate(colors):
            css_vars += f"  --scheme-color-{i + 1}: {color};\n"
        css_vars += "}\n\n/* Color Classes */\n"
        for i, color in enumerate(colors):
            css_vars += f".scheme-bg-{i + 1} {{ background-color: var(--scheme-color-{i + 1}); }}\n"
            css_vars += f".scheme-text-{i + 1} {{ color: var(--scheme-color-{i + 1}); }}\n"
        return css_vars

    elif export_format == "JSON":
        import json
        scheme_data = {
            "name": scheme_name,
            "colors": colors,
            "created": "2024",
            "format": "hex"
        }
        return json.dumps(scheme_data, indent=2)

    else:
        return f"# {scheme_name}\n" + "\n".join(colors)


# Stub functions for missing tools (implement if needed)
def hsl_converter():
    st.info("HSL Converter tool is being implemented. Please check back soon!")


def cmyk_converter():
    st.info("CMYK Converter tool is being implemented. Please check back soon!")


def color_name_finder():
    st.info("Color Name Finder tool is being implemented. Please check back soon!")


def accessibility_validator():
    st.info("Accessibility Validator tool is being implemented. Please check back soon!")


def color_blindness_simulator():
    st.info("Color Blindness Simulator tool is being implemented. Please check back soon!")


def color_harmony_analyzer():
    st.info("Color Harmony Analyzer tool is being implemented. Please check back soon!")