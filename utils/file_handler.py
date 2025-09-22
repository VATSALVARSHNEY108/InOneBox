import streamlit as st
from typing import List, Optional, Dict, Any
import io
import zipfile
import json
import csv
from PIL import Image
import pandas as pd


class FileHandler:
    """Unified file handling utilities for all tools"""

    @staticmethod
    def upload_files(file_types: List[str], accept_multiple: bool = False,
                     max_size_mb: int = 200) -> Optional[List[Any]]:
        """Universal file upload with validation"""
        uploaded = st.file_uploader(
            "Choose files" if accept_multiple else "Choose file",
            type=file_types,
            accept_multiple_files=accept_multiple
        )

        if uploaded:
            files = uploaded if accept_multiple else [uploaded]
            validated_files = []

            for file in files:
                # Size validation
                if file.size > max_size_mb * 1024 * 1024:
                    st.error(f"File {file.name} is too large (max {max_size_mb}MB)")
                    continue

                # Type validation
                file_ext = file.name.split('.')[-1].lower()
                if file_ext not in [t.lower() for t in file_types]:
                    st.error(f"File {file.name} has unsupported type")
                    continue

                validated_files.append(file)

            return validated_files if validated_files else None
        return None

    @staticmethod
    def create_download_link(data: bytes, filename: str, mime_type: str = "application/octet-stream"):
        """Create download button for processed files"""
        return st.download_button(
            label=f"📥 Download {filename}",
            data=data,
            file_name=filename,
            mime=mime_type
        )

    @staticmethod
    def process_text_file(uploaded_file) -> str:
        """Process text file upload"""
        try:
            content = uploaded_file.read()
            if isinstance(content, bytes):
                return content.decode('utf-8')
            return content
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
            return ""

    @staticmethod
    def process_image_file(uploaded_file) -> Optional[Image.Image]:
        """Process image file upload"""
        try:
            return Image.open(uploaded_file)
        except Exception as e:
            st.error(f"Error opening image: {str(e)}")
            return None

    @staticmethod
    def process_csv_file(uploaded_file) -> Optional[pd.DataFrame]:
        """Process CSV file upload"""
        try:
            return pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error reading CSV: {str(e)}")
            return None

    @staticmethod
    def process_json_file(uploaded_file) -> Optional[Dict[str, Any]]:
        """Process JSON file upload"""
        try:
            content = uploaded_file.read()
            if isinstance(content, bytes):
                content = content.decode('utf-8')
            return json.loads(content)
        except Exception as e:
            st.error(f"Error parsing JSON: {str(e)}")
            return None

    @staticmethod
    def create_zip_archive(files: Dict[str, bytes]) -> bytes:
        """Create ZIP archive from multiple files"""
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for filename, content in files.items():
                zip_file.writestr(filename, content)

        return zip_buffer.getvalue()

    @staticmethod
    def batch_process_files(files: List[Any], processor_func, **kwargs):
        """Process multiple files with progress tracking"""
        results = []
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i, file in enumerate(files):
            status_text.text(f"Processing {file.name}...")
            try:
                result = processor_func(file, **kwargs)
                results.append({'file': file, 'result': result, 'success': True})
            except Exception as e:
                results.append({'file': file, 'error': str(e), 'success': False})

            progress_bar.progress((i + 1) / len(files))

        status_text.text("Processing complete!")
        return results

    @staticmethod
    def display_file_info(uploaded_file):
        """Display file information"""
        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**Size:** {uploaded_file.size:,} bytes")
        st.write(f"**Type:** {uploaded_file.type}")

    @staticmethod
    def save_processed_data(data: Any, filename: str, format_type: str = "json"):
        """Save processed data in various formats"""
        if format_type == "json":
            json_data = json.dumps(data, indent=2)
            return json_data.encode('utf-8'), "application/json"
        elif format_type == "csv" and isinstance(data, (list, dict)):
            if isinstance(data, dict):
                df = pd.DataFrame([data])
            else:
                df = pd.DataFrame(data)
            csv_data = df.to_csv(index=False)
            return csv_data.encode('utf-8'), "text/csv"
        elif format_type == "txt":
            if isinstance(data, str):
                return data.encode('utf-8'), "text/plain"
            else:
                return str(data).encode('utf-8'), "text/plain"
        else:
            return str(data).encode('utf-8'), "text/plain"
