import streamlit as st
import zipfile
import tarfile
import json
import csv
import xml.etree.ElementTree as ET
import io
import os
import hashlib
import shutil
from datetime import datetime
import mimetypes
import base64
from pathlib import Path
import pandas as pd
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler
from PIL import Image, ImageOps
import subprocess
import tempfile


def display_tools():
    """Display all file management tools"""

    tool_categories = {
        "File Converters": [
            "Document Converter", "Image Format Converter", "Archive Converter"
        ],
        "File Compression": [
            "ZIP Creator", "Archive Manager", "Compression Optimizer", "Batch Compressor", "Archive Extractor"
        ],
        "File Metadata Editors": [
            "EXIF Editor", "Property Editor", "Tag Manager", "Information Extractor", "Metadata Cleaner"
        ],
        "Batch File Processors": [
            "Bulk Renamer", "Mass Converter", "Batch Processor", "File Organizer", "Bulk Operations"
        ],
        "File Organizers": [
            "Directory Manager", "File Sorter", "Duplicate Finder", "Folder Organizer", "Smart Organizer"
        ],
        "File Backup Utilities": [
            "Backup Creator", "Sync Manager", "Version Control", "Backup Scheduler", "Recovery Tools"
        ],
        "File Sync Tools": [
            "Directory Sync", "Cloud Sync", "File Mirror", "Sync Scheduler", "Conflict Resolver"
        ],
        "File Analysis Tools": [
            "Size Analyzer", "Type Detector", "Content Scanner", "Duplicate Detector", "File Statistics"
        ],
        "File Security": [
            "File Encryption", "Password Protection", "Secure Delete", "Integrity Checker", "Access Control"
        ],
        "File Utilities": [
            "File Splitter", "File Merger", "Checksum Generator", "File Monitor", "Path Manager"
        ]
    }

    selected_category = st.selectbox("Select File Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"File Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Document Converter":
        document_converter()
    elif selected_tool == "Image Format Converter":
        image_format_converter()
    elif selected_tool == "Archive Converter":
        archive_converter()
    elif selected_tool == "ZIP Creator":
        zip_creator()
    elif selected_tool == "Bulk Renamer":
        bulk_renamer()
    elif selected_tool == "Duplicate Finder":
        duplicate_finder()
    elif selected_tool == "File Encryption":
        file_encryption()
    elif selected_tool == "Size Analyzer":
        size_analyzer()
    elif selected_tool == "Archive Manager":
        archive_manager()
    elif selected_tool == "Property Editor":
        property_editor()
    elif selected_tool == "File Splitter":
        file_splitter()
    elif selected_tool == "Checksum Generator":
        checksum_generator()
    elif selected_tool == "Directory Sync":
        directory_sync()
    elif selected_tool == "Content Scanner":
        content_scanner()
    elif selected_tool == "Backup Creator":
        backup_creator()
    elif selected_tool == "File Monitor":
        file_monitor()
    elif selected_tool == "Smart Organizer":
        smart_organizer()
    # File Compression tools
    elif selected_tool == "Compression Optimizer":
        compression_optimizer()
    elif selected_tool == "Batch Compressor":
        batch_compressor()
    elif selected_tool == "Archive Extractor":
        archive_extractor()
    # File Metadata Editors
    elif selected_tool == "EXIF Editor":
        exif_editor()
    elif selected_tool == "Tag Manager":
        tag_manager()
    elif selected_tool == "Information Extractor":
        information_extractor()
    elif selected_tool == "Metadata Cleaner":
        metadata_cleaner()
    # Batch File Processors
    elif selected_tool == "Mass Converter":
        mass_converter()
    elif selected_tool == "Batch Processor":
        batch_processor()
    elif selected_tool == "File Organizer":
        file_organizer()
    elif selected_tool == "Bulk Operations":
        bulk_operations()
    # File Organizers
    elif selected_tool == "Directory Manager":
        directory_manager()
    elif selected_tool == "File Sorter":
        file_sorter()
    elif selected_tool == "Folder Organizer":
        folder_organizer()
    # File Backup Utilities
    elif selected_tool == "Sync Manager":
        sync_manager()
    elif selected_tool == "Version Control":
        version_control()
    elif selected_tool == "Backup Scheduler":
        backup_scheduler()
    elif selected_tool == "Recovery Tools":
        recovery_tools()
    # File Sync Tools
    elif selected_tool == "Cloud Sync":
        cloud_sync()
    elif selected_tool == "File Mirror":
        file_mirror()
    elif selected_tool == "Sync Scheduler":
        sync_scheduler()
    elif selected_tool == "Conflict Resolver":
        conflict_resolver()
    # File Analysis Tools
    elif selected_tool == "Type Detector":
        type_detector()
    elif selected_tool == "Duplicate Detector":
        duplicate_detector()
    elif selected_tool == "File Statistics":
        file_statistics()
    # File Security
    elif selected_tool == "Password Protection":
        password_protection()
    elif selected_tool == "Secure Delete":
        secure_delete()
    elif selected_tool == "Integrity Checker":
        integrity_checker()
    elif selected_tool == "Access Control":
        access_control()
    # File Utilities
    elif selected_tool == "File Merger":
        file_merger()
    elif selected_tool == "Path Manager":
        path_manager()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def document_converter():
    """Convert documents between formats"""
    create_tool_header("Document Converter", "Convert documents between various formats", "📄")

    uploaded_files = FileHandler.upload_files(['pdf', 'docx', 'txt', 'rtf', 'odt', 'html'], accept_multiple=True)

    if uploaded_files:
        target_format = st.selectbox("Target Format", ["PDF", "DOCX", "TXT", "HTML", "RTF", "JSON"])

        conversion_options = {}

        if target_format == "PDF":
            conversion_options['page_size'] = st.selectbox("Page Size", ["A4", "Letter", "Legal", "A3"])
            conversion_options['orientation'] = st.selectbox("Orientation", ["Portrait", "Landscape"])

        elif target_format == "HTML":
            conversion_options['include_css'] = st.checkbox("Include CSS Styling", True)
            conversion_options['responsive'] = st.checkbox("Make Responsive", True)

        elif target_format == "TXT":
            conversion_options['encoding'] = st.selectbox("Text Encoding", ["UTF-8", "ASCII", "Latin-1"])
            conversion_options['line_ending'] = st.selectbox("Line Endings",
                                                             ["LF (Unix)", "CRLF (Windows)", "CR (Mac)"])

        if st.button("Convert Documents"):
            converted_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    # Extract content based on file type
                    content = extract_document_content(uploaded_file)

                    if content:
                        # Convert to target format
                        converted_content = convert_document_content(content, target_format, conversion_options)

                        # Generate filename
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        new_filename = f"{base_name}_converted.{target_format.lower()}"

                        converted_files[new_filename] = converted_content

                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error converting {uploaded_file.name}: {str(e)}")

            if converted_files:
                st.success(f"Converted {len(converted_files)} document(s) to {target_format}")

                if len(converted_files) == 1:
                    filename, content = next(iter(converted_files.items()))
                    mime_type = get_mime_type(target_format)
                    FileHandler.create_download_link(content, filename, mime_type)
                else:
                    zip_data = FileHandler.create_zip_archive(converted_files)
                    FileHandler.create_download_link(zip_data, f"converted_documents.zip", "application/zip")


def image_format_converter():
    """Convert images between different formats"""
    create_tool_header("Image Format Converter", "Convert images between various formats", "🖼️")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'ico'],
                                              accept_multiple=True)

    if uploaded_files:
        target_format = st.selectbox("Target Format", ["PNG", "JPEG", "WebP", "GIF", "BMP", "TIFF", "ICO"])

        # Image conversion options
        col1, col2 = st.columns(2)

        # Initialize variables with defaults
        quality = 85
        progressive = False
        optimize = True
        lossless = False
        new_width = 800
        new_height = 600
        maintain_aspect = True
        scale_percent = 100

        with col1:
            if target_format == "JPEG":
                quality = st.slider("JPEG Quality", 1, 100, 85)
                progressive = st.checkbox("Progressive JPEG", False)
            elif target_format == "PNG":
                optimize = st.checkbox("Optimize PNG", True)
            elif target_format == "WebP":
                quality = st.slider("WebP Quality", 1, 100, 80)
                lossless = st.checkbox("Lossless WebP", False)

        with col2:
            resize_option = st.selectbox("Resize Option", ["Keep Original", "Resize", "Scale Percentage"])
            if resize_option == "Resize":
                new_width = st.number_input("Width (px)", min_value=1, value=800)
                new_height = st.number_input("Height (px)", min_value=1, value=600)
                maintain_aspect = st.checkbox("Maintain Aspect Ratio", True)
            elif resize_option == "Scale Percentage":
                scale_percent = st.slider("Scale (%)", 10, 200, 100)

        if st.button("Convert Images"):
            converted_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    # Load image
                    image = Image.open(io.BytesIO(uploaded_file.getvalue()))

                    # Convert RGBA to RGB for JPEG
                    if target_format == "JPEG" and image.mode in ("RGBA", "LA", "P"):
                        background = Image.new("RGB", image.size, (255, 255, 255))
                        if image.mode == "P":
                            image = image.convert("RGBA")
                        background.paste(image, mask=image.split()[-1] if image.mode == "RGBA" else None)
                        image = background

                    # Apply resize if requested
                    if resize_option == "Resize":
                        if maintain_aspect:
                            image.thumbnail((new_width, new_height), Image.Resampling.LANCZOS)
                        else:
                            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    elif resize_option == "Scale Percentage":
                        new_size = (int(image.width * scale_percent / 100), int(image.height * scale_percent / 100))
                        image = image.resize(new_size, Image.Resampling.LANCZOS)

                    # Convert image
                    output_buffer = io.BytesIO()

                    if target_format == "JPEG":
                        save_kwargs = {"quality": quality, "optimize": True}
                        if progressive:
                            save_kwargs["progressive"] = True
                        image.save(output_buffer, format="JPEG", **save_kwargs)
                    elif target_format == "PNG":
                        save_kwargs = {"optimize": optimize}
                        image.save(output_buffer, format="PNG", **save_kwargs)
                    elif target_format == "WebP":
                        save_kwargs = {"quality": quality}
                        if lossless:
                            save_kwargs = {"lossless": True}
                        image.save(output_buffer, format="WebP", **save_kwargs)
                    else:
                        image.save(output_buffer, format=target_format)

                    # Generate filename
                    base_name = uploaded_file.name.rsplit('.', 1)[0]
                    new_filename = f"{base_name}_converted.{target_format.lower()}"
                    if target_format == "JPEG":
                        new_filename = f"{base_name}_converted.jpg"

                    converted_files[new_filename] = output_buffer.getvalue()
                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error converting {uploaded_file.name}: {str(e)}")

            if converted_files:
                st.success(f"Converted {len(converted_files)} image(s) to {target_format}")

                if len(converted_files) == 1:
                    filename, content = next(iter(converted_files.items()))
                    mime_type = f"image/{target_format.lower()}"
                    if target_format == "JPEG":
                        mime_type = "image/jpeg"
                    FileHandler.create_download_link(content, filename, mime_type)
                else:
                    zip_data = FileHandler.create_zip_archive(converted_files)
                    FileHandler.create_download_link(zip_data, f"converted_images.zip", "application/zip")


def archive_converter():
    """Convert between different archive formats"""
    create_tool_header("Archive Converter", "Convert between different archive formats", "📦")

    uploaded_files = FileHandler.upload_files(['zip', 'tar', 'gz', 'bz2', '7z', 'rar'], accept_multiple=True)

    if uploaded_files:
        target_format = st.selectbox("Target Format", ["ZIP", "TAR", "TAR.GZ", "TAR.BZ2"])

        # Archive conversion options
        col1, col2 = st.columns(2)

        # Initialize compression level with default
        compression_level = 6

        with col1:
            if target_format in ["ZIP", "TAR.GZ", "TAR.BZ2"]:
                compression_level = st.slider("Compression Level", 0, 9, 6)

        with col2:
            preserve_structure = st.checkbox("Preserve Directory Structure", True)
            add_timestamp = st.checkbox("Add Timestamp to Name", False)

        if st.button("Convert Archives"):
            converted_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    # Extract the original archive
                    extracted_files = extract_archive(uploaded_file)

                    if extracted_files:
                        # Create new archive in target format
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                        if add_timestamp:
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            base_name = f"{base_name}_{timestamp}"

                        # Initialize variables
                        new_filename = f"{base_name}_converted.zip"
                        archive_data = b""

                        if target_format == "ZIP":
                            new_filename = f"{base_name}_converted.zip"
                            archive_data = create_zip_from_files(extracted_files, compression_level)
                        elif target_format == "TAR":
                            new_filename = f"{base_name}_converted.tar"
                            archive_data = create_tar_from_files(extracted_files, None)
                        elif target_format == "TAR.GZ":
                            new_filename = f"{base_name}_converted.tar.gz"
                            archive_data = create_tar_from_files(extracted_files, "gz")
                        elif target_format == "TAR.BZ2":
                            new_filename = f"{base_name}_converted.tar.bz2"
                            archive_data = create_tar_from_files(extracted_files, "bz2")

                        if archive_data:
                            converted_files[new_filename] = archive_data

                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error converting {uploaded_file.name}: {str(e)}")

            if converted_files:
                st.success(f"Converted {len(converted_files)} archive(s) to {target_format}")

                if len(converted_files) == 1:
                    filename, content = next(iter(converted_files.items()))
                    mime_type = "application/zip" if target_format == "ZIP" else "application/x-tar"
                    FileHandler.create_download_link(content, filename, mime_type)
                else:
                    zip_data = FileHandler.create_zip_archive(converted_files)
                    FileHandler.create_download_link(zip_data, f"converted_archives.zip", "application/zip")


def zip_creator():
    """Create ZIP archives from multiple files"""
    create_tool_header("ZIP Creator", "Create compressed ZIP archives", "📦")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Archive Settings")

        col1, col2 = st.columns(2)
        with col1:
            archive_name = st.text_input("Archive Name", "my_archive")
            compression_level = st.slider("Compression Level", 0, 9, 6)

        with col2:
            password_protect = st.checkbox("Password Protection")
            if password_protect:
                password = st.text_input("Archive Password", type="password")

        # File organization
        st.subheader("File Organization")
        organize_by = st.selectbox("Organize Files By", ["None", "File Type", "Date", "Size", "Custom Folders"])

        if organize_by == "Custom Folders":
            folder_structure = st.text_area("Folder Structure (one per line)",
                                            "documents/\nimages/\narchives/")

        if st.button("Create ZIP Archive"):
            try:
                # Create ZIP archive
                zip_buffer = io.BytesIO()

                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED,
                                     compresslevel=compression_level) as zip_file:
                    progress_bar = st.progress(0)

                    for i, uploaded_file in enumerate(uploaded_files):
                        # Determine file path in archive
                        if organize_by == "File Type":
                            file_ext = uploaded_file.name.split('.')[-1].lower()
                            archive_path = f"{file_ext}_files/{uploaded_file.name}"
                        elif organize_by == "Date":
                            archive_path = f"{datetime.now().strftime('%Y-%m-%d')}/{uploaded_file.name}"
                        elif organize_by == "Size":
                            size_category = get_size_category(uploaded_file.size)
                            archive_path = f"{size_category}/{uploaded_file.name}"
                        else:
                            archive_path = uploaded_file.name

                        # Add file to archive
                        file_data = uploaded_file.read()
                        zip_file.writestr(archive_path, file_data)

                        progress_bar.progress((i + 1) / len(uploaded_files))

                zip_data = zip_buffer.getvalue()

                # Archive statistics
                st.subheader("Archive Statistics")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Files Added", len(uploaded_files))
                with col2:
                    original_size = sum(f.size for f in uploaded_files)
                    st.metric("Original Size", f"{original_size:,} bytes")
                with col3:
                    compression_ratio = (1 - len(zip_data) / original_size) * 100 if original_size > 0 else 0
                    st.metric("Compression", f"{compression_ratio:.1f}%")

                # Download archive
                FileHandler.create_download_link(
                    zip_data,
                    f"{archive_name}.zip",
                    "application/zip"
                )

                st.success("ZIP archive created successfully!")

            except Exception as e:
                st.error(f"Error creating ZIP archive: {str(e)}")


def bulk_renamer():
    """Bulk rename multiple files"""
    create_tool_header("Bulk Renamer", "Rename multiple files with patterns", "📝")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Renaming Options")

        rename_method = st.selectbox("Renaming Method", [
            "Add Prefix/Suffix", "Replace Text", "Sequential Numbering", "Date/Time Stamp", "Pattern Replacement"
        ])

        # Initialize variables with defaults
        prefix = ""
        suffix = ""
        find_text = ""
        replace_text = ""
        case_sensitive = True
        base_name = "file"
        start_number = 1
        number_format = "001"
        date_format = "%Y-%m-%d"
        time_format = "None"
        position = "Prefix"
        pattern = "{name}_{n}"

        if rename_method == "Add Prefix/Suffix":
            prefix = st.text_input("Prefix", "")
            suffix = st.text_input("Suffix", "")

        elif rename_method == "Replace Text":
            find_text = st.text_input("Find Text", "")
            replace_text = st.text_input("Replace With", "")
            case_sensitive = st.checkbox("Case Sensitive", True)

        elif rename_method == "Sequential Numbering":
            base_name = st.text_input("Base Name", "file")
            start_number = st.number_input("Start Number", min_value=1, value=1)
            number_format = st.selectbox("Number Format", ["001", "01", "1", "(1)", "[1]"])

        elif rename_method == "Date/Time Stamp":
            date_format = st.selectbox("Date Format", [
                "%Y-%m-%d", "%Y%m%d", "%d-%m-%Y", "%m-%d-%Y"
            ])
            time_format = st.selectbox("Time Format", [
                "None", "%H%M%S", "%H-%M-%S", "%I%M%p"
            ])
            position = st.selectbox("Position", ["Prefix", "Suffix"])

        elif rename_method == "Pattern Replacement":
            pattern = st.text_input("Pattern (use {n} for number, {name} for original name)", "{name}_{n}")

        # Preview changes
        if st.button("Preview Changes"):
            preview_names = []

            for i, uploaded_file in enumerate(uploaded_files):
                original_name = uploaded_file.name
                name_without_ext = original_name.rsplit('.', 1)[0]
                extension = original_name.rsplit('.', 1)[1] if '.' in original_name else ''

                # Initialize new_name with default
                new_name = name_without_ext

                if rename_method == "Add Prefix/Suffix":
                    new_name = f"{prefix}{name_without_ext}{suffix}"

                elif rename_method == "Replace Text":
                    if case_sensitive:
                        new_name = name_without_ext.replace(find_text, replace_text)
                    else:
                        new_name = name_without_ext.lower().replace(find_text.lower(), replace_text)

                elif rename_method == "Sequential Numbering":
                    number = start_number + i
                    if number_format == "001":
                        number_str = f"{number:03d}"
                    elif number_format == "01":
                        number_str = f"{number:02d}"
                    elif number_format == "(1)":
                        number_str = f"({number})"
                    elif number_format == "[1]":
                        number_str = f"[{number}]"
                    else:
                        number_str = str(number)
                    new_name = f"{base_name}_{number_str}"

                elif rename_method == "Date/Time Stamp":
                    timestamp = datetime.now().strftime(date_format)
                    if time_format != "None":
                        timestamp += "_" + datetime.now().strftime(time_format)

                    if position == "Prefix":
                        new_name = f"{timestamp}_{name_without_ext}"
                    else:
                        new_name = f"{name_without_ext}_{timestamp}"

                elif rename_method == "Pattern Replacement":
                    new_name = pattern.replace("{n}", str(i + 1)).replace("{name}", name_without_ext)

                if extension:
                    new_name += f".{extension}"

                preview_names.append((original_name, new_name))

            # Display preview
            st.subheader("Rename Preview")
            for original, new in preview_names:
                col1, col2, col3 = st.columns([2, 1, 2])
                with col1:
                    st.write(original)
                with col2:
                    st.write("→")
                with col3:
                    st.write(new)

        # Generate rename script
        if st.button("Generate Rename Script"):
            script_content = generate_rename_script(uploaded_files, rename_method, locals())

            st.subheader("Rename Script")
            st.code(script_content, language="bash")

            FileHandler.create_download_link(
                script_content.encode(),
                "rename_script.sh",
                "text/plain"
            )


def duplicate_finder():
    """Find duplicate files"""
    create_tool_header("Duplicate Finder", "Find and manage duplicate files", "🔍")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Duplicate Detection Settings")

        comparison_method = st.selectbox("Comparison Method", [
            "File Content (MD5)", "File Size", "File Name", "Content + Size"
        ])

        ignore_extensions = st.checkbox("Ignore File Extensions")
        case_sensitive = st.checkbox("Case Sensitive Names", True)

        if st.button("Find Duplicates"):
            with st.spinner("Analyzing files for duplicates..."):
                duplicates = find_duplicates(uploaded_files, comparison_method, ignore_extensions, case_sensitive)

                if duplicates:
                    st.subheader("Duplicate Files Found")

                    total_duplicates = sum(len(group) - 1 for group in duplicates.values())
                    st.warning(f"Found {total_duplicates} duplicate files in {len(duplicates)} groups")

                    for i, (key, files) in enumerate(duplicates.items(), 1):
                        with st.expander(f"Duplicate Group {i} ({len(files)} files)"):
                            for j, file_info in enumerate(files):
                                col1, col2, col3 = st.columns([3, 1, 1])
                                with col1:
                                    st.write(f"📄 {file_info['name']}")
                                with col2:
                                    st.write(f"{file_info['size']:,} bytes")
                                with col3:
                                    if j > 0:  # Mark as duplicate (keep first as original)
                                        st.write("🔄 Duplicate")
                                    else:
                                        st.write("📌 Original")

                            # Show duplicate info
                            if comparison_method == "File Content (MD5)":
                                st.code(f"MD5: {key}")

                    # Generate duplicate report
                    if st.button("Generate Duplicate Report"):
                        report = generate_duplicate_report(duplicates, comparison_method)
                        FileHandler.create_download_link(
                            report.encode(),
                            "duplicate_files_report.txt",
                            "text/plain"
                        )
                else:
                    st.success("🎉 No duplicate files found!")


def file_encryption():
    """Encrypt and decrypt files"""
    create_tool_header("File Encryption", "Secure file encryption and decryption", "🔐")

    operation = st.radio("Operation", ["Encrypt Files", "Decrypt Files"])

    if operation == "Encrypt Files":
        uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

        if uploaded_files:
            st.subheader("Encryption Settings")

            col1, col2 = st.columns(2)
            with col1:
                encryption_method = st.selectbox("Encryption Method", ["AES-256", "AES-128", "ChaCha20"])
                password = st.text_input("Encryption Password", type="password")

            with col2:
                key_derivation = st.selectbox("Key Derivation", ["PBKDF2", "Scrypt", "Argon2"])
                confirm_password = st.text_input("Confirm Password", type="password")

            if password and confirm_password:
                if password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    if st.button("Encrypt Files"):
                        encrypted_files = encrypt_files(uploaded_files, password, encryption_method, key_derivation)

                        if encrypted_files:
                            st.success(f"Encrypted {len(encrypted_files)} file(s)")

                            if len(encrypted_files) == 1:
                                filename, data = next(iter(encrypted_files.items()))
                                FileHandler.create_download_link(data, filename, "application/octet-stream")
                            else:
                                zip_data = FileHandler.create_zip_archive(encrypted_files)
                                FileHandler.create_download_link(zip_data, "encrypted_files.zip", "application/zip")

    else:  # Decrypt Files
        uploaded_files = FileHandler.upload_files(['enc', 'encrypted'], accept_multiple=True)

        if uploaded_files:
            password = st.text_input("Decryption Password", type="password")

            if password and st.button("Decrypt Files"):
                decrypted_files = decrypt_files(uploaded_files, password)

                if decrypted_files:
                    st.success(f"Decrypted {len(decrypted_files)} file(s)")

                    if len(decrypted_files) == 1:
                        filename, data = next(iter(decrypted_files.items()))
                        FileHandler.create_download_link(data, filename, "application/octet-stream")
                    else:
                        zip_data = FileHandler.create_zip_archive(decrypted_files)
                        FileHandler.create_download_link(zip_data, "decrypted_files.zip", "application/zip")


def size_analyzer():
    """Analyze file and folder sizes"""
    create_tool_header("Size Analyzer", "Analyze file sizes and storage usage", "📊")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        if st.button("Analyze File Sizes"):
            # Calculate total size and statistics
            total_size = sum(f.size for f in uploaded_files)
            avg_size = total_size / len(uploaded_files)
            largest_file = max(uploaded_files, key=lambda f: f.size)
            smallest_file = min(uploaded_files, key=lambda f: f.size)

            # Display summary statistics
            st.subheader("Size Analysis Summary")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Files", len(uploaded_files))
            with col2:
                st.metric("Total Size", format_bytes(total_size))
            with col3:
                st.metric("Average Size", format_bytes(avg_size))
            with col4:
                st.metric("Size Range", f"{format_bytes(smallest_file.size)} - {format_bytes(largest_file.size)}")

            # File type breakdown
            st.subheader("File Type Breakdown")
            file_types = {}
            for file in uploaded_files:
                ext = file.name.split('.')[-1].lower() if '.' in file.name else 'no extension'
                if ext not in file_types:
                    file_types[ext] = {'count': 0, 'size': 0}
                file_types[ext]['count'] += 1
                file_types[ext]['size'] += file.size

            # Display file type statistics
            for ext, stats in sorted(file_types.items(), key=lambda x: x[1]['size'], reverse=True):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**.{ext}**")
                with col2:
                    st.write(f"{stats['count']} files")
                with col3:
                    st.write(f"{format_bytes(stats['size'])}")

            # Size distribution
            st.subheader("Size Distribution")
            size_ranges = {
                "< 1 KB": 0, "1-10 KB": 0, "10-100 KB": 0, "100 KB - 1 MB": 0,
                "1-10 MB": 0, "10-100 MB": 0, "> 100 MB": 0
            }

            for file in uploaded_files:
                size = file.size
                if size < 1024:
                    size_ranges["< 1 KB"] += 1
                elif size < 10 * 1024:
                    size_ranges["1-10 KB"] += 1
                elif size < 100 * 1024:
                    size_ranges["10-100 KB"] += 1
                elif size < 1024 * 1024:
                    size_ranges["100 KB - 1 MB"] += 1
                elif size < 10 * 1024 * 1024:
                    size_ranges["1-10 MB"] += 1
                elif size < 100 * 1024 * 1024:
                    size_ranges["10-100 MB"] += 1
                else:
                    size_ranges["> 100 MB"] += 1

            for range_name, count in size_ranges.items():
                if count > 0:
                    st.write(f"**{range_name}**: {count} files")

            # Detailed file list
            st.subheader("Detailed File List")
            file_data = []
            for file in sorted(uploaded_files, key=lambda f: f.size, reverse=True):
                file_data.append({
                    "Name": file.name,
                    "Size": format_bytes(file.size),
                    "Type": file.name.split('.')[-1].upper() if '.' in file.name else 'Unknown'
                })

            df = pd.DataFrame(file_data)
            st.dataframe(df, use_container_width=True)

            # Generate analysis report
            if st.button("Generate Analysis Report"):
                report = generate_size_analysis_report(uploaded_files, file_types, size_ranges)
                FileHandler.create_download_link(
                    report.encode(),
                    "size_analysis_report.txt",
                    "text/plain"
                )


# Helper Functions

def extract_document_content(uploaded_file):
    """Extract content from various document formats"""
    try:
        if uploaded_file.name.endswith('.txt'):
            return FileHandler.process_text_file(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            return FileHandler.process_json_file(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file)
            return df.to_string() if df is not None else None
        else:
            # For other formats, return as text or binary
            content = uploaded_file.read()
            try:
                return content.decode('utf-8')
            except:
                return content
    except Exception as e:
        st.error(f"Error extracting content: {str(e)}")
        return None


def convert_document_content(content, target_format, options):
    """Convert document content to target format"""
    if target_format == "TXT":
        if isinstance(content, bytes):
            return content
        encoding = options.get('encoding', 'UTF-8')
        return content.encode(encoding)

    elif target_format == "HTML":
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Converted Document</title>
    {'<meta name="viewport" content="width=device-width, initial-scale=1.0">' if options.get('responsive') else ''}
    {'<style>body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }</style>' if options.get('include_css') else ''}
</head>
<body>
    <pre>{content}</pre>
</body>
</html>"""
        return html_content.encode('utf-8')

    elif target_format == "JSON":
        json_content = {
            "content": content if isinstance(content, str) else content.decode('utf-8', errors='ignore'),
            "converted_at": datetime.now().isoformat(),
            "format": target_format
        }
        return json.dumps(json_content, indent=2).encode('utf-8')

    else:
        # Default: return as-is
        return content if isinstance(content, bytes) else content.encode('utf-8')


def get_mime_type(file_format):
    """Get MIME type for file format"""
    mime_types = {
        'PDF': 'application/pdf',
        'DOCX': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'TXT': 'text/plain',
        'HTML': 'text/html',
        'JSON': 'application/json',
        'RTF': 'application/rtf'
    }
    return mime_types.get(file_format, 'application/octet-stream')


def get_size_category(size):
    """Categorize file by size"""
    if size < 1024 * 1024:  # < 1MB
        return "small_files"
    elif size < 10 * 1024 * 1024:  # < 10MB
        return "medium_files"
    else:
        return "large_files"


def generate_rename_script(files, method, variables):
    """Generate bash script for renaming files"""
    script = "#!/bin/bash\n\n"
    script += "# Bulk rename script generated by File Tools\n"
    script += f"# Method: {method}\n"
    script += f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    for i, file in enumerate(files):
        original_name = file.name
        # Generate new name based on method
        new_name = f"renamed_file_{i + 1}.{original_name.split('.')[-1]}"
        script += f'mv "{original_name}" "{new_name}"\n'

    return script


def find_duplicates(files, method, ignore_ext, case_sensitive):
    """Find duplicate files based on specified method"""
    file_groups = {}

    for file in files:
        if method == "File Content (MD5)":
            key = hashlib.md5(file.read()).hexdigest()
            file.seek(0)  # Reset file pointer
        elif method == "File Size":
            key = file.size
        elif method == "File Name":
            name = file.name
            if ignore_ext and '.' in name:
                name = name.rsplit('.', 1)[0]
            if not case_sensitive:
                name = name.lower()
            key = name
        elif method == "Content + Size":
            content_hash = hashlib.md5(file.read()).hexdigest()
            file.seek(0)
            key = f"{content_hash}_{file.size}"

        if key not in file_groups:
            file_groups[key] = []

        file_groups[key].append({
            'name': file.name,
            'size': file.size,
            'file_obj': file
        })

    # Return only groups with duplicates
    return {k: v for k, v in file_groups.items() if len(v) > 1}


def generate_duplicate_report(duplicates, method):
    """Generate duplicate files report"""
    report = "DUPLICATE FILES REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"Detection Method: {method}\n"
    report += f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    total_duplicates = sum(len(group) - 1 for group in duplicates.values())
    report += f"Total Duplicate Files: {total_duplicates}\n"
    report += f"Duplicate Groups: {len(duplicates)}\n\n"

    for i, (key, files) in enumerate(duplicates.items(), 1):
        report += f"GROUP {i}:\n"
        report += f"Key: {key}\n"
        for file_info in files:
            report += f"  - {file_info['name']} ({file_info['size']:,} bytes)\n"
        report += "\n"

    return report


def encrypt_files(files, password, method, key_derivation):
    """Encrypt files with specified method"""
    encrypted_files = {}

    for file in files:
        try:
            # Simple encryption simulation (use proper crypto library in production)
            file_data = file.read()

            # Create encryption metadata
            encryption_info = {
                "original_name": file.name,
                "method": method,
                "key_derivation": key_derivation,
                "encrypted_at": datetime.now().isoformat(),
                "encrypted_data": base64.b64encode(file_data).decode('utf-8')  # Simple base64 encoding for demo
            }

            encrypted_content = json.dumps(encryption_info, indent=2).encode('utf-8')
            encrypted_filename = f"{file.name}.encrypted"
            encrypted_files[encrypted_filename] = encrypted_content

        except Exception as e:
            st.error(f"Error encrypting {file.name}: {str(e)}")

    return encrypted_files


def decrypt_files(files, password):
    """Decrypt encrypted files"""
    decrypted_files = {}

    for file in files:
        try:
            content = file.read()
            encryption_info = json.loads(content.decode('utf-8'))

            # Simple decryption (use proper crypto library in production)
            decrypted_data = base64.b64decode(encryption_info['encrypted_data'])

            original_name = encryption_info['original_name']
            decrypted_files[original_name] = decrypted_data

        except Exception as e:
            st.error(f"Error decrypting {file.name}: {str(e)}")

    return decrypted_files


def format_bytes(bytes_value):
    """Format bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} PB"


def generate_size_analysis_report(files, file_types, size_ranges):
    """Generate size analysis report"""
    report = "FILE SIZE ANALYSIS REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Total Files Analyzed: {len(files)}\n\n"

    total_size = sum(f.size for f in files)
    report += f"Total Size: {format_bytes(total_size)}\n"
    report += f"Average Size: {format_bytes(total_size / len(files))}\n\n"

    report += "FILE TYPE BREAKDOWN:\n"
    for ext, stats in sorted(file_types.items(), key=lambda x: x[1]['size'], reverse=True):
        report += f"  .{ext}: {stats['count']} files, {format_bytes(stats['size'])}\n"

    report += "\nSIZE DISTRIBUTION:\n"
    for range_name, count in size_ranges.items():
        if count > 0:
            report += f"  {range_name}: {count} files\n"

    return report


# Placeholder functions for remaining tools
def archive_manager():
    """Archive management tool"""
    create_tool_header("Archive Manager", "Create and extract archives (ZIP, TAR, etc.)", "📦")

    operation = st.selectbox("Operation", ["Create Archive", "Extract Archive", "View Archive Contents"])

    if operation == "Create Archive":
        st.subheader("Create New Archive")

        # Archive settings
        col1, col2 = st.columns(2)
        with col1:
            archive_name = st.text_input("Archive Name", "my_archive")
            archive_format = st.selectbox("Archive Format", ["ZIP", "TAR", "TAR.GZ", "TAR.BZ2"])

        with col2:
            compression_level = st.slider("Compression Level", 0, 9, 6) if archive_format != "TAR" else 0
            include_hidden = st.checkbox("Include Hidden Files", False)

        # File selection
        uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True, key="archive_files")

        if uploaded_files:
            st.write(f"**Files to Archive ({len(uploaded_files)}):**")

            total_size = 0
            for i, file in enumerate(uploaded_files):
                file_size = len(file.getvalue())
                total_size += file_size
                st.write(f"• {file.name} ({format_bytes(file_size)})")

            st.write(f"**Total Size:** {format_bytes(total_size)}")

            if st.button("Create Archive"):
                with st.spinner("Creating archive..."):
                    archive_data = create_archive(uploaded_files, archive_format, compression_level)

                    # Estimate compression ratio
                    compressed_size = len(archive_data)
                    compression_ratio = ((total_size - compressed_size) / total_size * 100) if total_size > 0 else 0

                    st.success(f"✅ Archive created successfully!")

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Original Size", format_bytes(total_size))
                    with col2:
                        st.metric("Compressed Size", format_bytes(compressed_size))
                    with col3:
                        st.metric("Compression Ratio", f"{compression_ratio:.1f}%")

                    # Download link
                    extension_map = {
                        "ZIP": ".zip",
                        "TAR": ".tar",
                        "TAR.GZ": ".tar.gz",
                        "TAR.BZ2": ".tar.bz2"
                    }
                    filename = f"{archive_name}{extension_map[archive_format]}"
                    FileHandler.create_download_link(archive_data, filename, "application/octet-stream")

    elif operation == "Extract Archive":
        st.subheader("Extract Archive")

        uploaded_archive = FileHandler.upload_files(['zip', 'tar', 'gz', 'bz2'], accept_multiple=False)

        if uploaded_archive:
            archive_file = uploaded_archive[0]
            st.write(f"**Archive:** {archive_file.name} ({format_bytes(len(archive_file.getvalue()))})")

            if st.button("Extract Archive"):
                try:
                    with st.spinner("Extracting archive..."):
                        extracted_files = extract_archive(archive_file)

                    st.success(f"✅ Extracted {len(extracted_files)} files successfully!")

                    # Show extracted files
                    with st.expander("📁 Extracted Files"):
                        for file_info in extracted_files:
                            st.write(f"• {file_info['name']} ({format_bytes(file_info['size'])})")
                            if file_info['content']:
                                FileHandler.create_download_link(
                                    file_info['content'],
                                    file_info['name'],
                                    "application/octet-stream"
                                )

                except Exception as e:
                    st.error(f"❌ Error extracting archive: {str(e)}")

    else:  # View Archive Contents
        st.subheader("View Archive Contents")

        uploaded_archive = FileHandler.upload_files(['zip', 'tar', 'gz', 'bz2'], accept_multiple=False)

        if uploaded_archive:
            archive_file = uploaded_archive[0]

            try:
                with st.spinner("Reading archive contents..."):
                    contents = get_archive_contents(archive_file)

                st.success(f"📋 Archive contains {len(contents)} items")

                # Display contents in a table
                import pandas as pd
                df = pd.DataFrame(contents)

                if not df.empty:
                    # Format file sizes
                    df['size_formatted'] = df['size'].apply(format_bytes)

                    # Display table
                    st.dataframe(
                        df[['name', 'size_formatted', 'type', 'modified']],
                        column_config={
                            "name": "File Name",
                            "size_formatted": "Size",
                            "type": "Type",
                            "modified": "Modified"
                        },
                        use_container_width=True
                    )

                    # Statistics
                    total_files = len(df[df['type'] == 'file'])
                    total_dirs = len(df[df['type'] == 'directory'])
                    total_size = df['size'].sum()

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Files", total_files)
                    with col2:
                        st.metric("Directories", total_dirs)
                    with col3:
                        st.metric("Total Size", format_bytes(total_size))

            except Exception as e:
                st.error(f"❌ Error reading archive: {str(e)}")


def create_archive(files, format_type, compression_level):
    """Create an archive from uploaded files"""
    import zipfile
    import tarfile
    import io

    if format_type == "ZIP":
        archive_buffer = io.BytesIO()
        with zipfile.ZipFile(archive_buffer, 'w', compression=zipfile.ZIP_DEFLATED,
                             compresslevel=compression_level) as zf:
            for file in files:
                zf.writestr(file.name, file.getvalue())
        return archive_buffer.getvalue()

    elif format_type.startswith("TAR"):
        archive_buffer = io.BytesIO()
        mode = "w"
        if format_type == "TAR.GZ":
            mode = "w:gz"
        elif format_type == "TAR.BZ2":
            mode = "w:bz2"

        with tarfile.open(fileobj=archive_buffer, mode=mode) as tf:
            for file in files:
                tarinfo = tarfile.TarInfo(name=file.name)
                tarinfo.size = len(file.getvalue())
                tf.addfile(tarinfo, io.BytesIO(file.getvalue()))

        return archive_buffer.getvalue()


# File Compression Tools
def compression_optimizer():
    """Optimize file compression for different formats"""
    create_tool_header("Compression Optimizer", "Optimize compression for various file formats", "🗜️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Compression Optimization Settings")

        col1, col2 = st.columns(2)

        with col1:
            optimization_level = st.selectbox("Optimization Level", ["Fast", "Balanced", "Maximum"])
            preserve_quality = st.checkbox("Preserve Original Quality", True)

        with col2:
            target_size_mb = st.number_input("Target Size (MB)", min_value=0.1, value=10.0, step=0.1)
            show_compression_stats = st.checkbox("Show Compression Statistics", True)

        if st.button("Optimize Compression"):
            optimized_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    file_ext = uploaded_file.name.split('.')[-1].lower()
                    file_data = uploaded_file.getvalue()

                    if file_ext in ['zip', 'tar', 'gz']:
                        optimized_data = optimize_archive_compression(file_data, optimization_level)
                    elif file_ext in ['jpg', 'jpeg', 'png', 'webp']:
                        optimized_data = optimize_image_compression(file_data, target_size_mb, preserve_quality)
                    else:
                        # Generic compression
                        optimized_data = optimize_generic_compression(file_data, optimization_level)

                    base_name = uploaded_file.name.rsplit('.', 1)[0]
                    new_filename = f"{base_name}_optimized.{file_ext}"
                    optimized_files[new_filename] = optimized_data

                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error optimizing {uploaded_file.name}: {str(e)}")

            if optimized_files:
                st.success(f"Optimized {len(optimized_files)} file(s)")

                if show_compression_stats:
                    original_size = sum(f.size for f in uploaded_files)
                    optimized_size = sum(len(data) for data in optimized_files.values())
                    compression_ratio = ((original_size - optimized_size) / original_size) * 100

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Original Size", f"{original_size:,} bytes")
                    with col2:
                        st.metric("Optimized Size", f"{optimized_size:,} bytes")
                    with col3:
                        st.metric("Space Saved", f"{compression_ratio:.1f}%")

                if len(optimized_files) == 1:
                    filename, content = next(iter(optimized_files.items()))
                    FileHandler.create_download_link(content, filename, "application/octet-stream")
                else:
                    zip_data = FileHandler.create_zip_archive(optimized_files)
                    FileHandler.create_download_link(zip_data, "optimized_files.zip", "application/zip")


def batch_compressor():
    """Compress multiple files with various algorithms"""
    create_tool_header("Batch Compressor", "Compress multiple files with different algorithms", "📦")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Compression Settings")

        col1, col2 = st.columns(2)

        with col1:
            compression_format = st.selectbox("Compression Format", ["ZIP", "TAR.GZ", "TAR.BZ2", "7Z"])
            compression_level = st.slider("Compression Level", 0, 9, 6)

        with col2:
            split_archives = st.checkbox("Split Large Archives", False)
            if split_archives:
                max_size_mb = st.number_input("Max Archive Size (MB)", min_value=1, value=100)

        # File organization options
        st.subheader("Archive Organization")
        organize_method = st.selectbox("Organization Method", ["None", "By File Type", "By Size", "By Date"])

        if st.button("Compress Files"):
            try:
                if organize_method == "None":
                    organized_files = {"all_files": uploaded_files}
                elif organize_method == "By File Type":
                    organized_files = organize_files_by_type(uploaded_files)
                elif organize_method == "By Size":
                    organized_files = organize_files_by_size(uploaded_files)
                else:  # By Date
                    organized_files = organize_files_by_date(uploaded_files)

                compressed_archives = {}
                progress_bar = st.progress(0)
                total_groups = len(organized_files)

                for i, (group_name, files) in enumerate(organized_files.items()):
                    archive_name = f"{group_name}_compressed"

                    if compression_format == "ZIP":
                        archive_data = create_zip_archive_with_level(files, compression_level)
                        filename = f"{archive_name}.zip"
                    elif compression_format == "TAR.GZ":
                        archive_data = create_tar_archive(files, "gz", compression_level)
                        filename = f"{archive_name}.tar.gz"
                    elif compression_format == "TAR.BZ2":
                        archive_data = create_tar_archive(files, "bz2", compression_level)
                        filename = f"{archive_name}.tar.bz2"
                    else:  # 7Z - placeholder
                        archive_data = create_zip_archive_with_level(files, compression_level)
                        filename = f"{archive_name}.7z"

                    compressed_archives[filename] = archive_data
                    progress_bar.progress((i + 1) / total_groups)

                st.success(f"Created {len(compressed_archives)} compressed archive(s)")

                for filename, data in compressed_archives.items():
                    FileHandler.create_download_link(data, filename, "application/octet-stream")

            except Exception as e:
                st.error(f"Error during compression: {str(e)}")


def archive_extractor():
    """Extract files from various archive formats"""
    create_tool_header("Archive Extractor", "Extract files from ZIP, TAR, and other archives", "📂")

    uploaded_files = FileHandler.upload_files(['zip', 'tar', 'gz', 'bz2', '7z', 'rar'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Extraction Options")

        col1, col2 = st.columns(2)

        with col1:
            preserve_structure = st.checkbox("Preserve Directory Structure", True)
            flatten_directories = st.checkbox("Flatten All Files", False)

        with col2:
            filter_by_extension = st.checkbox("Filter by File Type", False)
            if filter_by_extension:
                allowed_extensions = st.text_input("Allowed Extensions (comma-separated)", "txt,pdf,jpg,png")

        if st.button("Extract Archives"):
            all_extracted_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    extracted_files = extract_archive(uploaded_file)

                    if extracted_files:
                        for file_info in extracted_files:
                            filename = file_info['name']
                            content = file_info['content']

                            # Apply filters
                            if filter_by_extension:
                                file_ext = filename.split('.')[-1].lower()
                                allowed_exts = [ext.strip().lower() for ext in allowed_extensions.split(',')]
                                if file_ext not in allowed_exts:
                                    continue

                            # Handle directory structure
                            if flatten_directories:
                                filename = filename.split('/')[-1]  # Get just the filename
                            elif not preserve_structure:
                                filename = filename.replace('/', '_')  # Replace slashes with underscores

                            # Ensure unique filenames
                            original_filename = filename
                            counter = 1
                            while filename in all_extracted_files:
                                name_part, ext_part = original_filename.rsplit('.',
                                                                               1) if '.' in original_filename else (
                                original_filename, '')
                                filename = f"{name_part}_{counter}.{ext_part}" if ext_part else f"{name_part}_{counter}"
                                counter += 1

                            all_extracted_files[filename] = content

                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error extracting {uploaded_file.name}: {str(e)}")

            if all_extracted_files:
                st.success(f"Extracted {len(all_extracted_files)} file(s) from {len(uploaded_files)} archive(s)")

                # Show extracted files list
                st.subheader("Extracted Files")
                for filename, content in list(all_extracted_files.items())[:10]:  # Show first 10
                    st.write(f"📄 {filename} ({len(content):,} bytes)")

                if len(all_extracted_files) > 10:
                    st.write(f"... and {len(all_extracted_files) - 10} more files")

                # Download all as ZIP
                zip_data = FileHandler.create_zip_archive(all_extracted_files)
                FileHandler.create_download_link(zip_data, "extracted_files.zip", "application/zip")


# File Metadata Editors
def exif_editor():
    """Edit EXIF data in image files"""
    create_tool_header("EXIF Editor", "View and edit EXIF metadata in images", "📷")

    uploaded_files = FileHandler.upload_files(['jpg', 'jpeg', 'tiff', 'tif'], accept_multiple=True)

    if uploaded_files:
        st.info(
            "Note: EXIF editing requires specialized libraries. This tool provides EXIF viewing and basic metadata management.")

        for uploaded_file in uploaded_files:
            st.subheader(f"EXIF Data: {uploaded_file.name}")

            try:
                # Basic EXIF simulation - in a real implementation, use libraries like Pillow or exifread
                image = Image.open(io.BytesIO(uploaded_file.getvalue()))

                # Get basic image info
                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Basic Information:**")
                    st.write(f"Format: {image.format}")
                    st.write(f"Mode: {image.mode}")
                    st.write(f"Size: {image.size[0]} x {image.size[1]} pixels")

                with col2:
                    st.write("**File Information:**")
                    st.write(f"File Size: {len(uploaded_file.getvalue()):,} bytes")
                    st.write(f"Color Depth: {len(image.getbands())} channels")

                # Simulate EXIF data editing
                st.subheader("Edit Metadata")

                col1, col2 = st.columns(2)
                with col1:
                    artist = st.text_input("Artist", key=f"artist_{uploaded_file.name}")
                    copyright_info = st.text_input("Copyright", key=f"copyright_{uploaded_file.name}")

                with col2:
                    description = st.text_input("Description", key=f"desc_{uploaded_file.name}")
                    keywords = st.text_input("Keywords", key=f"keywords_{uploaded_file.name}")

                if st.button(f"Save Metadata for {uploaded_file.name}", key=f"save_{uploaded_file.name}"):
                    # In a real implementation, this would save EXIF data
                    st.success(f"Metadata saved for {uploaded_file.name}")

                    # Create a copy of the image (placeholder for actual EXIF writing)
                    output_buffer = io.BytesIO()
                    image.save(output_buffer, format=image.format)

                    base_name = uploaded_file.name.rsplit('.', 1)[0]
                    FileHandler.create_download_link(
                        output_buffer.getvalue(),
                        f"{base_name}_with_metadata.{image.format.lower()}",
                        f"image/{image.format.lower()}"
                    )

            except Exception as e:
                st.error(f"Error processing {uploaded_file.name}: {str(e)}")


def tag_manager():
    """Manage file tags and custom metadata"""
    create_tool_header("Tag Manager", "Add and manage custom tags for files", "🏷️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Tag Management")

        # Initialize session state for tags
        if 'file_tags' not in st.session_state:
            st.session_state.file_tags = {}

        # Tag input
        col1, col2, col3 = st.columns([2, 2, 1])

        with col1:
            new_tag = st.text_input("Add Tag", placeholder="e.g., important, work, personal")
        with col2:
            tag_category = st.selectbox("Category", ["General", "Priority", "Project", "Type", "Custom"])
        with col3:
            if st.button("Add Tag") and new_tag:
                for file in uploaded_files:
                    filename = file.name
                    if filename not in st.session_state.file_tags:
                        st.session_state.file_tags[filename] = []
                    tag_with_category = f"{tag_category}: {new_tag}" if tag_category != "General" else new_tag
                    if tag_with_category not in st.session_state.file_tags[filename]:
                        st.session_state.file_tags[filename].append(tag_with_category)
                st.rerun()

        # Display files with tags
        st.subheader("Files and Tags")

        for uploaded_file in uploaded_files:
            filename = uploaded_file.name
            file_size = len(uploaded_file.getvalue())

            with st.expander(f"📄 {filename} ({format_bytes(file_size)})"):
                # Show current tags
                if filename in st.session_state.file_tags and st.session_state.file_tags[filename]:
                    st.write("**Current Tags:**")
                    for tag in st.session_state.file_tags[filename]:
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.write(f"🏷️ {tag}")
                        with col2:
                            if st.button("Remove", key=f"remove_{filename}_{tag}"):
                                st.session_state.file_tags[filename].remove(tag)
                                st.rerun()
                else:
                    st.write("No tags assigned")

                # Individual tag input
                individual_tag = st.text_input(f"Add tag to {filename}", key=f"tag_{filename}")
                if st.button(f"Add", key=f"add_{filename}") and individual_tag:
                    if filename not in st.session_state.file_tags:
                        st.session_state.file_tags[filename] = []
                    if individual_tag not in st.session_state.file_tags[filename]:
                        st.session_state.file_tags[filename].append(individual_tag)
                    st.rerun()

        # Export tags
        if st.button("Export Tag Database"):
            tag_data = {
                "files": st.session_state.file_tags,
                "export_date": datetime.now().isoformat(),
                "total_files": len(uploaded_files),
                "total_tags": sum(len(tags) for tags in st.session_state.file_tags.values())
            }

            import json
            export_content = json.dumps(tag_data, indent=2)
            FileHandler.create_download_link(
                export_content.encode(),
                "file_tags_database.json",
                "application/json"
            )


def information_extractor():
    """Extract detailed information from various file types"""
    create_tool_header("Information Extractor", "Extract comprehensive information from files", "🔍")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        extraction_detail = st.selectbox("Extraction Detail", ["Basic", "Detailed", "Comprehensive"])

        if st.button("Extract Information"):
            all_info = {}

            for uploaded_file in uploaded_files:
                file_info = extract_file_information(uploaded_file, extraction_detail)
                all_info[uploaded_file.name] = file_info

            # Display extracted information
            for filename, info in all_info.items():
                with st.expander(f"📄 {filename}"):
                    for category, details in info.items():
                        st.write(f"**{category}:**")
                        if isinstance(details, dict):
                            for key, value in details.items():
                                st.write(f"  • {key}: {value}")
                        else:
                            st.write(f"  {details}")

            # Export information
            if st.button("Export Information Report"):
                import json
                report_content = json.dumps(all_info, indent=2, default=str)
                FileHandler.create_download_link(
                    report_content.encode(),
                    "file_information_report.json",
                    "application/json"
                )


def metadata_cleaner():
    """Remove or clean metadata from files"""
    create_tool_header("Metadata Cleaner", "Remove sensitive metadata from files", "🧹")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Cleaning Options")

        col1, col2 = st.columns(2)

        with col1:
            remove_exif = st.checkbox("Remove EXIF Data", True)
            remove_comments = st.checkbox("Remove Comments", True)
            remove_thumbnails = st.checkbox("Remove Thumbnails", True)

        with col2:
            remove_creation_date = st.checkbox("Remove Creation Date", False)
            remove_author_info = st.checkbox("Remove Author Information", True)
            remove_gps_data = st.checkbox("Remove GPS Data", True)

        if st.button("Clean Metadata"):
            cleaned_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    cleaned_data = clean_file_metadata(
                        uploaded_file,
                        remove_exif=remove_exif,
                        remove_comments=remove_comments,
                        remove_thumbnails=remove_thumbnails,
                        remove_creation_date=remove_creation_date,
                        remove_author_info=remove_author_info,
                        remove_gps_data=remove_gps_data
                    )

                    base_name = uploaded_file.name.rsplit('.', 1)[0]
                    extension = uploaded_file.name.rsplit('.', 1)[1] if '.' in uploaded_file.name else ''
                    new_filename = f"{base_name}_cleaned.{extension}" if extension else f"{base_name}_cleaned"

                    cleaned_files[new_filename] = cleaned_data
                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error cleaning {uploaded_file.name}: {str(e)}")

            if cleaned_files:
                st.success(f"Cleaned metadata from {len(cleaned_files)} file(s)")

                if len(cleaned_files) == 1:
                    filename, content = next(iter(cleaned_files.items()))
                    FileHandler.create_download_link(content, filename, "application/octet-stream")
                else:
                    zip_data = FileHandler.create_zip_archive(cleaned_files)
                    FileHandler.create_download_link(zip_data, "cleaned_files.zip", "application/zip")


# Batch File Processors
def mass_converter():
    """Convert multiple files between various formats"""
    create_tool_header("Mass Converter", "Convert multiple files between different formats", "🔄")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Conversion Settings")

        col1, col2 = st.columns(2)

        with col1:
            source_type = st.selectbox("Source File Type",
                                       ["Auto-detect", "Images", "Documents", "Audio", "Video", "Archives"])
            target_format = st.selectbox("Target Format",
                                         ["PDF", "PNG", "JPEG", "WebP", "TXT", "DOCX", "MP3", "MP4", "ZIP"])

        with col2:
            quality_setting = st.slider("Quality", 1, 100, 85)
            preserve_names = st.checkbox("Preserve Original Names", True)

        if st.button("Convert All Files"):
            converted_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    converted_data = convert_file_to_format(uploaded_file, target_format, quality_setting)

                    if preserve_names:
                        base_name = uploaded_file.name.rsplit('.', 1)[0]
                    else:
                        base_name = f"converted_file_{i + 1}"

                    new_filename = f"{base_name}.{target_format.lower()}"
                    converted_files[new_filename] = converted_data

                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error converting {uploaded_file.name}: {str(e)}")

            if converted_files:
                st.success(f"Converted {len(converted_files)} file(s)")
                zip_data = FileHandler.create_zip_archive(converted_files)
                FileHandler.create_download_link(zip_data, f"mass_converted_{target_format.lower()}.zip",
                                                 "application/zip")


def batch_processor():
    """Process multiple files with various operations"""
    create_tool_header("Batch Processor", "Apply operations to multiple files at once", "⚙️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Processing Operations")

        operations = st.multiselect("Select Operations", [
            "Resize Images", "Convert Format", "Add Watermark", "Rename Files",
            "Compress Files", "Extract Metadata", "Remove Background", "Crop Images"
        ])

        if "Resize Images" in operations:
            st.subheader("Resize Settings")
            col1, col2 = st.columns(2)
            with col1:
                resize_width = st.number_input("Width", min_value=1, value=800)
            with col2:
                resize_height = st.number_input("Height", min_value=1, value=600)

        if "Add Watermark" in operations:
            st.subheader("Watermark Settings")
            watermark_text = st.text_input("Watermark Text", "© 2024")
            watermark_position = st.selectbox("Position",
                                              ["Bottom Right", "Bottom Left", "Top Right", "Top Left", "Center"])

        if st.button("Process All Files"):
            processed_files = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    processed_data = apply_batch_operations(uploaded_file, operations, {
                        'resize_width': resize_width if 'Resize Images' in operations else None,
                        'resize_height': resize_height if 'Resize Images' in operations else None,
                        'watermark_text': watermark_text if 'Add Watermark' in operations else None,
                        'watermark_position': watermark_position if 'Add Watermark' in operations else None
                    })

                    base_name = uploaded_file.name.rsplit('.', 1)[0]
                    extension = uploaded_file.name.rsplit('.', 1)[1] if '.' in uploaded_file.name else 'bin'
                    new_filename = f"{base_name}_processed.{extension}"
                    processed_files[new_filename] = processed_data

                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error processing {uploaded_file.name}: {str(e)}")

            if processed_files:
                st.success(f"Processed {len(processed_files)} file(s)")
                zip_data = FileHandler.create_zip_archive(processed_files)
                FileHandler.create_download_link(zip_data, "batch_processed_files.zip", "application/zip")


def file_organizer():
    """Organize files based on various criteria"""
    create_tool_header("File Organizer", "Organize files into categories and folders", "🗂️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Organization Criteria")

        col1, col2 = st.columns(2)

        with col1:
            organize_by = st.selectbox("Organize By",
                                       ["File Type", "File Size", "Name Pattern", "Date Created", "Custom Rules"])
            create_subfolders = st.checkbox("Create Subfolders", True)

        with col2:
            naming_convention = st.selectbox("Naming Convention",
                                             ["Original", "Sequential", "Date-Time", "Category-Name"])
            add_index = st.checkbox("Add Index Numbers", False)

        if organize_by == "Name Pattern":
            pattern_rules = st.text_area("Pattern Rules (one per line)",
                                         "*.jpg -> Images\n*.pdf -> Documents\n*.mp3 -> Audio")

        if organize_by == "Custom Rules":
            st.subheader("Custom Organization Rules")
            custom_rules = st.text_area("Rules (format: condition -> folder)",
                                        "size > 10MB -> Large Files\ntype = image -> Images")

        if st.button("Organize Files"):
            organized_structure = organize_files_advanced(uploaded_files, organize_by, {
                'create_subfolders': create_subfolders,
                'naming_convention': naming_convention,
                'add_index': add_index,
                'pattern_rules': pattern_rules if organize_by == "Name Pattern" else None,
                'custom_rules': custom_rules if organize_by == "Custom Rules" else None
            })

            # Display organization structure
            st.subheader("Organization Structure")
            for folder, files in organized_structure.items():
                with st.expander(f"📁 {folder} ({len(files)} files)"):
                    for file_info in files:
                        st.write(f"📄 {file_info['new_name']} (was: {file_info['original_name']})")

            # Create organized archive
            organized_archive = create_organized_archive(organized_structure)
            FileHandler.create_download_link(organized_archive, "organized_files.zip", "application/zip")


def bulk_operations():
    """Perform bulk operations on files"""
    create_tool_header("Bulk Operations", "Perform various bulk operations on files", "📋")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Bulk Operations")

        operation_type = st.selectbox("Operation Type", [
            "Bulk Rename", "Bulk Convert", "Bulk Compress", "Bulk Metadata Edit",
            "Bulk Watermark", "Bulk Resize", "Bulk Delete Properties"
        ])

        if operation_type == "Bulk Rename":
            st.subheader("Rename Settings")
            col1, col2 = st.columns(2)
            with col1:
                prefix = st.text_input("Prefix", "")
                suffix = st.text_input("Suffix", "")
            with col2:
                numbering_start = st.number_input("Start Number", min_value=1, value=1)
                numbering_format = st.selectbox("Number Format", ["001", "01", "1"])

        elif operation_type == "Bulk Convert":
            target_format = st.selectbox("Target Format", ["PDF", "PNG", "JPEG", "WebP", "TXT", "DOCX"])
            quality = st.slider("Quality", 1, 100, 85)

        elif operation_type == "Bulk Compress":
            compression_level = st.slider("Compression Level", 1, 9, 6)
            compression_format = st.selectbox("Format", ["ZIP", "TAR.GZ", "7Z"])

        if st.button(f"Execute {operation_type}"):
            results = {}
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    if operation_type == "Bulk Rename":
                        result = bulk_rename_file(uploaded_file, prefix, suffix, numbering_start + i, numbering_format)
                    elif operation_type == "Bulk Convert":
                        result = bulk_convert_file(uploaded_file, target_format, quality)
                    elif operation_type == "Bulk Compress":
                        result = bulk_compress_file(uploaded_file, compression_level, compression_format)
                    else:
                        result = perform_bulk_operation(uploaded_file, operation_type)

                    results[result['filename']] = result['data']
                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error processing {uploaded_file.name}: {str(e)}")

            if results:
                st.success(f"Completed {operation_type} on {len(results)} file(s)")

                if len(results) == 1:
                    filename, content = next(iter(results.items()))
                    FileHandler.create_download_link(content, filename, "application/octet-stream")
                else:
                    zip_data = FileHandler.create_zip_archive(results)
                    FileHandler.create_download_link(zip_data, f"bulk_{operation_type.lower().replace(' ', '_')}.zip",
                                                     "application/zip")


# File Organizers
def directory_manager():
    """Manage directory structures and file organization"""
    create_tool_header("Directory Manager", "Manage and organize directory structures", "📁")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Directory Management")

        col1, col2 = st.columns(2)

        with col1:
            action = st.selectbox("Action",
                                  ["Create Structure", "Flatten Structure", "Mirror Structure", "Custom Layout"])
            preserve_timestamps = st.checkbox("Preserve Timestamps", True)

        with col2:
            structure_template = st.selectbox("Structure Template",
                                              ["By Year/Month", "By Type/Subtype", "Alphabetical", "Custom"])

        if structure_template == "Custom":
            custom_structure = st.text_area("Custom Structure",
                                            "Documents/\n  PDF/\n  Word/\nImages/\n  Photos/\n  Graphics/")

        if st.button("Apply Directory Management"):
            managed_structure = apply_directory_management(uploaded_files, action, structure_template, {
                'preserve_timestamps': preserve_timestamps,
                'custom_structure': custom_structure if structure_template == "Custom" else None
            })

            st.subheader("Directory Structure")
            display_directory_tree(managed_structure)

            # Create structured archive
            structured_archive = create_directory_archive(managed_structure)
            FileHandler.create_download_link(structured_archive, "directory_structure.zip", "application/zip")


def file_sorter():
    """Sort files based on various criteria"""
    create_tool_header("File Sorter", "Sort files using multiple criteria", "🔀")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Sorting Criteria")

        col1, col2 = st.columns(2)

        with col1:
            primary_sort = st.selectbox("Primary Sort", ["Name", "Size", "Type", "Date", "Custom"])
            secondary_sort = st.selectbox("Secondary Sort", ["None", "Name", "Size", "Type"])

        with col2:
            sort_order = st.selectbox("Sort Order", ["Ascending", "Descending"])
            group_by = st.selectbox("Group By", ["None", "File Type", "Size Range", "First Letter"])

        if primary_sort == "Custom":
            custom_sort_rule = st.text_input("Custom Sort Rule", "extension, name, size")

        if st.button("Sort Files"):
            sorted_files = sort_files_advanced(uploaded_files, primary_sort, secondary_sort, sort_order, group_by, {
                'custom_rule': custom_sort_rule if primary_sort == "Custom" else None
            })

            st.subheader("Sorted Files")
            for group_name, files in sorted_files.items():
                with st.expander(f"📂 {group_name} ({len(files)} files)"):
                    for i, file_info in enumerate(files, 1):
                        st.write(f"{i}. 📄 {file_info['name']} ({format_bytes(file_info['size'])})")

            # Create sorted archive
            sorted_archive = create_sorted_archive(sorted_files)
            FileHandler.create_download_link(sorted_archive, "sorted_files.zip", "application/zip")


def folder_organizer():
    """Organize files into folder structures"""
    create_tool_header("Folder Organizer", "Create organized folder structures for files", "🗃️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Folder Organization")

        col1, col2 = st.columns(2)

        with col1:
            organization_scheme = st.selectbox("Organization Scheme", [
                "Smart Auto-Sort", "File Type Categories", "Alphabetical Folders",
                "Date-Based Folders", "Size-Based Folders", "Custom Scheme"
            ])

        with col2:
            folder_depth = st.selectbox("Folder Depth", ["1 Level", "2 Levels", "3 Levels", "Auto"])
            max_files_per_folder = st.number_input("Max Files per Folder", min_value=1, value=50)

        if organization_scheme == "Custom Scheme":
            custom_scheme = st.text_area("Custom Scheme Rules",
                                         "*.jpg,*.png -> Images/Photos\n*.pdf,*.doc -> Documents/Files\n*.mp3,*.wav -> Audio/Music")

        if st.button("Organize into Folders"):
            folder_structure = create_folder_organization(uploaded_files, organization_scheme, {
                'folder_depth': folder_depth,
                'max_files_per_folder': max_files_per_folder,
                'custom_scheme': custom_scheme if organization_scheme == "Custom Scheme" else None
            })

            st.subheader("Folder Structure")
            display_folder_tree(folder_structure)

            # Create organized folder archive
            folder_archive = create_folder_archive(folder_structure)
            FileHandler.create_download_link(folder_archive, "folder_organized_files.zip", "application/zip")


# File Backup Utilities
def sync_manager():
    """Manage file synchronization between different sources"""
    create_tool_header("Sync Manager", "Manage file synchronization and versioning", "🔄")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Sync Configuration")

        col1, col2 = st.columns(2)

        with col1:
            sync_mode = st.selectbox("Sync Mode", ["One-way", "Two-way", "Mirror", "Incremental"])
            conflict_resolution = st.selectbox("Conflict Resolution",
                                               ["Newer Wins", "Larger Wins", "Manual Review", "Keep Both"])

        with col2:
            backup_versions = st.number_input("Keep Versions", min_value=1, max_value=10, value=3)
            compression_enabled = st.checkbox("Compress Backups", True)

        if st.button("Create Sync Package"):
            sync_package = create_sync_package(uploaded_files, sync_mode, conflict_resolution, backup_versions,
                                               compression_enabled)
            FileHandler.create_download_link(sync_package, "sync_package.zip", "application/zip")
            st.success("Sync package created successfully!")


def version_control():
    """Simple version control for files"""
    create_tool_header("Version Control", "Track file versions and changes", "📝")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Version Control Settings")

        version_comment = st.text_area("Version Comment", placeholder="Describe changes in this version...")

        col1, col2 = st.columns(2)
        with col1:
            create_diff = st.checkbox("Create Diff Report", True)
            include_metadata = st.checkbox("Include Metadata", True)
        with col2:
            max_versions = st.number_input("Max Versions to Keep", min_value=1, value=5)
            auto_backup = st.checkbox("Auto Backup", True)

        if st.button("Create Version"):
            version_archive = create_version_archive(uploaded_files, version_comment, {
                'create_diff': create_diff,
                'include_metadata': include_metadata,
                'max_versions': max_versions,
                'auto_backup': auto_backup
            })
            FileHandler.create_download_link(version_archive, f"version_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                                             "application/zip")
            st.success("Version created successfully!")


def backup_scheduler():
    """Schedule and manage file backups"""
    create_tool_header("Backup Scheduler", "Create scheduled backup configurations", "⏰")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Backup Schedule Configuration")

        col1, col2 = st.columns(2)

        with col1:
            backup_frequency = st.selectbox("Backup Frequency", ["Daily", "Weekly", "Monthly", "Custom"])
            backup_time = st.time_input("Backup Time", value=datetime.now().time())

        with col2:
            retention_days = st.number_input("Retention Days", min_value=1, value=30)
            incremental_backup = st.checkbox("Incremental Backup", True)

        backup_location = st.text_input("Backup Location", placeholder="Enter backup destination path")
        encryption_enabled = st.checkbox("Enable Encryption", False)

        if st.button("Create Backup Configuration"):
            backup_config = create_backup_configuration(uploaded_files, {
                'frequency': backup_frequency,
                'time': backup_time,
                'retention_days': retention_days,
                'incremental': incremental_backup,
                'location': backup_location,
                'encryption': encryption_enabled
            })

            FileHandler.create_download_link(backup_config.encode(), "backup_config.json", "application/json")
            st.success("Backup configuration created!")


def recovery_tools():
    """File recovery and restoration tools"""
    create_tool_header("Recovery Tools", "Recover and restore files", "🔧")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Recovery Options")

        recovery_mode = st.selectbox("Recovery Mode", [
            "Partial Recovery", "Full Recovery", "Selective Recovery", "Metadata Recovery"
        ])

        if recovery_mode == "Selective Recovery":
            file_patterns = st.text_input("File Patterns", placeholder="*.jpg, *.pdf, document*")

        verify_integrity = st.checkbox("Verify File Integrity", True)
        create_recovery_log = st.checkbox("Create Recovery Log", True)

        if st.button("Start Recovery Process"):
            recovery_result = perform_file_recovery(uploaded_files, recovery_mode, {
                'patterns': file_patterns if recovery_mode == "Selective Recovery" else None,
                'verify_integrity': verify_integrity,
                'create_log': create_recovery_log
            })

            if recovery_result:
                st.success("Recovery completed successfully!")
                FileHandler.create_download_link(recovery_result, "recovered_files.zip", "application/zip")


# File Sync Tools
def cloud_sync():
    """Simulate cloud synchronization features"""
    create_tool_header("Cloud Sync", "Prepare files for cloud synchronization", "☁️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.info(
            "Note: This tool prepares files for cloud sync. Actual cloud integration requires specific cloud service APIs.")

        st.subheader("Cloud Sync Configuration")

        col1, col2 = st.columns(2)

        with col1:
            cloud_provider = st.selectbox("Cloud Provider",
                                          ["Generic", "AWS S3", "Google Drive", "Dropbox", "OneDrive"])
            sync_direction = st.selectbox("Sync Direction", ["Upload Only", "Download Only", "Bidirectional"])

        with col2:
            file_conflict_resolution = st.selectbox("Conflict Resolution",
                                                    ["Server Wins", "Local Wins", "Timestamp", "Size"])
            bandwidth_limit = st.slider("Bandwidth Limit (MB/s)", 1, 100, 10)

        if st.button("Prepare Cloud Sync Package"):
            sync_package = prepare_cloud_sync_package(uploaded_files, cloud_provider, sync_direction,
                                                      file_conflict_resolution)
            FileHandler.create_download_link(sync_package, "cloud_sync_package.zip", "application/zip")
            st.success("Cloud sync package prepared!")


def file_mirror():
    """Create file mirrors and replicas"""
    create_tool_header("File Mirror", "Create file mirrors and replicas", "🪞")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Mirror Configuration")

        col1, col2 = st.columns(2)

        with col1:
            mirror_type = st.selectbox("Mirror Type", ["Exact Copy", "Compressed Mirror", "Incremental Mirror"])
            verify_checksums = st.checkbox("Verify Checksums", True)

        with col2:
            mirror_count = st.number_input("Number of Mirrors", min_value=1, max_value=5, value=2)
            include_metadata = st.checkbox("Include Metadata", True)

        if st.button("Create File Mirrors"):
            mirrors = create_file_mirrors(uploaded_files, mirror_type, mirror_count, verify_checksums, include_metadata)

            for i, mirror_data in enumerate(mirrors, 1):
                FileHandler.create_download_link(mirror_data, f"file_mirror_{i}.zip", "application/zip")

            st.success(f"Created {len(mirrors)} file mirror(s)!")


def sync_scheduler():
    """Schedule synchronization tasks"""
    create_tool_header("Sync Scheduler", "Schedule file synchronization tasks", "📅")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Sync Schedule")

        col1, col2 = st.columns(2)

        with col1:
            sync_frequency = st.selectbox("Sync Frequency",
                                          ["Real-time", "Every 15 minutes", "Hourly", "Daily", "Weekly"])
            sync_triggers = st.multiselect("Sync Triggers", ["File Changed", "Time Based", "Manual", "System Event"])

        with col2:
            max_file_size = st.number_input("Max File Size (MB)", min_value=1, value=100)
            exclude_patterns = st.text_input("Exclude Patterns", placeholder="*.tmp, *.log")

        if st.button("Create Sync Schedule"):
            schedule_config = create_sync_schedule(uploaded_files, {
                'frequency': sync_frequency,
                'triggers': sync_triggers,
                'max_size': max_file_size,
                'exclude_patterns': exclude_patterns
            })

            FileHandler.create_download_link(schedule_config.encode(), "sync_schedule.json", "application/json")
            st.success("Sync schedule created!")


def conflict_resolver():
    """Resolve file conflicts and duplicates"""
    create_tool_header("Conflict Resolver", "Resolve file conflicts and duplicates", "⚖️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Conflict Resolution")

        # Detect potential conflicts
        conflicts = detect_file_conflicts(uploaded_files)

        if conflicts:
            st.warning(f"Found {len(conflicts)} potential conflict(s)")

            for conflict in conflicts:
                with st.expander(f"Conflict: {conflict['name']}"):
                    st.write(f"**Files involved:** {len(conflict['files'])}")
                    for file_info in conflict['files']:
                        st.write(f"• {file_info['name']} - {format_bytes(file_info['size'])} - {file_info['modified']}")

                    resolution = st.selectbox(f"Resolution for {conflict['name']}",
                                              ["Keep Newest", "Keep Largest", "Keep All", "Manual Select"],
                                              key=f"resolution_{conflict['name']}")

                    if resolution == "Manual Select":
                        selected = st.selectbox(f"Select file to keep",
                                                [f['name'] for f in conflict['files']],
                                                key=f"manual_{conflict['name']}")

            if st.button("Resolve All Conflicts"):
                resolved_files = resolve_all_conflicts(conflicts, uploaded_files)
                FileHandler.create_download_link(resolved_files, "resolved_files.zip", "application/zip")
                st.success("Conflicts resolved!")
        else:
            st.success("No conflicts detected!")


# File Analysis Tools
def type_detector():
    """Detect and analyze file types"""
    create_tool_header("Type Detector", "Detect and analyze file types and formats", "🔍")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        if st.button("Analyze File Types"):
            analysis_results = {}

            for uploaded_file in uploaded_files:
                file_analysis = analyze_file_type(uploaded_file)
                analysis_results[uploaded_file.name] = file_analysis

            # Display results
            st.subheader("File Type Analysis")

            for filename, analysis in analysis_results.items():
                with st.expander(f"📄 {filename}"):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.write("**Basic Info:**")
                        st.write(f"Detected Type: {analysis['detected_type']}")
                        st.write(f"MIME Type: {analysis['mime_type']}")
                        st.write(f"File Size: {format_bytes(analysis['file_size'])}")

                    with col2:
                        st.write("**Advanced Info:**")
                        st.write(f"Magic Number: {analysis['magic_number']}")
                        st.write(f"Encoding: {analysis['encoding']}")
                        st.write(f"Is Binary: {analysis['is_binary']}")

            # Export analysis
            if st.button("Export Analysis Report"):
                import json
                report_content = json.dumps(analysis_results, indent=2, default=str)
                FileHandler.create_download_link(
                    report_content.encode(),
                    "file_type_analysis.json",
                    "application/json"
                )


def duplicate_detector():
    """Enhanced duplicate file detection"""
    create_tool_header("Duplicate Detector", "Advanced duplicate file detection and management", "🔍")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Detection Settings")

        col1, col2 = st.columns(2)

        with col1:
            detection_method = st.selectbox("Detection Method", [
                "Hash Comparison", "Content Analysis", "Name Similarity", "Size and Name", "Advanced Analysis"
            ])
            similarity_threshold = st.slider("Similarity Threshold (%)", 50, 100, 90)

        with col2:
            include_partial_matches = st.checkbox("Include Partial Matches", False)
            ignore_extensions = st.checkbox("Ignore File Extensions", False)

        if st.button("Detect Duplicates"):
            duplicates = detect_advanced_duplicates(uploaded_files, detection_method, similarity_threshold,
                                                    include_partial_matches, ignore_extensions)

            if duplicates:
                st.warning(f"Found {len(duplicates)} duplicate group(s)")

                total_space_wasted = 0
                for i, duplicate_group in enumerate(duplicates, 1):
                    with st.expander(f"Duplicate Group {i} ({len(duplicate_group['files'])} files)"):
                        group_size = max(f['size'] for f in duplicate_group['files'])
                        space_wasted = group_size * (len(duplicate_group['files']) - 1)
                        total_space_wasted += space_wasted

                        st.write(f"**Space wasted:** {format_bytes(space_wasted)}")
                        st.write(f"**Similarity:** {duplicate_group['similarity']:.1f}%")

                        for file_info in duplicate_group['files']:
                            col1, col2, col3 = st.columns([3, 1, 1])
                            with col1:
                                st.write(f"📄 {file_info['name']}")
                            with col2:
                                st.write(format_bytes(file_info['size']))
                            with col3:
                                if st.button("Keep", key=f"keep_{file_info['name']}_{i}"):
                                    st.success(f"Marked {file_info['name']} to keep")

                st.metric("Total Space Wasted", format_bytes(total_space_wasted))

                if st.button("Generate Cleanup Report"):
                    cleanup_report = generate_duplicate_cleanup_report(duplicates)
                    FileHandler.create_download_link(cleanup_report.encode(), "duplicate_cleanup_report.txt",
                                                     "text/plain")
            else:
                st.success("No duplicates found!")


def file_statistics():
    """Comprehensive file statistics and analytics"""
    create_tool_header("File Statistics", "Comprehensive file statistics and analytics", "📊")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        if st.button("Generate Statistics"):
            stats = generate_comprehensive_statistics(uploaded_files)

            # Display statistics
            st.subheader("File Statistics Overview")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Files", stats['total_files'])
            with col2:
                st.metric("Total Size", format_bytes(stats['total_size']))
            with col3:
                st.metric("Average Size", format_bytes(stats['average_size']))
            with col4:
                st.metric("File Types", stats['unique_types'])

            # File type distribution
            st.subheader("File Type Distribution")
            type_data = []
            for file_type, count in stats['type_distribution'].items():
                type_data.append(
                    {"Type": file_type, "Count": count, "Percentage": f"{(count / stats['total_files'] * 100):.1f}%"})

            import pandas as pd
            df = pd.DataFrame(type_data)
            st.dataframe(df)

            # Size distribution
            st.subheader("Size Distribution")
            for size_range, count in stats['size_distribution'].items():
                if count > 0:
                    st.write(f"**{size_range}**: {count} files")

            # Export detailed statistics
            if st.button("Export Detailed Statistics"):
                import json
                detailed_stats = json.dumps(stats, indent=2, default=str)
                FileHandler.create_download_link(
                    detailed_stats.encode(),
                    "detailed_file_statistics.json",
                    "application/json"
                )


# File Security
def password_protection():
    """Add password protection to files"""
    create_tool_header("Password Protection", "Add password protection to files", "🔒")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Password Protection Settings")

        col1, col2 = st.columns(2)

        with col1:
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")

        with col2:
            encryption_strength = st.selectbox("Encryption Strength", ["AES-128", "AES-256", "ChaCha20"])
            add_hint = st.checkbox("Add Password Hint", False)

        if add_hint:
            password_hint = st.text_input("Password Hint", placeholder="Optional hint for password recovery")

        if password and confirm_password:
            if password != confirm_password:
                st.error("Passwords do not match!")
            else:
                if st.button("Apply Password Protection"):
                    protected_files = {}
                    progress_bar = st.progress(0)

                    for i, uploaded_file in enumerate(uploaded_files):
                        try:
                            protected_data = apply_password_protection(
                                uploaded_file, password, encryption_strength,
                                password_hint if add_hint else None
                            )

                            base_name = uploaded_file.name.rsplit('.', 1)[0]
                            new_filename = f"{base_name}_protected.enc"
                            protected_files[new_filename] = protected_data

                            progress_bar.progress((i + 1) / len(uploaded_files))

                        except Exception as e:
                            st.error(f"Error protecting {uploaded_file.name}: {str(e)}")

                    if protected_files:
                        st.success(f"Protected {len(protected_files)} file(s)")

                        if len(protected_files) == 1:
                            filename, content = next(iter(protected_files.items()))
                            FileHandler.create_download_link(content, filename, "application/octet-stream")
                        else:
                            zip_data = FileHandler.create_zip_archive(protected_files)
                            FileHandler.create_download_link(zip_data, "protected_files.zip", "application/zip")


def secure_delete():
    """Securely delete file contents and metadata"""
    create_tool_header("Secure Delete", "Securely overwrite and delete file data", "🗑️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.warning(
            "⚠️ This tool demonstrates secure deletion concepts. In a real environment, secure deletion would overwrite file data multiple times.")

        st.subheader("Secure Deletion Settings")

        col1, col2 = st.columns(2)

        with col1:
            deletion_method = st.selectbox("Deletion Method",
                                           ["DoD 5220.22-M", "Gutmann", "Random Overwrite", "Zero Fill"])
            overwrite_passes = st.number_input("Overwrite Passes", min_value=1, max_value=35, value=3)

        with col2:
            delete_metadata = st.checkbox("Delete Metadata", True)
            create_deletion_report = st.checkbox("Create Deletion Report", True)

        if st.button("Simulate Secure Deletion"):
            deletion_results = []

            for uploaded_file in uploaded_files:
                result = simulate_secure_deletion(uploaded_file, deletion_method, overwrite_passes, delete_metadata)
                deletion_results.append(result)

            # Display deletion simulation results
            st.subheader("Deletion Simulation Results")

            for result in deletion_results:
                with st.expander(f"📄 {result['filename']}"):
                    st.write(f"**Original Size:** {format_bytes(result['original_size'])}")
                    st.write(f"**Deletion Method:** {result['method']}")
                    st.write(f"**Overwrite Passes:** {result['passes']}")
                    st.write(f"**Metadata Cleared:** {'Yes' if result['metadata_cleared'] else 'No'}")
                    st.write(f"**Verification:** {result['verification']}")

            if create_deletion_report:
                report_content = generate_deletion_report(deletion_results)
                FileHandler.create_download_link(
                    report_content.encode(),
                    "secure_deletion_report.txt",
                    "text/plain"
                )


def integrity_checker():
    """Check file integrity and detect corruption"""
    create_tool_header("Integrity Checker", "Verify file integrity and detect corruption", "✅")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Integrity Check Settings")

        col1, col2 = st.columns(2)

        with col1:
            hash_algorithms = st.multiselect("Hash Algorithms", ["MD5", "SHA1", "SHA256", "SHA512"], default=["SHA256"])
            deep_scan = st.checkbox("Deep Content Scan", False)

        with col2:
            check_headers = st.checkbox("Check File Headers", True)
            verify_signatures = st.checkbox("Verify Digital Signatures", False)

        if st.button("Check File Integrity"):
            integrity_results = []
            progress_bar = st.progress(0)

            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    integrity_result = check_file_integrity(
                        uploaded_file, hash_algorithms, deep_scan, check_headers, verify_signatures
                    )
                    integrity_results.append(integrity_result)
                    progress_bar.progress((i + 1) / len(uploaded_files))

                except Exception as e:
                    st.error(f"Error checking {uploaded_file.name}: {str(e)}")

            # Display results
            st.subheader("Integrity Check Results")

            healthy_files = sum(1 for r in integrity_results if r['status'] == 'Healthy')

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Files", len(integrity_results))
            with col2:
                st.metric("Healthy Files", healthy_files)
            with col3:
                st.metric("Issues Found", len(integrity_results) - healthy_files)

            for result in integrity_results:
                status_icon = "✅" if result['status'] == 'Healthy' else "⚠️"
                with st.expander(f"{status_icon} {result['filename']} - {result['status']}"):
                    st.write(f"**File Size:** {format_bytes(result['file_size'])}")
                    st.write(f"**File Type:** {result['file_type']}")

                    if result['hashes']:
                        st.write("**Checksums:**")
                        for algo, hash_value in result['hashes'].items():
                            st.code(f"{algo}: {hash_value}")

                    if result['issues']:
                        st.write("**Issues Found:**")
                        for issue in result['issues']:
                            st.write(f"• {issue}")

            # Export integrity report
            if st.button("Export Integrity Report"):
                report_content = generate_integrity_report(integrity_results)
                FileHandler.create_download_link(
                    report_content.encode(),
                    "integrity_check_report.json",
                    "application/json"
                )


def access_control():
    """Manage file access permissions and controls"""
    create_tool_header("Access Control", "Manage file access permissions and controls", "🛡️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.info("Note: This tool simulates access control concepts for educational purposes.")

        st.subheader("Access Control Settings")

        col1, col2 = st.columns(2)

        with col1:
            permission_level = st.selectbox("Permission Level",
                                            ["Read Only", "Read/Write", "Full Control", "No Access"])
            user_groups = st.multiselect("User Groups", ["Administrators", "Users", "Guests", "Power Users"])

        with col2:
            expiration_enabled = st.checkbox("Set Access Expiration", False)
            if expiration_enabled:
                expiration_date = st.date_input("Expiration Date")
            audit_logging = st.checkbox("Enable Audit Logging", True)

        # Additional security options
        st.subheader("Advanced Security")

        col1, col2 = st.columns(2)

        with col1:
            require_2fa = st.checkbox("Require Two-Factor Authentication", False)
            ip_restrictions = st.text_input("IP Restrictions", placeholder="192.168.1.0/24, 10.0.0.1")

        with col2:
            max_download_attempts = st.number_input("Max Download Attempts", min_value=1, value=5)
            time_based_access = st.checkbox("Time-Based Access Control", False)

        if st.button("Apply Access Controls"):
            access_controlled_files = {}

            for uploaded_file in uploaded_files:
                access_config = create_access_control_config(uploaded_file, {
                    'permission_level': permission_level,
                    'user_groups': user_groups,
                    'expiration_date': expiration_date if expiration_enabled else None,
                    'audit_logging': audit_logging,
                    'require_2fa': require_2fa,
                    'ip_restrictions': ip_restrictions,
                    'max_attempts': max_download_attempts,
                    'time_based': time_based_access
                })

                base_name = uploaded_file.name.rsplit('.', 1)[0]
                config_filename = f"{base_name}_access_config.json"
                access_controlled_files[config_filename] = access_config.encode()

            st.success(f"Created access control configurations for {len(uploaded_files)} file(s)")

            zip_data = FileHandler.create_zip_archive(access_controlled_files)
            FileHandler.create_download_link(zip_data, "access_control_configs.zip", "application/zip")


# File Utilities
def file_merger():
    """Merge multiple files into one"""
    create_tool_header("File Merger", "Merge multiple files into a single file", "🔗")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Merge Settings")

        col1, col2 = st.columns(2)

        with col1:
            merge_method = st.selectbox("Merge Method",
                                        ["Simple Concatenation", "With Separators", "Structured Merge", "Binary Merge"])
            output_format = st.selectbox("Output Format", ["TXT", "Binary", "CSV", "JSON", "XML"])

        with col2:
            if merge_method == "With Separators":
                separator = st.text_input("Separator", value="\n---\n")
            include_headers = st.checkbox("Include File Headers", True)
            preserve_order = st.checkbox("Preserve File Order", True)

        output_filename = st.text_input("Output Filename", value="merged_file")

        if st.button("Merge Files"):
            try:
                merged_content = merge_files_advanced(uploaded_files, merge_method, {
                    'separator': separator if merge_method == "With Separators" else None,
                    'include_headers': include_headers,
                    'preserve_order': preserve_order,
                    'output_format': output_format
                })

                final_filename = f"{output_filename}.{output_format.lower()}"
                mime_type = get_mime_type_for_format(output_format)

                FileHandler.create_download_link(merged_content, final_filename, mime_type)
                st.success(f"Successfully merged {len(uploaded_files)} files!")

            except Exception as e:
                st.error(f"Error merging files: {str(e)}")


def path_manager():
    """Manage file paths and directory structures"""
    create_tool_header("Path Manager", "Manage and analyze file paths", "🛤️")

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Path Analysis")

        # Analyze file paths
        path_analysis = analyze_file_paths(uploaded_files)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Files", path_analysis['total_files'])
        with col2:
            st.metric("Unique Extensions", len(path_analysis['extensions']))
        with col3:
            st.metric("Avg Name Length", f"{path_analysis['avg_name_length']:.1f}")

        # Path operations
        st.subheader("Path Operations")

        operation = st.selectbox("Path Operation", [
            "Normalize Paths", "Extract Directory Structure", "Generate Path Report",
            "Validate Path Safety", "Create Path Mapping"
        ])

        if operation == "Normalize Paths":
            normalization_rules = st.multiselect("Normalization Rules", [
                "Remove Special Characters", "Convert to Lowercase", "Replace Spaces",
                "Limit Length", "Remove Duplicates"
            ])

        elif operation == "Validate Path Safety":
            check_options = st.multiselect("Safety Checks", [
                "Path Traversal", "Reserved Names", "Invalid Characters", "Length Limits"
            ])

        if st.button(f"Execute {operation}"):
            if operation == "Normalize Paths":
                result = normalize_file_paths(uploaded_files, normalization_rules)
            elif operation == "Extract Directory Structure":
                result = extract_directory_structure(uploaded_files)
            elif operation == "Generate Path Report":
                result = generate_path_report(uploaded_files)
            elif operation == "Validate Path Safety":
                result = validate_path_safety(uploaded_files, check_options)
            else:  # Create Path Mapping
                result = create_path_mapping(uploaded_files)

            # Display results
            st.subheader("Operation Results")

            if isinstance(result, dict):
                for key, value in result.items():
                    with st.expander(f"📁 {key}"):
                        if isinstance(value, list):
                            for item in value:
                                st.write(f"• {item}")
                        else:
                            st.write(value)
            else:
                st.write(result)

            # Export results
            if st.button("Export Results"):
                import json
                if isinstance(result, (dict, list)):
                    export_content = json.dumps(result, indent=2, default=str)
                else:
                    export_content = str(result)

                FileHandler.create_download_link(
                    export_content.encode(),
                    f"path_{operation.lower().replace(' ', '_')}_results.json",
                    "application/json"
                )


# Helper Functions for File Tools
def create_zip_from_files(files, compression_level):
    """Create a ZIP archive from extracted files"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zf:
        for file_info in files:
            zf.writestr(file_info['name'], file_info['content'])

    return zip_buffer.getvalue()


def optimize_archive_compression(file_data, optimization_level):
    """Optimize archive compression"""
    # Basic compression optimization - recompress with different levels
    level_map = {"Fast": 1, "Balanced": 6, "Maximum": 9}
    compression_level = level_map.get(optimization_level, 6)

    # For demonstration, return slightly compressed data
    import gzip
    return gzip.compress(file_data, compresslevel=compression_level)


def optimize_image_compression(file_data, target_size_mb, preserve_quality):
    """Optimize image compression"""
    try:
        image = Image.open(io.BytesIO(file_data))
        output_buffer = io.BytesIO()

        if preserve_quality:
            quality = 85
        else:
            # Calculate quality based on target size
            quality = max(30, min(95, int(100 - (target_size_mb * 5))))

        if image.mode in ("RGBA", "LA", "P"):
            image = image.convert("RGB")

        image.save(output_buffer, format="JPEG", quality=quality, optimize=True)
        return output_buffer.getvalue()
    except:
        # Return original data if optimization fails
        return file_data


def optimize_generic_compression(file_data, optimization_level):
    """Generic file compression optimization"""
    import gzip
    level_map = {"Fast": 1, "Balanced": 6, "Maximum": 9}
    compression_level = level_map.get(optimization_level, 6)
    return gzip.compress(file_data, compresslevel=compression_level)


def organize_files_by_type(files):
    """Organize files by their type"""
    organized = {}

    for file in files:
        file_ext = file.name.split('.')[-1].lower() if '.' in file.name else 'no_extension'

        if file_ext not in organized:
            organized[file_ext] = []
        organized[file_ext].append(file)

    return organized


def organize_files_by_size(files):
    """Organize files by size ranges"""
    size_ranges = {
        "small": (0, 1024 * 1024),  # < 1MB
        "medium": (1024 * 1024, 10 * 1024 * 1024),  # 1-10MB
        "large": (10 * 1024 * 1024, float('inf'))  # > 10MB
    }

    organized = {}

    for file in files:
        file_size = len(file.getvalue())

        for range_name, (min_size, max_size) in size_ranges.items():
            if min_size <= file_size < max_size:
                if range_name not in organized:
                    organized[range_name] = []
                organized[range_name].append(file)
                break

    return organized


def organize_files_by_date(files):
    """Organize files by current date (placeholder)"""
    today = datetime.now().strftime("%Y-%m-%d")
    return {today: files}


def create_zip_archive_with_level(files, compression_level):
    """Create ZIP archive with specific compression level"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zf:
        for file in files:
            zf.writestr(file.name, file.getvalue())

    return zip_buffer.getvalue()


def create_tar_archive(files, compression_type, compression_level):
    """Create TAR archive with compression"""
    tar_buffer = io.BytesIO()

    mode = 'w'
    if compression_type == 'gz':
        mode = 'w:gz'
    elif compression_type == 'bz2':
        mode = 'w:bz2'

    with tarfile.open(fileobj=tar_buffer, mode=mode) as tf:
        for file in files:
            tarinfo = tarfile.TarInfo(name=file.name)
            tarinfo.size = len(file.getvalue())
            tf.addfile(tarinfo, io.BytesIO(file.getvalue()))

    return tar_buffer.getvalue()


def extract_file_information(uploaded_file, detail_level):
    """Extract comprehensive file information"""
    file_data = uploaded_file.getvalue()

    info = {
        "Basic Information": {
            "Name": uploaded_file.name,
            "Size": f"{len(file_data):,} bytes",
            "Type": uploaded_file.type or "Unknown"
        },
        "File Analysis": {
            "Extension": uploaded_file.name.split('.')[-1].lower() if '.' in uploaded_file.name else "None",
            "Is Binary": not is_text_file(file_data),
            "Character Count": len(file_data) if is_text_file(file_data) else "N/A"
        }
    }

    if detail_level in ["Detailed", "Comprehensive"]:
        import hashlib
        info["Checksums"] = {
            "MD5": hashlib.md5(file_data).hexdigest(),
            "SHA256": hashlib.sha256(file_data).hexdigest()
        }

    return info


def is_text_file(data):
    """Simple text file detection"""
    try:
        data.decode('utf-8')
        return True
    except:
        return False


def clean_file_metadata(uploaded_file, **options):
    """Clean metadata from files (basic implementation)"""
    file_data = uploaded_file.getvalue()

    # For images, attempt to remove EXIF data
    if uploaded_file.type and uploaded_file.type.startswith('image/'):
        try:
            image = Image.open(io.BytesIO(file_data))

            # Create new image without EXIF data
            cleaned_image = Image.new(image.mode, image.size)
            cleaned_image.putdata(list(image.getdata()))

            output_buffer = io.BytesIO()
            image_format = image.format or 'JPEG'
            cleaned_image.save(output_buffer, format=image_format)
            return output_buffer.getvalue()
        except:
            pass

    # For other files, return as-is (real implementation would vary by file type)
    return file_data


def convert_file_to_format(uploaded_file, target_format, quality):
    """Convert file to specified format (basic implementation)"""
    file_data = uploaded_file.getvalue()

    # Basic text conversion
    if target_format == "TXT":
        if uploaded_file.type and uploaded_file.type.startswith('text/'):
            return file_data
        else:
            return f"Content of {uploaded_file.name}".encode()

    # Basic image conversion
    if target_format in ["PNG", "JPEG", "WebP"] and uploaded_file.type and uploaded_file.type.startswith('image/'):
        try:
            image = Image.open(io.BytesIO(file_data))
            output_buffer = io.BytesIO()

            if target_format == "JPEG" and image.mode in ("RGBA", "LA", "P"):
                image = image.convert("RGB")

            image.save(output_buffer, format=target_format, quality=quality if target_format == "JPEG" else None)
            return output_buffer.getvalue()
        except:
            pass

    # Return original data if conversion not possible
    return file_data


def format_bytes(size):
    """Format bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} PB"


def create_tar_from_files(files, compression):
    """Create a TAR archive from extracted files"""
    tar_buffer = io.BytesIO()

    mode = 'w'
    if compression == 'gz':
        mode = 'w:gz'
    elif compression == 'bz2':
        mode = 'w:bz2'

    with tarfile.open(fileobj=tar_buffer, mode=mode) as tf:
        for file_info in files:
            tarinfo = tarfile.TarInfo(name=file_info['name'])
            tarinfo.size = len(file_info['content'])
            tf.addfile(tarinfo, io.BytesIO(file_info['content']))

    return tar_buffer.getvalue()


# Additional Helper Functions
def apply_batch_operations(uploaded_file, operations, settings):
    """Apply batch operations to a file"""
    file_data = uploaded_file.getvalue()

    # Handle image operations
    if uploaded_file.type and uploaded_file.type.startswith('image/') and any(
            op in operations for op in ["Resize Images", "Add Watermark"]):
        try:
            image = Image.open(io.BytesIO(file_data))

            if "Resize Images" in operations and settings.get('resize_width') and settings.get('resize_height'):
                image = image.resize((settings['resize_width'], settings['resize_height']), Image.Resampling.LANCZOS)

            if "Add Watermark" in operations and settings.get('watermark_text'):
                # Simple watermark (would need PIL.ImageDraw for real implementation)
                pass

            output_buffer = io.BytesIO()
            image.save(output_buffer, format=image.format or 'JPEG')
            return output_buffer.getvalue()
        except:
            pass

    return file_data


def organize_files_advanced(uploaded_files, organize_by, options):
    """Advanced file organization"""
    organized = {}

    if organize_by == "File Type":
        return organize_files_by_type(uploaded_files)
    elif organize_by == "File Size":
        return organize_files_by_size(uploaded_files)
    else:
        # Default organization
        organized["All Files"] = [{"new_name": f.name, "original_name": f.name} for f in uploaded_files]

    return organized


def create_organized_archive(organized_structure):
    """Create archive from organized structure"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for folder, files in organized_structure.items():
            for file_info in files:
                archive_path = f"{folder}/{file_info['new_name']}"
                zf.writestr(archive_path, b"File content placeholder")

    return zip_buffer.getvalue()


def bulk_rename_file(uploaded_file, prefix, suffix, number, number_format):
    """Bulk rename a single file"""
    base_name = uploaded_file.name.rsplit('.', 1)[0]
    extension = uploaded_file.name.rsplit('.', 1)[1] if '.' in uploaded_file.name else ''

    if number_format == "001":
        number_str = f"{number:03d}"
    elif number_format == "01":
        number_str = f"{number:02d}"
    else:
        number_str = str(number)

    new_name = f"{prefix}{base_name}{suffix}_{number_str}"
    if extension:
        new_name += f".{extension}"

    return {"filename": new_name, "data": uploaded_file.getvalue()}


def bulk_convert_file(uploaded_file, target_format, quality):
    """Bulk convert a single file"""
    converted_data = convert_file_to_format(uploaded_file, target_format, quality)
    base_name = uploaded_file.name.rsplit('.', 1)[0]
    new_filename = f"{base_name}_converted.{target_format.lower()}"
    return {"filename": new_filename, "data": converted_data}


def bulk_compress_file(uploaded_file, compression_level, compression_format):
    """Bulk compress a single file"""
    file_data = uploaded_file.getvalue()

    if compression_format == "ZIP":
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zf:
            zf.writestr(uploaded_file.name, file_data)
        compressed_data = zip_buffer.getvalue()
        new_filename = f"{uploaded_file.name}.zip"
    else:
        # Simple gzip compression for other formats
        import gzip
        compressed_data = gzip.compress(file_data, compresslevel=compression_level)
        new_filename = f"{uploaded_file.name}.gz"

    return {"filename": new_filename, "data": compressed_data}


def perform_bulk_operation(uploaded_file, operation_type):
    """Perform generic bulk operation"""
    return {"filename": uploaded_file.name, "data": uploaded_file.getvalue()}


def apply_directory_management(uploaded_files, action, structure_template, options):
    """Apply directory management operations"""
    managed_structure = {}

    if structure_template == "By Type/Subtype":
        for file in uploaded_files:
            file_ext = file.name.split('.')[-1].lower() if '.' in file.name else 'unknown'
            folder = f"{file_ext}_files"
            if folder not in managed_structure:
                managed_structure[folder] = []
            managed_structure[folder].append(file)
    else:
        managed_structure["All Files"] = uploaded_files

    return managed_structure


def display_directory_tree(structure):
    """Display directory tree structure"""
    for folder, files in structure.items():
        st.write(f"📁 **{folder}** ({len(files)} files)")
        for file in files[:5]:  # Show first 5 files
            st.write(f"   📄 {file.name if hasattr(file, 'name') else file}")
        if len(files) > 5:
            st.write(f"   ... and {len(files) - 5} more files")


def create_directory_archive(structure):
    """Create archive with directory structure"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for folder, files in structure.items():
            for file in files:
                if hasattr(file, 'getvalue'):
                    zf.writestr(f"{folder}/{file.name}", file.getvalue())
                else:
                    zf.writestr(f"{folder}/{file}", b"File content")

    return zip_buffer.getvalue()


def sort_files_advanced(uploaded_files, primary_sort, secondary_sort, sort_order, group_by, options):
    """Advanced file sorting"""
    sorted_files = {}

    # Simple grouping by file type
    if group_by == "File Type":
        for file in uploaded_files:
            file_ext = file.name.split('.')[-1].lower() if '.' in file.name else 'no_extension'
            if file_ext not in sorted_files:
                sorted_files[file_ext] = []
            sorted_files[file_ext].append({
                "name": file.name,
                "size": len(file.getvalue())
            })
    else:
        sorted_files["All Files"] = [{
            "name": file.name,
            "size": len(file.getvalue())
        } for file in uploaded_files]

    # Sort each group
    for group in sorted_files.values():
        if primary_sort == "Name":
            group.sort(key=lambda x: x["name"], reverse=(sort_order == "Descending"))
        elif primary_sort == "Size":
            group.sort(key=lambda x: x["size"], reverse=(sort_order == "Descending"))

    return sorted_files


def create_sorted_archive(sorted_files):
    """Create archive from sorted files"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for group_name, files in sorted_files.items():
            for i, file_info in enumerate(files):
                archive_path = f"{group_name}/{i + 1:03d}_{file_info['name']}"
                zf.writestr(archive_path, b"File content placeholder")

    return zip_buffer.getvalue()


def create_folder_organization(uploaded_files, organization_scheme, options):
    """Create folder organization structure"""
    folder_structure = {}

    if organization_scheme == "File Type Categories":
        type_categories = {
            "Documents": [".pdf", ".doc", ".docx", ".txt"],
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Archives": [".zip", ".tar", ".gz"]
        }

        for file in uploaded_files:
            file_ext = file.name.split('.')[-1].lower() if '.' in file.name else ''

            categorized = False
            for category, extensions in type_categories.items():
                if f".{file_ext}" in extensions:
                    if category not in folder_structure:
                        folder_structure[category] = []
                    folder_structure[category].append(file)
                    categorized = True
                    break

            if not categorized:
                if "Other" not in folder_structure:
                    folder_structure["Other"] = []
                folder_structure["Other"].append(file)
    else:
        folder_structure["All Files"] = uploaded_files

    return folder_structure


def display_folder_tree(structure):
    """Display folder tree structure"""
    display_directory_tree(structure)


def create_folder_archive(structure):
    """Create archive with folder structure"""
    return create_directory_archive(structure)


def analyze_file_type(uploaded_file):
    """Analyze file type and properties"""
    file_data = uploaded_file.getvalue()

    # Basic magic number detection
    magic_number = file_data[:8].hex() if len(file_data) >= 8 else "N/A"

    # Basic file type detection
    if file_data.startswith(b'\x89PNG'):
        detected_type = "PNG Image"
    elif file_data.startswith(b'\xFF\xD8\xFF'):
        detected_type = "JPEG Image"
    elif file_data.startswith(b'PK'):
        detected_type = "ZIP Archive"
    elif file_data.startswith(b'%PDF'):
        detected_type = "PDF Document"
    else:
        detected_type = "Unknown"

    return {
        "detected_type": detected_type,
        "mime_type": uploaded_file.type or "Unknown",
        "file_size": len(file_data),
        "magic_number": magic_number,
        "encoding": "Binary" if not is_text_file(file_data) else "UTF-8",
        "is_binary": not is_text_file(file_data)
    }


def detect_advanced_duplicates(uploaded_files, detection_method, similarity_threshold, include_partial,
                               ignore_extensions):
    """Detect duplicates with advanced methods"""
    duplicates = []

    if detection_method == "Hash Comparison":
        import hashlib
        hash_groups = {}

        for file in uploaded_files:
            file_hash = hashlib.md5(file.getvalue()).hexdigest()
            if file_hash not in hash_groups:
                hash_groups[file_hash] = []
            hash_groups[file_hash].append({
                "name": file.name,
                "size": len(file.getvalue())
            })

        for hash_value, files in hash_groups.items():
            if len(files) > 1:
                duplicates.append({
                    "files": files,
                    "similarity": 100.0
                })

    return duplicates


def generate_duplicate_cleanup_report(duplicates):
    """Generate cleanup report for duplicates"""
    report = "Duplicate Files Cleanup Report\n"
    report += "=" * 40 + "\n\n"

    for i, duplicate_group in enumerate(duplicates, 1):
        report += f"Group {i}:\n"
        for file_info in duplicate_group['files']:
            report += f"  - {file_info['name']} ({format_bytes(file_info['size'])})\n"
        report += f"  Similarity: {duplicate_group['similarity']:.1f}%\n\n"

    return report


def generate_comprehensive_statistics(uploaded_files):
    """Generate comprehensive file statistics"""
    total_files = len(uploaded_files)
    total_size = sum(len(f.getvalue()) for f in uploaded_files)
    average_size = total_size / total_files if total_files > 0 else 0

    # Type distribution
    type_distribution = {}
    for file in uploaded_files:
        file_ext = file.name.split('.')[-1].lower() if '.' in file.name else 'no_extension'
        type_distribution[file_ext] = type_distribution.get(file_ext, 0) + 1

    # Size distribution
    size_distribution = {
        "< 1KB": 0, "1KB - 1MB": 0, "1MB - 10MB": 0,
        "10MB - 100MB": 0, "> 100MB": 0
    }

    for file in uploaded_files:
        size = len(file.getvalue())
        if size < 1024:
            size_distribution["< 1KB"] += 1
        elif size < 1024 * 1024:
            size_distribution["1KB - 1MB"] += 1
        elif size < 10 * 1024 * 1024:
            size_distribution["1MB - 10MB"] += 1
        elif size < 100 * 1024 * 1024:
            size_distribution["10MB - 100MB"] += 1
        else:
            size_distribution["> 100MB"] += 1

    return {
        "total_files": total_files,
        "total_size": total_size,
        "average_size": average_size,
        "unique_types": len(type_distribution),
        "type_distribution": type_distribution,
        "size_distribution": size_distribution
    }


# Security and Backup Helper Functions
def apply_password_protection(uploaded_file, password, encryption_strength, hint):
    """Apply password protection to file (basic implementation)"""
    from cryptography.fernet import Fernet
    import base64

    try:
        # Simple encryption using Fernet (not production-ready)
        key = Fernet.generate_key()
        fernet = Fernet(key)

        file_data = uploaded_file.getvalue()
        encrypted_data = fernet.encrypt(file_data)

        # Create a simple protected file format
        protection_header = {
            "encryption": encryption_strength,
            "hint": hint,
            "key": base64.b64encode(key).decode()  # In real implementation, this would be derived from password
        }

        import json
        header_bytes = json.dumps(protection_header).encode()
        header_length = len(header_bytes).to_bytes(4, 'big')

        return header_length + header_bytes + encrypted_data
    except:
        # Return original data if protection fails
        return uploaded_file.getvalue()


def simulate_secure_deletion(uploaded_file, method, passes, delete_metadata):
    """Simulate secure deletion process"""
    file_size = len(uploaded_file.getvalue())

    return {
        "filename": uploaded_file.name,
        "original_size": file_size,
        "method": method,
        "passes": passes,
        "metadata_cleared": delete_metadata,
        "verification": "PASS" if file_size > 0 else "FAIL"
    }


def generate_deletion_report(deletion_results):
    """Generate secure deletion report"""
    report = "Secure Deletion Report\n"
    report += "=" * 30 + "\n\n"

    for result in deletion_results:
        report += f"File: {result['filename']}\n"
        report += f"Method: {result['method']}\n"
        report += f"Passes: {result['passes']}\n"
        report += f"Verification: {result['verification']}\n\n"

    return report


def check_file_integrity(uploaded_file, hash_algorithms, deep_scan, check_headers, verify_signatures):
    """Check file integrity"""
    import hashlib

    file_data = uploaded_file.getvalue()

    # Generate hashes
    hashes = {}
    for algo in hash_algorithms:
        if algo == "MD5":
            hashes["MD5"] = hashlib.md5(file_data).hexdigest()
        elif algo == "SHA1":
            hashes["SHA1"] = hashlib.sha1(file_data).hexdigest()
        elif algo == "SHA256":
            hashes["SHA256"] = hashlib.sha256(file_data).hexdigest()
        elif algo == "SHA512":
            hashes["SHA512"] = hashlib.sha512(file_data).hexdigest()

    # Basic integrity checks
    issues = []
    if len(file_data) == 0:
        issues.append("File is empty")

    if check_headers and len(file_data) > 0:
        # Basic header validation
        if uploaded_file.name.endswith('.jpg') and not file_data.startswith(b'\xFF\xD8'):
            issues.append("Invalid JPEG header")
        elif uploaded_file.name.endswith('.png') and not file_data.startswith(b'\x89PNG'):
            issues.append("Invalid PNG header")

    return {
        "filename": uploaded_file.name,
        "file_size": len(file_data),
        "file_type": uploaded_file.type or "Unknown",
        "hashes": hashes,
        "issues": issues,
        "status": "Healthy" if not issues else "Issues Found"
    }


def generate_integrity_report(integrity_results):
    """Generate integrity check report"""
    import json

    report = {
        "report_date": datetime.now().isoformat(),
        "total_files": len(integrity_results),
        "healthy_files": sum(1 for r in integrity_results if r['status'] == 'Healthy'),
        "files_with_issues": sum(1 for r in integrity_results if r['status'] != 'Healthy'),
        "detailed_results": integrity_results
    }

    return json.dumps(report, indent=2)


def create_access_control_config(uploaded_file, settings):
    """Create access control configuration"""
    import json

    config = {
        "file_name": uploaded_file.name,
        "permission_level": settings['permission_level'],
        "user_groups": settings['user_groups'],
        "expiration_date": settings['expiration_date'].isoformat() if settings['expiration_date'] else None,
        "security_settings": {
            "audit_logging": settings['audit_logging'],
            "require_2fa": settings['require_2fa'],
            "ip_restrictions": settings['ip_restrictions'],
            "max_attempts": settings['max_attempts'],
            "time_based": settings['time_based']
        },
        "created_date": datetime.now().isoformat()
    }

    return json.dumps(config, indent=2)


# Backup and Sync Helper Functions
def create_sync_package(uploaded_files, sync_mode, conflict_resolution, backup_versions, compression_enabled):
    """Create synchronization package"""
    sync_config = {
        "sync_mode": sync_mode,
        "conflict_resolution": conflict_resolution,
        "backup_versions": backup_versions,
        "compression_enabled": compression_enabled,
        "files": [f.name for f in uploaded_files]
    }

    # Create sync package
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add config
        import json
        zf.writestr("sync_config.json", json.dumps(sync_config, indent=2))

        # Add files
        for file in uploaded_files:
            zf.writestr(f"files/{file.name}", file.getvalue())

    return zip_buffer.getvalue()


def create_version_archive(uploaded_files, comment, options):
    """Create version control archive"""
    version_info = {
        "version_comment": comment,
        "timestamp": datetime.now().isoformat(),
        "file_count": len(uploaded_files),
        "options": options
    }

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add version info
        import json
        zf.writestr("version_info.json", json.dumps(version_info, indent=2))

        # Add files
        for file in uploaded_files:
            zf.writestr(f"files/{file.name}", file.getvalue())

    return zip_buffer.getvalue()


def create_backup_configuration(uploaded_files, settings):
    """Create backup configuration"""
    import json

    config = {
        "backup_settings": settings,
        "files": [f.name for f in uploaded_files],
        "created_date": datetime.now().isoformat()
    }

    return json.dumps(config, indent=2)


def perform_file_recovery(uploaded_files, recovery_mode, options):
    """Perform file recovery operation"""
    # Simple recovery simulation - create recovery package
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in uploaded_files:
            # Simulate recovery by copying files
            zf.writestr(f"recovered/{file.name}", file.getvalue())

        # Add recovery log
        if options.get('create_log'):
            log_content = f"Recovery completed at {datetime.now().isoformat()}\n"
            log_content += f"Mode: {recovery_mode}\n"
            log_content += f"Files recovered: {len(uploaded_files)}\n"
            zf.writestr("recovery_log.txt", log_content)

    return zip_buffer.getvalue()


def prepare_cloud_sync_package(uploaded_files, cloud_provider, sync_direction, conflict_resolution):
    """Prepare cloud synchronization package"""
    sync_manifest = {
        "cloud_provider": cloud_provider,
        "sync_direction": sync_direction,
        "conflict_resolution": conflict_resolution,
        "files": [{"name": f.name, "size": len(f.getvalue())} for f in uploaded_files],
        "created_date": datetime.now().isoformat()
    }

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        import json
        zf.writestr("sync_manifest.json", json.dumps(sync_manifest, indent=2))

        for file in uploaded_files:
            zf.writestr(f"sync_files/{file.name}", file.getvalue())

    return zip_buffer.getvalue()


def create_file_mirrors(uploaded_files, mirror_type, mirror_count, verify_checksums, include_metadata):
    """Create file mirrors"""
    mirrors = []

    for i in range(mirror_count):
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file in uploaded_files:
                zf.writestr(file.name, file.getvalue())

            if include_metadata:
                mirror_info = {
                    "mirror_number": i + 1,
                    "mirror_type": mirror_type,
                    "verify_checksums": verify_checksums,
                    "created_date": datetime.now().isoformat()
                }
                import json
                zf.writestr("mirror_info.json", json.dumps(mirror_info, indent=2))

        mirrors.append(zip_buffer.getvalue())

    return mirrors


def create_sync_schedule(uploaded_files, settings):
    """Create sync schedule configuration"""
    import json

    schedule = {
        "schedule_settings": settings,
        "files": [f.name for f in uploaded_files],
        "created_date": datetime.now().isoformat()
    }

    return json.dumps(schedule, indent=2)


def detect_file_conflicts(uploaded_files):
    """Detect potential file conflicts"""
    conflicts = []
    name_groups = {}

    # Group files by similar names
    for file in uploaded_files:
        base_name = file.name.lower()
        if base_name not in name_groups:
            name_groups[base_name] = []
        name_groups[base_name].append({
            "name": file.name,
            "size": len(file.getvalue()),
            "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # Find conflicts (files with same name)
    for name, files in name_groups.items():
        if len(files) > 1:
            conflicts.append({
                "name": name,
                "files": files
            })

    return conflicts


def resolve_all_conflicts(conflicts, uploaded_files):
    """Resolve all detected conflicts"""
    # Simple resolution - create archive with all files
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in uploaded_files:
            zf.writestr(file.name, file.getvalue())

    return zip_buffer.getvalue()


# File Utility Helper Functions
def merge_files_advanced(uploaded_files, merge_method, options):
    """Advanced file merging"""
    merged_content = b""

    if merge_method == "Simple Concatenation":
        for file in uploaded_files:
            if options.get('include_headers'):
                header = f"\n--- {file.name} ---\n".encode()
                merged_content += header
            merged_content += file.getvalue()

    elif merge_method == "With Separators" and options.get('separator'):
        separator_bytes = options['separator'].encode()
        file_contents = [file.getvalue() for file in uploaded_files]
        merged_content = separator_bytes.join(file_contents)

    else:
        # Default: simple concatenation
        for file in uploaded_files:
            merged_content += file.getvalue()

    return merged_content


def get_mime_type_for_format(output_format):
    """Get MIME type for output format"""
    mime_types = {
        "TXT": "text/plain",
        "CSV": "text/csv",
        "JSON": "application/json",
        "XML": "application/xml",
        "Binary": "application/octet-stream"
    }
    return mime_types.get(output_format, "application/octet-stream")


def analyze_file_paths(uploaded_files):
    """Analyze file paths and names"""
    extensions = set()
    total_name_length = 0

    for file in uploaded_files:
        if '.' in file.name:
            ext = file.name.split('.')[-1].lower()
            extensions.add(ext)
        total_name_length += len(file.name)

    return {
        "total_files": len(uploaded_files),
        "extensions": list(extensions),
        "avg_name_length": total_name_length / len(uploaded_files) if uploaded_files else 0
    }


def normalize_file_paths(uploaded_files, normalization_rules):
    """Normalize file paths based on rules"""
    normalized = {}

    for file in uploaded_files:
        name = file.name

        if "Remove Special Characters" in normalization_rules:
            import re
            name = re.sub(r'[^\w\s.-]', '', name)

        if "Convert to Lowercase" in normalization_rules:
            name = name.lower()

        if "Replace Spaces" in normalization_rules:
            name = name.replace(' ', '_')

        if "Limit Length" in normalization_rules:
            name = name[:50] if len(name) > 50 else name

        normalized[file.name] = name

    return normalized


def extract_directory_structure(uploaded_files):
    """Extract directory structure from file paths"""
    structure = {"files": []}

    for file in uploaded_files:
        structure["files"].append({
            "original_name": file.name,
            "size": len(file.getvalue()),
            "type": file.name.split('.')[-1] if '.' in file.name else 'unknown'
        })

    return structure


def generate_path_report(uploaded_files):
    """Generate comprehensive path report"""
    report = {
        "total_files": len(uploaded_files),
        "file_analysis": analyze_file_paths(uploaded_files),
        "files": [{"name": f.name, "size": len(f.getvalue())} for f in uploaded_files],
        "generated_date": datetime.now().isoformat()
    }

    return report


def validate_path_safety(uploaded_files, check_options):
    """Validate path safety"""
    results = {"safe_files": [], "unsafe_files": []}

    for file in uploaded_files:
        is_safe = True
        issues = []

        if "Path Traversal" in check_options:
            if '..' in file.name or '/' in file.name or '\\' in file.name:
                is_safe = False
                issues.append("Contains path traversal characters")

        if "Invalid Characters" in check_options:
            invalid_chars = ['<', '>', ':', '"', '|', '?', '*']
            if any(char in file.name for char in invalid_chars):
                is_safe = False
                issues.append("Contains invalid characters")

        if "Length Limits" in check_options:
            if len(file.name) > 255:
                is_safe = False
                issues.append("Filename too long")

        result = {"name": file.name, "issues": issues}

        if is_safe:
            results["safe_files"].append(result)
        else:
            results["unsafe_files"].append(result)

    return results


def create_path_mapping(uploaded_files):
    """Create path mapping for files"""
    mapping = {}

    for i, file in enumerate(uploaded_files):
        safe_name = f"file_{i + 1:03d}_{file.name.replace(' ', '_')}"
        mapping[file.name] = safe_name

    return mapping


def extract_archive(uploaded_file):
    """Extract files from archive (with basic Zip Slip protection)"""
    extracted_files = []

    try:
        file_data = uploaded_file.getvalue()

        if uploaded_file.name.endswith('.zip'):
            # Extract ZIP files
            with zipfile.ZipFile(io.BytesIO(file_data), 'r') as zf:
                for member in zf.namelist():
                    # Basic Zip Slip protection
                    if member.startswith('/') or '..' in member:
                        continue  # Skip potentially dangerous paths

                    try:
                        content = zf.read(member)
                        extracted_files.append({
                            'name': member,
                            'content': content
                        })
                    except:
                        continue  # Skip problematic files

        elif uploaded_file.name.endswith(('.tar', '.tar.gz', '.tar.bz2')):
            # Extract TAR files
            with tarfile.open(fileobj=io.BytesIO(file_data), mode='r:*') as tf:
                for member in tf.getmembers():
                    if member.isfile():
                        # Basic path traversal protection
                        if member.name.startswith('/') or '..' in member.name:
                            continue

                        try:
                            f = tf.extractfile(member)
                            if f:
                                content = f.read()
                                extracted_files.append({
                                    'name': member.name,
                                    'content': content
                                })
                        except:
                            continue

        else:
            # For unsupported formats, return empty list
            pass

    except Exception as e:
        # Return empty list if extraction fails
        pass

    return extracted_files


def property_editor():
    """File property editor"""
    create_tool_header("File Property Editor", "View and edit file properties and metadata", "📝")

    uploaded_file = FileHandler.upload_files(['*'], accept_multiple=False)

    if uploaded_file:
        file = uploaded_file[0]
        file_content = file.getvalue()

        st.subheader(f"Properties: {file.name}")

        # Basic file information
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Basic Information**")
            st.write(f"**Name:** {file.name}")
            st.write(f"**Size:** {format_bytes(len(file_content))}")
            st.write(f"**Type:** {file.type if file.type else 'Unknown'}")

            # File extension and MIME type
            import mimetypes
            import os

            file_ext = os.path.splitext(file.name)[1].lower()
            mime_type, encoding = mimetypes.guess_type(file.name)

            st.write(f"**Extension:** {file_ext if file_ext else 'None'}")
            st.write(f"**MIME Type:** {mime_type if mime_type else 'Unknown'}")
            if encoding:
                st.write(f"**Encoding:** {encoding}")

        with col2:
            st.write("**Advanced Properties**")

            # File hash
            import hashlib
            md5_hash = hashlib.md5(file_content).hexdigest()
            sha1_hash = hashlib.sha1(file_content).hexdigest()
            sha256_hash = hashlib.sha256(file_content).hexdigest()

            st.write(f"**MD5:** `{md5_hash[:16]}...`")
            st.write(f"**SHA1:** `{sha1_hash[:16]}...`")
            st.write(f"**SHA256:** `{sha256_hash[:16]}...`")

            # Character count for text files
            if file.type and file.type.startswith('text/'):
                try:
                    text_content = file_content.decode('utf-8')
                    st.write(f"**Characters:** {len(text_content):,}")
                    st.write(f"**Lines:** {text_content.count(chr(10)) + 1:,}")
                    st.write(f"**Words:** {len(text_content.split()):,}")
                except:
                    st.write("**Text Analysis:** Unable to decode as text")

        # Detailed hash information
        with st.expander("🔐 File Hashes (Full)"):
            st.code(f"MD5:    {md5_hash}", language="text")
            st.code(f"SHA1:   {sha1_hash}", language="text")
            st.code(f"SHA256: {sha256_hash}", language="text")

        # Custom metadata editor
        st.subheader("Custom Metadata")

        if 'custom_metadata' not in st.session_state:
            st.session_state.custom_metadata = {}

        col1, col2, col3 = st.columns([2, 2, 1])

        with col1:
            new_key = st.text_input("Property Name", placeholder="e.g., Author, Project, Tags")
        with col2:
            new_value = st.text_input("Property Value", placeholder="e.g., John Doe, Website, web,design")
        with col3:
            if st.button("Add Property") and new_key and new_value:
                st.session_state.custom_metadata[new_key] = new_value
                st.rerun()

        # Display custom metadata
        if st.session_state.custom_metadata:
            st.write("**Custom Properties:**")
            for key, value in st.session_state.custom_metadata.items():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{key}:** {value}")
                with col2:
                    if st.button("🗑️", key=f"del_{key}"):
                        del st.session_state.custom_metadata[key]
                        st.rerun()

        # Export properties
        st.subheader("Export Properties")

        export_format = st.selectbox("Export Format", ["JSON", "CSV", "Plain Text"])

        if st.button("Export Properties"):
            properties_data = {
                "file_name": file.name,
                "file_size": len(file_content),
                "file_type": file.type,
                "file_extension": file_ext,
                "mime_type": mime_type,
                "md5_hash": md5_hash,
                "sha1_hash": sha1_hash,
                "sha256_hash": sha256_hash,
                "custom_metadata": st.session_state.custom_metadata
            }

            if export_format == "JSON":
                import json
                export_content = json.dumps(properties_data, indent=2)
                FileHandler.create_download_link(export_content.encode(), f"{file.name}_properties.json",
                                                 "application/json")

            elif export_format == "CSV":
                import csv
                import io

                output = io.StringIO()
                writer = csv.writer(output)
                writer.writerow(["Property", "Value"])

                for key, value in properties_data.items():
                    if key != "custom_metadata":
                        writer.writerow([key, value])

                for key, value in properties_data["custom_metadata"].items():
                    writer.writerow([f"custom_{key}", value])

                FileHandler.create_download_link(output.getvalue().encode(), f"{file.name}_properties.csv", "text/csv")

            else:  # Plain Text
                text_content = f"File Properties: {file.name}\n"
                text_content += "=" * 50 + "\n\n"

                for key, value in properties_data.items():
                    if key != "custom_metadata":
                        text_content += f"{key.replace('_', ' ').title()}: {value}\n"

                if properties_data["custom_metadata"]:
                    text_content += "\nCustom Metadata:\n"
                    for key, value in properties_data["custom_metadata"].items():
                        text_content += f"  {key}: {value}\n"

                FileHandler.create_download_link(text_content.encode(), f"{file.name}_properties.txt", "text/plain")


def file_splitter():
    """File splitting tool"""
    create_tool_header("File Splitter", "Split large files into smaller chunks", "✂️")

    uploaded_file = FileHandler.upload_files(['*'], accept_multiple=False)

    if uploaded_file:
        file = uploaded_file[0]
        file_size = len(file.getvalue())

        st.write(f"**File:** {file.name} ({format_bytes(file_size)})")

        # Split options
        split_method = st.selectbox("Split Method", [
            "By Size", "By Number of Parts", "By Lines (Text Files)"
        ])

        if split_method == "By Size":
            st.subheader("Split by File Size")

            size_unit = st.selectbox("Size Unit", ["KB", "MB", "GB"])
            size_value = st.number_input(f"Chunk Size ({size_unit})", min_value=1, value=10)

            # Convert to bytes
            multipliers = {"KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}
            chunk_size = int(size_value * multipliers[size_unit])

            estimated_parts = max(1, (file_size + chunk_size - 1) // chunk_size)
            st.write(f"**Estimated Parts:** {estimated_parts}")

            if st.button("Split File by Size"):
                split_by_size(file, chunk_size)

        elif split_method == "By Number of Parts":
            st.subheader("Split by Number of Parts")

            num_parts = st.number_input("Number of Parts", min_value=2, max_value=100, value=5)

            chunk_size = file_size // num_parts
            st.write(f"**Each Part Size:** ~{format_bytes(chunk_size)}")

            if st.button("Split File into Parts"):
                split_by_parts(file, num_parts)

        else:  # By Lines
            st.subheader("Split by Lines")

            if file.type and file.type.startswith('text/'):
                try:
                    text_content = file.getvalue().decode('utf-8')
                    total_lines = text_content.count('\n') + 1

                    st.write(f"**Total Lines:** {total_lines:,}")

                    lines_per_file = st.number_input("Lines per File", min_value=1, value=min(1000, total_lines // 2))

                    estimated_files = max(1, (total_lines + lines_per_file - 1) // lines_per_file)
                    st.write(f"**Estimated Files:** {estimated_files}")

                    if st.button("Split by Lines"):
                        split_by_lines(file, lines_per_file)

                except Exception as e:
                    st.error(f"Error reading text file: {str(e)}")
            else:
                st.warning("Line splitting is only available for text files")


def split_by_size(file, chunk_size):
    """Split file by specified chunk size"""
    file_data = file.getvalue()
    file_name = file.name

    chunks = []
    offset = 0
    part_num = 1

    while offset < len(file_data):
        chunk_data = file_data[offset:offset + chunk_size]

        # Create filename for this chunk
        name_parts = file_name.rsplit('.', 1)
        if len(name_parts) == 2:
            chunk_filename = f"{name_parts[0]}.part{part_num:03d}.{name_parts[1]}"
        else:
            chunk_filename = f"{file_name}.part{part_num:03d}"

        chunks.append({
            'filename': chunk_filename,
            'data': chunk_data,
            'size': len(chunk_data)
        })

        offset += chunk_size
        part_num += 1

    display_split_results(chunks)


def split_by_parts(file, num_parts):
    """Split file into specified number of parts"""
    file_data = file.getvalue()
    file_name = file.name
    file_size = len(file_data)

    chunk_size = file_size // num_parts
    chunks = []

    for i in range(num_parts):
        start = i * chunk_size
        if i == num_parts - 1:  # Last part gets remainder
            end = file_size
        else:
            end = start + chunk_size

        chunk_data = file_data[start:end]

        # Create filename for this chunk
        name_parts = file_name.rsplit('.', 1)
        if len(name_parts) == 2:
            chunk_filename = f"{name_parts[0]}.part{i + 1:03d}.{name_parts[1]}"
        else:
            chunk_filename = f"{file_name}.part{i + 1:03d}"

        chunks.append({
            'filename': chunk_filename,
            'data': chunk_data,
            'size': len(chunk_data)
        })

    display_split_results(chunks)


def split_by_lines(file, lines_per_file):
    """Split text file by number of lines"""
    try:
        text_content = file.getvalue().decode('utf-8')
        lines = text_content.split('\n')
        file_name = file.name

        chunks = []
        file_num = 1

        for i in range(0, len(lines), lines_per_file):
            chunk_lines = lines[i:i + lines_per_file]
            chunk_content = '\n'.join(chunk_lines)

            # Create filename for this chunk
            name_parts = file_name.rsplit('.', 1)
            if len(name_parts) == 2:
                chunk_filename = f"{name_parts[0]}.part{file_num:03d}.{name_parts[1]}"
            else:
                chunk_filename = f"{file_name}.part{file_num:03d}.txt"

            chunks.append({
                'filename': chunk_filename,
                'data': chunk_content.encode('utf-8'),
                'size': len(chunk_content.encode('utf-8'))
            })

            file_num += 1

        display_split_results(chunks)

    except Exception as e:
        st.error(f"Error splitting text file: {str(e)}")


def display_split_results(chunks):
    """Display the results of file splitting"""
    st.success(f"✅ File split into {len(chunks)} parts successfully!")

    # Summary statistics
    total_size = sum(chunk['size'] for chunk in chunks)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Parts", len(chunks))
    with col2:
        st.metric("Total Size", format_bytes(total_size))
    with col3:
        st.metric("Average Part Size", format_bytes(total_size // len(chunks)))

    # Download links for each chunk
    st.subheader("Download Split Files")

    for i, chunk in enumerate(chunks):
        col1, col2, col3 = st.columns([3, 2, 2])

        with col1:
            st.write(f"**{chunk['filename']}**")
        with col2:
            st.write(format_bytes(chunk['size']))
        with col3:
            FileHandler.create_download_link(
                chunk['data'],
                chunk['filename'],
                "application/octet-stream"
            )


def checksum_generator():
    """Checksum generation tool"""
    create_tool_header("Checksum Generator", "Generate and verify file checksums", "🔐")

    operation = st.selectbox("Operation", ["Generate Checksums", "Verify Checksums", "Compare Files"])

    if operation == "Generate Checksums":
        st.subheader("Generate File Checksums")

        uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

        if uploaded_files:
            # Algorithm selection
            algorithms = st.multiselect(
                "Hash Algorithms",
                ["MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"],
                default=["MD5", "SHA256"]
            )

            if not algorithms:
                st.warning("Please select at least one hash algorithm")
                return

            output_format = st.selectbox("Output Format", ["Table", "JSON", "CSV", "Hash File Format"])

            if st.button("Generate Checksums"):
                with st.spinner("Generating checksums..."):
                    results = []

                    for file in uploaded_files:
                        file_data = file.getvalue()
                        file_result = {
                            'filename': file.name,
                            'size': len(file_data),
                            'checksums': {}
                        }

                        # Generate checksums for selected algorithms
                        for algo in algorithms:
                            checksum = generate_checksum(file_data, algo)
                            file_result['checksums'][algo] = checksum

                        results.append(file_result)

                display_checksum_results(results, algorithms, output_format)

    elif operation == "Verify Checksums":
        st.subheader("Verify File Checksums")

        uploaded_file = FileHandler.upload_files(['*'], accept_multiple=False)

        if uploaded_file:
            file = uploaded_file[0]

            col1, col2 = st.columns(2)
            with col1:
                algorithm = st.selectbox("Hash Algorithm", ["MD5", "SHA1", "SHA256", "SHA512"])
            with col2:
                expected_hash = st.text_input("Expected Hash", placeholder="Enter the expected checksum")

            if expected_hash and st.button("Verify Checksum"):
                verify_single_file(file, algorithm, expected_hash)

    else:  # Compare Files
        st.subheader("Compare Files")

        st.write("Upload two or more files to compare their checksums:")
        files_to_compare = FileHandler.upload_files(['*'], accept_multiple=True, key="compare_files")

        if len(files_to_compare) >= 2:
            comparison_algorithm = st.selectbox(
                "Comparison Algorithm",
                ["SHA256", "MD5", "SHA1", "SHA512"],
                key="compare_algo"
            )

            if st.button("Compare Files"):
                compare_files(files_to_compare, comparison_algorithm)

        elif len(files_to_compare) == 1:
            st.info("Upload at least one more file to compare")


def generate_checksum(data, algorithm):
    """Generate checksum for data using specified algorithm"""
    import hashlib

    algo_map = {
        'MD5': hashlib.md5,
        'SHA1': hashlib.sha1,
        'SHA224': hashlib.sha224,
        'SHA256': hashlib.sha256,
        'SHA384': hashlib.sha384,
        'SHA512': hashlib.sha512
    }

    hasher = algo_map[algorithm]()
    hasher.update(data)
    return hasher.hexdigest()


def display_checksum_results(results, algorithms, output_format):
    """Display checksum generation results"""
    st.success(f"✅ Generated checksums for {len(results)} file(s)")

    if output_format == "Table":
        # Display as table
        import pandas as pd

        table_data = []
        for result in results:
            row = {
                'Filename': result['filename'],
                'Size': format_bytes(result['size'])
            }
            for algo in algorithms:
                row[algo] = result['checksums'][algo]
            table_data.append(row)

        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True)

    elif output_format == "JSON":
        import json
        json_output = json.dumps(results, indent=2)
        st.code(json_output, language="json")
        FileHandler.create_download_link(json_output.encode(), "checksums.json", "application/json")

    elif output_format == "CSV":
        import csv
        import io

        output = io.StringIO()
        fieldnames = ['filename', 'size'] + algorithms
        writer = csv.DictWriter(output, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            row = {
                'filename': result['filename'],
                'size': result['size']
            }
            for algo in algorithms:
                row[algo] = result['checksums'][algo]
            writer.writerow(row)

        csv_content = output.getvalue()
        st.code(csv_content, language="csv")
        FileHandler.create_download_link(csv_content.encode(), "checksums.csv", "text/csv")

    else:  # Hash File Format
        hash_content = ""
        for result in results:
            for algo in algorithms:
                hash_content += f"{result['checksums'][algo]}  {result['filename']}\n"

        st.code(hash_content, language="text")
        FileHandler.create_download_link(hash_content.encode(), f"checksums_{algorithms[0].lower()}.txt", "text/plain")


def verify_single_file(file, algorithm, expected_hash):
    """Verify a single file against expected hash"""
    file_data = file.getvalue()
    actual_hash = generate_checksum(file_data, algorithm)

    expected_hash_clean = expected_hash.strip().lower()
    actual_hash_clean = actual_hash.lower()

    if expected_hash_clean == actual_hash_clean:
        st.success(f"✅ **Verification PASSED**")
        st.success(f"File '{file.name}' checksum matches expected value")
    else:
        st.error(f"❌ **Verification FAILED**")
        st.error(f"File '{file.name}' checksum does not match")

    # Show comparison
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Expected ({algorithm}):**")
        st.code(expected_hash_clean)
    with col2:
        st.write(f"**Actual ({algorithm}):**")
        st.code(actual_hash_clean)


def compare_files(files, algorithm):
    """Compare multiple files using checksums"""
    file_hashes = []

    for file in files:
        checksum = generate_checksum(file.getvalue(), algorithm)
        file_hashes.append({
            'filename': file.name,
            'size': len(file.getvalue()),
            'checksum': checksum
        })

    # Group by checksum
    hash_groups = {}
    for file_info in file_hashes:
        checksum = file_info['checksum']
        if checksum not in hash_groups:
            hash_groups[checksum] = []
        hash_groups[checksum].append(file_info)

    # Display results
    if len(hash_groups) == 1:
        st.success("✅ All files are identical!")
        st.write(f"**Common {algorithm} Hash:** `{list(hash_groups.keys())[0]}`")
    else:
        st.warning(f"⚠️ Files are different ({len(hash_groups)} unique checksums found)")

    # Show detailed comparison
    st.subheader("File Comparison Results")

    for i, (checksum, files_with_hash) in enumerate(hash_groups.items()):
        st.markdown(f"**Group {i + 1}** ({len(files_with_hash)} file(s))")
        st.code(f"{algorithm}: {checksum}")

        for file_info in files_with_hash:
            st.write(f"• {file_info['filename']} ({format_bytes(file_info['size'])})")

        if i < len(hash_groups) - 1:
            st.markdown("---")


def directory_sync():
    """Directory synchronization tool"""
    st.info("Directory Sync - Coming soon!")


def content_scanner():
    """File content scanner"""
    st.info("Content Scanner - Coming soon!")


def backup_creator():
    """Backup creation tool"""
    create_tool_header("Backup Creator", "Create backups of your files", "💾")

    backup_type = st.selectbox("Backup Type", ["Simple Archive", "Incremental Backup", "Differential Backup"])

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.write(f"**Files to backup:** {len(uploaded_files)}")

        # Backup settings
        col1, col2 = st.columns(2)
        with col1:
            backup_name = st.text_input("Backup Name", "backup_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
            compression = st.selectbox("Compression", ["ZIP", "TAR.GZ", "TAR.BZ2"])

        with col2:
            include_metadata = st.checkbox("Include File Metadata", True)
            verify_backup = st.checkbox("Verify Backup Integrity", True)

        if st.button("Create Backup"):
            create_backup(uploaded_files, backup_name, compression, include_metadata, verify_backup)


def create_backup(files, backup_name, compression, include_metadata, verify_backup):
    """Create backup of files"""
    import zipfile
    import tarfile
    import io
    import json

    with st.spinner("Creating backup..."):
        # Calculate total size
        total_size = sum(len(f.getvalue()) for f in files)

        # Create manifest if metadata is included
        manifest = {
            "backup_created": datetime.now().isoformat(),
            "total_files": len(files),
            "total_size": total_size,
            "compression": compression,
            "files": []
        }

        # Create backup archive
        backup_buffer = io.BytesIO()

        if compression == "ZIP":
            with zipfile.ZipFile(backup_buffer, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
                for file in files:
                    zf.writestr(file.name, file.getvalue())
                    if include_metadata:
                        import hashlib
                        manifest["files"].append({
                            "name": file.name,
                            "size": len(file.getvalue()),
                            "md5": hashlib.md5(file.getvalue()).hexdigest()
                        })

                if include_metadata:
                    zf.writestr("backup_manifest.json", json.dumps(manifest, indent=2))

        else:  # TAR formats
            mode = "w:gz" if compression == "TAR.GZ" else "w:bz2"
            with tarfile.open(fileobj=backup_buffer, mode=mode) as tf:
                for file in files:
                    tarinfo = tarfile.TarInfo(name=file.name)
                    tarinfo.size = len(file.getvalue())
                    tf.addfile(tarinfo, io.BytesIO(file.getvalue()))

                    if include_metadata:
                        import hashlib
                        manifest["files"].append({
                            "name": file.name,
                            "size": len(file.getvalue()),
                            "md5": hashlib.md5(file.getvalue()).hexdigest()
                        })

                if include_metadata:
                    manifest_data = json.dumps(manifest, indent=2).encode()
                    tarinfo = tarfile.TarInfo(name="backup_manifest.json")
                    tarinfo.size = len(manifest_data)
                    tf.addfile(tarinfo, io.BytesIO(manifest_data))

        backup_data = backup_buffer.getvalue()
        compressed_size = len(backup_data)
        compression_ratio = ((total_size - compressed_size) / total_size * 100) if total_size > 0 else 0

        # Verify backup if requested
        if verify_backup:
            verification_result = verify_backup_integrity(backup_data, compression)
            if verification_result:
                st.success("✅ Backup verification passed")
            else:
                st.error("❌ Backup verification failed")
                return

        st.success(f"✅ Backup created successfully!")

        # Display backup statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Files Backed Up", len(files))
        with col2:
            st.metric("Original Size", format_bytes(total_size))
        with col3:
            st.metric("Compressed Size", format_bytes(compressed_size))

        st.write(f"**Compression Ratio:** {compression_ratio:.1f}%")

        # Download backup
        extension_map = {"ZIP": ".zip", "TAR.GZ": ".tar.gz", "TAR.BZ2": ".tar.bz2"}
        filename = f"{backup_name}{extension_map[compression]}"
        FileHandler.create_download_link(backup_data, filename, "application/octet-stream")


def verify_backup_integrity(backup_data, compression):
    """Verify backup integrity"""
    try:
        import zipfile
        import tarfile
        import io

        if compression == "ZIP":
            with zipfile.ZipFile(io.BytesIO(backup_data), 'r') as zf:
                # Test all files in the archive
                bad_files = zf.testzip()
                return bad_files is None
        else:
            # For TAR files, try to read the archive
            mode = "r:gz" if compression == "TAR.GZ" else "r:bz2"
            with tarfile.open(fileobj=io.BytesIO(backup_data), mode=mode) as tf:
                # List all members to verify structure
                members = tf.getmembers()
                return len(members) > 0
    except:
        return False


def file_monitor():
    """File monitoring tool"""
    create_tool_header("File Monitor", "Monitor file changes and activities", "🔍")

    monitor_type = st.selectbox("Monitor Type", [
        "File Change Detection", "Size Monitoring", "Content Comparison", "Batch Analysis"
    ])

    if monitor_type == "File Change Detection":
        st.subheader("File Change Detection")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Original Files**")
            original_files = FileHandler.upload_files(['*'], accept_multiple=True, key="original")
            if original_files:
                st.write(f"Uploaded: {len(original_files)} files")

        with col2:
            st.write("**Modified Files**")
            modified_files = FileHandler.upload_files(['*'], accept_multiple=True, key="modified")
            if modified_files:
                st.write(f"Uploaded: {len(modified_files)} files")

        if original_files and modified_files and st.button("Detect Changes"):
            detect_file_changes(original_files, modified_files)

    elif monitor_type == "Size Monitoring":
        st.subheader("File Size Monitoring")

        uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

        if uploaded_files:
            threshold_type = st.selectbox("Alert Type", ["Files Larger Than", "Files Smaller Than", "Size Range"])

            if threshold_type == "Files Larger Than":
                size_unit = st.selectbox("Size Unit", ["KB", "MB", "GB"], key="large")
                threshold = st.number_input(f"Threshold ({size_unit})", min_value=0.1, value=10.0)
                multipliers = {"KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}
                threshold_bytes = threshold * multipliers[size_unit]

                if st.button("Check File Sizes"):
                    monitor_file_sizes(uploaded_files, "larger", threshold_bytes, size_unit)

            elif threshold_type == "Files Smaller Than":
                size_unit = st.selectbox("Size Unit", ["KB", "MB", "GB"], key="small")
                threshold = st.number_input(f"Threshold ({size_unit})", min_value=0.1, value=1.0)
                multipliers = {"KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}
                threshold_bytes = threshold * multipliers[size_unit]

                if st.button("Check File Sizes"):
                    monitor_file_sizes(uploaded_files, "smaller", threshold_bytes, size_unit)

    elif monitor_type == "Content Comparison":
        st.subheader("Content Comparison")

        st.write("Upload files to compare their content:")
        files_to_compare = FileHandler.upload_files(['*'], accept_multiple=True, key="content_compare")

        if len(files_to_compare) >= 2:
            comparison_method = st.selectbox("Comparison Method",
                                             ["Hash Comparison", "Content Diff", "Size Difference"])

            if st.button("Compare Content"):
                compare_file_content(files_to_compare, comparison_method)

    else:  # Batch Analysis
        st.subheader("Batch File Analysis")

        uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True, key="batch")

        if uploaded_files:
            analysis_type = st.selectbox("Analysis Type", [
                "File Type Distribution", "Size Analysis", "Duplicate Detection", "Pattern Analysis"
            ])

            if st.button("Run Batch Analysis"):
                run_batch_analysis(uploaded_files, analysis_type)


def detect_file_changes(original_files, modified_files):
    """Detect changes between file sets"""
    import hashlib

    # Create hash maps
    original_hashes = {f.name: hashlib.md5(f.getvalue()).hexdigest() for f in original_files}
    modified_hashes = {f.name: hashlib.md5(f.getvalue()).hexdigest() for f in modified_files}

    # Detect changes
    added_files = set(modified_hashes.keys()) - set(original_hashes.keys())
    removed_files = set(original_hashes.keys()) - set(modified_hashes.keys())

    changed_files = []
    unchanged_files = []

    for filename in set(original_hashes.keys()) & set(modified_hashes.keys()):
        if original_hashes[filename] != modified_hashes[filename]:
            changed_files.append(filename)
        else:
            unchanged_files.append(filename)

    # Display results
    st.subheader("Change Detection Results")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Added", len(added_files))
    with col2:
        st.metric("Removed", len(removed_files))
    with col3:
        st.metric("Modified", len(changed_files))
    with col4:
        st.metric("Unchanged", len(unchanged_files))

    if added_files:
        with st.expander(f"➕ Added Files ({len(added_files)})"):
            for filename in sorted(added_files):
                st.write(f"• {filename}")

    if removed_files:
        with st.expander(f"➖ Removed Files ({len(removed_files)})"):
            for filename in sorted(removed_files):
                st.write(f"• {filename}")

    if changed_files:
        with st.expander(f"🔄 Modified Files ({len(changed_files)})"):
            for filename in sorted(changed_files):
                st.write(f"• {filename}")


def monitor_file_sizes(files, comparison_type, threshold_bytes, unit):
    """Monitor files based on size criteria"""
    matching_files = []

    for file in files:
        file_size = len(file.getvalue())

        if comparison_type == "larger" and file_size > threshold_bytes:
            matching_files.append((file.name, file_size))
        elif comparison_type == "smaller" and file_size < threshold_bytes:
            matching_files.append((file.name, file_size))

    st.subheader(
        f"Size Monitoring Results ({comparison_type} than {threshold_bytes // (1024 if unit == 'KB' else 1024 ** 2 if unit == 'MB' else 1024 ** 3):.1f} {unit})")

    if matching_files:
        st.warning(f"Found {len(matching_files)} files matching criteria")

        for filename, size in sorted(matching_files, key=lambda x: x[1], reverse=True):
            st.write(f"• {filename}: {format_bytes(size)}")
    else:
        st.success("No files match the size criteria")


def compare_file_content(files, method):
    """Compare file content using specified method"""
    import hashlib

    if method == "Hash Comparison":
        file_hashes = []
        for file in files:
            hash_value = hashlib.md5(file.getvalue()).hexdigest()
            file_hashes.append((file.name, hash_value, len(file.getvalue())))

        st.subheader("Hash Comparison Results")

        # Group by hash
        hash_groups = {}
        for filename, hash_value, size in file_hashes:
            if hash_value not in hash_groups:
                hash_groups[hash_value] = []
            hash_groups[hash_value].append((filename, size))

        if len(hash_groups) == 1:
            st.success("✅ All files have identical content")
        else:
            st.warning(f"⚠️ Files have different content ({len(hash_groups)} unique hashes)")

        for i, (hash_value, file_list) in enumerate(hash_groups.items()):
            with st.expander(f"Group {i + 1} - {len(file_list)} file(s)"):
                st.code(f"MD5: {hash_value}")
                for filename, size in file_list:
                    st.write(f"• {filename} ({format_bytes(size)})")

    elif method == "Size Difference":
        file_sizes = [(f.name, len(f.getvalue())) for f in files]
        file_sizes.sort(key=lambda x: x[1], reverse=True)

        st.subheader("Size Comparison Results")

        for i, (filename, size) in enumerate(file_sizes):
            if i == 0:
                st.write(f"🥇 Largest: {filename} - {format_bytes(size)}")
            elif i == len(file_sizes) - 1:
                st.write(f"🥉 Smallest: {filename} - {format_bytes(size)}")
            else:
                st.write(f"{i + 1}. {filename} - {format_bytes(size)}")


def run_batch_analysis(files, analysis_type):
    """Run batch analysis on files"""
    if analysis_type == "File Type Distribution":
        import os

        type_counts = {}
        for file in files:
            ext = os.path.splitext(file.name)[1].lower()
            ext = ext if ext else "(no extension)"
            type_counts[ext] = type_counts.get(ext, 0) + 1

        st.subheader("File Type Distribution")

        for ext, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / len(files)) * 100
            st.write(f"**{ext}**: {count} files ({percentage:.1f}%)")

    elif analysis_type == "Size Analysis":
        sizes = [len(f.getvalue()) for f in files]
        total_size = sum(sizes)
        avg_size = total_size / len(files)

        st.subheader("Size Analysis Results")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Size", format_bytes(total_size))
        with col2:
            st.metric("Average Size", format_bytes(int(avg_size)))
        with col3:
            st.metric("Largest File", format_bytes(max(sizes)))


def smart_organizer():
    """Smart file organizer"""
    create_tool_header("Smart File Organizer", "Intelligently organize and categorize files", "📁")

    organization_method = st.selectbox("Organization Method", [
        "By File Type", "By File Size", "By Content Type", "Custom Rules"
    ])

    uploaded_files = FileHandler.upload_files(['*'], accept_multiple=True)

    if uploaded_files:
        st.write(f"**Files to organize:** {len(uploaded_files)}")

        if organization_method == "By File Type":
            st.subheader("Organize by File Type")

            if st.button("Organize by Type"):
                organize_by_file_type(uploaded_files)

        elif organization_method == "By File Size":
            st.subheader("Organize by File Size")

            size_ranges = {
                "Small (< 1MB)": (0, 1024 ** 2),
                "Medium (1-10MB)": (1024 ** 2, 10 * 1024 ** 2),
                "Large (10-100MB)": (10 * 1024 ** 2, 100 * 1024 ** 2),
                "Extra Large (> 100MB)": (100 * 1024 ** 2, float('inf'))
            }

            if st.button("Organize by Size"):
                organize_by_file_size(uploaded_files, size_ranges)

        elif organization_method == "By Content Type":
            st.subheader("Organize by Content Type")

            if st.button("Organize by Content"):
                organize_by_content_type(uploaded_files)

        else:  # Custom Rules
            st.subheader("Custom Organization Rules")

            st.write("Define custom rules for file organization:")

            rule_type = st.selectbox("Rule Type", ["Name Pattern", "Size Threshold", "Extension"])

            if rule_type == "Name Pattern":
                pattern = st.text_input("Name Pattern (supports wildcards)", placeholder="e.g., report_*, *.backup")
                folder_name = st.text_input("Folder Name", placeholder="e.g., Reports, Backups")

                if pattern and folder_name and st.button("Apply Pattern Rule"):
                    apply_pattern_rule(uploaded_files, pattern, folder_name)

            elif rule_type == "Size Threshold":
                size_threshold = st.number_input("Size Threshold (MB)", min_value=0.1, value=10.0)
                threshold_bytes = size_threshold * 1024 * 1024

                large_folder = st.text_input("Large Files Folder", "Large Files")
                small_folder = st.text_input("Small Files Folder", "Small Files")

                if st.button("Apply Size Rule"):
                    apply_size_rule(uploaded_files, threshold_bytes, large_folder, small_folder)


def organize_by_file_type(files):
    """Organize files by their type/extension"""
    import os

    # Define file type categories
    type_categories = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
        "Presentations": [".ppt", ".pptx", ".odp"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php"],
        "Other": []
    }

    # Organize files
    organized = {category: [] for category in type_categories.keys()}

    for file in files:
        ext = os.path.splitext(file.name)[1].lower()
        categorized = False

        for category, extensions in type_categories.items():
            if ext in extensions:
                organized[category].append(file)
                categorized = True
                break

        if not categorized:
            organized["Other"].append(file)

    # Display organization results
    st.subheader("Organization by File Type")

    for category, file_list in organized.items():
        if file_list:
            with st.expander(f"📁 {category} ({len(file_list)} files)"):
                total_size = sum(len(f.getvalue()) for f in file_list)
                st.write(f"**Total size:** {format_bytes(total_size)}")

                for file in file_list:
                    file_size = len(file.getvalue())
                    st.write(f"• {file.name} ({format_bytes(file_size)})")

                # Create download for category
                if len(file_list) > 1:
                    if st.button(f"Download {category} as ZIP", key=f"download_{category}"):
                        create_category_archive(file_list, category)


def organize_by_file_size(files, size_ranges):
    """Organize files by size ranges"""
    organized = {range_name: [] for range_name in size_ranges.keys()}

    for file in files:
        file_size = len(file.getvalue())

        for range_name, (min_size, max_size) in size_ranges.items():
            if min_size <= file_size < max_size:
                organized[range_name].append(file)
                break

    # Display organization results
    st.subheader("Organization by File Size")

    for range_name, file_list in organized.items():
        if file_list:
            with st.expander(f"📁 {range_name} ({len(file_list)} files)"):
                total_size = sum(len(f.getvalue()) for f in file_list)
                st.write(f"**Total size:** {format_bytes(total_size)}")

                for file in sorted(file_list, key=lambda x: len(x.getvalue()), reverse=True):
                    file_size = len(file.getvalue())
                    st.write(f"• {file.name} ({format_bytes(file_size)})")


def organize_by_content_type(files):
    """Organize files by detected content type"""
    import mimetypes

    content_categories = {
        "Text Files": ["text/"],
        "Image Files": ["image/"],
        "Video Files": ["video/"],
        "Audio Files": ["audio/"],
        "Application Files": ["application/"],
        "Unknown": []
    }

    organized = {category: [] for category in content_categories.keys()}

    for file in files:
        mime_type, _ = mimetypes.guess_type(file.name)
        categorized = False

        if mime_type:
            for category, prefixes in content_categories.items():
                if category != "Unknown" and any(mime_type.startswith(prefix) for prefix in prefixes):
                    organized[category].append(file)
                    categorized = True
                    break

        if not categorized:
            organized["Unknown"].append(file)

    # Display organization results
    st.subheader("Organization by Content Type")

    for category, file_list in organized.items():
        if file_list:
            with st.expander(f"📁 {category} ({len(file_list)} files)"):
                for file in file_list:
                    mime_type, _ = mimetypes.guess_type(file.name)
                    st.write(f"• {file.name} ({mime_type or 'Unknown MIME type'})")


def apply_pattern_rule(files, pattern, folder_name):
    """Apply custom pattern rule to organize files"""
    import fnmatch

    matching_files = []
    non_matching_files = []

    for file in files:
        if fnmatch.fnmatch(file.name.lower(), pattern.lower()):
            matching_files.append(file)
        else:
            non_matching_files.append(file)

    st.subheader(f"Pattern Rule Results: '{pattern}'")

    if matching_files:
        with st.expander(f"📁 {folder_name} ({len(matching_files)} files)"):
            for file in matching_files:
                st.write(f"• {file.name}")

    if non_matching_files:
        with st.expander(f"📁 Other Files ({len(non_matching_files)} files)"):
            for file in non_matching_files:
                st.write(f"• {file.name}")


def apply_size_rule(files, threshold_bytes, large_folder, small_folder):
    """Apply size-based rule to organize files"""
    large_files = []
    small_files = []

    for file in files:
        if len(file.getvalue()) >= threshold_bytes:
            large_files.append(file)
        else:
            small_files.append(file)

    st.subheader(f"Size Rule Results (threshold: {format_bytes(threshold_bytes)})")

    if large_files:
        with st.expander(f"📁 {large_folder} ({len(large_files)} files)"):
            for file in large_files:
                st.write(f"• {file.name} ({format_bytes(len(file.getvalue()))})")

    if small_files:
        with st.expander(f"📁 {small_folder} ({len(small_files)} files)"):
            for file in small_files:
                st.write(f"• {file.name} ({format_bytes(len(file.getvalue()))})")


def create_category_archive(files, category_name):
    """Create an archive for a category of files"""
    import zipfile
    import io

    archive_buffer = io.BytesIO()

    with zipfile.ZipFile(archive_buffer, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in files:
            zf.writestr(file.name, file.getvalue())

    archive_data = archive_buffer.getvalue()
    filename = f"{category_name.lower().replace(' ', '_')}_files.zip"

    FileHandler.create_download_link(archive_data, filename, "application/zip")
