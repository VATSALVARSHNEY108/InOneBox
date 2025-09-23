__author__ = "VATSAL VARSHNEY"
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps
import cv2
import io
import zipfile
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler
import time
import base64
import colorsys


def display_tools():
    tool_categories = {
        "Conversion Tools": [
            "Format Converter", "Batch Converter", "Animated GIF Creator", "PDF to Image", "SVG Converter"
        ],
        "Editing Tools": [
            "Image Resizer", "Image Cropper", "Rotate & Flip", "Brightness/Contrast", "Color Adjustment"
        ],
        "Design Tools": [
            "Canvas Creator", "Text Overlay", "Watermark Tool", "Collage Maker", "Border Tool"
        ],
        "Color Tools": [
            "Palette Extractor", "Color Replacer", "Histogram Analyzer", "Color Balance", "Hue Adjuster"
        ],
        "Analysis Tools": [
            "Metadata Extractor", "Image Comparison", "Face Detection", "Object Detection", "Image Statistics",
            "Image Recognition", "Scene Analysis", "OCR Reader", "Visual Search"
        ],
        "Compression Tools": [
            "Image Compressor", "Quality Optimizer", "Batch Compression", "Format-Specific Compression"
        ],
        "Effects Tools": [
            "Blur Effects", "Artistic Filters", "Vintage Effects", "Edge Detection", "Noise Reduction"
        ],
        "Annotation Tools": [
            "Shape Drawer", "Text Annotations", "Highlighting Tool", "Redaction Tool", "Markup Tool"
        ],
        "Miscellaneous": [
            "Icon Generator", "Placeholder Creator", "Image Statistics", "Format Info", "EXIF Viewer"
        ]
    }

    selected_category = st.selectbox("Select Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Image Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Format Converter":
        format_converter()
    elif selected_tool == "Image Resizer":
        image_resizer()
    elif selected_tool == "Image Cropper":
        image_cropper()
    elif selected_tool == "Palette Extractor":
        palette_extractor()
    elif selected_tool == "Image Compressor":
        image_compressor()
    elif selected_tool == "Quality Optimizer":
        quality_optimizer()
    elif selected_tool == "Batch Compression":
        batch_compression()
    elif selected_tool == "Format-Specific Compression":
        format_specific_compression()
    elif selected_tool == "Watermark Tool":
        watermark_tool()
    elif selected_tool == "Batch Converter":
        batch_converter()
    elif selected_tool == "Brightness/Contrast":
        brightness_contrast()
    elif selected_tool == "Rotate & Flip":
        rotate_flip()
    elif selected_tool == "Color Adjustment":
        color_adjustment()
    elif selected_tool == "Color Balance":
        color_balance()
    elif selected_tool == "Hue Adjuster":
        hue_adjuster()
    elif selected_tool == "Color Replacer":
        color_replacer()
    elif selected_tool == "Histogram Analyzer":
        histogram_analyzer()
    elif selected_tool == "Shape Drawer":
        shape_drawer()
    elif selected_tool == "Text Annotations":
        text_annotations()
    elif selected_tool == "Highlighting Tool":
        highlighting_tool()
    elif selected_tool == "Redaction Tool":
        redaction_tool()
    elif selected_tool == "Markup Tool":
        markup_tool()
    elif selected_tool == "Blur Effects":
        blur_effects()
    elif selected_tool == "Artistic Filters":
        artistic_filters()
    elif selected_tool == "Vintage Effects":
        vintage_effects()
    elif selected_tool == "Edge Detection":
        edge_detection()
    elif selected_tool == "Noise Reduction":
        noise_reduction()
    elif selected_tool == "Metadata Extractor":
        metadata_extractor()
    elif selected_tool == "Background Removal":
        background_removal()
    elif selected_tool == "Text Overlay":
        text_overlay()
    elif selected_tool == "Image Enhancement":
        image_enhancement()
    elif selected_tool == "Collage Maker":
        collage_maker()
    elif selected_tool == "Icon Generator":
        icon_generator()
    elif selected_tool == "Animated GIF Creator":
        animated_gif_creator()
    elif selected_tool == "PDF to Image":
        pdf_to_image()
    elif selected_tool == "SVG Converter":
        svg_converter()
    elif selected_tool == "Image Comparison":
        image_comparison()
    elif selected_tool == "Face Detection":
        face_detection()
    elif selected_tool == "Object Detection":
        object_detection()
    elif selected_tool == "Image Statistics":
        image_statistics()
    elif selected_tool == "Image Recognition":
        image_recognition()
    elif selected_tool == "Scene Analysis":
        scene_analysis()
    elif selected_tool == "OCR Reader":
        ocr_reader()
    elif selected_tool == "Visual Search":
        visual_search()
    elif selected_tool == "Placeholder Creator":
        placeholder_creator()
    elif selected_tool == "Format Info":
        format_info()
    elif selected_tool == "EXIF Viewer":
        exif_viewer()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def format_converter():
    """Convert image formats"""
    create_tool_header("Format Converter", "Convert images between different formats", "🔄")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        target_format = st.selectbox("Target Format", ["PNG", "JPEG", "GIF", "BMP", "TIFF", "WEBP"])

        if target_format == "JPEG":
            quality = st.slider("JPEG Quality", 1, 100, 85)
        else:
            quality = None

        if st.button("Convert Images"):
            converted_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        # Convert RGBA to RGB for JPEG
                        if target_format == "JPEG" and image.mode in ("RGBA", "P"):
                            rgb_image = Image.new("RGB", image.size, (255, 255, 255))
                            rgb_image.paste(image, mask=image.split()[-1] if image.mode == "RGBA" else None)
                            image = rgb_image

                        # Save converted image
                        output = io.BytesIO()
                        save_kwargs = {"format": target_format}
                        if quality and target_format == "JPEG":
                            save_kwargs["quality"] = quality

                        image.save(output, **save_kwargs)

                        # Generate filename
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        new_filename = f"{base_name}.{target_format.lower()}"
                        converted_files[new_filename] = output.getvalue()

                        progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error converting {uploaded_file.name}: {str(e)}")

            if converted_files:
                if len(converted_files) == 1:
                    filename, data = next(iter(converted_files.items()))
                    FileHandler.create_download_link(data, filename, f"image/{target_format.lower()}")
                else:
                    # Create ZIP archive for multiple files
                    zip_data = FileHandler.create_zip_archive(converted_files)
                    FileHandler.create_download_link(zip_data, "converted_images.zip", "application/zip")

                st.success(f"Converted {len(converted_files)} image(s) to {target_format}")


def image_resizer():
    """Resize images"""
    create_tool_header("Image Resizer", "Resize images with various options", "📐")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        resize_method = st.selectbox("Resize Method",
                                     ["Exact Dimensions", "Scale by Percentage", "Fit to Width", "Fit to Height"])

        if resize_method == "Exact Dimensions":
            col1, col2 = st.columns(2)
            with col1:
                width = st.number_input("Width (pixels)", min_value=1, value=800)
            with col2:
                height = st.number_input("Height (pixels)", min_value=1, value=600)
        elif resize_method == "Scale by Percentage":
            scale = st.slider("Scale Percentage", 10, 500, 100)
        elif resize_method == "Fit to Width":
            width = st.number_input("Target Width (pixels)", min_value=1, value=800)
        elif resize_method == "Fit to Height":
            height = st.number_input("Target Height (pixels)", min_value=1, value=600)

        maintain_aspect = st.checkbox("Maintain Aspect Ratio", True)
        resampling = st.selectbox("Resampling Algorithm", ["LANCZOS", "BILINEAR", "BICUBIC", "NEAREST"])

        if st.button("Resize Images"):
            resized_files = {}
            progress_bar = st.progress(0)

            resampling_map = {
                "LANCZOS": Image.Resampling.LANCZOS,
                "BILINEAR": Image.Resampling.BILINEAR,
                "BICUBIC": Image.Resampling.BICUBIC,
                "NEAREST": Image.Resampling.NEAREST
            }

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        original_width, original_height = image.size

                        if resize_method == "Exact Dimensions":
                            if maintain_aspect:
                                image.thumbnail((width, height), resampling_map[resampling])
                                new_image = image
                            else:
                                new_image = image.resize((width, height), resampling_map[resampling])
                        elif resize_method == "Scale by Percentage":
                            new_width = int(original_width * scale / 100)
                            new_height = int(original_height * scale / 100)
                            new_image = image.resize((new_width, new_height), resampling_map[resampling])
                        elif resize_method == "Fit to Width":
                            aspect_ratio = original_height / original_width
                            new_height = int(width * aspect_ratio)
                            new_image = image.resize((width, new_height), resampling_map[resampling])
                        elif resize_method == "Fit to Height":
                            aspect_ratio = original_width / original_height
                            new_width = int(height * aspect_ratio)
                            new_image = image.resize((new_width, height), resampling_map[resampling])

                        # Save resized image
                        output = io.BytesIO()
                        format_name = image.format if image.format else "PNG"
                        new_image.save(output, format=format_name)

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        extension = uploaded_file.name.rsplit('.', 1)[1]
                        new_filename = f"{base_name}_resized.{extension}"
                        resized_files[new_filename] = output.getvalue()

                        progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error resizing {uploaded_file.name}: {str(e)}")

            if resized_files:
                if len(resized_files) == 1:
                    filename, data = next(iter(resized_files.items()))
                    FileHandler.create_download_link(data, filename, "image/png")
                else:
                    zip_data = FileHandler.create_zip_archive(resized_files)
                    FileHandler.create_download_link(zip_data, "resized_images.zip", "application/zip")

                st.success(f"Resized {len(resized_files)} image(s)")


def image_cropper():
    """Crop images"""
    create_tool_header("Image Cropper", "Crop images with precise control", "✂️")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            st.subheader("Original Image")
            st.image(image, caption="Original Image", use_column_width=True)

            width, height = image.size
            st.write(f"Image dimensions: {width} × {height} pixels")

            # Crop parameters
            col1, col2 = st.columns(2)
            with col1:
                left = st.slider("Left", 0, width - 1, 0)
                top = st.slider("Top", 0, height - 1, 0)
            with col2:
                right = st.slider("Right", left + 1, width, width)
                bottom = st.slider("Bottom", top + 1, height, height)

            # Preview crop area
            preview_image = image.copy()
            draw = ImageDraw.Draw(preview_image)
            draw.rectangle([left, top, right, bottom], outline="red", width=3)
            st.image(preview_image, caption="Crop Preview (red rectangle)", use_column_width=True)

            if st.button("Crop Image"):
                try:
                    cropped_image = image.crop((left, top, right, bottom))

                    st.subheader("Cropped Image")
                    st.image(cropped_image, caption="Cropped Image", use_column_width=True)

                    # Save cropped image
                    output = io.BytesIO()
                    format_name = image.format if image.format else "PNG"
                    cropped_image.save(output, format=format_name)

                    base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                    extension = uploaded_file[0].name.rsplit('.', 1)[1]
                    filename = f"{base_name}_cropped.{extension}"

                    FileHandler.create_download_link(output.getvalue(), filename, "image/png")
                    st.success("Image cropped successfully!")

                except Exception as e:
                    st.error(f"Error cropping image: {str(e)}")


def palette_extractor():
    """Extract color palette from images"""
    create_tool_header("Palette Extractor", "Extract dominant colors from images", "🎨")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            st.image(image, caption="Source Image", use_column_width=True)

            num_colors = st.slider("Number of colors to extract", 2, 20, 8)

            if st.button("Extract Palette"):
                try:
                    # Convert image to RGB and resize for faster processing
                    rgb_image = image.convert('RGB')
                    rgb_image.thumbnail((200, 200))

                    # Convert to numpy array
                    img_array = np.array(rgb_image)
                    img_array = img_array.reshape(-1, 3)

                    # Use KMeans to find dominant colors
                    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
                    kmeans.fit(img_array)

                    colors = kmeans.cluster_centers_.astype(int)

                    # Create palette visualization
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

                    # Show original image
                    ax1.imshow(rgb_image)
                    ax1.set_title("Original Image")
                    ax1.axis('off')

                    # Show color palette
                    palette_height = 100
                    palette_width = len(colors) * 50
                    palette_image = np.zeros((palette_height, palette_width, 3), dtype=np.uint8)

                    for i, color in enumerate(colors):
                        start_x = i * 50
                        end_x = (i + 1) * 50
                        palette_image[:, start_x:end_x] = color

                    ax2.imshow(palette_image)
                    ax2.set_title("Extracted Palette")
                    ax2.axis('off')

                    # Display color information
                    st.subheader("Color Palette")
                    st.pyplot(fig)
                    plt.close()

                    # Show color codes
                    st.subheader("Color Codes")
                    for i, color in enumerate(colors):
                        hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
                        rgb_color = f"rgb({color[0]}, {color[1]}, {color[2]})"

                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.markdown(
                                f'<div style="width:50px;height:30px;background-color:{hex_color};border:1px solid #000;"></div>',
                                unsafe_allow_html=True)
                        with col2:
                            st.code(hex_color)
                        with col3:
                            st.code(rgb_color)
                        with col4:
                            st.code(f"HSV: {cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_RGB2HSV)[0][0]}")

                    # Create downloadable palette data
                    palette_data = []
                    for i, color in enumerate(colors):
                        hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
                        rgb_color = f"rgb({color[0]}, {color[1]}, {color[2]})"
                        palette_data.append(f"Color {i + 1}: {hex_color} | {rgb_color}")

                    palette_text = '\n'.join(palette_data)
                    FileHandler.create_download_link(palette_text.encode(), "color_palette.txt", "text/plain")

                except Exception as e:
                    st.error(f"Error extracting palette: {str(e)}")


def image_compressor():
    """Compress images with quality control"""
    create_tool_header("Image Compressor", "Reduce image file sizes", "🗜️")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        compression_method = st.selectbox("Compression Method",
                                          ["Quality Reduction", "Resize + Quality", "Format Optimization"])

        if compression_method in ["Quality Reduction", "Resize + Quality"]:
            quality = st.slider("Quality", 1, 100, 75)

        if compression_method == "Resize + Quality":
            scale_factor = st.slider("Scale Factor", 0.1, 1.0, 0.8)

        target_format = st.selectbox("Output Format", ["Keep Original", "JPEG", "PNG", "WEBP"])

        if st.button("Compress Images"):
            compressed_files = {}
            progress_bar = st.progress(0)
            total_original_size = 0
            total_compressed_size = 0

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        total_original_size += uploaded_file.size

                        # Apply compression method
                        if compression_method == "Resize + Quality":
                            new_width = int(image.width * scale_factor)
                            new_height = int(image.height * scale_factor)
                            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                        # Determine output format
                        if target_format == "Keep Original":
                            output_format = image.format if image.format else "PNG"
                        else:
                            output_format = target_format

                        # Handle format-specific requirements
                        if output_format == "JPEG" and image.mode in ("RGBA", "P"):
                            rgb_image = Image.new("RGB", image.size, (255, 255, 255))
                            rgb_image.paste(image, mask=image.split()[-1] if image.mode == "RGBA" else None)
                            image = rgb_image

                        # Save compressed image
                        output = io.BytesIO()
                        save_kwargs = {"format": output_format}

                        if compression_method in ["Quality Reduction", "Resize + Quality"] and output_format == "JPEG":
                            save_kwargs["quality"] = quality
                            save_kwargs["optimize"] = True
                        elif output_format == "PNG":
                            save_kwargs["optimize"] = True
                        elif output_format == "WEBP":
                            save_kwargs["quality"] = quality if compression_method in ["Quality Reduction",
                                                                                       "Resize + Quality"] else 80
                            save_kwargs["optimize"] = True

                        image.save(output, **save_kwargs)
                        compressed_data = output.getvalue()
                        total_compressed_size += len(compressed_data)

                        # Generate filename
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        extension = output_format.lower() if target_format != "Keep Original" else \
                            uploaded_file.name.rsplit('.', 1)[1]
                        new_filename = f"{base_name}_compressed.{extension}"
                        compressed_files[new_filename] = compressed_data

                        progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error compressing {uploaded_file.name}: {str(e)}")

            if compressed_files:
                # Show compression statistics
                compression_ratio = (total_original_size - total_compressed_size) / total_original_size * 100
                st.success(f"Compression complete! Reduced size by {compression_ratio:.1f}%")
                st.write(f"Original total size: {total_original_size:,} bytes")
                st.write(f"Compressed total size: {total_compressed_size:,} bytes")

                if len(compressed_files) == 1:
                    filename, data = next(iter(compressed_files.items()))
                    FileHandler.create_download_link(data, filename, "image/jpeg")
                else:
                    zip_data = FileHandler.create_zip_archive(compressed_files)
                    FileHandler.create_download_link(zip_data, "compressed_images.zip", "application/zip")


def watermark_tool():
    """Add watermarks to images"""
    create_tool_header("Watermark Tool", "Add text or image watermarks", "💧")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        watermark_type = st.selectbox("Watermark Type", ["Text", "Image"])

        if watermark_type == "Text":
            watermark_text = st.text_input("Watermark Text", "© Your Name")
            font_size = st.slider("Font Size", 10, 200, 36)
            opacity = st.slider("Opacity", 10, 100, 50)
            color = st.color_picker("Text Color", "#FFFFFF")
        else:
            watermark_image = FileHandler.upload_files(['png'], accept_multiple=False)
            if watermark_image:
                opacity = st.slider("Opacity", 10, 100, 50)
                scale = st.slider("Scale", 10, 100, 20)

        position = st.selectbox("Position", ["Bottom Right", "Bottom Left", "Top Right", "Top Left", "Center"])
        margin = st.slider("Margin", 0, 100, 20)

        if st.button("Add Watermark"):
            watermarked_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        # Convert to RGBA for transparency support
                        if image.mode != 'RGBA':
                            image = image.convert('RGBA')

                        # Create watermark overlay
                        overlay = Image.new('RGBA', image.size, (0, 0, 0, 0))
                        draw = ImageDraw.Draw(overlay)

                        if watermark_type == "Text":
                            # Calculate text size and position
                            try:
                                font = ImageFont.truetype("arial.ttf", font_size)
                            except:
                                font = ImageFont.load_default()

                            bbox = draw.textbbox((0, 0), watermark_text, font=font)
                            text_width = bbox[2] - bbox[0]
                            text_height = bbox[3] - bbox[1]

                            # Calculate position
                            x, y = calculate_position(position, image.size, (text_width, text_height), margin)

                            # Convert color and add opacity
                            hex_color = color.lstrip('#')
                            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
                            rgba_color = rgb_color + (int(255 * opacity / 100),)

                            draw.text((x, y), watermark_text, font=font, fill=rgba_color)

                        else:  # Image watermark
                            if watermark_image:
                                wm_img = FileHandler.process_image_file(watermark_image[0])
                                if wm_img:
                                    # Scale watermark
                                    wm_width = int(wm_img.width * scale / 100)
                                    wm_height = int(wm_img.height * scale / 100)
                                    wm_img = wm_img.resize((wm_width, wm_height), Image.Resampling.LANCZOS)

                                    # Ensure RGBA mode
                                    if wm_img.mode != 'RGBA':
                                        wm_img = wm_img.convert('RGBA')

                                    # Apply opacity
                                    alpha = wm_img.split()[-1]
                                    alpha = alpha.point(lambda p: int(p * opacity / 100))
                                    wm_img.putalpha(alpha)

                                    # Calculate position
                                    x, y = calculate_position(position, image.size, wm_img.size, margin)

                                    overlay.paste(wm_img, (x, y), wm_img)

                        # Composite the watermark
                        watermarked = Image.alpha_composite(image, overlay)

                        # Convert back to original mode if needed
                        if uploaded_file.name.lower().endswith(('.jpg', '.jpeg')):
                            watermarked = watermarked.convert('RGB')

                        # Save watermarked image
                        output = io.BytesIO()
                        format_name = "JPEG" if uploaded_file.name.lower().endswith(('.jpg', '.jpeg')) else "PNG"
                        watermarked.save(output, format=format_name)

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        extension = uploaded_file.name.rsplit('.', 1)[1]
                        new_filename = f"{base_name}_watermarked.{extension}"
                        watermarked_files[new_filename] = output.getvalue()

                        progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error adding watermark to {uploaded_file.name}: {str(e)}")

            if watermarked_files:
                if len(watermarked_files) == 1:
                    filename, data = next(iter(watermarked_files.items()))
                    FileHandler.create_download_link(data, filename, "image/png")
                else:
                    zip_data = FileHandler.create_zip_archive(watermarked_files)
                    FileHandler.create_download_link(zip_data, "watermarked_images.zip", "application/zip")

                st.success(f"Added watermark to {len(watermarked_files)} image(s)")


def calculate_position(position, image_size, element_size, margin):
    """Calculate position for watermark or overlay"""
    img_width, img_height = image_size
    elem_width, elem_height = element_size

    if position == "Bottom Right":
        x = img_width - elem_width - margin
        y = img_height - elem_height - margin
    elif position == "Bottom Left":
        x = margin
        y = img_height - elem_height - margin
    elif position == "Top Right":
        x = img_width - elem_width - margin
        y = margin
    elif position == "Top Left":
        x = margin
        y = margin
    else:  # Center
        x = (img_width - elem_width) // 2
        y = (img_height - elem_height) // 2

    return max(0, x), max(0, y)


def batch_converter():
    """Batch process multiple images"""
    create_tool_header("Batch Converter", "Process multiple images at once", "⚡")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        st.subheader("Batch Operations")

        operations = st.multiselect("Select Operations", [
            "Format Conversion", "Resize", "Quality Adjustment", "Add Border", "Apply Filter"
        ])

        settings = {}

        if "Format Conversion" in operations:
            settings['target_format'] = st.selectbox("Target Format", ["PNG", "JPEG", "WEBP", "GIF"])

        if "Resize" in operations:
            col1, col2 = st.columns(2)
            with col1:
                settings['resize_width'] = st.number_input("Width", min_value=1, value=800)
            with col2:
                settings['resize_height'] = st.number_input("Height", min_value=1, value=600)
            settings['maintain_aspect'] = st.checkbox("Maintain Aspect Ratio", True)

        if "Quality Adjustment" in operations:
            settings['quality'] = st.slider("Quality", 1, 100, 85)

        if "Add Border" in operations:
            settings['border_width'] = st.slider("Border Width", 1, 50, 10)
            settings['border_color'] = st.color_picker("Border Color", "#000000")

        if "Apply Filter" in operations:
            settings['filter_type'] = st.selectbox("Filter Type", ["Blur", "Sharpen", "Enhance", "Grayscale"])

        if st.button("Process All Images"):
            processed_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        processed_image = image.copy()

                        # Apply operations in sequence
                        for operation in operations:
                            if operation == "Resize":
                                if settings['maintain_aspect']:
                                    processed_image.thumbnail((settings['resize_width'], settings['resize_height']),
                                                              Image.Resampling.LANCZOS)
                                else:
                                    processed_image = processed_image.resize(
                                        (settings['resize_width'], settings['resize_height']), Image.Resampling.LANCZOS)

                            elif operation == "Add Border":
                                hex_color = settings['border_color'].lstrip('#')
                                border_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
                                processed_image = ImageOps.expand(processed_image, border=settings['border_width'],
                                                                  fill=border_color)

                            elif operation == "Apply Filter":
                                filter_type = settings['filter_type']
                                if filter_type == "Blur":
                                    processed_image = processed_image.filter(ImageFilter.BLUR)
                                elif filter_type == "Sharpen":
                                    processed_image = processed_image.filter(ImageFilter.SHARPEN)
                                elif filter_type == "Enhance":
                                    enhancer = ImageEnhance.Sharpness(processed_image)
                                    processed_image = enhancer.enhance(1.5)
                                elif filter_type == "Grayscale":
                                    processed_image = processed_image.convert('L').convert('RGB')

                        # Handle format conversion
                        output_format = settings.get('target_format', image.format if image.format else "PNG")

                        if output_format == "JPEG" and processed_image.mode in ("RGBA", "P"):
                            rgb_image = Image.new("RGB", processed_image.size, (255, 255, 255))
                            rgb_image.paste(processed_image, mask=processed_image.split()[
                                -1] if processed_image.mode == "RGBA" else None)
                            processed_image = rgb_image

                        # Save processed image
                        output = io.BytesIO()
                        save_kwargs = {"format": output_format}

                        if "Quality Adjustment" in operations and output_format in ["JPEG", "WEBP"]:
                            save_kwargs["quality"] = settings['quality']

                        processed_image.save(output, **save_kwargs)

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        extension = output_format.lower()
                        new_filename = f"{base_name}_processed.{extension}"
                        processed_files[new_filename] = output.getvalue()

                        progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error processing {uploaded_file.name}: {str(e)}")

            if processed_files:
                zip_data = FileHandler.create_zip_archive(processed_files)
                FileHandler.create_download_link(zip_data, "batch_processed_images.zip", "application/zip")
                st.success(f"Processed {len(processed_files)} image(s)")


def brightness_contrast():
    """Adjust brightness and contrast"""
    create_tool_header("Brightness/Contrast", "Adjust image brightness and contrast", "☀️")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Adjustment controls
            brightness = st.slider("Brightness", 0.1, 3.0, 1.0, 0.1)
            contrast = st.slider("Contrast", 0.1, 3.0, 1.0, 0.1)

            # Apply adjustments in real-time
            enhancer_brightness = ImageEnhance.Brightness(image)
            temp_image = enhancer_brightness.enhance(brightness)

            enhancer_contrast = ImageEnhance.Contrast(temp_image)
            adjusted_image = enhancer_contrast.enhance(contrast)

            with col2:
                st.subheader("Adjusted Image")
                st.image(adjusted_image, use_column_width=True)

            if st.button("Download Adjusted Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                adjusted_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_adjusted.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def rotate_flip():
    """Rotate and flip images"""
    create_tool_header("Rotate & Flip", "Rotate and flip images with various options", "🔄")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Rotation and flip controls
            st.subheader("Transform Options")

            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**Rotation**")
                rotation_angle = st.selectbox("Rotation Angle", [0, 90, 180, 270])
                custom_angle = st.slider("Custom Angle (degrees)", -180, 180, 0, 1)

            with col_b:
                st.write("**Flip Options**")
                flip_horizontal = st.checkbox("Flip Horizontal")
                flip_vertical = st.checkbox("Flip Vertical")

            # Preview transformation
            transformed_image = image.copy()

            # Apply rotation
            total_rotation = rotation_angle + custom_angle
            if total_rotation != 0:
                # Normalize angle to 0-360 range
                total_rotation = total_rotation % 360

                if total_rotation == 90:
                    transformed_image = transformed_image.transpose(Image.Transpose.ROTATE_90)
                elif total_rotation == 180:
                    transformed_image = transformed_image.transpose(Image.Transpose.ROTATE_180)
                elif total_rotation == 270:
                    transformed_image = transformed_image.transpose(Image.Transpose.ROTATE_270)
                else:
                    # For custom angles, use rotate with expand=True to avoid cropping
                    transformed_image = transformed_image.rotate(-total_rotation, expand=True, fillcolor='white')

            # Apply flips
            if flip_horizontal:
                transformed_image = transformed_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

            if flip_vertical:
                transformed_image = transformed_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

            with col2:
                st.subheader("Transformed Image")
                st.image(transformed_image, use_column_width=True)

            # Show transformation info
            original_size = f"{image.width} × {image.height}"
            new_size = f"{transformed_image.width} × {transformed_image.height}"

            col_info1, col_info2 = st.columns(2)
            with col_info1:
                st.metric("Original Size", original_size)
            with col_info2:
                st.metric("New Size", new_size)

            if st.button("Download Transformed Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                transformed_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_transformed.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def shape_drawer():
    """Draw shapes on images"""
    create_tool_header("Shape Drawer", "Draw shapes and geometric elements on images", "🟢")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Shape drawing controls
            st.subheader("Shape Options")

            col_a, col_b = st.columns(2)
            with col_a:
                shape_type = st.selectbox("Shape Type", ["Rectangle", "Circle", "Line", "Arrow", "Polygon"])
                fill_shape = st.checkbox("Fill Shape", False)

            with col_b:
                shape_color = st.color_picker("Shape Color", "#FF0000")
                line_width = st.slider("Line Width", 1, 20, 3)

            # Position controls
            st.subheader("Position & Size")
            width, height = image.size

            if shape_type in ["Rectangle", "Circle"]:
                col_pos1, col_pos2, col_pos3, col_pos4 = st.columns(4)
                with col_pos1:
                    x1 = st.slider("X1", 0, width, width // 4)
                with col_pos2:
                    y1 = st.slider("Y1", 0, height, height // 4)
                with col_pos3:
                    x2 = st.slider("X2", x1, width, 3 * width // 4)
                with col_pos4:
                    y2 = st.slider("Y2", y1, height, 3 * height // 4)

            elif shape_type in ["Line", "Arrow"]:
                col_pos1, col_pos2, col_pos3, col_pos4 = st.columns(4)
                with col_pos1:
                    x1 = st.slider("Start X", 0, width, width // 4)
                with col_pos2:
                    y1 = st.slider("Start Y", 0, height, height // 2)
                with col_pos3:
                    x2 = st.slider("End X", 0, width, 3 * width // 4)
                with col_pos4:
                    y2 = st.slider("End Y", 0, height, height // 2)

            # Create shape on image
            result_image = image.copy()
            draw = ImageDraw.Draw(result_image)

            # Convert color
            hex_color = shape_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

            if shape_type == "Rectangle":
                if fill_shape:
                    draw.rectangle([x1, y1, x2, y2], fill=rgb_color, outline=rgb_color, width=line_width)
                else:
                    draw.rectangle([x1, y1, x2, y2], outline=rgb_color, width=line_width)

            elif shape_type == "Circle":
                if fill_shape:
                    draw.ellipse([x1, y1, x2, y2], fill=rgb_color, outline=rgb_color, width=line_width)
                else:
                    draw.ellipse([x1, y1, x2, y2], outline=rgb_color, width=line_width)

            elif shape_type == "Line":
                draw.line([x1, y1, x2, y2], fill=rgb_color, width=line_width)

            elif shape_type == "Arrow":
                # Draw line
                draw.line([x1, y1, x2, y2], fill=rgb_color, width=line_width)
                # Draw arrowhead
                import math
                angle = math.atan2(y2 - y1, x2 - x1)
                arrow_length = 15
                arrow_angle = math.pi / 6

                # Calculate arrowhead points
                ax1 = x2 - arrow_length * math.cos(angle - arrow_angle)
                ay1 = y2 - arrow_length * math.sin(angle - arrow_angle)
                ax2 = x2 - arrow_length * math.cos(angle + arrow_angle)
                ay2 = y2 - arrow_length * math.sin(angle + arrow_angle)

                draw.polygon([(x2, y2), (ax1, ay1), (ax2, ay2)], fill=rgb_color)

            with col2:
                st.subheader("Image with Shape")
                st.image(result_image, use_column_width=True)

            if st.button("Download Image with Shape"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                result_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_with_shape.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def text_annotations():
    """Add text annotations to images"""
    create_tool_header("Text Annotations", "Add text annotations and labels to images", "📝")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Text annotation controls
            st.subheader("Text Annotation Options")

            annotation_text = st.text_area("Annotation Text", "Sample annotation text")

            col_a, col_b = st.columns(2)
            with col_a:
                font_size = st.slider("Font Size", 12, 100, 24)
                text_color = st.color_picker("Text Color", "#000000")

            with col_b:
                background_enabled = st.checkbox("Text Background", True)
                background_color = st.color_picker("Background Color", "#FFFFFF")
                background_opacity = st.slider("Background Opacity", 0, 100, 80)

            # Position controls
            st.subheader("Position")
            width, height = image.size

            col_pos1, col_pos2 = st.columns(2)
            with col_pos1:
                text_x = st.slider("X Position", 0, width, width // 4)
            with col_pos2:
                text_y = st.slider("Y Position", 0, height, height // 4)

            # Create annotated image
            result_image = image.copy().convert('RGBA')

            # Create overlay for text
            overlay = Image.new('RGBA', result_image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)

            # Try to use a font, fallback to default
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()

            # Get text dimensions
            bbox = draw.textbbox((0, 0), annotation_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Convert colors
            def hex_to_rgba(hex_color, opacity=100):
                hex_color = hex_color.lstrip('#')
                rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
                return rgb + (int(255 * opacity / 100),)

            text_rgba = hex_to_rgba(text_color, 100)
            bg_rgba = hex_to_rgba(background_color, background_opacity)

            # Draw background if enabled
            if background_enabled:
                padding = 5
                bg_coords = [
                    text_x - padding,
                    text_y - padding,
                    text_x + text_width + padding,
                    text_y + text_height + padding
                ]
                draw.rectangle(bg_coords, fill=bg_rgba)

            # Draw text
            draw.text((text_x, text_y), annotation_text, font=font, fill=text_rgba)

            # Composite the overlay
            result_image = Image.alpha_composite(result_image, overlay)
            result_image = result_image.convert('RGB')

            with col2:
                st.subheader("Annotated Image")
                st.image(result_image, use_column_width=True)

            if st.button("Download Annotated Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                result_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_annotated.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def highlighting_tool():
    """Highlight areas of images"""
    create_tool_header("Highlighting Tool", "Highlight important areas in images", "🟡")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Highlighting controls
            st.subheader("Highlight Options")

            col_a, col_b = st.columns(2)
            with col_a:
                highlight_type = st.selectbox("Highlight Type", ["Rectangle", "Circle", "Free Form"])
                highlight_color = st.color_picker("Highlight Color", "#FFFF00")

            with col_b:
                opacity = st.slider("Highlight Opacity", 10, 90, 50)
                border_width = st.slider("Border Width", 0, 10, 2)

            # Position controls
            st.subheader("Highlight Area")
            width, height = image.size

            col_pos1, col_pos2, col_pos3, col_pos4 = st.columns(4)
            with col_pos1:
                x1 = st.slider("Left", 0, width, width // 4)
            with col_pos2:
                y1 = st.slider("Top", 0, height, height // 4)
            with col_pos3:
                x2 = st.slider("Right", x1, width, 3 * width // 4)
            with col_pos4:
                y2 = st.slider("Bottom", y1, height, 3 * height // 4)

            # Create highlighted image
            result_image = image.copy().convert('RGBA')

            # Create highlight overlay
            overlay = Image.new('RGBA', result_image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)

            # Convert color
            hex_color = highlight_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
            highlight_rgba = rgb_color + (int(255 * opacity / 100),)
            border_rgba = rgb_color + (255,)

            if highlight_type == "Rectangle":
                # Fill highlight area
                draw.rectangle([x1, y1, x2, y2], fill=highlight_rgba)
                # Draw border if specified
                if border_width > 0:
                    draw.rectangle([x1, y1, x2, y2], outline=border_rgba, width=border_width)

            elif highlight_type == "Circle":
                # Fill highlight area
                draw.ellipse([x1, y1, x2, y2], fill=highlight_rgba)
                # Draw border if specified
                if border_width > 0:
                    draw.ellipse([x1, y1, x2, y2], outline=border_rgba, width=border_width)

            # Composite the highlight
            result_image = Image.alpha_composite(result_image, overlay)
            result_image = result_image.convert('RGB')

            with col2:
                st.subheader("Highlighted Image")
                st.image(result_image, use_column_width=True)

            if st.button("Download Highlighted Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                result_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_highlighted.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def redaction_tool():
    """Redact sensitive areas in images"""
    create_tool_header("Redaction Tool", "Redact or censor sensitive information", "⬛")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Redaction controls
            st.subheader("Redaction Options")

            col_a, col_b = st.columns(2)
            with col_a:
                redaction_type = st.selectbox("Redaction Type", ["Black Bar", "Blur", "Pixelate", "Custom Color"])

            with col_b:
                if redaction_type == "Custom Color":
                    redaction_color = st.color_picker("Redaction Color", "#000000")
                elif redaction_type in ["Blur", "Pixelate"]:
                    blur_intensity = st.slider("Blur/Pixelate Intensity", 1, 20, 10)

            # Position controls
            st.subheader("Redaction Area")
            width, height = image.size

            # Allow multiple redaction areas
            num_areas = st.number_input("Number of Redaction Areas", 1, 5, 1)

            redaction_areas = []
            for i in range(num_areas):
                st.write(f"**Redaction Area {i + 1}**")
                col_pos1, col_pos2, col_pos3, col_pos4 = st.columns(4)
                with col_pos1:
                    x1 = st.slider(f"Left {i + 1}", 0, width, width // 4, key=f"x1_{i}")
                with col_pos2:
                    y1 = st.slider(f"Top {i + 1}", 0, height, height // 4 + i * 50, key=f"y1_{i}")
                with col_pos3:
                    x2 = st.slider(f"Right {i + 1}", x1, width, 3 * width // 4, key=f"x2_{i}")
                with col_pos4:
                    y2 = st.slider(f"Bottom {i + 1}", y1, height, 3 * height // 4 + i * 50, key=f"y2_{i}")

                redaction_areas.append((x1, y1, x2, y2))

            # Create redacted image
            result_image = image.copy()

            for x1, y1, x2, y2 in redaction_areas:
                if redaction_type == "Black Bar":
                    draw = ImageDraw.Draw(result_image)
                    draw.rectangle([x1, y1, x2, y2], fill=(0, 0, 0))

                elif redaction_type == "Custom Color":
                    hex_color = redaction_color.lstrip('#')
                    rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
                    draw = ImageDraw.Draw(result_image)
                    draw.rectangle([x1, y1, x2, y2], fill=rgb_color)

                elif redaction_type == "Blur":
                    # Extract area, blur it, and paste back
                    area = result_image.crop((x1, y1, x2, y2))
                    blurred_area = area.filter(ImageFilter.GaussianBlur(radius=blur_intensity))
                    result_image.paste(blurred_area, (x1, y1))

                elif redaction_type == "Pixelate":
                    # Extract area, pixelate it, and paste back
                    area = result_image.crop((x1, y1, x2, y2))
                    area_width, area_height = area.size

                    # Resize down and up to create pixelation
                    pixel_size = max(1, min(area_width, area_height) // blur_intensity)
                    small_area = area.resize((pixel_size, pixel_size), Image.Resampling.NEAREST)
                    pixelated_area = small_area.resize((area_width, area_height), Image.Resampling.NEAREST)
                    result_image.paste(pixelated_area, (x1, y1))

            with col2:
                st.subheader("Redacted Image")
                st.image(result_image, use_column_width=True)

            if st.button("Download Redacted Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                result_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_redacted.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def markup_tool():
    """General markup and annotation tool"""
    create_tool_header("Markup Tool", "Add various markup elements to images", "✏️")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Markup controls
            st.subheader("Markup Options")

            markup_type = st.selectbox("Markup Type",
                                       ["Text Label", "Callout Box", "Border Frame", "Stamp", "Badge"])

            col_a, col_b = st.columns(2)
            with col_a:
                markup_color = st.color_picker("Markup Color", "#FF0000")
                if markup_type in ["Text Label", "Callout Box", "Stamp", "Badge"]:
                    markup_text = st.text_input("Markup Text", "IMPORTANT")

            with col_b:
                opacity = st.slider("Opacity", 10, 100, 80)
                if markup_type in ["Text Label", "Callout Box", "Stamp", "Badge"]:
                    font_size = st.slider("Font Size", 12, 72, 24)

            # Position controls based on markup type
            width, height = image.size

            if markup_type in ["Text Label", "Stamp", "Badge"]:
                position = st.selectbox("Position",
                                        ["Top Left", "Top Right", "Bottom Left", "Bottom Right", "Center", "Custom"])

                if position == "Custom":
                    col_pos1, col_pos2 = st.columns(2)
                    with col_pos1:
                        custom_x = st.slider("X Position", 0, width, width // 2)
                    with col_pos2:
                        custom_y = st.slider("Y Position", 0, height, height // 2)

            elif markup_type in ["Callout Box", "Border Frame"]:
                col_pos1, col_pos2, col_pos3, col_pos4 = st.columns(4)
                with col_pos1:
                    x1 = st.slider("Left", 0, width, width // 4)
                with col_pos2:
                    y1 = st.slider("Top", 0, height, height // 4)
                with col_pos3:
                    x2 = st.slider("Right", x1, width, 3 * width // 4)
                with col_pos4:
                    y2 = st.slider("Bottom", y1, height, 3 * height // 4)

            # Create markup on image
            result_image = image.copy().convert('RGBA')
            overlay = Image.new('RGBA', result_image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)

            # Convert color
            hex_color = markup_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
            markup_rgba = rgb_color + (int(255 * opacity / 100),)

            # Try to use a font, fallback to default
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()

            if markup_type == "Text Label":
                # Calculate position
                if position == "Custom":
                    text_x, text_y = custom_x, custom_y
                else:
                    bbox = draw.textbbox((0, 0), markup_text, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    if position == "Top Left":
                        text_x, text_y = 10, 10
                    elif position == "Top Right":
                        text_x, text_y = width - text_width - 10, 10
                    elif position == "Bottom Left":
                        text_x, text_y = 10, height - text_height - 10
                    elif position == "Bottom Right":
                        text_x, text_y = width - text_width - 10, height - text_height - 10
                    else:  # Center
                        text_x, text_y = (width - text_width) // 2, (height - text_height) // 2

                draw.text((text_x, text_y), markup_text, font=font, fill=markup_rgba)

            elif markup_type == "Callout Box":
                # Draw callout box background
                draw.rectangle([x1, y1, x2, y2], fill=markup_rgba, outline=rgb_color + (255,), width=2)
                # Add text inside
                bbox = draw.textbbox((0, 0), markup_text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                text_x = x1 + (x2 - x1 - text_width) // 2
                text_y = y1 + (y2 - y1 - text_height) // 2
                draw.text((text_x, text_y), markup_text, font=font, fill=(255, 255, 255, 255))

            elif markup_type == "Border Frame":
                # Draw border frame
                border_width = 5
                draw.rectangle([x1, y1, x2, y2], outline=markup_rgba, width=border_width)

            elif markup_type == "Stamp":
                # Create stamp effect
                if position == "Custom":
                    stamp_x, stamp_y = custom_x, custom_y
                else:
                    bbox = draw.textbbox((0, 0), markup_text, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    if position == "Top Left":
                        stamp_x, stamp_y = 20, 20
                    elif position == "Top Right":
                        stamp_x, stamp_y = width - text_width - 20, 20
                    elif position == "Bottom Left":
                        stamp_x, stamp_y = 20, height - text_height - 20
                    elif position == "Bottom Right":
                        stamp_x, stamp_y = width - text_width - 20, height - text_height - 20
                    else:  # Center
                        stamp_x, stamp_y = (width - text_width) // 2, (height - text_height) // 2

                # Draw stamp background and border
                padding = 10
                bbox = draw.textbbox((0, 0), markup_text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]

                stamp_rect = [stamp_x - padding, stamp_y - padding,
                              stamp_x + text_width + padding, stamp_y + text_height + padding]
                draw.rectangle(stamp_rect, outline=markup_rgba, width=3)
                draw.text((stamp_x, stamp_y), markup_text, font=font, fill=markup_rgba)

            elif markup_type == "Badge":
                # Create badge effect
                if position == "Custom":
                    badge_x, badge_y = custom_x, custom_y
                else:
                    bbox = draw.textbbox((0, 0), markup_text, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    if position == "Top Left":
                        badge_x, badge_y = 10, 10
                    elif position == "Top Right":
                        badge_x, badge_y = width - text_width - 20, 10
                    elif position == "Bottom Left":
                        badge_x, badge_y = 10, height - text_height - 20
                    elif position == "Bottom Right":
                        badge_x, badge_y = width - text_width - 20, height - text_height - 20
                    else:  # Center
                        badge_x, badge_y = (width - text_width) // 2, (height - text_height) // 2

                # Draw badge background
                padding = 8
                bbox = draw.textbbox((0, 0), markup_text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]

                badge_rect = [badge_x - padding, badge_y - padding,
                              badge_x + text_width + padding, badge_y + text_height + padding]
                draw.rounded_rectangle(badge_rect, radius=5, fill=markup_rgba)
                draw.text((badge_x, badge_y), markup_text, font=font, fill=(255, 255, 255, 255))

            # Composite the markup
            result_image = Image.alpha_composite(result_image, overlay)
            result_image = result_image.convert('RGB')

            with col2:
                st.subheader("Marked Up Image")
                st.image(result_image, use_column_width=True)

            if st.button("Download Marked Up Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                result_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_markup.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def color_adjustment():
    """Comprehensive color adjustment tool"""
    create_tool_header("Color Adjustment", "Adjust saturation, hue, and color balance", "🎨")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Color adjustment controls
            st.subheader("Color Adjustments")

            col_a, col_b = st.columns(2)
            with col_a:
                saturation = st.slider("Saturation", 0.0, 3.0, 1.0, 0.1)
                hue_shift = st.slider("Hue Shift", -180, 180, 0, 5)

            with col_b:
                vibrance = st.slider("Vibrance", 0.0, 2.0, 1.0, 0.1)
                warmth = st.slider("Temperature", -50, 50, 0, 5)

            # Apply color adjustments
            if image.mode != 'RGB':
                rgb_image = image.convert('RGB')
            else:
                rgb_image = image.copy()

            # Convert to numpy array for processing
            img_array = np.array(rgb_image, dtype=np.float32) / 255.0

            # Apply saturation adjustment
            if saturation != 1.0:
                enhancer = ImageEnhance.Color(rgb_image)
                rgb_image = enhancer.enhance(saturation)
                img_array = np.array(rgb_image, dtype=np.float32) / 255.0

            # Apply hue shift
            if hue_shift != 0:
                hsv_array = np.array([colorsys.rgb_to_hsv(r, g, b) for r, g, b in img_array.reshape(-1, 3)])
                hsv_array[:, 0] = (hsv_array[:, 0] + hue_shift / 360.0) % 1.0
                rgb_array = np.array([colorsys.hsv_to_rgb(h, s, v) for h, s, v in hsv_array])
                img_array = rgb_array.reshape(img_array.shape)

            # Apply vibrance (selective saturation)
            if vibrance != 1.0:
                hsv_array = np.array([colorsys.rgb_to_hsv(r, g, b) for r, g, b in img_array.reshape(-1, 3)])
                # Vibrance affects less saturated colors more
                saturation_mask = 1.0 - hsv_array[:, 1]
                hsv_array[:, 1] = hsv_array[:, 1] * (1.0 + (vibrance - 1.0) * saturation_mask)
                hsv_array[:, 1] = np.clip(hsv_array[:, 1], 0, 1)
                rgb_array = np.array([colorsys.hsv_to_rgb(h, s, v) for h, s, v in hsv_array])
                img_array = rgb_array.reshape(img_array.shape)

            # Apply temperature adjustment
            if warmth != 0:
                if warmth > 0:  # Warmer
                    img_array[:, :, 0] *= (1.0 + warmth * 0.01)  # More red
                    img_array[:, :, 2] *= (1.0 - warmth * 0.005)  # Less blue
                else:  # Cooler
                    img_array[:, :, 0] *= (1.0 + warmth * 0.005)  # Less red
                    img_array[:, :, 2] *= (1.0 - warmth * 0.01)  # More blue

            # Convert back to PIL Image
            img_array = np.clip(img_array * 255, 0, 255).astype(np.uint8)
            adjusted_image = Image.fromarray(img_array)

            with col2:
                st.subheader("Adjusted Image")
                st.image(adjusted_image, use_column_width=True)

            if st.button("Download Adjusted Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                adjusted_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_color_adjusted.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def color_balance():
    """Adjust color balance for shadows, midtones, and highlights"""
    create_tool_header("Color Balance", "Adjust RGB balance for shadows/midtones/highlights", "⚖️")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Color balance controls
            st.subheader("Color Balance Controls")

            tone_range = st.selectbox("Tone Range", ["Shadows", "Midtones", "Highlights"])

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                red_cyan = st.slider("Red ↔ Cyan", -100, 100, 0, 5)
            with col_b:
                green_magenta = st.slider("Green ↔ Magenta", -100, 100, 0, 5)
            with col_c:
                blue_yellow = st.slider("Blue ↔ Yellow", -100, 100, 0, 5)

            preserve_luminosity = st.checkbox("Preserve Luminosity", True)

            # Apply color balance
            if image.mode != 'RGB':
                rgb_image = image.convert('RGB')
            else:
                rgb_image = image.copy()

            # Convert to numpy array
            img_array = np.array(rgb_image, dtype=np.float32) / 255.0

            if red_cyan != 0 or green_magenta != 0 or blue_yellow != 0:
                # Create tone mask based on luminosity
                luminosity = 0.299 * img_array[:, :, 0] + 0.587 * img_array[:, :, 1] + 0.114 * img_array[:, :, 2]

                if tone_range == "Shadows":
                    mask = np.exp(-4 * luminosity * luminosity)
                elif tone_range == "Highlights":
                    mask = np.exp(-4 * (1 - luminosity) * (1 - luminosity))
                else:  # Midtones
                    mask = np.exp(-4 * (luminosity - 0.5) * (luminosity - 0.5))

                # Normalize mask
                mask = mask / np.max(mask)

                # Apply color adjustments
                if red_cyan != 0:
                    if red_cyan > 0:  # More red
                        img_array[:, :, 0] += (red_cyan / 100.0) * 0.3 * mask
                        img_array[:, :, 1] -= (red_cyan / 100.0) * 0.1 * mask
                        img_array[:, :, 2] -= (red_cyan / 100.0) * 0.1 * mask
                    else:  # More cyan
                        img_array[:, :, 0] += (red_cyan / 100.0) * 0.3 * mask
                        img_array[:, :, 1] -= (red_cyan / 100.0) * 0.15 * mask
                        img_array[:, :, 2] -= (red_cyan / 100.0) * 0.15 * mask

                if green_magenta != 0:
                    if green_magenta > 0:  # More green
                        img_array[:, :, 1] += (green_magenta / 100.0) * 0.3 * mask
                        img_array[:, :, 0] -= (green_magenta / 100.0) * 0.15 * mask
                        img_array[:, :, 2] -= (green_magenta / 100.0) * 0.15 * mask
                    else:  # More magenta
                        img_array[:, :, 0] -= (green_magenta / 100.0) * 0.15 * mask
                        img_array[:, :, 1] += (green_magenta / 100.0) * 0.3 * mask
                        img_array[:, :, 2] -= (green_magenta / 100.0) * 0.15 * mask

                if blue_yellow != 0:
                    if blue_yellow > 0:  # More blue
                        img_array[:, :, 2] += (blue_yellow / 100.0) * 0.3 * mask
                        img_array[:, :, 0] -= (blue_yellow / 100.0) * 0.15 * mask
                        img_array[:, :, 1] -= (blue_yellow / 100.0) * 0.15 * mask
                    else:  # More yellow
                        img_array[:, :, 0] -= (blue_yellow / 100.0) * 0.1 * mask
                        img_array[:, :, 1] -= (blue_yellow / 100.0) * 0.1 * mask
                        img_array[:, :, 2] += (blue_yellow / 100.0) * 0.3 * mask

            # Convert back to PIL Image
            img_array = np.clip(img_array * 255, 0, 255).astype(np.uint8)
            adjusted_image = Image.fromarray(img_array)

            with col2:
                st.subheader("Color Balanced Image")
                st.image(adjusted_image, use_column_width=True)

            if st.button("Download Color Balanced Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                adjusted_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_color_balanced.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def hue_adjuster():
    """Selective hue adjustment tool"""
    create_tool_header("Hue Adjuster", "Adjust specific color ranges independently", "🌈")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Hue adjustment controls
            st.subheader("Selective Hue Adjustments")

            target_color = st.selectbox("Target Color Range",
                                        ["Reds", "Oranges", "Yellows", "Greens", "Cyans", "Blues", "Magentas"])

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                hue_shift = st.slider("Hue Shift", -180, 180, 0, 5)
            with col_b:
                saturation_adj = st.slider("Saturation", -100, 100, 0, 5)
            with col_c:
                lightness_adj = st.slider("Lightness", -100, 100, 0, 5)

            # Apply selective hue adjustment
            if image.mode != 'RGB':
                rgb_image = image.convert('RGB')
            else:
                rgb_image = image.copy()

            # Convert to numpy array and HSV
            img_array = np.array(rgb_image, dtype=np.float32) / 255.0
            hsv_array = np.array([colorsys.rgb_to_hsv(r, g, b) for r, g, b in img_array.reshape(-1, 3)])
            hsv_array = hsv_array.reshape(img_array.shape)

            # Define color ranges in HSV
            color_ranges = {
                "Reds": (0.0, 0.08, 0.92, 1.0),  # 0-30° and 330-360°
                "Oranges": (0.08, 0.17, 0, 0),  # 30-60°
                "Yellows": (0.17, 0.25, 0, 0),  # 60-90°
                "Greens": (0.25, 0.42, 0, 0),  # 90-150°
                "Cyans": (0.42, 0.58, 0, 0),  # 150-210°
                "Blues": (0.58, 0.75, 0, 0),  # 210-270°
                "Magentas": (0.75, 0.92, 0, 0)  # 270-330°
            }

            if hue_shift != 0 or saturation_adj != 0 or lightness_adj != 0:
                h_min, h_max, h_min2, h_max2 = color_ranges[target_color]

                # Create mask for target color range
                if target_color == "Reds":  # Reds wrap around
                    mask = ((hsv_array[:, :, 0] >= h_min) & (hsv_array[:, :, 0] <= h_max)) | \
                           ((hsv_array[:, :, 0] >= h_min2) & (hsv_array[:, :, 0] <= h_max2))
                else:
                    mask = (hsv_array[:, :, 0] >= h_min) & (hsv_array[:, :, 0] <= h_max)

                # Apply feathering to mask for smooth transitions
                mask_float = mask.astype(np.float32)
                kernel_size = max(3, int(2.0 * 2 + 1)) | 1  # Ensure odd kernel size
                mask_smooth = cv2.GaussianBlur(mask_float, (kernel_size, kernel_size), sigmaX=1.0)

                # Apply adjustments
                if hue_shift != 0:
                    hsv_array[:, :, 0] = hsv_array[:, :, 0] + (hue_shift / 360.0) * mask_smooth
                    hsv_array[:, :, 0] = hsv_array[:, :, 0] % 1.0

                if saturation_adj != 0:
                    sat_factor = 1.0 + (saturation_adj / 100.0)
                    hsv_array[:, :, 1] = hsv_array[:, :, 1] * (1.0 + (sat_factor - 1.0) * mask_smooth)
                    hsv_array[:, :, 1] = np.clip(hsv_array[:, :, 1], 0, 1)

                if lightness_adj != 0:
                    light_factor = 1.0 + (lightness_adj / 100.0)
                    hsv_array[:, :, 2] = hsv_array[:, :, 2] * (1.0 + (light_factor - 1.0) * mask_smooth)
                    hsv_array[:, :, 2] = np.clip(hsv_array[:, :, 2], 0, 1)

            # Convert back to RGB
            rgb_array = np.array([colorsys.hsv_to_rgb(h, s, v) for h, s, v in hsv_array.reshape(-1, 3)])
            img_array = rgb_array.reshape(img_array.shape)
            img_array = np.clip(img_array * 255, 0, 255).astype(np.uint8)
            adjusted_image = Image.fromarray(img_array)

            with col2:
                st.subheader("Hue Adjusted Image")
                st.image(adjusted_image, use_column_width=True)

            if st.button("Download Hue Adjusted Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                adjusted_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_hue_adjusted.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def color_replacer():
    """Replace specific colors in images"""
    create_tool_header("Color Replacer", "Replace specific colors with new ones", "🎯")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            # Color replacement controls
            st.subheader("Color Replacement")

            col_a, col_b = st.columns(2)
            with col_a:
                source_color = st.color_picker("Source Color to Replace", "#FF0000")
                tolerance = st.slider("Color Tolerance", 0, 100, 20, 1)
            with col_b:
                target_color = st.color_picker("Replacement Color", "#00FF00")
                feather = st.slider("Edge Feathering", 0, 10, 2, 1)

            # Apply color replacement
            if image.mode != 'RGB':
                rgb_image = image.convert('RGB')
            else:
                rgb_image = image.copy()

            # Convert color picker hex to RGB
            def hex_to_rgb(hex_color):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

            source_rgb = np.array(hex_to_rgb(source_color))
            target_rgb = np.array(hex_to_rgb(target_color))

            # Convert image to numpy array
            img_array = np.array(rgb_image, dtype=np.float32)

            # Calculate color distance
            color_diff = np.sqrt(np.sum((img_array - source_rgb) ** 2, axis=2))
            max_distance = tolerance * 255 / 100 * np.sqrt(3)  # Max possible distance

            # Create mask
            mask = color_diff <= max_distance

            if feather > 0:
                # Apply feathering
                distance_mask = 1.0 - (color_diff / max_distance)
                distance_mask = np.clip(distance_mask, 0, 1)

                # Smooth the mask
                kernel_size = max(3, int(feather * 2 + 1)) | 1  # Ensure odd kernel size
                smooth_mask = cv2.GaussianBlur(distance_mask.astype(np.float32),
                                               (kernel_size, kernel_size),
                                               sigmaX=feather / 3.0)
                smooth_mask = np.clip(smooth_mask, 0, 1)
            else:
                smooth_mask = mask.astype(float)

            # Apply color replacement
            result_image = img_array.copy()
            for channel in range(3):
                result_image[:, :, channel] = (img_array[:, :, channel] * (1 - smooth_mask) +
                                               target_rgb[channel] * smooth_mask)

            # Convert back to PIL Image
            result_image = np.clip(result_image, 0, 255).astype(np.uint8)
            replaced_image = Image.fromarray(result_image)

            with col2:
                st.subheader("Color Replaced Image")
                st.image(replaced_image, use_column_width=True)

            # Show replacement statistics
            replaced_pixels = np.sum(mask)
            total_pixels = mask.size
            replacement_percentage = (replaced_pixels / total_pixels) * 100
            st.write(f"Replaced {replaced_pixels:,} pixels ({replacement_percentage:.1f}% of image)")

            if st.button("Download Color Replaced Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                replaced_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_color_replaced.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def histogram_analyzer():
    """Analyze and display color histograms"""
    create_tool_header("Histogram Analyzer", "Analyze color distribution and histograms", "📊")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)

            # Convert to RGB if needed
            if image.mode != 'RGB':
                rgb_image = image.convert('RGB')
            else:
                rgb_image = image

            # Analysis options
            analysis_type = st.selectbox("Analysis Type",
                                         ["RGB Histograms", "HSV Histograms", "Luminosity", "Color Statistics"])

            if analysis_type == "RGB Histograms":
                # Create RGB histograms
                img_array = np.array(rgb_image)

                fig, axes = plt.subplots(2, 2, figsize=(12, 10))

                # Individual channel histograms
                colors = ['red', 'green', 'blue']
                for i, color in enumerate(colors):
                    axes[0, i].hist(img_array[:, :, i].flatten(), bins=256, color=color, alpha=0.7)
                    axes[0, i].set_title(f'{color.capitalize()} Channel')
                    axes[0, i].set_xlabel('Pixel Value')
                    axes[0, i].set_ylabel('Frequency')

                # Combined histogram
                axes[1, 0].hist(img_array[:, :, 0].flatten(), bins=256, color='red', alpha=0.5, label='Red')
                axes[1, 0].hist(img_array[:, :, 1].flatten(), bins=256, color='green', alpha=0.5, label='Green')
                axes[1, 0].hist(img_array[:, :, 2].flatten(), bins=256, color='blue', alpha=0.5, label='Blue')
                axes[1, 0].set_title('Combined RGB Histogram')
                axes[1, 0].set_xlabel('Pixel Value')
                axes[1, 0].set_ylabel('Frequency')
                axes[1, 0].legend()

                # Remove empty subplot
                fig.delaxes(axes[1, 1])

                plt.tight_layout()
                st.pyplot(fig)
                plt.close()

            elif analysis_type == "HSV Histograms":
                # Convert to HSV
                hsv_image = rgb_image.convert('HSV')
                hsv_array = np.array(hsv_image)

                fig, axes = plt.subplots(1, 3, figsize=(15, 5))

                # HSV histograms
                hsv_labels = ['Hue', 'Saturation', 'Value']
                colors = ['red', 'green', 'blue']

                for i, (label, color) in enumerate(zip(hsv_labels, colors)):
                    axes[i].hist(hsv_array[:, :, i].flatten(), bins=256, color=color, alpha=0.7)
                    axes[i].set_title(f'{label} Distribution')
                    axes[i].set_xlabel('Value')
                    axes[i].set_ylabel('Frequency')

                plt.tight_layout()
                st.pyplot(fig)
                plt.close()

            elif analysis_type == "Luminosity":
                # Calculate luminosity
                img_array = np.array(rgb_image, dtype=np.float32)
                luminosity = 0.299 * img_array[:, :, 0] + 0.587 * img_array[:, :, 1] + 0.114 * img_array[:, :, 2]

                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

                # Luminosity histogram
                ax1.hist(luminosity.flatten(), bins=256, color='gray', alpha=0.7)
                ax1.set_title('Luminosity Distribution')
                ax1.set_xlabel('Luminosity Value')
                ax1.set_ylabel('Frequency')

                # Luminosity image
                ax2.imshow(luminosity, cmap='gray')
                ax2.set_title('Luminosity Map')
                ax2.axis('off')

                plt.tight_layout()
                st.pyplot(fig)
                plt.close()

            elif analysis_type == "Color Statistics":
                # Calculate color statistics
                img_array = np.array(rgb_image)

                st.subheader("Color Statistics")

                # RGB statistics
                rgb_stats = {}
                channels = ['Red', 'Green', 'Blue']

                for i, channel in enumerate(channels):
                    channel_data = img_array[:, :, i]
                    rgb_stats[channel] = {
                        'Mean': np.mean(channel_data),
                        'Median': np.median(channel_data),
                        'Std Dev': np.std(channel_data),
                        'Min': np.min(channel_data),
                        'Max': np.max(channel_data)
                    }

                # Display statistics table
                import pandas as pd
                stats_df = pd.DataFrame(rgb_stats).round(2)
                st.dataframe(stats_df)

                # Overall image statistics
                st.subheader("Overall Image Statistics")
                total_pixels = img_array.shape[0] * img_array.shape[1]

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Pixels", f"{total_pixels:,}")
                    st.metric("Image Dimensions", f"{img_array.shape[1]}×{img_array.shape[0]}")

                with col2:
                    # Calculate dominant color
                    flat_img = img_array.reshape(-1, 3)
                    from sklearn.cluster import KMeans
                    kmeans = KMeans(n_clusters=1, random_state=42, n_init=10)
                    dominant_color = kmeans.fit(flat_img).cluster_centers_[0].astype(int)
                    st.metric("Dominant Color", f"RGB({dominant_color[0]}, {dominant_color[1]}, {dominant_color[2]})")

                    # Color diversity (standard deviation of all pixels)
                    color_diversity = np.std(flat_img)
                    st.metric("Color Diversity", f"{color_diversity:.1f}")

                with col3:
                    # Brightness
                    brightness = np.mean(img_array)
                    st.metric("Average Brightness", f"{brightness:.1f}")

                    # Contrast (RMS contrast)
                    contrast = np.std(img_array)
                    st.metric("Contrast (RMS)", f"{contrast:.1f}")


def blur_effects():
    """Apply blur effects to images"""
    create_tool_header("Blur Effects", "Apply various blur effects", "〰️")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            blur_type = st.selectbox("Blur Type", ["Gaussian Blur", "Motion Blur", "Radial Blur", "Simple Blur"])

            if blur_type == "Gaussian Blur":
                radius = st.slider("Radius", 0.1, 10.0, 1.0, 0.1)
            elif blur_type == "Motion Blur":
                radius = st.slider("Radius", 1, 20, 5)
            else:
                radius = st.slider("Intensity", 1, 10, 2)

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)

            with col2:
                st.subheader("Blurred Image")

                if blur_type == "Gaussian Blur":
                    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=radius))
                elif blur_type == "Simple Blur":
                    blurred_image = image
                    for _ in range(int(radius)):
                        blurred_image = blurred_image.filter(ImageFilter.BLUR)
                elif blur_type == "Motion Blur":
                    # Simple motion blur simulation
                    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=radius / 2))
                else:  # Radial blur
                    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=radius))

                st.image(blurred_image, use_column_width=True)

            if st.button("Download Blurred Image"):
                output = io.BytesIO()
                format_name = image.format if image.format else "PNG"
                blurred_image.save(output, format=format_name)

                base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                extension = uploaded_file[0].name.rsplit('.', 1)[1]
                filename = f"{base_name}_blurred.{extension}"

                FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def metadata_extractor():
    """Extract image metadata and EXIF data"""
    create_tool_header("Metadata Extractor", "Extract image metadata and EXIF data", "📋")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.subheader(f"Metadata for: {uploaded_file.name}")

            try:
                image = FileHandler.process_image_file(uploaded_file)
                if image:
                    # Basic image info
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Width", f"{image.width} px")
                    with col2:
                        st.metric("Height", f"{image.height} px")
                    with col3:
                        st.metric("Mode", image.mode)

                    col4, col5, col6 = st.columns(3)
                    with col4:
                        st.metric("Format", image.format or "Unknown")
                    with col5:
                        st.metric("File Size", f"{uploaded_file.size:,} bytes")
                    with col6:
                        aspect_ratio = round(image.width / image.height, 2)
                        st.metric("Aspect Ratio", f"{aspect_ratio}:1")

                    # EXIF data (for JPEG images)
                    if hasattr(image, '_getexif') and image._getexif():
                        exif = image._getexif()
                        if exif:
                            st.subheader("EXIF Data")
                            exif_data = {}

                            # Common EXIF tags
                            exif_tags = {
                                256: 'ImageWidth',
                                257: 'ImageLength',
                                272: 'Make',
                                273: 'StripOffsets',
                                274: 'Orientation',
                                282: 'XResolution',
                                283: 'YResolution',
                                306: 'DateTime',
                                315: 'Artist'
                            }

                            for tag_id, value in exif.items():
                                tag_name = exif_tags.get(tag_id, f'Tag_{tag_id}')
                                exif_data[tag_name] = str(value)

                            if exif_data:
                                for key, value in exif_data.items():
                                    st.write(f"**{key}**: {value}")
                            else:
                                st.info("No readable EXIF data found")
                        else:
                            st.info("No EXIF data available")
                    else:
                        st.info("EXIF data not available for this format")

                    # Color analysis
                    st.subheader("Color Analysis")
                    if image.mode == 'RGB':
                        # Calculate average color
                        img_array = np.array(image)
                        avg_color = np.mean(img_array, axis=(0, 1)).astype(int)
                        hex_color = f"#{avg_color[0]:02x}{avg_color[1]:02x}{avg_color[2]:02x}"

                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Average Color**: {hex_color}")
                            st.markdown(
                                f'<div style="width:100px;height:50px;background-color:{hex_color};border:1px solid #000;"></div>',
                                unsafe_allow_html=True)

                        with col2:
                            # Calculate histogram
                            histogram = cv2.calcHist([cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)], [0, 1, 2], None,
                                                     [256, 256, 256], [0, 256, 0, 256, 0, 256])
                            st.write(f"**Total Pixels**: {image.width * image.height:,}")
                            st.write(f"**Color Depth**: {image.mode}")

            except Exception as e:
                st.error(f"Error extracting metadata from {uploaded_file.name}: {str(e)}")

            st.markdown("---")


def background_removal():
    """AI-powered background removal"""
    create_tool_header("Background Removal", "Remove backgrounds using AI", "🎭")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            st.image(image, caption="Original Image", use_column_width=True)

            if st.button("Remove Background"):
                with st.spinner("Processing image with AI..."):
                    # Convert image to bytes for AI processing
                    img_bytes = io.BytesIO()
                    image.save(img_bytes, format='PNG')
                    img_bytes.seek(0)

                    # Processing background removal using computer vision
                    st.info("Processing image using edge detection and masking techniques...")

                    # Simple background removal using color thresholding (basic implementation)
                    # This is a simplified version - in a real scenario, you'd use more sophisticated AI models

                    # Convert to HSV for better color separation
                    img_array = np.array(image)
                    hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)

                    # Create a simple mask based on edge detection
                    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                    edges = cv2.Canny(gray, 50, 150)

                    # Dilate edges to create a rough mask
                    kernel = np.ones((5, 5), np.uint8)
                    mask = cv2.dilate(edges, kernel, iterations=2)
                    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

                    # Create alpha channel
                    result_img = image.convert("RGBA")
                    result_array = np.array(result_img)

                    # Apply mask (simplified approach)
                    alpha_channel = 255 - mask
                    result_array[:, :, 3] = alpha_channel

                    result_image = Image.fromarray(result_array, 'RGBA')

                    st.subheader("Result (Simplified Background Removal)")
                    st.image(result_image, caption="Background Removed", use_column_width=True)
                    st.warning(
                        "This is a simplified background removal. For professional results, use dedicated AI services like Remove.bg or similar APIs.")

                    # Save result
                    output = io.BytesIO()
                    result_image.save(output, format='PNG')

                    base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                    filename = f"{base_name}_no_bg.png"

                    FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def text_overlay():
    """Add text overlay to images"""
    create_tool_header("Text Overlay", "Add customizable text to images", "📝")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                             accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            st.image(image, caption="Original Image", use_column_width=True)

            # Text settings
            text_content = st.text_area("Text to add:", "Your Text Here")

            col1, col2, col3 = st.columns(3)
            with col1:
                font_size = st.slider("Font Size", 10, 200, 48)
                text_color = st.color_picker("Text Color", "#FFFFFF")
            with col2:
                outline_width = st.slider("Outline Width", 0, 10, 2)
                outline_color = st.color_picker("Outline Color", "#000000")
            with col3:
                opacity = st.slider("Opacity", 10, 100, 100)
                rotation = st.slider("Rotation", -180, 180, 0)

            position = st.selectbox("Position", ["Custom", "Top Left", "Top Center", "Top Right",
                                                 "Center Left", "Center", "Center Right",
                                                 "Bottom Left", "Bottom Center", "Bottom Right"])

            if position == "Custom":
                col1, col2 = st.columns(2)
                with col1:
                    x_pos = st.slider("X Position", 0, image.width, image.width // 2)
                with col2:
                    y_pos = st.slider("Y Position", 0, image.height, image.height // 2)

            shadow = st.checkbox("Add Shadow")
            if shadow:
                shadow_offset = st.slider("Shadow Offset", 1, 20, 5)
                shadow_color = st.color_picker("Shadow Color", "#808080")

            if st.button("Add Text"):
                try:
                    # Create a copy of the image
                    result_image = image.copy()
                    if result_image.mode != 'RGBA':
                        result_image = result_image.convert('RGBA')

                    # Create overlay for text
                    overlay = Image.new('RGBA', result_image.size, (0, 0, 0, 0))
                    draw = ImageDraw.Draw(overlay)

                    # Try to load a better font
                    try:
                        font = ImageFont.truetype("arial.ttf", font_size)
                    except:
                        try:
                            font = ImageFont.truetype("Arial.ttf", font_size)
                        except:
                            font = ImageFont.load_default()

                    # Calculate text position
                    bbox = draw.textbbox((0, 0), text_content, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    if position == "Custom":
                        x, y = x_pos, y_pos
                    else:
                        position_map = {
                            "Top Left": (20, 20),
                            "Top Center": ((image.width - text_width) // 2, 20),
                            "Top Right": (image.width - text_width - 20, 20),
                            "Center Left": (20, (image.height - text_height) // 2),
                            "Center": ((image.width - text_width) // 2, (image.height - text_height) // 2),
                            "Center Right": (image.width - text_width - 20, (image.height - text_height) // 2),
                            "Bottom Left": (20, image.height - text_height - 20),
                            "Bottom Center": ((image.width - text_width) // 2, image.height - text_height - 20),
                            "Bottom Right": (image.width - text_width - 20, image.height - text_height - 20)
                        }
                        x, y = position_map.get(position, (50, 50))

                    # Convert colors
                    def hex_to_rgba(hex_color, alpha=255):
                        hex_color = hex_color.lstrip('#')
                        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)

                    text_rgba = hex_to_rgba(text_color, int(255 * opacity / 100))
                    outline_rgba = hex_to_rgba(outline_color, int(255 * opacity / 100))

                    # Add shadow if enabled
                    if shadow:
                        shadow_rgba = hex_to_rgba(shadow_color, int(128 * opacity / 100))
                        draw.text((x + shadow_offset, y + shadow_offset), text_content,
                                  font=font, fill=shadow_rgba)

                    # Add outline if enabled
                    if outline_width > 0:
                        for dx in range(-outline_width, outline_width + 1):
                            for dy in range(-outline_width, outline_width + 1):
                                if dx != 0 or dy != 0:
                                    draw.text((x + dx, y + dy), text_content,
                                              font=font, fill=outline_rgba)

                    # Add main text
                    draw.text((x, y), text_content, font=font, fill=text_rgba)

                    # Handle rotation if needed
                    if rotation != 0:
                        overlay = overlay.rotate(rotation, expand=True)

                    # Composite the overlay
                    result_image = Image.alpha_composite(result_image, overlay)

                    st.subheader("Result")
                    st.image(result_image, caption="Image with Text Overlay", use_column_width=True)

                    # Save result
                    output = io.BytesIO()
                    result_image.save(output, format='PNG')

                    base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                    filename = f"{base_name}_with_text.png"

                    FileHandler.create_download_link(output.getvalue(), filename, "image/png")

                except Exception as e:
                    st.error(f"Error adding text overlay: {str(e)}")


def image_enhancement():
    """AI-powered image enhancement"""
    create_tool_header("Image Enhancement", "Enhance images using AI", "✨")

    uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    if uploaded_file:
        image = FileHandler.process_image_file(uploaded_file[0])

        if image:
            st.image(image, caption="Original Image", use_column_width=True)

            enhancement_type = st.selectbox("Enhancement Type", [
                "Auto Enhance", "Noise Reduction", "Sharpening", "Color Correction", "Upscaling"
            ])

            if st.button("Enhance Image"):
                with st.spinner("Enhancing image with AI..."):
                    # Get AI analysis and suggestions
                    img_bytes = io.BytesIO()
                    image.save(img_bytes, format='PNG')
                    img_bytes.seek(0)

                    # Processing image enhancement
                    st.info(f"Applying {enhancement_type} enhancement to the image...")

                    # Apply basic enhancements based on type
                    enhanced_image = image.copy()

                    if enhancement_type == "Auto Enhance":
                        # Apply multiple enhancements
                        enhancer = ImageEnhance.Sharpness(enhanced_image)
                        enhanced_image = enhancer.enhance(1.2)

                        enhancer = ImageEnhance.Contrast(enhanced_image)
                        enhanced_image = enhancer.enhance(1.1)

                        enhancer = ImageEnhance.Color(enhanced_image)
                        enhanced_image = enhancer.enhance(1.05)

                    elif enhancement_type == "Noise Reduction":
                        # Simple noise reduction using blur
                        enhanced_image = enhanced_image.filter(ImageFilter.SMOOTH)

                    elif enhancement_type == "Sharpening":
                        enhancer = ImageEnhance.Sharpness(enhanced_image)
                        enhanced_image = enhancer.enhance(1.5)
                        enhanced_image = enhanced_image.filter(ImageFilter.SHARPEN)

                    elif enhancement_type == "Color Correction":
                        enhancer = ImageEnhance.Color(enhanced_image)
                        enhanced_image = enhancer.enhance(1.2)

                        enhancer = ImageEnhance.Contrast(enhanced_image)
                        enhanced_image = enhancer.enhance(1.1)

                    elif enhancement_type == "Upscaling":
                        # Simple upscaling (2x)
                        new_size = (image.width * 2, image.height * 2)
                        enhanced_image = enhanced_image.resize(new_size, Image.Resampling.LANCZOS)

                    st.subheader("Enhanced Image")
                    st.image(enhanced_image, caption=f"Enhanced ({enhancement_type})", use_column_width=True)

                    # Save enhanced image
                    output = io.BytesIO()
                    enhanced_image.save(output, format='PNG')

                    base_name = uploaded_file[0].name.rsplit('.', 1)[0]
                    filename = f"{base_name}_enhanced.png"

                    FileHandler.create_download_link(output.getvalue(), filename, "image/png")


def collage_maker():
    """Create image collages"""
    create_tool_header("Collage Maker", "Create collages from multiple images", "🖼️")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp'], accept_multiple=True)

    if uploaded_files and len(uploaded_files) >= 2:
        st.write(f"Uploaded {len(uploaded_files)} images")

        # Collage settings
        col1, col2 = st.columns(2)
        with col1:
            layout = st.selectbox("Layout", ["Grid", "Mosaic", "Linear"])
            if layout == "Grid":
                cols = st.slider("Columns", 1, min(len(uploaded_files), 5), 2)
                rows = st.slider("Rows", 1, min(len(uploaded_files), 5), 2)

        with col2:
            canvas_width = st.number_input("Canvas Width", min_value=100, value=1200)
            canvas_height = st.number_input("Canvas Height", min_value=100, value=800)

        spacing = st.slider("Image Spacing", 0, 50, 10)
        background_color = st.color_picker("Background Color", "#FFFFFF")

        if st.button("Create Collage"):
            try:
                # Create canvas
                canvas = Image.new('RGB', (canvas_width, canvas_height), background_color)

                # Process images
                images = []
                for uploaded_file in uploaded_files:
                    img = FileHandler.process_image_file(uploaded_file)
                    if img:
                        images.append(img)

                if layout == "Grid":
                    # Calculate cell size
                    cell_width = (canvas_width - spacing * (cols + 1)) // cols
                    cell_height = (canvas_height - spacing * (rows + 1)) // rows

                    for i, img in enumerate(images[:cols * rows]):
                        row = i // cols
                        col = i % cols

                        # Resize image to fit cell
                        img.thumbnail((cell_width, cell_height), Image.Resampling.LANCZOS)

                        # Calculate position
                        x = spacing + col * (cell_width + spacing)
                        y = spacing + row * (cell_height + spacing)

                        # Center image in cell
                        x += (cell_width - img.width) // 2
                        y += (cell_height - img.height) // 2

                        canvas.paste(img, (x, y))

                elif layout == "Linear":
                    # Arrange images in a row
                    total_width = canvas_width - spacing * (len(images) + 1)
                    img_width = total_width // len(images)

                    for i, img in enumerate(images):
                        # Resize image
                        aspect_ratio = img.height / img.width
                        new_height = int(img_width * aspect_ratio)
                        img = img.resize((img_width, new_height), Image.Resampling.LANCZOS)

                        # Calculate position
                        x = spacing + i * (img_width + spacing)
                        y = (canvas_height - img.height) // 2

                        canvas.paste(img, (x, y))

                else:  # Mosaic
                    # Simple mosaic layout
                    positions = [
                        (spacing, spacing),
                        (canvas_width // 2, spacing),
                        (spacing, canvas_height // 2),
                        (canvas_width // 2, canvas_height // 2)
                    ]

                    cell_width = (canvas_width - spacing * 3) // 2
                    cell_height = (canvas_height - spacing * 3) // 2

                    for i, img in enumerate(images[:4]):
                        img.thumbnail((cell_width, cell_height), Image.Resampling.LANCZOS)

                        x, y = positions[i]
                        x += (cell_width - img.width) // 2
                        y += (cell_height - img.height) // 2

                        canvas.paste(img, (x, y))

                st.subheader("Collage Result")
                st.image(canvas, caption="Created Collage", use_column_width=True)

                # Save collage
                output = io.BytesIO()
                canvas.save(output, format='PNG')

                FileHandler.create_download_link(output.getvalue(), "collage.png", "image/png")

            except Exception as e:
                st.error(f"Error creating collage: {str(e)}")

    elif uploaded_files and len(uploaded_files) < 2:
        st.warning("Please upload at least 2 images to create a collage.")


def icon_generator():
    """Generate icons and favicons"""
    create_tool_header("Icon Generator", "Generate icons and favicons", "🔮")

    # Icon generation options
    generation_method = st.selectbox("Generation Method", ["From Text", "From Image", "AI Generated"])

    if generation_method == "From Text":
        text = st.text_input("Text for Icon", "AB")
        font_size = st.slider("Font Size", 10, 200, 64)
        text_color = st.color_picker("Text Color", "#FFFFFF")
        bg_color = st.color_picker("Background Color", "#007BFF")

    elif generation_method == "From Image":
        uploaded_file = FileHandler.upload_files(['jpg', 'jpeg', 'png'], accept_multiple=False)

    else:  # AI Generated
        prompt = st.text_input("Describe your icon", "A modern, minimalist app icon")

    # Icon sizes
    sizes = st.multiselect("Icon Sizes", [16, 32, 48, 64, 128, 256, 512], default=[32, 64, 128])

    if st.button("Generate Icons"):
        icon_files = {}

        try:
            if generation_method == "From Text":
                # Create base icon
                base_size = max(sizes)
                icon = Image.new('RGB', (base_size, base_size), bg_color)
                draw = ImageDraw.Draw(icon)

                # Try to load a font
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()

                # Calculate text position
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                x = (base_size - text_width) // 2
                y = (base_size - text_height) // 2

                draw.text((x, y), text, font=font, fill=text_color)

                # Generate different sizes
                for size in sizes:
                    if size == base_size:
                        sized_icon = icon
                    else:
                        sized_icon = icon.resize((size, size), Image.Resampling.LANCZOS)

                    output = io.BytesIO()
                    sized_icon.save(output, format='PNG')
                    icon_files[f"icon_{size}x{size}.png"] = output.getvalue()

            elif generation_method == "From Image" and uploaded_file:
                source_image = FileHandler.process_image_file(uploaded_file[0])
                if source_image:
                    # Make square
                    min_dim = min(source_image.width, source_image.height)
                    left = (source_image.width - min_dim) // 2
                    top = (source_image.height - min_dim) // 2
                    square_image = source_image.crop((left, top, left + min_dim, top + min_dim))

                    # Generate different sizes
                    for size in sizes:
                        sized_icon = square_image.resize((size, size), Image.Resampling.LANCZOS)

                        output = io.BytesIO()
                        sized_icon.save(output, format='PNG')
                        icon_files[f"icon_{size}x{size}.png"] = output.getvalue()

            else:  # AI Generated
                st.info(
                    "AI icon generation requires an image generation service. For now, please use the 'From Color' or 'From Image' options.")

            if icon_files:
                # Display generated icons
                st.subheader("Generated Icons")
                cols = st.columns(len(sizes))
                for i, size in enumerate(sizes):
                    with cols[i]:
                        filename = next((f for f in icon_files.keys() if f"_{size}x{size}" in f), None)
                        if filename:
                            img_data = icon_files[filename]
                            st.image(io.BytesIO(img_data), caption=f"{size}×{size}", width=size)

                # Create download
                if len(icon_files) == 1:
                    filename, data = next(iter(icon_files.items()))
                    FileHandler.create_download_link(data, filename, "image/png")
                else:
                    zip_data = FileHandler.create_zip_archive(icon_files)
                    FileHandler.create_download_link(zip_data, "icons.zip", "application/zip")

                st.success(f"Generated {len(icon_files)} icon(s)")

        except Exception as e:
            st.error(f"Error generating icons: {str(e)}")


def animated_gif_creator():
    """Create animated GIFs from multiple images"""
    create_tool_header("Animated GIF Creator", "Create animated GIFs from multiple images", "🎬")

    st.markdown("### 🎬 Create Animated GIF")
    st.write("Upload multiple images to create an animated GIF")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files and len(uploaded_files) >= 2:
        st.success(f"Uploaded {len(uploaded_files)} images")

        # GIF settings
        col1, col2, col3 = st.columns(3)

        with col1:
            duration = st.slider("Frame duration (seconds)", 0.1, 5.0, 0.5, 0.1)

        with col2:
            loop_count = st.selectbox("Loop count", ["Infinite", "1", "2", "3", "5", "10"])
            loop_value = 0 if loop_count == "Infinite" else int(loop_count)

        with col3:
            resize_option = st.selectbox("Resize images", ["Keep original", "Resize to first image", "Custom size"])

        # Initialize custom size variables
        custom_width = 400
        custom_height = 400

        # Custom size options
        if resize_option == "Custom size":
            size_col1, size_col2 = st.columns(2)
            with size_col1:
                custom_width = st.number_input("Width (px):", value=400, min_value=50, max_value=2000)
            with size_col2:
                custom_height = st.number_input("Height (px):", value=400, min_value=50, max_value=2000)

        # Preview uploaded images
        if st.checkbox("Preview images"):
            cols = st.columns(min(4, len(uploaded_files)))
            for i, uploaded_file in enumerate(uploaded_files[:4]):
                with cols[i]:
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        st.image(image, caption=f"Frame {i + 1}", use_column_width=True)

            if len(uploaded_files) > 4:
                st.write(f"... and {len(uploaded_files) - 4} more images")

        if st.button("Create Animated GIF"):
            try:
                progress_bar = st.progress(0)
                st.info("Processing images...")

                images = []
                target_size = None

                # Process first image to get target size
                first_image = FileHandler.process_image_file(uploaded_files[0])
                if not first_image:
                    st.error("Failed to process the first image")
                    return

                if resize_option == "Keep original":
                    target_size = first_image.size
                elif resize_option == "Resize to first image":
                    target_size = first_image.size
                else:  # Custom size
                    target_size = (custom_width, custom_height)

                # Process all images
                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        # Convert to RGB if necessary
                        if image.mode == 'RGBA':
                            # Create white background for transparency
                            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
                            rgb_image.paste(image, mask=image.split()[-1])
                            image = rgb_image
                        elif image.mode != 'RGB':
                            image = image.convert('RGB')

                        # Resize if needed
                        if image.size != target_size:
                            image = image.resize(target_size, Image.Resampling.LANCZOS)

                        images.append(image)

                    progress_bar.progress((i + 1) / len(uploaded_files))

                if len(images) >= 2:
                    # Create animated GIF
                    st.info("Creating animated GIF...")

                    output = io.BytesIO()

                    # Save as animated GIF
                    images[0].save(
                        output,
                        format='GIF',
                        save_all=True,
                        append_images=images[1:],
                        duration=int(duration * 1000),  # Convert to milliseconds
                        loop=loop_value,
                        optimize=True
                    )

                    gif_data = output.getvalue()

                    # Display result
                    st.success("Animated GIF created successfully! 🎉")
                    st.image(gif_data, caption="Animated GIF Preview")

                    # Create download
                    FileHandler.create_download_link(gif_data, "animated.gif", "image/gif")

                    # Show file info
                    file_size_mb = len(gif_data) / (1024 * 1024)
                    st.info(
                        f"File size: {file_size_mb:.2f} MB | Frames: {len(images)} | Duration per frame: {duration}s")

                else:
                    st.error("Need at least 2 valid images to create an animated GIF")

            except Exception as e:
                st.error(f"Error creating animated GIF: {str(e)}")

    elif uploaded_files and len(uploaded_files) < 2:
        st.warning("Please upload at least 2 images to create an animated GIF")

    else:
        st.info("👆 Upload multiple images to get started")

        # Tips
        st.markdown("### 💡 Tips for better GIFs:")
        st.write("• Use images with similar dimensions for best results")
        st.write("• Keep file sizes reasonable - large GIFs may not load well")
        st.write("• Shorter frame durations create smoother animations")
        st.write("• Consider the order of images for smooth transitions")


def pdf_to_image():
    """Convert PDF pages to images"""
    create_tool_header("PDF to Image", "Convert PDF pages to images", "📄➡️🖼️")

    st.markdown("### 📄 Convert PDF to Images")
    st.write("Upload a PDF file to convert its pages to images")

    uploaded_file = st.file_uploader("Choose PDF file", type=['pdf'])

    if uploaded_file:
        st.success(f"Uploaded PDF: {uploaded_file.name}")

        # Conversion settings
        col1, col2, col3 = st.columns(3)

        with col1:
            output_format = st.selectbox("Output format", ["PNG", "JPEG", "WEBP"])

        with col2:
            dpi = st.slider("Quality (DPI)", 72, 300, 150, step=12)
            st.write(f"Higher DPI = better quality but larger files")

        with col3:
            page_range = st.selectbox("Pages to convert", ["All pages", "First page only", "Custom range"])

        # Initialize page range variables
        start_page = 1
        end_page = 1

        # Custom page range
        if page_range == "Custom range":
            range_col1, range_col2 = st.columns(2)
            with range_col1:
                start_page = st.number_input("Start page", value=1, min_value=1)
            with range_col2:
                end_page = st.number_input("End page", value=5, min_value=1)

        if st.button("Convert PDF to Images"):
            try:
                # Check if pdf2image is available
                try:
                    from pdf2image import convert_from_bytes
                    has_pdf2image = True
                except ImportError:
                    has_pdf2image = False

                if has_pdf2image:
                    st.info("Converting PDF using pdf2image...")
                    progress_bar = st.progress(0)

                    # Read PDF bytes
                    pdf_bytes = uploaded_file.getvalue()

                    # Set page range
                    first_page = None
                    last_page = None

                    if page_range == "First page only":
                        first_page = 1
                        last_page = 1
                    elif page_range == "Custom range":
                        first_page = start_page
                        last_page = end_page

                    # Convert PDF to images
                    images = convert_from_bytes(
                        pdf_bytes,
                        dpi=dpi,
                        first_page=first_page,
                        last_page=last_page,
                        fmt=output_format.lower()
                    )

                    if images:
                        progress_bar.progress(0.5)

                        st.success(f"Successfully converted {len(images)} page(s)! 🎉")

                        # Prepare files for download
                        converted_files = {}

                        for i, image in enumerate(images):
                            page_num = i + 1 if page_range != "Custom range" else start_page + i

                            # Convert to desired format
                            output = io.BytesIO()

                            if output_format == "JPEG" and image.mode in ("RGBA", "P"):
                                # Convert RGBA to RGB for JPEG
                                rgb_image = Image.new("RGB", image.size, (255, 255, 255))
                                rgb_image.paste(image, mask=image.split()[-1] if image.mode == "RGBA" else None)
                                image = rgb_image

                            image.save(output, format=output_format)
                            converted_files[f"page_{page_num:03d}.{output_format.lower()}"] = output.getvalue()

                        progress_bar.progress(1.0)

                        # Display preview of first few images
                        st.subheader("Preview")
                        preview_cols = st.columns(min(3, len(images)))
                        for i, image in enumerate(images[:3]):
                            with preview_cols[i]:
                                st.image(image, caption=f"Page {i + 1}", use_column_width=True)

                        if len(images) > 3:
                            st.write(f"... and {len(images) - 3} more pages")

                        # Create download
                        if len(converted_files) == 1:
                            filename, data = next(iter(converted_files.items()))
                            FileHandler.create_download_link(data, filename, f"image/{output_format.lower()}")
                        else:
                            zip_data = FileHandler.create_zip_archive(converted_files)
                            FileHandler.create_download_link(zip_data, f"{uploaded_file.name}_pages.zip",
                                                             "application/zip")

                        # Show conversion info
                        total_size_mb = sum(len(data) for data in converted_files.values()) / (1024 * 1024)
                        st.info(
                            f"Converted {len(images)} pages | Total size: {total_size_mb:.2f} MB | DPI: {dpi} | Format: {output_format}")

                    else:
                        st.error("No pages could be converted from the PDF")

                else:
                    # Fallback: Show instructions for installing pdf2image
                    st.error("PDF to Image conversion requires the pdf2image library")

                    st.markdown("### 📦 Installation Required")
                    st.write("To use PDF to Image conversion, you need to install:")

                    st.code("pip install pdf2image", language="bash")

                    st.write("You may also need to install system dependencies:")
                    st.markdown("**Linux (Ubuntu/Debian):**")
                    st.code("sudo apt-get install poppler-utils", language="bash")

                    st.markdown("**macOS:**")
                    st.code("brew install poppler", language="bash")

                    st.markdown("**Windows:**")
                    st.write("Download Poppler from: https://github.com/oschwartz10612/poppler-windows/releases/")

                    st.info("Once installed, restart the application to use this feature.")

            except Exception as e:
                st.error(f"Error converting PDF: {str(e)}")
                st.write("This might be due to:")
                st.write("• Missing system dependencies (poppler)")
                st.write("• Corrupted or encrypted PDF file")
                st.write("• Memory limitations for very large PDFs")

    else:
        st.info("👆 Upload a PDF file to get started")

        # Information about PDF conversion
        st.markdown("### 🔍 About PDF to Image Conversion")
        st.write("• Converts each page of a PDF into a separate image")
        st.write("• Supports PNG, JPEG, and WebP output formats")
        st.write("• Adjustable DPI for quality vs. file size balance")
        st.write("• Can convert specific page ranges or all pages")
        st.write("• Automatically handles multi-page PDFs")


def svg_converter():
    """Convert SVG files to other image formats"""
    create_tool_header("SVG Converter", "Convert SVG files to raster images", "🎨➡️🖼️")

    st.markdown("### 🎨 Convert SVG to Images")
    st.write("Upload SVG files to convert them to raster image formats")

    uploaded_files = FileHandler.upload_files(['svg'], accept_multiple=True)

    if uploaded_files:
        st.success(f"Uploaded {len(uploaded_files)} SVG file(s)")

        # Conversion settings
        col1, col2, col3 = st.columns(3)

        with col1:
            output_format = st.selectbox("Output format", ["PNG", "JPEG", "WEBP"])

        with col2:
            width = st.number_input("Width (pixels)", value=512, min_value=16, max_value=4096)

        with col3:
            height = st.number_input("Height (pixels)", value=512, min_value=16, max_value=4096)

        # Additional options
        col4, col5 = st.columns(2)
        with col4:
            maintain_aspect = st.checkbox("Maintain aspect ratio", value=True)
        with col5:
            background_color = st.color_picker("Background color (for JPEG)", "#FFFFFF")

        if st.button("Convert SVG"):
            try:
                # Check if cairosvg is available
                try:
                    import cairosvg
                    has_cairosvg = True
                except ImportError:
                    has_cairosvg = False

                if has_cairosvg:
                    st.info("Converting SVG using cairosvg...")
                    progress_bar = st.progress(0)

                    converted_files = {}

                    for i, uploaded_file in enumerate(uploaded_files):
                        try:
                            # Read SVG content
                            svg_content = uploaded_file.getvalue()

                            # Convert SVG to PNG first (cairosvg's native output)
                            if maintain_aspect:
                                png_data = cairosvg.svg2png(
                                    bytestring=svg_content,
                                    parent_width=width,
                                    parent_height=height
                                )
                            else:
                                png_data = cairosvg.svg2png(
                                    bytestring=svg_content,
                                    output_width=width,
                                    output_height=height
                                )

                            # Load as PIL Image for further processing
                            png_image = Image.open(io.BytesIO(png_data))

                            # Convert to desired format
                            output = io.BytesIO()

                            if output_format == "JPEG":
                                # Convert RGBA to RGB with background color for JPEG
                                if png_image.mode in ("RGBA", "P"):
                                    rgb_image = Image.new("RGB", png_image.size, background_color)
                                    rgb_image.paste(png_image,
                                                    mask=png_image.split()[-1] if png_image.mode == "RGBA" else None)
                                    png_image = rgb_image
                                png_image.save(output, format="JPEG", quality=90)

                            elif output_format == "WEBP":
                                png_image.save(output, format="WEBP", quality=90)

                            else:  # PNG
                                png_image.save(output, format="PNG")

                            # Generate filename
                            original_name = uploaded_file.name.rsplit('.', 1)[0]
                            filename = f"{original_name}.{output_format.lower()}"
                            converted_files[filename] = output.getvalue()

                        except Exception as e:
                            st.error(f"Error converting {uploaded_file.name}: {str(e)}")

                        progress_bar.progress((i + 1) / len(uploaded_files))

                    if converted_files:
                        st.success(f"Successfully converted {len(converted_files)} SVG file(s)! 🎉")

                        # Display preview
                        st.subheader("Preview")
                        preview_cols = st.columns(min(3, len(converted_files)))
                        file_items = list(converted_files.items())

                        for i, (filename, data) in enumerate(file_items[:3]):
                            with preview_cols[i]:
                                st.image(io.BytesIO(data), caption=filename, use_column_width=True)

                        if len(converted_files) > 3:
                            st.write(f"... and {len(converted_files) - 3} more files")

                        # Create download
                        if len(converted_files) == 1:
                            filename, data = next(iter(converted_files.items()))
                            FileHandler.create_download_link(data, filename, f"image/{output_format.lower()}")
                        else:
                            zip_data = FileHandler.create_zip_archive(converted_files)
                            FileHandler.create_download_link(zip_data, "converted_svgs.zip", "application/zip")

                        # Show conversion info
                        total_size_mb = sum(len(data) for data in converted_files.values()) / (1024 * 1024)
                        st.info(
                            f"Converted {len(converted_files)} files | Total size: {total_size_mb:.2f} MB | Size: {width}×{height} | Format: {output_format}")

                    else:
                        st.error("No SVG files could be converted")

                else:
                    # Fallback: Simple SVG to image conversion using Wand or basic approach
                    st.warning("Advanced SVG conversion requires the cairosvg library")

                    # Try basic conversion using PIL and svg handling
                    st.info("Attempting basic SVG conversion...")

                    converted_files = {}
                    progress_bar = st.progress(0)

                    for i, uploaded_file in enumerate(uploaded_files):
                        try:
                            # Basic SVG handling - this is limited but might work for simple SVGs
                            svg_content = uploaded_file.getvalue().decode('utf-8')

                            # Try to use Wand if available
                            try:
                                from wand.image import Image as WandImage
                                from wand.color import Color

                                with WandImage() as img:
                                    img.format = 'svg'
                                    img.read(blob=uploaded_file.getvalue())
                                    img.format = output_format.lower()
                                    img.resize(width, height)

                                    if output_format == "JPEG":
                                        img.background_color = Color(background_color)
                                        img.alpha_channel = 'remove'

                                    output = io.BytesIO()
                                    img.save(output)

                                    original_name = uploaded_file.name.rsplit('.', 1)[0]
                                    filename = f"{original_name}.{output_format.lower()}"
                                    converted_files[filename] = output.getvalue()

                            except ImportError:
                                st.error(f"Cannot convert {uploaded_file.name}: Missing conversion libraries")

                        except Exception as e:
                            st.error(f"Error converting {uploaded_file.name}: {str(e)}")

                        progress_bar.progress((i + 1) / len(uploaded_files))

                    if converted_files:
                        st.success(f"Successfully converted {len(converted_files)} SVG file(s)! 🎉")

                        # Create download
                        if len(converted_files) == 1:
                            filename, data = next(iter(converted_files.items()))
                            FileHandler.create_download_link(data, filename, f"image/{output_format.lower()}")
                        else:
                            zip_data = FileHandler.create_zip_archive(converted_files)
                            FileHandler.create_download_link(zip_data, "converted_svgs.zip", "application/zip")
                    else:
                        # Show installation instructions
                        st.markdown("### 📦 Installation Required")
                        st.write("For full SVG conversion support, install one of these libraries:")

                        st.markdown("**Option 1 - CairoSVG (Recommended):**")
                        st.code("pip install cairosvg", language="bash")

                        st.markdown("**Option 2 - Wand (ImageMagick):**")
                        st.code("pip install Wand", language="bash")

                        st.write("System dependencies may also be required:")
                        st.markdown("**Linux:** `sudo apt-get install libcairo2-dev libffi-dev`")
                        st.markdown("**macOS:** `brew install cairo libffi`")
                        st.markdown("**Windows:** May require GTK+ runtime")

                        st.info("Once installed, restart the application to use this feature.")

            except Exception as e:
                st.error(f"Error during SVG conversion: {str(e)}")

    else:
        st.info("👆 Upload SVG file(s) to get started")

        # Information about SVG conversion
        st.markdown("### 🔍 About SVG Conversion")
        st.write("• Converts scalable SVG graphics to raster images")
        st.write("• Supports PNG, JPEG, and WebP output formats")
        st.write("• Customizable width and height")
        st.write("• Option to maintain original aspect ratio")
        st.write("• Background color setting for JPEG format")
        st.write("• Batch conversion support for multiple files")


def image_comparison():
    """Compare two images using various similarity metrics"""
    create_tool_header("Image Comparison", "Compare images using similarity metrics", "🔍")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Image 1")
        uploaded_file1 = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                                  accept_multiple=False, key="img1")

    with col2:
        st.subheader("Image 2")
        uploaded_file2 = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                                  accept_multiple=False, key="img2")

    if uploaded_file1 and uploaded_file2:
        try:
            image1 = FileHandler.process_image_file(uploaded_file1[0])
            image2 = FileHandler.process_image_file(uploaded_file2[0])

            if image1 and image2:
                # Display images
                col1, col2 = st.columns(2)
                with col1:
                    st.image(image1, caption="Image 1", use_column_width=True)
                    st.write(f"Size: {image1.size[0]} × {image1.size[1]} pixels")
                with col2:
                    st.image(image2, caption="Image 2", use_column_width=True)
                    st.write(f"Size: {image2.size[0]} × {image2.size[1]} pixels")

                if st.button("Compare Images"):
                    # Convert to same size for comparison
                    target_size = (min(image1.size[0], image2.size[0]), min(image1.size[1], image2.size[1]))
                    img1_resized = image1.resize(target_size, Image.Resampling.LANCZOS)
                    img2_resized = image2.resize(target_size, Image.Resampling.LANCZOS)

                    # Convert to RGB
                    img1_rgb = img1_resized.convert('RGB')
                    img2_rgb = img2_resized.convert('RGB')

                    # Convert to numpy arrays
                    arr1 = np.array(img1_rgb)
                    arr2 = np.array(img2_rgb)

                    # Calculate various similarity metrics
                    st.subheader("Similarity Analysis")

                    # Mean Squared Error
                    mse = np.mean((arr1.astype(float) - arr2.astype(float)) ** 2)
                    st.metric("Mean Squared Error (MSE)", f"{mse:.2f}",
                              help="Lower values indicate more similar images")

                    # Peak Signal-to-Noise Ratio
                    if mse > 0:
                        psnr = 20 * np.log10(255.0 / np.sqrt(mse))
                        st.metric("Peak Signal-to-Noise Ratio (PSNR)", f"{psnr:.2f} dB",
                                  help="Higher values indicate more similar images")

                    # Structural Similarity Index (SSIM) approximation
                    # Convert to grayscale for SSIM calculation
                    gray1 = cv2.cvtColor(arr1, cv2.COLOR_RGB2GRAY)
                    gray2 = cv2.cvtColor(arr2, cv2.COLOR_RGB2GRAY)

                    # Calculate means
                    mu1 = np.mean(gray1)
                    mu2 = np.mean(gray2)

                    # Calculate variances and covariance
                    var1 = np.var(gray1)
                    var2 = np.var(gray2)
                    cov = np.mean((gray1 - mu1) * (gray2 - mu2))

                    # SSIM calculation
                    c1 = (0.01 * 255) ** 2
                    c2 = (0.03 * 255) ** 2
                    ssim = ((2 * mu1 * mu2 + c1) * (2 * cov + c2)) / ((mu1 ** 2 + mu2 ** 2 + c1) * (var1 + var2 + c2))

                    st.metric("Structural Similarity Index (SSIM)", f"{ssim:.4f}",
                              help="Values closer to 1 indicate more similar images")

                    # Color histogram comparison
                    hist1_r = cv2.calcHist([arr1], [0], None, [256], [0, 256])
                    hist1_g = cv2.calcHist([arr1], [1], None, [256], [0, 256])
                    hist1_b = cv2.calcHist([arr1], [2], None, [256], [0, 256])

                    hist2_r = cv2.calcHist([arr2], [0], None, [256], [0, 256])
                    hist2_g = cv2.calcHist([arr2], [1], None, [256], [0, 256])
                    hist2_b = cv2.calcHist([arr2], [2], None, [256], [0, 256])

                    corr_r = cv2.compareHist(hist1_r, hist2_r, cv2.HISTCMP_CORREL)
                    corr_g = cv2.compareHist(hist1_g, hist2_g, cv2.HISTCMP_CORREL)
                    corr_b = cv2.compareHist(hist1_b, hist2_b, cv2.HISTCMP_CORREL)

                    color_similarity = (corr_r + corr_g + corr_b) / 3
                    st.metric("Color Histogram Correlation", f"{color_similarity:.4f}",
                              help="Values closer to 1 indicate more similar color distributions")

                    # Overall similarity score
                    overall_similarity = (ssim + color_similarity) / 2 * 100
                    st.metric("Overall Similarity Score", f"{overall_similarity:.1f}%",
                              help="Combined similarity score")

                    # Create difference visualization
                    st.subheader("Difference Visualization")
                    diff = cv2.absdiff(arr1, arr2)

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.image(diff, caption="Absolute Difference", use_column_width=True)
                    with col2:
                        # Highlight significant differences
                        diff_gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                        threshold_diff = cv2.threshold(diff_gray, 30, 255, cv2.THRESH_BINARY)[1]
                        st.image(threshold_diff, caption="Significant Differences", use_column_width=True)
                    with col3:
                        # Create heatmap
                        diff_intensity = np.mean(diff, axis=2)
                        plt.figure(figsize=(6, 6))
                        plt.imshow(diff_intensity, cmap='hot', interpolation='nearest')
                        plt.colorbar(label='Difference Intensity')
                        plt.title('Difference Heatmap')
                        plt.axis('off')
                        st.pyplot(plt)
                        plt.close()

        except Exception as e:
            st.error(f"Error comparing images: {str(e)}")


def face_detection():
    """Detect faces in images using OpenCV"""
    create_tool_header("Face Detection", "Detect and highlight faces in images", "👤")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        # Detection parameters
        st.subheader("Detection Settings")
        scale_factor = st.slider("Scale Factor", 1.1, 2.0, 1.3, 0.1,
                                 help="How much the image size is reduced at each scale")
        min_neighbors = st.slider("Minimum Neighbors", 1, 10, 5,
                                  help="How many neighbors each candidate rectangle should retain")
        min_size = st.slider("Minimum Face Size", 20, 200, 30, help="Minimum possible face size in pixels")

        detection_color = st.color_picker("Detection Box Color", "#00FF00")
        box_thickness = st.slider("Box Thickness", 1, 10, 3)

        if st.button("Detect Faces"):
            try:
                # Initialize face cascade
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                detected_files = {}
                total_faces = 0
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        # Convert to OpenCV format
                        opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

                        # Detect faces
                        faces = face_cascade.detectMultiScale(
                            gray,
                            scaleFactor=scale_factor,
                            minNeighbors=min_neighbors,
                            minSize=(min_size, min_size)
                        )

                        total_faces += len(faces)

                        # Draw rectangles around faces
                        result_image = opencv_image.copy()
                        color_bgr = tuple(int(detection_color[i:i + 2], 16) for i in (5, 3, 1))  # Convert hex to BGR

                        for (x, y, w, h) in faces:
                            cv2.rectangle(result_image, (x, y), (x + w, y + h), color_bgr, box_thickness)
                            # Add face number
                            cv2.putText(result_image, f'Face {len(detected_files) + 1}',
                                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color_bgr, 2)

                        # Convert back to RGB for display
                        result_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
                        result_pil = Image.fromarray(result_rgb)

                        # Save processed image
                        output = io.BytesIO()
                        result_pil.save(output, format='PNG')

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        filename = f"{base_name}_faces_detected.png"
                        detected_files[filename] = output.getvalue()

                        # Display results
                        st.subheader(f"Results for {uploaded_file.name}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(image, caption="Original", use_column_width=True)
                        with col2:
                            st.image(result_pil, caption=f"Detected {len(faces)} face(s)", use_column_width=True)

                        st.write(f"Faces detected: {len(faces)}")
                        if len(faces) > 0:
                            for j, (x, y, w, h) in enumerate(faces):
                                st.write(f"Face {j + 1}: Position ({x}, {y}), Size {w}×{h} pixels")

                        progress_bar.progress((i + 1) / len(uploaded_files))

                st.success(f"Detection complete! Found {total_faces} face(s) across {len(uploaded_files)} image(s)")

                # Create downloads
                if detected_files:
                    if len(detected_files) == 1:
                        filename, data = next(iter(detected_files.items()))
                        FileHandler.create_download_link(data, filename, "image/png")
                    else:
                        zip_data = FileHandler.create_zip_archive(detected_files)
                        FileHandler.create_download_link(zip_data, "face_detection_results.zip", "application/zip")

            except Exception as e:
                st.error(f"Error during face detection: {str(e)}")
                st.info("Make sure OpenCV is properly installed with Haar cascade files.")


def object_detection():
    """Detect objects and shapes in images using OpenCV"""
    create_tool_header("Object Detection", "Detect objects, contours, and shapes in images", "🎯")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        # Detection method selection
        detection_method = st.selectbox("Detection Method",
                                        ["Contour Detection", "Edge Detection", "Shape Detection", "Blob Detection"])

        # Common parameters
        st.subheader("Detection Settings")

        if detection_method == "Contour Detection":
            threshold_val = st.slider("Binary Threshold", 50, 255, 127)
            min_area = st.slider("Minimum Contour Area", 100, 5000, 500)
            contour_color = st.color_picker("Contour Color", "#FF0000")
            thickness = st.slider("Line Thickness", 1, 10, 2)

        elif detection_method == "Edge Detection":
            low_threshold = st.slider("Low Threshold", 50, 200, 100)
            high_threshold = st.slider("High Threshold", 100, 300, 200)
            edge_color = st.color_picker("Edge Color", "#00FF00")

        elif detection_method == "Shape Detection":
            approx_epsilon = st.slider("Approximation Epsilon", 0.01, 0.1, 0.02, 0.01)
            min_area = st.slider("Minimum Shape Area", 1000, 10000, 3000)
            shape_color = st.color_picker("Shape Color", "#0000FF")
            thickness = st.slider("Line Thickness", 1, 10, 3)

        elif detection_method == "Blob Detection":
            min_threshold = st.slider("Min Threshold", 10, 100, 50)
            max_threshold = st.slider("Max Threshold", 100, 255, 200)
            min_area = st.slider("Minimum Blob Area", 50, 2000, 300)
            blob_color = st.color_picker("Blob Color", "#FF00FF")

        if st.button("Detect Objects"):
            try:
                detected_files = {}
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        # Convert to OpenCV format
                        opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
                        result_image = opencv_image.copy()
                        detection_count = 0

                        if detection_method == "Contour Detection":
                            # Binary threshold
                            _, thresh = cv2.threshold(gray, threshold_val, 255, cv2.THRESH_BINARY)
                            # Find contours
                            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                            # Filter by area and draw
                            color_bgr = tuple(int(contour_color[i:i + 2], 16) for i in (5, 3, 1))
                            for contour in contours:
                                area = cv2.contourArea(contour)
                                if area > min_area:
                                    cv2.drawContours(result_image, [contour], -1, color_bgr, thickness)
                                    detection_count += 1

                        elif detection_method == "Edge Detection":
                            # Canny edge detection
                            edges = cv2.Canny(gray, low_threshold, high_threshold)
                            # Convert edges to colored image
                            color_bgr = tuple(int(edge_color[i:i + 2], 16) for i in (5, 3, 1))
                            result_image[edges != 0] = color_bgr
                            detection_count = np.count_nonzero(edges)

                        elif detection_method == "Shape Detection":
                            # Binary threshold and contour detection
                            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
                            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                            color_bgr = tuple(int(shape_color[i:i + 2], 16) for i in (5, 3, 1))

                            for contour in contours:
                                area = cv2.contourArea(contour)
                                if area > min_area:
                                    # Approximate contour
                                    epsilon = approx_epsilon * cv2.arcLength(contour, True)
                                    approx = cv2.approxPolyDP(contour, epsilon, True)

                                    # Draw shape and label
                                    cv2.drawContours(result_image, [approx], -1, color_bgr, thickness)

                                    # Determine shape type
                                    vertices = len(approx)
                                    if vertices == 3:
                                        shape_name = "Triangle"
                                    elif vertices == 4:
                                        shape_name = "Rectangle"
                                    elif vertices > 8:
                                        shape_name = "Circle"
                                    else:
                                        shape_name = f"{vertices}-sided"

                                    # Add label
                                    M = cv2.moments(contour)
                                    if M["m00"] != 0:
                                        cx = int(M["m10"] / M["m00"])
                                        cy = int(M["m01"] / M["m00"])
                                        cv2.putText(result_image, shape_name, (cx - 30, cy),
                                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_bgr, 2)

                                    detection_count += 1

                        elif detection_method == "Blob Detection":
                            # Simple blob detection using threshold
                            _, thresh = cv2.threshold(gray, min_threshold, 255, cv2.THRESH_BINARY)

                            # Find contours as blobs
                            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                            color_bgr = tuple(int(blob_color[i:i + 2], 16) for i in (5, 3, 1))

                            for contour in contours:
                                area = cv2.contourArea(contour)
                                if area > min_area:
                                    # Draw filled circle at centroid
                                    M = cv2.moments(contour)
                                    if M["m00"] != 0:
                                        cx = int(M["m10"] / M["m00"])
                                        cy = int(M["m01"] / M["m00"])
                                        cv2.circle(result_image, (cx, cy), 10, color_bgr, -1)
                                        detection_count += 1

                        # Convert back to RGB for display
                        result_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
                        result_pil = Image.fromarray(result_rgb)

                        # Save processed image
                        output = io.BytesIO()
                        result_pil.save(output, format='PNG')

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        filename = f"{base_name}_{detection_method.lower().replace(' ', '_')}.png"
                        detected_files[filename] = output.getvalue()

                        # Display results
                        st.subheader(f"Results for {uploaded_file.name}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(image, caption="Original", use_column_width=True)
                        with col2:
                            st.image(result_pil, caption=f"Detected: {detection_count} objects", use_column_width=True)

                        progress_bar.progress((i + 1) / len(uploaded_files))

                st.success(f"Object detection complete using {detection_method}!")

                # Create downloads
                if detected_files:
                    if len(detected_files) == 1:
                        filename, data = next(iter(detected_files.items()))
                        FileHandler.create_download_link(data, filename, "image/png")
                    else:
                        zip_data = FileHandler.create_zip_archive(detected_files)
                        FileHandler.create_download_link(zip_data, "object_detection_results.zip", "application/zip")

            except Exception as e:
                st.error(f"Error during object detection: {str(e)}")


def image_statistics():
    """Analyze comprehensive image statistics"""
    create_tool_header("Image Statistics", "Comprehensive statistical analysis of images", "📊")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        analysis_type = st.selectbox("Analysis Type",
                                     ["Basic Statistics", "Color Analysis", "Histogram Analysis",
                                      "Comprehensive Report"])

        if st.button("Analyze Images"):
            try:
                all_stats = []
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        st.subheader(f"Analysis for {uploaded_file.name}")

                        # Convert to numpy array
                        img_array = np.array(image)

                        # Basic image information
                        stats = {
                            'filename': uploaded_file.name,
                            'width': image.size[0],
                            'height': image.size[1],
                            'channels': len(img_array.shape),
                            'mode': image.mode,
                            'format': image.format or 'Unknown'
                        }

                        if analysis_type in ["Basic Statistics", "Comprehensive Report"]:
                            st.markdown("### Basic Statistics")
                            col1, col2, col3 = st.columns(3)

                            with col1:
                                st.metric("Width", f"{stats['width']} px")
                                st.metric("Height", f"{stats['height']} px")
                                st.metric("Total Pixels", f"{stats['width'] * stats['height']:,}")

                            with col2:
                                st.metric("Color Mode", stats['mode'])
                                st.metric("File Format", stats['format'])
                                aspect_ratio = stats['width'] / stats['height']
                                st.metric("Aspect Ratio", f"{aspect_ratio:.2f}:1")

                            with col3:
                                file_size = len(uploaded_file.getvalue())
                                st.metric("File Size", f"{file_size:,} bytes")
                                st.metric("Size (KB)", f"{file_size / 1024:.1f} KB")
                                if file_size > 1024 * 1024:
                                    st.metric("Size (MB)", f"{file_size / (1024 * 1024):.2f} MB")

                        if analysis_type in ["Color Analysis", "Comprehensive Report"]:
                            st.markdown("### Color Analysis")

                            if len(img_array.shape) == 3 and img_array.shape[2] >= 3:
                                # RGB color analysis
                                r_channel = img_array[:, :, 0]
                                g_channel = img_array[:, :, 1]
                                b_channel = img_array[:, :, 2]

                                # Channel statistics
                                col1, col2, col3 = st.columns(3)

                                with col1:
                                    st.markdown("**Red Channel**")
                                    st.metric("Mean", f"{np.mean(r_channel):.1f}")
                                    st.metric("Std Dev", f"{np.std(r_channel):.1f}")
                                    st.metric("Min/Max", f"{np.min(r_channel)}/{np.max(r_channel)}")

                                with col2:
                                    st.markdown("**Green Channel**")
                                    st.metric("Mean", f"{np.mean(g_channel):.1f}")
                                    st.metric("Std Dev", f"{np.std(g_channel):.1f}")
                                    st.metric("Min/Max", f"{np.min(g_channel)}/{np.max(g_channel)}")

                                with col3:
                                    st.markdown("**Blue Channel**")
                                    st.metric("Mean", f"{np.mean(b_channel):.1f}")
                                    st.metric("Std Dev", f"{np.std(b_channel):.1f}")
                                    st.metric("Min/Max", f"{np.min(b_channel)}/{np.max(b_channel)}")

                                # Overall brightness and contrast
                                brightness = np.mean(img_array)
                                contrast = np.std(img_array)

                                col1, col2 = st.columns(2)
                                with col1:
                                    st.metric("Average Brightness", f"{brightness:.1f}")
                                with col2:
                                    st.metric("Contrast (Std Dev)", f"{contrast:.1f}")

                                # Dominant colors using k-means
                                rgb_image = image.convert('RGB')
                                rgb_image.thumbnail((100, 100))  # Reduce size for faster processing
                                img_small = np.array(rgb_image).reshape(-1, 3)

                                try:
                                    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
                                    kmeans.fit(img_small)
                                    colors = kmeans.cluster_centers_.astype(int)

                                    st.markdown("**Top 5 Dominant Colors**")
                                    cols = st.columns(5)
                                    for j, color in enumerate(colors):
                                        hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
                                        with cols[j]:
                                            st.markdown(
                                                f'<div style="width:100%;height:50px;background-color:{hex_color};border:1px solid #000;"></div>',
                                                unsafe_allow_html=True)
                                            st.caption(hex_color)
                                except:
                                    st.info("Could not calculate dominant colors")

                        if analysis_type in ["Histogram Analysis", "Comprehensive Report"]:
                            st.markdown("### Histogram Analysis")

                            # Create histograms
                            fig, axes = plt.subplots(2, 2, figsize=(12, 8))

                            if len(img_array.shape) == 3 and img_array.shape[2] >= 3:
                                # RGB histograms
                                axes[0, 0].hist(img_array[:, :, 0].ravel(), bins=50, color='red', alpha=0.7,
                                                label='Red')
                                axes[0, 0].set_title('Red Channel Histogram')
                                axes[0, 0].set_ylabel('Frequency')

                                axes[0, 1].hist(img_array[:, :, 1].ravel(), bins=50, color='green', alpha=0.7,
                                                label='Green')
                                axes[0, 1].set_title('Green Channel Histogram')

                                axes[1, 0].hist(img_array[:, :, 2].ravel(), bins=50, color='blue', alpha=0.7,
                                                label='Blue')
                                axes[1, 0].set_title('Blue Channel Histogram')
                                axes[1, 0].set_xlabel('Pixel Value')
                                axes[1, 0].set_ylabel('Frequency')

                                # Combined RGB histogram
                                axes[1, 1].hist(img_array[:, :, 0].ravel(), bins=50, color='red', alpha=0.5,
                                                label='Red')
                                axes[1, 1].hist(img_array[:, :, 1].ravel(), bins=50, color='green', alpha=0.5,
                                                label='Green')
                                axes[1, 1].hist(img_array[:, :, 2].ravel(), bins=50, color='blue', alpha=0.5,
                                                label='Blue')
                                axes[1, 1].set_title('Combined RGB Histogram')
                                axes[1, 1].set_xlabel('Pixel Value')
                                axes[1, 1].legend()
                            else:
                                # Grayscale histogram
                                if len(img_array.shape) == 2:
                                    gray_data = img_array
                                else:
                                    gray_data = np.mean(img_array, axis=2)

                                axes[0, 0].hist(gray_data.ravel(), bins=50, color='gray', alpha=0.7)
                                axes[0, 0].set_title('Grayscale Histogram')
                                axes[0, 0].set_ylabel('Frequency')
                                axes[0, 0].set_xlabel('Pixel Value')

                                # Hide other subplots
                                for ax in [axes[0, 1], axes[1, 0], axes[1, 1]]:
                                    ax.set_visible(False)

                            plt.tight_layout()
                            st.pyplot(fig)
                            plt.close()

                        if analysis_type == "Comprehensive Report":
                            st.markdown("### Advanced Metrics")

                            # Calculate additional metrics
                            entropy = -np.sum(np.histogram(img_array.ravel(), bins=256)[0] * np.log2(
                                np.histogram(img_array.ravel(), bins=256)[0] + 1e-10))

                            # Laplacian variance (focus measure)
                            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if len(
                                img_array.shape) == 3 else img_array
                            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Image Entropy", f"{entropy:.2f}", help="Measure of image complexity")
                            with col2:
                                st.metric("Focus Measure", f"{laplacian_var:.2f}",
                                          help="Higher values indicate sharper images")
                            with col3:
                                unique_colors = len(np.unique(img_array.reshape(-1, img_array.shape[-1]), axis=0))
                                st.metric("Unique Colors", f"{unique_colors:,}")

                        all_stats.append(stats)
                        st.markdown("---")

                        progress_bar.progress((i + 1) / len(uploaded_files))

                # Summary for multiple images
                if len(uploaded_files) > 1:
                    st.subheader("Summary Comparison")

                    # Create comparison table
                    import pandas as pd
                    df = pd.DataFrame(all_stats)
                    st.dataframe(df)

                    # Summary statistics
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Average Width", f"{df['width'].mean():.0f} px")
                        st.metric("Average Height", f"{df['height'].mean():.0f} px")
                    with col2:
                        total_pixels = (df['width'] * df['height']).sum()
                        st.metric("Total Pixels (all images)", f"{total_pixels:,}")
                        most_common_format = df['format'].mode().values[0] if len(df['format'].mode()) > 0 else "Mixed"
                        st.metric("Most Common Format", most_common_format)

                st.success(f"Statistical analysis complete for {len(uploaded_files)} image(s)!")

            except Exception as e:
                st.error(f"Error during statistical analysis: {str(e)}")


def quality_optimizer():
    """Intelligently optimize image quality with smart compression"""
    create_tool_header("Quality Optimizer", "Smart quality optimization with automatic settings", "⚡")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        st.subheader("Optimization Settings")

        optimization_mode = st.selectbox("Optimization Mode",
                                         ["Automatic", "Target File Size", "Quality Score", "Custom Settings"])

        if optimization_mode == "Target File Size":
            target_size_kb = st.slider("Target Size (KB)", 10, 2000, 200)

        elif optimization_mode == "Quality Score":
            quality_score = st.slider("Quality Score (1-10)", 1, 10, 7)

        elif optimization_mode == "Custom Settings":
            jpeg_quality = st.slider("JPEG Quality", 10, 100, 85)
            png_compression = st.slider("PNG Compression", 0, 9, 6)
            webp_quality = st.slider("WebP Quality", 10, 100, 80)

        output_format = st.selectbox("Output Format", ["Auto-Select", "JPEG", "PNG", "WebP"])
        preserve_metadata = st.checkbox("Preserve Metadata", False)

        if st.button("Optimize Images"):
            try:
                optimized_files = {}
                progress_bar = st.progress(0)
                total_original_size = 0
                total_optimized_size = 0

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        original_size = len(uploaded_file.getvalue())
                        total_original_size += original_size

                        # Analyze image characteristics
                        img_array = np.array(image)

                        # Calculate image complexity metrics
                        if len(img_array.shape) == 3:
                            # Color complexity
                            unique_colors = len(np.unique(img_array.reshape(-1, img_array.shape[-1]), axis=0))
                            color_variance = np.var(img_array)

                            # Edge density (detail level)
                            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                            edges = cv2.Canny(gray, 50, 150)
                            edge_density = np.count_nonzero(edges) / edges.size
                        else:
                            unique_colors = len(np.unique(img_array))
                            color_variance = np.var(img_array)
                            edges = cv2.Canny(img_array, 50, 150)
                            edge_density = np.count_nonzero(edges) / edges.size

                        # Determine optimal settings
                        if optimization_mode == "Automatic":
                            # Smart format selection
                            if output_format == "Auto-Select":
                                if unique_colors < 256 and edge_density < 0.1:
                                    best_format = "PNG"  # Low color count, clean edges
                                elif edge_density > 0.3 or color_variance > 3000:
                                    best_format = "JPEG"  # High detail, natural images
                                else:
                                    best_format = "WebP"  # Good balance
                            else:
                                best_format = output_format

                            # Smart quality selection
                            if edge_density > 0.4:  # High detail
                                quality = 90
                            elif edge_density > 0.2:  # Medium detail
                                quality = 80
                            else:  # Low detail
                                quality = 70

                        elif optimization_mode == "Target File Size":
                            best_format = output_format if output_format != "Auto-Select" else "JPEG"
                            # Estimate quality needed for target size
                            size_ratio = target_size_kb * 1024 / original_size
                            if size_ratio > 1:
                                quality = 95
                            elif size_ratio > 0.5:
                                quality = 85
                            elif size_ratio > 0.3:
                                quality = 70
                            elif size_ratio > 0.2:
                                quality = 55
                            else:
                                quality = 40

                        elif optimization_mode == "Quality Score":
                            best_format = output_format if output_format != "Auto-Select" else "JPEG"
                            quality = int(quality_score * 10)  # Convert 1-10 to 10-100

                        else:  # Custom Settings
                            best_format = output_format if output_format != "Auto-Select" else "JPEG"
                            if best_format == "JPEG":
                                quality = jpeg_quality
                            elif best_format == "PNG":
                                quality = png_compression
                            else:
                                quality = webp_quality

                        # Apply optimization
                        optimized_image = image.copy()

                        # Handle format-specific requirements
                        if best_format == "JPEG" and optimized_image.mode in ("RGBA", "P"):
                            rgb_image = Image.new("RGB", optimized_image.size, (255, 255, 255))
                            rgb_image.paste(optimized_image, mask=optimized_image.split()[
                                -1] if optimized_image.mode == "RGBA" else None)
                            optimized_image = rgb_image

                        # Save optimized image
                        output = io.BytesIO()
                        save_kwargs = {"format": best_format}

                        if best_format == "JPEG":
                            save_kwargs.update({"quality": quality, "optimize": True})
                        elif best_format == "PNG":
                            save_kwargs.update({"compress_level": min(quality, 9), "optimize": True})
                        elif best_format == "WebP":
                            save_kwargs.update({"quality": quality, "optimize": True})

                        # Preserve metadata if requested
                        if preserve_metadata and hasattr(image, 'info'):
                            save_kwargs["exif"] = image.info.get("exif")

                        optimized_image.save(output, **save_kwargs)
                        optimized_data = output.getvalue()
                        optimized_size = len(optimized_data)
                        total_optimized_size += optimized_size

                        # Generate filename
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        new_filename = f"{base_name}_optimized.{best_format.lower()}"
                        optimized_files[new_filename] = optimized_data

                        # Show optimization results
                        compression_ratio = (original_size - optimized_size) / original_size * 100
                        st.write(
                            f"**{uploaded_file.name}**: {original_size:,} → {optimized_size:,} bytes ({compression_ratio:.1f}% reduction)")
                        st.write(f"Format: {best_format}, Quality: {quality}")

                        progress_bar.progress((i + 1) / len(uploaded_files))

                # Overall statistics
                overall_compression = (total_original_size - total_optimized_size) / total_original_size * 100
                st.success(f"Optimization complete! Overall size reduction: {overall_compression:.1f}%")
                st.write(f"Total original size: {total_original_size:,} bytes")
                st.write(f"Total optimized size: {total_optimized_size:,} bytes")

                # Create downloads
                if optimized_files:
                    if len(optimized_files) == 1:
                        filename, data = next(iter(optimized_files.items()))
                        FileHandler.create_download_link(data, filename, "image/jpeg")
                    else:
                        zip_data = FileHandler.create_zip_archive(optimized_files)
                        FileHandler.create_download_link(zip_data, "optimized_images.zip", "application/zip")

            except Exception as e:
                st.error(f"Error during optimization: {str(e)}")


def batch_compression():
    """Compress multiple images with consistent settings"""
    create_tool_header("Batch Compression", "Compress multiple images with uniform settings", "📦")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        st.subheader("Batch Compression Settings")

        # Compression profile
        compression_profile = st.selectbox("Compression Profile",
                                           ["Web Optimized", "Print Quality", "Archive", "Maximum Compression",
                                            "Custom"])

        if compression_profile == "Custom":
            target_format = st.selectbox("Output Format", ["Keep Original", "JPEG", "PNG", "WebP"])
            quality = st.slider("Quality", 1, 100, 75)
            resize_option = st.checkbox("Resize Images")
            if resize_option:
                max_dimension = st.slider("Maximum Dimension (pixels)", 100, 4000, 1920)
        else:
            # Predefined profiles
            profiles = {
                "Web Optimized": {"format": "JPEG", "quality": 85, "max_dim": 1920},
                "Print Quality": {"format": "JPEG", "quality": 95, "max_dim": None},
                "Archive": {"format": "PNG", "quality": 9, "max_dim": None},
                "Maximum Compression": {"format": "JPEG", "quality": 60, "max_dim": 1200}
            }

            profile = profiles[compression_profile]
            st.write(f"Profile settings: Format={profile['format']}, Quality={profile['quality']}")
            if profile['max_dim']:
                st.write(f"Max dimension: {profile['max_dim']} pixels")

        # Advanced options
        with st.expander("Advanced Options"):
            progressive_jpeg = st.checkbox("Progressive JPEG", True)
            strip_metadata = st.checkbox("Strip Metadata", True)
            convert_to_srgb = st.checkbox("Convert to sRGB Color Space", False)
            apply_sharpening = st.checkbox("Apply Light Sharpening", False)

        if st.button("Start Batch Compression"):
            try:
                compressed_files = {}
                progress_bar = st.progress(0)
                compression_stats = []

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        original_size = len(uploaded_file.getvalue())

                        # Apply profile settings
                        if compression_profile == "Custom":
                            output_format = target_format if target_format != "Keep Original" else (
                                        image.format or "PNG")
                            output_quality = quality
                            max_dim = max_dimension if resize_option else None
                        else:
                            profile = profiles[compression_profile]
                            output_format = profile["format"]
                            output_quality = profile["quality"]
                            max_dim = profile["max_dim"]

                        processed_image = image.copy()

                        # Resize if needed
                        if max_dim and max(processed_image.size) > max_dim:
                            processed_image.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)

                        # Convert color space if requested
                        if convert_to_srgb and processed_image.mode != "RGB":
                            processed_image = processed_image.convert("RGB")

                        # Apply sharpening if requested
                        if apply_sharpening:
                            processed_image = processed_image.filter(
                                ImageFilter.UnsharpMask(radius=1, percent=100, threshold=3))

                        # Handle format requirements
                        if output_format == "JPEG" and processed_image.mode in ("RGBA", "P"):
                            rgb_image = Image.new("RGB", processed_image.size, (255, 255, 255))
                            rgb_image.paste(processed_image, mask=processed_image.split()[
                                -1] if processed_image.mode == "RGBA" else None)
                            processed_image = rgb_image

                        # Save compressed image
                        output = io.BytesIO()
                        save_kwargs = {"format": output_format}

                        if output_format == "JPEG":
                            save_kwargs.update({
                                "quality": output_quality,
                                "optimize": True,
                                "progressive": progressive_jpeg
                            })
                        elif output_format == "PNG":
                            save_kwargs.update({
                                "compress_level": min(output_quality // 10, 9),
                                "optimize": True
                            })
                        elif output_format == "WebP":
                            save_kwargs.update({
                                "quality": output_quality,
                                "optimize": True
                            })

                        # Handle metadata
                        if not strip_metadata and hasattr(image, 'info') and 'exif' in image.info:
                            save_kwargs["exif"] = image.info["exif"]

                        processed_image.save(output, **save_kwargs)
                        compressed_data = output.getvalue()
                        compressed_size = len(compressed_data)

                        # Generate filename
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        new_filename = f"{base_name}_compressed.{output_format.lower()}"
                        compressed_files[new_filename] = compressed_data

                        # Track statistics
                        compression_ratio = (original_size - compressed_size) / original_size * 100
                        compression_stats.append({
                            "filename": uploaded_file.name,
                            "original_size": original_size,
                            "compressed_size": compressed_size,
                            "compression_ratio": compression_ratio,
                            "format": output_format
                        })

                        progress_bar.progress((i + 1) / len(uploaded_files))

                # Display results
                st.subheader("Compression Results")

                total_original = sum(stat["original_size"] for stat in compression_stats)
                total_compressed = sum(stat["compressed_size"] for stat in compression_stats)
                overall_compression = (total_original - total_compressed) / total_original * 100

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Images Processed", len(compression_stats))
                with col2:
                    st.metric("Overall Compression", f"{overall_compression:.1f}%")
                with col3:
                    st.metric("Space Saved", f"{(total_original - total_compressed) / (1024 * 1024):.1f} MB")

                # Detailed results table
                for stat in compression_stats:
                    st.write(
                        f"**{stat['filename']}**: {stat['original_size']:,} → {stat['compressed_size']:,} bytes ({stat['compression_ratio']:.1f}% reduction)")

                # Create downloads
                if compressed_files:
                    if len(compressed_files) == 1:
                        filename, data = next(iter(compressed_files.items()))
                        FileHandler.create_download_link(data, filename, "image/jpeg")
                    else:
                        zip_data = FileHandler.create_zip_archive(compressed_files)
                        FileHandler.create_download_link(zip_data, "batch_compressed_images.zip", "application/zip")

                st.success(f"Batch compression complete! Processed {len(compression_stats)} images.")

            except Exception as e:
                st.error(f"Error during batch compression: {str(e)}")


def format_specific_compression():
    """Apply format-specific compression optimizations"""
    create_tool_header("Format-Specific Compression", "Optimize compression for specific image formats", "🎯")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        target_format = st.selectbox("Target Format", ["JPEG", "PNG", "WebP", "AVIF (WebP fallback)"])

        st.subheader(f"{target_format} Optimization Settings")

        if target_format == "JPEG":
            quality = st.slider("JPEG Quality", 10, 100, 85)
            progressive = st.checkbox("Progressive JPEG", True, help="Loads progressively for better user experience")
            optimize_huffman = st.checkbox("Optimize Huffman Tables", True,
                                           help="Better compression at cost of encoding time")
            subsampling = st.selectbox("Color Subsampling",
                                       ["4:4:4 (Best Quality)", "4:2:2 (Balanced)", "4:2:0 (Smallest Size)"])

        elif target_format == "PNG":
            compression_level = st.slider("Compression Level", 0, 9, 6,
                                          help="Higher values = smaller files but slower compression")
            optimize = st.checkbox("Optimize", True, help="Additional compression optimization")
            quantize_colors = st.checkbox("Color Quantization", False, help="Reduce color palette for smaller files")
            if quantize_colors:
                max_colors = st.slider("Maximum Colors", 2, 256, 256)

        elif target_format in ["WebP", "AVIF (WebP fallback)"]:
            quality = st.slider("WebP Quality", 0, 100, 80)
            lossless = st.checkbox("Lossless Compression", False, help="Perfect quality but larger files")
            if not lossless:
                method = st.slider("Compression Method", 0, 6, 4, help="Higher values = better compression but slower")
            alpha_quality = st.slider("Alpha Channel Quality", 0, 100, 100, help="Quality of transparency channel")

        # Common settings
        with st.expander("Advanced Settings"):
            strip_metadata = st.checkbox("Strip Metadata", True)
            resize_images = st.checkbox("Resize Images")
            if resize_images:
                resize_method = st.selectbox("Resize Method",
                                             ["Maintain Aspect Ratio", "Exact Dimensions", "Smart Crop"])
                if resize_method == "Maintain Aspect Ratio":
                    max_width = st.number_input("Max Width", 100, 4000, 1920)
                    max_height = st.number_input("Max Height", 100, 4000, 1080)
                elif resize_method == "Exact Dimensions":
                    exact_width = st.number_input("Width", 100, 4000, 1920)
                    exact_height = st.number_input("Height", 100, 4000, 1080)
                elif resize_method == "Smart Crop":
                    crop_width = st.number_input("Crop Width", 100, 4000, 1920)
                    crop_height = st.number_input("Crop Height", 100, 4000, 1080)

        if st.button("Apply Format-Specific Compression"):
            try:
                compressed_files = {}
                progress_bar = st.progress(0)
                format_stats = []

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        original_size = len(uploaded_file.getvalue())
                        processed_image = image.copy()

                        # Apply resizing if requested
                        if resize_images:
                            if resize_method == "Maintain Aspect Ratio":
                                processed_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
                            elif resize_method == "Exact Dimensions":
                                processed_image = processed_image.resize((exact_width, exact_height),
                                                                         Image.Resampling.LANCZOS)
                            elif resize_method == "Smart Crop":
                                # Smart crop to center
                                aspect_ratio = crop_width / crop_height
                                img_ratio = processed_image.width / processed_image.height

                                if img_ratio > aspect_ratio:
                                    # Image is wider, crop width
                                    new_width = int(processed_image.height * aspect_ratio)
                                    left = (processed_image.width - new_width) // 2
                                    processed_image = processed_image.crop(
                                        (left, 0, left + new_width, processed_image.height))
                                else:
                                    # Image is taller, crop height
                                    new_height = int(processed_image.width / aspect_ratio)
                                    top = (processed_image.height - new_height) // 2
                                    processed_image = processed_image.crop(
                                        (0, top, processed_image.width, top + new_height))

                                processed_image = processed_image.resize((crop_width, crop_height),
                                                                         Image.Resampling.LANCZOS)

                        # Format-specific processing
                        output = io.BytesIO()

                        if target_format == "JPEG":
                            # Convert to RGB if needed
                            if processed_image.mode in ("RGBA", "P"):
                                rgb_image = Image.new("RGB", processed_image.size, (255, 255, 255))
                                rgb_image.paste(processed_image, mask=processed_image.split()[
                                    -1] if processed_image.mode == "RGBA" else None)
                                processed_image = rgb_image

                            # Map subsampling
                            subsampling_map = {
                                "4:4:4 (Best Quality)": "4:4:4",
                                "4:2:2 (Balanced)": "4:2:2",
                                "4:2:0 (Smallest Size)": "4:2:0"
                            }

                            save_kwargs = {
                                "format": "JPEG",
                                "quality": quality,
                                "progressive": progressive,
                                "optimize": optimize_huffman,
                                "subsampling": subsampling_map[subsampling]
                            }

                        elif target_format == "PNG":
                            if quantize_colors and processed_image.mode == "RGB":
                                processed_image = processed_image.quantize(colors=max_colors)

                            save_kwargs = {
                                "format": "PNG",
                                "compress_level": compression_level,
                                "optimize": optimize
                            }

                        elif target_format in ["WebP", "AVIF (WebP fallback)"]:
                            save_kwargs = {
                                "format": "WebP",
                                "lossless": lossless,
                                "quality": quality if not lossless else 100
                            }

                            if not lossless:
                                save_kwargs["method"] = method

                            # Handle alpha channel
                            if processed_image.mode in ("RGBA", "LA"):
                                save_kwargs["alpha_quality"] = alpha_quality

                        # Handle metadata
                        if not strip_metadata and hasattr(image, 'info') and 'exif' in image.info:
                            save_kwargs["exif"] = image.info["exif"]

                        processed_image.save(output, **save_kwargs)
                        compressed_data = output.getvalue()
                        compressed_size = len(compressed_data)

                        # Generate filename
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        format_ext = target_format.lower().split()[0]  # Handle "AVIF (WebP fallback)"
                        new_filename = f"{base_name}_optimized.{format_ext}"
                        compressed_files[new_filename] = compressed_data

                        # Track statistics
                        compression_ratio = (original_size - compressed_size) / original_size * 100
                        format_stats.append({
                            "filename": uploaded_file.name,
                            "original_size": original_size,
                            "compressed_size": compressed_size,
                            "compression_ratio": compression_ratio,
                            "original_format": image.format or "Unknown",
                            "target_format": target_format
                        })

                        progress_bar.progress((i + 1) / len(uploaded_files))

                # Display format-specific results
                st.subheader(f"{target_format} Compression Results")

                total_original = sum(stat["original_size"] for stat in format_stats)
                total_compressed = sum(stat["compressed_size"] for stat in format_stats)
                overall_compression = (total_original - total_compressed) / total_original * 100

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Images Processed", len(format_stats))
                with col2:
                    st.metric(f"{target_format} Compression", f"{overall_compression:.1f}%")
                with col3:
                    avg_compression = sum(stat["compression_ratio"] for stat in format_stats) / len(format_stats)
                    st.metric("Average Compression", f"{avg_compression:.1f}%")

                # Show format conversion benefits
                format_conversions = {}
                for stat in format_stats:
                    orig_fmt = stat["original_format"]
                    if orig_fmt not in format_conversions:
                        format_conversions[orig_fmt] = {"count": 0, "total_compression": 0}
                    format_conversions[orig_fmt]["count"] += 1
                    format_conversions[orig_fmt]["total_compression"] += stat["compression_ratio"]

                st.write("**Format Conversion Benefits:**")
                for orig_fmt, data in format_conversions.items():
                    avg_comp = data["total_compression"] / data["count"]
                    st.write(
                        f"• {orig_fmt} → {target_format}: {avg_comp:.1f}% average compression ({data['count']} files)")

                # Create downloads
                if compressed_files:
                    if len(compressed_files) == 1:
                        filename, data = next(iter(compressed_files.items()))
                        FileHandler.create_download_link(data, filename, f"image/{format_ext}")
                    else:
                        zip_data = FileHandler.create_zip_archive(compressed_files)
                        FileHandler.create_download_link(zip_data, f"{target_format.lower()}_compressed_images.zip",
                                                         "application/zip")

                st.success(f"Format-specific compression to {target_format} complete!")

            except Exception as e:
                st.error(f"Error during format-specific compression: {str(e)}")


def artistic_filters():
    """Apply artistic filters and effects to images"""
    create_tool_header("Artistic Filters", "Transform photos with artistic effects", "🎨")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        st.subheader("Artistic Filter Settings")

        filter_type = st.selectbox("Filter Type", [
            "Oil Painting", "Watercolor", "Pencil Sketch", "Cartoon", "Impressionist",
            "Pop Art", "Mosaic", "Stained Glass", "Emboss", "Solarize"
        ])

        # Filter-specific parameters
        if filter_type == "Oil Painting":
            brush_size = st.slider("Brush Size", 1, 15, 7)
            color_reduction = st.slider("Color Reduction", 2, 16, 8)

        elif filter_type == "Watercolor":
            blur_value = st.slider("Blur Intensity", 5, 25, 15)
            transparency = st.slider("Transparency Effect", 0.3, 0.8, 0.6)

        elif filter_type == "Pencil Sketch":
            sketch_type = st.selectbox("Sketch Style", ["Graphite", "Colored Pencil", "Charcoal"])
            line_strength = st.slider("Line Strength", 1, 10, 5)

        elif filter_type == "Cartoon":
            edge_threshold = st.slider("Edge Threshold", 50, 200, 100)
            color_bands = st.slider("Color Bands", 4, 12, 8)

        elif filter_type == "Impressionist":
            brush_strokes = st.slider("Brush Stroke Intensity", 1, 10, 5)
            color_variance = st.slider("Color Variance", 10, 50, 25)

        elif filter_type == "Pop Art":
            color_levels = st.slider("Color Levels", 3, 8, 4)
            contrast_boost = st.slider("Contrast Boost", 1.0, 3.0, 2.0)

        elif filter_type == "Mosaic":
            tile_size = st.slider("Tile Size", 5, 50, 20)
            gap_width = st.slider("Gap Width", 0, 5, 1)

        elif filter_type == "Stained Glass":
            segment_size = st.slider("Segment Size", 10, 100, 30)
            edge_thickness = st.slider("Edge Thickness", 1, 5, 2)

        elif filter_type == "Emboss":
            depth = st.slider("Emboss Depth", 1, 10, 5)
            angle = st.slider("Light Angle", 0, 360, 45)

        elif filter_type == "Solarize":
            threshold = st.slider("Solarize Threshold", 50, 200, 128)

        if st.button("Apply Artistic Filter"):
            try:
                filtered_files = {}
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        # Convert to numpy array
                        img_array = np.array(image)

                        # Apply selected filter
                        if filter_type == "Oil Painting":
                            # Simulate oil painting effect
                            filtered_img = cv2.bilateralFilter(img_array, brush_size * 2, 80, 80)
                            # Reduce colors
                            data = filtered_img.reshape((-1, 3))
                            data = np.float32(data)
                            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
                            _, labels, centers = cv2.kmeans(data, color_reduction, None, criteria, 10,
                                                            cv2.KMEANS_RANDOM_CENTERS)
                            centers = np.uint8(centers)
                            filtered_img = centers[labels.flatten()]
                            filtered_img = filtered_img.reshape(img_array.shape)

                        elif filter_type == "Watercolor":
                            # Watercolor effect
                            filtered_img = cv2.bilateralFilter(img_array, blur_value, 200, 200)
                            blurred = cv2.GaussianBlur(filtered_img, (blur_value, blur_value), 0)
                            filtered_img = cv2.addWeighted(filtered_img, transparency, blurred, 1 - transparency, 0)

                        elif filter_type == "Pencil Sketch":
                            # Convert to grayscale
                            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                            # Invert colors
                            inverted = 255 - gray
                            # Blur the inverted image
                            blurred_inv = cv2.GaussianBlur(inverted, (21, 21), 0)
                            # Invert the blurred image
                            inverted_blur = 255 - blurred_inv
                            # Create pencil sketch
                            pencil_sketch = cv2.divide(gray, inverted_blur, scale=256.0)

                            if sketch_type == "Colored Pencil":
                                # Apply to original colors
                                pencil_sketch_colored = np.zeros_like(img_array)
                                for c in range(3):
                                    pencil_sketch_colored[:, :, c] = cv2.multiply(img_array[:, :, c], pencil_sketch,
                                                                                  scale=1 / 255.0)
                                filtered_img = pencil_sketch_colored
                            else:
                                # Convert to RGB
                                filtered_img = cv2.cvtColor(pencil_sketch, cv2.COLOR_GRAY2RGB)

                        elif filter_type == "Cartoon":
                            # Create edge mask
                            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                            gray_blur = cv2.medianBlur(gray, 5)
                            edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                                          9, 9)

                            # Quantize colors
                            data = img_array.reshape((-1, 3))
                            data = np.float32(data)
                            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
                            _, labels, centers = cv2.kmeans(data, color_bands, None, criteria, 10,
                                                            cv2.KMEANS_RANDOM_CENTERS)
                            centers = np.uint8(centers)
                            cartoon = centers[labels.flatten()]
                            cartoon = cartoon.reshape(img_array.shape)

                            # Combine with edges
                            edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
                            filtered_img = cv2.bitwise_and(cartoon, edges)

                        elif filter_type == "Impressionist":
                            # Create impressionist effect using random brush strokes
                            filtered_img = img_array.copy()
                            height, width = filtered_img.shape[:2]

                            for _ in range(brush_strokes * 1000):
                                # Random position and brush size
                                x = np.random.randint(0, width)
                                y = np.random.randint(0, height)
                                brush_w = np.random.randint(3, 15)
                                brush_h = np.random.randint(3, 15)

                                # Get average color in region
                                x1, y1 = max(0, x - brush_w // 2), max(0, y - brush_h // 2)
                                x2, y2 = min(width, x + brush_w // 2), min(height, y + brush_h // 2)

                                if x2 > x1 and y2 > y1:
                                    region = img_array[y1:y2, x1:x2]
                                    avg_color = np.mean(region, axis=(0, 1))
                                    # Add variance
                                    color_noise = np.random.normal(0, color_variance, 3)
                                    brush_color = np.clip(avg_color + color_noise, 0, 255).astype(np.uint8)

                                    # Draw brush stroke
                                    cv2.ellipse(filtered_img, (x, y), (brush_w // 2, brush_h // 2),
                                                np.random.randint(0, 180), 0, 360, tuple(map(int, brush_color)), -1)

                        elif filter_type == "Pop Art":
                            # Quantize colors dramatically
                            data = img_array.reshape((-1, 3))
                            data = np.float32(data)
                            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
                            _, labels, centers = cv2.kmeans(data, color_levels, None, criteria, 10,
                                                            cv2.KMEANS_RANDOM_CENTERS)
                            centers = np.uint8(centers)
                            pop_art = centers[labels.flatten()]
                            pop_art = pop_art.reshape(img_array.shape)

                            # Boost contrast
                            filtered_img = cv2.convertScaleAbs(pop_art, alpha=contrast_boost, beta=0)

                        elif filter_type == "Mosaic":
                            # Create mosaic effect
                            height, width = img_array.shape[:2]
                            filtered_img = img_array.copy()

                            for y in range(0, height, tile_size + gap_width):
                                for x in range(0, width, tile_size + gap_width):
                                    # Get tile region
                                    y1, y2 = y, min(y + tile_size, height)
                                    x1, x2 = x, min(x + tile_size, width)

                                    if y2 > y1 and x2 > x1:
                                        # Get average color
                                        tile = img_array[y1:y2, x1:x2]
                                        avg_color = np.mean(tile, axis=(0, 1))
                                        # Fill tile with average color
                                        filtered_img[y1:y2, x1:x2] = avg_color

                                        # Add gap
                                        if gap_width > 0:
                                            gap_y2 = min(y2 + gap_width, height)
                                            gap_x2 = min(x2 + gap_width, width)
                                            filtered_img[y1:gap_y2, x1:gap_x2] = [240, 240, 240]  # Light gray gaps

                        elif filter_type == "Stained Glass":
                            # Simplified stained glass effect
                            # Segment the image
                            data = img_array.reshape((-1, 3))
                            data = np.float32(data)
                            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
                            _, labels, centers = cv2.kmeans(data, segment_size, None, criteria, 10,
                                                            cv2.KMEANS_RANDOM_CENTERS)
                            centers = np.uint8(centers)
                            segmented = centers[labels.flatten()]
                            segmented = segmented.reshape(img_array.shape)

                            # Add black edges
                            gray = cv2.cvtColor(segmented, cv2.COLOR_RGB2GRAY)
                            edges = cv2.Canny(gray, 50, 150)
                            edges = cv2.dilate(edges, np.ones((edge_thickness, edge_thickness), np.uint8))

                            filtered_img = segmented.copy()
                            filtered_img[edges > 0] = [0, 0, 0]  # Black edges

                        elif filter_type == "Emboss":
                            # Create emboss kernel
                            kernel = np.array([[-2, -1, 0],
                                               [-1, 1, 1],
                                               [0, 1, 2]]) * depth

                            # Apply emboss effect
                            filtered_img = cv2.filter2D(img_array, -1, kernel)
                            # Normalize and add gray
                            filtered_img = cv2.convertScaleAbs(filtered_img)
                            filtered_img = cv2.addWeighted(filtered_img, 0.7, np.full_like(filtered_img, 128), 0.3, 0)

                        elif filter_type == "Solarize":
                            # Solarize effect
                            filtered_img = img_array.copy()
                            filtered_img[filtered_img > threshold] = 255 - filtered_img[filtered_img > threshold]

                        # Convert back to PIL Image
                        result_image = Image.fromarray(filtered_img.astype(np.uint8))

                        # Save filtered image
                        output = io.BytesIO()
                        result_image.save(output, format='PNG')

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        filename = f"{base_name}_{filter_type.lower().replace(' ', '_')}.png"
                        filtered_files[filename] = output.getvalue()

                        # Display results
                        st.subheader(f"Results for {uploaded_file.name}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(image, caption="Original", use_column_width=True)
                        with col2:
                            st.image(result_image, caption=f"{filter_type} Effect", use_column_width=True)

                        progress_bar.progress((i + 1) / len(uploaded_files))

                st.success(f"Applied {filter_type} filter to {len(uploaded_files)} image(s)!")

                # Create downloads
                if filtered_files:
                    if len(filtered_files) == 1:
                        filename, data = next(iter(filtered_files.items()))
                        FileHandler.create_download_link(data, filename, "image/png")
                    else:
                        zip_data = FileHandler.create_zip_archive(filtered_files)
                        FileHandler.create_download_link(zip_data, "artistic_filtered_images.zip", "application/zip")

            except Exception as e:
                st.error(f"Error applying artistic filter: {str(e)}")


def vintage_effects():
    """Apply vintage and retro effects to images"""
    create_tool_header("Vintage Effects", "Add nostalgic vintage and retro styling", "📷")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        st.subheader("Vintage Effect Settings")

        vintage_style = st.selectbox("Vintage Style", [
            "Sepia Tone", "Black & White Film", "Cross Process", "Lomography",
            "Polaroid", "Film Grain", "Faded Colors", "Warm Vintage", "Cool Vintage", "Retro Gaming"
        ])

        # Style-specific parameters
        intensity = st.slider("Effect Intensity", 0.1, 1.0, 0.7)

        if vintage_style in ["Film Grain", "Polaroid"]:
            grain_amount = st.slider("Grain Amount", 0.1, 2.0, 1.0)

        if vintage_style in ["Cross Process", "Lomography"]:
            color_shift = st.slider("Color Shift", 0.1, 2.0, 1.2)

        if vintage_style in ["Faded Colors", "Warm Vintage", "Cool Vintage"]:
            fade_amount = st.slider("Fade Amount", 0.1, 0.8, 0.3)

        # Additional options
        with st.expander("Additional Effects"):
            add_vignette = st.checkbox("Add Vignette", True)
            if add_vignette:
                vignette_strength = st.slider("Vignette Strength", 0.1, 1.0, 0.5)

            add_dust = st.checkbox("Add Dust/Scratches", False)
            if add_dust:
                dust_amount = st.slider("Dust Amount", 0.1, 1.0, 0.3)

        if st.button("Apply Vintage Effect"):
            try:
                vintage_files = {}
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        img_array = np.array(image).astype(np.float32)
                        height, width = img_array.shape[:2]

                        # Apply selected vintage effect
                        if vintage_style == "Sepia Tone":
                            # Sepia transformation matrix
                            sepia_kernel = np.array([[0.393, 0.769, 0.189],
                                                     [0.349, 0.686, 0.168],
                                                     [0.272, 0.534, 0.131]])
                            vintage_img = cv2.transform(img_array, sepia_kernel)

                        elif vintage_style == "Black & White Film":
                            # Classic B&W with slight warmth
                            gray = cv2.cvtColor(img_array.astype(np.uint8), cv2.COLOR_RGB2GRAY)
                            vintage_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB).astype(np.float32)
                            # Add slight sepia tint
                            vintage_img[:, :, 0] *= 1.1  # Red
                            vintage_img[:, :, 1] *= 1.05  # Green

                        elif vintage_style == "Cross Process":
                            # Cross processing effect
                            vintage_img = img_array.copy()
                            # Boost contrast and shift colors
                            vintage_img = cv2.convertScaleAbs(vintage_img, alpha=1.3, beta=-20)
                            # Color channel mixing
                            vintage_img[:, :, 0] = np.clip(vintage_img[:, :, 0] * color_shift, 0, 255)  # Red boost
                            vintage_img[:, :, 2] = np.clip(vintage_img[:, :, 2] * 0.8, 0, 255)  # Blue reduce

                        elif vintage_style == "Lomography":
                            # Lomo effect with color saturation
                            vintage_img = img_array.copy()
                            # Increase saturation
                            hsv = cv2.cvtColor(vintage_img.astype(np.uint8), cv2.COLOR_RGB2HSV).astype(np.float32)
                            hsv[:, :, 1] *= color_shift  # Saturation
                            hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255)
                            vintage_img = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB).astype(np.float32)

                        elif vintage_style == "Polaroid":
                            # Polaroid effect with slight overexposure
                            vintage_img = img_array * 1.15 + 10  # Overexpose slightly
                            vintage_img = np.clip(vintage_img, 0, 255)

                        elif vintage_style == "Film Grain":
                            # Add film grain
                            vintage_img = img_array.copy()

                        elif vintage_style == "Faded Colors":
                            # Fade colors by mixing with white
                            vintage_img = img_array * (1 - fade_amount) + 255 * fade_amount

                        elif vintage_style == "Warm Vintage":
                            # Warm color temperature
                            vintage_img = img_array.copy()
                            vintage_img[:, :, 0] *= 1.2  # Boost red
                            vintage_img[:, :, 1] *= 1.1  # Boost green slightly
                            vintage_img[:, :, 2] *= 0.9  # Reduce blue
                            vintage_img = vintage_img * (1 - fade_amount) + 255 * fade_amount

                        elif vintage_style == "Cool Vintage":
                            # Cool color temperature
                            vintage_img = img_array.copy()
                            vintage_img[:, :, 0] *= 0.9  # Reduce red
                            vintage_img[:, :, 1] *= 0.95  # Reduce green slightly
                            vintage_img[:, :, 2] *= 1.1  # Boost blue
                            vintage_img = vintage_img * (1 - fade_amount) + 255 * fade_amount

                        elif vintage_style == "Retro Gaming":
                            # 8-bit style color reduction
                            vintage_img = (img_array // 32) * 32  # Quantize to 8 levels per channel

                        # Apply intensity
                        vintage_img = img_array * (1 - intensity) + vintage_img * intensity

                        # Add film grain if selected or if it's the Film Grain style
                        if vintage_style == "Film Grain" or (
                                vintage_style == "Polaroid" and 'grain_amount' in locals()):
                            grain_strength = grain_amount if vintage_style == "Film Grain" or vintage_style == "Polaroid" else 0.5
                            noise = np.random.normal(0, grain_strength * 10, vintage_img.shape)
                            vintage_img = vintage_img + noise

                        # Add vignette effect
                        if add_vignette:
                            # Create vignette mask
                            center_x, center_y = width // 2, height // 2
                            Y, X = np.ogrid[:height, :width]
                            dist_from_center = np.sqrt((X - center_x) ** 2 + (Y - center_y) ** 2)
                            max_dist = np.sqrt(center_x ** 2 + center_y ** 2)
                            vignette_mask = 1 - (dist_from_center / max_dist) * vignette_strength
                            vignette_mask = np.clip(vignette_mask, 0, 1)

                            # Apply vignette
                            for channel in range(3):
                                vintage_img[:, :, channel] *= vignette_mask

                        # Add dust and scratches
                        if add_dust:
                            for _ in range(int(dust_amount * 100)):
                                # Random dust spots
                                x = np.random.randint(0, width)
                                y = np.random.randint(0, height)
                                size = np.random.randint(1, 3)
                                cv2.circle(vintage_img, (x, y), size, (200, 200, 200), -1)

                            # Random scratches
                            for _ in range(int(dust_amount * 20)):
                                x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
                                x2, y2 = np.random.randint(0, width), np.random.randint(0, height)
                                cv2.line(vintage_img, (x1, y1), (x2, y2), (180, 180, 180), 1)

                        # Ensure values are in valid range
                        vintage_img = np.clip(vintage_img, 0, 255)

                        # Convert back to PIL Image
                        result_image = Image.fromarray(vintage_img.astype(np.uint8))

                        # Save vintage image
                        output = io.BytesIO()
                        result_image.save(output, format='PNG')

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        filename = f"{base_name}_{vintage_style.lower().replace(' ', '_').replace('&', 'and')}.png"
                        vintage_files[filename] = output.getvalue()

                        # Display results
                        st.subheader(f"Results for {uploaded_file.name}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(image, caption="Original", use_column_width=True)
                        with col2:
                            st.image(result_image, caption=f"{vintage_style} Effect", use_column_width=True)

                        progress_bar.progress((i + 1) / len(uploaded_files))

                st.success(f"Applied {vintage_style} effect to {len(uploaded_files)} image(s)!")

                # Create downloads
                if vintage_files:
                    if len(vintage_files) == 1:
                        filename, data = next(iter(vintage_files.items()))
                        FileHandler.create_download_link(data, filename, "image/png")
                    else:
                        zip_data = FileHandler.create_zip_archive(vintage_files)
                        FileHandler.create_download_link(zip_data, "vintage_effect_images.zip", "application/zip")

            except Exception as e:
                st.error(f"Error applying vintage effect: {str(e)}")


def edge_detection():
    """Detect and highlight edges in images using various algorithms"""
    create_tool_header("Edge Detection", "Detect edges using advanced algorithms", "⚡")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        st.subheader("Edge Detection Settings")

        detection_algorithm = st.selectbox("Detection Algorithm", [
            "Canny", "Sobel", "Laplacian", "Roberts", "Prewitt", "Scharr", "LoG (Laplacian of Gaussian)"
        ])

        # Algorithm-specific parameters
        if detection_algorithm == "Canny":
            low_threshold = st.slider("Low Threshold", 50, 200, 100)
            high_threshold = st.slider("High Threshold", 100, 300, 200)
            aperture_size = st.selectbox("Aperture Size", [3, 5, 7])

        elif detection_algorithm in ["Sobel", "Scharr"]:
            dx = st.slider("X Derivative Order", 0, 2, 1)
            dy = st.slider("Y Derivative Order", 0, 2, 1)
            ksize = st.selectbox("Kernel Size", [1, 3, 5, 7]) if detection_algorithm == "Sobel" else 3

        elif detection_algorithm == "Laplacian":
            ksize = st.selectbox("Kernel Size", [1, 3, 5, 7])

        elif detection_algorithm == "LoG (Laplacian of Gaussian)":
            sigma = st.slider("Gaussian Sigma", 0.5, 3.0, 1.0)

        # Output options
        output_type = st.selectbox("Output Type", ["Edge Lines Only", "Colored Edges", "Overlay on Original"])
        if output_type == "Colored Edges":
            edge_color = st.color_picker("Edge Color", "#FF0000")

        # Preprocessing options
        with st.expander("Preprocessing Options"):
            apply_blur = st.checkbox("Apply Gaussian Blur", True)
            if apply_blur:
                blur_kernel = st.slider("Blur Kernel Size", 3, 15, 5, step=2)

        if st.button("Detect Edges"):
            try:
                edge_files = {}
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        img_array = np.array(image)

                        # Convert to grayscale for edge detection
                        if len(img_array.shape) == 3:
                            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                        else:
                            gray = img_array

                        # Apply preprocessing
                        if apply_blur:
                            gray = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel), 0)

                        # Apply edge detection algorithm
                        if detection_algorithm == "Canny":
                            edges = cv2.Canny(gray, low_threshold, high_threshold, apertureSize=aperture_size)

                        elif detection_algorithm == "Sobel":
                            # Calculate gradients
                            if ksize == 1:
                                sobelx = cv2.Sobel(gray, cv2.CV_64F, dx, 0, ksize=3)
                                sobely = cv2.Sobel(gray, cv2.CV_64F, 0, dy, ksize=3)
                            else:
                                sobelx = cv2.Sobel(gray, cv2.CV_64F, dx, 0, ksize=ksize)
                                sobely = cv2.Sobel(gray, cv2.CV_64F, 0, dy, ksize=ksize)

                            # Combine gradients
                            edges = np.sqrt(sobelx ** 2 + sobely ** 2)
                            edges = np.uint8(np.clip(edges, 0, 255))

                        elif detection_algorithm == "Laplacian":
                            edges = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
                            edges = np.uint8(np.absolute(edges))

                        elif detection_algorithm == "Roberts":
                            # Roberts cross-gradient masks
                            roberts_x = np.array([[1, 0], [0, -1]])
                            roberts_y = np.array([[0, 1], [-1, 0]])

                            edges_x = cv2.filter2D(gray, cv2.CV_64F, roberts_x)
                            edges_y = cv2.filter2D(gray, cv2.CV_64F, roberts_y)
                            edges = np.sqrt(edges_x ** 2 + edges_y ** 2)
                            edges = np.uint8(np.clip(edges, 0, 255))

                        elif detection_algorithm == "Prewitt":
                            # Prewitt operators
                            prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
                            prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

                            edges_x = cv2.filter2D(gray, cv2.CV_64F, prewitt_x)
                            edges_y = cv2.filter2D(gray, cv2.CV_64F, prewitt_y)
                            edges = np.sqrt(edges_x ** 2 + edges_y ** 2)
                            edges = np.uint8(np.clip(edges, 0, 255))

                        elif detection_algorithm == "Scharr":
                            scharr_x = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
                            scharr_y = cv2.Scharr(gray, cv2.CV_64F, 0, 1)
                            edges = np.sqrt(scharr_x ** 2 + scharr_y ** 2)
                            edges = np.uint8(np.clip(edges, 0, 255))

                        elif detection_algorithm == "LoG (Laplacian of Gaussian)":
                            # Apply Gaussian blur first
                            blurred = cv2.GaussianBlur(gray, (0, 0), sigma)
                            # Then Laplacian
                            edges = cv2.Laplacian(blurred, cv2.CV_64F)
                            edges = np.uint8(np.absolute(edges))

                        # Create output based on selected type
                        if output_type == "Edge Lines Only":
                            # Simple black and white edges
                            result_image = Image.fromarray(edges, mode='L').convert('RGB')

                        elif output_type == "Colored Edges":
                            # Colored edges on black background
                            result_array = np.zeros((edges.shape[0], edges.shape[1], 3), dtype=np.uint8)
                            # Convert hex color to RGB
                            color_rgb = tuple(int(edge_color[i:i + 2], 16) for i in (1, 3, 5))

                            # Apply color to edges
                            edge_mask = edges > 50  # Threshold for edge visibility
                            result_array[edge_mask] = color_rgb
                            result_image = Image.fromarray(result_array)

                        elif output_type == "Overlay on Original":
                            # Overlay edges on original image
                            result_array = img_array.copy()
                            edge_mask = edges > 50

                            # Make edges red
                            result_array[edge_mask] = [255, 0, 0]
                            result_image = Image.fromarray(result_array)

                        # Save edge-detected image
                        output = io.BytesIO()
                        result_image.save(output, format='PNG')

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        filename = f"{base_name}_{detection_algorithm.lower().replace(' ', '_')}_edges.png"
                        edge_files[filename] = output.getvalue()

                        # Display results
                        st.subheader(f"Results for {uploaded_file.name}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(image, caption="Original", use_column_width=True)
                        with col2:
                            st.image(result_image, caption=f"{detection_algorithm} Edges", use_column_width=True)

                        # Show edge statistics
                        edge_pixels = np.count_nonzero(edges > 50)
                        total_pixels = edges.shape[0] * edges.shape[1]
                        edge_percentage = (edge_pixels / total_pixels) * 100
                        st.write(f"Edge density: {edge_percentage:.2f}% ({edge_pixels:,} edge pixels)")

                        progress_bar.progress((i + 1) / len(uploaded_files))

                st.success(f"Applied {detection_algorithm} edge detection to {len(uploaded_files)} image(s)!")

                # Create downloads
                if edge_files:
                    if len(edge_files) == 1:
                        filename, data = next(iter(edge_files.items()))
                        FileHandler.create_download_link(data, filename, "image/png")
                    else:
                        zip_data = FileHandler.create_zip_archive(edge_files)
                        FileHandler.create_download_link(zip_data, "edge_detection_results.zip", "application/zip")

            except Exception as e:
                st.error(f"Error during edge detection: {str(e)}")


def noise_reduction():
    """Reduce noise in images using various denoising algorithms"""
    create_tool_header("Noise Reduction", "Remove noise and improve image quality", "🔧")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        st.subheader("Noise Reduction Settings")

        denoising_method = st.selectbox("Denoising Method", [
            "Gaussian Blur", "Bilateral Filter", "Non-Local Means", "Median Filter",
            "Morphological", "Wiener Filter", "Total Variation", "Adaptive"
        ])

        # Method-specific parameters
        if denoising_method == "Gaussian Blur":
            kernel_size = st.slider("Kernel Size", 3, 15, 5, step=2)
            sigma = st.slider("Sigma", 0.5, 3.0, 1.0)

        elif denoising_method == "Bilateral Filter":
            d = st.slider("Diameter", 5, 15, 9)
            sigma_color = st.slider("Sigma Color", 10, 150, 75)
            sigma_space = st.slider("Sigma Space", 10, 150, 75)

        elif denoising_method == "Non-Local Means":
            h = st.slider("Filter Strength", 3, 20, 10)
            template_window_size = st.slider("Template Window Size", 7, 21, 7, step=2)
            search_window_size = st.slider("Search Window Size", 21, 35, 21, step=2)

        elif denoising_method == "Median Filter":
            kernel_size = st.slider("Kernel Size", 3, 15, 5, step=2)

        elif denoising_method == "Morphological":
            operation = st.selectbox("Morphological Operation", ["Opening", "Closing", "Gradient"])
            kernel_size = st.slider("Kernel Size", 3, 9, 5, step=2)

        elif denoising_method == "Total Variation":
            weight = st.slider("Regularization Weight", 0.01, 0.3, 0.1)
            iterations = st.slider("Iterations", 50, 200, 100)

        # Noise type estimation
        with st.expander("Advanced Options"):
            estimate_noise = st.checkbox("Estimate Noise Level", True)
            preserve_edges = st.checkbox("Preserve Edges", True)
            apply_sharpening = st.checkbox("Apply Post-Sharpening", False)
            if apply_sharpening:
                sharpening_amount = st.slider("Sharpening Amount", 0.1, 2.0, 0.5)

        if st.button("Reduce Noise"):
            try:
                denoised_files = {}
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    image = FileHandler.process_image_file(uploaded_file)
                    if image:
                        img_array = np.array(image)

                        # Estimate noise level if requested
                        noise_level = 0
                        if estimate_noise:
                            if len(img_array.shape) == 3:
                                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                            else:
                                gray = img_array
                            # Simple noise estimation using Laplacian variance
                            noise_level = cv2.Laplacian(gray, cv2.CV_64F).var()

                        # Apply denoising method
                        if denoising_method == "Gaussian Blur":
                            if len(img_array.shape) == 3:
                                denoised = cv2.GaussianBlur(img_array, (kernel_size, kernel_size), sigma)
                            else:
                                denoised = cv2.GaussianBlur(img_array, (kernel_size, kernel_size), sigma)

                        elif denoising_method == "Bilateral Filter":
                            if len(img_array.shape) == 3:
                                denoised = cv2.bilateralFilter(img_array, d, sigma_color, sigma_space)
                            else:
                                denoised = cv2.bilateralFilter(img_array, d, sigma_color, sigma_space)

                        elif denoising_method == "Non-Local Means":
                            if len(img_array.shape) == 3:
                                denoised = cv2.fastNlMeansDenoisingColored(img_array, None, h, h,
                                                                           template_window_size, search_window_size)
                            else:
                                denoised = cv2.fastNlMeansDenoising(img_array, None, h,
                                                                    template_window_size, search_window_size)

                        elif denoising_method == "Median Filter":
                            denoised = cv2.medianBlur(img_array, kernel_size)

                        elif denoising_method == "Morphological":
                            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
                            if operation == "Opening":
                                denoised = cv2.morphologyEx(img_array, cv2.MORPH_OPEN, kernel)
                            elif operation == "Closing":
                                denoised = cv2.morphologyEx(img_array, cv2.MORPH_CLOSE, kernel)
                            elif operation == "Gradient":
                                denoised = cv2.morphologyEx(img_array, cv2.MORPH_GRADIENT, kernel)

                        elif denoising_method == "Wiener Filter":
                            # Simplified Wiener filter using frequency domain
                            if len(img_array.shape) == 3:
                                # Process each channel separately
                                denoised = np.zeros_like(img_array)
                                for c in range(3):
                                    # FFT
                                    f_transform = np.fft.fft2(img_array[:, :, c])
                                    f_shift = np.fft.fftshift(f_transform)

                                    # Create Wiener filter
                                    rows, cols = img_array.shape[:2]
                                    crow, ccol = rows // 2, cols // 2
                                    y, x = np.ogrid[:rows, :cols]
                                    mask = ((x - ccol) ** 2 + (y - crow) ** 2) <= (min(rows, cols) // 4) ** 2

                                    # Apply filter
                                    f_shift[~mask] *= 0.1  # Reduce high frequencies

                                    # Inverse FFT
                                    f_ishift = np.fft.ifftshift(f_shift)
                                    img_back = np.fft.ifft2(f_ishift)
                                    denoised[:, :, c] = np.abs(img_back)
                            else:
                                # Single channel
                                f_transform = np.fft.fft2(img_array)
                                f_shift = np.fft.fftshift(f_transform)
                                rows, cols = img_array.shape
                                crow, ccol = rows // 2, cols // 2
                                y, x = np.ogrid[:rows, :cols]
                                mask = ((x - ccol) ** 2 + (y - crow) ** 2) <= (min(rows, cols) // 4) ** 2
                                f_shift[~mask] *= 0.1
                                f_ishift = np.fft.ifftshift(f_shift)
                                img_back = np.fft.ifft2(f_ishift)
                                denoised = np.abs(img_back)

                            denoised = np.uint8(np.clip(denoised, 0, 255))

                        elif denoising_method == "Total Variation":
                            # Simplified total variation denoising
                            denoised = img_array.astype(np.float32)

                            for _ in range(iterations):
                                if len(img_array.shape) == 3:
                                    for c in range(3):
                                        # Calculate gradients
                                        grad_x = np.diff(denoised[:, :, c], axis=1, prepend=denoised[:, :c, 0:1])
                                        grad_y = np.diff(denoised[:, :, c], axis=0, prepend=denoised[0:1, :, c])

                                        # Total variation regularization
                                        tv = weight * (np.abs(grad_x) + np.abs(grad_y))
                                        denoised[:, :, c] -= tv
                                else:
                                    grad_x = np.diff(denoised, axis=1, prepend=denoised[:, 0:1])
                                    grad_y = np.diff(denoised, axis=0, prepend=denoised[0:1, :])
                                    tv = weight * (np.abs(grad_x) + np.abs(grad_y))
                                    denoised -= tv

                            denoised = np.uint8(np.clip(denoised, 0, 255))

                        elif denoising_method == "Adaptive":
                            # Adaptive denoising based on local statistics
                            if len(img_array.shape) == 3:
                                denoised = np.zeros_like(img_array)
                                for c in range(3):
                                    # Calculate local variance
                                    kernel = np.ones((5, 5)) / 25
                                    local_mean = cv2.filter2D(img_array[:, :, c].astype(np.float32), -1, kernel)
                                    local_sqr_mean = cv2.filter2D((img_array[:, :, c] ** 2).astype(np.float32), -1,
                                                                  kernel)
                                    local_var = local_sqr_mean - local_mean ** 2

                                    # Adaptive filtering
                                    noise_var = np.mean(local_var)
                                    wiener_filter = np.maximum(local_var - noise_var, 0) / np.maximum(local_var,
                                                                                                      noise_var)
                                    denoised[:, :, c] = local_mean + wiener_filter * (img_array[:, :, c] - local_mean)
                            else:
                                kernel = np.ones((5, 5)) / 25
                                local_mean = cv2.filter2D(img_array.astype(np.float32), -1, kernel)
                                local_sqr_mean = cv2.filter2D((img_array ** 2).astype(np.float32), -1, kernel)
                                local_var = local_sqr_mean - local_mean ** 2
                                noise_var = np.mean(local_var)
                                wiener_filter = np.maximum(local_var - noise_var, 0) / np.maximum(local_var, noise_var)
                                denoised = local_mean + wiener_filter * (img_array - local_mean)

                            denoised = np.uint8(np.clip(denoised, 0, 255))

                        # Apply post-sharpening if requested
                        if apply_sharpening:
                            # Unsharp mask
                            blurred = cv2.GaussianBlur(denoised, (0, 0), 1.0)
                            sharpened = cv2.addWeighted(denoised, 1 + sharpening_amount, blurred, -sharpening_amount, 0)
                            denoised = np.clip(sharpened, 0, 255).astype(np.uint8)

                        # Convert back to PIL Image
                        result_image = Image.fromarray(denoised)

                        # Save denoised image
                        output = io.BytesIO()
                        result_image.save(output, format='PNG')

                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        filename = f"{base_name}_{denoising_method.lower().replace(' ', '_')}_denoised.png"
                        denoised_files[filename] = output.getvalue()

                        # Display results
                        st.subheader(f"Results for {uploaded_file.name}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(image, caption="Original", use_column_width=True)
                        with col2:
                            st.image(result_image, caption=f"{denoising_method} Denoised", use_column_width=True)

                        # Show noise statistics
                        if estimate_noise:
                            st.write(f"Estimated noise level: {noise_level:.2f}")

                        progress_bar.progress((i + 1) / len(uploaded_files))

                st.success(f"Applied {denoising_method} to {len(uploaded_files)} image(s)!")

                # Create downloads
                if denoised_files:
                    if len(denoised_files) == 1:
                        filename, data = next(iter(denoised_files.items()))
                        FileHandler.create_download_link(data, filename, "image/png")
                    else:
                        zip_data = FileHandler.create_zip_archive(denoised_files)
                        FileHandler.create_download_link(zip_data, "noise_reduction_results.zip", "application/zip")

            except Exception as e:
                st.error(f"Error during noise reduction: {str(e)}")


def placeholder_creator():
    """Create customizable placeholder images"""
    create_tool_header("Placeholder Creator", "Generate custom placeholder images", "🖼️")

    st.subheader("Placeholder Settings")

    # Dimension settings
    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input("Width (px)", min_value=50, max_value=5000, value=800)
        height = st.number_input("Height (px)", min_value=50, max_value=5000, value=600)

    with col2:
        # Common aspect ratios
        aspect_ratio = st.selectbox("Common Sizes", [
            "Custom", "16:9 (1920x1080)", "4:3 (1024x768)", "1:1 (Square)",
            "3:2 (1440x960)", "21:9 (2560x1080)", "Social Media (1200x630)"
        ])

        if aspect_ratio != "Custom":
            if aspect_ratio == "16:9 (1920x1080)":
                width, height = 1920, 1080
            elif aspect_ratio == "4:3 (1024x768)":
                width, height = 1024, 768
            elif aspect_ratio == "1:1 (Square)":
                width = height = 800
            elif aspect_ratio == "3:2 (1440x960)":
                width, height = 1440, 960
            elif aspect_ratio == "21:9 (2560x1080)":
                width, height = 2560, 1080
            elif aspect_ratio == "Social Media (1200x630)":
                width, height = 1200, 630

    # Appearance settings
    st.subheader("Appearance")

    # Background options
    background_type = st.selectbox("Background Type", ["Solid Color", "Gradient", "Pattern", "Noise"])

    if background_type == "Solid Color":
        bg_color = st.color_picker("Background Color", "#CCCCCC")

    elif background_type == "Gradient":
        color1 = st.color_picker("Start Color", "#FF6B6B")
        color2 = st.color_picker("End Color", "#4ECDC4")
        gradient_direction = st.selectbox("Direction", ["Horizontal", "Vertical", "Diagonal"])

    elif background_type == "Pattern":
        pattern_type = st.selectbox("Pattern", ["Checkerboard", "Stripes", "Dots", "Grid"])
        pattern_color1 = st.color_picker("Pattern Color 1", "#FFFFFF")
        pattern_color2 = st.color_picker("Pattern Color 2", "#E0E0E0")
        pattern_size = st.slider("Pattern Size", 10, 100, 30)

    elif background_type == "Noise":
        noise_color = st.color_picker("Base Color", "#CCCCCC")
        noise_intensity = st.slider("Noise Intensity", 10, 100, 30)

    # Text overlay
    with st.expander("Text Overlay"):
        add_text = st.checkbox("Add Text", True)
        if add_text:
            placeholder_text = st.text_input("Text", f"{width}×{height}")
            text_color = st.color_picker("Text Color", "#666666")
            text_size = st.slider("Text Size", 12, 200, 48)
            text_position = st.selectbox("Text Position",
                                         ["Center", "Top", "Bottom", "Top Left", "Top Right", "Bottom Left",
                                          "Bottom Right"])

    # Border settings
    with st.expander("Border"):
        add_border = st.checkbox("Add Border", False)
        if add_border:
            border_color = st.color_picker("Border Color", "#000000")
            border_width = st.slider("Border Width", 1, 20, 2)

    # Output settings
    st.subheader("Output Settings")
    output_format = st.selectbox("Format", ["PNG", "JPEG", "WebP"])
    quantity = st.number_input("Number of Images", min_value=1, max_value=50, value=1)

    if output_format == "JPEG":
        jpeg_quality = st.slider("JPEG Quality", 60, 100, 90)

    if st.button("Generate Placeholder Images"):
        try:
            placeholder_files = {}
            progress_bar = st.progress(0)

            for i in range(quantity):
                # Create base image
                image = Image.new('RGB', (width, height), (255, 255, 255))

                # Apply background
                if background_type == "Solid Color":
                    # Convert hex to RGB
                    rgb_color = tuple(int(bg_color[j:j + 2], 16) for j in (1, 3, 5))
                    image = Image.new('RGB', (width, height), rgb_color)

                elif background_type == "Gradient":
                    # Create gradient
                    rgb1 = tuple(int(color1[j:j + 2], 16) for j in (1, 3, 5))
                    rgb2 = tuple(int(color2[j:j + 2], 16) for j in (1, 3, 5))

                    gradient = Image.new('RGB', (width, height))
                    draw = ImageDraw.Draw(gradient)

                    if gradient_direction == "Horizontal":
                        for x in range(width):
                            ratio = x / width
                            r = int(rgb1[0] * (1 - ratio) + rgb2[0] * ratio)
                            g = int(rgb1[1] * (1 - ratio) + rgb2[1] * ratio)
                            b = int(rgb1[2] * (1 - ratio) + rgb2[2] * ratio)
                            draw.line([(x, 0), (x, height)], fill=(r, g, b))
                    elif gradient_direction == "Vertical":
                        for y in range(height):
                            ratio = y / height
                            r = int(rgb1[0] * (1 - ratio) + rgb2[0] * ratio)
                            g = int(rgb1[1] * (1 - ratio) + rgb2[1] * ratio)
                            b = int(rgb1[2] * (1 - ratio) + rgb2[2] * ratio)
                            draw.line([(0, y), (width, y)], fill=(r, g, b))
                    else:  # Diagonal
                        for y in range(height):
                            for x in range(width):
                                ratio = (x + y) / (width + height)
                                r = int(rgb1[0] * (1 - ratio) + rgb2[0] * ratio)
                                g = int(rgb1[1] * (1 - ratio) + rgb2[1] * ratio)
                                b = int(rgb1[2] * (1 - ratio) + rgb2[2] * ratio)
                                draw.point((x, y), fill=(r, g, b))

                    image = gradient

                elif background_type == "Pattern":
                    rgb1 = tuple(int(pattern_color1[j:j + 2], 16) for j in (1, 3, 5))
                    rgb2 = tuple(int(pattern_color2[j:j + 2], 16) for j in (1, 3, 5))

                    pattern_img = Image.new('RGB', (width, height), rgb1)
                    draw = ImageDraw.Draw(pattern_img)

                    if pattern_type == "Checkerboard":
                        for y in range(0, height, pattern_size):
                            for x in range(0, width, pattern_size):
                                if (x // pattern_size + y // pattern_size) % 2:
                                    draw.rectangle([x, y, x + pattern_size, y + pattern_size], fill=rgb2)

                    elif pattern_type == "Stripes":
                        for x in range(0, width, pattern_size):
                            if (x // pattern_size) % 2:
                                draw.rectangle([x, 0, x + pattern_size, height], fill=rgb2)

                    elif pattern_type == "Dots":
                        for y in range(pattern_size // 2, height, pattern_size):
                            for x in range(pattern_size // 2, width, pattern_size):
                                draw.ellipse([x - pattern_size // 4, y - pattern_size // 4,
                                              x + pattern_size // 4, y + pattern_size // 4], fill=rgb2)

                    elif pattern_type == "Grid":
                        for x in range(0, width, pattern_size):
                            draw.line([(x, 0), (x, height)], fill=rgb2, width=2)
                        for y in range(0, height, pattern_size):
                            draw.line([(0, y), (width, y)], fill=rgb2, width=2)

                    image = pattern_img

                elif background_type == "Noise":
                    rgb_base = tuple(int(noise_color[j:j + 2], 16) for j in (1, 3, 5))
                    noise_img = Image.new('RGB', (width, height), rgb_base)

                    # Add noise
                    img_array = np.array(noise_img)
                    noise = np.random.randint(-noise_intensity, noise_intensity, img_array.shape)
                    noisy_array = np.clip(img_array.astype(np.int16) + noise, 0, 255).astype(np.uint8)
                    image = Image.fromarray(noisy_array)

                # Add border
                if add_border:
                    border_rgb = tuple(int(border_color[j:j + 2], 16) for j in (1, 3, 5))
                    bordered = Image.new('RGB', (width + 2 * border_width, height + 2 * border_width), border_rgb)
                    bordered.paste(image, (border_width, border_width))
                    image = bordered
                    # Update dimensions for text positioning
                    actual_width = width + 2 * border_width
                    actual_height = height + 2 * border_width
                else:
                    actual_width = width
                    actual_height = height

                # Add text overlay
                if add_text:
                    draw = ImageDraw.Draw(image)
                    text_rgb = tuple(int(text_color[j:j + 2], 16) for j in (1, 3, 5))

                    try:
                        font = ImageFont.truetype("arial.ttf", text_size)
                    except:
                        font = ImageFont.load_default()

                    # Get text dimensions
                    bbox = draw.textbbox((0, 0), placeholder_text, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    # Calculate text position
                    if text_position == "Center":
                        x = (actual_width - text_width) // 2
                        y = (actual_height - text_height) // 2
                    elif text_position == "Top":
                        x = (actual_width - text_width) // 2
                        y = 20
                    elif text_position == "Bottom":
                        x = (actual_width - text_width) // 2
                        y = actual_height - text_height - 20
                    elif text_position == "Top Left":
                        x = 20
                        y = 20
                    elif text_position == "Top Right":
                        x = actual_width - text_width - 20
                        y = 20
                    elif text_position == "Bottom Left":
                        x = 20
                        y = actual_height - text_height - 20
                    elif text_position == "Bottom Right":
                        x = actual_width - text_width - 20
                        y = actual_height - text_height - 20

                    draw.text((x, y), placeholder_text, fill=text_rgb, font=font)

                # Save image
                output = io.BytesIO()
                if output_format == "JPEG":
                    if image.mode != "RGB":
                        image = image.convert("RGB")
                    image.save(output, format='JPEG', quality=jpeg_quality)
                else:
                    image.save(output, format=output_format)

                # Generate filename
                if quantity == 1:
                    filename = f"placeholder_{width}x{height}.{output_format.lower()}"
                else:
                    filename = f"placeholder_{width}x{height}_{i + 1:02d}.{output_format.lower()}"

                placeholder_files[filename] = output.getvalue()

                # Display preview for first image
                if i == 0:
                    st.subheader("Preview")
                    st.image(image, caption=f"Placeholder {width}×{height}", use_column_width=True)

                progress_bar.progress((i + 1) / quantity)

            st.success(f"Generated {quantity} placeholder image(s)!")

            # Create downloads
            if placeholder_files:
                if len(placeholder_files) == 1:
                    filename, data = next(iter(placeholder_files.items()))
                    mime_type = f"image/{output_format.lower()}"
                    FileHandler.create_download_link(data, filename, mime_type)
                else:
                    zip_data = FileHandler.create_zip_archive(placeholder_files)
                    FileHandler.create_download_link(zip_data, "placeholder_images.zip", "application/zip")

        except Exception as e:
            st.error(f"Error generating placeholder images: {str(e)}")


def format_info():
    """Display detailed format information about uploaded images"""
    create_tool_header("Format Info", "Get comprehensive format details", "📋")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'ico'],
                                              accept_multiple=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            try:
                # Load image
                image = FileHandler.process_image_file(uploaded_file)
                if image:
                    st.subheader(f"Format Information: {uploaded_file.name}")

                    # Basic information
                    col1, col2 = st.columns(2)

                    with col1:
                        st.write("**Basic Properties**")
                        st.write(f"• **Filename:** {uploaded_file.name}")
                        st.write(
                            f"• **File Size:** {len(uploaded_file.getvalue()):,} bytes ({len(uploaded_file.getvalue()) / 1024:.2f} KB)")
                        st.write(f"• **Dimensions:** {image.width} × {image.height} pixels")
                        st.write(f"• **Aspect Ratio:** {image.width / image.height:.3f}")
                        st.write(f"• **Total Pixels:** {image.width * image.height:,}")

                        # Calculate megapixels
                        megapixels = (image.width * image.height) / 1_000_000
                        st.write(f"• **Megapixels:** {megapixels:.2f} MP")

                    with col2:
                        st.write("**Format Details**")
                        st.write(f"• **Format:** {image.format or 'Unknown'}")
                        st.write(f"• **Mode:** {image.mode}")
                        st.write(f"• **Color Space:** {image.mode}")

                        # Mode explanations
                        mode_explanations = {
                            'RGB': 'Red, Green, Blue (24-bit color)',
                            'RGBA': 'Red, Green, Blue, Alpha (32-bit with transparency)',
                            'L': 'Grayscale (8-bit)',
                            'P': 'Palette mode (8-bit mapped)',
                            'CMYK': 'Cyan, Magenta, Yellow, Black (print colors)',
                            '1': 'Black and white (1-bit)'
                        }

                        if image.mode in mode_explanations:
                            st.write(f"• **Mode Info:** {mode_explanations[image.mode]}")

                        # Calculate bits per pixel
                        mode_bits = {
                            'RGB': 24, 'RGBA': 32, 'L': 8, 'P': 8,
                            'CMYK': 32, '1': 1, 'LA': 16, 'PA': 16
                        }
                        bits_per_pixel = mode_bits.get(image.mode, 0)
                        if bits_per_pixel:
                            st.write(f"• **Bits per Pixel:** {bits_per_pixel}")

                    # Advanced technical details
                    st.write("**Technical Analysis**")

                    # File type specific information
                    if image.format:
                        format_info = {
                            'JPEG': {
                                'description': 'Joint Photographic Experts Group - Lossy compression',
                                'best_for': 'Photographs and images with many colors',
                                'pros': 'Small file size, widely supported',
                                'cons': 'Lossy compression, no transparency'
                            },
                            'PNG': {
                                'description': 'Portable Network Graphics - Lossless compression',
                                'best_for': 'Graphics with transparency, logos, screenshots',
                                'pros': 'Lossless compression, transparency support',
                                'cons': 'Larger file sizes than JPEG'
                            },
                            'GIF': {
                                'description': 'Graphics Interchange Format - Limited color palette',
                                'best_for': 'Simple graphics and animations',
                                'pros': 'Animation support, small file size for simple images',
                                'cons': 'Limited to 256 colors'
                            },
                            'WEBP': {
                                'description': 'Modern web format with excellent compression',
                                'best_for': 'Web images requiring quality and small size',
                                'pros': 'Superior compression, transparency support',
                                'cons': 'Limited browser support (older browsers)'
                            },
                            'BMP': {
                                'description': 'Bitmap - Uncompressed raster format',
                                'best_for': 'Simple graphics, system compatibility',
                                'pros': 'Simple format, widely supported',
                                'cons': 'Large file sizes, no compression'
                            },
                            'TIFF': {
                                'description': 'Tagged Image File Format - Professional format',
                                'best_for': 'Professional photography and printing',
                                'pros': 'High quality, supports various compressions',
                                'cons': 'Large file sizes, limited web support'
                            }
                        }

                        if image.format in format_info:
                            info = format_info[image.format]
                            st.write(f"**{image.format} Format Analysis:**")
                            st.write(f"• **Description:** {info['description']}")
                            st.write(f"• **Best for:** {info['best_for']}")
                            st.write(f"• **Pros:** {info['pros']}")
                            st.write(f"• **Cons:** {info['cons']}")

                    # Color analysis
                    if image.mode in ['RGB', 'RGBA']:
                        st.write("**Color Analysis**")
                        img_array = np.array(image)

                        if len(img_array.shape) == 3:
                            if img_array.shape[2] >= 3:
                                # Calculate color statistics
                                red_avg = np.mean(img_array[:, :, 0])
                                green_avg = np.mean(img_array[:, :, 1])
                                blue_avg = np.mean(img_array[:, :, 2])

                                st.write(f"• **Average Red:** {red_avg:.1f}")
                                st.write(f"• **Average Green:** {green_avg:.1f}")
                                st.write(f"• **Average Blue:** {blue_avg:.1f}")

                                # Dominant color
                                dominant_color = f"rgb({int(red_avg)}, {int(green_avg)}, {int(blue_avg)})"
                                st.write(f"• **Dominant Color:** {dominant_color}")

                                # Color diversity (unique colors)
                                unique_colors = len(np.unique(img_array.reshape(-1, img_array.shape[-1]), axis=0))
                                total_possible = 256 ** img_array.shape[-1]
                                color_diversity = (unique_colors / total_possible) * 100
                                st.write(f"• **Unique Colors:** {unique_colors:,}")
                                st.write(f"• **Color Diversity:** {color_diversity:.2f}%")

                    # Compression and quality estimates
                    st.write("**Quality Metrics**")

                    # Estimate compression ratio (compared to uncompressed)
                    uncompressed_size = image.width * image.height * bits_per_pixel // 8
                    actual_size = len(uploaded_file.getvalue())
                    compression_ratio = uncompressed_size / actual_size if actual_size > 0 else 0

                    st.write(f"• **Uncompressed Size:** {uncompressed_size:,} bytes")
                    st.write(f"• **Actual Size:** {actual_size:,} bytes")
                    st.write(f"• **Compression Ratio:** {compression_ratio:.1f}:1")
                    st.write(f"• **Size Efficiency:** {(1 - actual_size / uncompressed_size) * 100:.1f}% reduction")

                    # DPI estimation (if available)
                    try:
                        dpi = image.info.get('dpi', (72, 72))
                        if dpi:
                            st.write(f"• **DPI:** {dpi[0]} × {dpi[1]}")
                    except:
                        pass

                    # Recommendations
                    st.write("**Optimization Recommendations**")

                    recommendations = []

                    # Size recommendations
                    if actual_size > 5_000_000:  # 5MB
                        recommendations.append("Large file size - consider compression or resizing")

                    # Format recommendations
                    if image.format == 'BMP':
                        recommendations.append("BMP format is uncompressed - convert to PNG or JPEG for smaller size")
                    elif image.format == 'PNG' and image.mode == 'RGB' and unique_colors > 10000:
                        recommendations.append("Complex PNG might be better as JPEG for smaller size")
                    elif image.format == 'JPEG' and image.mode == 'RGBA':
                        recommendations.append("JPEG doesn't support transparency - consider PNG")

                    # Dimension recommendations
                    if image.width > 4000 or image.height > 4000:
                        recommendations.append("Very high resolution - consider resizing for web use")

                    if recommendations:
                        for rec in recommendations:
                            st.write(f"• {rec}")
                    else:
                        st.write("• Image appears well-optimized for its intended use")

                    # Display thumbnail
                    st.write("**Image Preview**")
                    st.image(image, caption=f"{uploaded_file.name}", width=300)

                    st.divider()

            except Exception as e:
                st.error(f"Error analyzing {uploaded_file.name}: {str(e)}")


def exif_viewer():
    """Extract and display EXIF metadata from images"""
    create_tool_header("EXIF Viewer", "Extract detailed camera and image metadata", "📷")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'tiff', 'tif'],
                                              accept_multiple=True)

    if uploaded_files:
        st.info("📝 EXIF data is most commonly found in JPEG and TIFF files from digital cameras")

        for uploaded_file in uploaded_files:
            try:
                # Load image
                image = FileHandler.process_image_file(uploaded_file)
                if image:
                    st.subheader(f"EXIF Data: {uploaded_file.name}")

                    # Extract EXIF data
                    exif_data = image.getexif()

                    if exif_data:
                        # EXIF tag names mapping
                        exif_tags = {
                            256: "ImageWidth", 257: "ImageLength", 258: "BitsPerSample",
                            259: "Compression", 262: "PhotometricInterpretation", 270: "ImageDescription",
                            271: "Make", 272: "Model", 273: "StripOffsets", 274: "Orientation",
                            277: "SamplesPerPixel", 278: "RowsPerStrip", 279: "StripByteCounts",
                            282: "XResolution", 283: "YResolution", 284: "PlanarConfiguration",
                            296: "ResolutionUnit", 305: "Software", 306: "DateTime",
                            315: "Artist", 316: "HostComputer", 33432: "Copyright",
                            33434: "ExposureTime", 33437: "FNumber", 34665: "ExifOffset",
                            34850: "ExposureProgram", 34852: "SpectralSensitivity", 34855: "ISOSpeedRatings",
                            36864: "ExifVersion", 36867: "DateTimeOriginal", 36868: "DateTimeDigitized",
                            37121: "ComponentsConfiguration", 37122: "CompressedBitsPerPixel",
                            37377: "ShutterSpeedValue", 37378: "ApertureValue", 37379: "BrightnessValue",
                            37380: "ExposureBiasValue", 37381: "MaxApertureValue", 37382: "SubjectDistance",
                            37383: "MeteringMode", 37384: "LightSource", 37385: "Flash",
                            37386: "FocalLength", 37396: "SubjectArea", 37500: "MakerNote",
                            37510: "UserComment", 37520: "SubsecTime", 37521: "SubsecTimeOriginal",
                            37522: "SubsecTimeDigitized", 40960: "FlashpixVersion", 40961: "ColorSpace",
                            40962: "PixelXDimension", 40963: "PixelYDimension", 41483: "FlashEnergy",
                            41484: "SpatialFrequencyResponse", 41486: "FocalPlaneXResolution",
                            41487: "FocalPlaneYResolution", 41488: "FocalPlaneResolutionUnit",
                            41492: "SubjectLocation", 41493: "ExposureIndex", 41495: "SensingMethod",
                            41728: "FileSource", 41729: "SceneType", 41730: "CFAPattern",
                            41985: "CustomRendered", 41986: "ExposureMode", 41987: "WhiteBalance",
                            41988: "DigitalZoomRatio", 41989: "FocalLengthIn35mmFilm", 41990: "SceneCaptureType",
                            41991: "GainControl", 41992: "Contrast", 41993: "Saturation",
                            41994: "Sharpness", 41996: "SubjectDistanceRange", 42016: "ImageUniqueID"
                        }

                        # Organize EXIF data by categories
                        camera_info = {}
                        shooting_info = {}
                        image_info = {}
                        datetime_info = {}
                        other_info = {}

                        for tag_id, value in exif_data.items():
                            tag_name = exif_tags.get(tag_id, f"Tag {tag_id}")

                            # Format values appropriately
                            if isinstance(value, bytes):
                                try:
                                    value = value.decode('utf-8', errors='ignore')
                                except:
                                    value = str(value)

                            # Categorize tags
                            if tag_name in ["Make", "Model", "Software", "LensModel"]:
                                camera_info[tag_name] = value
                            elif tag_name in ["ExposureTime", "FNumber", "ISOSpeedRatings", "FocalLength",
                                              "Flash", "ExposureMode", "WhiteBalance", "MeteringMode"]:
                                shooting_info[tag_name] = value
                            elif tag_name in ["ImageWidth", "ImageLength", "XResolution", "YResolution",
                                              "ColorSpace", "Orientation"]:
                                image_info[tag_name] = value
                            elif tag_name in ["DateTime", "DateTimeOriginal", "DateTimeDigitized"]:
                                datetime_info[tag_name] = value
                            else:
                                other_info[tag_name] = value

                        # Display organized EXIF data
                        if camera_info:
                            st.write("**📷 Camera Information**")
                            for tag, value in camera_info.items():
                                st.write(f"• **{tag}:** {value}")
                            st.write("")

                        if shooting_info:
                            st.write("**⚙️ Shooting Parameters**")
                            for tag, value in shooting_info.items():
                                # Format specific values for better readability
                                if tag == "ExposureTime":
                                    if isinstance(value, tuple) and len(value) == 2:
                                        exposure = value[0] / value[1] if value[1] != 0 else value[0]
                                        if exposure < 1:
                                            st.write(f"• **Shutter Speed:** 1/{int(1 / exposure)}s")
                                        else:
                                            st.write(f"• **Shutter Speed:** {exposure}s")
                                    else:
                                        st.write(f"• **{tag}:** {value}")
                                elif tag == "FNumber":
                                    if isinstance(value, tuple) and len(value) == 2:
                                        f_number = value[0] / value[1] if value[1] != 0 else value[0]
                                        st.write(f"• **Aperture:** f/{f_number:.1f}")
                                    else:
                                        st.write(f"• **{tag}:** {value}")
                                elif tag == "FocalLength":
                                    if isinstance(value, tuple) and len(value) == 2:
                                        focal = value[0] / value[1] if value[1] != 0 else value[0]
                                        st.write(f"• **Focal Length:** {focal:.0f}mm")
                                    else:
                                        st.write(f"• **{tag}:** {value}")
                                elif tag == "ISOSpeedRatings":
                                    st.write(f"• **ISO:** {value}")
                                else:
                                    st.write(f"• **{tag}:** {value}")
                            st.write("")

                        if image_info:
                            st.write("**🖼️ Image Properties**")
                            for tag, value in image_info.items():
                                if tag == "Orientation":
                                    orientation_map = {
                                        1: "Normal", 2: "Mirrored horizontally", 3: "Rotated 180°",
                                        4: "Mirrored vertically", 5: "Mirrored horizontally and rotated 270°",
                                        6: "Rotated 90°", 7: "Mirrored horizontally and rotated 90°",
                                        8: "Rotated 270°"
                                    }
                                    orientation_desc = orientation_map.get(value, f"Unknown ({value})")
                                    st.write(f"• **{tag}:** {orientation_desc}")
                                else:
                                    st.write(f"• **{tag}:** {value}")
                            st.write("")

                        if datetime_info:
                            st.write("**📅 Date & Time Information**")
                            for tag, value in datetime_info.items():
                                st.write(f"• **{tag}:** {value}")
                            st.write("")

                        # GPS information (if available)
                        gps_info = {}
                        if hasattr(image, '_getexif'):
                            try:
                                exif_dict = image._getexif()
                                if exif_dict and 34853 in exif_dict:  # GPS tag
                                    gps_data = exif_dict[34853]
                                    if gps_data:
                                        st.write("**🌍 GPS Location Data**")
                                        for gps_tag, gps_value in gps_data.items():
                                            st.write(f"• **GPS Tag {gps_tag}:** {gps_value}")
                                        st.write("")
                            except:
                                pass

                        if other_info:
                            with st.expander("Additional EXIF Data"):
                                for tag, value in other_info.items():
                                    st.write(f"• **{tag}:** {value}")

                        # Export EXIF data
                        st.write("**💾 Export EXIF Data**")

                        # Create downloadable EXIF report
                        exif_report = f"EXIF Data Report for {uploaded_file.name}\n"
                        exif_report += "=" * 50 + "\n\n"

                        if camera_info:
                            exif_report += "CAMERA INFORMATION:\n"
                            for tag, value in camera_info.items():
                                exif_report += f"{tag}: {value}\n"
                            exif_report += "\n"

                        if shooting_info:
                            exif_report += "SHOOTING PARAMETERS:\n"
                            for tag, value in shooting_info.items():
                                exif_report += f"{tag}: {value}\n"
                            exif_report += "\n"

                        if image_info:
                            exif_report += "IMAGE PROPERTIES:\n"
                            for tag, value in image_info.items():
                                exif_report += f"{tag}: {value}\n"
                            exif_report += "\n"

                        if datetime_info:
                            exif_report += "DATE & TIME:\n"
                            for tag, value in datetime_info.items():
                                exif_report += f"{tag}: {value}\n"
                            exif_report += "\n"

                        if other_info:
                            exif_report += "OTHER DATA:\n"
                            for tag, value in other_info.items():
                                exif_report += f"{tag}: {value}\n"

                        # Create download link for EXIF report
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        report_filename = f"{base_name}_exif_report.txt"
                        FileHandler.create_download_link(
                            exif_report.encode('utf-8'),
                            report_filename,
                            "text/plain"
                        )

                    else:
                        st.warning(f"No EXIF data found in {uploaded_file.name}")
                        st.info("💡 EXIF data is typically found in:\n"
                                "• JPEG files from digital cameras\n"
                                "• TIFF files with embedded metadata\n"
                                "• RAW files (after conversion)\n\n"
                                "Images edited or processed by some software may have EXIF data removed.")

                    # Display thumbnail
                    st.image(image, caption=f"{uploaded_file.name}", width=300)
                    st.divider()

            except Exception as e:
                st.error(f"Error extracting EXIF data from {uploaded_file.name}: {str(e)}")

    else:
        st.info("📸 **About EXIF Data:**\n\n"
                "EXIF (Exchangeable Image File Format) data contains metadata about how a photo was taken, including:\n\n"
                "• **Camera settings** (aperture, shutter speed, ISO)\n"
                "• **Camera information** (make, model, lens)\n"
                "• **Date and time** the photo was taken\n"
                "• **GPS coordinates** (if location services were enabled)\n"
                "• **Image properties** (dimensions, color space, orientation)\n\n"
                "Upload a JPEG or TIFF file to view its EXIF metadata!")


def image_recognition():
    """Advanced AI-powered image recognition and description"""
    create_tool_header("Image Recognition", "AI-powered comprehensive image analysis and description", "🔍")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        from utils.ai_client import AIClient
        ai_client = AIClient()

        # Analysis options
        st.subheader("Analysis Options")
        analysis_type = st.selectbox("Analysis Type", [
            "General Description",
            "Detailed Analysis",
            "Objects & People",
            "Colors & Composition",
            "Emotions & Mood",
            "Technical Details",
            "Custom Analysis"
        ])

        custom_prompt = ""
        if analysis_type == "Custom Analysis":
            custom_prompt = st.text_area("Custom Analysis Prompt:",
                                         placeholder="Describe what you want to analyze about the image...")

        if st.button("Analyze Images"):
            try:
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    # Display image
                    image = Image.open(uploaded_file)
                    st.subheader(f"Analysis: {uploaded_file.name}")
                    col1, col2 = st.columns([1, 2])

                    with col1:
                        st.image(image, caption=uploaded_file.name, use_column_width=True)

                    with col2:
                        # Create analysis prompt based on type
                        if analysis_type == "General Description":
                            prompt = "Describe this image in detail. What do you see?"
                        elif analysis_type == "Detailed Analysis":
                            prompt = "Provide a comprehensive analysis of this image including objects, people, setting, activities, colors, mood, and any notable details."
                        elif analysis_type == "Objects & People":
                            prompt = "Identify all objects and people in this image. Describe their positions, actions, and relationships."
                        elif analysis_type == "Colors & Composition":
                            prompt = "Analyze the colors, composition, lighting, and artistic elements of this image."
                        elif analysis_type == "Emotions & Mood":
                            prompt = "Describe the emotions, mood, and atmosphere conveyed by this image."
                        elif analysis_type == "Technical Details":
                            prompt = "Analyze the technical aspects of this image including composition, lighting, depth of field, and photographic techniques."
                        else:
                            prompt = custom_prompt or "Analyze this image."

                        # Convert image to bytes for AI analysis
                        img_buffer = io.BytesIO()
                        # Detect original format or use JPEG as fallback
                        img_format = image.format if image.format else 'JPEG'
                        # Ensure RGB mode for JPEG conversion
                        if img_format == 'JPEG' and image.mode != 'RGB':
                            image = image.convert('RGB')
                        image.save(img_buffer, format=img_format)
                        img_bytes = img_buffer.getvalue()

                        # Analyze with AI
                        with st.spinner("Analyzing image..."):
                            analysis = ai_client.analyze_image(img_bytes, prompt, image_format=img_format)

                        st.write("**Analysis Results:**")
                        st.write(analysis)

                    progress_bar.progress((i + 1) / len(uploaded_files))
                    st.markdown("---")

                st.success("✅ Image recognition analysis completed!")

            except Exception as e:
                st.error(f"Error during image recognition: {str(e)}")


def scene_analysis():
    """AI-powered scene understanding and context analysis"""
    create_tool_header("Scene Analysis", "Understand image context, environment, and scene composition", "🏞️")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        from utils.ai_client import AIClient
        ai_client = AIClient()

        # Scene analysis options
        st.subheader("Scene Analysis Options")
        analysis_focus = st.multiselect("Analysis Focus", [
            "Environment & Setting",
            "Weather & Lighting",
            "Architecture & Structures",
            "Nature & Landscape",
            "Human Activity",
            "Transportation",
            "Indoor/Outdoor Context",
            "Time of Day",
            "Season & Climate"
        ], default=["Environment & Setting", "Weather & Lighting"])

        include_safety = st.checkbox("Include Safety Assessment", help="Analyze potential safety concerns in the scene")
        include_accessibility = st.checkbox("Include Accessibility Analysis",
                                            help="Assess accessibility features in the scene")

        if st.button("Analyze Scenes"):
            try:
                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    # Display image
                    image = Image.open(uploaded_file)
                    st.subheader(f"Scene Analysis: {uploaded_file.name}")
                    col1, col2 = st.columns([1, 2])

                    with col1:
                        st.image(image, caption=uploaded_file.name, use_column_width=True)

                    with col2:
                        # Build comprehensive scene analysis prompt
                        prompt_parts = ["Analyze this scene in detail, focusing on:"]

                        if "Environment & Setting" in analysis_focus:
                            prompt_parts.append(
                                "- The overall environment and setting (urban, rural, indoor, outdoor, etc.)")
                        if "Weather & Lighting" in analysis_focus:
                            prompt_parts.append(
                                "- Weather conditions and lighting (natural/artificial, time of day indicators)")
                        if "Architecture & Structures" in analysis_focus:
                            prompt_parts.append("- Architectural elements and structures visible")
                        if "Nature & Landscape" in analysis_focus:
                            prompt_parts.append("- Natural elements, vegetation, and landscape features")
                        if "Human Activity" in analysis_focus:
                            prompt_parts.append("- Human activities and interactions occurring in the scene")
                        if "Transportation" in analysis_focus:
                            prompt_parts.append("- Transportation methods and infrastructure visible")
                        if "Indoor/Outdoor Context" in analysis_focus:
                            prompt_parts.append("- Whether this is an indoor or outdoor scene and contextual clues")
                        if "Time of Day" in analysis_focus:
                            prompt_parts.append("- Time of day indicators and temporal context")
                        if "Season & Climate" in analysis_focus:
                            prompt_parts.append("- Seasonal indicators and climate characteristics")

                        if include_safety:
                            prompt_parts.append("- Potential safety concerns or hazards in the scene")
                        if include_accessibility:
                            prompt_parts.append("- Accessibility features or barriers for people with disabilities")

                        prompt = "\n".join(prompt_parts)

                        # Convert image to bytes for AI analysis
                        img_buffer = io.BytesIO()
                        # Detect original format or use JPEG as fallback
                        img_format = image.format if image.format else 'JPEG'
                        # Ensure RGB mode for JPEG conversion
                        if img_format == 'JPEG' and image.mode != 'RGB':
                            image = image.convert('RGB')
                        image.save(img_buffer, format=img_format)
                        img_bytes = img_buffer.getvalue()

                        # Analyze with AI
                        with st.spinner("Analyzing scene..."):
                            analysis = ai_client.analyze_image(img_bytes, prompt, image_format=img_format)

                        st.write("**Scene Analysis Results:**")
                        st.write(analysis)

                    progress_bar.progress((i + 1) / len(uploaded_files))
                    st.markdown("---")

                st.success("✅ Scene analysis completed!")

            except Exception as e:
                st.error(f"Error during scene analysis: {str(e)}")


def ocr_reader():
    """AI-powered optical character recognition for text extraction"""
    create_tool_header("OCR Reader", "Extract and recognize text from images using AI", "📖")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        from utils.ai_client import AIClient
        ai_client = AIClient()

        # OCR options
        st.subheader("OCR Options")
        ocr_mode = st.selectbox("OCR Mode", [
            "Extract All Text",
            "Extract Structured Text",
            "Extract Specific Content",
            "Text Translation",
            "Handwriting Recognition"
        ])

        target_language = ""
        custom_extraction = ""

        if ocr_mode == "Text Translation":
            target_language = st.selectbox("Translate to:", [
                "Spanish", "French", "German", "Italian", "Portuguese",
                "Chinese", "Japanese", "Korean", "Arabic", "Russian",
                "Dutch", "Swedish", "Norwegian", "Other"
            ])
            if target_language == "Other":
                target_language = st.text_input("Specify language:")

        elif ocr_mode == "Extract Specific Content":
            custom_extraction = st.text_area("What to extract:",
                                             placeholder="e.g., phone numbers, email addresses, dates, prices...")

        preserve_formatting = st.checkbox("Preserve Formatting", value=True)
        include_confidence = st.checkbox("Include Confidence Assessment")

        if st.button("Extract Text"):
            try:
                progress_bar = st.progress(0)
                all_extracted_text = []

                for i, uploaded_file in enumerate(uploaded_files):
                    # Display image
                    image = Image.open(uploaded_file)
                    st.subheader(f"OCR Results: {uploaded_file.name}")
                    col1, col2 = st.columns([1, 2])

                    with col1:
                        st.image(image, caption=uploaded_file.name, use_column_width=True)

                    with col2:
                        # Create OCR prompt based on mode
                        if ocr_mode == "Extract All Text":
                            prompt = "Extract all text from this image. Maintain the original structure and formatting as much as possible."
                        elif ocr_mode == "Extract Structured Text":
                            prompt = "Extract all text from this image and organize it in a structured format with headings, paragraphs, and lists as appropriate."
                        elif ocr_mode == "Extract Specific Content":
                            prompt = f"Extract the following specific content from this image: {custom_extraction}. Provide only the requested information."
                        elif ocr_mode == "Text Translation":
                            prompt = f"Extract all text from this image and translate it to {target_language}. Provide both the original text and translation."
                        elif ocr_mode == "Handwriting Recognition":
                            prompt = "This image contains handwritten text. Please extract and transcribe all handwritten content as accurately as possible."
                        else:
                            prompt = "Extract all text from this image."

                        if preserve_formatting:
                            prompt += " Preserve the original formatting, spacing, and structure of the text."

                        if include_confidence:
                            prompt += " Also provide a confidence assessment for the text recognition accuracy."

                        # Convert image to bytes for AI analysis
                        img_buffer = io.BytesIO()
                        # Detect original format or use JPEG as fallback
                        img_format = image.format if image.format else 'JPEG'
                        # Ensure RGB mode for JPEG conversion
                        if img_format == 'JPEG' and image.mode != 'RGB':
                            image = image.convert('RGB')
                        image.save(img_buffer, format=img_format)
                        img_bytes = img_buffer.getvalue()

                        # Extract text with AI
                        with st.spinner("Extracting text..."):
                            extracted_text = ai_client.analyze_image(img_bytes, prompt, image_format=img_format)

                        st.write("**Extracted Text:**")
                        st.text_area("", value=extracted_text, height=300, key=f"ocr_{i}")

                        # Add to combined results
                        all_extracted_text.append(f"=== {uploaded_file.name} ===\n{extracted_text}\n\n")

                    progress_bar.progress((i + 1) / len(uploaded_files))
                    st.markdown("---")

                # Create download link for combined results
                if len(uploaded_files) > 1:
                    combined_text = "\n".join(all_extracted_text)
                    FileHandler.create_download_link(
                        combined_text.encode('utf-8'),
                        "extracted_text_combined.txt",
                        "text/plain"
                    )
                    st.success("✅ Text extraction completed! Download link available above.")
                else:
                    FileHandler.create_download_link(
                        all_extracted_text[0].encode('utf-8'),
                        "extracted_text.txt",
                        "text/plain"
                    )
                    st.success("✅ Text extraction completed!")

            except Exception as e:
                st.error(f"Error during OCR processing: {str(e)}")


def visual_search():
    """AI-powered visual search and image similarity analysis"""
    create_tool_header("Visual Search", "Find similar images and analyze visual patterns", "🎯")

    st.subheader("Visual Search Options")
    search_mode = st.selectbox("Search Mode", [
        "Describe Visual Elements",
        "Find Similar Styles",
        "Color Pattern Analysis",
        "Object Recognition Comparison",
        "Artistic Style Analysis",
        "Visual Similarity Assessment"
    ])

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
                                              accept_multiple=True)

    if uploaded_files:
        from utils.ai_client import AIClient
        ai_client = AIClient()

        # Additional options based on search mode
        if search_mode == "Visual Similarity Assessment" and len(uploaded_files) > 1:
            st.info("Multiple images detected - will compare similarity between uploaded images")

        include_technical = st.checkbox("Include Technical Analysis", help="Add technical visual analysis")
        include_suggestions = st.checkbox("Include Search Suggestions",
                                          help="Provide suggestions for finding similar images")

        if st.button("Analyze Visual Patterns"):
            try:
                progress_bar = st.progress(0)

                if search_mode == "Visual Similarity Assessment" and len(uploaded_files) > 1:
                    # Compare multiple images
                    st.subheader("Visual Similarity Analysis")

                    images = []
                    image_names = []
                    for uploaded_file in uploaded_files:
                        image = Image.open(uploaded_file)
                        images.append(image)
                        image_names.append(uploaded_file.name)

                    # Display all images
                    cols = st.columns(min(len(images), 4))
                    for i, (image, name) in enumerate(zip(images, image_names)):
                        with cols[i % 4]:
                            st.image(image, caption=name, use_column_width=True)

                    # Create comparison prompt
                    prompt = f"""Compare these {len(images)} images and analyze their visual similarity. For each pair of images, describe:
                    1. Visual similarities (colors, composition, subjects, style)
                    2. Key differences 
                    3. Overall similarity score (1-10)
                    4. What makes them similar or different

                    Image names: {', '.join(image_names)}"""

                    if include_technical:
                        prompt += "\n\nInclude technical analysis of composition, lighting, color schemes, and visual techniques."

                    # Analyze first image as reference (AI vision models work better with single image analysis)
                    img_buffer = io.BytesIO()
                    images[0].save(img_buffer, format='JPEG')
                    img_bytes = img_buffer.getvalue()

                    enhanced_prompt = prompt + f"\n\nAnalyze the visual characteristics of this first image ({image_names[0]}) and describe what similar images would look like in terms of style, composition, colors, and subject matter."

                    with st.spinner("Analyzing visual similarity..."):
                        similarity_analysis = ai_client.analyze_image(img_bytes, enhanced_prompt)

                    st.write("**Visual Similarity Analysis:**")
                    st.write(similarity_analysis)

                else:
                    # Analyze individual images
                    for i, uploaded_file in enumerate(uploaded_files):
                        image = Image.open(uploaded_file)
                        st.subheader(f"Visual Analysis: {uploaded_file.name}")
                        col1, col2 = st.columns([1, 2])

                        with col1:
                            st.image(image, caption=uploaded_file.name, use_column_width=True)

                        with col2:
                            # Create analysis prompt based on search mode
                            if search_mode == "Describe Visual Elements":
                                prompt = "Describe all visual elements in this image including colors, shapes, textures, patterns, composition, and visual style. Focus on elements that could be used for visual search."
                            elif search_mode == "Find Similar Styles":
                                prompt = "Analyze the artistic and visual style of this image. Describe the style, technique, aesthetic, and what other images with similar styles would look like."
                            elif search_mode == "Color Pattern Analysis":
                                prompt = "Analyze the color patterns, palette, and color relationships in this image. Describe the dominant colors, color harmony, and visual impact of the color scheme."
                            elif search_mode == "Object Recognition Comparison":
                                prompt = "Identify and describe all objects, people, animals, and items in this image. Include their positions, relationships, and how they could be used for visual matching."
                            elif search_mode == "Artistic Style Analysis":
                                prompt = "Analyze the artistic style, technique, and aesthetic qualities of this image. Compare it to known art movements or photographic styles."
                            else:
                                prompt = "Provide a comprehensive visual analysis of this image for search purposes."

                            if include_technical:
                                prompt += "\\n\\nInclude technical analysis of photographic/artistic techniques, composition rules, lighting, and visual effects."

                            if include_suggestions:
                                prompt += "\\n\\nProvide suggestions for search terms and keywords that could help find visually similar images."

                            # Convert image to bytes for AI analysis
                            img_buffer = io.BytesIO()
                            image.save(img_buffer, format='JPEG')
                            img_bytes = img_buffer.getvalue()

                            # Analyze with AI
                            with st.spinner("Analyzing visual patterns..."):
                                analysis = ai_client.analyze_image(img_bytes, prompt)

                            st.write("**Visual Analysis Results:**")
                            st.write(analysis)

                        progress_bar.progress((i + 1) / len(uploaded_files))
                        st.markdown("---")

                st.success("✅ Visual search analysis completed!")

            except Exception as e:
                st.error(f"Error during visual search: {str(e)}")


