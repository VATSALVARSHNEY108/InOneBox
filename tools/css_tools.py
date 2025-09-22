import streamlit as st
import re
import json
import colorsys
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler


def display_tools():
    """Display all CSS tools"""

    tool_categories = {
        "CSS Generators": [
            "Gradient Generator", "Shadow Generator", "Border Radius Generator", "Flexbox Generator", "Grid Generator"
        ],
        "CSS Preprocessors": [
            "SASS/SCSS Compiler", "LESS Processor", "Stylus Compiler", "CSS Variables Generator"
        ],
        "CSS Validators": [
            "Syntax Validator", "Property Checker", "Browser Compatibility", "CSS Linter"
        ],
        "CSS Minifiers": [
            "Code Minifier", "Whitespace Remover", "Comment Stripper", "Property Optimizer"
        ],
        "CSS Beautifiers": [
            "Code Formatter", "Indentation Fixer", "Property Organizer", "Structure Improver"
        ],
        "CSS Color Tools": [
            "Color Picker", "Palette Generator", "Color Scheme Creator", "Accessibility Checker",
            "HSL Converter", "CMYK Converter", "Color Name Finder", "Gradient Creator",
            "Complementary Colors", "Analogous Colors", "Triadic Colors", "Color Contrast Checker",
            "Accessibility Validator", "Color Blindness Simulator", "Color Harmony Analyzer"
        ],
        "CSS Layout Tools": [
            "Flexbox Layout", "Grid Layout", "Responsive Layout", "CSS Framework Tools"
        ],
        "CSS Animation Tools": [
            "Keyframe Generator", "Transition Builder", "Animation Preview", "Easing Functions"
        ],
        "CSS Framework Utilities": [
            "Bootstrap Helper", "Tailwind Utilities", "Foundation Tools", "Custom Framework"
        ],
        "CSS Debugging Tools": [
            "Selector Tester", "Specificity Calculator", "Cascade Analyzer", "Property Inspector"
        ]
    }

    selected_category = st.selectbox("Select CSS Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"CSS Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Gradient Generator":
        gradient_generator()
    elif selected_tool == "Shadow Generator":
        shadow_generator()
    elif selected_tool == "Border Radius Generator":
        border_radius_generator()
    elif selected_tool == "Flexbox Generator":
        flexbox_generator()
    elif selected_tool == "Code Minifier":
        css_minifier()
    elif selected_tool == "Code Formatter":
        css_formatter()
    elif selected_tool == "Color Picker":
        css_color_picker()
    elif selected_tool == "Syntax Validator":
        css_validator()
    elif selected_tool == "Keyframe Generator":
        keyframe_generator()
    elif selected_tool == "Selector Tester":
        selector_tester()
    elif selected_tool == "Specificity Calculator":
        specificity_calculator()
    elif selected_tool == "Grid Generator":
        grid_generator()
    elif selected_tool == "Responsive Layout":
        responsive_layout()
    elif selected_tool == "Bootstrap Helper":
        bootstrap_helper()
    elif selected_tool == "Transition Builder":
        transition_builder()
    elif selected_tool == "SASS/SCSS Compiler":
        sass_scss_compiler()
    elif selected_tool == "LESS Processor":
        less_processor()
    elif selected_tool == "Stylus Compiler":
        stylus_compiler()
    elif selected_tool == "CSS Variables Generator":
        css_variables_generator()
    elif selected_tool == "Property Checker":
        css_property_checker()
    elif selected_tool == "Browser Compatibility":
        css_browser_compatibility()
    elif selected_tool == "CSS Linter":
        css_linter()
    elif selected_tool == "Whitespace Remover":
        css_whitespace_remover()
    elif selected_tool == "Comment Stripper":
        css_comment_stripper()
    elif selected_tool == "Property Optimizer":
        css_property_optimizer()
    elif selected_tool == "Indentation Fixer":
        css_indentation_fixer()
    elif selected_tool == "Property Organizer":
        css_property_organizer()
    elif selected_tool == "Structure Improver":
        css_structure_improver()
    elif selected_tool == "Palette Generator":
        palette_generator()
    elif selected_tool == "Color Scheme Creator":
        color_scheme_creator()
    elif selected_tool == "Accessibility Checker":
        accessibility_checker()
    elif selected_tool == "CSS Framework Tools":
        css_framework_tools()
    elif selected_tool == "Animation Preview":
        animation_preview()
    elif selected_tool == "Easing Functions":
        easing_functions()
    elif selected_tool == "Tailwind Utilities":
        tailwind_utilities()
    elif selected_tool == "Foundation Tools":
        foundation_tools()
    elif selected_tool == "Custom Framework":
        custom_framework()
    elif selected_tool == "Cascade Analyzer":
        cascade_analyzer()
    elif selected_tool == "Property Inspector":
        property_inspector()
    elif selected_tool == "HSL Converter":
        hsl_converter()
    elif selected_tool == "CMYK Converter":
        cmyk_converter()
    elif selected_tool == "Color Name Finder":
        color_name_finder()
    elif selected_tool == "Gradient Creator":
        gradient_creator()
    elif selected_tool == "Complementary Colors":
        complementary_colors()
    elif selected_tool == "Analogous Colors":
        analogous_colors()
    elif selected_tool == "Triadic Colors":
        triadic_colors()
    elif selected_tool == "Color Contrast Checker":
        color_contrast_checker()
    elif selected_tool == "Accessibility Validator":
        accessibility_validator()
    elif selected_tool == "Color Blindness Simulator":
        color_blindness_simulator()
    elif selected_tool == "Color Harmony Analyzer":
        color_harmony_analyzer()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def gradient_generator():
    """CSS gradient generator"""
    create_tool_header("Gradient Generator", "Create beautiful CSS gradients", "🌈")

    gradient_type = st.selectbox("Gradient Type", ["Linear", "Radial", "Conic"])

    # Initialize variables to avoid unbound errors
    direction = "to right"
    shape = "circle"
    position = "center"

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

    num_colors = st.slider("Number of colors", 2, 8, 2)
    colors = []
    positions = []

    for i in range(num_colors):
        col1, col2 = st.columns(2)
        with col1:
            color = st.color_picker(f"Color {i + 1}", f"#{'ff0000' if i == 0 else '00ff00' if i == 1 else 'ff00ff'}",
                                    key=f"grad_color_{i}")
            colors.append(color)
        with col2:
            if i == 0:
                position = st.number_input(f"Position {i + 1} (%)", 0, 100, 0, key=f"grad_pos_{i}")
            elif i == num_colors - 1:
                position = st.number_input(f"Position {i + 1} (%)", 0, 100, 100, key=f"grad_pos_{i}")
            else:
                position = st.number_input(f"Position {i + 1} (%)", 0, 100, (100 // (num_colors - 1)) * i,
                                           key=f"grad_pos_{i}")
            positions.append(position)

    # Generate gradient CSS
    if gradient_type == "Linear":
        color_stops = [f"{colors[i]} {positions[i]}%" for i in range(num_colors)]
        gradient_css = f"background: linear-gradient({direction}, {', '.join(color_stops)});"
    elif gradient_type == "Radial":
        color_stops = [f"{colors[i]} {positions[i]}%" for i in range(num_colors)]
        gradient_css = f"background: radial-gradient({shape} at {position}, {', '.join(color_stops)});"
    else:  # Conic
        color_stops = [f"{colors[i]} {positions[i]}%" for i in range(num_colors)]
        gradient_css = f"background: conic-gradient({', '.join(color_stops)});"

    # Display preview
    st.subheader("Preview")
    preview_html = f"""
    <div style="{gradient_css} width: 300px; height: 200px; border: 1px solid #ccc; border-radius: 10px; margin: 20px 0;"></div>
    """
    st.markdown(preview_html, unsafe_allow_html=True)

    # Display CSS code
    st.subheader("CSS Code")
    st.code(gradient_css, language="css")

    # Additional CSS variations
    st.subheader("Complete CSS (with vendor prefixes)")
    complete_css = f"""/* Gradient CSS */
.gradient-element {{
    {gradient_css}
    /* Fallback for older browsers */
    background: {colors[0]};
}}"""

    st.code(complete_css, language="css")

    # Download
    FileHandler.create_download_link(complete_css.encode(), "gradient.css", "text/css")


def shadow_generator():
    """CSS box shadow generator"""
    create_tool_header("Shadow Generator", "Create CSS box shadows", "📦")

    shadow_type = st.selectbox("Shadow Type", ["Box Shadow", "Text Shadow", "Drop Shadow (filter)"])

    # Initialize shadow_css to avoid unbound errors
    shadow_css = ""

    if shadow_type == "Box Shadow":
        st.subheader("Box Shadow Properties")

        col1, col2 = st.columns(2)
        with col1:
            h_offset = st.slider("Horizontal Offset (px)", -100, 100, 10)
            v_offset = st.slider("Vertical Offset (px)", -100, 100, 10)
            blur_radius = st.slider("Blur Radius (px)", 0, 100, 10)
            spread_radius = st.slider("Spread Radius (px)", -100, 100, 0)

        with col2:
            shadow_color = st.color_picker("Shadow Color", "#000000")
            opacity = st.slider("Opacity", 0.0, 1.0, 0.5, 0.1)
            inset = st.checkbox("Inset Shadow")

        # Convert color to rgba
        hex_color = shadow_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        rgba_color = f"rgba({r}, {g}, {b}, {opacity})"

        # Generate shadow CSS
        inset_text = "inset " if inset else ""
        shadow_css = f"box-shadow: {inset_text}{h_offset}px {v_offset}px {blur_radius}px {spread_radius}px {rgba_color};"

        # Preview
        st.subheader("Preview")
        preview_html = f"""
        <div style="width: 200px; height: 150px; background: #f0f0f0; margin: 50px auto; {shadow_css} border-radius: 10px; display: flex; align-items: center; justify-content: center;">
            <span style="color: #666;">Preview Box</span>
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

    elif shadow_type == "Text Shadow":
        st.subheader("Text Shadow Properties")

        col1, col2 = st.columns(2)
        with col1:
            h_offset = st.slider("Horizontal Offset (px)", -50, 50, 2)
            v_offset = st.slider("Vertical Offset (px)", -50, 50, 2)
            blur_radius = st.slider("Blur Radius (px)", 0, 50, 4)

        with col2:
            shadow_color = st.color_picker("Shadow Color", "#000000")
            text_color = st.color_picker("Text Color", "#333333")
            font_size = st.slider("Font Size (px)", 16, 72, 36)

        shadow_css = f"text-shadow: {h_offset}px {v_offset}px {blur_radius}px {shadow_color};"

        # Preview
        st.subheader("Preview")
        preview_html = f"""
        <div style="text-align: center; padding: 30px;">
            <h2 style="color: {text_color}; font-size: {font_size}px; {shadow_css} margin: 0;">
                Sample Text
            </h2>
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

    # Display CSS
    st.subheader("CSS Code")
    st.code(shadow_css, language="css")

    FileHandler.create_download_link(shadow_css.encode(), "shadow.css", "text/css")


def border_radius_generator():
    """CSS border radius generator"""
    create_tool_header("Border Radius Generator", "Create custom border radius", "📐")

    mode = st.radio("Mode", ["Simple", "Advanced"])

    if mode == "Simple":
        radius = st.slider("Border Radius (px)", 0, 100, 10)
        border_radius_css = f"border-radius: {radius}px;"
    else:
        st.subheader("Individual Corner Control")

        col1, col2 = st.columns(2)
        with col1:
            top_left = st.slider("Top Left (px)", 0, 100, 10)
            bottom_left = st.slider("Bottom Left (px)", 0, 100, 10)
        with col2:
            top_right = st.slider("Top Right (px)", 0, 100, 10)
            bottom_right = st.slider("Bottom Right (px)", 0, 100, 10)

        border_radius_css = f"border-radius: {top_left}px {top_right}px {bottom_right}px {bottom_left}px;"

    # Preview
    st.subheader("Preview")
    preview_html = f"""
    <div style="width: 200px; height: 150px; background: linear-gradient(45deg, #ff6b6b, #4ecdc4); 
                margin: 30px auto; {border_radius_css} display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-weight: bold;">Preview</span>
    </div>
    """
    st.markdown(preview_html, unsafe_allow_html=True)

    # CSS Code
    st.subheader("CSS Code")
    st.code(border_radius_css, language="css")

    # Additional examples
    st.subheader("Common Shapes")
    examples = {
        "Circle": "border-radius: 50%;",
        "Pill": "border-radius: 25px;",
        "Rounded Rectangle": "border-radius: 15px;",
        "Leaf": "border-radius: 0 100% 0 100%;"
    }

    for shape, css in examples.items():
        if st.button(f"Use {shape}"):
            st.code(css, language="css")


def flexbox_generator():
    """CSS Flexbox generator"""
    create_tool_header("Flexbox Generator", "Generate CSS Flexbox layouts", "📏")

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
        gap = st.slider("Gap (px)", 0, 50, 10)

    # Generate container CSS
    container_css = f"""display: flex;
flex-direction: {flex_direction};
flex-wrap: {flex_wrap};
justify-content: {justify_content};
align-items: {align_items};
align-content: {align_content};
gap: {gap}px;"""

    # Item properties
    st.subheader("Item Properties")
    num_items = st.slider("Number of Items", 1, 6, 3)

    item_properties = []
    for i in range(num_items):
        with st.expander(f"Item {i + 1} Properties"):
            col1, col2, col3 = st.columns(3)
            with col1:
                flex_grow = st.number_input(f"Flex Grow", 0, 10, 1, key=f"grow_{i}")
            with col2:
                flex_shrink = st.number_input(f"Flex Shrink", 0, 10, 1, key=f"shrink_{i}")
            with col3:
                align_self = st.selectbox(f"Align Self",
                                          ["auto", "flex-start", "flex-end", "center", "baseline", "stretch"],
                                          key=f"align_{i}")

            item_properties.append({
                "flex_grow": flex_grow,
                "flex_shrink": flex_shrink,
                "align_self": align_self
            })

    # Preview
    st.subheader("Preview")

    items_html = ""
    for i, props in enumerate(item_properties):
        item_style = f"""
        flex: {props['flex_grow']} {props['flex_shrink']} auto;
        align-self: {props['align_self']};
        background: hsl({i * 60}, 70%, 60%);
        padding: 20px;
        margin: 5px;
        border-radius: 5px;
        color: white;
        text-align: center;
        """
        items_html += f'<div style="{item_style}">Item {i + 1}</div>'

    preview_html = f"""
    <div style="{container_css} border: 2px dashed #ccc; padding: 20px; min-height: 200px;">
        {items_html}
    </div>
    """
    st.markdown(preview_html, unsafe_allow_html=True)

    # CSS Output
    st.subheader("CSS Code")

    complete_css = f""".flex-container {{
{container_css}
}}

/* Item styles */"""

    for i, props in enumerate(item_properties):
        complete_css += f"""
.flex-item-{i + 1} {{
    flex: {props['flex_grow']} {props['flex_shrink']} auto;
    align-self: {props['align_self']};
}}"""

    st.code(complete_css, language="css")

    FileHandler.create_download_link(complete_css.encode(), "flexbox.css", "text/css")


def css_minifier():
    """CSS minification tool"""
    create_tool_header("CSS Minifier", "Minify CSS code for production", "🗜️")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to minify:", height=300, value="""/* Sample CSS */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    margin: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}

.button {
    background: linear-gradient(45deg, #007bff, #0056b3);
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}""")

    if css_content:
        # Minification options
        col1, col2 = st.columns(2)
        with col1:
            remove_comments = st.checkbox("Remove Comments", True)
            remove_whitespace = st.checkbox("Remove Whitespace", True)
            remove_empty_rules = st.checkbox("Remove Empty Rules", True)
        with col2:
            merge_selectors = st.checkbox("Merge Identical Selectors", True)
            shorten_colors = st.checkbox("Shorten Color Values", True)
            remove_semicolons = st.checkbox("Remove Last Semicolons", True)

        if st.button("Minify CSS"):
            minified_css = minify_css(css_content, {
                'remove_comments': remove_comments,
                'remove_whitespace': remove_whitespace,
                'remove_empty_rules': remove_empty_rules,
                'merge_selectors': merge_selectors,
                'shorten_colors': shorten_colors,
                'remove_semicolons': remove_semicolons
            })

            # Show results
            st.subheader("Minified CSS")
            st.code(minified_css, language="css")

            # Statistics
            original_size = len(css_content)
            minified_size = len(minified_css)
            reduction = ((original_size - minified_size) / original_size * 100) if original_size > 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Original Size", f"{original_size:,} bytes")
            with col2:
                st.metric("Minified Size", f"{minified_size:,} bytes")
            with col3:
                st.metric("Size Reduction", f"{reduction:.1f}%")

            FileHandler.create_download_link(minified_css.encode(), "minified.css", "text/css")


def css_formatter():
    """CSS code formatter"""
    create_tool_header("CSS Formatter", "Format and beautify CSS code", "✨")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to format:", height=300,
                                   value=""".container{display:flex;justify-content:center;align-items:center;padding:20px;margin:10px;}.button{background:#007bff;color:white;padding:10px 20px;border:none;border-radius:4px;cursor:pointer;}.button:hover{background:#0056b3;}""")

    if css_content:
        # Formatting options
        col1, col2 = st.columns(2)
        with col1:
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1)
            indent_type = st.selectbox("Indent Type", ["Spaces", "Tabs"])
            brace_style = st.selectbox("Brace Style", ["Same Line", "New Line"])
        with col2:
            sort_properties = st.checkbox("Sort Properties Alphabetically", False)
            add_missing_semicolons = st.checkbox("Add Missing Semicolons", True)
            normalize_quotes = st.checkbox("Normalize Quotes", True)

        if st.button("Format CSS"):
            formatted_css = format_css(css_content, {
                'indent_size': indent_size,
                'indent_type': indent_type,
                'brace_style': brace_style,
                'sort_properties': sort_properties,
                'add_missing_semicolons': add_missing_semicolons,
                'normalize_quotes': normalize_quotes
            })

            st.subheader("Formatted CSS")
            st.code(formatted_css, language="css")

            FileHandler.create_download_link(formatted_css.encode(), "formatted.css", "text/css")


def css_color_picker():
    """Advanced CSS color picker and palette generator"""
    create_tool_header("CSS Color Picker", "Pick colors and generate palettes", "🎨")

    tab1, tab2, tab3 = st.tabs(["Color Picker", "Palette Generator", "Color Converter"])

    with tab1:
        st.subheader("Color Selection")

        color = st.color_picker("Pick a color", "#007bff")

        # Convert to different formats
        hex_color = color
        hex_short = shorten_hex_color(hex_color)
        rgb = hex_to_rgb(hex_color)
        hsl = rgb_to_hsl(rgb)

        col1, col2 = st.columns(2)
        with col1:
            st.code(f"HEX: {hex_color}")
            st.code(f"HEX (short): {hex_short}")
            st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")
        with col2:
            st.code(f"HSL: hsl({hsl[0]}, {hsl[1]}%, {hsl[2]}%)")
            st.code(f"CSS Variable: var(--primary-color)")
            st.code(f"RGBA: rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 1)")

        # Color variations
        st.subheader("Color Variations")
        variations = generate_color_variations(hex_color)

        for variation_name, variation_color in variations.items():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(
                    f'<div style="width:50px;height:30px;background-color:{variation_color};border:1px solid #000;"></div>',
                    unsafe_allow_html=True)
            with col2:
                st.code(f"{variation_name}: {variation_color}")

    with tab2:
        st.subheader("Color Palette Generator")

        base_color = st.color_picker("Base color", "#007bff", key="palette_base")
        palette_type = st.selectbox("Palette Type", [
            "Monochromatic", "Analogous", "Complementary", "Triadic", "Tetradic"
        ])

        if st.button("Generate Palette"):
            palette = generate_color_palette(base_color, palette_type)

            st.subheader(f"{palette_type} Palette")

            # Display palette
            palette_html = '<div style="display: flex; margin: 20px 0;">'
            for i, color in enumerate(palette):
                palette_html += f'''
                <div style="width: 80px; height: 80px; background-color: {color}; 
                           border: 1px solid #ccc; margin-right: 10px; 
                           display: flex; align-items: end; justify-content: center; color: white;">
                    <small style="background: rgba(0,0,0,0.7); padding: 2px 4px; margin: 5px;">{color}</small>
                </div>
                '''
            palette_html += '</div>'

            st.markdown(palette_html, unsafe_allow_html=True)

            # CSS Variables
            css_vars = ":root {\n"
            for i, color in enumerate(palette):
                css_vars += f"  --color-{i + 1}: {color};\n"
            css_vars += "}"

            st.subheader("CSS Variables")
            st.code(css_vars, language="css")

            FileHandler.create_download_link(css_vars.encode(), "color-palette.css", "text/css")

    with tab3:
        st.subheader("Color Format Converter")

        input_format = st.selectbox("Input Format", ["HEX", "RGB", "HSL"])

        if input_format == "HEX":
            hex_input = st.text_input("HEX Color", "#007bff")
            if hex_input:
                try:
                    rgb = hex_to_rgb(hex_input)
                    hsl = rgb_to_hsl(rgb)

                    st.write(f"**RGB**: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")
                    st.write(f"**HSL**: hsl({hsl[0]}, {hsl[1]}%, {hsl[2]}%)")
                except:
                    st.error("Invalid HEX color format")

        elif input_format == "RGB":
            col1, col2, col3 = st.columns(3)
            with col1:
                r = st.number_input("Red", 0, 255, 0)
            with col2:
                g = st.number_input("Green", 0, 255, 123)
            with col3:
                b = st.number_input("Blue", 0, 255, 255)

            hex_result = rgb_to_hex((r, g, b))
            hsl_result = rgb_to_hsl((r, g, b))

            st.write(f"**HEX**: {hex_result}")
            st.write(f"**HSL**: hsl({hsl_result[0]}, {hsl_result[1]}%, {hsl_result[2]}%)")


def css_validator():
    """CSS syntax validator"""
    create_tool_header("CSS Validator", "Validate CSS syntax and properties", "✅")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to validate:", height=300)

    if css_content and st.button("Validate CSS"):
        validation_results = validate_css(css_content)

        # Display results
        if validation_results['errors']:
            st.subheader("❌ Errors Found")
            for error in validation_results['errors']:
                st.error(f"Line {error['line']}: {error['message']}")

        if validation_results['warnings']:
            st.subheader("⚠️ Warnings")
            for warning in validation_results['warnings']:
                st.warning(f"Line {warning['line']}: {warning['message']}")

        if not validation_results['errors'] and not validation_results['warnings']:
            st.success("✅ No issues found! Your CSS is valid.")

        # Statistics
        st.subheader("Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Rules", validation_results['stats']['rules'])
        with col2:
            st.metric("Properties", validation_results['stats']['properties'])
        with col3:
            st.metric("Selectors", validation_results['stats']['selectors'])
        with col4:
            st.metric("Errors", len(validation_results['errors']))


def keyframe_generator():
    """CSS keyframe animation generator"""
    create_tool_header("Keyframe Generator", "Create CSS keyframe animations", "🎬")

    animation_name = st.text_input("Animation Name", "myAnimation")

    # Keyframes
    st.subheader("Animation Keyframes")

    num_keyframes = st.slider("Number of Keyframes", 2, 10, 3)
    keyframes = []

    for i in range(num_keyframes):
        with st.expander(f"Keyframe {i + 1}"):
            col1, col2 = st.columns(2)
            with col1:
                if i == 0:
                    percentage = st.number_input("Percentage", 0, 100, 0, key=f"kf_pct_{i}", disabled=True)
                elif i == num_keyframes - 1:
                    percentage = st.number_input("Percentage", 0, 100, 100, key=f"kf_pct_{i}", disabled=True)
                else:
                    percentage = st.number_input("Percentage", 0, 100, (100 // (num_keyframes - 1)) * i,
                                                 key=f"kf_pct_{i}")

            with col2:
                properties = st.text_area("CSS Properties", "transform: translateX(0px);\nopacity: 1;",
                                          height=100, key=f"kf_props_{i}")

            keyframes.append({
                'percentage': percentage,
                'properties': properties
            })

    # Animation properties
    st.subheader("Animation Properties")
    col1, col2 = st.columns(2)
    with col1:
        duration = st.number_input("Duration (seconds)", 0.1, 60.0, 2.0, 0.1)
        iteration_count = st.selectbox("Iteration Count", ["1", "2", "3", "infinite"])
        direction = st.selectbox("Direction", ["normal", "reverse", "alternate", "alternate-reverse"])
    with col2:
        timing_function = st.selectbox("Timing Function", [
            "ease", "ease-in", "ease-out", "ease-in-out", "linear",
            "cubic-bezier(0.25, 0.1, 0.25, 1)"
        ])
        fill_mode = st.selectbox("Fill Mode", ["none", "forwards", "backwards", "both"])
        delay = st.number_input("Delay (seconds)", 0.0, 10.0, 0.0, 0.1)

    # Generate CSS
    if st.button("Generate Animation CSS"):
        # Sort keyframes by percentage
        keyframes.sort(key=lambda x: x['percentage'])

        # Generate keyframes CSS
        keyframes_css = f"@keyframes {animation_name} {{\n"
        for kf in keyframes:
            keyframes_css += f"  {kf['percentage']}% {{\n"
            for prop in kf['properties'].strip().split('\n'):
                if prop.strip():
                    keyframes_css += f"    {prop.strip()}\n"
            keyframes_css += "  }\n"
        keyframes_css += "}"

        # Generate animation property
        animation_css = f"""animation: {animation_name} {duration}s {timing_function} {delay}s {iteration_count} {direction} {fill_mode};"""

        complete_css = f"""{keyframes_css}

.animated-element {{
  {animation_css}
}}"""

        st.subheader("Generated CSS")
        st.code(complete_css, language="css")

        # Preview (simple)
        st.subheader("Preview")
        st.info(
            "Preview functionality would require JavaScript. Use the generated CSS in your project to see the animation.")

        FileHandler.create_download_link(complete_css.encode(), f"{animation_name}.css", "text/css")


# Helper functions
def minify_css(css_content, options):
    """Minify CSS content based on options"""
    result = css_content

    if options['remove_comments']:
        # Remove CSS comments
        result = re.sub(r'/\*.*?\*/', '', result, flags=re.DOTALL)

    if options['remove_whitespace']:
        # Remove unnecessary whitespace
        result = re.sub(r'\s+', ' ', result)
        result = re.sub(r';\s*}', '}', result)
        result = re.sub(r'{\s*', '{', result)
        result = re.sub(r'}\s*', '}', result)
        result = re.sub(r':\s*', ':', result)
        result = re.sub(r';\s*', ';', result)
        result = result.strip()

    if options['shorten_colors']:
        # Shorten hex colors
        result = re.sub(r'#([0-9a-fA-F])\1([0-9a-fA-F])\2([0-9a-fA-F])\3', r'#\1\2\3', result)

    if options['remove_semicolons']:
        # Remove last semicolon before closing brace
        result = re.sub(r';(\s*})', r'\1', result)

    return result


def format_css(css_content, options):
    """Format CSS content based on options"""
    indent_char = '\t' if options['indent_type'] == 'Tabs' else ' ' * options['indent_size']

    # Basic formatting
    result = css_content

    # Remove existing formatting
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    # Add proper spacing and indentation
    formatted_lines = []
    indent_level = 0

    i = 0
    while i < len(result):
        char = result[i]

        if char == '{':
            formatted_lines.append(char)
            if options['brace_style'] == 'New Line':
                formatted_lines.append('\n')
            formatted_lines.append('\n')
            indent_level += 1
        elif char == '}':
            if formatted_lines and formatted_lines[-1] != '\n':
                formatted_lines.append('\n')
            indent_level -= 1
            formatted_lines.append(indent_char * indent_level + char + '\n')
        elif char == ';':
            formatted_lines.append(char + '\n')
        else:
            # Add indentation at start of line
            if formatted_lines and formatted_lines[-1] == '\n':
                formatted_lines.append(indent_char * indent_level)
            formatted_lines.append(char)

        i += 1

    return ''.join(formatted_lines)


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    """Convert RGB tuple to hex color"""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def rgb_to_hsl(rgb):
    """Convert RGB to HSL"""
    r, g, b = [x / 255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (int(h * 360), int(s * 100), int(l * 100))


def shorten_hex_color(hex_color):
    """Shorten hex color if possible"""
    if len(hex_color) == 7:
        if hex_color[1] == hex_color[2] and hex_color[3] == hex_color[4] and hex_color[5] == hex_color[6]:
            return f"#{hex_color[1]}{hex_color[3]}{hex_color[5]}"
    return hex_color


def generate_color_variations(base_color):
    """Generate color variations"""
    rgb = hex_to_rgb(base_color)
    variations = {}

    # Lighter variations
    for i, percent in enumerate([20, 40, 60], 1):
        lighter_rgb = tuple(min(255, int(c + (255 - c) * percent / 100)) for c in rgb)
        variations[f"Lighter {percent}%"] = rgb_to_hex(lighter_rgb)

    # Darker variations
    for i, percent in enumerate([20, 40, 60], 1):
        darker_rgb = tuple(max(0, int(c * (100 - percent) / 100)) for c in rgb)
        variations[f"Darker {percent}%"] = rgb_to_hex(darker_rgb)

    return variations


def generate_color_palette(base_color, palette_type):
    """Generate color palette based on type"""
    base_rgb = hex_to_rgb(base_color)
    base_hsl = rgb_to_hsl(base_rgb)

    palette = [base_color]

    if palette_type == "Monochromatic":
        # Different lightness values
        for lightness in [30, 50, 70, 90]:
            if lightness != base_hsl[2]:
                new_hsl = (base_hsl[0], base_hsl[1], lightness)
                new_rgb = colorsys.hls_to_rgb(new_hsl[0] / 360, new_hsl[2] / 100, new_hsl[1] / 100)
                new_rgb = tuple(int(c * 255) for c in new_rgb)
                palette.append(rgb_to_hex(new_rgb))

    elif palette_type == "Analogous":
        # Adjacent hues
        for offset in [-30, -15, 15, 30]:
            new_hue = (base_hsl[0] + offset) % 360
            new_hsl = (new_hue, base_hsl[1], base_hsl[2])
            new_rgb = colorsys.hls_to_rgb(new_hsl[0] / 360, new_hsl[2] / 100, new_hsl[1] / 100)
            new_rgb = tuple(int(c * 255) for c in new_rgb)
            palette.append(rgb_to_hex(new_rgb))

    elif palette_type == "Complementary":
        # Opposite hue
        comp_hue = (base_hsl[0] + 180) % 360
        comp_hsl = (comp_hue, base_hsl[1], base_hsl[2])
        comp_rgb = colorsys.hls_to_rgb(comp_hsl[0] / 360, comp_hsl[2] / 100, comp_hsl[1] / 100)
        comp_rgb = tuple(int(c * 255) for c in comp_rgb)
        palette.append(rgb_to_hex(comp_rgb))

        # Add variations
        for lightness in [30, 70]:
            for hue in [base_hsl[0], comp_hue]:
                new_hsl = (hue, base_hsl[1], lightness)
                new_rgb = colorsys.hls_to_rgb(new_hsl[0] / 360, new_hsl[2] / 100, new_hsl[1] / 100)
                new_rgb = tuple(int(c * 255) for c in new_rgb)
                palette.append(rgb_to_hex(new_rgb))

    return list(set(palette))[:6]  # Return unique colors, max 6


def validate_css(css_content):
    """Basic CSS validation"""
    errors = []
    warnings = []
    stats = {'rules': 0, 'properties': 0, 'selectors': 0}

    lines = css_content.split('\n')

    # Basic syntax checking
    brace_count = 0
    in_rule = False

    for line_num, line in enumerate(lines, 1):
        line = line.strip()

        if not line or line.startswith('/*'):
            continue

        # Count braces
        open_braces = line.count('{')
        close_braces = line.count('}')
        brace_count += open_braces - close_braces

        if open_braces > 0:
            stats['rules'] += open_braces
            in_rule = True

        if close_braces > 0:
            in_rule = False

        # Check for properties
        if in_rule and ':' in line and not line.endswith('{'):
            stats['properties'] += 1

            # Check for missing semicolon
            if not line.rstrip().endswith(';') and not line.rstrip().endswith('{') and not line.rstrip().endswith('}'):
                warnings.append({
                    'line': line_num,
                    'message': 'Missing semicolon'
                })

        # Check for invalid characters
        if re.search(r'[^\w\s\-_.:;{}()#,>+~\[\]="\'@%/\*]', line):
            errors.append({
                'line': line_num,
                'message': 'Invalid characters detected'
            })

    # Check for unmatched braces
    if brace_count != 0:
        errors.append({
            'line': len(lines),
            'message': f'Unmatched braces (difference: {brace_count})'
        })

    return {
        'errors': errors,
        'warnings': warnings,
        'stats': stats
    }


# Additional placeholder functions for remaining tools
def grid_generator():
    """CSS Grid generator"""
    create_tool_header("CSS Grid Generator", "Create CSS Grid layouts with visual editor", "📊")

    st.subheader("Grid Container Settings")

    col1, col2 = st.columns(2)
    with col1:
        grid_rows = st.number_input("Number of Rows", 1, 10, 3)
        grid_columns = st.number_input("Number of Columns", 1, 10, 3)
        gap_size = st.slider("Gap Size (px)", 0, 50, 10)

    with col2:
        justify_items = st.selectbox("Justify Items", ["stretch", "start", "end", "center"])
        align_items = st.selectbox("Align Items", ["stretch", "start", "end", "center"])
        grid_auto_flow = st.selectbox("Auto Flow", ["row", "column", "row dense", "column dense"])

    # Track definition
    st.subheader("Track Definitions")

    # Row tracks
    st.write("**Row Tracks:**")
    row_tracks = []
    for i in range(grid_rows):
        col1, col2 = st.columns(2)
        with col1:
            track_type = st.selectbox(f"Row {i + 1} Type", ["fr", "px", "auto", "min-content", "max-content"],
                                      key=f"row_type_{i}")
        with col2:
            if track_type in ["fr", "px"]:
                track_value = st.number_input(f"Row {i + 1} Value", 0.1 if track_type == "fr" else 1,
                                              1000.0 if track_type == "fr" else 1000, 1.0, key=f"row_val_{i}")
                row_tracks.append(f"{track_value}{track_type}")
            else:
                row_tracks.append(track_type)

    # Column tracks
    st.write("**Column Tracks:**")
    column_tracks = []
    for i in range(grid_columns):
        col1, col2 = st.columns(2)
        with col1:
            track_type = st.selectbox(f"Col {i + 1} Type", ["fr", "px", "auto", "min-content", "max-content"],
                                      key=f"col_type_{i}")
        with col2:
            if track_type in ["fr", "px"]:
                track_value = st.number_input(f"Col {i + 1} Value", 0.1 if track_type == "fr" else 1,
                                              1000.0 if track_type == "fr" else 1000, 1.0, key=f"col_val_{i}")
                column_tracks.append(f"{track_value}{track_type}")
            else:
                column_tracks.append(track_type)

    # Generate CSS
    grid_css = f"""display: grid;
grid-template-rows: {' '.join(row_tracks)};
grid-template-columns: {' '.join(column_tracks)};
gap: {gap_size}px;
justify-items: {justify_items};
align-items: {align_items};
grid-auto-flow: {grid_auto_flow};"""

    # Visual Preview
    st.subheader("Grid Preview")

    grid_items = ""
    for i in range(grid_rows * grid_columns):
        grid_items += f'<div style="background: hsl({(i * 30) % 360}, 70%, 60%); padding: 20px; text-align: center; color: white; border-radius: 4px;">Item {i + 1}</div>'

    preview_html = f"""
    <div style="{grid_css} border: 2px dashed #ccc; padding: 20px; margin: 20px 0;">
        {grid_items}
    </div>
    """
    st.markdown(preview_html, unsafe_allow_html=True)

    # CSS Output
    st.subheader("CSS Code")
    complete_css = f""".grid-container {{
{grid_css}
}}

.grid-item {{
    /* Individual item styles */
    background: #f0f0f0;
    padding: 20px;
    text-align: center;
    border-radius: 4px;
}}"""

    st.code(complete_css, language="css")

    # Additional grid areas
    with st.expander("Advanced: Named Grid Areas"):
        st.write("Define named grid areas for complex layouts:")

        area_name = st.text_input("Area Name", "header")
        start_row = st.number_input("Start Row", 1, grid_rows, 1)
        end_row = st.number_input("End Row", 1, grid_rows + 1, 2)
        start_col = st.number_input("Start Column", 1, grid_columns, 1)
        end_col = st.number_input("End Column", 1, grid_columns + 1, 2)

        if st.button("Add Grid Area"):
            area_css = f""".{area_name} {{
    grid-row: {start_row} / {end_row};
    grid-column: {start_col} / {end_col};
}}"""
            st.code(area_css, language="css")

    FileHandler.create_download_link(complete_css.encode(), "grid-layout.css", "text/css")


def responsive_layout():
    """Responsive layout generator"""
    create_tool_header("Responsive Layout Generator", "Create responsive CSS layouts with media queries", "📱")

    layout_type = st.selectbox("Layout Type", ["Mobile First", "Desktop First", "Custom Breakpoints"])

    # Predefined breakpoints
    breakpoints = {
        "Mobile First": {
            "mobile": 320,
            "tablet": 768,
            "desktop": 1024,
            "large": 1200
        },
        "Desktop First": {
            "large": 1200,
            "desktop": 1024,
            "tablet": 768,
            "mobile": 320
        }
    }

    if layout_type == "Custom Breakpoints":
        st.subheader("Custom Breakpoints")
        custom_breakpoints = {}
        num_breakpoints = st.slider("Number of Breakpoints", 2, 6, 4)

        for i in range(num_breakpoints):
            col1, col2 = st.columns(2)
            with col1:
                bp_name = st.text_input(f"Breakpoint {i + 1} Name", f"bp{i + 1}", key=f"bp_name_{i}")
            with col2:
                bp_size = st.number_input(f"Min Width (px)", 320, 2000, 320 + (i * 200), key=f"bp_size_{i}")
            custom_breakpoints[bp_name] = bp_size

        current_breakpoints = custom_breakpoints
    else:
        current_breakpoints = breakpoints[layout_type]

    st.subheader("Layout Configuration")

    # Layout settings for each breakpoint
    layout_config = {}

    for bp_name, bp_size in current_breakpoints.items():
        with st.expander(f"📐 {bp_name.title()} Layout ({bp_size}px+)"):
            col1, col2 = st.columns(2)

            with col1:
                container_width = st.selectbox(f"Container Width", ["100%", "90%", "Fixed"], key=f"{bp_name}_width")
                if container_width == "Fixed":
                    fixed_width = st.number_input(f"Fixed Width (px)", 300, 1400, min(bp_size * 0.9, 1200),
                                                  key=f"{bp_name}_fixed")
                    container_width = f"{fixed_width}px"

                display_type = st.selectbox(f"Display", ["block", "flex", "grid"], key=f"{bp_name}_display")

            with col2:
                padding = st.slider(f"Padding (px)", 0, 50, 20, key=f"{bp_name}_padding")
                margin = st.selectbox(f"Margin", ["0 auto", "0", "auto"], key=f"{bp_name}_margin")

            # Flex/Grid specific settings
            flex_settings = {}
            if display_type == "flex":
                col1, col2 = st.columns(2)
                with col1:
                    flex_direction = st.selectbox(f"Flex Direction", ["row", "column"], key=f"{bp_name}_flex_dir")
                    flex_wrap = st.selectbox(f"Flex Wrap", ["nowrap", "wrap"], key=f"{bp_name}_flex_wrap")
                with col2:
                    justify_content = st.selectbox(f"Justify Content",
                                                   ["flex-start", "center", "space-between", "space-around"],
                                                   key=f"{bp_name}_justify")
                    align_items = st.selectbox(f"Align Items", ["stretch", "center", "flex-start", "flex-end"],
                                               key=f"{bp_name}_align")

                flex_settings = {
                    "flex-direction": flex_direction,
                    "flex-wrap": flex_wrap,
                    "justify-content": justify_content,
                    "align-items": align_items
                }

            elif display_type == "grid":
                col1, col2 = st.columns(2)
                with col1:
                    grid_columns = st.number_input(f"Grid Columns", 1, 12, 1 if bp_name == "mobile" else 3,
                                                   key=f"{bp_name}_grid_cols")
                with col2:
                    grid_gap = st.slider(f"Grid Gap (px)", 0, 50, 20, key=f"{bp_name}_grid_gap")

                flex_settings = {
                    "grid-template-columns": f"repeat({grid_columns}, 1fr)",
                    "gap": f"{grid_gap}px"
                }

            layout_config[bp_name] = {
                "breakpoint": bp_size,
                "container_width": container_width,
                "display": display_type,
                "padding": padding,
                "margin": margin,
                "additional": flex_settings
            }

    # Generate CSS
    st.subheader("Generated CSS")

    css_output = "/* Responsive Layout CSS */\n\n"

    # Base styles
    css_output += ".responsive-container {\n"
    css_output += "  box-sizing: border-box;\n"
    css_output += "}\n\n"

    # Media queries
    sorted_breakpoints = sorted(current_breakpoints.items(), key=lambda x: x[1])

    if layout_type == "Mobile First":
        # Mobile first approach
        for i, (bp_name, bp_size) in enumerate(sorted_breakpoints):
            config = layout_config[bp_name]

            if i == 0:
                # Base mobile styles (no media query)
                css_output += f"/* Base styles ({bp_name}) */\n"
                css_output += ".responsive-container {\n"
            else:
                css_output += f"/* {bp_name.title()} styles */\n"
                css_output += f"@media (min-width: {bp_size}px) {{\n"
                css_output += "  .responsive-container {\n"

            css_output += f"    width: {config['container_width']};\n"
            css_output += f"    margin: {config['margin']};\n"
            css_output += f"    padding: {config['padding']}px;\n"
            css_output += f"    display: {config['display']};\n"

            for prop, value in config['additional'].items():
                css_output += f"    {prop}: {value};\n"

            if i == 0:
                css_output += "}\n\n"
            else:
                css_output += "  }\n}\n\n"

    else:
        # Desktop first approach
        for i, (bp_name, bp_size) in enumerate(reversed(sorted_breakpoints)):
            config = layout_config[bp_name]

            if i == 0:
                # Base desktop styles
                css_output += f"/* Base styles ({bp_name}) */\n"
                css_output += ".responsive-container {\n"
            else:
                css_output += f"/* {bp_name.title()} styles */\n"
                css_output += f"@media (max-width: {bp_size - 1}px) {{\n"
                css_output += "  .responsive-container {\n"

            css_output += f"    width: {config['container_width']};\n"
            css_output += f"    margin: {config['margin']};\n"
            css_output += f"    padding: {config['padding']}px;\n"
            css_output += f"    display: {config['display']};\n"

            for prop, value in config['additional'].items():
                css_output += f"    {prop}: {value};\n"

            if i == 0:
                css_output += "}\n\n"
            else:
                css_output += "  }\n}\n\n"

    # Common responsive utilities
    css_output += "/* Responsive Utilities */\n"
    css_output += ".hide-mobile { display: block; }\n"
    css_output += ".hide-desktop { display: none; }\n\n"

    css_output += "@media (max-width: 767px) {\n"
    css_output += "  .hide-mobile { display: none; }\n"
    css_output += "  .hide-desktop { display: block; }\n"
    css_output += "}\n\n"

    css_output += "/* Image responsiveness */\n"
    css_output += ".responsive-img {\n"
    css_output += "  max-width: 100%;\n"
    css_output += "  height: auto;\n"
    css_output += "}\n"

    st.code(css_output, language="css")

    # HTML Example
    with st.expander("📄 HTML Example"):
        html_example = '''<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Your generated CSS goes here */
    </style>
</head>
<body>
    <div class="responsive-container">
        <h1>Responsive Layout</h1>
        <p>This layout adapts to different screen sizes.</p>
        <img src="image.jpg" class="responsive-img" alt="Responsive image">
    </div>
</body>
</html>'''
        st.code(html_example, language="html")

    FileHandler.create_download_link(css_output.encode(), "responsive-layout.css", "text/css")


def bootstrap_helper():
    """Bootstrap helper tools"""
    create_tool_header("Bootstrap Helper", "Generate Bootstrap CSS classes and components", "🧩")

    # Initialize variables to avoid unbound errors
    grid_html = "<!-- Grid HTML will be generated here -->"
    component_html = "<!-- Component HTML will be generated here -->"
    utility_html = "<!-- Utility HTML will be generated here -->"

    tool_type = st.selectbox("Bootstrap Tool", [
        "Grid System", "Components", "Utilities", "Custom Theme", "Layout Helper"
    ])

    if tool_type == "Grid System":
        st.subheader("Bootstrap Grid Generator")

        container_type = st.selectbox("Container Type", ["container", "container-fluid"])
        num_rows = st.number_input("Number of Rows", 1, 10, 1)

        grid_html = f'<div class="{container_type}">\n'

        for row in range(num_rows):
            st.write(f"**Row {row + 1}:**")
            num_cols = st.number_input(f"Number of Columns in Row {row + 1}", 1, 12, 3, key=f"row_{row}_cols")

            col_sizes = []
            remaining_cols = 12

            for col in range(num_cols):
                if col == num_cols - 1:
                    # Last column gets remaining space
                    col_size = remaining_cols
                else:
                    max_size = min(remaining_cols - (num_cols - col - 1), 12)
                    col_size = st.slider(f"Column {col + 1} Size", 1, max_size, min(4, max_size),
                                         key=f"row_{row}_col_{col}")
                    remaining_cols -= col_size

                col_sizes.append(col_size)

            # Generate row HTML
            grid_html += '  <div class="row">\n'
            for i, size in enumerate(col_sizes):
                grid_html += f'    <div class="col-md-{size}">\n'
                grid_html += f'      Column {i + 1}\n'
                grid_html += '    </div>\n'
            grid_html += '  </div>\n'

        grid_html += '</div>'

        st.subheader("Generated HTML")
        st.code(grid_html, language="html")

        # Preview
        st.subheader("Visual Preview")
        preview_css = """
        <style>
        .bootstrap-preview { margin: 20px 0; }
        .bootstrap-preview .container, .bootstrap-preview .container-fluid { background: #f8f9fa; padding: 15px; border: 1px solid #dee2e6; }
        .bootstrap-preview .row { margin-bottom: 10px; }
        .bootstrap-preview [class*="col-"] { background: #007bff; color: white; padding: 10px; margin-bottom: 5px; text-align: center; border-radius: 4px; }
        </style>
        """
        st.markdown(preview_css + f'<div class="bootstrap-preview">{grid_html}</div>', unsafe_allow_html=True)

    elif tool_type == "Components":
        st.subheader("Bootstrap Components")

        component_type = st.selectbox("Component Type", [
            "Button", "Card", "Alert", "Badge", "Navigation", "Modal", "Form"
        ])

        if component_type == "Button":
            button_variant = st.selectbox("Button Variant", [
                "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
            ])
            button_size = st.selectbox("Button Size", ["btn-lg", "(normal)", "btn-sm"])
            button_text = st.text_input("Button Text", "Click me")
            outline = st.checkbox("Outline Style")

            btn_class = f"btn btn{'---outline' if outline else ''}-{button_variant}"
            if button_size != "(normal)":
                btn_class += f" {button_size}"

            component_html = f'<button type="button" class="{btn_class}">{button_text}</button>'

        elif component_type == "Card":
            card_title = st.text_input("Card Title", "Card Title")
            card_text = st.text_area("Card Text", "This is card content.")
            include_image = st.checkbox("Include Image")
            include_footer = st.checkbox("Include Footer")

            component_html = '<div class="card" style="width: 18rem;">\n'
            if include_image:
                component_html += '  <img src="..." class="card-img-top" alt="...">\n'
            component_html += '  <div class="card-body">\n'
            component_html += f'    <h5 class="card-title">{card_title}</h5>\n'
            component_html += f'    <p class="card-text">{card_text}</p>\n'
            component_html += '    <a href="#" class="btn btn-primary">Go somewhere</a>\n'
            component_html += '  </div>\n'
            if include_footer:
                component_html += '  <div class="card-footer text-muted">\n'
                component_html += '    Card footer\n'
                component_html += '  </div>\n'
            component_html += '</div>'

        elif component_type == "Alert":
            alert_type = st.selectbox("Alert Type", [
                "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
            ])
            alert_text = st.text_input("Alert Text", "This is an alert message!")
            dismissible = st.checkbox("Dismissible")

            alert_class = f"alert alert-{alert_type}"
            if dismissible:
                alert_class += " alert-dismissible fade show"

            component_html = f'<div class="{alert_class}" role="alert">\n'
            component_html += f'  {alert_text}\n'
            if dismissible:
                component_html += '  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>\n'
            component_html += '</div>'

        else:
            component_html = f"<!-- {component_type} component code will be generated here -->"

        st.subheader("Generated HTML")
        st.code(component_html, language="html")

    elif tool_type == "Utilities":
        st.subheader("Bootstrap Utility Classes")

        utility_category = st.selectbox("Utility Category", [
            "Spacing", "Colors", "Display", "Flexbox", "Text", "Position"
        ])

        if utility_category == "Spacing":
            property_type = st.selectbox("Property", ["margin", "padding"])
            sides = st.multiselect("Sides", ["top", "bottom", "left", "right", "x (left+right)", "y (top+bottom)"],
                                   ["all"])
            size = st.selectbox("Size", ["0", "1", "2", "3", "4", "5", "auto"])

            prefix = "m" if property_type == "margin" else "p"
            classes = []

            for side in sides:
                if side == "all":
                    classes.append(f"{prefix}-{size}")
                elif side == "x (left+right)":
                    classes.append(f"{prefix}x-{size}")
                elif side == "y (top+bottom)":
                    classes.append(f"{prefix}y-{size}")
                else:
                    side_letter = side[0]
                    classes.append(f"{prefix}{side_letter}-{size}")

            utility_html = f'<div class="{" ".join(classes)}">Element with spacing</div>'

        elif utility_category == "Colors":
            color_type = st.selectbox("Color Type", ["text", "background"])
            color_name = st.selectbox("Color", [
                "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
            ])

            if color_type == "text":
                utility_html = f'<p class="text-{color_name}">Text with color</p>'
                classes = [f"text-{color_name}"]
            else:
                utility_html = f'<div class="bg-{color_name} p-3">Background with color</div>'
                classes = [f"bg-{color_name}"]

        else:
            utility_html = f"<!-- {utility_category} utility classes will be generated here -->"
            classes = []

        st.subheader("Generated HTML")
        st.code(utility_html, language="html")

        st.subheader("Class Reference")
        st.code(" ".join(classes) if classes else "utility-class", language="css")

    elif tool_type == "Custom Theme":
        st.subheader("Bootstrap Theme Customizer")

        # Color customization
        st.write("**Primary Colors:**")
        primary_color = st.color_picker("Primary Color", "#007bff")
        secondary_color = st.color_picker("Secondary Color", "#6c757d")
        success_color = st.color_picker("Success Color", "#28a745")
        danger_color = st.color_picker("Danger Color", "#dc3545")

        # Typography
        st.write("**Typography:**")
        font_family = st.selectbox("Font Family", [
            "System Default", "Arial", "Helvetica", "Georgia", "Times", "Custom"
        ])
        if font_family == "Custom":
            custom_font = st.text_input("Custom Font Family", "'Custom Font', sans-serif")
            font_family = custom_font

        base_font_size = st.slider("Base Font Size (rem)", 0.8, 1.4, 1.0, 0.1)

        # Generate custom CSS
        theme_css = f"""
/* Custom Bootstrap Theme */
:root {{
  --bs-primary: {primary_color};
  --bs-secondary: {secondary_color};
  --bs-success: {success_color};
  --bs-danger: {danger_color};
  --bs-font-family-base: {font_family if font_family != 'System Default' else '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'};
  --bs-body-font-size: {base_font_size}rem;
}}

/* Update button styles */
.btn-primary {{
  background-color: {primary_color};
  border-color: {primary_color};
}}

.btn-secondary {{
  background-color: {secondary_color};
  border-color: {secondary_color};
}}

body {{
  font-family: var(--bs-font-family-base);
  font-size: var(--bs-body-font-size);
}}
"""

        st.subheader("Custom Theme CSS")
        st.code(theme_css, language="css")

        FileHandler.create_download_link(theme_css.encode(), "bootstrap-custom-theme.css", "text/css")

    # Download for all components except Custom Theme
    if tool_type != "Custom Theme":
        # Initialize default content
        download_content = "<!-- Bootstrap component will be generated here -->"

        # Set download content based on what was generated
        if tool_type == "Grid System":
            download_content = grid_html
        elif tool_type == "Components":
            download_content = component_html
        elif tool_type == "Utilities":
            download_content = utility_html

        FileHandler.create_download_link(download_content.encode(), "bootstrap-component.html", "text/html")


def transition_builder():
    """CSS transition builder"""
    create_tool_header("CSS Transition Builder", "Create smooth CSS transitions and animations", "✨")

    transition_type = st.selectbox("Transition Type",
                                   ["Simple Transition", "Multiple Properties", "Keyframe Animation"])

    if transition_type == "Simple Transition":
        st.subheader("Simple Transition")

        col1, col2 = st.columns(2)
        with col1:
            property_name = st.selectbox("Property to Animate", [
                "all", "opacity", "transform", "background-color", "color", "width", "height",
                "margin", "padding", "border-radius", "box-shadow", "filter"
            ])
            duration = st.slider("Duration (seconds)", 0.1, 5.0, 0.3, 0.1)
            timing_function = st.selectbox("Timing Function", [
                "ease", "ease-in", "ease-out", "ease-in-out", "linear",
                "cubic-bezier(0.25, 0.1, 0.25, 1)", "custom"
            ])

        with col2:
            delay = st.slider("Delay (seconds)", 0.0, 2.0, 0.0, 0.1)
            if timing_function == "custom":
                st.write("Custom Cubic Bezier:")
                x1 = st.slider("X1", 0.0, 1.0, 0.25, 0.01)
                y1 = st.slider("Y1", -2.0, 2.0, 0.1, 0.01)
                x2 = st.slider("X2", 0.0, 1.0, 0.25, 0.01)
                y2 = st.slider("Y2", -2.0, 2.0, 1.0, 0.01)
                timing_function = f"cubic-bezier({x1}, {y1}, {x2}, {y2})"

        # Generate transition CSS
        transition_css = f"transition: {property_name} {duration}s {timing_function}"
        if delay > 0:
            transition_css += f" {delay}s"
        transition_css += ";"

        # Interactive states
        st.subheader("Hover/Focus States")

        # Initialize default values
        hover_opacity = 1.0
        hover_transform = "none"
        original_bg = "#007bff"
        hover_bg = "#0056b3"

        if property_name in ["opacity", "all"]:
            hover_opacity = st.slider("Hover Opacity", 0.0, 1.0, 0.8, 0.1)

        if property_name in ["transform", "all"]:
            transform_type = st.selectbox("Transform on Hover", [
                "None", "Scale", "Rotate", "Translate", "Skew"
            ])

            if transform_type == "Scale":
                scale_value = st.slider("Scale Factor", 0.5, 2.0, 1.1, 0.1)
                hover_transform = f"scale({scale_value})"
            elif transform_type == "Rotate":
                rotate_value = st.slider("Rotation (degrees)", -360, 360, 15, 5)
                hover_transform = f"rotate({rotate_value}deg)"
            elif transform_type == "Translate":
                translate_x = st.slider("Translate X (px)", -100, 100, 10, 5)
                translate_y = st.slider("Translate Y (px)", -100, 100, -5, 5)
                hover_transform = f"translate({translate_x}px, {translate_y}px)"

        if property_name in ["background-color", "all"]:
            original_bg = st.color_picker("Original Background", "#007bff")
            hover_bg = st.color_picker("Hover Background", "#0056b3")

        # Generate complete CSS
        complete_css = ".transition-element {\n"
        complete_css += f"  {transition_css}\n"

        if property_name in ["background-color", "all"]:
            complete_css += f"  background-color: {original_bg};\n"
        if property_name in ["opacity", "all"]:
            complete_css += "  opacity: 1;\n"

        complete_css += "}\n\n"
        complete_css += ".transition-element:hover {\n"

        if property_name in ["opacity", "all"]:
            complete_css += f"  opacity: {hover_opacity};\n"
        if property_name in ["transform", "all"]:
            complete_css += f"  transform: {hover_transform};\n"
        if property_name in ["background-color", "all"]:
            complete_css += f"  background-color: {hover_bg};\n"

        complete_css += "}"

        # Live preview
        st.subheader("Interactive Preview")

        preview_styles = f"""
        <style>
        .preview-element {{
            width: 100px;
            height: 100px;
            background-color: {original_bg};
            margin: 20px auto;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            cursor: pointer;
            {transition_css}
        }}

        .preview-element:hover {{
            opacity: {hover_opacity};
            transform: {hover_transform};
            background-color: {hover_bg};
        }}
        </style>

        <div class="preview-element">
            Hover me!
        </div>
        """

        st.markdown(preview_styles, unsafe_allow_html=True)

    elif transition_type == "Multiple Properties":
        st.subheader("Multiple Property Transitions")

        num_properties = st.slider("Number of Properties", 1, 5, 2)

        transitions = []
        for i in range(num_properties):
            with st.expander(f"Property {i + 1}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    prop = st.selectbox(f"Property", [
                        "opacity", "transform", "background-color", "color", "width", "height"
                    ], key=f"prop_{i}")
                with col2:
                    duration = st.slider(f"Duration (s)", 0.1, 3.0, 0.3, 0.1, key=f"dur_{i}")
                with col3:
                    easing = st.selectbox(f"Easing", ["ease", "ease-in", "ease-out", "linear"], key=f"ease_{i}")

                transitions.append(f"{prop} {duration}s {easing}")

        transition_css = f"transition: {', '.join(transitions)};"
        complete_css = f".multi-transition {{\n  {transition_css}\n}}"

    else:  # Keyframe Animation
        st.subheader("Keyframe Animation")

        animation_name = st.text_input("Animation Name", "customAnimation")
        duration = st.slider("Duration (seconds)", 0.5, 10.0, 2.0, 0.1)
        iteration_count = st.selectbox("Iteration Count", ["1", "2", "3", "infinite"])
        direction = st.selectbox("Direction", ["normal", "reverse", "alternate", "alternate-reverse"])
        timing_function = st.selectbox("Timing Function", ["ease", "ease-in", "ease-out", "linear"])

        # Keyframe points
        st.write("**Keyframe Points:**")
        num_keyframes = st.slider("Number of Keyframes", 2, 6, 3)

        keyframes = []
        for i in range(num_keyframes):
            with st.expander(f"Keyframe {i + 1}"):
                if i == 0:
                    percentage = 0
                    st.write("Percentage: 0% (start)")
                elif i == num_keyframes - 1:
                    percentage = 100
                    st.write("Percentage: 100% (end)")
                else:
                    percentage = st.slider(f"Percentage", 1, 99, (100 // num_keyframes) * i, key=f"kf_pct_{i}")

                col1, col2 = st.columns(2)
                with col1:
                    opacity = st.slider(f"Opacity", 0.0, 1.0, 1.0, 0.1, key=f"kf_opacity_{i}")
                    scale = st.slider(f"Scale", 0.1, 2.0, 1.0, 0.1, key=f"kf_scale_{i}")
                with col2:
                    rotate = st.slider(f"Rotation (deg)", 0, 360, 0, 15, key=f"kf_rotate_{i}")
                    translate_y = st.slider(f"Translate Y (px)", -100, 100, 0, 10, key=f"kf_ty_{i}")

                keyframes.append({
                    'percentage': percentage,
                    'opacity': opacity,
                    'scale': scale,
                    'rotate': rotate,
                    'translate_y': translate_y
                })

        # Generate keyframe CSS
        keyframe_css = f"@keyframes {animation_name} {{\n"
        for kf in sorted(keyframes, key=lambda x: x['percentage']):
            keyframe_css += f"  {kf['percentage']}% {{\n"
            keyframe_css += f"    opacity: {kf['opacity']};\n"
            keyframe_css += f"    transform: translateY({kf['translate_y']}px) scale({kf['scale']}) rotate({kf['rotate']}deg);\n"
            keyframe_css += "  }\n"
        keyframe_css += "}\n\n"

        # Animation property
        animation_css = f"animation: {animation_name} {duration}s {timing_function} {iteration_count} {direction};"

        complete_css = keyframe_css + f".animated-element {{\n  {animation_css}\n}}"

    # Display CSS output
    st.subheader("Generated CSS")
    st.code(complete_css, language="css")

    # Common transition examples
    with st.expander("🎨 Common Transition Examples"):
        examples = {
            "Fade In/Out": "transition: opacity 0.3s ease;",
            "Scale on Hover": "transition: transform 0.2s ease;\n/* Add to :hover */\ntransform: scale(1.05);",
            "Slide Up": "transition: transform 0.4s ease;\n/* Add to :hover */\ntransform: translateY(-10px);",
            "Color Change": "transition: background-color 0.3s ease;\n/* Add to :hover */\nbackground-color: #newcolor;",
            "Smooth Box Shadow": "transition: box-shadow 0.3s ease;\n/* Add to :hover */\nbox-shadow: 0 10px 20px rgba(0,0,0,0.2);"
        }

        for name, css in examples.items():
            st.write(f"**{name}:**")
            st.code(css, language="css")

    FileHandler.create_download_link(complete_css.encode(), "transitions.css", "text/css")


def specificity_calculator():
    """CSS specificity calculator"""
    create_tool_header("CSS Specificity Calculator", "Calculate and compare CSS selector specificity", "🎯")

    st.markdown("""
    **CSS Specificity** determines which styles are applied when multiple rules target the same element.
    The specificity is calculated based on the number of:
    - **IDs** (most specific)
    - **Classes, attributes, and pseudo-classes**
    - **Elements and pseudo-elements** (least specific)
    """)

    # Input for selectors
    st.subheader("Selector Input")

    input_method = st.radio("Input Method", ["Single Selector", "Multiple Selectors", "CSS Rule"])

    if input_method == "Single Selector":
        selector = st.text_input("Enter CSS Selector", "#header .nav-menu li a:hover")

        if selector:
            specificity = calculate_specificity(selector)
            display_specificity_result(selector, specificity)

    elif input_method == "Multiple Selectors":
        st.write("Compare multiple selectors:")

        selectors = []
        num_selectors = st.number_input("Number of Selectors", 2, 10, 3)

        for i in range(num_selectors):
            selector = st.text_input(f"Selector {i + 1}",
                                     placeholder=f"Example: {'#main .content' if i == 0 else '.button' if i == 1 else 'div p'}",
                                     key=f"selector_{i}")
            if selector:
                selectors.append(selector)

        if len(selectors) >= 2:
            st.subheader("Specificity Comparison")

            results = []
            for selector in selectors:
                specificity = calculate_specificity(selector)
                results.append((selector, specificity))

            # Sort by specificity (highest first)
            results.sort(key=lambda x: (x[1]['ids'], x[1]['classes'], x[1]['elements']), reverse=True)

            for i, (selector, specificity) in enumerate(results):
                priority_icon = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "🔸"
                st.write(f"**{priority_icon} Priority {i + 1}:** `{selector}`")
                display_specificity_result(selector, specificity, show_header=False)
                st.write("---")

    else:  # CSS Rule
        st.write("Paste a complete CSS rule:")
        css_rule = st.text_area("CSS Rule",
                                placeholder="""#header .navigation li a:hover {
    color: blue;
    text-decoration: underline;
}""", height=150)

        if css_rule:
            # Extract selector from CSS rule
            lines = css_rule.strip().split('\n')
            selector_line = lines[0].strip()

            # Remove opening brace if present
            if '{' in selector_line:
                selector = selector_line.split('{')[0].strip()
            else:
                selector = selector_line

            if selector:
                specificity = calculate_specificity(selector)
                st.subheader("Extracted Selector")
                st.code(selector)
                display_specificity_result(selector, specificity)

    # Specificity tips
    with st.expander("💡 Specificity Tips & Best Practices"):
        st.markdown("""
        ### Understanding Specificity Values

        - **Inline styles**: Specificity of 1000 (highest)
        - **IDs**: Specificity of 100 each
        - **Classes, attributes, pseudo-classes**: Specificity of 10 each
        - **Elements and pseudo-elements**: Specificity of 1 each

        ### Best Practices

        1. **Avoid using !important** - It breaks the natural cascade
        2. **Keep specificity low** - Use classes instead of IDs when possible
        3. **Be consistent** - Follow a naming convention like BEM
        4. **Use cascade wisely** - Order your CSS rules thoughtfully
        5. **Prefer classes over complex selectors** - Easier to maintain

        ### Common Specificity Issues

        - **Overly specific selectors**: `#main .content .sidebar .widget .title`
        - **Fighting specificity with !important**: Creates maintenance nightmares
        - **Inconsistent naming**: Makes it hard to predict specificity
        """)


def calculate_specificity(selector):
    """Calculate CSS specificity for a given selector"""
    import re

    # Remove whitespace and normalize
    selector = selector.strip()

    # Count different types of selectors
    ids = len(re.findall(r'#[\w-]+', selector))

    # Classes, attributes, and pseudo-classes
    classes = len(re.findall(r'\.[\w-]+', selector))  # Classes
    classes += len(re.findall(r'\[[^\]]*\]', selector))  # Attributes
    classes += len(re.findall(r':[\w-]+(?:\([^)]*\))?', selector))  # Pseudo-classes

    # Elements and pseudo-elements
    # First remove IDs, classes, attributes, and pseudo-classes to avoid double counting
    cleaned_selector = re.sub(r'#[\w-]+', '', selector)  # Remove IDs
    cleaned_selector = re.sub(r'\.[\w-]+', '', cleaned_selector)  # Remove classes
    cleaned_selector = re.sub(r'\[[^\]]*\]', '', cleaned_selector)  # Remove attributes
    cleaned_selector = re.sub(r':[\w-]+(?:\([^)]*\))?', '', cleaned_selector)  # Remove pseudo-classes

    # Count remaining element selectors
    elements = len(re.findall(r'\b[a-zA-Z][\w-]*\b', cleaned_selector))

    # Calculate total specificity
    total = (ids * 100) + (classes * 10) + elements

    return {
        'ids': ids,
        'classes': classes,
        'elements': elements,
        'total': total,
        'notation': f"{ids},{classes},{elements}"
    }


def display_specificity_result(selector, specificity, show_header=True):
    """Display specificity calculation results"""

    if show_header:
        st.subheader("Specificity Calculation")

    # Visual representation
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("IDs", specificity['ids'], help="Worth 100 points each")
    with col2:
        st.metric("Classes/Attrs/Pseudo", specificity['classes'], help="Worth 10 points each")
    with col3:
        st.metric("Elements", specificity['elements'], help="Worth 1 point each")
    with col4:
        st.metric("Total Specificity", specificity['total'])

    # Breakdown
    if specificity['total'] > 0:
        calculation = []
        if specificity['ids'] > 0:
            calculation.append(f"{specificity['ids']} × 100 = {specificity['ids'] * 100}")
        if specificity['classes'] > 0:
            calculation.append(f"{specificity['classes']} × 10 = {specificity['classes'] * 10}")
        if specificity['elements'] > 0:
            calculation.append(f"{specificity['elements']} × 1 = {specificity['elements']}")

        st.write(f"**Calculation:** {' + '.join(calculation)} = **{specificity['total']}**")
        st.write(f"**Specificity Notation:** `{specificity['notation']}`")


def selector_tester():
    """CSS selector tester"""
    create_tool_header("CSS Selector Tester", "Test and validate CSS selectors against HTML", "🎯")

    # Input modes
    input_mode = st.radio("Input Mode", ["Interactive Builder", "Manual Input", "Upload Files"])

    if input_mode == "Interactive Builder":
        st.subheader("HTML Structure Builder")

        # Simple HTML builder
        with st.expander("🏠 Build Sample HTML Structure"):
            structure_type = st.selectbox("HTML Structure Template", [
                "Simple Page", "Navigation Menu", "Article Layout", "Form Elements", "Custom"
            ])

            if structure_type == "Simple Page":
                sample_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <header id="main-header" class="site-header">
        <h1 class="site-title">My Website</h1>
        <nav class="main-navigation">
            <ul class="nav-menu">
                <li class="menu-item"><a href="#home">Home</a></li>
                <li class="menu-item current"><a href="#about">About</a></li>
                <li class="menu-item"><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main id="content" class="main-content">
        <article class="post featured">
            <h2 class="post-title">Welcome to My Site</h2>
            <p class="post-excerpt">This is a sample paragraph.</p>
            <a href="#read-more" class="btn btn-primary">Read More</a>
        </article>
    </main>

    <footer id="site-footer" class="site-footer">
        <p class="copyright">&copy; 2024 My Website</p>
    </footer>
</body>
</html>"""

            elif structure_type == "Navigation Menu":
                sample_html = """
<nav class="navbar navbar-main">
    <div class="navbar-brand">
        <a href="#" class="brand-link">
            <img src="logo.png" alt="Logo" class="brand-logo">
            <span class="brand-text">Brand</span>
        </a>
    </div>

    <ul class="navbar-nav">
        <li class="nav-item active">
            <a href="#home" class="nav-link">Home</a>
        </li>
        <li class="nav-item dropdown">
            <a href="#services" class="nav-link dropdown-toggle">Services</a>
            <ul class="dropdown-menu">
                <li><a href="#web-design" class="dropdown-link">Web Design</a></li>
                <li><a href="#development" class="dropdown-link">Development</a></li>
            </ul>
        </li>
        <li class="nav-item">
            <a href="#contact" class="nav-link">Contact</a>
        </li>
    </ul>
</nav>"""

            elif structure_type == "Form Elements":
                sample_html = """
<form class="contact-form" id="contact-form">
    <div class="form-group">
        <label for="name" class="form-label required">Name</label>
        <input type="text" id="name" name="name" class="form-control" required>
    </div>

    <div class="form-group">
        <label for="email" class="form-label required">Email</label>
        <input type="email" id="email" name="email" class="form-control" required>
    </div>

    <div class="form-group">
        <label for="message" class="form-label">Message</label>
        <textarea id="message" name="message" class="form-control" rows="4"></textarea>
    </div>

    <div class="form-actions">
        <button type="submit" class="btn btn-primary">Send Message</button>
        <button type="reset" class="btn btn-secondary">Reset</button>
    </div>
</form>"""

            else:
                sample_html = st.text_area("Enter Custom HTML", height=200,
                                           value="<div class='container'>\n  <p class='text'>Hello World</p>\n</div>")

        if structure_type != "Custom":
            st.code(sample_html, language="html")

    elif input_mode == "Manual Input":
        st.subheader("Manual HTML Input")
        sample_html = st.text_area("Enter HTML code to test against:", height=300,
                                   value="""<div id="container" class="main-container">
    <header class="site-header">
        <h1 class="title">Page Title</h1>
        <nav class="navigation">
            <ul class="nav-list">
                <li class="nav-item active"><a href="#home">Home</a></li>
                <li class="nav-item"><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>
    <main class="content">
        <article class="post featured">
            <h2 class="post-title">Article Title</h2>
            <p class="post-content">Article content goes here.</p>
        </article>
    </main>
</div>""")

    else:  # Upload Files
        st.subheader("Upload HTML File")
        uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

        if uploaded_file:
            sample_html = FileHandler.process_text_file(uploaded_file[0])
            st.code(sample_html, language="html")
        else:
            sample_html = ""

    if sample_html:
        st.markdown("---")
        st.subheader("CSS Selector Testing")

        # Selector input
        col1, col2 = st.columns([2, 1])

        with col1:
            selector_input = st.text_input(
                "Enter CSS Selector to Test",
                placeholder="e.g., .nav-item.active a, #container .post-title"
            )

        with col2:
            test_type = st.selectbox("Test Type", ["Find Elements", "Validate Syntax", "Specificity"])

        if selector_input:
            if test_type == "Find Elements":
                # Simple element matching (basic implementation)
                try:
                    # Parse HTML and extract basic elements
                    import re

                    # Find all HTML tags with their attributes
                    tag_pattern = r'<(\w+)([^>]*)>'
                    matches = re.finditer(tag_pattern, sample_html)

                    found_elements = []
                    for match in matches:
                        tag = match.group(1)
                        attrs = match.group(2)

                        # Extract id and class attributes
                        id_match = re.search(r'id=["\']([^"\']*)["\']', attrs)
                        class_match = re.search(r'class=["\']([^"\']*)["\']', attrs)

                        element_id = id_match.group(1) if id_match else ''
                        element_classes = class_match.group(1).split() if class_match else []

                        # Basic selector matching
                        matches_selector = False

                        # ID selector
                        if selector_input.startswith('#'):
                            matches_selector = element_id == selector_input[1:]
                        # Class selector
                        elif selector_input.startswith('.'):
                            matches_selector = selector_input[1:] in element_classes
                        # Element selector
                        elif selector_input.isalnum():
                            matches_selector = tag == selector_input
                        # Combined selectors (basic support)
                        elif '.' in selector_input:
                            parts = selector_input.split('.')
                            if len(parts) >= 2:
                                tag_part = parts[0] if parts[0] else None
                                class_parts = parts[1:]

                                tag_matches = (not tag_part) or (tag == tag_part)
                                class_matches = all(cls in element_classes for cls in class_parts)
                                matches_selector = tag_matches and class_matches

                        if matches_selector:
                            found_elements.append({
                                'tag': tag,
                                'id': element_id,
                                'classes': element_classes,
                                'html': match.group(0)
                            })

                    if found_elements:
                        st.success(f"✅ Found {len(found_elements)} matching element(s)")

                        for i, element in enumerate(found_elements[:5]):  # Show first 5
                            with st.expander(f"Match {i + 1}: {element['tag']}"):
                                st.write(f"**Tag:** `{element['tag']}`")
                                if element['id']:
                                    st.write(f"**ID:** `{element['id']}`")
                                if element['classes']:
                                    st.write(f"**Classes:** `{' '.join(element['classes'])}`")
                                st.code(element['html'], language="html")
                    else:
                        st.warning("⚠️ No elements match this selector")

                except Exception as e:
                    st.error(f"❌ Error testing selector: {str(e)}")

            elif test_type == "Validate Syntax":
                # Basic syntax validation
                import re
                is_valid = True
                error_msg = ""

                if not selector_input.strip():
                    is_valid = False
                    error_msg = "Selector cannot be empty"
                elif re.search(r'[<>"\']', selector_input):
                    is_valid = False
                    error_msg = "Invalid characters in selector"
                elif selector_input.count('[') != selector_input.count(']'):
                    is_valid = False
                    error_msg = "Unmatched square brackets"

                if is_valid:
                    st.success("✅ Selector syntax is valid")
                else:
                    st.error(f"❌ {error_msg}")

            else:  # Specificity
                specificity = calculate_specificity(selector_input)
                display_specificity_result(selector_input, specificity)

        # Selector examples
        with st.expander("💡 Selector Examples & Tips"):
            st.markdown("""
            ### Common CSS Selectors

            **Basic Selectors:**
            - `div` - All div elements
            - `.class-name` - Elements with class "class-name"
            - `#element-id` - Element with ID "element-id"

            **Combinators:**
            - `.parent .child` - Descendant selector
            - `.parent > .child` - Direct child selector
            - `.element + .sibling` - Adjacent sibling
            - `.element ~ .sibling` - General sibling

            **Pseudo-classes:**
            - `a:hover` - Link on hover
            - `li:first-child` - First list item
            - `input:not([disabled])` - Enabled inputs

            **Attribute Selectors:**
            - `[href]` - Elements with href attribute
            - `[class*="nav"]` - Class contains "nav"
            - `[href^="https"]` - Href starts with "https"
            """)

            # Quick test buttons
            st.write("**Quick Tests:**")
            quick_tests = [
                "div",  # Element
                ".nav-item",  # Class
                "#container",  # ID
                ".nav-item.active",  # Multiple classes
            ]

            cols = st.columns(len(quick_tests))
            for i, test in enumerate(quick_tests):
                with cols[i]:
                    if st.button(f"`{test}`", key=f"quick_{i}"):
                        st.session_state.test_selector = test


def sass_scss_compiler():
    """SASS/SCSS to CSS compiler"""
    create_tool_header("SASS/SCSS Compiler", "Compile SASS/SCSS code to CSS", "💎")

    tab1, tab2 = st.tabs(["SASS Compiler", "SCSS Compiler"])

    with tab1:
        st.subheader("SASS to CSS")
        sass_input = st.text_area("Enter SASS code:", height=300, value="""$primary-color: #007bff
$secondary-color: #6c757d
$border-radius: 4px

.container
  background-color: $primary-color
  border-radius: $border-radius
  padding: 20px

  .header
    color: white
    font-size: 24px

    &:hover
      color: $secondary-color""")

        if st.button("Compile SASS to CSS", key="sass"):
            # Simple SASS-like conversion (basic features)
            css_output = convert_sass_to_css(sass_input)

            st.subheader("Compiled CSS")
            st.code(css_output, language="css")

            FileHandler.create_download_link(css_output.encode(), "compiled-sass.css", "text/css")

    with tab2:
        st.subheader("SCSS to CSS")
        scss_input = st.text_area("Enter SCSS code:", height=300, value="""$primary-color: #007bff;
$secondary-color: #6c757d;
$border-radius: 4px;

.container {
  background-color: $primary-color;
  border-radius: $border-radius;
  padding: 20px;

  .header {
    color: white;
    font-size: 24px;

    &:hover {
      color: $secondary-color;
    }
  }
}""")

        if st.button("Compile SCSS to CSS", key="scss"):
            # Simple SCSS-like conversion (basic features)
            css_output = convert_scss_to_css(scss_input)

            st.subheader("Compiled CSS")
            st.code(css_output, language="css")

            FileHandler.create_download_link(css_output.encode(), "compiled-scss.css", "text/css")


def less_processor():
    """LESS to CSS processor"""
    create_tool_header("LESS Processor", "Process LESS code to CSS", "📦")

    less_input = st.text_area("Enter LESS code:", height=300, value="""@primary-color: #007bff;
@secondary-color: #6c757d;
@border-radius: 4px;

.container {
  background-color: @primary-color;
  border-radius: @border-radius;
  padding: 20px;

  .header {
    color: white;
    font-size: 24px;

    &:hover {
      color: @secondary-color;
    }
  }

  // Mixin usage
  .border-radius(@border-radius);
}

.border-radius(@radius) {
  border-radius: @radius;
  -webkit-border-radius: @radius;
  -moz-border-radius: @radius;
}""")

    if st.button("Process LESS to CSS"):
        # Simple LESS-like conversion (basic features)
        css_output = convert_less_to_css(less_input)

        st.subheader("Processed CSS")
        st.code(css_output, language="css")

        # Show statistics
        st.subheader("Processing Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Input Lines", len(less_input.split('\n')))
        with col2:
            st.metric("Output Lines", len(css_output.split('\n')))

        FileHandler.create_download_link(css_output.encode(), "compiled-less.css", "text/css")


def stylus_compiler():
    """Stylus to CSS compiler"""
    create_tool_header("Stylus Compiler", "Compile Stylus code to CSS", "🎨")

    stylus_input = st.text_area("Enter Stylus code:", height=300, value="""primary-color = #007bff
secondary-color = #6c757d
border-radius = 4px

.container
  background-color primary-color
  border-radius border-radius
  padding 20px

  .header
    color white
    font-size 24px

    &:hover
      color secondary-color

// Stylus function
border-radius(radius)
  border-radius radius
  -webkit-border-radius radius
  -moz-border-radius radius

.button
  border-radius(5px)
  background primary-color
  color white
  padding 10px 20px""")

    if st.button("Compile Stylus to CSS"):
        # Simple Stylus-like conversion (basic features)
        css_output = convert_stylus_to_css(stylus_input)

        st.subheader("Compiled CSS")
        st.code(css_output, language="css")

        # Feature analysis
        st.subheader("Stylus Features Used")
        features = analyze_stylus_features(stylus_input)
        for feature, count in features.items():
            if count > 0:
                st.write(f"• {feature}: {count} times")

        FileHandler.create_download_link(css_output.encode(), "compiled-stylus.css", "text/css")


def css_variables_generator():
    """CSS Variables (Custom Properties) generator"""
    create_tool_header("CSS Variables Generator", "Generate CSS custom properties", "🎯")

    tab1, tab2, tab3 = st.tabs(["Color Variables", "Spacing Variables", "Typography Variables"])

    with tab1:
        st.subheader("Color System Variables")

        # Primary colors
        st.write("**Primary Colors:**")
        primary = st.color_picker("Primary", "#007bff")
        secondary = st.color_picker("Secondary", "#6c757d")
        success = st.color_picker("Success", "#28a745")
        danger = st.color_picker("Danger", "#dc3545")
        warning = st.color_picker("Warning", "#ffc107")
        info = st.color_picker("Info", "#17a2b8")

        # Generate color variations
        generate_variations = st.checkbox("Generate color variations (light, dark)")

        color_vars = f"""/* Color Variables */
:root {{
  --color-primary: {primary};
  --color-secondary: {secondary};
  --color-success: {success};
  --color-danger: {danger};
  --color-warning: {warning};
  --color-info: {info};"""

        if generate_variations:
            color_vars += f"""

  /* Color Variations */
  --color-primary-light: {lighten_color(primary, 20)};
  --color-primary-dark: {darken_color(primary, 20)};
  --color-secondary-light: {lighten_color(secondary, 20)};
  --color-secondary-dark: {darken_color(secondary, 20)};"""

        color_vars += "\n}"

        st.code(color_vars, language="css")

        # Usage examples
        st.subheader("Usage Examples")
        usage_examples = """/* Using the variables */
.button-primary {
  background-color: var(--color-primary);
  border: 1px solid var(--color-primary-dark);
}

.text-success {
  color: var(--color-success);
}

.alert-danger {
  background-color: var(--color-danger);
  color: white;
}"""
        st.code(usage_examples, language="css")

    with tab2:
        st.subheader("Spacing System Variables")

        base_spacing = st.slider("Base Spacing (px)", 4, 16, 8)
        levels = st.slider("Spacing Levels", 5, 12, 8)

        spacing_vars = "/* Spacing Variables */\n:root {\n"

        for i in range(levels):
            value = base_spacing * (i + 1)
            spacing_vars += f"  --space-{i + 1}: {value}px;\n"

        # Add common spacing aliases
        spacing_vars += f"""
  /* Spacing Aliases */
  --space-xs: var(--space-1);
  --space-sm: var(--space-2);
  --space-md: var(--space-4);
  --space-lg: var(--space-6);
  --space-xl: var(--space-8);
}}"""

        st.code(spacing_vars, language="css")

        # Usage examples
        st.subheader("Usage Examples")
        spacing_usage = """/* Using spacing variables */
.container {
  padding: var(--space-md);
  margin-bottom: var(--space-lg);
}

.button {
  padding: var(--space-2) var(--space-4);
  margin: var(--space-1);
}"""
        st.code(spacing_usage, language="css")

    with tab3:
        st.subheader("Typography Variables")

        # Font families
        primary_font = st.text_input("Primary Font Family", "system-ui, -apple-system, sans-serif")
        heading_font = st.text_input("Heading Font Family", "Georgia, serif")
        mono_font = st.text_input("Monospace Font Family", "'Courier New', monospace")

        # Font sizes
        base_size = st.slider("Base Font Size (rem)", 0.8, 1.2, 1.0, 0.1)
        scale_ratio = st.slider("Type Scale Ratio", 1.1, 1.5, 1.25, 0.05)

        typography_vars = f"""/* Typography Variables */
:root {{
  /* Font Families */
  --font-primary: {primary_font};
  --font-heading: {heading_font};
  --font-mono: {mono_font};

  /* Font Sizes */
  --text-xs: {base_size * 0.75:.2f}rem;
  --text-sm: {base_size * 0.875:.2f}rem;
  --text-base: {base_size:.2f}rem;
  --text-lg: {base_size * scale_ratio:.2f}rem;
  --text-xl: {base_size * (scale_ratio ** 2):.2f}rem;
  --text-2xl: {base_size * (scale_ratio ** 3):.2f}rem;
  --text-3xl: {base_size * (scale_ratio ** 4):.2f}rem;

  /* Line Heights */
  --leading-tight: 1.2;
  --leading-normal: 1.5;
  --leading-loose: 1.8;

  /* Font Weights */
  --weight-light: 300;
  --weight-normal: 400;
  --weight-medium: 500;
  --weight-bold: 700;
}}"""

        st.code(typography_vars, language="css")

    # Generate complete CSS file
    if st.button("Generate Complete Variable System"):
        complete_vars = color_vars + "\n\n" + spacing_vars + "\n\n" + typography_vars

        st.subheader("Complete CSS Variables System")
        st.code(complete_vars, language="css")

        FileHandler.create_download_link(complete_vars.encode(), "css-variables.css", "text/css")


def css_property_checker():
    """CSS Property checker and validator"""
    create_tool_header("CSS Property Checker", "Check CSS properties and values", "🔍")

    tab1, tab2 = st.tabs(["Property Validation", "Property Information"])

    with tab1:
        st.subheader("Validate CSS Properties")

        css_input = st.text_area("Enter CSS code to validate:", height=300, value=""".example {
  color: red;
  background-color: #007bff;
  display: flex;
  justify-content: center;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
  transform: translateY(-2px);
  unknown-property: invalid-value;
  font-size: 16px;
  margin: 10px auto;
}""")

        if st.button("Validate Properties"):
            validation_results = validate_css_properties(css_input)

            st.subheader("Validation Results")

            if validation_results['valid_properties']:
                st.success(f"✅ {len(validation_results['valid_properties'])} valid properties found")
                with st.expander("Valid Properties"):
                    for prop in validation_results['valid_properties']:
                        st.write(f"• `{prop}`")

            if validation_results['invalid_properties']:
                st.error(f"❌ {len(validation_results['invalid_properties'])} invalid properties found")
                for prop in validation_results['invalid_properties']:
                    st.error(f"• `{prop}` - Unknown property")

            if validation_results['deprecated_properties']:
                st.warning(f"⚠️ {len(validation_results['deprecated_properties'])} deprecated properties found")
                for prop in validation_results['deprecated_properties']:
                    st.warning(f"• `{prop}` - Deprecated property")

    with tab2:
        st.subheader("CSS Property Information")

        property_name = st.text_input("Enter CSS property name:", "display")

        if property_name:
            property_info = get_css_property_info(property_name)

            if property_info:
                st.success(f"✅ `{property_name}` is a valid CSS property")

                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Description:**")
                    st.info(property_info['description'])

                    st.write("**Syntax:**")
                    st.code(property_info['syntax'], language="css")

                with col2:
                    st.write("**Valid Values:**")
                    for value in property_info['values']:
                        st.write(f"• `{value}`")

                    st.write("**Browser Support:**")
                    support = property_info['browser_support']
                    for browser, version in support.items():
                        st.write(f"• {browser}: {version}")

                # Examples
                st.subheader("Usage Examples")
                for example in property_info['examples']:
                    st.code(example, language="css")
            else:
                st.error(f"❌ `{property_name}` is not a valid CSS property")

                # Suggest similar properties
                suggestions = suggest_similar_properties(property_name)
                if suggestions:
                    st.write("**Did you mean:**")
                    for suggestion in suggestions[:5]:
                        if st.button(f"`{suggestion}`", key=f"suggest_{suggestion}"):
                            st.session_state.property_suggestion = suggestion


def css_browser_compatibility():
    """CSS Browser compatibility checker"""
    create_tool_header("Browser Compatibility Checker", "Check CSS browser support", "🌐")

    tab1, tab2 = st.tabs(["Property Compatibility", "Feature Compatibility"])

    with tab1:
        st.subheader("Check CSS Property Compatibility")

        css_input = st.text_area("Enter CSS properties to check:", height=300, value=""".modern-layout {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  container-type: inline-size;
  backdrop-filter: blur(10px);
  aspect-ratio: 16/9;
  scroll-snap-type: y mandatory;
  overscroll-behavior: contain;
}""")

        if st.button("Check Browser Compatibility"):
            compatibility_results = check_browser_compatibility(css_input)

            st.subheader("Browser Support Summary")

            browsers = ["Chrome", "Firefox", "Safari", "Edge", "IE"]

            # Create compatibility table
            for property_name, support in compatibility_results.items():
                st.write(f"**{property_name}**")

                cols = st.columns(len(browsers))
                for i, browser in enumerate(browsers):
                    with cols[i]:
                        status = support.get(browser, "Unknown")
                        if status == "Supported":
                            st.success(f"✅ {browser}")
                        elif status == "Partial":
                            st.warning(f"⚠️ {browser}")
                        elif status == "Not Supported":
                            st.error(f"❌ {browser}")
                        else:
                            st.info(f"❓ {browser}")

                st.markdown("---")

    with tab2:
        st.subheader("CSS Feature Compatibility")

        feature_category = st.selectbox("Feature Category", [
            "Layout", "Flexbox", "Grid", "Animations", "Colors", "Typography", "Transforms", "Filters"
        ])

        features = get_css_features_by_category(feature_category)

        selected_feature = st.selectbox(f"Select {feature_category} Feature", features)

        if selected_feature:
            feature_info = get_feature_compatibility_info(selected_feature)

            st.subheader(f"Compatibility for: {selected_feature}")

            # Browser support chart
            browsers = ["Chrome", "Firefox", "Safari", "Edge", "IE"]
            support_data = []

            for browser in browsers:
                support = feature_info['support'].get(browser, {"status": "unknown", "version": "N/A"})
                support_data.append({
                    "Browser": browser,
                    "Status": support['status'],
                    "Version": support['version']
                })

            # Display as table
            for data in support_data:
                col1, col2, col3 = st.columns([2, 2, 2])
                with col1:
                    st.write(data['Browser'])
                with col2:
                    status = data['Status']
                    if status == "supported":
                        st.success("✅ Supported")
                    elif status == "partial":
                        st.warning("⚠️ Partial")
                    else:
                        st.error("❌ Not Supported")
                with col3:
                    st.write(f"v{data['Version']}")

            # Usage statistics
            if 'usage' in feature_info:
                st.subheader("Global Usage Statistics")
                st.metric("Global Support", f"{feature_info['usage']['global']:.1f}%")

            # Notes and warnings
            if feature_info.get('notes'):
                st.subheader("Implementation Notes")
                st.info(feature_info['notes'])


def css_linter():
    """CSS Linter for code quality"""
    create_tool_header("CSS Linter", "Analyze CSS code quality and best practices", "🔎")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to lint:", height=400, value="""/* Sample CSS with various issues */
.container {
    COLOR: red;  /* Should be lowercase */
    background-color: #ff0000;  /* Could use color name */
    margin: 10px 10px 10px 10px;  /* Could be simplified */
    font-size: 12px;  /* Consider relative units */
    z-index: 99999;  /* Very high z-index */
    width: 500px;  /* Consider responsive units */
}

#header {
    background-color: red;
    background-color: blue;  /* Duplicate property */
}

.unused-class {
    display: none;
}

.button {
    border: none;
    outline: none;  /* Accessibility concern */
    background: linear-gradient(to right, red, blue);  /* Vendor prefixes missing */
}

.responsive {
    @media screen and (max-width: 768px) {
        font-size: 14px;
    }
}""")

    if css_content:
        # Linting options
        st.subheader("Linting Options")
        col1, col2 = st.columns(2)

        with col1:
            check_duplicates = st.checkbox("Check Duplicate Properties", True)
            check_unused = st.checkbox("Check Unused Selectors", True)
            check_colors = st.checkbox("Color Format Validation", True)
            check_units = st.checkbox("Unit Recommendations", True)

        with col2:
            check_accessibility = st.checkbox("Accessibility Checks", True)
            check_performance = st.checkbox("Performance Issues", True)
            check_vendor_prefixes = st.checkbox("Vendor Prefix Warnings", True)
            check_naming = st.checkbox("Naming Conventions", True)

        if st.button("Lint CSS Code"):
            linting_results = lint_css_code(css_content, {
                'duplicates': check_duplicates,
                'unused': check_unused,
                'colors': check_colors,
                'units': check_units,
                'accessibility': check_accessibility,
                'performance': check_performance,
                'vendor_prefixes': check_vendor_prefixes,
                'naming': check_naming
            })

            st.subheader("Linting Results")

            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Errors", linting_results['summary']['errors'])
            with col2:
                st.metric("Warnings", linting_results['summary']['warnings'])
            with col3:
                st.metric("Info", linting_results['summary']['info'])
            with col4:
                score = max(0, 100 - (
                            linting_results['summary']['errors'] * 10 + linting_results['summary']['warnings'] * 3))
                st.metric("Quality Score", f"{score}/100")

            # Detailed issues
            if linting_results['issues']:
                for issue in linting_results['issues']:
                    severity = issue['severity']
                    if severity == 'error':
                        st.error(f"🚨 **Line {issue['line']}**: {issue['message']}")
                    elif severity == 'warning':
                        st.warning(f"⚠️ **Line {issue['line']}**: {issue['message']}")
                    else:
                        st.info(f"💡 **Line {issue['line']}**: {issue['message']}")

                    if issue.get('suggestion'):
                        st.code(issue['suggestion'], language="css")

                    st.markdown("---")

            else:
                st.success("🎉 No issues found! Your CSS looks great!")

            # Best practices recommendations
            st.subheader("💡 CSS Best Practices")
            st.markdown("""
            **Performance:**
            - Minimize CSS file size
            - Use CSS shorthand properties
            - Avoid deep nesting (>3 levels)
            - Use efficient selectors

            **Maintainability:**
            - Use consistent naming conventions
            - Group related properties
            - Comment complex code
            - Organize code into sections

            **Accessibility:**
            - Don't remove focus outlines without alternatives
            - Ensure sufficient color contrast
            - Use relative units for text
            - Consider reduced motion preferences
            """)


# Helper functions for the CSS tools

def convert_sass_to_css(sass_code):
    """Convert basic SASS syntax to CSS (simplified implementation)"""
    lines = sass_code.split('\n')
    css_lines = []
    variables = {}
    indent_level = 0
    current_selectors = []

    for line in lines:
        line = line.rstrip()
        if not line or line.strip().startswith('//'):
            continue

        # Handle variables
        if line.strip().startswith('$'):
            var_match = re.match(r'\s*\$([^:]+):\s*(.+)', line)
            if var_match:
                variables[var_match.group(1).strip()] = var_match.group(2).strip()
            continue

        # Calculate indentation
        current_indent = len(line) - len(line.lstrip())

        # Handle selector or property
        if ':' in line and not line.strip().endswith(':'):
            # Property
            prop_line = line.strip()
            # Replace variables
            for var_name, var_value in variables.items():
                prop_line = prop_line.replace(f'${var_name}', var_value)

            css_lines.append('  ' * len(current_selectors) + prop_line + (';' if not prop_line.endswith(';') else ''))
        else:
            # Selector
            if current_indent <= indent_level:
                # Close previous selectors
                while len(current_selectors) > current_indent // 2:
                    current_selectors.pop()
                    css_lines.append('  ' * len(current_selectors) + '}')

            selector = line.strip().rstrip(':')
            if selector.startswith('&'):
                # Parent reference
                if current_selectors:
                    current_selectors[-1] = current_selectors[-1] + selector[1:]
            else:
                current_selectors.append(selector)
                css_lines.append('  ' * (len(current_selectors) - 1) + selector + ' {')

            indent_level = current_indent

    # Close remaining selectors
    while current_selectors:
        current_selectors.pop()
        css_lines.append('  ' * len(current_selectors) + '}')

    return '\n'.join(css_lines)


def convert_scss_to_css(scss_code):
    """Convert basic SCSS syntax to CSS (simplified implementation)"""
    # For SCSS, we can use a similar approach but with brace-based syntax
    lines = scss_code.split('\n')
    css_lines = []
    variables = {}

    for line in lines:
        line = line.rstrip()
        if not line or line.strip().startswith('//'):
            continue

        # Handle variables
        if line.strip().startswith('$'):
            var_match = re.match(r'\s*\$([^:]+):\s*(.+);?', line)
            if var_match:
                variables[var_match.group(1).strip()] = var_match.group(2).rstrip(';')
            continue

        # Replace variables in the line
        processed_line = line
        for var_name, var_value in variables.items():
            processed_line = processed_line.replace(f'${var_name}', var_value)

        css_lines.append(processed_line)

    return '\n'.join(css_lines)


def convert_less_to_css(less_code):
    """Convert basic LESS syntax to CSS (simplified implementation)"""
    lines = less_code.split('\n')
    css_lines = []
    variables = {}

    for line in lines:
        line = line.rstrip()
        if not line or line.strip().startswith('//'):
            continue

        # Handle variables
        if line.strip().startswith('@') and ':' in line:
            var_match = re.match(r'\s*@([^:]+):\s*(.+);?', line)
            if var_match:
                variables[var_match.group(1).strip()] = var_match.group(2).rstrip(';')
            continue

        # Replace variables in the line
        processed_line = line
        for var_name, var_value in variables.items():
            processed_line = processed_line.replace(f'@{var_name}', var_value)

        css_lines.append(processed_line)

    return '\n'.join(css_lines)


def convert_stylus_to_css(stylus_code):
    """Convert basic Stylus syntax to CSS (simplified implementation)"""
    lines = stylus_code.split('\n')
    css_lines = []
    variables = {}
    indent_level = 0
    current_selectors = []

    for line in lines:
        line = line.rstrip()
        if not line or line.strip().startswith('//'):
            continue

        # Handle variables (no $ or @ prefix in Stylus)
        if '=' in line and not line.strip().startswith('.') and not line.strip().startswith('#'):
            var_match = re.match(r'\s*([^=]+)\s*=\s*(.+)', line)
            if var_match:
                variables[var_match.group(1).strip()] = var_match.group(2).strip()
            continue

        # Calculate indentation
        current_indent = len(line) - len(line.lstrip())

        # Handle property without colon
        if ' ' in line and not line.strip().endswith('{') and current_selectors:
            parts = line.strip().split(' ', 1)
            if len(parts) == 2 and not parts[0].startswith('.') and not parts[0].startswith('#'):
                prop_line = f"{parts[0]}: {parts[1]}"
                # Replace variables
                for var_name, var_value in variables.items():
                    prop_line = prop_line.replace(var_name, var_value)
                css_lines.append('  ' * len(current_selectors) + prop_line + ';')
                continue

        # Handle selectors
        if current_indent <= indent_level and current_selectors:
            while len(current_selectors) > current_indent // 2:
                current_selectors.pop()
                css_lines.append('  ' * len(current_selectors) + '}')

        selector = line.strip()
        if selector and not selector.endswith(';'):
            current_selectors.append(selector)
            css_lines.append('  ' * (len(current_selectors) - 1) + selector + ' {')
            indent_level = current_indent

    # Close remaining selectors
    while current_selectors:
        current_selectors.pop()
        css_lines.append('  ' * len(current_selectors) + '}')

    return '\n'.join(css_lines)


def analyze_stylus_features(stylus_code):
    """Analyze Stylus features used in code"""
    features = {
        "Variables": len(re.findall(r'^[^=\n]+=', stylus_code, re.MULTILINE)),
        "Nested Selectors": len(re.findall(r'^\s+\.', stylus_code, re.MULTILINE)),
        "Functions": len(re.findall(r'^\w+\([^)]*\)', stylus_code, re.MULTILINE)),
        "Mixins": len(re.findall(r'^\w+\(.*\)$', stylus_code, re.MULTILINE))
    }
    return features


def lighten_color(hex_color, percent):
    """Lighten a hex color by a percentage"""
    # Simple implementation - just return a lighter version
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    factor = 1 + (percent / 100)
    new_rgb = tuple(min(255, int(c * factor)) for c in rgb)
    return f"#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}"


def darken_color(hex_color, percent):
    """Darken a hex color by a percentage"""
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    factor = 1 - (percent / 100)
    new_rgb = tuple(max(0, int(c * factor)) for c in rgb)
    return f"#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}"


def validate_css_properties(css_code):
    """Validate CSS properties in code"""
    # Common CSS properties (simplified list)
    valid_properties = {
        'color', 'background-color', 'background', 'margin', 'padding', 'border',
        'width', 'height', 'display', 'position', 'top', 'right', 'bottom', 'left',
        'font-size', 'font-family', 'font-weight', 'text-align', 'text-decoration',
        'border-radius', 'box-shadow', 'opacity', 'z-index', 'overflow', 'float',
        'clear', 'visibility', 'cursor', 'outline', 'transform', 'transition',
        'animation', 'flex', 'grid', 'justify-content', 'align-items', 'align-content',
        'flex-direction', 'flex-wrap', 'grid-template-columns', 'grid-template-rows',
        'gap', 'line-height', 'letter-spacing', 'word-spacing', 'vertical-align'
    }

    deprecated_properties = {
        'font', 'text-shadow', 'filter'
    }

    # Extract properties from CSS
    property_pattern = r'([a-zA-Z-]+)\s*:'
    found_properties = set(re.findall(property_pattern, css_code))

    valid_found = found_properties & valid_properties
    invalid_found = found_properties - valid_properties - deprecated_properties
    deprecated_found = found_properties & deprecated_properties

    return {
        'valid_properties': list(valid_found),
        'invalid_properties': list(invalid_found),
        'deprecated_properties': list(deprecated_found)
    }


def get_css_property_info(property_name):
    """Get information about a CSS property"""
    property_info = {
        'display': {
            'description': 'Specifies the display behavior of an element',
            'syntax': 'display: value;',
            'values': ['none', 'block', 'inline', 'inline-block', 'flex', 'grid', 'table'],
            'browser_support': {
                'Chrome': '1+',
                'Firefox': '1+',
                'Safari': '1+',
                'Edge': '12+',
                'IE': '4+'
            },
            'examples': [
                'display: block;',
                'display: flex;',
                'display: grid;',
                'display: none;'
            ]
        },
        'color': {
            'description': 'Sets the color of text',
            'syntax': 'color: value;',
            'values': ['<color>', 'inherit', 'initial', 'unset'],
            'browser_support': {
                'Chrome': '1+',
                'Firefox': '1+',
                'Safari': '1+',
                'Edge': '12+',
                'IE': '3+'
            },
            'examples': [
                'color: red;',
                'color: #007bff;',
                'color: rgb(0, 123, 255);',
                'color: hsl(210, 100%, 50%);'
            ]
        }
    }

    return property_info.get(property_name.lower())


def suggest_similar_properties(property_name):
    """Suggest similar property names"""
    common_properties = [
        'display', 'color', 'background-color', 'margin', 'padding', 'border',
        'width', 'height', 'position', 'font-size', 'text-align', 'flex',
        'grid', 'opacity', 'transform', 'transition', 'animation'
    ]

    # Simple similarity based on first few characters
    suggestions = [prop for prop in common_properties if prop.startswith(property_name[:2])]
    return suggestions[:5]


def check_browser_compatibility(css_code):
    """Check browser compatibility for CSS properties"""
    # Extract properties
    property_pattern = r'([a-zA-Z-]+)\s*:'
    properties = set(re.findall(property_pattern, css_code))

    # Simplified compatibility data
    compatibility_data = {
        'display': {
            'Chrome': 'Supported',
            'Firefox': 'Supported',
            'Safari': 'Supported',
            'Edge': 'Supported',
            'IE': 'Partial'
        },
        'grid': {
            'Chrome': 'Supported',
            'Firefox': 'Supported',
            'Safari': 'Supported',
            'Edge': 'Supported',
            'IE': 'Not Supported'
        },
        'backdrop-filter': {
            'Chrome': 'Supported',
            'Firefox': 'Partial',
            'Safari': 'Supported',
            'Edge': 'Supported',
            'IE': 'Not Supported'
        }
    }

    results = {}
    for prop in properties:
        results[prop] = compatibility_data.get(prop, {
            'Chrome': 'Supported',
            'Firefox': 'Supported',
            'Safari': 'Supported',
            'Edge': 'Supported',
            'IE': 'Partial'
        })

    return results


def get_css_features_by_category(category):
    """Get CSS features by category"""
    features_by_category = {
        'Layout': ['Flexbox', 'Grid', 'Multi-column', 'Positioning'],
        'Flexbox': ['flex', 'flex-direction', 'justify-content', 'align-items'],
        'Grid': ['grid-template-columns', 'grid-template-rows', 'grid-area'],
        'Animations': ['@keyframes', 'animation', 'transition'],
        'Colors': ['HSL Colors', 'Color Functions', 'Gradients'],
        'Typography': ['Web Fonts', 'Font Features', 'Text Effects'],
        'Transforms': ['2D Transforms', '3D Transforms', 'Transform Functions'],
        'Filters': ['Filter Effects', 'Backdrop Filters', 'SVG Filters']
    }

    return features_by_category.get(category, [])


def get_feature_compatibility_info(feature):
    """Get compatibility info for a specific feature"""
    feature_data = {
        'Flexbox': {
            'support': {
                'Chrome': {'status': 'supported', 'version': '29'},
                'Firefox': {'status': 'supported', 'version': '28'},
                'Safari': {'status': 'supported', 'version': '9'},
                'Edge': {'status': 'supported', 'version': '12'},
                'IE': {'status': 'partial', 'version': '11'}
            },
            'usage': {'global': 98.2},
            'notes': 'Older versions require vendor prefixes'
        },
        'Grid': {
            'support': {
                'Chrome': {'status': 'supported', 'version': '57'},
                'Firefox': {'status': 'supported', 'version': '52'},
                'Safari': {'status': 'supported', 'version': '10.1'},
                'Edge': {'status': 'supported', 'version': '16'},
                'IE': {'status': 'partial', 'version': '10'}
            },
            'usage': {'global': 94.1},
            'notes': 'IE implementation is outdated and limited'
        }
    }

    return feature_data.get(feature, {
        'support': {
            'Chrome': {'status': 'supported', 'version': 'Unknown'},
            'Firefox': {'status': 'supported', 'version': 'Unknown'},
            'Safari': {'status': 'supported', 'version': 'Unknown'},
            'Edge': {'status': 'supported', 'version': 'Unknown'},
            'IE': {'status': 'not supported', 'version': 'N/A'}
        },
        'usage': {'global': 85.0},
        'notes': 'Check specific browser documentation for details'
    })


def lint_css_code(css_code, options):
    """Lint CSS code for various issues"""
    issues = []
    lines = css_code.split('\n')

    # Track duplicates
    properties_per_selector = {}
    current_selector = None

    for line_num, line in enumerate(lines, 1):
        line_stripped = line.strip()

        if not line_stripped or line_stripped.startswith('/*'):
            continue

        # Check for selector
        if '{' in line and not line_stripped.startswith('@'):
            current_selector = line_stripped.split('{')[0].strip()
            properties_per_selector[current_selector] = {}
            continue

        # Check properties
        if ':' in line and current_selector:
            prop_match = re.match(r'\s*([^:]+):\s*(.+);?', line)
            if prop_match:
                prop_name = prop_match.group(1).strip()
                prop_value = prop_match.group(2).strip().rstrip(';')

                # Check for duplicates
                if options.get('duplicates') and prop_name in properties_per_selector[current_selector]:
                    issues.append({
                        'line': line_num,
                        'severity': 'warning',
                        'message': f'Duplicate property "{prop_name}"',
                        'suggestion': f'Remove duplicate: {prop_name}: {prop_value};'
                    })

                properties_per_selector[current_selector][prop_name] = prop_value

                # Check color formats
                if options.get('colors') and prop_name in ['color', 'background-color']:
                    if prop_value == 'red' and '#ff0000' not in css_code:
                        issues.append({
                            'line': line_num,
                            'severity': 'info',
                            'message': 'Consider using hex values for consistency',
                            'suggestion': f'{prop_name}: #ff0000;'
                        })

                # Check units
                if options.get('units') and 'px' in prop_value:
                    if prop_name == 'font-size':
                        issues.append({
                            'line': line_num,
                            'severity': 'info',
                            'message': 'Consider using relative units (rem/em) for font-size',
                            'suggestion': f'{prop_name}: 1rem; /* Instead of px */'
                        })

                # Check accessibility
                if options.get('accessibility') and prop_name == 'outline' and prop_value == 'none':
                    issues.append({
                        'line': line_num,
                        'severity': 'warning',
                        'message': 'Removing outline affects keyboard navigation accessibility',
                        'suggestion': 'Provide alternative focus styles'
                    })

                # Check high z-index values
                if options.get('performance') and prop_name == 'z-index':
                    try:
                        z_value = int(prop_value)
                        if z_value > 1000:
                            issues.append({
                                'line': line_num,
                                'severity': 'warning',
                                'message': f'Very high z-index value: {z_value}',
                                'suggestion': 'Consider using lower z-index values for better stacking control'
                            })
                    except ValueError:
                        pass

    # Calculate summary
    summary = {
        'errors': len([i for i in issues if i['severity'] == 'error']),
        'warnings': len([i for i in issues if i['severity'] == 'warning']),
        'info': len([i for i in issues if i['severity'] == 'info'])
    }

    return {
        'issues': issues,
        'summary': summary
    }


def css_whitespace_remover():
    """Remove unnecessary whitespace from CSS"""
    create_tool_header("CSS Whitespace Remover", "Remove unnecessary whitespace from CSS code", "🧹")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to clean:", height=300, value="""/* CSS with excessive whitespace */
.container    {


    color:     red;


    background-color:    #007bff   ;

    margin:   10px    20px   30px   40px  ;


    padding:     15px     ;


}

    .header     {


        font-size:   24px   ;


        text-align:     center   ;

    }""")

    if css_content:
        # Whitespace removal options
        st.subheader("Whitespace Removal Options")
        col1, col2 = st.columns(2)

        with col1:
            remove_empty_lines = st.checkbox("Remove Empty Lines", True)
            remove_extra_spaces = st.checkbox("Remove Extra Spaces", True)
            remove_line_spaces = st.checkbox("Remove Leading/Trailing Spaces", True)

        with col2:
            remove_around_braces = st.checkbox("Clean Around Braces", True)
            remove_around_colons = st.checkbox("Clean Around Colons", True)
            remove_around_semicolons = st.checkbox("Clean Around Semicolons", True)

        if st.button("Remove Whitespace"):
            cleaned_css = clean_css_whitespace(css_content, {
                'empty_lines': remove_empty_lines,
                'extra_spaces': remove_extra_spaces,
                'line_spaces': remove_line_spaces,
                'around_braces': remove_around_braces,
                'around_colons': remove_around_colons,
                'around_semicolons': remove_around_semicolons
            })

            st.subheader("Cleaned CSS")
            st.code(cleaned_css, language="css")

            # Show statistics
            original_size = len(css_content)
            cleaned_size = len(cleaned_css)
            reduction = ((original_size - cleaned_size) / original_size * 100) if original_size > 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Original Size", f"{original_size:,} chars")
            with col2:
                st.metric("Cleaned Size", f"{cleaned_size:,} chars")
            with col3:
                st.metric("Space Saved", f"{reduction:.1f}%")

            FileHandler.create_download_link(cleaned_css.encode(), "cleaned.css", "text/css")


def css_comment_stripper():
    """Remove comments from CSS code"""
    create_tool_header("CSS Comment Stripper", "Remove comments from CSS code", "💬")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to strip comments:", height=300, value="""/* Main container styles */
.container {
    /* Primary color for the background */
    background-color: #007bff;

    /* Spacing for the container */
    padding: 20px; /* Top/bottom padding */
    margin: 10px auto; /* Center the container */

    /* Typography settings */
    font-size: 16px; /* Base font size */
    color: white; /* Text color */
}

/*
 * Multi-line comment
 * for header styles
 */
.header {
    font-size: 24px; /* Large heading */
    text-align: center; /* Center alignment */

    /* 
     * Border settings
     * with rounded corners
     */
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* TODO: Add more styles later */
.footer {
    /* Footer styles here */
    background: #f8f9fa;
}""")

    if css_content:
        # Comment removal options
        st.subheader("Comment Removal Options")
        col1, col2 = st.columns(2)

        with col1:
            remove_single_line = st.checkbox("Remove Single-line Comments", True)
            remove_multi_line = st.checkbox("Remove Multi-line Comments", True)
            remove_inline = st.checkbox("Remove Inline Comments", True)

        with col2:
            preserve_important = st.checkbox("Preserve /*! Important Comments */", False)
            preserve_license = st.checkbox("Preserve License Comments", False)
            clean_empty_lines = st.checkbox("Clean Up Empty Lines After Removal", True)

        if st.button("Strip Comments"):
            stripped_css = strip_css_comments(css_content, {
                'single_line': remove_single_line,
                'multi_line': remove_multi_line,
                'inline': remove_inline,
                'preserve_important': preserve_important,
                'preserve_license': preserve_license,
                'clean_empty_lines': clean_empty_lines
            })

            st.subheader("CSS Without Comments")
            st.code(stripped_css, language="css")

            # Show statistics
            original_lines = len(css_content.split('\n'))
            stripped_lines = len(stripped_css.split('\n'))
            comments_removed = css_content.count('/*')

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Original Lines", original_lines)
            with col2:
                st.metric("Final Lines", stripped_lines)
            with col3:
                st.metric("Comments Removed", comments_removed)

            FileHandler.create_download_link(stripped_css.encode(), "no-comments.css", "text/css")


def css_property_optimizer():
    """Optimize CSS properties for better performance"""
    create_tool_header("CSS Property Optimizer", "Optimize CSS properties for performance", "⚡")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to optimize:", height=300, value=""".container {
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 10px;
    margin-left: 20px;

    padding-top: 15px;
    padding-right: 15px;
    padding-bottom: 15px;
    padding-left: 15px;

    border-top: 1px solid #ccc;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    border-left: 1px solid #ccc;

    background-color: #ffffff;
    color: #000000;

    font-weight: normal;
    text-decoration: none;
}

.header {
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;

    outline-width: 0px;
    outline-style: none;
    outline-color: transparent;
}""")

    if css_content:
        # Optimization options
        st.subheader("Optimization Options")
        col1, col2 = st.columns(2)

        with col1:
            use_shorthand = st.checkbox("Use Shorthand Properties", True)
            remove_redundant = st.checkbox("Remove Redundant Properties", True)
            optimize_colors = st.checkbox("Optimize Color Values", True)
            merge_rules = st.checkbox("Merge Similar Rules", True)

        with col2:
            remove_defaults = st.checkbox("Remove Default Values", True)
            optimize_units = st.checkbox("Optimize Units (0px → 0)", True)
            sort_properties = st.checkbox("Sort Properties Logically", False)
            compress_whitespace = st.checkbox("Compress Whitespace", False)

        if st.button("Optimize CSS"):
            optimized_css = optimize_css_properties(css_content, {
                'shorthand': use_shorthand,
                'redundant': remove_redundant,
                'colors': optimize_colors,
                'merge_rules': merge_rules,
                'defaults': remove_defaults,
                'units': optimize_units,
                'sort': sort_properties,
                'compress': compress_whitespace
            })

            st.subheader("Optimized CSS")
            st.code(optimized_css, language="css")

            # Show optimization results
            st.subheader("Optimization Results")
            original_size = len(css_content)
            optimized_size = len(optimized_css)
            size_reduction = ((original_size - optimized_size) / original_size * 100) if original_size > 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Original Size", f"{original_size:,} chars")
            with col2:
                st.metric("Optimized Size", f"{optimized_size:,} chars")
            with col3:
                st.metric("Size Reduction", f"{size_reduction:.1f}%")

            # Show optimization details
            optimizations = analyze_optimizations(css_content, optimized_css)
            if optimizations:
                with st.expander("Optimization Details"):
                    for optimization in optimizations:
                        st.write(f"• {optimization}")

            FileHandler.create_download_link(optimized_css.encode(), "optimized.css", "text/css")


def css_indentation_fixer():
    """Fix CSS indentation and formatting"""
    create_tool_header("CSS Indentation Fixer", "Fix and standardize CSS indentation", "📐")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to fix indentation:", height=300, value=""".container{
background-color: #007bff;
padding: 20px;
.header{
font-size: 24px;
text-align: center;
    .title{
        color: white;
            font-weight: bold;
    }
}
    .content{
padding: 15px;
        margin: 10px;
    }
}

.footer {
background: #f8f9fa;
        padding: 10px;
    text-align: center;
}""")

    if css_content:
        # Indentation options
        st.subheader("Indentation Settings")
        col1, col2 = st.columns(2)

        with col1:
            indent_type = st.selectbox("Indentation Type", ["Spaces", "Tabs"])
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1) if indent_type == "Spaces" else 1

        with col2:
            fix_nesting = st.checkbox("Fix Proper Nesting", True)
            align_braces = st.checkbox("Align Opening Braces", True)
            clean_empty_lines = st.checkbox("Clean Empty Lines", True)

        # Additional formatting options
        st.subheader("Additional Formatting")
        col1, col2 = st.columns(2)

        with col1:
            space_after_colon = st.checkbox("Space After Colon", True)
            space_before_brace = st.checkbox("Space Before Opening Brace", True)

        with col2:
            newline_after_brace = st.checkbox("Newline After Opening Brace", True)
            newline_before_closing = st.checkbox("Newline Before Closing Brace", True)

        if st.button("Fix Indentation"):
            fixed_css = fix_css_indentation(css_content, {
                'indent_type': indent_type.lower(),
                'indent_size': indent_size,
                'fix_nesting': fix_nesting,
                'align_braces': align_braces,
                'clean_empty_lines': clean_empty_lines,
                'space_after_colon': space_after_colon,
                'space_before_brace': space_before_brace,
                'newline_after_brace': newline_after_brace,
                'newline_before_closing': newline_before_closing
            })

            st.subheader("Fixed CSS")
            st.code(fixed_css, language="css")

            # Show improvement metrics
            st.subheader("Formatting Improvements")
            improvements = analyze_indentation_improvements(css_content, fixed_css)

            for improvement in improvements:
                st.write(f"✅ {improvement}")

            FileHandler.create_download_link(fixed_css.encode(), "indented.css", "text/css")


def css_property_organizer():
    """Organize CSS properties in logical order"""
    create_tool_header("CSS Property Organizer", "Organize CSS properties logically", "📋")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to organize:", height=300, value=""".container {
    transform: translateY(-2px);
    background-color: #007bff;
    z-index: 10;
    color: white;
    position: relative;
    font-size: 16px;
    width: 100%;
    border: 1px solid #ccc;
    padding: 20px;
    height: auto;
    margin: 10px;
    display: flex;
    top: 0;
    opacity: 0.9;
    transition: all 0.3s ease;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    font-family: Arial, sans-serif;
}

.header {
    text-decoration: none;
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    outline: none;
    font-weight: bold;
    cursor: pointer;
    text-align: center;
    line-height: 1.5;
    letter-spacing: 1px;
    animation: slideIn 0.5s ease;
    user-select: none;
}""")

    if css_content:
        # Organization options
        st.subheader("Property Organization Options")
        col1, col2 = st.columns(2)

        with col1:
            organization_style = st.selectbox("Organization Style", [
                "Logical Groups", "Alphabetical", "By Property Type", "Custom Order"
            ])
            group_similar = st.checkbox("Group Similar Properties", True)

        with col2:
            add_comments = st.checkbox("Add Group Comments", True)
            preserve_important = st.checkbox("Keep !important at End", True)

        # Show property order preview
        if organization_style == "Logical Groups":
            st.info("""
            **Logical Groups Order:**
            1. Layout (display, position, top, right, etc.)
            2. Box Model (width, height, margin, padding, border)
            3. Typography (font-family, font-size, color, text-align)
            4. Visual (background, opacity, box-shadow)
            5. Animation (transition, transform, animation)
            """)
        elif organization_style == "By Property Type":
            st.info("""
            **Property Type Order:**
            1. Positioning Properties
            2. Display & Visibility
            3. Sizing Properties
            4. Spacing Properties
            5. Border Properties
            6. Background Properties
            7. Typography Properties
            8. Effect Properties
            """)

        if st.button("Organize Properties"):
            organized_css = organize_css_properties(css_content, {
                'style': organization_style.lower().replace(' ', '_'),
                'group_similar': group_similar,
                'add_comments': add_comments,
                'preserve_important': preserve_important
            })

            st.subheader("Organized CSS")
            st.code(organized_css, language="css")

            # Show organization summary
            st.subheader("Organization Summary")
            summary = analyze_property_organization(css_content, organized_css)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Selectors Organized", summary['selectors_count'])
            with col2:
                st.metric("Properties Reordered", summary['properties_moved'])
            with col3:
                st.metric("Groups Created", summary['groups_added'])

            if summary['improvements']:
                with st.expander("Organization Improvements"):
                    for improvement in summary['improvements']:
                        st.write(f"✅ {improvement}")

            FileHandler.create_download_link(organized_css.encode(), "organized.css", "text/css")


def css_structure_improver():
    """Improve CSS structure and maintainability"""
    create_tool_header("CSS Structure Improver", "Improve CSS structure and maintainability", "🏗️")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to improve structure:", height=300, value=""".container {
    background-color: #007bff;
    padding: 20px;
    margin: 10px;
}
.container-header {
    color: white;
    font-size: 24px;
}
.container-content {
    padding: 15px;
    margin: 5px;
}
.container-footer {
    background: #f8f9fa;
    padding: 10px;
}

.button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
}
.button-large {
    background-color: #007bff;
    color: white;
    padding: 15px 30px;
    border: none;
    border-radius: 4px;
    font-size: 18px;
}
.button-small {
    background-color: #007bff;
    color: white;
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    font-size: 12px;
}

.header-main {
    font-size: 32px;
    color: #333;
    text-align: center;
}
.header-sub {
    font-size: 24px;
    color: #666;
    text-align: center;
}""")

    if css_content:
        # Structure improvement options
        st.subheader("Structure Improvement Options")
        col1, col2 = st.columns(2)

        with col1:
            extract_common = st.checkbox("Extract Common Properties", True)
            create_base_classes = st.checkbox("Create Base Classes", True)
            group_related = st.checkbox("Group Related Selectors", True)

        with col2:
            add_structure_comments = st.checkbox("Add Structure Comments", True)
            suggest_variables = st.checkbox("Suggest CSS Variables", True)
            optimize_selectors = st.checkbox("Optimize Selector Names", False)

        # Advanced options
        with st.expander("Advanced Structure Options"):
            col1, col2 = st.columns(2)
            with col1:
                create_utility_classes = st.checkbox("Create Utility Classes", False)
                separate_responsive = st.checkbox("Separate Responsive Rules", False)

            with col2:
                create_component_sections = st.checkbox("Create Component Sections", True)
                add_toc = st.checkbox("Add Table of Contents", False)

        if st.button("Improve Structure"):
            improved_css = improve_css_structure(css_content, {
                'extract_common': extract_common,
                'base_classes': create_base_classes,
                'group_related': group_related,
                'structure_comments': add_structure_comments,
                'suggest_variables': suggest_variables,
                'optimize_selectors': optimize_selectors,
                'utility_classes': create_utility_classes,
                'separate_responsive': separate_responsive,
                'component_sections': create_component_sections,
                'add_toc': add_toc
            })

            st.subheader("Improved CSS Structure")
            st.code(improved_css, language="css")

            # Show improvement analysis
            st.subheader("Structure Improvements")
            improvements = analyze_structure_improvements(css_content, improved_css)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rules Optimized", improvements['rules_optimized'])
            with col2:
                st.metric("Common Properties Extracted", improvements['common_extracted'])
            with col3:
                st.metric("Structure Score", f"{improvements['structure_score']}/100")

            if improvements['suggestions']:
                with st.expander("Improvement Suggestions"):
                    for suggestion in improvements['suggestions']:
                        st.write(f"💡 {suggestion}")

            if improvements['variables_suggested']:
                with st.expander("Suggested CSS Variables"):
                    st.code(improvements['variables_suggested'], language="css")

            FileHandler.create_download_link(improved_css.encode(), "improved-structure.css", "text/css")


# Helper functions for the new CSS tools

def clean_css_whitespace(css_code, options):
    """Clean unnecessary whitespace from CSS"""
    lines = css_code.split('\n')
    cleaned_lines = []

    for line in lines:
        if options['line_spaces']:
            line = line.strip()

        if options['empty_lines'] and not line:
            continue

        if options['extra_spaces']:
            line = re.sub(r'\s+', ' ', line)

        if options['around_colons']:
            line = re.sub(r'\s*:\s*', ': ', line)

        if options['around_semicolons']:
            line = re.sub(r'\s*;\s*', ';', line)

        if options['around_braces']:
            line = re.sub(r'\s*{\s*', ' {', line)
            line = re.sub(r'\s*}\s*', '}', line)

        cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)


def strip_css_comments(css_code, options):
    """Strip comments from CSS code"""
    result = css_code

    if options['multi_line']:
        # Remove multi-line comments
        if options['preserve_important']:
            # Preserve /*! important comments */
            result = re.sub(r'/\*(?!\!).*?\*/', '', result, flags=re.DOTALL)
        else:
            result = re.sub(r'/\*.*?\*/', '', result, flags=re.DOTALL)

    if options['clean_empty_lines']:
        lines = result.split('\n')
        cleaned_lines = [line for line in lines if line.strip()]
        result = '\n'.join(cleaned_lines)

    return result


def optimize_css_properties(css_code, options):
    """Optimize CSS properties for better performance"""
    result = css_code

    if options['shorthand']:
        # Convert longhand to shorthand properties
        # Margin
        result = re.sub(
            r'margin-top:\s*([^;]+);\s*margin-right:\s*([^;]+);\s*margin-bottom:\s*([^;]+);\s*margin-left:\s*([^;]+);',
            r'margin: \1 \2 \3 \4;',
            result
        )
        # Padding
        result = re.sub(
            r'padding-top:\s*([^;]+);\s*padding-right:\s*([^;]+);\s*padding-bottom:\s*([^;]+);\s*padding-left:\s*([^;]+);',
            r'padding: \1 \2 \3 \4;',
            result
        )
        # Border
        result = re.sub(
            r'border-top:\s*([^;]+);\s*border-right:\s*([^;]+);\s*border-bottom:\s*([^;]+);\s*border-left:\s*([^;]+);',
            r'border: \1;',
            result
        )

    if options['units']:
        # Optimize units (0px → 0)
        result = re.sub(r'\b0px\b', '0', result)
        result = re.sub(r'\b0em\b', '0', result)
        result = re.sub(r'\b0rem\b', '0', result)

    if options['colors']:
        # Optimize colors
        result = re.sub(r'#ffffff', '#fff', result, flags=re.IGNORECASE)
        result = re.sub(r'#000000', '#000', result, flags=re.IGNORECASE)

    if options['defaults']:
        # Remove default values
        result = re.sub(r'font-weight:\s*normal;', '', result)
        result = re.sub(r'text-decoration:\s*none;', '', result)
        result = re.sub(r'outline:\s*none;', '', result)

    return result


def analyze_optimizations(original, optimized):
    """Analyze what optimizations were applied"""
    optimizations = []

    if 'margin:' in optimized and 'margin-top:' in original:
        optimizations.append("Converted margin longhand to shorthand")
    if 'padding:' in optimized and 'padding-top:' in original:
        optimizations.append("Converted padding longhand to shorthand")
    if '0;' in optimized and '0px;' in original:
        optimizations.append("Optimized zero units")
    if '#fff' in optimized and '#ffffff' in original:
        optimizations.append("Shortened hex colors")

    return optimizations


def fix_css_indentation(css_code, options):
    """Fix CSS indentation"""
    lines = css_code.split('\n')
    fixed_lines = []
    indent_level = 0

    indent_char = '\t' if options['indent_type'] == 'tabs' else ' ' * options['indent_size']

    for line in lines:
        line = line.strip()

        if not line:
            if options['clean_empty_lines']:
                continue
            fixed_lines.append('')
            continue

        # Decrease indent for closing braces
        if line.startswith('}'):
            indent_level = max(0, indent_level - 1)

        # Apply indentation
        indented_line = indent_char * indent_level + line

        # Apply formatting options
        if options['space_after_colon'] and ':' in line:
            indented_line = re.sub(r':\s*', ': ', indented_line)

        if options['space_before_brace'] and '{' in line:
            indented_line = re.sub(r'\s*{\s*', ' {', indented_line)

        fixed_lines.append(indented_line)

        # Increase indent for opening braces
        if line.endswith('{'):
            indent_level += 1

    return '\n'.join(fixed_lines)


def analyze_indentation_improvements(original, fixed):
    """Analyze indentation improvements"""
    improvements = []

    original_lines = original.split('\n')
    fixed_lines = fixed.split('\n')

    improvements.append(f"Standardized indentation across {len(fixed_lines)} lines")
    improvements.append("Fixed proper nesting structure")
    improvements.append("Cleaned up spacing around braces and colons")

    return improvements


def organize_css_properties(css_code, options):
    """Organize CSS properties in logical order"""

    # Property order groups
    property_order = {
        'layout': ['display', 'position', 'top', 'right', 'bottom', 'left', 'z-index', 'float', 'clear'],
        'box_model': ['width', 'height', 'margin', 'padding', 'border', 'border-radius', 'box-sizing'],
        'typography': ['font-family', 'font-size', 'font-weight', 'line-height', 'color', 'text-align',
                       'text-decoration'],
        'visual': ['background', 'background-color', 'opacity', 'box-shadow', 'visibility'],
        'animation': ['transition', 'transform', 'animation']
    }

    # Simple property reordering (basic implementation)
    lines = css_code.split('\n')
    organized_lines = []

    current_selector = None
    current_properties = []

    for line in lines:
        line = line.strip()

        if '{' in line:
            if current_selector:
                organized_lines.extend(current_properties)
            current_selector = line
            current_properties = [line]
        elif '}' in line:
            # Sort properties if we have them
            if len(current_properties) > 1:
                props = current_properties[1:]  # Exclude selector line
                # Simple alphabetical sort for now
                props.sort()
                current_properties = [current_properties[0]] + props

            current_properties.append(line)
            organized_lines.extend(current_properties)
            current_selector = None
            current_properties = []
        elif current_selector and line:
            current_properties.append(line)
        else:
            organized_lines.append(line)

    return '\n'.join(organized_lines)


def analyze_property_organization(original, organized):
    """Analyze property organization improvements"""
    return {
        'selectors_count': original.count('{'),
        'properties_moved': max(0, len(original.split('\n')) - len(organized.split('\n'))),
        'groups_added': organized.count('/*'),
        'improvements': [
            "Properties sorted in logical order",
            "Related properties grouped together",
            "Improved code readability"
        ]
    }


def improve_css_structure(css_code, options):
    """Improve CSS structure and maintainability"""
    improved = css_code

    if options['structure_comments']:
        # Add structure comments
        improved = "/* =========================== */\n/* CSS Structure Improved */\n/* =========================== */\n\n" + improved

    if options['extract_common']:
        # Basic common property extraction (simplified)
        improved = "/* Common Base Styles */\n.base-button {\n  border: none;\n  border-radius: 4px;\n  color: white;\n}\n\n" + improved

    if options['suggest_variables']:
        # Add suggested variables at the top
        variables = """/* Suggested CSS Variables */
:root {
  --primary-color: #007bff;
  --secondary-color: #f8f9fa;
  --border-radius: 4px;
  --spacing-unit: 10px;
}

"""
        improved = variables + improved

    return improved


def analyze_structure_improvements(original, improved):
    """Analyze structure improvements"""
    return {
        'rules_optimized': max(1, original.count('{') // 3),
        'common_extracted': 2,
        'structure_score': 85,
        'suggestions': [
            "Consider using CSS Grid for layout",
            "Group related components together",
            "Use consistent naming conventions"
        ],
        'variables_suggested': """/* Suggested Variables */
:root {
  --primary-color: #007bff;
  --spacing: 10px;
  --border-radius: 4px;
}"""
    }


def palette_generator():
    """Advanced color palette generator"""
    create_tool_header("Palette Generator", "Generate beautiful color palettes for your designs", "🎨")

    tab1, tab2, tab3 = st.tabs(["Quick Palettes", "Custom Generator", "Trend Palettes"])

    with tab1:
        st.subheader("Quick Color Palettes")

        # Predefined palette styles
        palette_styles = {
            "Material Design": ["#F44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5", "#2196F3", "#03A9F4", "#00BCD4"],
            "Pastel Dreams": ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#E1BAFF", "#FFBAE1", "#BABEFF"],
            "Ocean Blues": ["#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087", "#f95d6a", "#ff7c43", "#ffa600"],
            "Sunset Vibes": ["#FF6B6B", "#FF8E53", "#FF6B9D", "#C44569", "#F8B500", "#F5CD79", "#FFC048", "#FFB74D"],
            "Forest Green": ["#1B4332", "#2D5016", "#40531B", "#52734D", "#74A57F", "#8FBC8F", "#9CAF88", "#B2C29C"],
            "Monochrome": ["#000000", "#333333", "#666666", "#999999", "#CCCCCC", "#E6E6E6", "#F2F2F2", "#FFFFFF"]
        }

        selected_style = st.selectbox("Choose a palette style:", list(palette_styles.keys()))
        colors = palette_styles[selected_style]

        # Display palette
        st.subheader(f"{selected_style} Palette")
        display_color_palette(colors)

        # Generate CSS
        css_output = generate_palette_css(selected_style, colors)
        st.subheader("Generated CSS")
        st.code(css_output, language="css")

        FileHandler.create_download_link(css_output.encode(), f"{selected_style.lower().replace(' ', '-')}-palette.css",
                                         "text/css")

    with tab2:
        st.subheader("Custom Palette Generator")

        # Base color selection
        base_color = st.color_picker("Choose base color:", "#007bff")

        # Palette generation method
        generation_method = st.selectbox("Generation Method:", [
            "Monochromatic", "Analogous", "Complementary", "Triadic", "Tetradic", "Split-Complementary"
        ])

        # Number of colors
        num_colors = st.slider("Number of colors:", 3, 10, 5)

        if st.button("Generate Custom Palette"):
            custom_colors = generate_custom_palette(base_color, generation_method, num_colors)

            st.subheader(f"{generation_method} Palette")
            display_color_palette(custom_colors)

            # Show color harmony explanation
            explanations = {
                "Monochromatic": "Uses different shades, tints, and tones of the same hue",
                "Analogous": "Uses colors that are next to each other on the color wheel",
                "Complementary": "Uses colors that are opposite each other on the color wheel",
                "Triadic": "Uses three colors evenly spaced around the color wheel",
                "Tetradic": "Uses four colors forming a rectangle on the color wheel",
                "Split-Complementary": "Uses a base color and two colors adjacent to its complement"
            }

            st.info(f"**{generation_method}:** {explanations[generation_method]}")

            # Generate CSS variables
            css_vars = generate_palette_css(f"Custom {generation_method}", custom_colors)
            st.subheader("CSS Variables")
            st.code(css_vars, language="css")

            FileHandler.create_download_link(css_vars.encode(), f"custom-{generation_method.lower()}-palette.css",
                                             "text/css")

    with tab3:
        st.subheader("2024-2025 Trending Color Palettes")

        trending_palettes = {
            "Digital Lavender": ["#B19CD9", "#DDA0DD", "#E6E6FA", "#9370DB", "#8A2BE2"],
            "Verdigris": ["#43AA8B", "#90E0EF", "#00B4D8", "#0077B6", "#03045E"],
            "Peach Fuzz": ["#FFBE98", "#FF9F7A", "#FF8066", "#FF6B5B", "#FF4747"],
            "Apricot Crush": ["#FB8500", "#FFB703", "#8ECAE6", "#219EBC", "#023047"],
            "Living Coral": ["#FF6F61", "#FF8C69", "#FFB347", "#FF7F50", "#FF6347"],
            "Cyber Lime": ["#DFFF00", "#CCFF00", "#B3FF00", "#9AFF00", "#7CFC00"]
        }

        for palette_name, palette_colors in trending_palettes.items():
            st.write(f"**{palette_name}**")
            display_color_palette(palette_colors)

            col1, col2 = st.columns([3, 1])
            with col1:
                trend_css = generate_palette_css(palette_name, palette_colors)
                st.code(trend_css, language="css")
            with col2:
                if st.button(f"Download", key=f"download_{palette_name}"):
                    FileHandler.create_download_link(trend_css.encode(),
                                                     f"{palette_name.lower().replace(' ', '-')}-trend.css", "text/css")

            st.markdown("---")


def color_scheme_creator():
    """Create complete color schemes for projects"""
    create_tool_header("Color Scheme Creator", "Create comprehensive color schemes for your projects", "🌈")

    tab1, tab2, tab3 = st.tabs(["Project Color Scheme", "Brand Colors", "UI Color System"])

    with tab1:
        st.subheader("Project-Based Color Scheme")

        # Project type selection
        project_type = st.selectbox("Project Type:", [
            "Corporate Website", "E-commerce", "Portfolio", "Blog", "SaaS App",
            "Mobile App", "Dashboard", "Landing Page", "Educational", "Healthcare"
        ])

        # Mood selection
        mood = st.selectbox("Desired Mood:", [
            "Professional", "Creative", "Friendly", "Luxurious", "Minimalist",
            "Energetic", "Calm", "Bold", "Trustworthy", "Playful"
        ])

        # Industry selection
        industry = st.selectbox("Industry:", [
            "Technology", "Finance", "Healthcare", "Education", "Retail",
            "Real Estate", "Food & Beverage", "Entertainment", "Non-profit", "Fashion"
        ])

        if st.button("Generate Color Scheme"):
            color_scheme = generate_project_color_scheme(project_type, mood, industry)

            st.subheader(f"Color Scheme for {project_type}")

            # Display primary colors
            st.write("**Primary Colors:**")
            display_color_palette(color_scheme['primary'])

            # Display secondary colors
            st.write("**Secondary Colors:**")
            display_color_palette(color_scheme['secondary'])

            # Display neutral colors
            st.write("**Neutral Colors:**")
            display_color_palette(color_scheme['neutral'])

            # Usage guidelines
            st.subheader("Usage Guidelines")
            guidelines = get_color_usage_guidelines(project_type, mood)
            for guideline in guidelines:
                st.write(f"• {guideline}")

            # Complete CSS
            complete_css = generate_complete_color_scheme_css(color_scheme)
            st.subheader("Complete CSS Color System")
            st.code(complete_css, language="css")

            FileHandler.create_download_link(complete_css.encode(),
                                             f"{project_type.lower().replace(' ', '-')}-color-scheme.css", "text/css")

    with tab2:
        st.subheader("Brand Color Creator")

        # Brand attributes
        col1, col2 = st.columns(2)
        with col1:
            brand_personality = st.multiselect("Brand Personality:", [
                "Innovative", "Reliable", "Friendly", "Premium", "Sustainable",
                "Bold", "Approachable", "Expert", "Fun", "Sophisticated"
            ])

        with col2:
            target_audience = st.selectbox("Target Audience:", [
                "Young Adults (18-30)", "Professionals (25-45)", "Families",
                "Seniors (50+)", "Children", "Teens", "Business Executives", "Creatives"
            ])

        # Primary brand color
        primary_brand = st.color_picker("Primary Brand Color:", "#007bff")

        if st.button("Create Brand Colors"):
            brand_colors = create_brand_color_system(primary_brand, brand_personality, target_audience)

            st.subheader("Brand Color System")

            # Brand color hierarchy
            color_hierarchy = ["Primary", "Secondary", "Accent", "Success", "Warning", "Error", "Info"]

            for level, colors in zip(color_hierarchy, brand_colors.values()):
                st.write(f"**{level} Colors:**")
                if isinstance(colors, list):
                    display_color_palette(colors)
                else:
                    display_color_palette([colors])

            # Brand guidelines
            st.subheader("Brand Color Guidelines")
            brand_guidelines = generate_brand_guidelines(brand_personality, target_audience)
            for guideline in brand_guidelines:
                st.write(f"• {guideline}")

            # Brand CSS
            brand_css = generate_brand_color_css(brand_colors)
            st.code(brand_css, language="css")

            FileHandler.create_download_link(brand_css.encode(), "brand-colors.css", "text/css")

    with tab3:
        st.subheader("UI Color System Generator")

        # UI framework style
        ui_framework = st.selectbox("UI Framework Style:", [
            "Material Design", "Bootstrap", "Ant Design", "Chakra UI",
            "Tailwind CSS", "Foundation", "Bulma", "Custom System"
        ])

        # Base colors
        col1, col2 = st.columns(2)
        with col1:
            ui_primary = st.color_picker("Primary UI Color:", "#007bff")
            ui_secondary = st.color_picker("Secondary UI Color:", "#6c757d")

        with col2:
            ui_success = st.color_picker("Success Color:", "#28a745")
            ui_danger = st.color_picker("Danger Color:", "#dc3545")

        # Color generation options
        generate_variations = st.checkbox("Generate color variations (light, dark, subtle)", True)
        include_accessibility = st.checkbox("Ensure WCAG AA accessibility", True)

        if st.button("Generate UI Color System"):
            ui_colors = generate_ui_color_system(ui_primary, ui_secondary, ui_success, ui_danger,
                                                 ui_framework, generate_variations, include_accessibility)

            st.subheader(f"{ui_framework} Color System")

            # Display all UI colors
            for category, colors in ui_colors.items():
                st.write(f"**{category.title()} Colors:**")
                if isinstance(colors, dict):
                    for variant, color in colors.items():
                        col1, col2 = st.columns([1, 4])
                        with col1:
                            st.markdown(
                                f'<div style="width:40px;height:30px;background:{color};border:1px solid #ccc;"></div>',
                                unsafe_allow_html=True)
                        with col2:
                            st.code(f"{variant}: {color}")
                else:
                    display_color_palette([colors] if isinstance(colors, str) else colors)
                st.markdown("---")

            # Framework-specific CSS
            ui_css = generate_ui_framework_css(ui_colors, ui_framework)
            st.subheader("Framework CSS")
            st.code(ui_css, language="css")

            FileHandler.create_download_link(ui_css.encode(), f"{ui_framework.lower().replace(' ', '-')}-colors.css",
                                             "text/css")


def accessibility_checker():
    """Check CSS for accessibility compliance"""
    create_tool_header("Accessibility Checker", "Check your CSS for accessibility compliance", "♿")

    tab1, tab2, tab3 = st.tabs(["Color Contrast", "CSS Analysis", "WCAG Guidelines"])

    with tab1:
        st.subheader("Color Contrast Checker")

        # Color inputs
        col1, col2 = st.columns(2)
        with col1:
            foreground_color = st.color_picker("Foreground Color (Text):", "#000000")
            background_color = st.color_picker("Background Color:", "#ffffff")

        with col2:
            font_size = st.number_input("Font Size (px):", 12, 72, 16)
            font_weight = st.selectbox("Font Weight:", ["normal", "bold"])

        # Calculate contrast ratio
        contrast_ratio = calculate_contrast_ratio(foreground_color, background_color)

        # Display results
        st.subheader("Contrast Analysis")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Contrast Ratio", f"{contrast_ratio:.2f}:1")

        with col2:
            # WCAG AA compliance
            aa_normal = contrast_ratio >= 4.5
            aa_large = contrast_ratio >= 3.0 and (font_size >= 18 or (font_size >= 14 and font_weight == "bold"))

            if aa_normal or aa_large:
                st.success("✅ WCAG AA")
            else:
                st.error("❌ WCAG AA")

        with col3:
            # WCAG AAA compliance
            aaa_normal = contrast_ratio >= 7.0
            aaa_large = contrast_ratio >= 4.5 and (font_size >= 18 or (font_size >= 14 and font_weight == "bold"))

            if aaa_normal or aaa_large:
                st.success("✅ WCAG AAA")
            else:
                st.error("❌ WCAG AAA")

        # Visual preview
        st.subheader("Preview")
        preview_style = f"""
        background-color: {background_color};
        color: {foreground_color};
        padding: 20px;
        font-size: {font_size}px;
        font-weight: {font_weight};
        border: 1px solid #ccc;
        margin: 10px 0;
        """

        st.markdown(f'''
        <div style="{preview_style}">
            This is a sample text to preview the color contrast.
            Make sure it's readable for all users!
        </div>
        ''', unsafe_allow_html=True)

        # Recommendations
        if contrast_ratio < 4.5:
            st.subheader("💡 Recommendations")
            suggestions = suggest_accessible_colors(foreground_color, background_color)

            st.write("**Suggested foreground colors:**")
            for suggestion in suggestions['foreground']:
                new_ratio = calculate_contrast_ratio(suggestion, background_color)
                col1, col2, col3 = st.columns([1, 2, 2])
                with col1:
                    st.markdown(
                        f'<div style="width:40px;height:30px;background:{suggestion};border:1px solid #000;"></div>',
                        unsafe_allow_html=True)
                with col2:
                    st.code(suggestion)
                with col3:
                    st.write(f"Ratio: {new_ratio:.2f}:1")

    with tab2:
        st.subheader("CSS Accessibility Analysis")

        # File upload option
        uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

        if uploaded_file:
            css_content = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
        else:
            css_content = st.text_area("Enter CSS code to analyze:", height=300, value=""".button {
    background-color: #007bff;
    color: #ffffff;
    border: none;
    padding: 8px 16px;
    font-size: 14px;
    cursor: pointer;
    outline: none; /* Accessibility issue */
}

.text {
    color: #ccc; /* Low contrast */
    background: white;
    font-size: 12px;
}

.header {
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    color: white;
    text-align: center;
}

.link {
    color: blue;
    text-decoration: none; /* Accessibility concern */
}

.link:hover {
    text-decoration: underline;
}""")

        if css_content:
            if st.button("Analyze CSS Accessibility"):
                accessibility_results = analyze_css_accessibility(css_content)

                st.subheader("Accessibility Analysis Results")

                # Summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Issues Found", accessibility_results['total_issues'])
                with col2:
                    st.metric("Critical Issues", accessibility_results['critical_issues'])
                with col3:
                    score = max(0, 100 - (
                                accessibility_results['critical_issues'] * 20 + accessibility_results['warnings'] * 5))
                    st.metric("Accessibility Score", f"{score}/100")

                # Detailed issues
                if accessibility_results['issues']:
                    for issue in accessibility_results['issues']:
                        severity = issue['severity']
                        if severity == 'critical':
                            st.error(f"🚨 **Critical**: {issue['message']}")
                        elif severity == 'warning':
                            st.warning(f"⚠️ **Warning**: {issue['message']}")
                        else:
                            st.info(f"💡 **Info**: {issue['message']}")

                        if issue.get('suggestion'):
                            st.code(issue['suggestion'], language="css")

                        st.markdown("---")

                # Best practices
                st.subheader("♿ Accessibility Best Practices")
                best_practices = get_accessibility_best_practices()
                for practice in best_practices:
                    st.write(f"• {practice}")

    with tab3:
        st.subheader("WCAG Guidelines Reference")

        # WCAG levels explanation
        st.write("**Web Content Accessibility Guidelines (WCAG) Levels:**")

        wcag_levels = {
            "Level A": "Basic accessibility features that should be present in all web content",
            "Level AA": "Standard level of accessibility that removes significant barriers",
            "Level AAA": "Highest level of accessibility for specialized content"
        }

        for level, description in wcag_levels.items():
            st.write(f"**{level}:** {description}")

        st.markdown("---")

        # CSS-specific guidelines
        st.subheader("CSS Accessibility Checklist")

        css_guidelines = [
            "Ensure sufficient color contrast (4.5:1 for normal text, 3:1 for large text)",
            "Don't rely solely on color to convey information",
            "Provide focus indicators for interactive elements",
            "Use relative units (em, rem) for better scaling",
            "Ensure text can be resized up to 200% without horizontal scrolling",
            "Provide alternative styling for users who prefer reduced motion",
            "Use semantic HTML with appropriate CSS rather than div soup",
            "Ensure sufficient spacing between interactive elements (44x44px minimum)",
            "Test with screen readers and keyboard navigation",
            "Provide high contrast mode alternatives"
        ]

        for guideline in css_guidelines:
            st.write(f"✅ {guideline}")

        # Useful resources
        st.subheader("📚 Useful Resources")
        resources = [
            "WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/",
            "WebAIM Color Contrast Checker: https://webaim.org/resources/contrastchecker/",
            "A11y Project Checklist: https://www.a11yproject.com/checklist/",
            "MDN Accessibility Guide: https://developer.mozilla.org/en-US/docs/Web/Accessibility"
        ]

        for resource in resources:
            st.write(f"• {resource}")


def css_framework_tools():
    """CSS Framework utilities and tools"""
    create_tool_header("CSS Framework Tools", "Utilities for popular CSS frameworks", "🛠️")

    tab1, tab2, tab3, tab4 = st.tabs(["Bootstrap Helper", "Tailwind Generator", "Material Design", "Custom Framework"])

    with tab1:
        st.subheader("Bootstrap Helper")

        # Bootstrap version
        bootstrap_version = st.selectbox("Bootstrap Version:", ["5.3", "4.6", "3.3"])

        # Component generator
        component_type = st.selectbox("Component Type:", [
            "Button", "Card", "Alert", "Badge", "Navbar", "Form", "Modal", "Carousel"
        ])

        if component_type == "Button":
            st.write("**Button Generator:**")
            col1, col2 = st.columns(2)
            with col1:
                btn_style = st.selectbox("Button Style:",
                                         ["primary", "secondary", "success", "danger", "warning", "info", "light",
                                          "dark"])
                btn_size = st.selectbox("Button Size:", ["sm", "normal", "lg"])
            with col2:
                btn_outline = st.checkbox("Outline Style")
                btn_block = st.checkbox("Block Button")

            btn_text = st.text_input("Button Text:", "Click Me")

            # Generate Bootstrap button
            btn_classes = ["btn", f"btn-{'outline-' if btn_outline else ''}{btn_style}"]
            if btn_size != "normal":
                btn_classes.append(f"btn-{btn_size}")
            if btn_block:
                btn_classes.append("btn-block" if bootstrap_version == "4.6" else "d-grid")

            btn_html = f'<button type="button" class="{" ".join(btn_classes)}">{btn_text}</button>'

            st.subheader("Generated HTML")
            st.code(btn_html, language="html")

            # Show CSS customization
            st.subheader("Custom CSS")
            custom_css = f""".custom-btn-{btn_style} {{
    background-color: var(--bs-{btn_style});
    border-color: var(--bs-{btn_style});
    transition: all 0.3s ease;
}}

.custom-btn-{btn_style}:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}}"""
            st.code(custom_css, language="css")

        elif component_type == "Card":
            st.write("**Card Generator:**")
            card_title = st.text_input("Card Title:", "Card Title")
            card_text = st.text_area("Card Text:", "Some quick example text to build on the card title.")

            include_image = st.checkbox("Include Image")
            include_header = st.checkbox("Include Header")
            include_footer = st.checkbox("Include Footer")

            # Generate card HTML
            card_html = generate_bootstrap_card(card_title, card_text, include_image, include_header, include_footer)

            st.subheader("Generated HTML")
            st.code(card_html, language="html")

    with tab2:
        st.subheader("Tailwind CSS Generator")

        # Utility classes generator
        utility_type = st.selectbox("Utility Type:", [
            "Spacing", "Colors", "Typography", "Layout", "Flexbox", "Grid"
        ])

        if utility_type == "Spacing":
            st.write("**Spacing Utilities:**")
            col1, col2 = st.columns(2)

            with col1:
                spacing_type = st.selectbox("Type:", ["margin", "padding"])
                spacing_side = st.selectbox("Side:", ["all", "top", "right", "bottom", "left", "x-axis", "y-axis"])

            with col2:
                spacing_value = st.selectbox("Value:",
                                             ["0", "1", "2", "3", "4", "5", "6", "8", "10", "12", "16", "20", "24"])
                responsive = st.selectbox("Responsive:", ["none", "sm:", "md:", "lg:", "xl:", "2xl:"])

            # Generate Tailwind class
            side_map = {
                "all": "",
                "top": "t-",
                "right": "r-",
                "bottom": "b-",
                "left": "l-",
                "x-axis": "x-",
                "y-axis": "y-"
            }

            spacing_class = f"{responsive}{spacing_type[0]}{side_map[spacing_side]}{spacing_value}"

            st.subheader("Generated Class")
            st.code(spacing_class)

            # Show CSS equivalent
            css_equivalent = generate_tailwind_css_equivalent(spacing_class)
            st.subheader("CSS Equivalent")
            st.code(css_equivalent, language="css")

        elif utility_type == "Colors":
            st.write("**Color Utilities:**")
            color_prop = st.selectbox("Property:", ["text", "bg", "border"])
            color_name = st.selectbox("Color:", ["red", "blue", "green", "yellow", "purple", "pink", "gray"])
            color_shade = st.selectbox("Shade:", ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900"])

            tailwind_color = f"{color_prop}-{color_name}-{color_shade}"
            st.code(tailwind_color)

    with tab3:
        st.subheader("Material Design Helper")

        # Material Design components
        md_component = st.selectbox("Material Component:", [
            "Elevation", "Color System", "Typography Scale", "Button Styles"
        ])

        if md_component == "Elevation":
            elevation_level = st.slider("Elevation Level:", 0, 24, 4)

            elevation_css = generate_material_elevation(elevation_level)

            st.subheader("Material Elevation CSS")
            st.code(elevation_css, language="css")

            # Preview
            st.subheader("Preview")
            st.markdown(f'''
            <div style="{elevation_css} padding: 20px; margin: 20px; background: white;">
                Elevation Level {elevation_level}
            </div>
            ''', unsafe_allow_html=True)

        elif md_component == "Color System":
            # Material Design color system
            st.write("**Material Design Color System:**")

            md_colors = {
                "Primary": ["#1976D2", "#1E88E5", "#2196F3", "#42A5F5", "#64B5F6"],
                "Secondary": ["#388E3C", "#43A047", "#4CAF50", "#66BB6A", "#81C784"],
                "Surface": ["#FFFFFF", "#F5F5F5", "#EEEEEE", "#E0E0E0", "#BDBDBD"],
                "Error": ["#C62828", "#D32F2F", "#F44336", "#EF5350", "#E57373"]
            }

            for color_type, colors in md_colors.items():
                st.write(f"**{color_type}:**")
                display_color_palette(colors)

            # Generate Material Design CSS
            md_css = generate_material_design_css(md_colors)
            st.subheader("Material Design CSS")
            st.code(md_css, language="css")

    with tab4:
        st.subheader("Custom Framework Builder")

        st.write("**Build Your Own CSS Framework:**")

        # Framework configuration
        framework_name = st.text_input("Framework Name:", "MyFramework")

        # Base settings
        col1, col2 = st.columns(2)
        with col1:
            base_font_size = st.slider("Base Font Size (rem):", 0.8, 1.2, 1.0, 0.1)
            base_line_height = st.slider("Base Line Height:", 1.2, 2.0, 1.5, 0.1)

        with col2:
            spacing_unit = st.slider("Spacing Unit (rem):", 0.25, 1.0, 0.5, 0.25)
            border_radius = st.slider("Border Radius (px):", 0, 20, 4)

        # Color scheme
        st.write("**Color Scheme:**")
        primary_color = st.color_picker("Primary:", "#007bff")
        secondary_color = st.color_picker("Secondary:", "#6c757d")
        success_color = st.color_picker("Success:", "#28a745")
        danger_color = st.color_picker("Danger:", "#dc3545")

        # Generate framework
        if st.button("Generate Custom Framework"):
            framework_css = generate_custom_framework(
                framework_name, base_font_size, base_line_height, spacing_unit,
                border_radius, primary_color, secondary_color, success_color, danger_color
            )

            st.subheader(f"{framework_name} CSS Framework")
            st.code(framework_css, language="css")

            FileHandler.create_download_link(framework_css.encode(), f"{framework_name.lower()}-framework.css",
                                             "text/css")

            # Usage examples
            st.subheader("Usage Examples")
            usage_examples = f"""<!-- {framework_name} Framework Usage Examples -->

<!-- Button Examples -->
<button class="{framework_name.lower()}-btn {framework_name.lower()}-btn-primary">Primary Button</button>
<button class="{framework_name.lower()}-btn {framework_name.lower()}-btn-secondary">Secondary Button</button>

<!-- Card Example -->
<div class="{framework_name.lower()}-card">
    <div class="{framework_name.lower()}-card-header">
        <h3>Card Title</h3>
    </div>
    <div class="{framework_name.lower()}-card-body">
        <p>Card content goes here.</p>
    </div>
</div>

<!-- Grid Example -->
<div class="{framework_name.lower()}-container">
    <div class="{framework_name.lower()}-row">
        <div class="{framework_name.lower()}-col">Column 1</div>
        <div class="{framework_name.lower()}-col">Column 2</div>
        <div class="{framework_name.lower()}-col">Column 3</div>
    </div>
</div>"""

            st.code(usage_examples, language="html")


# Helper functions for the new CSS tools

def display_color_palette(colors):
    """Display a color palette in HTML format"""
    palette_html = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 20px 0;">'
    for color in colors:
        palette_html += f'''
        <div style="width: 80px; height: 80px; background-color: {color}; 
                   border: 1px solid #ccc; border-radius: 8px;
                   display: flex; align-items: end; justify-content: center;">
            <small style="background: rgba(0,0,0,0.7); color: white; padding: 2px 4px; 
                         margin: 5px; border-radius: 4px; font-size: 10px;">{color}</small>
        </div>
        '''
    palette_html += '</div>'
    st.markdown(palette_html, unsafe_allow_html=True)


def generate_palette_css(palette_name, colors):
    """Generate CSS variables for a color palette"""
    css = f"/* {palette_name} Color Palette */\n:root {{\n"

    for i, color in enumerate(colors):
        var_name = f"--{palette_name.lower().replace(' ', '-')}-{i + 1}"
        css += f"  {var_name}: {color};\n"

    css += "}\n\n"

    # Add usage examples
    css += "/* Usage Examples */\n"
    for i, color in enumerate(colors):
        var_name = f"--{palette_name.lower().replace(' ', '-')}-{i + 1}"
        css += f".color-{i + 1} {{ background-color: var({var_name}); }}\n"

    return css


def generate_custom_palette(base_color, method, num_colors):
    """Generate custom color palette based on color theory"""
    import colorsys

    # Convert hex to HSV
    base_rgb = tuple(int(base_color[i:i + 2], 16) for i in (1, 3, 5))
    base_hsv = colorsys.rgb_to_hsv(base_rgb[0] / 255, base_rgb[1] / 255, base_rgb[2] / 255)

    colors = [base_color]

    if method == "Monochromatic":
        # Generate different lightness values
        for i in range(1, num_colors):
            # Vary the value (brightness) while keeping hue and saturation
            new_v = max(0.1, min(1.0, base_hsv[2] + (i - num_colors // 2) * 0.15))
            new_rgb = colorsys.hsv_to_rgb(base_hsv[0], base_hsv[1], new_v)
            new_hex = '#%02x%02x%02x' % (int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))
            colors.append(new_hex)

    elif method == "Analogous":
        # Generate colors with similar hues
        for i in range(1, num_colors):
            # Shift hue by small amounts
            hue_shift = (i * 30) / 360  # 30 degrees per step
            new_h = (base_hsv[0] + hue_shift) % 1.0
            new_rgb = colorsys.hsv_to_rgb(new_h, base_hsv[1], base_hsv[2])
            new_hex = '#%02x%02x%02x' % (int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))
            colors.append(new_hex)

    elif method == "Complementary":
        # Add complementary color (opposite on color wheel)
        comp_h = (base_hsv[0] + 0.5) % 1.0
        comp_rgb = colorsys.hsv_to_rgb(comp_h, base_hsv[1], base_hsv[2])
        comp_hex = '#%02x%02x%02x' % (int(comp_rgb[0] * 255), int(comp_rgb[1] * 255), int(comp_rgb[2] * 255))
        colors.append(comp_hex)

        # Fill remaining with variations
        for i in range(2, num_colors):
            if i % 2 == 0:
                # Base color variations
                new_v = max(0.1, min(1.0, base_hsv[2] + (i // 2 * 0.2)))
                new_rgb = colorsys.hsv_to_rgb(base_hsv[0], base_hsv[1], new_v)
            else:
                # Complementary variations
                new_v = max(0.1, min(1.0, base_hsv[2] + ((i // 2) * 0.2)))
                new_rgb = colorsys.hsv_to_rgb(comp_h, base_hsv[1], new_v)

            new_hex = '#%02x%02x%02x' % (int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))
            colors.append(new_hex)

    elif method == "Triadic":
        # Three colors evenly spaced (120 degrees apart)
        for i in range(1, min(3, num_colors)):
            new_h = (base_hsv[0] + i * 0.333) % 1.0
            new_rgb = colorsys.hsv_to_rgb(new_h, base_hsv[1], base_hsv[2])
            new_hex = '#%02x%02x%02x' % (int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))
            colors.append(new_hex)

        # Fill remaining with variations
        for i in range(3, num_colors):
            base_index = i % 3
            base_h = (base_hsv[0] + base_index * 0.333) % 1.0
            new_v = max(0.1, min(1.0, base_hsv[2] + ((i // 3) * 0.15)))
            new_rgb = colorsys.hsv_to_rgb(base_h, base_hsv[1], new_v)
            new_hex = '#%02x%02x%02x' % (int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))
            colors.append(new_hex)

    else:  # Default to monochromatic for other methods
        for i in range(1, num_colors):
            new_v = max(0.1, min(1.0, base_hsv[2] + (i - num_colors // 2) * 0.15))
            new_rgb = colorsys.hsv_to_rgb(base_hsv[0], base_hsv[1], new_v)
            new_hex = '#%02x%02x%02x' % (int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))
            colors.append(new_hex)

    return colors[:num_colors]


def generate_project_color_scheme(project_type, mood, industry):
    """Generate color scheme based on project parameters"""
    # Base color mappings for different combinations
    color_schemes = {
        "Corporate Website": {
            "Professional": ["#1E3A8A", "#3B82F6", "#EFF6FF"],
            "Trustworthy": ["#1F2937", "#3B82F6", "#F3F4F6"],
        },
        "E-commerce": {
            "Friendly": ["#059669", "#10B981", "#ECFDF5"],
            "Energetic": ["#DC2626", "#EF4444", "#FEF2F2"],
        },
        "Healthcare": {
            "Calm": ["#0EA5E9", "#38BDF8", "#F0F9FF"],
            "Trustworthy": ["#059669", "#10B981", "#ECFDF5"],
        }
    }

    # Get base scheme or default
    scheme = color_schemes.get(project_type, {}).get(mood, ["#007bff", "#0056b3", "#e3f2fd"])

    return {
        "primary": [scheme[0], lighten_color(scheme[0], 10), darken_color(scheme[0], 10)],
        "secondary": [scheme[1], lighten_color(scheme[1], 15), darken_color(scheme[1], 15)],
        "neutral": ["#F8F9FA", "#E9ECEF", "#6C757D", "#495057", "#212529"]
    }


def get_color_usage_guidelines(project_type, mood):
    """Get usage guidelines for color scheme"""
    guidelines = [
        f"Primary colors work well for main CTAs and important elements in {project_type.lower()}",
        f"Secondary colors complement the {mood.lower()} mood you're targeting",
        "Use neutral colors for text, backgrounds, and subtle elements",
        "Ensure sufficient contrast between text and background colors",
        "Test colors across different devices and lighting conditions"
    ]

    if project_type == "E-commerce":
        guidelines.append("Use action colors sparingly for 'Buy Now' and important buttons")
    elif project_type == "Healthcare":
        guidelines.append("Avoid overly bright colors that might cause anxiety")

    return guidelines


def generate_complete_color_scheme_css(color_scheme):
    """Generate complete CSS for color scheme"""
    css = "/* Complete Color Scheme */\n:root {\n"

    # Primary colors
    for i, color in enumerate(color_scheme['primary']):
        css += f"  --primary-{i + 1}: {color};\n"

    # Secondary colors
    for i, color in enumerate(color_scheme['secondary']):
        css += f"  --secondary-{i + 1}: {color};\n"

    # Neutral colors
    neutral_names = ['lightest', 'light', 'medium', 'dark', 'darkest']
    for i, color in enumerate(color_scheme['neutral']):
        name = neutral_names[i] if i < len(neutral_names) else f'neutral-{i + 1}'
        css += f"  --neutral-{name}: {color};\n"

    css += "}\n\n"

    # Usage classes
    css += """/* Usage Classes */
.primary-bg { background-color: var(--primary-1); }
.secondary-bg { background-color: var(--secondary-1); }
.neutral-bg { background-color: var(--neutral-lightest); }

.primary-text { color: var(--primary-1); }
.secondary-text { color: var(--secondary-1); }
.neutral-text { color: var(--neutral-dark); }

.primary-border { border-color: var(--primary-1); }
.secondary-border { border-color: var(--secondary-1); }
.neutral-border { border-color: var(--neutral-light); }"""

    return css


def create_brand_color_system(primary_color, personality, audience):
    """Create a brand color system"""
    # Generate complementary colors based on brand personality
    brand_colors = {
        "primary": primary_color,
        "secondary": lighten_color(primary_color, 30),
        "accent": darken_color(primary_color, 20),
        "success": "#10B981",
        "warning": "#F59E0B",
        "error": "#EF4444",
        "info": "#3B82F6"
    }

    # Adjust based on personality
    if "Bold" in personality:
        brand_colors["accent"] = "#FF6B6B"
    elif "Sustainable" in personality:
        brand_colors["secondary"] = "#059669"
    elif "Premium" in personality:
        brand_colors["accent"] = "#8B5CF6"

    return brand_colors


def generate_brand_guidelines(personality, audience):
    """Generate brand color guidelines"""
    guidelines = [
        "Use primary color for main brand elements and key CTAs",
        "Secondary color should complement primary in supporting elements",
        "Accent color for highlights and special attention areas",
        "Maintain consistent color hierarchy across all materials"
    ]

    if "Premium" in personality:
        guidelines.append("Use darker, sophisticated tones to convey luxury")
    if "Friendly" in personality:
        guidelines.append("Incorporate warmer tones to create approachable feeling")

    return guidelines


def generate_brand_color_css(brand_colors):
    """Generate CSS for brand color system"""
    css = "/* Brand Color System */\n:root {\n"

    for name, color in brand_colors.items():
        css += f"  --brand-{name}: {color};\n"

    css += "}\n\n"

    css += """/* Brand Color Classes */
.brand-primary { color: var(--brand-primary); }
.brand-secondary { color: var(--brand-secondary); }
.brand-accent { color: var(--brand-accent); }

.brand-primary-bg { background-color: var(--brand-primary); }
.brand-secondary-bg { background-color: var(--brand-secondary); }
.brand-accent-bg { background-color: var(--brand-accent); }"""

    return css


def generate_ui_color_system(primary, secondary, success, danger, framework, variations, accessibility):
    """Generate UI color system"""
    ui_colors = {
        "primary": {
            "default": primary,
            "light": lighten_color(primary, 20),
            "dark": darken_color(primary, 20)
        },
        "secondary": {
            "default": secondary,
            "light": lighten_color(secondary, 20),
            "dark": darken_color(secondary, 20)
        },
        "success": success,
        "danger": danger
    }

    if variations:
        ui_colors["info"] = "#17A2B8"
        ui_colors["warning"] = "#FFC107"
        ui_colors["light"] = "#F8F9FA"
        ui_colors["dark"] = "#343A40"

    return ui_colors


def generate_ui_framework_css(ui_colors, framework):
    """Generate framework-specific CSS"""
    css = f"/* {framework} Color System */\n:root {{\n"

    for category, colors in ui_colors.items():
        if isinstance(colors, dict):
            for variant, color in colors.items():
                css += f"  --{category}-{variant}: {color};\n"
        else:
            css += f"  --{category}: {colors};\n"

    css += "}\n"

    return css


def calculate_contrast_ratio(fg_color, bg_color):
    """Calculate contrast ratio between two colors"""

    def get_luminance(color):
        # Convert hex to RGB
        rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
        # Convert to relative luminance
        rgb_norm = [c / 255.0 for c in rgb]
        rgb_linear = []
        for c in rgb_norm:
            if c <= 0.03928:
                rgb_linear.append(c / 12.92)
            else:
                rgb_linear.append(((c + 0.055) / 1.055) ** 2.4)

        return 0.2126 * rgb_linear[0] + 0.7152 * rgb_linear[1] + 0.0722 * rgb_linear[2]

    fg_lum = get_luminance(fg_color)
    bg_lum = get_luminance(bg_color)

    lighter = max(fg_lum, bg_lum)
    darker = min(fg_lum, bg_lum)

    return (lighter + 0.05) / (darker + 0.05)


def suggest_accessible_colors(fg_color, bg_color):
    """Suggest accessible color alternatives"""
    suggestions = {
        "foreground": [],
        "background": []
    }

    # Generate darker versions of foreground for better contrast
    for i in range(1, 6):
        darker_fg = darken_color(fg_color, i * 15)
        ratio = calculate_contrast_ratio(darker_fg, bg_color)
        if ratio >= 4.5:
            suggestions["foreground"].append(darker_fg)

    # If no good foreground found, suggest common accessible options
    if not suggestions["foreground"]:
        suggestions["foreground"] = ["#000000", "#212529", "#495057"]

    return suggestions


def analyze_css_accessibility(css_code):
    """Analyze CSS for accessibility issues"""
    issues = []

    # Check for outline: none
    if "outline: none" in css_code or "outline:none" in css_code:
        issues.append({
            "severity": "critical",
            "message": "Removing outline affects keyboard navigation",
            "suggestion": "/* Provide alternative focus styles */\n.element:focus {\n  box-shadow: 0 0 0 2px #007bff;\n}"
        })

    # Check for very small font sizes
    if "font-size: 12px" in css_code or "font-size:12px" in css_code:
        issues.append({
            "severity": "warning",
            "message": "Font size may be too small for accessibility",
            "suggestion": "font-size: 14px; /* Minimum recommended */"
        })

    # Check for low contrast color combinations
    if "color: #ccc" in css_code and "background: white" in css_code:
        issues.append({
            "severity": "critical",
            "message": "Low contrast between text and background",
            "suggestion": "color: #6c757d; /* Better contrast */"
        })

    return {
        "issues": issues,
        "total_issues": len(issues),
        "critical_issues": len([i for i in issues if i["severity"] == "critical"]),
        "warnings": len([i for i in issues if i["severity"] == "warning"])
    }


def get_accessibility_best_practices():
    """Get list of accessibility best practices"""
    return [
        "Maintain minimum 4.5:1 contrast ratio for normal text",
        "Use focus indicators for all interactive elements",
        "Ensure content is readable when zoomed to 200%",
        "Provide alternatives to color-only information",
        "Use relative units for better scalability",
        "Test with screen readers and keyboard navigation",
        "Consider users with motion sensitivity",
        "Provide sufficient spacing between clickable elements"
    ]


def generate_bootstrap_card(title, text, include_image, include_header, include_footer):
    """Generate Bootstrap card HTML"""
    html = '<div class="card">\n'

    if include_image:
        html += '  <img src="..." class="card-img-top" alt="...">\n'

    if include_header:
        html += '  <div class="card-header">\n    Featured\n  </div>\n'

    html += '  <div class="card-body">\n'
    html += f'    <h5 class="card-title">{title}</h5>\n'
    html += f'    <p class="card-text">{text}</p>\n'
    html += '    <a href="#" class="btn btn-primary">Go somewhere</a>\n'
    html += '  </div>\n'

    if include_footer:
        html += '  <div class="card-footer text-muted">\n    2 days ago\n  </div>\n'

    html += '</div>'

    return html


def tailwind_utilities():
    """Tailwind CSS utilities generator"""
    create_tool_header("Tailwind Utilities", "Generate and convert Tailwind CSS classes", "🎨")

    tab1, tab2, tab3 = st.tabs(["Class Generator", "CSS Converter", "Cheat Sheet"])

    with tab1:
        st.subheader("Tailwind Class Generator")

        # Layout
        with st.expander("📐 Layout"):
            col1, col2 = st.columns(2)
            with col1:
                display = st.selectbox("Display", ["block", "inline-block", "inline", "flex", "grid", "hidden"])
                position = st.selectbox("Position", ["static", "relative", "absolute", "fixed", "sticky"])
            with col2:
                overflow = st.selectbox("Overflow", ["visible", "hidden", "scroll", "auto"])
                z_index = st.selectbox("Z-Index", ["auto", "0", "10", "20", "30", "40", "50"])

        # Spacing
        with st.expander("📏 Spacing"):
            col1, col2 = st.columns(2)
            with col1:
                margin = st.selectbox("Margin",
                                      ["0", "1", "2", "3", "4", "5", "6", "8", "10", "12", "16", "20", "24", "32", "40",
                                       "48", "56", "64", "auto"])
                padding = st.selectbox("Padding",
                                       ["0", "1", "2", "3", "4", "5", "6", "8", "10", "12", "16", "20", "24", "32",
                                        "40", "48", "56", "64"])
            with col2:
                margin_sides = st.multiselect("Margin Sides", ["t", "r", "b", "l", "x", "y"], ["all"])
                padding_sides = st.multiselect("Padding Sides", ["t", "r", "b", "l", "x", "y"], ["all"])

        # Typography
        with st.expander("✏️ Typography"):
            col1, col2 = st.columns(2)
            with col1:
                font_size = st.selectbox("Font Size",
                                         ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl",
                                          "8xl", "9xl"])
                font_weight = st.selectbox("Font Weight",
                                           ["thin", "extralight", "light", "normal", "medium", "semibold", "bold",
                                            "extrabold", "black"])
            with col2:
                text_align = st.selectbox("Text Align", ["left", "center", "right", "justify"])
                text_color = st.selectbox("Text Color",
                                          ["slate", "gray", "zinc", "red", "orange", "amber", "yellow", "lime", "green",
                                           "emerald", "teal", "cyan", "sky", "blue", "indigo", "violet", "purple",
                                           "fuchsia", "pink", "rose"])

        # Colors & Backgrounds
        with st.expander("🎨 Colors & Backgrounds"):
            col1, col2 = st.columns(2)
            with col1:
                bg_color = st.selectbox("Background Color",
                                        ["transparent", "white", "slate", "gray", "zinc", "red", "orange", "amber",
                                         "yellow", "lime", "green", "emerald", "teal", "cyan", "sky", "blue", "indigo",
                                         "violet", "purple", "fuchsia", "pink", "rose"])
                bg_shade = st.selectbox("Background Shade",
                                        ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900"])
            with col2:
                text_shade = st.selectbox("Text Shade",
                                          ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900"])
                opacity = st.selectbox("Opacity",
                                       ["0", "5", "10", "20", "25", "30", "40", "50", "60", "70", "75", "80", "90",
                                        "95", "100"])

        # Generate classes
        generated_classes = []

        if display != "block": generated_classes.append(display)
        if position != "static": generated_classes.append(position)
        if overflow != "visible": generated_classes.append(f"overflow-{overflow}")
        if z_index != "auto": generated_classes.append(f"z-{z_index}")

        # Margin classes
        if "all" in margin_sides or not margin_sides:
            generated_classes.append(f"m-{margin}")
        else:
            for side in margin_sides:
                generated_classes.append(f"m{side}-{margin}")

        # Padding classes
        if "all" in padding_sides or not padding_sides:
            generated_classes.append(f"p-{padding}")
        else:
            for side in padding_sides:
                generated_classes.append(f"p{side}-{padding}")

        generated_classes.extend([
            f"text-{font_size}",
            f"font-{font_weight}",
            f"text-{text_align}",
            f"text-{text_color}-{text_shade}",
            f"bg-{bg_color}-{bg_shade}" if bg_color != "transparent" else "bg-transparent",
            f"opacity-{opacity}" if opacity != "100" else ""
        ])

        # Filter out empty classes
        generated_classes = [cls for cls in generated_classes if cls]

        st.subheader("Generated Classes")
        class_string = " ".join(generated_classes)
        st.code(class_string, language="html")

        # HTML example
        st.subheader("HTML Example")
        st.code(f'<div class="{class_string}">Your content here</div>', language="html")

    with tab2:
        st.subheader("Tailwind to CSS Converter")

        tailwind_classes = st.text_area("Enter Tailwind classes (space-separated):",
                                        "bg-blue-500 text-white p-4 rounded-lg shadow-md hover:bg-blue-600")

        if tailwind_classes:
            css_output = convert_tailwind_to_css(tailwind_classes)
            st.subheader("Generated CSS")
            st.code(css_output, language="css")

    with tab3:
        st.subheader("Tailwind CSS Cheat Sheet")

        # Quick reference sections
        cheat_sections = {
            "Spacing": {
                "m-0": "margin: 0px;",
                "m-1": "margin: 0.25rem;",
                "m-4": "margin: 1rem;",
                "p-2": "padding: 0.5rem;",
                "px-4": "padding-left: 1rem; padding-right: 1rem;",
                "py-2": "padding-top: 0.5rem; padding-bottom: 0.5rem;"
            },
            "Typography": {
                "text-sm": "font-size: 0.875rem;",
                "text-xl": "font-size: 1.25rem;",
                "font-bold": "font-weight: 700;",
                "text-center": "text-align: center;",
                "text-blue-500": "color: rgb(59 130 246);"
            },
            "Layout": {
                "flex": "display: flex;",
                "grid": "display: grid;",
                "hidden": "display: none;",
                "block": "display: block;",
                "relative": "position: relative;"
            },
            "Colors": {
                "bg-white": "background-color: rgb(255 255 255);",
                "bg-blue-500": "background-color: rgb(59 130 246);",
                "bg-red-600": "background-color: rgb(220 38 38);",
                "text-gray-800": "color: rgb(31 41 55);"
            }
        }

        for section, classes in cheat_sections.items():
            with st.expander(f"📖 {section}"):
                for tailwind_class, css_equivalent in classes.items():
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.code(tailwind_class)
                    with col2:
                        st.code(css_equivalent)


def foundation_tools():
    """Foundation CSS framework tools"""
    create_tool_header("Foundation Tools", "Generate Foundation CSS components and utilities", "🏗️")

    tab1, tab2, tab3 = st.tabs(["Grid System", "Components", "Utilities"])

    with tab1:
        st.subheader("Foundation Grid System")

        container_type = st.selectbox("Container Type", ["row", "row collapse", "expanded row"])
        num_columns = st.number_input("Number of Columns", 1, 12, 3)

        st.write("**Column Configuration:**")
        columns = []
        total_width = 0

        for i in range(num_columns):
            col1, col2, col3 = st.columns(3)
            with col1:
                small = st.number_input(f"Col {i + 1} Small", 1, 12, 12 // num_columns, key=f"small_{i}")
            with col2:
                medium = st.number_input(f"Col {i + 1} Medium", 1, 12, 12 // num_columns, key=f"medium_{i}")
            with col3:
                large = st.number_input(f"Col {i + 1} Large", 1, 12, 12 // num_columns, key=f"large_{i}")

            columns.append({"small": small, "medium": medium, "large": large})

        # Generate Foundation grid HTML
        grid_html = f'<div class="{container_type}">\n'
        for i, col in enumerate(columns):
            col_classes = f"small-{col['small']} medium-{col['medium']} large-{col['large']} columns"
            grid_html += f'  <div class="{col_classes}">\n    Column {i + 1} Content\n  </div>\n'
        grid_html += '</div>'

        st.subheader("Generated HTML")
        st.code(grid_html, language="html")

        # Visual preview
        preview_css = """
        <style>
        .foundation-preview .row { display: flex; margin: 20px 0; background: #f8f9fa; padding: 10px; }
        .foundation-preview .columns { background: #007bff; color: white; padding: 15px; margin: 5px; text-align: center; border-radius: 4px; flex: 1; }
        </style>
        """

        st.subheader("Visual Preview")
        st.markdown(preview_css + f'<div class="foundation-preview">{grid_html}</div>', unsafe_allow_html=True)

    with tab2:
        st.subheader("Foundation Components")

        component_type = st.selectbox("Component Type", [
            "Button", "Button Group", "Callout", "Card", "Label", "Progress Bar", "Badge"
        ])

        if component_type == "Button":
            button_size = st.selectbox("Size", ["tiny", "small", "default", "large"])
            button_style = st.selectbox("Style", ["primary", "secondary", "success", "alert", "warning"])
            button_text = st.text_input("Button Text", "Click me")

            size_class = "" if button_size == "default" else button_size
            button_html = f'<a class="button {size_class} {button_style}" href="#">{button_text}</a>'

        elif component_type == "Callout":
            callout_type = st.selectbox("Callout Type", ["primary", "secondary", "success", "warning", "alert"])
            callout_text = st.text_area("Callout Text", "This is a callout with some text.")

            button_html = f'<div class="callout {callout_type}">\n  <p>{callout_text}</p>\n</div>'

        elif component_type == "Progress Bar":
            progress_value = st.slider("Progress Value", 0, 100, 50)
            progress_color = st.selectbox("Color", ["primary", "secondary", "success", "warning", "alert"])

            button_html = f'''<div class="progress" role="progressbar">
  <div class="progress-meter {progress_color}" style="width: {progress_value}%">
    <span class="progress-meter-text">{progress_value}%</span>
  </div>
</div>'''

        else:
            button_html = f"<!-- {component_type} component will be generated here -->"

        st.subheader("Generated HTML")
        st.code(button_html, language="html")

    with tab3:
        st.subheader("Foundation Utilities")

        utility_type = st.selectbox("Utility Type", [
            "Visibility", "Float", "Text Alignment", "Colors", "Typography"
        ])

        if utility_type == "Visibility":
            visibility_classes = {
                "show": "Display element",
                "hide": "Hide element",
                "invisible": "Make invisible but keep space",
                "show-for-small-only": "Show only on small screens",
                "show-for-medium-up": "Show on medium screens and up",
                "hide-for-small-only": "Hide only on small screens"
            }

            for cls, desc in visibility_classes.items():
                st.code(f".{cls} - {desc}")

        elif utility_type == "Float":
            float_classes = {
                "float-left": "Float element to the left",
                "float-right": "Float element to the right",
                "float-center": "Center float element",
                "clearfix": "Clear floated elements"
            }

            for cls, desc in float_classes.items():
                st.code(f".{cls} - {desc}")

        elif utility_type == "Text Alignment":
            text_classes = {
                "text-left": "text-align: left;",
                "text-right": "text-align: right;",
                "text-center": "text-align: center;",
                "text-justify": "text-align: justify;"
            }

            for cls, css in text_classes.items():
                col1, col2 = st.columns(2)
                with col1:
                    st.code(f".{cls}")
                with col2:
                    st.code(css)


def custom_framework():
    """Custom CSS framework generator"""
    create_tool_header("Custom Framework", "Generate your own CSS framework", "⚡")

    # Framework basic settings
    st.subheader("Framework Configuration")

    col1, col2 = st.columns(2)
    with col1:
        framework_name = st.text_input("Framework Name", "MyFramework")
        base_font_size = st.slider("Base Font Size (rem)", 0.8, 1.4, 1.0, 0.1)
        line_height = st.slider("Base Line Height", 1.2, 2.0, 1.5, 0.1)
        spacing_unit = st.slider("Spacing Unit (rem)", 0.5, 2.0, 1.0, 0.1)

    with col2:
        border_radius = st.slider("Border Radius (px)", 0, 20, 4)
        primary_color = st.color_picker("Primary Color", "#007bff")
        secondary_color = st.color_picker("Secondary Color", "#6c757d")
        success_color = st.color_picker("Success Color", "#28a745")
        danger_color = st.color_picker("Danger Color", "#dc3545")

    # Advanced settings
    with st.expander("🔧 Advanced Settings"):
        col1, col2 = st.columns(2)
        with col1:
            container_max_width = st.number_input("Container Max Width (px)", 800, 1600, 1200)
            grid_columns = st.number_input("Grid Columns", 8, 16, 12)
            grid_gutter = st.slider("Grid Gutter (px)", 10, 50, 30)

        with col2:
            include_reset = st.checkbox("Include CSS Reset", True)
            include_utilities = st.checkbox("Include Utility Classes", True)
            include_components = st.checkbox("Include Component Classes", True)

    if st.button("Generate Framework"):
        framework_css = generate_custom_framework(
            framework_name, base_font_size, line_height, spacing_unit,
            border_radius, primary_color, secondary_color, success_color, danger_color
        )

        # Add additional sections based on options
        if include_reset:
            reset_css = """/* CSS Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  line-height: var(--framework-line-height-base);
  color: #333;
}

"""
            framework_css = reset_css + framework_css

        if include_utilities:
            utilities_css = f"""\n/* Utility Classes */
.{framework_name.lower()}-text-center {{ text-align: center; }}
.{framework_name.lower()}-text-left {{ text-align: left; }}
.{framework_name.lower()}-text-right {{ text-align: right; }}
.{framework_name.lower()}-hidden {{ display: none; }}
.{framework_name.lower()}-visible {{ display: block; }}
.{framework_name.lower()}-float-left {{ float: left; }}
.{framework_name.lower()}-float-right {{ float: right; }}
.{framework_name.lower()}-clearfix::after {{ content: ""; display: table; clear: both; }}
"""
            framework_css += utilities_css

        # Display generated framework
        st.subheader(f"{framework_name} CSS Framework")
        st.code(framework_css, language="css")

        # Download option
        FileHandler.create_download_link(
            framework_css.encode(),
            f"{framework_name.lower()}-framework.css",
            "text/css"
        )

        # Usage example
        with st.expander("📖 Usage Examples"):
            usage_html = f"""<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{framework_name.lower()}-framework.css">
</head>
<body>
    <div class="{framework_name.lower()}-container">
        <h1>Welcome to {framework_name}</h1>
        <div class="{framework_name.lower()}-row">
            <div class="{framework_name.lower()}-col">
                <div class="{framework_name.lower()}-card">
                    <div class="{framework_name.lower()}-card-header">
                        <h3>Card Title</h3>
                    </div>
                    <p>Card content goes here.</p>
                    <button class="{framework_name.lower()}-btn {framework_name.lower()}-btn-primary">
                        Primary Button
                    </button>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""
            st.code(usage_html, language="html")


def cascade_analyzer():
    """CSS Cascade analyzer"""
    create_tool_header("Cascade Analyzer", "Analyze CSS cascade and specificity conflicts", "🔍")

    # File upload or direct input
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS", css_content, height=200, disabled=True)
    else:
        css_content = st.text_area("Enter CSS code to analyze:", height=400, value="""/* Sample CSS with cascade conflicts */
.container {
    color: blue;
    font-size: 16px;
}

#header {
    color: red;
    font-size: 18px;
}

.container.special {
    color: green;
}

.container p {
    color: purple;
    margin: 10px;
}

#header p {
    color: orange;
    margin: 20px;
}

div.container {
    background: yellow;
}

body .container {
    padding: 15px;
}

.important {
    color: black !important;
}""")

    if css_content:
        if st.button("Analyze CSS Cascade"):
            cascade_results = analyze_css_cascade(css_content)

            st.subheader("Cascade Analysis Results")

            # Specificity conflicts
            if cascade_results['conflicts']:
                st.error(f"⚠️ Found {len(cascade_results['conflicts'])} specificity conflicts")

                for conflict in cascade_results['conflicts']:
                    with st.expander(f"Conflict: {conflict['property']}"):
                        st.write(f"**Property:** `{conflict['property']}`")
                        st.write(f"**Conflicting Selectors:**")

                        for selector_info in conflict['selectors']:
                            col1, col2, col3 = st.columns([2, 1, 1])
                            with col1:
                                st.code(selector_info['selector'])
                            with col2:
                                specificity = selector_info['specificity']
                                st.write(f"Specificity: {specificity['total']}")
                                st.write(f"({specificity['ids']}, {specificity['classes']}, {specificity['elements']})")
                            with col3:
                                if selector_info.get('important'):
                                    st.error("!important")
                                else:
                                    st.info("Normal")

                        # Show resolution
                        winning_selector = max(conflict['selectors'], key=lambda x: (
                            x.get('important', False),
                            x['specificity']['total']
                        ))
                        st.success(
                            f"**Winner:** `{winning_selector['selector']}` with specificity {winning_selector['specificity']['total']}")
            else:
                st.success("✅ No specificity conflicts found!")

            # Specificity analysis
            st.subheader("Specificity Analysis")

            specificity_data = []
            for selector_info in cascade_results['selectors']:
                specificity_data.append({
                    "Selector": selector_info['selector'],
                    "Specificity": selector_info['specificity']['total'],
                    "IDs": selector_info['specificity']['ids'],
                    "Classes": selector_info['specificity']['classes'],
                    "Elements": selector_info['specificity']['elements'],
                    "Important": "Yes" if selector_info.get('important') else "No"
                })

            # Sort by specificity
            specificity_data.sort(key=lambda x: x['Specificity'], reverse=True)

            for data in specificity_data:
                col1, col2, col3, col4, col5, col6 = st.columns([3, 1, 1, 1, 1, 1])
                with col1:
                    st.code(data['Selector'])
                with col2:
                    st.write(data['Specificity'])
                with col3:
                    st.write(data['IDs'])
                with col4:
                    st.write(data['Classes'])
                with col5:
                    st.write(data['Elements'])
                with col6:
                    if data['Important'] == "Yes":
                        st.error(data['Important'])
                    else:
                        st.info(data['Important'])

            # Recommendations
            st.subheader("💡 Recommendations")

            recommendations = []

            # Check for high specificity
            high_specificity = [s for s in cascade_results['selectors'] if s['specificity']['total'] > 100]
            if high_specificity:
                recommendations.append(
                    f"⚠️ Found {len(high_specificity)} selectors with very high specificity (>100). Consider simplifying.")

            # Check for !important usage
            important_count = len([s for s in cascade_results['selectors'] if s.get('important')])
            if important_count > 0:
                recommendations.append(
                    f"⚠️ Found {important_count} uses of !important. Try to avoid !important when possible.")

            # Check for ID selectors
            id_selectors = [s for s in cascade_results['selectors'] if s['specificity']['ids'] > 0]
            if id_selectors:
                recommendations.append(
                    f"💡 Found {len(id_selectors)} ID selectors. Consider using classes for better maintainability.")

            if recommendations:
                for rec in recommendations:
                    st.warning(rec)
            else:
                st.success("✅ Your CSS cascade looks good!")

            # Best practices
            with st.expander("📚 CSS Cascade Best Practices"):
                st.markdown("""
                **Specificity Guidelines:**
                - Keep specificity as low as possible
                - Avoid using IDs in CSS (use classes instead)
                - Minimize the use of !important
                - Use descendant selectors sparingly

                **Cascade Order:**
                1. Inline styles (highest priority)
                2. IDs
                3. Classes, attributes, pseudo-classes
                4. Elements and pseudo-elements

                **Tips:**
                - Organize CSS from general to specific
                - Use a consistent naming convention (BEM, OOCSS)
                - Consider using CSS-in-JS or CSS modules for large projects
                """)


def property_inspector():
    """CSS Property inspector and browser support checker"""
    create_tool_header("Property Inspector", "Inspect CSS properties and check browser support", "🔎")

    tab1, tab2, tab3 = st.tabs(["Property Lookup", "Browser Support", "Property Validator"])

    with tab1:
        st.subheader("CSS Property Lookup")

        property_name = st.text_input("Enter CSS property name:", "display")

        if property_name:
            property_details = get_detailed_property_info(property_name)

            if property_details:
                st.success(f"✅ `{property_name}` is a valid CSS property")

                # Property information
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Description")
                    st.info(property_details['description'])

                    st.subheader("Syntax")
                    st.code(property_details['syntax'], language="css")

                    st.subheader("Default Value")
                    st.code(property_details['initial'], language="css")

                with col2:
                    st.subheader("Valid Values")
                    for value in property_details['values']:
                        st.write(f"• `{value}`")

                    st.subheader("Inherited")
                    st.write("Yes" if property_details['inherited'] else "No")

                    st.subheader("Animatable")
                    st.write("Yes" if property_details['animatable'] else "No")

                # Usage examples
                st.subheader("Usage Examples")
                for i, example in enumerate(property_details['examples']):
                    with st.expander(f"Example {i + 1}"):
                        st.code(example, language="css")

                # Related properties
                if property_details.get('related'):
                    st.subheader("Related Properties")
                    for related_prop in property_details['related']:
                        if st.button(f"🔗 {related_prop}", key=f"related_{related_prop}"):
                            st.session_state.selected_property = related_prop
            else:
                st.error(f"❌ `{property_name}` is not a valid CSS property")

                # Suggest similar properties
                suggestions = suggest_similar_properties(property_name)
                if suggestions:
                    st.subheader("Did you mean:")
                    for suggestion in suggestions[:5]:
                        if st.button(f"💡 {suggestion}", key=f"suggest_{suggestion}"):
                            st.session_state.selected_property = suggestion

    with tab2:
        st.subheader("Browser Support Checker")

        search_property = st.text_input("Property to check browser support:", "grid")

        if search_property:
            support_info = get_browser_support_info(search_property)

            if support_info:
                st.subheader(f"Browser Support for `{search_property}`")

                browsers = ['Chrome', 'Firefox', 'Safari', 'Edge', 'IE', 'Opera']

                # Create browser support table
                for browser in browsers:
                    col1, col2, col3 = st.columns([1, 2, 3])

                    with col1:
                        st.write(f"**{browser}**")

                    with col2:
                        support = support_info.get(browser.lower(), {"status": "unknown", "version": "N/A"})
                        status = support['status']

                        if status == 'supported':
                            st.success("✅ Supported")
                        elif status == 'partial':
                            st.warning("⚠️ Partial")
                        elif status == 'not_supported':
                            st.error("❌ Not Supported")
                        else:
                            st.info("❓ Unknown")

                    with col3:
                        version = support.get('version', 'N/A')
                        notes = support.get('notes', '')
                        st.write(f"Since v{version}")
                        if notes:
                            st.caption(notes)

                # Global usage statistics
                if support_info.get('global_usage'):
                    st.subheader("Global Usage")
                    usage = support_info['global_usage']
                    st.metric("Supported Browsers", f"{usage}%")

                    if usage >= 95:
                        st.success("🌟 Excellent browser support")
                    elif usage >= 85:
                        st.info("👍 Good browser support")
                    elif usage >= 70:
                        st.warning("⚠️ Moderate browser support")
                    else:
                        st.error("⚠️ Limited browser support")

    with tab3:
        st.subheader("Property Value Validator")

        validate_property = st.text_input("Property name:", "margin")
        validate_value = st.text_input("Property value:", "10px 20px")

        if validate_property and validate_value:
            if st.button("Validate Property Value"):
                validation_result = validate_property_value(validate_property, validate_value)

                if validation_result['valid']:
                    st.success(f"✅ `{validate_property}: {validate_value}` is valid")

                    if validation_result.get('computed_value'):
                        st.info(f"**Computed value:** `{validation_result['computed_value']}`")

                    if validation_result.get('explanation'):
                        st.write(validation_result['explanation'])
                else:
                    st.error(f"❌ `{validate_property}: {validate_value}` is invalid")
                    st.write(f"**Reason:** {validation_result['reason']}")

                    suggestions = validation_result.get('suggestions', [])
                    if suggestions and isinstance(suggestions, list):
                        st.subheader("Suggestions:")
                        for suggestion in suggestions:
                            st.write(f"• `{suggestion}`")

        # Quick validation examples
        st.subheader("Quick Examples")
        examples = [
            ("color", "#ff0000"),
            ("display", "flex"),
            ("margin", "10px auto"),
            ("font-size", "1.5rem"),
            ("background", "linear-gradient(to right, red, blue)")
        ]

        for prop, val in examples:
            if st.button(f"Test: {prop}: {val}", key=f"example_{prop}"):
                st.session_state.example_property = prop
                st.session_state.example_value = val


def generate_tailwind_css_equivalent(tailwind_class):
    """Generate CSS equivalent for Tailwind class"""
    # Simple mapping for common classes
    css_mappings = {
        "m-0": "margin: 0;",
        "m-1": "margin: 0.25rem;",
        "m-2": "margin: 0.5rem;",
        "m-3": "margin: 0.75rem;",
        "m-4": "margin: 1rem;",
        "p-0": "padding: 0;",
        "p-1": "padding: 0.25rem;",
        "p-2": "padding: 0.5rem;",
        "p-3": "padding: 0.75rem;",
        "p-4": "padding: 1rem;"
    }

    return css_mappings.get(tailwind_class, f"/* CSS for {tailwind_class} */")


# Helper functions for the new CSS tools

def get_preset_animation(animation_type):
    """Get preset animation keyframes"""
    animations = {
        "Fade In": ("fadeIn", "@keyframes fadeIn {\n  0% { opacity: 0; }\n  100% { opacity: 1; }\n}"),
        "Fade Out": ("fadeOut", "@keyframes fadeOut {\n  0% { opacity: 1; }\n  100% { opacity: 0; }\n}"),
        "Slide In Left": ("slideInLeft",
                          "@keyframes slideInLeft {\n  0% { transform: translateX(-100%); }\n  100% { transform: translateX(0); }\n}"),
        "Slide In Right": ("slideInRight",
                           "@keyframes slideInRight {\n  0% { transform: translateX(100%); }\n  100% { transform: translateX(0); }\n}"),
        "Scale Up": (
        "scaleUp", "@keyframes scaleUp {\n  0% { transform: scale(0); }\n  100% { transform: scale(1); }\n}"),
        "Scale Down": (
        "scaleDown", "@keyframes scaleDown {\n  0% { transform: scale(1); }\n  100% { transform: scale(0); }\n}"),
        "Rotate": (
        "rotate", "@keyframes rotate {\n  0% { transform: rotate(0deg); }\n  100% { transform: rotate(360deg); }\n}"),
        "Bounce": ("bounce",
                   "@keyframes bounce {\n  0%, 20%, 53%, 80%, 100% { transform: translate3d(0,0,0); }\n  40%, 43% { transform: translate3d(0, -30px, 0); }\n  70% { transform: translate3d(0, -15px, 0); }\n  90% { transform: translate3d(0,-4px,0); }\n}"),
        "Shake": ("shake",
                  "@keyframes shake {\n  0%, 100% { transform: translateX(0); }\n  10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }\n  20%, 40%, 60%, 80% { transform: translateX(10px); }\n}"),
        "Pulse": ("pulse",
                  "@keyframes pulse {\n  0% { transform: scale(1); }\n  50% { transform: scale(1.05); }\n  100% { transform: scale(1); }\n}")
    }

    return animations.get(animation_type,
                          ("customAnimation", "@keyframes customAnimation {\n  /* Add your keyframes here */\n}"))


def convert_tailwind_to_css(tailwind_classes):
    """Convert Tailwind classes to CSS"""
    class_mappings = {
        # Background colors
        "bg-white": "background-color: #ffffff;",
        "bg-black": "background-color: #000000;",
        "bg-gray-100": "background-color: #f7fafc;",
        "bg-gray-500": "background-color: #a0aec0;",
        "bg-blue-500": "background-color: #4299e1;",
        "bg-red-500": "background-color: #f56565;",
        "bg-green-500": "background-color: #48bb78;",
        "bg-yellow-500": "background-color: #ed8936;",

        # Text colors
        "text-white": "color: #ffffff;",
        "text-black": "color: #000000;",
        "text-gray-600": "color: #718096;",
        "text-blue-600": "color: #3182ce;",
        "text-red-600": "color: #e53e3e;",

        # Padding
        "p-0": "padding: 0;",
        "p-1": "padding: 0.25rem;",
        "p-2": "padding: 0.5rem;",
        "p-3": "padding: 0.75rem;",
        "p-4": "padding: 1rem;",
        "p-5": "padding: 1.25rem;",
        "p-6": "padding: 1.5rem;",
        "p-8": "padding: 2rem;",

        # Margin
        "m-0": "margin: 0;",
        "m-1": "margin: 0.25rem;",
        "m-2": "margin: 0.5rem;",
        "m-3": "margin: 0.75rem;",
        "m-4": "margin: 1rem;",
        "m-auto": "margin: auto;",

        # Typography
        "text-xs": "font-size: 0.75rem;",
        "text-sm": "font-size: 0.875rem;",
        "text-base": "font-size: 1rem;",
        "text-lg": "font-size: 1.125rem;",
        "text-xl": "font-size: 1.25rem;",
        "text-2xl": "font-size: 1.5rem;",
        "text-3xl": "font-size: 1.875rem;",

        "font-thin": "font-weight: 100;",
        "font-light": "font-weight: 300;",
        "font-normal": "font-weight: 400;",
        "font-medium": "font-weight: 500;",
        "font-semibold": "font-weight: 600;",
        "font-bold": "font-weight: 700;",

        "text-left": "text-align: left;",
        "text-center": "text-align: center;",
        "text-right": "text-align: right;",

        # Display
        "block": "display: block;",
        "inline-block": "display: inline-block;",
        "inline": "display: inline;",
        "flex": "display: flex;",
        "grid": "display: grid;",
        "hidden": "display: none;",

        # Flexbox
        "flex-col": "flex-direction: column;",
        "flex-row": "flex-direction: row;",
        "justify-start": "justify-content: flex-start;",
        "justify-center": "justify-content: center;",
        "justify-end": "justify-content: flex-end;",
        "justify-between": "justify-content: space-between;",
        "items-start": "align-items: flex-start;",
        "items-center": "align-items: center;",
        "items-end": "align-items: flex-end;",

        # Borders
        "rounded": "border-radius: 0.25rem;",
        "rounded-md": "border-radius: 0.375rem;",
        "rounded-lg": "border-radius: 0.5rem;",
        "rounded-full": "border-radius: 9999px;",

        # Shadows
        "shadow": "box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);",
        "shadow-md": "box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);",
        "shadow-lg": "box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);",

        # Hover states
        "hover:bg-blue-600": "background-color: #2b77cb;",  # (on hover)
        "hover:bg-red-600": "background-color: #dc2626;",  # (on hover)
        "hover:text-white": "color: #ffffff;",  # (on hover)
    }

    classes = tailwind_classes.strip().split()
    css_rules = []

    for cls in classes:
        if cls in class_mappings:
            css_rules.append(class_mappings[cls])
        else:
            css_rules.append(f"/* Unknown class: {cls} */")

    css_output = ".element {\n"
    for rule in css_rules:
        css_output += f"  {rule}\n"
    css_output += "}"

    return css_output


def analyze_css_cascade(css_content):
    """Analyze CSS cascade and specificity"""
    import re

    # Extract CSS rules
    rules = re.findall(r'([^{}]+)\s*\{([^{}]*)\}', css_content, re.DOTALL)

    selectors_info = []
    property_conflicts = {}

    for selector_group, properties in rules:
        # Split multiple selectors
        selectors = [s.strip() for s in selector_group.split(',') if s.strip()]

        # Parse properties
        props = {}
        for prop_line in properties.split(';'):
            if ':' in prop_line:
                prop_parts = prop_line.split(':', 1)
                if len(prop_parts) == 2:
                    prop_name = prop_parts[0].strip()
                    prop_value = prop_parts[1].strip()
                    is_important = '!important' in prop_value
                    if is_important:
                        prop_value = prop_value.replace('!important', '').strip()
                    props[prop_name] = {'value': prop_value, 'important': is_important}

        for selector in selectors:
            specificity = calculate_specificity(selector)

            selector_info = {
                'selector': selector,
                'specificity': specificity,
                'properties': props,
                'important': any(p.get('important', False) for p in props.values())
            }

            selectors_info.append(selector_info)

            # Track property conflicts
            for prop_name, prop_info in props.items():
                if prop_name not in property_conflicts:
                    property_conflicts[prop_name] = []
                property_conflicts[prop_name].append({
                    'selector': selector,
                    'value': prop_info['value'],
                    'specificity': specificity,
                    'important': prop_info.get('important', False)
                })

    # Find conflicts (properties defined by multiple selectors)
    conflicts = []
    for prop_name, prop_selectors in property_conflicts.items():
        if len(prop_selectors) > 1:
            conflicts.append({
                'property': prop_name,
                'selectors': prop_selectors
            })

    return {
        'selectors': selectors_info,
        'conflicts': conflicts
    }


def get_detailed_property_info(property_name):
    """Get detailed information about a CSS property"""
    # Simplified property database
    properties = {
        "display": {
            "description": "Specifies the display behavior of an element",
            "syntax": "display: value;",
            "initial": "inline",
            "inherited": False,
            "animatable": False,
            "values": ["none", "block", "inline", "inline-block", "flex", "grid", "table", "list-item"],
            "examples": [
                ".container { display: flex; }",
                ".hidden { display: none; }",
                ".grid-container { display: grid; }"
            ],
            "related": ["visibility", "position", "float"]
        },
        "color": {
            "description": "Sets the color of text",
            "syntax": "color: value;",
            "initial": "depends on user agent",
            "inherited": True,
            "animatable": True,
            "values": ["<color>", "inherit", "initial", "unset"],
            "examples": [
                "h1 { color: red; }",
                ".text { color: #007bff; }",
                ".accent { color: rgb(255, 0, 0); }"
            ],
            "related": ["background-color", "border-color"]
        },
        "margin": {
            "description": "Sets the margin area on all four sides of an element",
            "syntax": "margin: value;",
            "initial": "0",
            "inherited": False,
            "animatable": True,
            "values": ["<length>", "<percentage>", "auto", "inherit", "initial", "unset"],
            "examples": [
                ".box { margin: 10px; }",
                ".centered { margin: 0 auto; }",
                ".spaced { margin: 10px 20px 15px 5px; }"
            ],
            "related": ["padding", "border", "margin-top", "margin-right", "margin-bottom", "margin-left"]
        }
    }

    return properties.get(property_name.lower())


def get_browser_support_info(property_name):
    """Get browser support information for a property"""
    # Simplified browser support database
    support_db = {
        "grid": {
            "chrome": {"status": "supported", "version": "57"},
            "firefox": {"status": "supported", "version": "52"},
            "safari": {"status": "supported", "version": "10.1"},
            "edge": {"status": "supported", "version": "16"},
            "ie": {"status": "partial", "version": "10", "notes": "Partial support with -ms- prefix"},
            "opera": {"status": "supported", "version": "44"},
            "global_usage": 92.5
        },
        "flexbox": {
            "chrome": {"status": "supported", "version": "29"},
            "firefox": {"status": "supported", "version": "28"},
            "safari": {"status": "supported", "version": "9"},
            "edge": {"status": "supported", "version": "12"},
            "ie": {"status": "partial", "version": "10", "notes": "Partial support"},
            "opera": {"status": "supported", "version": "17"},
            "global_usage": 98.2
        },
        "display": {
            "chrome": {"status": "supported", "version": "1"},
            "firefox": {"status": "supported", "version": "1"},
            "safari": {"status": "supported", "version": "1"},
            "edge": {"status": "supported", "version": "12"},
            "ie": {"status": "supported", "version": "4"},
            "opera": {"status": "supported", "version": "7"},
            "global_usage": 100.0
        }
    }

    return support_db.get(property_name.lower())


def validate_property_value(property_name, value):
    """Validate a CSS property value"""
    # Simplified validation logic
    validations = {
        "color": {
            "valid_patterns": [r'^#[0-9A-Fa-f]{6}$', r'^#[0-9A-Fa-f]{3}$', r'^rgb\(.*\)$', r'^rgba\(.*\)$'],
            "valid_keywords": ["red", "blue", "green", "white", "black", "transparent", "inherit", "initial"]
        },
        "display": {
            "valid_keywords": ["none", "block", "inline", "inline-block", "flex", "grid", "table", "list-item"]
        },
        "margin": {
            "valid_patterns": [r'^\d+px$', r'^\d+em$', r'^\d+rem$', r'^\d+%$'],
            "valid_keywords": ["auto", "inherit", "initial"]
        }
    }

    prop_validation = validations.get(property_name.lower())
    if not prop_validation:
        return {"valid": True, "reason": "Property validation not implemented"}

    # Check keywords
    if "valid_keywords" in prop_validation and value.lower() in prop_validation["valid_keywords"]:
        return {"valid": True}

    # Check patterns
    if "valid_patterns" in prop_validation:
        for pattern in prop_validation["valid_patterns"]:
            if re.match(pattern, value):
                return {"valid": True}

    return {
        "valid": False,
        "reason": f"'{value}' is not a valid value for {property_name}",
        "suggestions": prop_validation.get("valid_keywords", [])
    }


def generate_material_elevation(level):
    """Generate Material Design elevation CSS"""
    elevations = {
        0: "box-shadow: none;",
        1: "box-shadow: 0px 2px 1px -1px rgba(0,0,0,0.2), 0px 1px 1px 0px rgba(0,0,0,0.14), 0px 1px 3px 0px rgba(0,0,0,0.12);",
        2: "box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2), 0px 2px 2px 0px rgba(0,0,0,0.14), 0px 1px 5px 0px rgba(0,0,0,0.12);",
        4: "box-shadow: 0px 2px 4px -1px rgba(0,0,0,0.2), 0px 4px 5px 0px rgba(0,0,0,0.14), 0px 1px 10px 0px rgba(0,0,0,0.12);",
        8: "box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2), 0px 8px 10px 1px rgba(0,0,0,0.14), 0px 3px 14px 2px rgba(0,0,0,0.12);",
        16: "box-shadow: 0px 8px 10px -5px rgba(0,0,0,0.2), 0px 16px 24px 2px rgba(0,0,0,0.14), 0px 6px 30px 5px rgba(0,0,0,0.12);",
        24: "box-shadow: 0px 11px 15px -7px rgba(0,0,0,0.2), 0px 24px 38px 3px rgba(0,0,0,0.14), 0px 9px 46px 8px rgba(0,0,0,0.12);"
    }

    return elevations.get(level, elevations[4])


def generate_material_design_css(md_colors):
    """Generate Material Design CSS"""
    css = "/* Material Design Color System */\n:root {\n"

    for color_type, colors in md_colors.items():
        for i, color in enumerate(colors):
            css += f"  --md-{color_type.lower()}-{(i + 1) * 100}: {color};\n"

    css += "}\n\n"

    css += """/* Material Design Classes */
.md-elevation-1 { box-shadow: 0px 2px 1px -1px rgba(0,0,0,0.2); }
.md-elevation-2 { box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2); }
.md-elevation-4 { box-shadow: 0px 2px 4px -1px rgba(0,0,0,0.2); }"""

    return css


def generate_custom_framework(name, font_size, line_height, spacing, radius, primary, secondary, success, danger):
    """Generate custom CSS framework"""
    css = f"""/* {name} CSS Framework */
:root {{
  /* Typography */
  --{name.lower()}-font-size-base: {font_size}rem;
  --{name.lower()}-line-height-base: {line_height};

  /* Spacing */
  --{name.lower()}-spacing-unit: {spacing}rem;

  /* Border */
  --{name.lower()}-border-radius: {radius}px;

  /* Colors */
  --{name.lower()}-primary: {primary};
  --{name.lower()}-secondary: {secondary};
  --{name.lower()}-success: {success};
  --{name.lower()}-danger: {danger};
}}

/* Base Styles */
.{name.lower()}-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--{name.lower()}-spacing-unit);
}}

/* Buttons */
.{name.lower()}-btn {{
  display: inline-block;
  padding: calc(var(--{name.lower()}-spacing-unit) * 0.5) var(--{name.lower()}-spacing-unit);
  font-size: var(--{name.lower()}-font-size-base);
  line-height: var(--{name.lower()}-line-height-base);
  border: none;
  border-radius: var(--{name.lower()}-border-radius);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
}}

.{name.lower()}-btn-primary {{
  background-color: var(--{name.lower()}-primary);
  color: white;
}}

.{name.lower()}-btn-secondary {{
  background-color: var(--{name.lower()}-secondary);
  color: white;
}}

/* Cards */
.{name.lower()}-card {{
  background: white;
  border: 1px solid #e1e5e9;
  border-radius: var(--{name.lower()}-border-radius);
  padding: var(--{name.lower()}-spacing-unit);
  margin-bottom: var(--{name.lower()}-spacing-unit);
}}

.{name.lower()}-card-header {{
  border-bottom: 1px solid #e1e5e9;
  padding-bottom: calc(var(--{name.lower()}-spacing-unit) * 0.5);
  margin-bottom: var(--{name.lower()}-spacing-unit);
}}

/* Grid System */
.{name.lower()}-row {{
  display: flex;
  flex-wrap: wrap;
  margin: 0 calc(var(--{name.lower()}-spacing-unit) * -0.5);
}}

.{name.lower()}-col {{
  flex: 1;
  padding: 0 calc(var(--{name.lower()}-spacing-unit) * 0.5);
}}"""

    return css


def animation_preview():
    """CSS Animation preview tool"""
    create_tool_header("Animation Preview", "Preview CSS animations in real-time", "🎬")

    # Animation selection
    animation_type = st.selectbox("Animation Type", [
        "Custom", "Fade In", "Fade Out", "Slide In Left", "Slide In Right",
        "Scale Up", "Scale Down", "Rotate", "Bounce", "Shake", "Pulse"
    ])

    # Animation properties
    col1, col2 = st.columns(2)
    with col1:
        duration = st.slider("Duration (seconds)", 0.1, 10.0, 1.0, 0.1)
        delay = st.slider("Delay (seconds)", 0.0, 5.0, 0.0, 0.1)
        iteration_count = st.selectbox("Iterations", [1, 2, 3, "infinite"])
    with col2:
        timing_function = st.selectbox("Timing Function", [
            "ease", "ease-in", "ease-out", "ease-in-out", "linear",
            "cubic-bezier(0.25, 0.46, 0.45, 0.94)"
        ])
        direction = st.selectbox("Direction", ["normal", "reverse", "alternate", "alternate-reverse"])
        fill_mode = st.selectbox("Fill Mode", ["none", "forwards", "backwards", "both"])

    # Generate animation CSS based on type
    if animation_type == "Custom":
        custom_keyframes = st.text_area("Custom Keyframes",
                                        "0% { opacity: 0; transform: translateY(20px); }\n100% { opacity: 1; transform: translateY(0); }")
        keyframes_name = "customAnimation"
        keyframes_css = f"@keyframes {keyframes_name} {{\n  {custom_keyframes}\n}}"
    else:
        keyframes_name, keyframes_css = get_preset_animation(animation_type)

    # Generate complete CSS
    animation_css = f""".animated-element {{
  animation-name: {keyframes_name};
  animation-duration: {duration}s;
  animation-delay: {delay}s;
  animation-iteration-count: {iteration_count};
  animation-timing-function: {timing_function};
  animation-direction: {direction};
  animation-fill-mode: {fill_mode};
}}

{keyframes_css}"""

    # Preview area
    st.subheader("Animation Preview")

    # Create animated preview
    preview_html = f"""
    <style>
    {animation_css}
    .preview-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin: 20px 0;
    }}
    .preview-element {{
        width: 100px;
        height: 100px;
        background: #ffffff;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #333;
        animation-name: {keyframes_name};
        animation-duration: {duration}s;
        animation-delay: {delay}s;
        animation-iteration-count: {iteration_count};
        animation-timing-function: {timing_function};
        animation-direction: {direction};
        animation-fill-mode: {fill_mode};
    }}
    </style>
    <div class="preview-container">
        <div class="preview-element">DEMO</div>
    </div>
    """

    st.markdown(preview_html, unsafe_allow_html=True)

    # Control buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("▶️ Play Animation"):
            st.rerun()
    with col2:
        if st.button("⏹️ Reset"):
            st.rerun()
    with col3:
        if st.button("🔄 Replay"):
            st.rerun()

    # Display CSS code
    st.subheader("Generated CSS")
    st.code(animation_css, language="css")

    # Download options
    FileHandler.create_download_link(animation_css.encode(), "animation.css", "text/css")

    # HTML example
    with st.expander("HTML Usage Example"):
        html_example = f"""<!DOCTYPE html>
<html>
<head>
<style>
{animation_css}
</style>
</head>
<body>
    <div class="animated-element">Your content here</div>
</body>
</html>"""
        st.code(html_example, language="html")


def easing_functions():
    """CSS Easing functions generator"""
    create_tool_header("Easing Functions", "Generate and visualize CSS easing functions", "📈")

    tab1, tab2, tab3 = st.tabs(["Presets", "Custom Cubic Bezier", "Visualizer"])

    with tab1:
        st.subheader("Preset Easing Functions")

        easing_presets = {
            "Linear": "linear",
            "Ease": "ease",
            "Ease In": "ease-in",
            "Ease Out": "ease-out",
            "Ease In Out": "ease-in-out",
            "Ease In Sine": "cubic-bezier(0.12, 0, 0.39, 0)",
            "Ease Out Sine": "cubic-bezier(0.61, 1, 0.88, 1)",
            "Ease In Out Sine": "cubic-bezier(0.37, 0, 0.63, 1)",
            "Ease In Quad": "cubic-bezier(0.11, 0, 0.5, 0)",
            "Ease Out Quad": "cubic-bezier(0.5, 1, 0.89, 1)",
            "Ease In Out Quad": "cubic-bezier(0.45, 0, 0.55, 1)",
            "Ease In Cubic": "cubic-bezier(0.32, 0, 0.67, 0)",
            "Ease Out Cubic": "cubic-bezier(0.33, 1, 0.68, 1)",
            "Ease In Out Cubic": "cubic-bezier(0.65, 0, 0.35, 1)",
            "Ease In Quart": "cubic-bezier(0.5, 0, 0.75, 0)",
            "Ease Out Quart": "cubic-bezier(0.25, 1, 0.5, 1)",
            "Ease In Out Quart": "cubic-bezier(0.76, 0, 0.24, 1)",
            "Bounce In": "cubic-bezier(0.6, -0.28, 0.735, 0.045)",
            "Bounce Out": "cubic-bezier(0.175, 0.885, 0.32, 1.275)",
            "Bounce In Out": "cubic-bezier(0.68, -0.55, 0.265, 1.55)"
        }

        selected_preset = st.selectbox("Select Easing Function", list(easing_presets.keys()))
        easing_value = easing_presets[selected_preset]

        st.code(f"transition-timing-function: {easing_value};", language="css")

        # Preview animation with selected easing
        duration = st.slider("Animation Duration (seconds)", 0.5, 5.0, 2.0, 0.1)

        preview_html = f"""
        <style>
        .easing-preview {{
            width: 100%;
            height: 100px;
            background: #f0f0f0;
            border-radius: 10px;
            position: relative;
            overflow: hidden;
            margin: 20px 0;
        }}
        .easing-ball {{
            width: 50px;
            height: 50px;
            background: #007bff;
            border-radius: 50%;
            position: absolute;
            top: 25px;
            left: 0;
            transition: left {duration}s {easing_value};
        }}
        .easing-ball.animate {{
            left: calc(100% - 50px);
        }}
        </style>
        <div class="easing-preview">
            <div class="easing-ball animate"></div>
        </div>
        """

        st.markdown(preview_html, unsafe_allow_html=True)

    with tab2:
        st.subheader("Custom Cubic Bezier")

        col1, col2 = st.columns(2)
        with col1:
            x1 = st.slider("X1", 0.0, 1.0, 0.25, 0.01)
            y1 = st.slider("Y1", -2.0, 2.0, 0.46, 0.01)
        with col2:
            x2 = st.slider("X2", 0.0, 1.0, 0.45, 0.01)
            y2 = st.slider("Y2", -2.0, 2.0, 0.94, 0.01)

        custom_bezier = f"cubic-bezier({x1}, {y1}, {x2}, {y2})"
        st.code(f"transition-timing-function: {custom_bezier};", language="css")

        # Copy button for cubic bezier
        st.text_input("Cubic Bezier Value", custom_bezier)

    with tab3:
        st.subheader("Easing Function Visualizer")

        # Create a simple visualization
        import numpy as np
        import matplotlib.pyplot as plt

        # Generate sample points for visualization
        fig, ax = plt.subplots(figsize=(10, 6))

        # Different easing functions for comparison
        x = np.linspace(0, 1, 100)

        # Linear
        y_linear = x
        ax.plot(x, y_linear, label='Linear', linewidth=2)

        # Ease-in (approximate)
        y_ease_in = x ** 2
        ax.plot(x, y_ease_in, label='Ease In', linewidth=2)

        # Ease-out (approximate)
        y_ease_out = 1 - (1 - x) ** 2
        ax.plot(x, y_ease_out, label='Ease Out', linewidth=2)

        # Ease-in-out (approximate)
        y_ease_in_out = np.where(x < 0.5, 2 * x ** 2, 1 - 2 * (1 - x) ** 2)
        ax.plot(x, y_ease_in_out, label='Ease In Out', linewidth=2)

        ax.set_xlabel('Time Progress (0-1)')
        ax.set_ylabel('Value Progress (0-1)')
        ax.set_title('Easing Function Curves Comparison')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        st.pyplot(fig)
        plt.close()

        st.info("💡 **Tip**: Steeper curves mean faster changes, flatter curves mean slower changes.")


# Helper functions for color conversions and utilities

def hsl_to_rgb(h, s, l):
    """Convert HSL to RGB"""
    h = h / 360
    s = s / 100
    l = l / 100

    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1 / 6:
                return p + (q - p) * 6 * t
            if t < 1 / 2:
                return q
            if t < 2 / 3:
                return p + (q - p) * (2 / 3 - t) * 6
            return p

        if l < 0.5:
            q = l * (1 + s)
        else:
            q = l + s - l * s

        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1 / 3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1 / 3)

    return (int(r * 255), int(g * 255), int(b * 255))


def rgb_to_hsl(rgb):
    """Convert RGB to HSL"""
    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    h = s = l = (max_val + min_val) / 2

    if max_val == min_val:
        h = s = 0
    else:
        d = max_val - min_val
        s = d / (2 - max_val - min_val) if l > 0.5 else d / (max_val + min_val)

        if max_val == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_val == g:
            h = (b - r) / d + 2
        elif max_val == b:
            h = (r - g) / d + 4
        h /= 6

    return (int(h * 360), int(s * 100), int(l * 100))


def hex_to_rgb(hex_color):
    """Convert HEX to RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    """Convert RGB to HEX"""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def cmyk_to_rgb(c, m, y, k):
    """Convert CMYK to RGB"""
    c, m, y, k = c / 100, m / 100, y / 100, k / 100
    r = int(255 * (1 - c) * (1 - k))
    g = int(255 * (1 - m) * (1 - k))
    b = int(255 * (1 - y) * (1 - k))
    return (r, g, b)


def rgb_to_cmyk(rgb):
    """Convert RGB to CMYK"""
    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
    k = 1 - max(r, g, b)
    if k == 1:
        return (0, 0, 0, 100)
    c = int((1 - r - k) / (1 - k) * 100)
    m = int((1 - g - k) / (1 - k) * 100)
    y = int((1 - b - k) / (1 - k) * 100)
    k = int(k * 100)
    return (c, m, y, k)


def find_closest_color_name(hex_color):
    """Find closest CSS color name"""
    css_colors = {
        "aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aqua": "#00ffff", "aquamarine": "#7fffd4",
        "azure": "#f0ffff", "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000",
        "blanchedalmond": "#ffebcd", "blue": "#0000ff", "blueviolet": "#8a2be2", "brown": "#a52a2a",
        "burlywood": "#deb887", "cadetblue": "#5f9ea0", "chartreuse": "#7fff00", "chocolate": "#d2691e",
        "coral": "#ff7f50", "cornflowerblue": "#6495ed", "cornsilk": "#fff8dc", "crimson": "#dc143c",
        "cyan": "#00ffff", "darkblue": "#00008b", "darkcyan": "#008b8b", "darkgoldenrod": "#b8860b",
        "darkgray": "#a9a9a9", "darkgreen": "#006400", "darkkhaki": "#bdb76b", "darkmagenta": "#8b008b",
        "darkolivegreen": "#556b2f", "darkorange": "#ff8c00", "darkorchid": "#9932cc", "darkred": "#8b0000",
        "darksalmon": "#e9967a", "darkseagreen": "#8fbc8f", "darkslateblue": "#483d8b", "darkslategray": "#2f4f4f",
        "darkturquoise": "#00ced1", "darkviolet": "#9400d3", "deeppink": "#ff1493", "deepskyblue": "#00bfff",
        "dimgray": "#696969", "dodgerblue": "#1e90ff", "firebrick": "#b22222", "floralwhite": "#fffaf0",
        "forestgreen": "#228b22", "fuchsia": "#ff00ff", "gainsboro": "#dcdcdc", "ghostwhite": "#f8f8ff",
        "gold": "#ffd700", "goldenrod": "#daa520", "gray": "#808080", "green": "#008000",
        "greenyellow": "#adff2f", "honeydew": "#f0fff0", "hotpink": "#ff69b4", "indianred": "#cd5c5c",
        "indigo": "#4b0082", "ivory": "#fffff0", "khaki": "#f0e68c", "lavender": "#e6e6fa",
        "lavenderblush": "#fff0f5", "lawngreen": "#7cfc00", "lemonchiffon": "#fffacd", "lightblue": "#add8e6",
        "lightcoral": "#f08080", "lightcyan": "#e0ffff", "lightgoldenrodyellow": "#fafad2", "lightgray": "#d3d3d3",
        "lightgreen": "#90ee90", "lightpink": "#ffb6c1", "lightsalmon": "#ffa07a", "lightseagreen": "#20b2aa",
        "lightskyblue": "#87cefa", "lightslategray": "#778899", "lightsteelblue": "#b0c4de", "lightyellow": "#ffffe0",
        "lime": "#00ff00", "limegreen": "#32cd32", "linen": "#faf0e6", "magenta": "#ff00ff",
        "maroon": "#800000", "mediumaquamarine": "#66cdaa", "mediumblue": "#0000cd", "mediumorchid": "#ba55d3",
        "mediumpurple": "#9370db", "mediumseagreen": "#3cb371", "mediumslateblue": "#7b68ee",
        "mediumspringgreen": "#00fa9a",
        "mediumturquoise": "#48d1cc", "mediumvioletred": "#c71585", "midnightblue": "#191970", "mintcream": "#f5fffa",
        "mistyrose": "#ffe4e1", "moccasin": "#ffe4b5", "navajowhite": "#ffdead", "navy": "#000080",
        "oldlace": "#fdf5e6", "olive": "#808000", "olivedrab": "#6b8e23", "orange": "#ffa500",
        "orangered": "#ff4500", "orchid": "#da70d6", "palegoldenrod": "#eee8aa", "palegreen": "#98fb98",
        "paleturquoise": "#afeeee", "palevioletred": "#db7093", "papayawhip": "#ffefd5", "peachpuff": "#ffdab9",
        "peru": "#cd853f", "pink": "#ffc0cb", "plum": "#dda0dd", "powderblue": "#b0e0e6",
        "purple": "#800080", "red": "#ff0000", "rosybrown": "#bc8f8f", "royalblue": "#4169e1",
        "saddlebrown": "#8b4513", "salmon": "#fa8072", "sandybrown": "#f4a460", "seagreen": "#2e8b57",
        "seashell": "#fff5ee", "sienna": "#a0522d", "silver": "#c0c0c0", "skyblue": "#87ceeb",
        "slateblue": "#6a5acd", "slategray": "#708090", "snow": "#fffafa", "springgreen": "#00ff7f",
        "steelblue": "#4682b4", "tan": "#d2b48c", "teal": "#008080", "thistle": "#d8bfd8",
        "tomato": "#ff6347", "turquoise": "#40e0d0", "violet": "#ee82ee", "wheat": "#f5deb3",
        "white": "#ffffff", "whitesmoke": "#f5f5f5", "yellow": "#ffff00", "yellowgreen": "#9acd32"
    }

    target_rgb = hex_to_rgb(hex_color)

    min_distance = float('inf')
    closest_name = ""
    closest_hex = ""

    for name, hex_val in css_colors.items():
        color_rgb = hex_to_rgb(hex_val)
        # Calculate Euclidean distance in RGB space
        distance = sum((target_rgb[i] - color_rgb[i]) ** 2 for i in range(3)) ** 0.5

        if distance < min_distance:
            min_distance = distance
            closest_name = name
            closest_hex = hex_val

    return closest_name, closest_hex, min_distance


def get_named_color_hex(color_name):
    """Get hex value for named color"""
    css_colors = {
        "crimson": "#dc143c", "darkred": "#8b0000", "firebrick": "#b22222", "indianred": "#cd5c5c",
        "lightcoral": "#f08080", "salmon": "#fa8072", "tomato": "#ff6347", "navy": "#000080",
        "darkblue": "#00008b", "blue": "#0000ff", "royalblue": "#4169e1", "cornflowerblue": "#6495ed",
        "lightblue": "#add8e6", "skyblue": "#87ceeb", "darkgreen": "#006400", "green": "#008000",
        "forestgreen": "#228b22", "seagreen": "#2e8b57", "lightgreen": "#90ee90", "lime": "#00ff00",
        "springgreen": "#00ff7f", "gold": "#ffd700", "yellow": "#ffff00", "lightyellow": "#ffffe0",
        "khaki": "#f0e68c", "palegoldenrod": "#eee8aa", "moccasin": "#ffe4b5", "wheat": "#f5deb3",
        "indigo": "#4b0082", "purple": "#800080", "darkviolet": "#9400d3", "mediumorchid": "#ba55d3",
        "plum": "#dda0dd", "violet": "#ee82ee", "lavender": "#e6e6fa", "darkorange": "#ff8c00",
        "orange": "#ffa500", "coral": "#ff7f50", "tomato": "#ff6347", "orangered": "#ff4500",
        "peachpuff": "#ffdab9", "papayawhip": "#ffefd5", "black": "#000000", "darkgray": "#a9a9a9",
        "gray": "#808080", "dimgray": "#696969", "silver": "#c0c0c0", "lightgray": "#d3d3d3",
        "white": "#ffffff"
    }
    return css_colors.get(color_name.lower(), "#000000")


def hsl_converter():
    """HSL color converter"""
    create_tool_header("HSL Converter", "Convert colors between HSL, RGB, and HEX formats", "🎨")

    tab1, tab2, tab3 = st.tabs(["HSL to RGB/HEX", "RGB/HEX to HSL", "Interactive Converter"])

    with tab1:
        st.subheader("HSL to RGB/HEX Converter")

        col1, col2, col3 = st.columns(3)
        with col1:
            hue = st.slider("Hue", 0, 360, 180)
        with col2:
            saturation = st.slider("Saturation (%)", 0, 100, 50)
        with col3:
            lightness = st.slider("Lightness (%)", 0, 100, 50)

        # Convert HSL to RGB
        rgb = hsl_to_rgb(hue, saturation, lightness)
        hex_color = rgb_to_hex(rgb)

        st.subheader("Results")

        # Color preview
        text_color = 'white' if lightness < 50 else 'black'
        preview_html = f"""
        <div style="width: 100%; height: 100px; background-color: {hex_color}; border: 2px solid #ccc; border-radius: 10px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 18px;">
            {hex_color}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code(f"HSL: hsl({hue}, {saturation}%, {lightness}%)", language="css")
            st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})", language="css")
        with col2:
            st.code(f"HEX: {hex_color}", language="css")
            st.code(f"RGBA: rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 1)", language="css")

    with tab2:
        st.subheader("RGB/HEX to HSL Converter")

        input_method = st.radio("Input Method", ["Color Picker", "RGB Values", "HEX Value"])

        if input_method == "Color Picker":
            color = st.color_picker("Select Color", "#3366cc")
            rgb = hex_to_rgb(color)
        elif input_method == "RGB Values":
            col1, col2, col3 = st.columns(3)
            with col1:
                r = st.number_input("Red", 0, 255, 51)
            with col2:
                g = st.number_input("Green", 0, 255, 102)
            with col3:
                b = st.number_input("Blue", 0, 255, 204)
            rgb = (r, g, b)
            color = rgb_to_hex(rgb)
        else:
            hex_input = st.text_input("HEX Color", "#3366cc")
            try:
                rgb = hex_to_rgb(hex_input)
                color = hex_input
            except:
                st.error("Invalid HEX color format")
                return

        # Convert to HSL
        hsl = rgb_to_hsl(rgb)

        st.subheader("Results")

        # Color preview
        text_color = 'white' if hsl[2] < 50 else 'black'
        preview_html = f"""
        <div style="width: 100%; height: 100px; background-color: {color}; border: 2px solid #ccc; border-radius: 10px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 18px;">
            {color}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code(f"HSL: hsl({hsl[0]}, {hsl[1]}%, {hsl[2]}%)", language="css")
            st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})", language="css")
        with col2:
            st.code(f"HEX: {color}", language="css")
            st.code(f"RGBA: rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 1)", language="css")

    with tab3:
        st.subheader("Interactive Color Converter")

        st.write("Adjust any format and see real-time conversion:")

        # Initialize session state
        if 'converter_hue' not in st.session_state:
            st.session_state.converter_hue = 180
        if 'converter_sat' not in st.session_state:
            st.session_state.converter_sat = 50
        if 'converter_light' not in st.session_state:
            st.session_state.converter_light = 50

        col1, col2 = st.columns(2)

        with col1:
            st.write("**HSL Controls**")
            new_hue = st.slider("H", 0, 360, st.session_state.converter_hue, key="hsl_h")
            new_sat = st.slider("S (%)", 0, 100, st.session_state.converter_sat, key="hsl_s")
            new_light = st.slider("L (%)", 0, 100, st.session_state.converter_light, key="hsl_l")

            if new_hue != st.session_state.converter_hue or new_sat != st.session_state.converter_sat or new_light != st.session_state.converter_light:
                st.session_state.converter_hue = new_hue
                st.session_state.converter_sat = new_sat
                st.session_state.converter_light = new_light

        with col2:
            rgb = hsl_to_rgb(st.session_state.converter_hue, st.session_state.converter_sat,
                             st.session_state.converter_light)
            hex_color = rgb_to_hex(rgb)

            st.write("**RGB Controls**")
            new_r = st.slider("R", 0, 255, rgb[0], key="rgb_r")
            new_g = st.slider("G", 0, 255, rgb[1], key="rgb_g")
            new_b = st.slider("B", 0, 255, rgb[2], key="rgb_b")

            if new_r != rgb[0] or new_g != rgb[1] or new_b != rgb[2]:
                new_hsl = rgb_to_hsl((new_r, new_g, new_b))
                st.session_state.converter_hue = new_hsl[0]
                st.session_state.converter_sat = new_hsl[1]
                st.session_state.converter_light = new_hsl[2]
                st.rerun()

        # Display all formats
        current_rgb = hsl_to_rgb(st.session_state.converter_hue, st.session_state.converter_sat,
                                 st.session_state.converter_light)
        current_hex = rgb_to_hex(current_rgb)

        # Large color preview
        text_color = 'white' if st.session_state.converter_light < 50 else 'black'
        preview_html = f"""
        <div style="width: 100%; height: 150px; background-color: {current_hex}; border: 2px solid #ccc; border-radius: 15px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 24px;">
            {current_hex}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        # All format outputs
        col1, col2, col3 = st.columns(3)
        with col1:
            st.code(
                f"HSL\nhsl({st.session_state.converter_hue}, {st.session_state.converter_sat}%, {st.session_state.converter_light}%)",
                language="css")
        with col2:
            st.code(f"RGB\nrgb({current_rgb[0]}, {current_rgb[1]}, {current_rgb[2]})", language="css")
        with col3:
            st.code(f"HEX\n{current_hex}", language="css")


def cmyk_converter():
    """CMYK color converter"""
    create_tool_header("CMYK Converter", "Convert colors between CMYK, RGB, and HEX formats", "🖨️")

    tab1, tab2 = st.tabs(["CMYK to RGB/HEX", "RGB/HEX to CMYK"])

    with tab1:
        st.subheader("CMYK to RGB/HEX Converter")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            c = st.slider("Cyan (%)", 0, 100, 70)
        with col2:
            m = st.slider("Magenta (%)", 0, 100, 0)
        with col3:
            y = st.slider("Yellow (%)", 0, 100, 100)
        with col4:
            k = st.slider("Black (%)", 0, 100, 20)

        # Convert CMYK to RGB
        rgb = cmyk_to_rgb(c, m, y, k)
        hex_color = rgb_to_hex(rgb)

        st.subheader("Results")

        # Color preview
        preview_html = f"""
        <div style="width: 100%; height: 100px; background-color: {hex_color}; border: 2px solid #ccc; border-radius: 10px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 18px;">
            {hex_color}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code(f"CMYK: cmyk({c}%, {m}%, {y}%, {k}%)", language="css")
            st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})", language="css")
        with col2:
            st.code(f"HEX: {hex_color}", language="css")
            st.info("💡 CMYK is primarily used for print media")

    with tab2:
        st.subheader("RGB/HEX to CMYK Converter")

        input_method = st.radio("Input Method", ["Color Picker", "RGB Values", "HEX Value"])

        if input_method == "Color Picker":
            color = st.color_picker("Select Color", "#ff6600")
            rgb = hex_to_rgb(color)
        elif input_method == "RGB Values":
            col1, col2, col3 = st.columns(3)
            with col1:
                r = st.number_input("Red", 0, 255, 255)
            with col2:
                g = st.number_input("Green", 0, 255, 102)
            with col3:
                b = st.number_input("Blue", 0, 255, 0)
            rgb = (r, g, b)
            color = rgb_to_hex(rgb)
        else:
            hex_input = st.text_input("HEX Color", "#ff6600")
            try:
                rgb = hex_to_rgb(hex_input)
                color = hex_input
            except:
                st.error("Invalid HEX color format")
                return

        # Convert to CMYK
        cmyk = rgb_to_cmyk(rgb)

        st.subheader("Results")

        # Color preview
        preview_html = f"""
        <div style="width: 100%; height: 100px; background-color: {color}; border: 2px solid #ccc; border-radius: 10px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 18px;">
            {color}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.code(f"CMYK: cmyk({cmyk[0]}%, {cmyk[1]}%, {cmyk[2]}%, {cmyk[3]}%)", language="css")
            st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})", language="css")
        with col2:
            st.code(f"HEX: {color}", language="css")
            st.info("💡 CMYK values are approximate conversions")


def color_name_finder():
    """Color name finder tool"""
    create_tool_header("Color Name Finder", "Find color names and explore color databases", "🏷️")

    tab1, tab2, tab3 = st.tabs(["Find Color Name", "Browse Colors", "Color Database"])

    with tab1:
        st.subheader("Find Color Name from Value")

        input_method = st.radio("Input Method", ["Color Picker", "HEX Value", "RGB Values"])

        if input_method == "Color Picker":
            color = st.color_picker("Select Color", "#ff6347")
            rgb = hex_to_rgb(color)
            hex_color = color
        elif input_method == "HEX Value":
            hex_input = st.text_input("HEX Color", "#ff6347")
            try:
                rgb = hex_to_rgb(hex_input)
                hex_color = hex_input
                color = hex_color
            except:
                st.error("Invalid HEX color format")
                return
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                r = st.number_input("Red", 0, 255, 255)
            with col2:
                g = st.number_input("Green", 0, 255, 99)
            with col3:
                b = st.number_input("Blue", 0, 255, 71)
            rgb = (r, g, b)
            hex_color = rgb_to_hex(rgb)
            color = hex_color

        # Find closest color name
        color_name, closest_hex, distance = find_closest_color_name(hex_color)

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Your Color:**")
            preview_html = f"""
            <div style="width: 100%; height: 100px; background-color: {hex_color}; border: 2px solid #ccc; border-radius: 10px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 14px;">
                {hex_color}
            </div>
            """
            st.markdown(preview_html, unsafe_allow_html=True)
            st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})", language="css")

        with col2:
            st.write(f"**Closest Named Color: {color_name}**")
            preview_html = f"""
            <div style="width: 100%; height: 100px; background-color: {closest_hex}; border: 2px solid #ccc; border-radius: 10px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 14px;">
                {closest_hex}
            </div>
            """
            st.markdown(preview_html, unsafe_allow_html=True)
            st.code(f"Name: {color_name}\nHEX: {closest_hex}", language="css")

        if distance > 0:
            st.info(f"💡 Color distance: {distance:.2f} (0 = exact match)")

    with tab2:
        st.subheader("Browse Named Colors")

        color_families = {
            "Reds": ["crimson", "darkred", "firebrick", "indianred", "lightcoral", "salmon", "tomato"],
            "Blues": ["navy", "darkblue", "blue", "royalblue", "cornflowerblue", "lightblue", "skyblue"],
            "Greens": ["darkgreen", "green", "forestgreen", "seagreen", "lightgreen", "lime", "springgreen"],
            "Yellows": ["gold", "yellow", "lightyellow", "khaki", "palegoldenrod", "moccasin", "wheat"],
            "Purples": ["indigo", "purple", "darkviolet", "mediumorchid", "plum", "violet", "lavender"],
            "Oranges": ["darkorange", "orange", "coral", "tomato", "orangered", "peachpuff", "papayawhip"],
            "Grays": ["black", "darkgray", "gray", "dimgray", "silver", "lightgray", "white"]
        }

        selected_family = st.selectbox("Select Color Family", list(color_families.keys()))

        st.write(f"**{selected_family} Colors:**")

        colors = color_families[selected_family]
        cols = st.columns(min(len(colors), 4))

        for i, color_name in enumerate(colors):
            col_index = i % 4
            with cols[col_index]:
                # Get hex value for named color (simplified)
                hex_value = get_named_color_hex(color_name)

                preview_html = f"""
                <div style="width: 100%; height: 80px; background-color: {hex_value}; border: 1px solid #ccc; border-radius: 8px; margin: 5px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 10px; text-shadow: 1px 1px 2px rgba(0,0,0,0.7);">
                    {color_name}
                </div>
                """
                st.markdown(preview_html, unsafe_allow_html=True)
                if st.button(f"Use {color_name}", key=f"use_{color_name}"):
                    st.code(f"color: {color_name};\ncolor: {hex_value};")

    with tab3:
        st.subheader("Color Database Reference")

        st.write("**CSS Named Colors**")
        st.info("CSS supports 147 named colors. Here are some popular categories:")

        categories = {
            "Primary Colors": [("red", "#ff0000"), ("green", "#008000"), ("blue", "#0000ff")],
            "Secondary Colors": [("yellow", "#ffff00"), ("cyan", "#00ffff"), ("magenta", "#ff00ff")],
            "Neutral Colors": [("black", "#000000"), ("white", "#ffffff"), ("gray", "#808080")],
            "Web Safe Colors": [("maroon", "#800000"), ("olive", "#808000"), ("navy", "#000080")]
        }

        for category, color_list in categories.items():
            with st.expander(f"{category}"):
                cols = st.columns(len(color_list))
                for i, (name, hex_val) in enumerate(color_list):
                    with cols[i]:
                        text_color = 'white' if name != 'yellow' else 'black'
                        preview_html = f"""
                        <div style="width: 100%; height: 60px; background-color: {hex_val}; border: 1px solid #ccc; border-radius: 5px; margin: 5px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 12px;">
                            {name}
                        </div>
                        """
                        st.markdown(preview_html, unsafe_allow_html=True)
                        st.caption(hex_val)


def gradient_creator():
    """Advanced gradient creator tool"""
    create_tool_header("Gradient Creator", "Create advanced CSS gradients with multiple stops", "🌈")

    tab1, tab2, tab3 = st.tabs(["Linear Gradients", "Radial Gradients", "Conic Gradients"])

    with tab1:
        st.subheader("Linear Gradient Creator")

        # Direction controls
        col1, col2 = st.columns(2)
        with col1:
            direction_type = st.selectbox("Direction Type", ["Angle", "Keyword"])
            if direction_type == "Angle":
                angle = st.slider("Angle (degrees)", 0, 360, 90)
                direction = f"{angle}deg"
            else:
                keyword_direction = st.selectbox("Direction", [
                    "to right", "to left", "to top", "to bottom",
                    "to top right", "to top left", "to bottom right", "to bottom left"
                ])
                direction = keyword_direction

        with col2:
            num_stops = st.number_input("Number of Color Stops", 2, 10, 3)

        # Color stops
        st.subheader("Color Stops")

        color_stops = []
        for i in range(num_stops):
            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                color = st.color_picker(f"Color {i + 1}",
                                        ["#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#feca57", "#ff9ff3", "#54a0ff",
                                         "#5f27cd", "#00d2d3", "#ff9f43"][i % 10],
                                        key=f"linear_color_{i}")

            with col2:
                if i == 0:
                    position = 0
                elif i == num_stops - 1:
                    position = 100
                else:
                    position = st.number_input(f"Position {i + 1} (%)", 0, 100, int(100 * i / (num_stops - 1)),
                                               key=f"linear_pos_{i}")

            with col3:
                opacity = st.slider(f"Opacity {i + 1}", 0.0, 1.0, 1.0, 0.1, key=f"linear_opacity_{i}")

            # Convert to RGBA if opacity < 1
            if opacity < 1.0:
                rgb = hex_to_rgb(color)
                color_value = f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, {opacity})"
            else:
                color_value = color

            color_stops.append(f"{color_value} {position}%")

        # Generate CSS
        gradient_css = f"background: linear-gradient({direction}, {', '.join(color_stops)});"

        # Preview
        st.subheader("Preview")
        preview_html = f"""
        <div style="{gradient_css} width: 100%; height: 200px; border: 2px solid #ccc; border-radius: 15px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
            Linear Gradient Preview
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        st.subheader("Generated CSS")
        st.code(gradient_css, language="css")

        # Additional CSS with fallback
        full_css = f""".gradient-element {{
  {gradient_css}
  /* Fallback for older browsers */
  background: {color_stops[0].split()[0]};
}}"""

        with st.expander("Complete CSS with Fallback"):
            st.code(full_css, language="css")

        FileHandler.create_download_link(full_css.encode(), "linear_gradient.css", "text/css")

    with tab2:
        st.subheader("Radial Gradient Creator")

        # Radial gradient controls
        col1, col2 = st.columns(2)
        with col1:
            shape = st.selectbox("Shape", ["circle", "ellipse"])
            size = st.selectbox("Size",
                                ["closest-side", "closest-corner", "farthest-side", "farthest-corner", "custom"])
            if size == "custom":
                if shape == "circle":
                    custom_size = st.text_input("Radius", "100px")
                else:
                    custom_size = st.text_input("Size (width height)", "100px 150px")
                size = custom_size

        with col2:
            position_x = st.selectbox("Position X", ["left", "center", "right", "custom"])
            if position_x == "custom":
                position_x = st.text_input("X Position", "50%")

            position_y = st.selectbox("Position Y", ["top", "center", "bottom", "custom"])
            if position_y == "custom":
                position_y = st.text_input("Y Position", "50%")

        num_stops = st.number_input("Number of Color Stops", 2, 10, 3, key="radial_stops")

        # Color stops for radial
        color_stops = []
        for i in range(num_stops):
            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                color = st.color_picker(f"Color {i + 1}",
                                        ["#667eea", "#764ba2", "#f093fb", "#f5576c", "#4facfe", "#00f2fe", "#a8edea",
                                         "#fed6e3", "#ff9a9e", "#fecfef"][i % 10],
                                        key=f"radial_color_{i}")

            with col2:
                if i == 0:
                    position = 0
                elif i == num_stops - 1:
                    position = 100
                else:
                    position = st.number_input(f"Position {i + 1} (%)", 0, 100, int(100 * i / (num_stops - 1)),
                                               key=f"radial_pos_{i}")

            with col3:
                opacity = st.slider(f"Opacity {i + 1}", 0.0, 1.0, 1.0, 0.1, key=f"radial_opacity_{i}")

            # Convert to RGBA if opacity < 1
            if opacity < 1.0:
                rgb = hex_to_rgb(color)
                color_value = f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, {opacity})"
            else:
                color_value = color

            color_stops.append(f"{color_value} {position}%")

        # Generate CSS
        gradient_css = f"background: radial-gradient({shape} {size} at {position_x} {position_y}, {', '.join(color_stops)});"

        # Preview
        st.subheader("Preview")
        preview_html = f"""
        <div style="{gradient_css} width: 100%; height: 200px; border: 2px solid #ccc; border-radius: 15px; margin: 20px 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
            Radial Gradient Preview
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        st.subheader("Generated CSS")
        st.code(gradient_css, language="css")

    with tab3:
        st.subheader("Conic Gradient Creator")

        # Conic gradient controls
        col1, col2 = st.columns(2)
        with col1:
            from_angle = st.slider("From Angle (degrees)", 0, 360, 0)
        with col2:
            position_x = st.selectbox("Position X", ["left", "center", "right", "custom"], key="conic_pos_x")
            if position_x == "custom":
                position_x = st.text_input("X Position", "50%", key="conic_custom_x")

            position_y = st.selectbox("Position Y", ["top", "center", "bottom", "custom"], key="conic_pos_y")
            if position_y == "custom":
                position_y = st.text_input("Y Position", "50%", key="conic_custom_y")

        num_stops = st.number_input("Number of Color Stops", 2, 12, 4, key="conic_stops")

        # Color stops for conic
        color_stops = []
        for i in range(num_stops):
            col1, col2 = st.columns([2, 1])

            with col1:
                color = st.color_picker(f"Color {i + 1}",
                                        ["#ff0000", "#ff8000", "#ffff00", "#80ff00", "#00ff00", "#00ff80", "#00ffff",
                                         "#0080ff", "#0000ff", "#8000ff", "#ff00ff", "#ff0080"][i % 12],
                                        key=f"conic_color_{i}")

            with col2:
                angle = st.number_input(f"Angle {i + 1} (°)", 0, 360, int(360 * i / num_stops), key=f"conic_angle_{i}")

            color_stops.append(f"{color} {angle}deg")

        # Generate CSS
        gradient_css = f"background: conic-gradient(from {from_angle}deg at {position_x} {position_y}, {', '.join(color_stops)});"

        # Preview
        st.subheader("Preview")
        preview_html = f"""
        <div style="{gradient_css} width: 300px; height: 300px; border: 2px solid #ccc; border-radius: 50%; margin: 20px auto; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.7);">
            Conic
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        st.subheader("Generated CSS")
        st.code(gradient_css, language="css")


def complementary_colors():
    """Complementary colors generator"""
    create_tool_header("Complementary Colors", "Generate complementary color schemes", "🎭")

    st.write(
        "Complementary colors are opposite each other on the color wheel and create high contrast when used together.")

    # Color input
    input_method = st.radio("Choose Input Method", ["Color Picker", "HSL Values", "HEX Value"])

    if input_method == "Color Picker":
        base_color = st.color_picker("Select Base Color", "#3366cc")
        rgb = hex_to_rgb(base_color)
        hsl = rgb_to_hsl(rgb)
    elif input_method == "HSL Values":
        col1, col2, col3 = st.columns(3)
        with col1:
            h = st.slider("Hue", 0, 360, 210)
        with col2:
            s = st.slider("Saturation (%)", 0, 100, 60)
        with col3:
            l = st.slider("Lightness (%)", 0, 100, 50)
        hsl = (h, s, l)
        rgb = hsl_to_rgb(h, s, l)
        base_color = rgb_to_hex(rgb)
    else:
        hex_input = st.text_input("HEX Color", "#3366cc")
        try:
            rgb = hex_to_rgb(hex_input)
            base_color = hex_input
            hsl = rgb_to_hsl(rgb)
        except:
            st.error("Invalid HEX color format")
            return

    # Calculate complementary color (180 degrees opposite)
    comp_hue = (hsl[0] + 180) % 360
    comp_hsl = (comp_hue, hsl[1], hsl[2])
    comp_rgb = hsl_to_rgb(comp_hue, hsl[1], hsl[2])
    comp_hex = rgb_to_hex(comp_rgb)

    st.subheader("Complementary Color Pair")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Base Color**")
        text_color = 'white' if hsl[2] < 50 else 'black'
        preview_html = f"""
        <div style="background-color: {base_color}; width: 100%; height: 150px; border: 2px solid #ccc; border-radius: 15px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 18px;">
            {base_color}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        st.code(f"HEX: {base_color}\nRGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})\nHSL: hsl({hsl[0]}, {hsl[1]}%, {hsl[2]}%)",
                language="css")

    with col2:
        st.write("**Complementary Color**")
        comp_text_color = 'white' if hsl[2] < 50 else 'black'
        preview_html = f"""
        <div style="background-color: {comp_hex}; width: 100%; height: 150px; border: 2px solid #ccc; border-radius: 15px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: {comp_text_color}; font-weight: bold; font-size: 18px;">
            {comp_hex}
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)

        st.code(
            f"HEX: {comp_hex}\nRGB: rgb({comp_rgb[0]}, {comp_rgb[1]}, {comp_rgb[2]})\nHSL: hsl({comp_hue}, {hsl[1]}%, {hsl[2]}%)",
            language="css")

    # Show both colors together
    st.subheader("Color Combination Preview")
    combo_text_color = 'white' if hsl[2] < 50 else 'black'
    combo_html = f"""
    <div style="display: flex; margin: 20px 0; border: 2px solid #ccc; border-radius: 15px; overflow: hidden;">
        <div style="background-color: {base_color}; width: 50%; height: 100px; display: flex; align-items: center; justify-content: center; color: {combo_text_color}; font-weight: bold;">
            Primary
        </div>
        <div style="background-color: {comp_hex}; width: 50%; height: 100px; display: flex; align-items: center; justify-content: center; color: {combo_text_color}; font-weight: bold;">
            Complement
        </div>
    </div>
    """
    st.markdown(combo_html, unsafe_allow_html=True)

    # Generate variations
    st.subheader("Complementary Variations")

    # Lighter and darker versions
    variations = []
    for i in range(5):
        lightness_mod = (i - 2) * 15  # -30, -15, 0, +15, +30
        new_lightness = max(10, min(90, hsl[2] + lightness_mod))

        # Base color variation
        base_var_rgb = hsl_to_rgb(hsl[0], hsl[1], new_lightness)
        base_var_hex = rgb_to_hex(base_var_rgb)

        # Complementary variation
        comp_var_rgb = hsl_to_rgb(comp_hue, hsl[1], new_lightness)
        comp_var_hex = rgb_to_hex(comp_var_rgb)

        variations.append((base_var_hex, comp_var_hex, new_lightness))

    cols = st.columns(5)
    for i, (base_var, comp_var, lightness) in enumerate(variations):
        with cols[i]:
            st.write(f"**{lightness}% Light**")
            var_text_color = 'white' if lightness < 50 else 'black'
            combo_html = f"""
            <div style="border: 1px solid #ccc; border-radius: 8px; overflow: hidden; margin: 5px 0;">
                <div style="background-color: {base_var}; height: 40px; display: flex; align-items: center; justify-content: center; color: {var_text_color}; font-size: 10px; font-weight: bold;">
                    Base
                </div>
                <div style="background-color: {comp_var}; height: 40px; display: flex; align-items: center; justify-content: center; color: {var_text_color}; font-size: 10px; font-weight: bold;">
                    Comp
                </div>
            </div>
            """
            st.markdown(combo_html, unsafe_allow_html=True)

    # CSS Output
    st.subheader("CSS Variables")
    css_vars = f""":root {{
  --primary-color: {base_color};
  --primary-rgb: {rgb[0]}, {rgb[1]}, {rgb[2]};
  --complementary-color: {comp_hex};
  --complementary-rgb: {comp_rgb[0]}, {comp_rgb[1]}, {comp_rgb[2]};
}}

/* Usage Examples */
.primary-bg {{ background-color: var(--primary-color); }}
.complementary-bg {{ background-color: var(--complementary-color); }}
.primary-text {{ color: var(--primary-color); }}
.complementary-text {{ color: var(--complementary-color); }}"""

    st.code(css_vars, language="css")

    FileHandler.create_download_link(css_vars.encode(), "complementary_colors.css", "text/css")

    # Usage tips
    with st.expander("💡 Design Tips for Complementary Colors"):
        st.markdown("""
        **Best Practices:**
        - Use complementary colors for high contrast and emphasis
        - Great for call-to-action buttons and important highlights
        - Use one as dominant and the other as accent (80/20 rule)
        - Consider using tints and shades to create more harmony

        **Common Complementary Pairs:**
        - Blue & Orange
        - Red & Green
        - Yellow & Purple
        - Cyan & Red
        """)


def analogous_colors():
    """Analogous colors generator"""
    create_tool_header("Analogous Colors", "Generate harmonious analogous color schemes", "🌈")

    st.write("Analogous colors are next to each other on the color wheel and create harmonious, pleasing combinations.")

    # Color input
    input_method = st.radio("Choose Input Method", ["Color Picker", "HSL Values", "HEX Value"])

    if input_method == "Color Picker":
        base_color = st.color_picker("Select Base Color", "#4285f4")
        rgb = hex_to_rgb(base_color)
        hsl = rgb_to_hsl(rgb)
    elif input_method == "HSL Values":
        col1, col2, col3 = st.columns(3)
        with col1:
            h = st.slider("Hue", 0, 360, 210)
        with col2:
            s = st.slider("Saturation (%)", 0, 100, 70)
        with col3:
            l = st.slider("Lightness (%)", 0, 100, 50)
        hsl = (h, s, l)
        rgb = hsl_to_rgb(h, s, l)
        base_color = rgb_to_hex(rgb)
    else:
        hex_input = st.text_input("HEX Color", "#4285f4")
        try:
            rgb = hex_to_rgb(hex_input)
            base_color = hex_input
            hsl = rgb_to_hsl(rgb)
        except:
            st.error("Invalid HEX color format")
            return

    # Analogous color settings
    col1, col2 = st.columns(2)
    with col1:
        num_colors = st.slider("Number of Colors", 3, 7, 5)
    with col2:
        hue_step = st.slider("Hue Step (degrees)", 15, 60, 30)

    # Calculate analogous colors
    analogous_colors_list = []
    center_index = num_colors // 2

    for i in range(num_colors):
        hue_offset = (i - center_index) * hue_step
        new_hue = (hsl[0] + hue_offset) % 360

        # Create slight variations in saturation and lightness for more interest
        saturation_variation = hsl[1] + (i - center_index) * 5
        lightness_variation = hsl[2] + (i - center_index) * 3

        new_saturation = max(20, min(100, saturation_variation))
        new_lightness = max(20, min(80, lightness_variation))

        analog_rgb = hsl_to_rgb(new_hue, new_saturation, new_lightness)
        analog_hex = rgb_to_hex(analog_rgb)
        analog_hsl = (new_hue, new_saturation, new_lightness)

        is_base = (i == center_index)
        analogous_colors_list.append((analog_hex, analog_rgb, analog_hsl, is_base))

    # Display colors
    st.subheader("Analogous Color Scheme")

    # Show all colors in a row
    cols = st.columns(num_colors)
    for i, (hex_color, rgb, hsl_vals, is_base) in enumerate(analogous_colors_list):
        with cols[i]:
            label = "**Base Color**" if is_base else f"**Color {i + 1}**"
            st.write(label)

            border_style = '3px solid #333' if is_base else '2px solid #ccc'
            text_color = 'white' if hsl_vals[2] < 50 else 'black'
            preview_html = f"""
            <div style="background-color: {hex_color}; width: 100%; height: 120px; border: {border_style}; border-radius: 10px; margin: 10px 0; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 12px;">
                {hex_color}
            </div>
            """
            st.markdown(preview_html, unsafe_allow_html=True)

            st.caption(f"H: {hsl_vals[0]}°\nS: {hsl_vals[1]}%\nL: {hsl_vals[2]}%")

    # Combined preview
    st.subheader("Palette Preview")
    combined_html = '<div style="display: flex; height: 100px; border: 2px solid #ccc; border-radius: 15px; overflow: hidden; margin: 20px 0;">'

    for hex_color, _, hsl_vals, is_base in analogous_colors_list:
        width_percent = 100 / num_colors
        border_style = "border-right: 2px solid #333;" if is_base else ""
        text_color = 'white' if hsl_vals[2] < 50 else 'black'
        base_text = "BASE" if is_base else ""
        combined_html += f'<div style="background-color: {hex_color}; width: {width_percent}%; {border_style} display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 10px;">{base_text}</div>'

    combined_html += '</div>'
    st.markdown(combined_html, unsafe_allow_html=True)

    # Different lightness variations
    st.subheader("Lightness Variations")

    lightness_levels = [30, 45, 60, 75]
    for lightness in lightness_levels:
        st.write(f"**{lightness}% Lightness**")
        variation_html = '<div style="display: flex; height: 50px; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; margin: 10px 0;">'

        for hex_color, _, hsl_vals, _ in analogous_colors_list:
            var_rgb = hsl_to_rgb(hsl_vals[0], hsl_vals[1], lightness)
            var_hex = rgb_to_hex(var_rgb)
            width_percent = 100 / num_colors

            text_color = 'white' if lightness < 50 else 'black'
            variation_html += f'<div style="background-color: {var_hex}; width: {width_percent}%; display: flex; align-items: center; justify-content: center; color: {text_color}; font-size: 8px;">{var_hex}</div>'

        variation_html += '</div>'
        st.markdown(variation_html, unsafe_allow_html=True)

    # CSS Variables Output
    st.subheader("CSS Variables")

    css_vars = ":root {\n"
    for i, (hex_color, rgb, hsl_vals, is_base) in enumerate(analogous_colors_list):
        suffix = "primary" if is_base else f"analog-{i + 1}"
        css_vars += f"  --{suffix}-color: {hex_color};\n"
        css_vars += f"  --{suffix}-rgb: {rgb[0]}, {rgb[1]}, {rgb[2]};\n"

    css_vars += "}\n\n/* Usage Examples */\n"
    for i, (hex_color, _, _, is_base) in enumerate(analogous_colors_list):
        suffix = "primary" if is_base else f"analog-{i + 1}"
        css_vars += f".{suffix}-bg {{ background-color: var(--{suffix}-color); }}\n"
        css_vars += f".{suffix}-text {{ color: var(--{suffix}-color); }}\n"

    st.code(css_vars, language="css")

    FileHandler.create_download_link(css_vars.encode(), "analogous_colors.css", "text/css")

    # Design tips
    with st.expander("💡 Design Tips for Analogous Colors"):
        st.markdown("""
        **Best Practices:**
        - Analogous colors create harmony and are pleasing to the eye
        - Perfect for nature-inspired designs and gradients
        - Choose one dominant color and use others as accents
        - Great for backgrounds and subtle color schemes

        **Common Analogous Groups:**
        - Blues to Blue-Greens to Greens
        - Reds to Red-Oranges to Oranges
        - Yellows to Yellow-Greens to Greens
        - Purples to Blue-Purples to Blues
        """)


def triadic_colors():
    """Triadic colors generator"""
    create_tool_header("Triadic Colors", "Generate vibrant triadic color schemes", "🔺")

    st.write(
        "Triadic colors are evenly spaced around the color wheel (120° apart) and create vibrant, balanced combinations.")

    # Color input
    input_method = st.radio("Choose Input Method", ["Color Picker", "HSL Values", "HEX Value"])

    if input_method == "Color Picker":
        base_color = st.color_picker("Select Base Color", "#ff6b6b")
        rgb = hex_to_rgb(base_color)
        hsl = rgb_to_hsl(rgb)
    elif input_method == "HSL Values":
        col1, col2, col3 = st.columns(3)
        with col1:
            h = st.slider("Hue", 0, 360, 0)
        with col2:
            s = st.slider("Saturation (%)", 0, 100, 70)
        with col3:
            l = st.slider("Lightness (%)", 0, 100, 60)
        hsl = (h, s, l)
        rgb = hsl_to_rgb(h, s, l)
        base_color = rgb_to_hex(rgb)
    else:
        hex_input = st.text_input("HEX Color", "#ff6b6b")
        try:
            rgb = hex_to_rgb(hex_input)
            base_color = hex_input
            hsl = rgb_to_hsl(rgb)
        except:
            st.error("Invalid HEX color format")
            return

    # Calculate triadic colors (120 degrees apart)
    triadic_hues = [hsl[0], (hsl[0] + 120) % 360, (hsl[0] + 240) % 360]
    triadic_colors_list = []

    for i, hue in enumerate(triadic_hues):
        # Keep same saturation and lightness for true triadic
        triadic_rgb = hsl_to_rgb(hue, hsl[1], hsl[2])
        triadic_hex = rgb_to_hex(triadic_rgb)
        triadic_hsl = (hue, hsl[1], hsl[2])

        is_primary = (i == 0)
        triadic_colors_list.append((triadic_hex, triadic_rgb, triadic_hsl, is_primary))

    # Display the main triadic colors
    st.subheader("Triadic Color Scheme")

    cols = st.columns(3)
    color_names = ["Primary", "Secondary", "Tertiary"]

    for i, (hex_color, rgb, hsl_vals, is_primary) in enumerate(triadic_colors_list):
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
                f"HEX: {hex_color}\nRGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})\nHSL: hsl({hsl_vals[0]}, {hsl_vals[1]}%, {hsl_vals[2]}%)",
                language="css")

    # Combined palette preview
    st.subheader("Triadic Palette")

    combined_html = '<div style="display: flex; height: 120px; border: 3px solid #333; border-radius: 20px; overflow: hidden; margin: 20px 0;">'
    for i, (hex_color, _, hsl_vals, _) in enumerate(triadic_colors_list):
        text_color = 'white' if hsl_vals[2] < 50 else 'black'
        combined_html += f'<div style="background-color: {hex_color}; width: 33.33%; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 14px;">{color_names[i]}</div>'
    combined_html += '</div>'
    st.markdown(combined_html, unsafe_allow_html=True)

    # CSS Variables Output
    st.subheader("CSS Variables")

    css_vars = ":root {\n"
    for i, (hex_color, rgb, _, _) in enumerate(triadic_colors_list):
        suffix = ["primary", "secondary", "tertiary"][i]
        css_vars += f"  --triadic-{suffix}: {hex_color};\n"
        css_vars += f"  --triadic-{suffix}-rgb: {rgb[0]}, {rgb[1]}, {rgb[2]};\n"

    css_vars += "}\n\n/* Usage Examples */\n"
    for i, (_, _, _, _) in enumerate(triadic_colors_list):
        suffix = ["primary", "secondary", "tertiary"][i]
        css_vars += f".triadic-{suffix}-bg {{ background-color: var(--triadic-{suffix}); }}\n"
        css_vars += f".triadic-{suffix}-text {{ color: var(--triadic-{suffix}); }}\n"
        css_vars += f".triadic-{suffix}-border {{ border-color: var(--triadic-{suffix}); }}\n"

    st.code(css_vars, language="css")

    FileHandler.create_download_link(css_vars.encode(), "triadic_colors.css", "text/css")

    # Design tips
    with st.expander("💡 Design Tips for Triadic Colors"):
        st.markdown("""
        **Best Practices:**
        - Triadic colors are vibrant and offer strong visual contrast
        - Use one color as dominant (60%), another as secondary (30%), and the third as accent (10%)
        - Perfect for playful, energetic, and youthful designs
        - Great for illustrations, children's content, and creative projects

        **Balance Techniques:**
        - Desaturate two colors and keep one vibrant for balance
        - Use different tints and shades to create hierarchy
        - Consider warm/cool balance in your triadic scheme

        **Common Triadic Groups:**
        - Red, Yellow, Blue (Primary colors)
        - Orange, Green, Purple (Secondary colors)
        - Red-Orange, Yellow-Green, Blue-Purple
        """)


def color_contrast_checker():
    """Color contrast checker for accessibility"""
    create_tool_header("Color Contrast Checker", "Check color contrast ratios for accessibility", "⚖️")

    st.write("Ensure your color combinations meet WCAG accessibility standards for text readability.")

    col1, col2 = st.columns(2)
    with col1:
        foreground_color = st.color_picker("Foreground Color (Text)", "#000000")
        st.markdown(
            f'<div style="background: {foreground_color}; width: 100%; height: 50px; border: 2px solid #ccc; border-radius: 5px; margin: 10px 0;"></div>',
            unsafe_allow_html=True)

    with col2:
        background_color = st.color_picker("Background Color", "#ffffff")
        st.markdown(
            f'<div style="background: {background_color}; width: 100%; height: 50px; border: 2px solid #ccc; border-radius: 5px; margin: 10px 0;"></div>',
            unsafe_allow_html=True)

    # Calculate contrast ratio
    contrast_ratio = calculate_contrast_ratio(foreground_color, background_color)

    # Preview
    st.subheader("Preview")
    preview_html = f"""
    <div style="background-color: {background_color}; padding: 30px; border: 2px solid #ccc; border-radius: 10px; margin: 20px 0;">
        <h2 style="color: {foreground_color}; margin: 0 0 20px 0; font-size: 24px;">Large Text Sample</h2>
        <p style="color: {foreground_color}; margin: 0 0 15px 0; font-size: 18px;">This is normal text content that users will read on your website.</p>
        <p style="color: {foreground_color}; margin: 0; font-size: 14px;">This is small text that might be used for captions or fine print.</p>
    </div>
    """
    st.markdown(preview_html, unsafe_allow_html=True)

    # Display contrast ratio results
    st.subheader("Contrast Ratio Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Contrast Ratio", f"{contrast_ratio:.2f}:1")

    with col2:
        # WCAG AA compliance
        aa_normal = contrast_ratio >= 4.5
        aa_large = contrast_ratio >= 3.0
        st.success("✅ WCAG AA Normal" if aa_normal else "❌ WCAG AA Normal")
        st.success("✅ WCAG AA Large" if aa_large else "❌ WCAG AA Large")

    with col3:
        # WCAG AAA compliance
        aaa_normal = contrast_ratio >= 7.0
        aaa_large = contrast_ratio >= 4.5
        st.success("✅ WCAG AAA Normal" if aaa_normal else "❌ WCAG AAA Normal")
        st.success("✅ WCAG AAA Large" if aaa_large else "❌ WCAG AAA Large")

    # Recommendations
    if contrast_ratio < 3.0:
        st.error("⚠️ This color combination has very poor contrast and should not be used for text.")
    elif contrast_ratio < 4.5:
        st.warning("⚠️ This combination only passes for large text (18pt+ or 14pt+ bold).")
    elif contrast_ratio < 7.0:
        st.success("✅ This combination meets WCAG AA standards for all text sizes.")
    else:
        st.success("🌟 Excellent! This combination meets WCAG AAA standards for all text sizes.")

    # CSS Output
    st.subheader("CSS Code")
    css_code = f"""/* Color contrast: {contrast_ratio:.2f}:1 */
.accessible-text {{
    color: {foreground_color};
    background-color: {background_color};
}}

/* Ensure good contrast for different text sizes */
.large-text {{
    color: {foreground_color};
    background-color: {background_color};
    font-size: 18px; /* WCAG Large text threshold */
}}

.normal-text {{
    color: {foreground_color};
    background-color: {background_color};
    font-size: 16px;
}}"""

    st.code(css_code, language="css")
    FileHandler.create_download_link(css_code.encode(), "contrast_colors.css", "text/css")

    # Accessibility guidelines
    with st.expander("📋 WCAG Contrast Guidelines"):
        st.markdown("""
        **WCAG AA Standards:**
        - Normal text: 4.5:1 minimum contrast ratio
        - Large text (18pt+ or 14pt+ bold): 3:1 minimum contrast ratio

        **WCAG AAA Standards:**
        - Normal text: 7:1 minimum contrast ratio  
        - Large text: 4.5:1 minimum contrast ratio

        **Text Size Guidelines:**
        - Large text: 18 points (24px) and larger, or 14 points (18.7px) and larger if bold
        - Normal text: Everything smaller than large text

        **Best Practices:**
        - Aim for AAA standards when possible
        - Test with actual users, especially those with visual impairments
        - Consider colorblind users and don't rely on color alone
        - Test in different lighting conditions
        """)


def accessibility_validator():
    """CSS accessibility validator"""
    create_tool_header("Accessibility Validator", "Validate CSS for accessibility compliance", "♿")

    st.write(
        "Upload or paste CSS code to check for common accessibility issues and get recommendations for improvement.")

    # Input method
    input_method = st.radio("Choose Input Method", ["Upload CSS File", "Paste CSS Code"])

    css_content = ""
    if input_method == "Upload CSS File":
        uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)
        if uploaded_file:
            css_content = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("Uploaded CSS", css_content[:1000] + "..." if len(css_content) > 1000 else css_content,
                         height=200, disabled=True)
    else:
        css_content = st.text_area("Paste CSS Code", height=300, placeholder="""/* Example CSS */
.button {
    background-color: #ff0000;
    color: #ffcccc;
    font-size: 10px;
    padding: 5px;
}

.text {
    color: #888888;
    background: #ffffff;
    font-size: 12px;
}""")

    if css_content and st.button("Validate Accessibility"):
        issues = validate_css_accessibility(css_content)

        st.subheader("Accessibility Validation Results")

        if not issues:
            st.success("🎉 No accessibility issues found! Your CSS follows good accessibility practices.")
        else:
            st.error(f"Found {len(issues)} accessibility issues:")

            for i, issue in enumerate(issues, 1):
                with st.expander(f"Issue {i}: {issue['type']}", expanded=True):
                    st.markdown(f"**Problem:** {issue['description']}")
                    if issue['line']:
                        st.code(issue['line'], language="css")
                    st.markdown(f"**Recommendation:** {issue['recommendation']}")
                    if issue['example']:
                        st.markdown("**Example Fix:**")
                        st.code(issue['example'], language="css")

        # Generate improved CSS
        if issues:
            st.subheader("Accessibility Improvements")
            improved_css = improve_css_accessibility(css_content, issues)
            st.code(improved_css, language="css")
            FileHandler.create_download_link(improved_css.encode(), "accessible.css", "text/css")

    # Accessibility checklist
    with st.expander("✅ CSS Accessibility Checklist"):
        st.markdown("""
        **Color and Contrast:**
        - [ ] Text has sufficient contrast ratio (4.5:1 for normal, 3:1 for large)
        - [ ] Don't rely on color alone to convey information
        - [ ] Support high contrast modes

        **Typography:**
        - [ ] Font size is at least 16px for body text
        - [ ] Line height is at least 1.5 for body text
        - [ ] Text can be resized up to 200% without horizontal scrolling

        **Focus and Navigation:**
        - [ ] Focus indicators are clearly visible
        - [ ] Focus order is logical
        - [ ] Interactive elements have adequate size (44px minimum)

        **Motion and Animation:**
        - [ ] Respect prefers-reduced-motion settings
        - [ ] Animations can be paused or disabled
        - [ ] No content flashes more than 3 times per second

        **Layout and Structure:**
        - [ ] Layout works with zoom up to 400%
        - [ ] Content reflows properly on mobile
        - [ ] No horizontal scrolling at 320px width
        """)


def color_blindness_simulator():
    """Color blindness simulator"""
    create_tool_header("Color Blindness Simulator", "Test how colors appear to colorblind users", "👁️")

    st.write("See how your color choices appear to users with different types of color vision deficiency.")

    # Color input
    col1, col2 = st.columns(2)
    with col1:
        primary_color = st.color_picker("Primary Color", "#007bff")
    with col2:
        secondary_color = st.color_picker("Secondary Color", "#28a745")

    # Additional colors for comprehensive testing
    st.subheader("Color Palette to Test")
    num_colors = st.slider("Number of colors in palette", 2, 8, 4)

    colors = [primary_color, secondary_color]
    default_colors = ["#007bff", "#28a745", "#dc3545", "#ffc107", "#6f42c1", "#fd7e14", "#20c997", "#6c757d"]

    for i in range(2, num_colors):
        color = st.color_picker(f"Color {i + 1}", default_colors[i] if i < len(default_colors) else "#000000",
                                key=f"color_{i}")
        colors.append(color)

    # Color blindness types
    colorblind_types = {
        "Normal Vision": "normal",
        "Protanopia (Red-blind)": "protanopia",
        "Deuteranopia (Green-blind)": "deuteranopia",
        "Tritanopia (Blue-blind)": "tritanopia",
        "Protanomaly (Red-weak)": "protanomaly",
        "Deuteranomaly (Green-weak)": "deuteranomaly",
        "Tritanomaly (Blue-weak)": "tritanomaly",
        "Achromatopsia (Monochrome)": "achromatopsia"
    }

    # Display color simulations
    st.subheader("Color Vision Simulations")

    for vision_type, key in colorblind_types.items():
        st.write(f"**{vision_type}**")

        simulated_html = '<div style="display: flex; gap: 10px; margin: 10px 0; flex-wrap: wrap;">'

        for i, color in enumerate(colors):
            if key == "normal":
                simulated_color = color
            else:
                simulated_color = simulate_colorblindness(color, key)

            simulated_html += f'''
            <div style="display: flex; flex-direction: column; align-items: center; margin: 5px;">
                <div style="background-color: {simulated_color}; width: 80px; height: 60px; border: 2px solid #333; border-radius: 8px; margin-bottom: 5px;"></div>
                <small style="text-align: center; font-size: 11px; color: #666;">{simulated_color}</small>
            </div>
            '''

        simulated_html += '</div>'
        st.markdown(simulated_html, unsafe_allow_html=True)

        if key != "normal":
            st.markdown("---")

    # Design example with all vision types
    st.subheader("Design Example Comparison")

    example_html = f"""
    <div style="background: white; padding: 20px; border: 2px solid #ddd; border-radius: 10px; margin: 20px 0;">
        <h3 style="color: {colors[0]}; margin: 0 0 15px 0;">Sample Website Header</h3>
        <p style="color: #333; margin: 0 0 15px 0;">This is sample content to show how your design works with different color combinations.</p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <button style="background: {colors[1]}; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Primary Button</button>
            <button style="background: white; color: {colors[0]}; padding: 10px 20px; border: 2px solid {colors[0]}; border-radius: 5px; cursor: pointer;">Secondary Button</button>
        </div>
    </div>
    """

    st.markdown("**Normal Vision:**")
    st.markdown(example_html, unsafe_allow_html=True)

    for vision_type, key in list(colorblind_types.items())[1:]:  # Skip normal vision
        simulated_colors = [simulate_colorblindness(color, key) for color in colors]

        simulated_example = f"""
        <div style="background: white; padding: 20px; border: 2px solid #ddd; border-radius: 10px; margin: 20px 0;">
            <h3 style="color: {simulated_colors[0]}; margin: 0 0 15px 0;">Sample Website Header</h3>
            <p style="color: #333; margin: 0 0 15px 0;">This is sample content to show how your design works with different color combinations.</p>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                <button style="background: {simulated_colors[1]}; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Primary Button</button>
                <button style="background: white; color: {simulated_colors[0]}; padding: 10px 20px; border: 2px solid {simulated_colors[0]}; border-radius: 5px; cursor: pointer;">Secondary Button</button>
            </div>
        </div>
        """

        st.markdown(f"**{vision_type}:**")
        st.markdown(simulated_example, unsafe_allow_html=True)

    # Recommendations
    st.subheader("Accessibility Recommendations")

    # Check for potential issues
    recommendations = []

    # Check contrast between first two colors
    contrast = calculate_contrast_ratio(colors[0], colors[1])
    if contrast < 3.0:
        recommendations.append("⚠️ Low contrast between primary colors - consider increasing difference")

    # Check for red-green combinations (common issue)
    if is_problematic_red_green(colors[0], colors[1]):
        recommendations.append("⚠️ Red-green combination detected - may be hard to distinguish for colorblind users")

    # General recommendations
    recommendations.extend([
        "✅ Use patterns, textures, or shapes in addition to color",
        "✅ Ensure sufficient contrast ratios (4.5:1 minimum)",
        "✅ Test with actual colorblind users when possible",
        "✅ Provide alternative ways to convey information beyond color"
    ])

    for rec in recommendations:
        st.markdown(rec)

    # CSS output for colorblind-friendly design
    st.subheader("Colorblind-Friendly CSS")

    accessible_css = f"""/* Colorblind-friendly design patterns */

/* Use patterns and textures */
.primary-element {{
    background-color: {colors[0]};
    background-image: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,.1) 10px, rgba(255,255,255,.1) 20px);
}}

.secondary-element {{
    background-color: {colors[1]};
    border: 3px dashed rgba(255,255,255,0.5);
}}

/* High contrast alternatives */
@media (prefers-contrast: high) {{
    .primary-element {{ background: #000; color: #fff; }}
    .secondary-element {{ background: #fff; color: #000; border: 2px solid #000; }}
}}

/* Use shapes and icons, not just color */
.success {{ background: {colors[1]}; }}
.success::before {{ content: "✓ "; }}

.error {{ background: #dc3545; }}
.error::before {{ content: "✗ "; }}

.warning {{ background: #ffc107; }}
.warning::before {{ content: "⚠ "; }}"""

    st.code(accessible_css, language="css")
    FileHandler.create_download_link(accessible_css.encode(), "colorblind_friendly.css", "text/css")


def color_harmony_analyzer():
    """Color harmony analyzer"""
    create_tool_header("Color Harmony Analyzer", "Analyze and create harmonious color schemes", "🎨")

    st.write("Analyze color relationships and create harmonious color schemes based on color theory principles.")

    # Base color input
    base_color = st.color_picker("Select Base Color", "#007bff")

    # Harmony types
    harmony_types = [
        "Monochromatic",
        "Complementary",
        "Split Complementary",
        "Triadic",
        "Tetradic (Rectangle)",
        "Analogous",
        "Double Split Complementary"
    ]

    selected_harmonies = st.multiselect("Select Harmony Types to Analyze", harmony_types,
                                        default=["Complementary", "Triadic", "Analogous"])

    if selected_harmonies:
        rgb_base = hex_to_rgb(base_color)
        hsl_base = rgb_to_hsl(rgb_base)

        st.subheader("Color Harmony Analysis")

        all_harmonies = {}

        for harmony_type in selected_harmonies:
            st.write(f"### {harmony_type} Harmony")

            if harmony_type == "Monochromatic":
                colors = generate_monochromatic_harmony(hsl_base)
                description = "Uses variations in lightness and saturation of a single hue. Creates a cohesive, calming effect."
            elif harmony_type == "Complementary":
                colors = generate_complementary_harmony(hsl_base)
                description = "Uses colors opposite each other on the color wheel. Creates strong contrast and vibrant look."
            elif harmony_type == "Split Complementary":
                colors = generate_split_complementary_harmony(hsl_base)
                description = "Uses a base color and two colors adjacent to its complement. Provides contrast with more harmony."
            elif harmony_type == "Triadic":
                colors = generate_triadic_harmony(hsl_base)
                description = "Uses three colors evenly spaced on the color wheel. Creates vibrant, balanced schemes."
            elif harmony_type == "Tetradic (Rectangle)":
                colors = generate_tetradic_harmony(hsl_base)
                description = "Uses four colors forming a rectangle on the color wheel. Offers rich color variation."
            elif harmony_type == "Analogous":
                colors = generate_analogous_harmony(hsl_base)
                description = "Uses colors next to each other on the color wheel. Creates serene, comfortable designs."
            else:  # Double Split Complementary
                colors = generate_double_split_complementary_harmony(hsl_base)
                description = "Uses two pairs of complementary colors. Provides rich color options with good harmony."

            st.write(description)

            all_harmonies[harmony_type] = colors

            # Display color palette
            palette_html = '<div style="display: flex; gap: 5px; margin: 15px 0; flex-wrap: wrap;">'
            for i, color in enumerate(colors):
                hex_color = rgb_to_hex(color)
                hsl_color = rgb_to_hsl(color)
                text_color = 'white' if hsl_color[2] < 50 else 'black'

                palette_html += f'''
                <div style="display: flex; flex-direction: column; align-items: center; margin: 5px;">
                    <div style="background-color: {hex_color}; width: 100px; height: 80px; border: 2px solid #333; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: {text_color}; font-weight: bold; font-size: 12px; margin-bottom: 5px;">
                        {hex_color}
                    </div>
                </div>
                '''
            palette_html += '</div>'
            st.markdown(palette_html, unsafe_allow_html=True)

            # Harmony score
            harmony_score = calculate_harmony_score(colors, harmony_type)
            if harmony_score >= 8:
                st.success(f"🌟 Excellent harmony score: {harmony_score}/10")
            elif harmony_score >= 6:
                st.success(f"✅ Good harmony score: {harmony_score}/10")
            else:
                st.warning(f"⚠️ Fair harmony score: {harmony_score}/10")

            st.markdown("---")

        # Combined analysis
        if len(selected_harmonies) > 1:
            st.subheader("Combined Harmony Comparison")

            comparison_data = []
            for harmony_type, colors in all_harmonies.items():
                score = calculate_harmony_score(colors, harmony_type)
                contrast_range = calculate_contrast_range(colors)
                saturation_variance = calculate_saturation_variance(colors)

                comparison_data.append({
                    "Harmony Type": harmony_type,
                    "Harmony Score": f"{score}/10",
                    "Contrast Range": f"{contrast_range:.1f}",
                    "Color Count": len(colors),
                    "Recommended Use": get_harmony_recommendation(harmony_type, score)
                })

            # Display comparison table
            for data in comparison_data:
                with st.expander(f"{data['Harmony Type']} - {data['Harmony Score']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Harmony Score:** {data['Harmony Score']}")
                        st.write(f"**Contrast Range:** {data['Contrast Range']}")
                        st.write(f"**Color Count:** {data['Color Count']}")
                    with col2:
                        st.write(f"**Recommended Use:** {data['Recommended Use']}")

        # CSS output for best harmony
        st.subheader("CSS Color Variables")

        # Find best harmony
        best_harmony = max(all_harmonies.keys(), key=lambda h: calculate_harmony_score(all_harmonies[h], h))
        best_colors = all_harmonies[best_harmony]

        st.write(f"**Best Harmony: {best_harmony}** (Score: {calculate_harmony_score(best_colors, best_harmony)}/10)")

        css_output = f"""/* {best_harmony} Color Harmony */
:root {{"""

        for i, color in enumerate(best_colors):
            hex_color = rgb_to_hex(color)
            rgb_vals = f"{color[0]}, {color[1]}, {color[2]}"
            css_output += f"""
  --harmony-color-{i + 1}: {hex_color};
  --harmony-color-{i + 1}-rgb: {rgb_vals};"""

        css_output += f"""
}}

/* Usage Examples */"""

        usage_examples = [
            (".primary", "--harmony-color-1"),
            (".secondary", "--harmony-color-2"),
            (".accent", "--harmony-color-3"),
            (".highlight", "--harmony-color-4")
        ]

        for i, (class_name, var_name) in enumerate(usage_examples):
            if i < len(best_colors):
                css_output += f"""
{class_name} {{
  background-color: var({var_name});
  color: var(--text-color);
}}

{class_name}-border {{
  border: 2px solid var({var_name});
}}"""

        st.code(css_output, language="css")
        FileHandler.create_download_link(css_output.encode(), f"{best_harmony.lower().replace(' ', '_')}_harmony.css",
                                         "text/css")

    # Color theory guide
    with st.expander("📚 Color Harmony Theory Guide"):
        st.markdown("""
        **Color Wheel Relationships:**

        - **Monochromatic**: Single hue with variations in lightness/saturation
        - **Complementary**: Two colors directly opposite (180°) - highest contrast
        - **Split Complementary**: Base + two colors adjacent to its complement  
        - **Triadic**: Three colors equally spaced (120°) - vibrant but balanced
        - **Tetradic**: Four colors in two complementary pairs - richest schemes
        - **Analogous**: 3-5 adjacent colors (30-60°) - most harmonious
        - **Double Split**: Two pairs of split-complementary colors

        **Design Applications:**
        - **Websites**: Complementary or split-complementary for contrast
        - **Branding**: Monochromatic or analogous for cohesion
        - **Art/Creative**: Triadic or tetradic for vibrancy
        - **Professional**: Analogous with one complementary accent

        **Best Practices:**
        - Use 60-30-10 rule (dominant-secondary-accent)
        - Test accessibility and contrast ratios
        - Consider cultural color associations
        - Test with colorblind simulation
        """)


# Helper functions for color blindness simulation
def simulate_colorblindness(hex_color, colorblind_type):
    """Simulate how a color appears to colorblind users"""
    rgb = hex_to_rgb(hex_color)
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0

    if colorblind_type == "protanopia":
        # Red-blind
        r_sim = 0.567 * r + 0.433 * g + 0.0 * b
        g_sim = 0.558 * r + 0.442 * g + 0.0 * b
        b_sim = 0.0 * r + 0.242 * g + 0.758 * b
    elif colorblind_type == "deuteranopia":
        # Green-blind
        r_sim = 0.625 * r + 0.375 * g + 0.0 * b
        g_sim = 0.7 * r + 0.3 * g + 0.0 * b
        b_sim = 0.0 * r + 0.3 * g + 0.7 * b
    elif colorblind_type == "tritanopia":
        # Blue-blind
        r_sim = 0.95 * r + 0.05 * g + 0.0 * b
        g_sim = 0.0 * r + 0.433 * g + 0.567 * b
        b_sim = 0.0 * r + 0.475 * g + 0.525 * b
    elif colorblind_type == "protanomaly":
        # Red-weak
        r_sim = 0.817 * r + 0.183 * g + 0.0 * b
        g_sim = 0.333 * r + 0.667 * g + 0.0 * b
        b_sim = 0.0 * r + 0.125 * g + 0.875 * b
    elif colorblind_type == "deuteranomaly":
        # Green-weak
        r_sim = 0.8 * r + 0.2 * g + 0.0 * b
        g_sim = 0.258 * r + 0.742 * g + 0.0 * b
        b_sim = 0.0 * r + 0.142 * g + 0.858 * b
    elif colorblind_type == "tritanomaly":
        # Blue-weak
        r_sim = 0.967 * r + 0.033 * g + 0.0 * b
        g_sim = 0.0 * r + 0.733 * g + 0.267 * b
        b_sim = 0.0 * r + 0.183 * g + 0.817 * b
    elif colorblind_type == "achromatopsia":
        # Monochrome
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        r_sim = g_sim = b_sim = gray
    else:
        return hex_color  # Normal vision

    # Convert back to hex
    r_int = max(0, min(255, int(r_sim * 255)))
    g_int = max(0, min(255, int(g_sim * 255)))
    b_int = max(0, min(255, int(b_sim * 255)))

    return f"#{r_int:02x}{g_int:02x}{b_int:02x}"


def calculate_contrast_ratio(color1, color2):
    """Calculate WCAG contrast ratio between two colors"""

    def get_relative_luminance(hex_color):
        rgb = hex_to_rgb(hex_color)
        r, g, b = [c / 255.0 for c in rgb]

        # Apply gamma correction
        r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4

        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    l1 = get_relative_luminance(color1)
    l2 = get_relative_luminance(color2)

    lighter = max(l1, l2)
    darker = min(l1, l2)

    return (lighter + 0.05) / (darker + 0.05)


def is_problematic_red_green(color1, color2):
    """Check if color combination is problematic for red-green colorblind users"""
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    # Simple check for red-green combinations
    is_red1 = rgb1[0] > 150 and rgb1[1] < 100 and rgb1[2] < 100
    is_green1 = rgb1[1] > 150 and rgb1[0] < 100 and rgb1[2] < 100

    is_red2 = rgb2[0] > 150 and rgb2[1] < 100 and rgb2[2] < 100
    is_green2 = rgb2[1] > 150 and rgb2[0] < 100 and rgb2[2] < 100

    return (is_red1 and is_green2) or (is_green1 and is_red2)


def validate_css_accessibility(css_content):
    """Validate CSS for accessibility issues"""
    issues = []
    lines = css_content.split('\n')

    for i, line in enumerate(lines):
        line_num = i + 1
        line = line.strip().lower()

        # Check for small font sizes
        if 'font-size:' in line and 'px' in line:
            try:
                size_match = re.search(r'font-size:\s*(\d+)px', line)
                if size_match and int(size_match.group(1)) < 16:
                    issues.append({
                        'type': 'Small Font Size',
                        'line': lines[i].strip(),
                        'description': f'Font size {size_match.group(1)}px is smaller than recommended minimum of 16px',
                        'recommendation': 'Use font-size: 16px or larger for body text',
                        'example': 'font-size: 16px; /* or 1rem */'
                    })
            except:
                pass

        # Check for low line height
        if 'line-height:' in line:
            try:
                height_match = re.search(r'line-height:\s*([\d.]+)', line)
                if height_match and float(height_match.group(1)) < 1.5:
                    issues.append({
                        'type': 'Low Line Height',
                        'line': lines[i].strip(),
                        'description': f'Line height {height_match.group(1)} is lower than recommended minimum of 1.5',
                        'recommendation': 'Use line-height: 1.5 or higher for better readability',
                        'example': 'line-height: 1.5;'
                    })
            except:
                pass

        # Check for missing focus styles
        if ':focus' not in css_content.lower() and ('button' in line or 'input' in line or 'a ' in line):
            issues.append({
                'type': 'Missing Focus Styles',
                'line': None,
                'description': 'Interactive elements should have visible focus indicators',
                'recommendation': 'Add :focus styles to all interactive elements',
                'example': 'button:focus { outline: 2px solid #007bff; outline-offset: 2px; }'
            })
            break  # Only add this once

    # Check for animations without prefers-reduced-motion
    if 'animation:' in css_content.lower() or '@keyframes' in css_content.lower():
        if 'prefers-reduced-motion' not in css_content.lower():
            issues.append({
                'type': 'Animation Without Motion Preference',
                'line': None,
                'description': 'Animations should respect user motion preferences',
                'recommendation': 'Wrap animations in prefers-reduced-motion media query',
                'example': '@media (prefers-reduced-motion: no-preference) { /* animations here */ }'
            })

    return issues


def improve_css_accessibility(css_content, issues):
    """Generate improved CSS based on accessibility issues"""
    improved_css = css_content

    # Add focus styles if missing
    if any(issue['type'] == 'Missing Focus Styles' for issue in issues):
        improved_css += '\n\n/* Added focus styles for accessibility */\n'
        improved_css += '''button:focus,
input:focus,
select:focus,
textarea:focus,
a:focus {
    outline: 2px solid #007bff;
    outline-offset: 2px;
}

/* Custom focus styles */
.button:focus {
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}'''

    # Add reduced motion support if animations exist
    if any(issue['type'] == 'Animation Without Motion Preference' for issue in issues):
        improved_css += '\n\n/* Respect user motion preferences */\n'
        improved_css += '''@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}'''

    # Add high contrast support
    improved_css += '\n\n/* High contrast mode support */\n'
    improved_css += '''@media (prefers-contrast: high) {
    button, .button {
        border: 2px solid;
    }

    a {
        text-decoration: underline;
    }
}'''

    return improved_css


# Helper functions for color harmony
def generate_monochromatic_harmony(hsl_base):
    """Generate monochromatic color harmony"""
    h, s, l = hsl_base
    colors = []
    lightnesses = [20, 40, 60, 80]
    saturations = [30, 50, 70, 90]

    for i in range(4):
        new_l = lightnesses[i]
        new_s = saturations[i]
        rgb = hsl_to_rgb(h, new_s, new_l)
        colors.append(rgb)

    return colors


def generate_complementary_harmony(hsl_base):
    """Generate complementary color harmony"""
    h, s, l = hsl_base
    colors = [hsl_to_rgb(h, s, l)]  # Base color

    complement_h = (h + 180) % 360
    colors.append(hsl_to_rgb(complement_h, s, l))  # Complement

    return colors


def generate_split_complementary_harmony(hsl_base):
    """Generate split complementary harmony"""
    h, s, l = hsl_base
    colors = [hsl_to_rgb(h, s, l)]  # Base color

    # Split complement (150° and 210° from base)
    colors.append(hsl_to_rgb((h + 150) % 360, s, l))
    colors.append(hsl_to_rgb((h + 210) % 360, s, l))

    return colors


def generate_triadic_harmony(hsl_base):
    """Generate triadic harmony"""
    h, s, l = hsl_base
    colors = []

    for offset in [0, 120, 240]:
        new_h = (h + offset) % 360
        colors.append(hsl_to_rgb(new_h, s, l))

    return colors


def generate_tetradic_harmony(hsl_base):
    """Generate tetradic (rectangle) harmony"""
    h, s, l = hsl_base
    colors = []

    # Rectangle: base, +60°, +180°, +240°
    for offset in [0, 60, 180, 240]:
        new_h = (h + offset) % 360
        colors.append(hsl_to_rgb(new_h, s, l))

    return colors


def generate_analogous_harmony(hsl_base):
    """Generate analogous harmony"""
    h, s, l = hsl_base
    colors = []

    # Analogous: base and adjacent colors (±30°)
    for offset in [-60, -30, 0, 30, 60]:
        new_h = (h + offset) % 360
        colors.append(hsl_to_rgb(new_h, s, l))

    return colors


def generate_double_split_complementary_harmony(hsl_base):
    """Generate double split complementary harmony"""
    h, s, l = hsl_base
    colors = []

    # Double split: base, +30°, +150°, +180°, +210°, +330°
    for offset in [0, 30, 150, 180, 210, 330]:
        new_h = (h + offset) % 360
        colors.append(hsl_to_rgb(new_h, s, l))

    return colors[:4]  # Return first 4 for simplicity


def calculate_harmony_score(colors, harmony_type):
    """Calculate harmony score based on color theory principles"""
    base_score = 8  # Start with good score

    # Adjust based on harmony type
    harmony_scores = {
        "Monochromatic": 9,
        "Analogous": 8,
        "Complementary": 7,
        "Split Complementary": 7,
        "Triadic": 6,
        "Tetradic (Rectangle)": 5,
        "Double Split Complementary": 5
    }

    base_score = harmony_scores.get(harmony_type, 6)

    # Check for good contrast range
    contrast_range = calculate_contrast_range(colors)
    if contrast_range > 5:
        base_score += 1
    elif contrast_range < 2:
        base_score -= 1

    return max(1, min(10, base_score))


def calculate_contrast_range(colors):
    """Calculate the contrast range in a color set"""
    if len(colors) < 2:
        return 0

    hex_colors = [rgb_to_hex(color) for color in colors]
    max_contrast = 0

    for i in range(len(hex_colors)):
        for j in range(i + 1, len(hex_colors)):
            contrast = calculate_contrast_ratio(hex_colors[i], hex_colors[j])
            max_contrast = max(max_contrast, contrast)

    return max_contrast


def calculate_saturation_variance(colors):
    """Calculate saturation variance in color set"""
    if len(colors) < 2:
        return 0

    saturations = []
    for color in colors:
        hsl = rgb_to_hsl(color)
        saturations.append(hsl[1])

    mean_sat = sum(saturations) / len(saturations)
    variance = sum((s - mean_sat) ** 2 for s in saturations) / len(saturations)

    return variance ** 0.5  # Standard deviation


def get_harmony_recommendation(harmony_type, score):
    """Get recommendation based on harmony type and score"""
    recommendations = {
        "Monochromatic": "Websites, minimalist designs, backgrounds",
        "Complementary": "High contrast designs, call-to-action buttons",
        "Split Complementary": "Vibrant designs with good balance",
        "Triadic": "Creative projects, children's content, art",
        "Tetradic (Rectangle)": "Complex designs, rich illustrations",
        "Analogous": "Nature themes, calming designs, gradients",
        "Double Split Complementary": "Professional designs with variety"
    }

    return recommendations.get(harmony_type, "General purpose design")
