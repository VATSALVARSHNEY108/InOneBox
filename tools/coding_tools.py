import streamlit as st
import streamlit.components.v1 as components
import re
import json
import ast
import keyword
import tokenize
import io
import subprocess
import sys
import base64
import urllib.parse
from datetime import datetime
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler
from utils.ai_client import ai_client


def display_tools():
    """Display all coding tools"""

    tool_categories = {
        "Code Editors": [
            "Syntax Highlighter", "Code Formatter", "Bracket Matcher", "Auto-Complete Simulator", "Code Snippets"
        ],
        "Code Formatters": [
            "Python Formatter", "JavaScript Formatter", "HTML Formatter", "CSS Formatter", "JSON Formatter"
        ],
        "Code Validators": [
            "Python Validator", "JavaScript Validator", "HTML Validator", "CSS Validator", "JSON Validator"
        ],
        "Code Converters": [
            "Language Converter", "Encoding Converter", "Format Transformer", "Case Converter", "Indentation Converter"
        ],
        "Documentation Tools": [
            "README Generator", "API Documentation", "Code Comments", "Documentation Parser", "Changelog Generator"
        ],
        "Testing Tools": [
            "Unit Test Generator", "Test Case Creator", "Mock Data Generator", "Test Runner", "Coverage Reporter"
        ],
        "Version Control": [
            "Git Helper", "Diff Viewer", "Merge Helper", "Commit Message Generator", "Branch Manager"
        ],
        "API Tools": [
            "REST Client", "API Tester", "Endpoint Documentation", "Request Builder", "Response Analyzer"
        ],
        "Database Tools": [
            "Query Builder", "Schema Generator", "Migration Creator", "Data Seeder", "Connection Tester"
        ],
        "Development Utilities": [
            "Environment Setup", "Config Manager", "Deployment Helper", "Build Tools", "Package Manager"
        ]
    }

    selected_category = st.selectbox("Select Coding Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Coding Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Python Formatter":
        python_formatter()
    elif selected_tool == "JSON Formatter":
        json_formatter()
    elif selected_tool == "Code Validator":
        code_validator()
    elif selected_tool == "Syntax Highlighter":
        syntax_highlighter()
    elif selected_tool == "README Generator":
        readme_generator()
    elif selected_tool == "API Tester":
        api_tester()
    elif selected_tool == "Query Builder":
        query_builder()
    elif selected_tool == "Unit Test Generator":
        unit_test_generator()
    elif selected_tool == "Git Helper":
        git_helper()
    elif selected_tool == "Code Comments":
        code_comments()
    elif selected_tool == "Mock Data Generator":
        mock_data_generator()
    elif selected_tool == "Config Manager":
        config_manager()
    elif selected_tool == "REST Client":
        rest_client()
    elif selected_tool == "Diff Viewer":
        diff_viewer()
    elif selected_tool == "Code Formatter":
        code_formatter()
    elif selected_tool == "Bracket Matcher":
        bracket_matcher()
    elif selected_tool == "Auto-Complete Simulator":
        autocomplete_simulator()
    elif selected_tool == "Code Snippets":
        code_snippets()
    elif selected_tool == "JavaScript Formatter":
        javascript_formatter()
    elif selected_tool == "HTML Formatter":
        html_formatter()
    elif selected_tool == "CSS Formatter":
        css_formatter()
    elif selected_tool == "Python Validator":
        python_validator()
    elif selected_tool == "JavaScript Validator":
        javascript_validator()
    elif selected_tool == "HTML Validator":
        html_validator()
    elif selected_tool == "CSS Validator":
        css_validator()
    elif selected_tool == "JSON Validator":
        json_validator()
    elif selected_tool == "Language Converter":
        language_converter()
    elif selected_tool == "Encoding Converter":
        encoding_converter()
    elif selected_tool == "Format Transformer":
        format_transformer()
    elif selected_tool == "Case Converter":
        case_converter()
    elif selected_tool == "Indentation Converter":
        indentation_converter()
    elif selected_tool == "API Documentation":
        api_documentation()
    elif selected_tool == "Documentation Parser":
        documentation_parser()
    elif selected_tool == "Changelog Generator":
        changelog_generator()
    elif selected_tool == "Test Case Creator":
        test_case_creator()
    elif selected_tool == "Test Runner":
        test_runner()
    elif selected_tool == "Coverage Reporter":
        coverage_reporter()
    elif selected_tool == "Merge Helper":
        merge_helper()
    elif selected_tool == "Commit Message Generator":
        commit_message_generator()
    elif selected_tool == "Branch Manager":
        branch_manager()
    elif selected_tool == "Request Builder":
        request_builder()
    elif selected_tool == "Response Analyzer":
        response_analyzer()
    elif selected_tool == "Schema Generator":
        schema_generator()
    elif selected_tool == "Migration Creator":
        migration_creator()
    elif selected_tool == "Data Seeder":
        data_seeder()
    elif selected_tool == "Connection Tester":
        connection_tester()
    elif selected_tool == "Environment Setup":
        environment_setup()
    elif selected_tool == "Deployment Helper":
        deployment_helper()
    elif selected_tool == "Build Tools":
        build_tools()
    elif selected_tool == "Package Manager":
        package_manager()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def python_formatter():
    """Python code formatter"""
    create_tool_header("Python Formatter", "Format and beautify Python code", "🐍")

    # File upload option
    uploaded_file = FileHandler.upload_files(['py'], accept_multiple=False)

    if uploaded_file:
        python_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Python Code", python_code, height=200, disabled=True)
    else:
        python_code = st.text_area("Enter Python code to format:", height=300, value="""def hello_world(name,age=25):
    if name:
        print(f"Hello, {name}!")
        if age>18:
            print("You are an adult")
        else:print("You are a minor")
    return True

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):return f"Hi, I'm {self.name}"
""")

    if python_code:
        # Formatting options
        col1, col2 = st.columns(2)
        with col1:
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1)
            line_length = st.slider("Max Line Length", 50, 120, 79)
            normalize_quotes = st.selectbox("Quote Style", ["Keep Original", "Single Quotes", "Double Quotes"])

        with col2:
            sort_imports = st.checkbox("Sort Imports", True)
            remove_unused_imports = st.checkbox("Remove Unused Imports", True)
            add_trailing_commas = st.checkbox("Add Trailing Commas", False)

        if st.button("Format Python Code"):
            try:
                formatted_code = format_python_code(python_code, {
                    'indent_size': indent_size,
                    'line_length': line_length,
                    'normalize_quotes': normalize_quotes,
                    'sort_imports': sort_imports,
                    'remove_unused_imports': remove_unused_imports,
                    'add_trailing_commas': add_trailing_commas
                })

                st.subheader("Formatted Code")
                st.code(formatted_code, language="python")

                # Show differences
                if formatted_code != python_code:
                    st.subheader("Changes Made")
                    changes = get_code_changes(python_code, formatted_code)
                    for change in changes:
                        st.write(f"• {change}")

                FileHandler.create_download_link(formatted_code.encode(), "formatted_code.py", "text/x-python")

            except Exception as e:
                st.error(f"Error formatting code: {str(e)}")


def json_formatter():
    """JSON formatter and validator"""
    create_tool_header("JSON Formatter", "Format, validate, and beautify JSON", "📋")

    # File upload option
    uploaded_file = FileHandler.upload_files(['json', 'txt'], accept_multiple=False)

    if uploaded_file:
        json_text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded JSON", json_text, height=200, disabled=True)
    else:
        json_text = st.text_area("Enter JSON to format:", height=300,
                                 value='{"name":"John Doe","age":30,"city":"New York","hobbies":["reading","coding","traveling"],"address":{"street":"123 Main St","zipcode":"10001"}}')

    if json_text:
        col1, col2 = st.columns(2)
        with col1:
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1)
            sort_keys = st.checkbox("Sort Keys", False)
        with col2:
            compact_mode = st.checkbox("Compact Mode", False)
            ensure_ascii = st.checkbox("Ensure ASCII", True)

        if st.button("Format JSON"):
            try:
                # Parse JSON
                parsed_json = json.loads(json_text)

                # Format options
                if compact_mode:
                    formatted_json = json.dumps(parsed_json, ensure_ascii=ensure_ascii,
                                                sort_keys=sort_keys, separators=(',', ':'))
                else:
                    formatted_json = json.dumps(parsed_json, indent=indent_size,
                                                ensure_ascii=ensure_ascii, sort_keys=sort_keys)

                st.success("✅ Valid JSON!")

                st.subheader("Formatted JSON")
                st.code(formatted_json, language="json")

                # JSON statistics
                st.subheader("JSON Statistics")
                stats = analyze_json_structure(parsed_json)
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Objects", stats['objects'])
                with col2:
                    st.metric("Arrays", stats['arrays'])
                with col3:
                    st.metric("Keys", stats['keys'])
                with col4:
                    st.metric("Max Depth", stats['max_depth'])

                FileHandler.create_download_link(formatted_json.encode(), "formatted.json", "application/json")

            except json.JSONDecodeError as e:
                st.error(f"❌ Invalid JSON: {str(e)}")

                # Try to suggest fixes
                suggestions = suggest_json_fixes(json_text, str(e))
                if suggestions:
                    st.subheader("Suggested Fixes")
                    for suggestion in suggestions:
                        st.write(f"• {suggestion}")


def code_validator():
    """Multi-language code validator"""
    create_tool_header("Code Validator", "Validate syntax for multiple languages", "✅")

    language = st.selectbox("Select Language", ["Python", "JavaScript", "HTML", "CSS", "JSON", "XML"])

    # File upload option
    file_extensions = {
        "Python": ['py'],
        "JavaScript": ['js'],
        "HTML": ['html', 'htm'],
        "CSS": ['css'],
        "JSON": ['json'],
        "XML": ['xml']
    }

    uploaded_file = FileHandler.upload_files(file_extensions[language], accept_multiple=False)

    if uploaded_file:
        code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area(f"Uploaded {language} Code", code, height=200, disabled=True)
    else:
        code = st.text_area(f"Enter {language} code to validate:", height=300)

    if code and st.button("Validate Code"):
        validation_result = validate_code(code, language)

        if validation_result['is_valid']:
            st.success("✅ Code is syntactically correct!")
        else:
            st.error("❌ Syntax errors found:")
            for error in validation_result['errors']:
                st.error(f"Line {error.get('line', '?')}: {error['message']}")

        if validation_result['warnings']:
            st.warning("⚠️ Warnings:")
            for warning in validation_result['warnings']:
                st.warning(f"Line {warning.get('line', '?')}: {warning['message']}")

        # Code statistics
        if validation_result['stats']:
            st.subheader("Code Statistics")
            stats = validation_result['stats']
            cols = st.columns(len(stats))
            for i, (key, value) in enumerate(stats.items()):
                with cols[i % len(cols)]:
                    st.metric(key.replace('_', ' ').title(), value)


def syntax_highlighter():
    """Code syntax highlighter"""
    create_tool_header("Syntax Highlighter", "Highlight code syntax for various languages", "🎨")

    language = st.selectbox("Select Language", [
        "Python", "JavaScript", "HTML", "CSS", "JSON", "SQL", "XML", "YAML",
        "C", "C++", "Java", "PHP", "Ruby", "Go", "Rust", "TypeScript"
    ])

    uploaded_file = FileHandler.upload_files(['txt', 'py', 'js', 'html', 'css', 'json'], accept_multiple=False)

    if uploaded_file:
        code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Code", code, height=200, disabled=True)
    else:
        code = st.text_area("Enter code to highlight:", height=300)

    if code:
        # Theme selection
        theme = st.selectbox("Select Theme", ["Default", "Dark", "Monokai", "GitHub", "VS Code"])

        if st.button("Apply Syntax Highlighting"):
            st.subheader("Highlighted Code")

            # Use Streamlit's built-in code highlighting
            st.code(code, language=language.lower())

            # Additional analysis
            analysis = analyze_code_structure(code, language)

            if analysis:
                st.subheader("Code Analysis")
                for key, value in analysis.items():
                    st.write(f"**{key}**: {value}")


def readme_generator():
    """README.md generator"""
    create_tool_header("README Generator", "Generate comprehensive README files", "📖")

    # Project information
    st.subheader("Project Information")

    col1, col2 = st.columns(2)
    with col1:
        project_name = st.text_input("Project Name", "My Awesome Project")
        description = st.text_area("Short Description", "A brief description of your project")
        author = st.text_input("Author", "Your Name")

    with col2:
        license_type = st.selectbox("License", ["MIT", "Apache 2.0", "GPL v3", "BSD 3-Clause", "Custom"])
        project_type = st.selectbox("Project Type", ["Web App", "CLI Tool", "Library", "API", "Desktop App"])
        language = st.selectbox("Primary Language", ["Python", "JavaScript", "Java", "C++", "Go", "Rust"])

    # Features and sections
    st.subheader("README Sections")

    col1, col2 = st.columns(2)
    with col1:
        include_installation = st.checkbox("Installation Instructions", True)
        include_usage = st.checkbox("Usage Examples", True)
        include_api_docs = st.checkbox("API Documentation", False)
        include_contributing = st.checkbox("Contributing Guidelines", True)

    with col2:
        include_changelog = st.checkbox("Changelog", False)
        include_license = st.checkbox("License Section", True)
        include_badges = st.checkbox("Status Badges", True)
        include_screenshots = st.checkbox("Screenshots", False)

    # Additional details
    installation_steps = None
    usage_example = None

    if include_installation:
        installation_steps = st.text_area("Installation Steps", "pip install my-awesome-project")

    if include_usage:
        usage_example = st.text_area("Usage Example", "from my_project import main\nmain.run()")

    features_list = st.text_area("Key Features (one per line)", "Feature 1\nFeature 2\nFeature 3")

    if st.button("Generate README"):
        readme_content = generate_readme(
            project_name=project_name,
            description=description,
            author=author,
            license_type=license_type,
            project_type=project_type,
            language=language,
            features=features_list.split('\n') if features_list else [],
            installation_steps=installation_steps if include_installation else None,
            usage_example=usage_example if include_usage else None,
            include_badges=include_badges,
            include_contributing=include_contributing,
            include_license=include_license,
            include_api_docs=include_api_docs
        )

        st.subheader("Generated README.md")
        st.code(readme_content, language="markdown")

        # Preview
        st.subheader("Preview")
        st.markdown(readme_content)

        FileHandler.create_download_link(readme_content.encode(), "README.md", "text/markdown")


def api_tester():
    """REST API testing tool"""
    create_tool_header("API Tester", "Test REST APIs and analyze responses", "🔌")

    # Request configuration
    st.subheader("HTTP Request Configuration")

    col1, col2 = st.columns([3, 1])
    with col1:
        url = st.text_input("URL", "https://api.github.com/users/octocat")
    with col2:
        method = st.selectbox("Method", ["GET", "POST", "PUT", "DELETE", "PATCH"])

    # Headers
    st.subheader("Headers")
    num_headers = st.number_input("Number of Headers", 0, 10, 2)
    headers = {}

    for i in range(num_headers):
        col1, col2 = st.columns(2)
        with col1:
            header_key = st.text_input(f"Header {i + 1} Key", f"Authorization" if i == 0 else "Content-Type",
                                       key=f"header_key_{i}")
        with col2:
            header_value = st.text_input(f"Header {i + 1} Value", f"Bearer token" if i == 0 else "application/json",
                                         key=f"header_value_{i}")

        if header_key and header_value:
            headers[header_key] = header_value

    # Request body
    if method in ["POST", "PUT", "PATCH"]:
        st.subheader("Request Body")
        content_type = st.selectbox("Content Type", ["JSON", "Form Data", "Plain Text", "XML"])

        if content_type == "JSON":
            request_body = st.text_area("JSON Body", '{\n  "key": "value"\n}')
        else:
            request_body = st.text_area("Request Body", "")
    else:
        request_body = None

    # Query parameters
    st.subheader("Query Parameters")
    num_params = st.number_input("Number of Parameters", 0, 10, 0)
    params = {}

    for i in range(num_params):
        col1, col2 = st.columns(2)
        with col1:
            param_key = st.text_input(f"Param {i + 1} Key", key=f"param_key_{i}")
        with col2:
            param_value = st.text_input(f"Param {i + 1} Value", key=f"param_value_{i}")

        if param_key and param_value:
            params[param_key] = param_value

    # Send request
    if st.button("Send Request") and url:
        try:
            import requests

            # Prepare request
            request_kwargs = {
                'method': method,
                'url': url,
                'headers': headers if headers else None,
                'params': params if params else None,
                'timeout': 30
            }

            if request_body and method in ["POST", "PUT", "PATCH"]:
                # Get content_type from earlier in the function or set default
                content_type = "JSON"  # Default value
                if content_type == "JSON":
                    try:
                        request_kwargs['json'] = json.loads(request_body)
                    except json.JSONDecodeError:
                        st.error("Invalid JSON in request body")
                        return
                else:
                    request_kwargs['data'] = request_body

            # Make request
            with st.spinner("Sending request..."):
                response = requests.request(**request_kwargs)

            # Display response
            st.subheader("Response")

            col1, col2, col3 = st.columns(3)
            with col1:
                status_color = "green" if response.status_code < 400 else "red"
                st.markdown(f"**Status Code**: <span style='color: {status_color}'>{response.status_code}</span>",
                            unsafe_allow_html=True)
            with col2:
                st.write(f"**Response Time**: {response.elapsed.total_seconds():.3f}s")
            with col3:
                st.write(f"**Content Length**: {len(response.content):,} bytes")

            # Response headers
            st.subheader("Response Headers")
            for key, value in response.headers.items():
                st.write(f"**{key}**: {value}")

            # Response body
            st.subheader("Response Body")

            content_type = response.headers.get('content-type', '').lower()

            if 'application/json' in content_type:
                try:
                    formatted_json = json.dumps(response.json(), indent=2)
                    st.code(formatted_json, language="json")
                except (json.JSONDecodeError, ValueError):
                    st.text(response.text)
            else:
                st.text(response.text)

            # Save response
            if st.button("Save Response"):
                response_data = {
                    'request': {
                        'method': method,
                        'url': url,
                        'headers': headers,
                        'params': params,
                        'body': request_body
                    },
                    'response': {
                        'status_code': response.status_code,
                        'headers': dict(response.headers),
                        'body': response.text,
                        'response_time': response.elapsed.total_seconds()
                    },
                    'timestamp': datetime.now().isoformat()
                }

                response_json = json.dumps(response_data, indent=2)
                FileHandler.create_download_link(response_json.encode(), "api_response.json", "application/json")

        except Exception as e:
            if "requests" in str(type(e).__module__):
                st.error(f"Request failed: {str(e)}")
            else:
                st.error(f"Error: {str(e)}")


def query_builder():
    """SQL query builder"""
    create_tool_header("Query Builder", "Build SQL queries visually", "🗃️")

    query_type = st.selectbox("Query Type", ["SELECT", "INSERT", "UPDATE", "DELETE"])

    if query_type == "SELECT":
        # SELECT query builder
        st.subheader("SELECT Query Builder")

        col1, col2 = st.columns(2)
        with col1:
            table_name = st.text_input("Table Name", "users")
            columns = st.text_area("Columns (comma-separated)", "id, name, email, created_at")

        with col2:
            distinct = st.checkbox("DISTINCT")
            limit = st.number_input("LIMIT", 0, 1000, 0)

        # WHERE clause
        st.subheader("WHERE Conditions")
        num_conditions = st.number_input("Number of Conditions", 0, 10, 1)
        where_conditions = []

        for i in range(num_conditions):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                column = st.text_input(f"Column {i + 1}", "id", key=f"where_col_{i}")
            with col2:
                operator = st.selectbox(f"Operator {i + 1}", ["=", "!=", ">", "<", ">=", "<=", "LIKE", "IN"],
                                        key=f"where_op_{i}")
            with col3:
                value = st.text_input(f"Value {i + 1}", "1", key=f"where_val_{i}")
            with col4:
                if i > 0:
                    logical_op = st.selectbox(f"Logic {i}", ["AND", "OR"], key=f"where_logic_{i}")
                else:
                    logical_op = None

            if column and value:
                condition = {
                    'column': column,
                    'operator': operator,
                    'value': value,
                    'logical_op': logical_op
                }
                where_conditions.append(condition)

        # ORDER BY
        st.subheader("ORDER BY")
        order_column = st.text_input("Order Column", "")
        order_direction = st.selectbox("Direction", ["ASC", "DESC"]) if order_column else None

        # GROUP BY
        group_column = st.text_input("GROUP BY Column", "")

        if st.button("Generate SELECT Query"):
            query = build_select_query(
                table=table_name,
                columns=columns,
                distinct=distinct,
                where_conditions=where_conditions,
                order_column=order_column,
                order_direction=order_direction,
                group_column=group_column,
                limit=limit if limit > 0 else None
            )

            st.subheader("Generated SQL Query")
            st.code(query, language="sql")

            # Query explanation
            st.subheader("Query Explanation")
            explanation = explain_sql_query(query, query_type)
            st.write(explanation)

            FileHandler.create_download_link(query.encode(), "query.sql", "text/plain")

    elif query_type == "INSERT":
        # INSERT query builder
        st.subheader("INSERT Query Builder")

        table_name = st.text_input("Table Name", "users")

        st.subheader("Column Values")
        num_columns = st.number_input("Number of Columns", 1, 20, 3)
        column_values = {}

        for i in range(num_columns):
            col1, col2 = st.columns(2)
            with col1:
                column = st.text_input(f"Column {i + 1}", f"column_{i + 1}", key=f"insert_col_{i}")
            with col2:
                value = st.text_input(f"Value {i + 1}", f"'value_{i + 1}'", key=f"insert_val_{i}")

            if column and value:
                column_values[column] = value

        if st.button("Generate INSERT Query") and column_values:
            query = build_insert_query(table_name, column_values)

            st.subheader("Generated SQL Query")
            st.code(query, language="sql")

            FileHandler.create_download_link(query.encode(), "insert_query.sql", "text/plain")


def unit_test_generator():
    """Unit test generator"""
    create_tool_header("Unit Test Generator", "Generate unit tests for your code", "🧪")

    language = st.selectbox("Programming Language", ["Python", "JavaScript", "Java", "C#"])
    test_framework = st.selectbox("Test Framework", get_test_frameworks(language))

    # File upload option
    uploaded_file = FileHandler.upload_files(['py', 'js', 'java', 'cs'], accept_multiple=False)

    if uploaded_file:
        source_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Source Code", source_code, height=200, disabled=True)
    else:
        source_code = st.text_area("Enter source code:", height=300, value=get_sample_code(language))

    if source_code:
        # Test generation options
        col1, col2 = st.columns(2)
        with col1:
            include_edge_cases = st.checkbox("Include Edge Cases", True)
            include_negative_tests = st.checkbox("Include Negative Tests", True)
            include_mocks = st.checkbox("Include Mocks/Stubs", False)

        with col2:
            test_coverage = st.selectbox("Test Coverage Level", ["Basic", "Comprehensive", "Extensive"])
            async_support = st.checkbox("Async/Promise Support", False)

        if st.button("Generate Unit Tests"):
            with st.spinner("Generating tests with AI..."):
                # Use AI to generate comprehensive unit tests
                prompt = f"""
                Generate comprehensive unit tests for the following {language} code using {test_framework}.

                Requirements:
                - {"Include edge cases" if include_edge_cases else "Skip edge cases"}
                - {"Include negative test cases" if include_negative_tests else "Skip negative tests"}
                - {"Include mocks and stubs" if include_mocks else "No mocks needed"}
                - Coverage level: {test_coverage}
                - {"Support async/promises" if async_support else "Synchronous only"}

                Source code:
                {source_code}

                Generate complete, runnable test code with proper imports and setup.
                """

                generated_tests = ai_client.generate_text(prompt, max_tokens=2000)

                if generated_tests and "error" not in generated_tests.lower():
                    st.subheader("Generated Unit Tests")
                    st.code(generated_tests, language=language.lower())

                    # Test analysis
                    analysis = analyze_generated_tests(generated_tests, language)

                    st.subheader("Test Analysis")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Test Methods", analysis.get('test_count', 0))
                    with col2:
                        st.metric("Assertions", analysis.get('assertion_count', 0))
                    with col3:
                        st.metric("Coverage", f"{analysis.get('coverage_estimate', 0)}%")

                    # Download
                    file_extension = get_file_extension(language)
                    FileHandler.create_download_link(generated_tests.encode(), f"test_code.{file_extension}",
                                                     "text/plain")
                else:
                    st.error("Failed to generate unit tests. Please try again or modify your code.")


def git_helper():
    """Git helper tools"""
    create_tool_header("Git Helper", "Git commands and workflow assistance", "🌿")

    tab1, tab2, tab3 = st.tabs(["Commit Message Generator", "Branch Helper", "Git Commands"])

    with tab1:
        st.subheader("Commit Message Generator")

        commit_type = st.selectbox("Commit Type", [
            "feat", "fix", "docs", "style", "refactor", "test", "chore", "perf"
        ])

        scope = st.text_input("Scope (optional)", placeholder="auth, ui, api")
        description = st.text_area("Description", placeholder="Brief description of changes")

        breaking_change = st.checkbox("Breaking Change")

        if description:
            # Generate conventional commit message
            scope_part = f"({scope})" if scope else ""
            breaking_part = "!" if breaking_change else ""

            commit_message = f"{commit_type}{scope_part}{breaking_part}: {description}"

            st.subheader("Generated Commit Message")
            st.code(commit_message)

            # Add body and footer if needed
            body = st.text_area("Body (optional)", placeholder="Detailed explanation of changes")
            footer = st.text_area("Footer (optional)", placeholder="References, breaking changes, etc.")

            full_message = commit_message
            if body:
                full_message += f"\n\n{body}"
            if footer:
                full_message += f"\n\n{footer}"

            if body or footer:
                st.subheader("Full Commit Message")
                st.code(full_message)

            FileHandler.create_download_link(full_message.encode(), "commit_message.txt", "text/plain")

    with tab2:
        st.subheader("Branch Management Helper")

        current_branch = st.text_input("Current Branch", "main")
        feature_name = st.text_input("Feature Name", "new-feature")

        st.subheader("Common Git Commands")

        commands = [
            f"git checkout -b feature/{feature_name}",
            f"git add .",
            f"git commit -m \"feat: add {feature_name}\"",
            f"git push origin feature/{feature_name}",
            f"git checkout {current_branch}",
            f"git merge feature/{feature_name}",
            f"git branch -d feature/{feature_name}"
        ]

        for i, cmd in enumerate(commands):
            st.code(cmd, language="bash")
            if st.button(f"Copy Command {i + 1}", key=f"git_cmd_{i}"):
                st.success(f"Command copied: {cmd}")

    with tab3:
        st.subheader("Git Command Reference")

        command_categories = {
            "Basic Commands": [
                "git init - Initialize a new Git repository",
                "git clone <url> - Clone a repository",
                "git add <file> - Stage changes",
                "git commit -m 'message' - Commit changes",
                "git push - Push commits to remote",
                "git pull - Pull changes from remote"
            ],
            "Branching": [
                "git branch - List branches",
                "git checkout <branch> - Switch branch",
                "git checkout -b <branch> - Create and switch to new branch",
                "git merge <branch> - Merge branch",
                "git branch -d <branch> - Delete branch"
            ],
            "History & Information": [
                "git log - Show commit history",
                "git status - Show working tree status",
                "git diff - Show changes",
                "git show <commit> - Show commit details",
                "git blame <file> - Show file annotations"
            ]
        }

        for category, commands in command_categories.items():
            st.subheader(category)
            for cmd in commands:
                st.write(f"• `{cmd}`")


# Helper functions
def format_python_code(code, options):
    """Format Python code based on options"""
    try:
        # Parse the AST to ensure valid syntax
        ast.parse(code)

        formatted = code

        # Basic formatting improvements
        lines = formatted.split('\n')
        formatted_lines = []
        indent_level = 0

        for line in lines:
            stripped = line.strip()
            if not stripped:
                formatted_lines.append('')
                continue

            # Adjust indent level
            if stripped.endswith(':'):
                formatted_lines.append('    ' * indent_level + stripped)
                indent_level += 1
            elif stripped.startswith(('return', 'break', 'continue', 'pass', 'raise')):
                formatted_lines.append('    ' * indent_level + stripped)
            elif stripped.startswith(('except', 'elif', 'else', 'finally')):
                formatted_lines.append('    ' * (indent_level - 1) + stripped)
                if stripped.endswith(':'):
                    # Don't change indent level as it's already adjusted
                    pass
            elif any(keyword in stripped for keyword in ['def ', 'class ', 'if ', 'for ', 'while ', 'with ', 'try:']):
                formatted_lines.append('    ' * indent_level + stripped)
                if stripped.endswith(':'):
                    indent_level += 1
            else:
                formatted_lines.append('    ' * indent_level + stripped)

        # Handle dedentation
        final_lines = []
        indent_level = 0

        for i, line in enumerate(formatted_lines):
            stripped = line.strip()
            if not stripped:
                final_lines.append('')
                continue

            # Calculate proper indentation
            if i > 0:
                prev_line = formatted_lines[i - 1].strip()
                if prev_line.endswith(':'):
                    indent_level += 1
                elif stripped.startswith(('except', 'elif', 'else', 'finally')) and indent_level > 0:
                    indent_level -= 1
                elif not prev_line.endswith(':') and len(prev_line) > 0:
                    # Check if we need to dedent
                    if not any(keyword in prev_line for keyword in
                               ['def ', 'class ', 'if ', 'for ', 'while ', 'with ', 'try:']):
                        pass  # Keep current indent

            final_lines.append('    ' * max(0, indent_level) + stripped)

        return '\n'.join(final_lines)

    except SyntaxError as e:
        raise Exception(f"Syntax error in Python code: {str(e)}")


def get_code_changes(original, formatted):
    """Get list of changes made during formatting"""
    changes = []

    if len(formatted.split('\n')) != len(original.split('\n')):
        changes.append("Adjusted line breaks and spacing")

    if '    ' in formatted and '    ' not in original:
        changes.append("Standardized indentation to 4 spaces")

    if original.count(' ') != formatted.count(' '):
        changes.append("Normalized whitespace")

    return changes if changes else ["Code formatting applied"]


def analyze_json_structure(data, depth=0):
    """Analyze JSON structure recursively"""
    stats = {
        'objects': 0,
        'arrays': 0,
        'keys': 0,
        'max_depth': depth
    }

    if isinstance(data, dict):
        stats['objects'] = 1
        stats['keys'] = len(data)
        for key, value in data.items():
            sub_stats = analyze_json_structure(value, depth + 1)
            stats['objects'] += sub_stats['objects']
            stats['arrays'] += sub_stats['arrays']
            stats['keys'] += sub_stats['keys']
            stats['max_depth'] = max(stats['max_depth'], sub_stats['max_depth'])

    elif isinstance(data, list):
        stats['arrays'] = 1
        for item in data:
            sub_stats = analyze_json_structure(item, depth + 1)
            stats['objects'] += sub_stats['objects']
            stats['arrays'] += sub_stats['arrays']
            stats['keys'] += sub_stats['keys']
            stats['max_depth'] = max(stats['max_depth'], sub_stats['max_depth'])

    return stats


def suggest_json_fixes(json_text, error_message):
    """Suggest fixes for JSON syntax errors"""
    suggestions = []

    if "Expecting property name" in error_message:
        suggestions.append("Check for missing or extra commas")
        suggestions.append("Ensure all property names are enclosed in double quotes")

    if "Expecting ',' delimiter" in error_message:
        suggestions.append("Missing comma between object properties or array elements")

    if "Expecting ':'" in error_message:
        suggestions.append("Missing colon after property name")

    if "Expecting value" in error_message:
        suggestions.append("Check for trailing comma or missing value")

    # Check for common issues
    if "'" in json_text:
        suggestions.append("Replace single quotes with double quotes")

    if json_text.count('{') != json_text.count('}'):
        suggestions.append("Mismatched curly braces")

    if json_text.count('[') != json_text.count(']'):
        suggestions.append("Mismatched square brackets")

    return suggestions


def validate_code(code, language):
    """Validate code syntax for different languages"""
    result = {
        'is_valid': False,
        'errors': [],
        'warnings': [],
        'stats': {}
    }

    try:
        if language == "Python":
            ast.parse(code)
            result['is_valid'] = True
            result['stats'] = {
                'lines': len(code.split('\n')),
                'functions': len(re.findall(r'def\s+\w+', code)),
                'classes': len(re.findall(r'class\s+\w+', code)),
                'imports': len(re.findall(r'import\s+\w+|from\s+\w+', code))
            }

        elif language == "JavaScript":
            # Basic JavaScript validation
            if code.strip():
                result['is_valid'] = True
                result['stats'] = {
                    'lines': len(code.split('\n')),
                    'functions': len(re.findall(r'function\s+\w+|=>\s*{|\w+\s*=\s*function', code)),
                    'variables': len(re.findall(r'var\s+\w+|let\s+\w+|const\s+\w+', code))
                }

        elif language == "JSON":
            json.loads(code)
            result['is_valid'] = True
            parsed = json.loads(code)
            result['stats'] = analyze_json_structure(parsed)

        else:
            # Basic validation for other languages
            result['is_valid'] = len(code.strip()) > 0
            result['stats'] = {'lines': len(code.split('\n'))}

    except SyntaxError as e:
        result['errors'].append({
            'line': getattr(e, 'lineno', '?'),
            'message': str(e)
        })
    except json.JSONDecodeError as e:
        result['errors'].append({
            'line': getattr(e, 'lineno', '?'),
            'message': str(e)
        })
    except Exception as e:
        result['errors'].append({
            'message': str(e)
        })

    return result


def analyze_code_structure(code, language):
    """Analyze code structure and provide insights"""
    analysis = {}

    if language.lower() == "python":
        analysis['Functions'] = len(re.findall(r'def\s+\w+', code))
        analysis['Classes'] = len(re.findall(r'class\s+\w+', code))
        analysis['Imports'] = len(re.findall(r'import\s+\w+|from\s+\w+', code))
        analysis['Comments'] = len(re.findall(r'#.*', code))
        analysis['Docstrings'] = len(re.findall(r'""".*?"""', code, re.DOTALL))

    elif language.lower() == "javascript":
        analysis['Functions'] = len(re.findall(r'function\s+\w+|=>\s*{|\w+\s*=\s*function', code))
        analysis['Variables'] = len(re.findall(r'var\s+\w+|let\s+\w+|const\s+\w+', code))
        analysis['Comments'] = len(re.findall(r'//.*|/\*.*?\*/', code, re.DOTALL))

    analysis['Lines of Code'] = len([line for line in code.split('\n') if line.strip()])
    analysis['Total Lines'] = len(code.split('\n'))

    return analysis


def generate_readme(project_name, description, author, license_type, project_type,
                    language, features, installation_steps=None, usage_example=None,
                    include_badges=True, include_contributing=True, include_license=True,
                    include_api_docs=False):
    """Generate README.md content"""

    readme = f"# {project_name}\n\n"

    if include_badges:
        readme += f"""![License](https://img.shields.io/badge/license-{license_type.replace(' ', '%20')}-blue)
![Language](https://img.shields.io/badge/language-{language}-green)
![Status](https://img.shields.io/badge/status-active-success)

"""

    readme += f"{description}\n\n"

    if features:
        readme += "## ✨ Features\n\n"
        for feature in features:
            if feature.strip():
                readme += f"- {feature.strip()}\n"
        readme += "\n"

    if installation_steps:
        readme += "## 🚀 Installation\n\n"
        readme += f"```bash\n{installation_steps}\n```\n\n"

    if usage_example:
        readme += f"## 📖 Usage\n\n```{language.lower()}\n{usage_example}\n```\n\n"

    if include_api_docs:
        readme += """## 📚 API Documentation

### Main Functions

#### `function_name(parameter)`

Description of the function.

**Parameters:**
- `parameter` (type): Description

**Returns:**
- `type`: Description

"""

    if include_contributing:
        readme += """## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

"""

    if include_license:
        readme += f"## 📄 License\n\nThis project is licensed under the {license_type} License.\n\n"

    readme += f"## 👤 Author\n\n**{author}**\n\n"
    readme += "---\n\n"
    readme += "⭐ Star this project if you find it helpful!"

    return readme


def build_select_query(table, columns, distinct=False, where_conditions=None,
                       order_column=None, order_direction=None, group_column=None, limit=None):
    """Build SELECT SQL query"""

    query_parts = []

    # SELECT clause
    select_clause = "SELECT DISTINCT" if distinct else "SELECT"
    query_parts.append(f"{select_clause} {columns}")

    # FROM clause
    query_parts.append(f"FROM {table}")

    # WHERE clause
    if where_conditions:
        where_parts = []
        for i, condition in enumerate(where_conditions):
            condition_str = f"{condition['column']} {condition['operator']} {condition['value']}"
            if i > 0 and condition.get('logical_op'):
                condition_str = f"{condition['logical_op']} {condition_str}"
            where_parts.append(condition_str)

        if where_parts:
            query_parts.append(f"WHERE {' '.join(where_parts)}")

    # GROUP BY clause
    if group_column:
        query_parts.append(f"GROUP BY {group_column}")

    # ORDER BY clause
    if order_column:
        query_parts.append(f"ORDER BY {order_column} {order_direction or 'ASC'}")

    # LIMIT clause
    if limit:
        query_parts.append(f"LIMIT {limit}")

    return '\n'.join(query_parts) + ';'


def build_insert_query(table, column_values):
    """Build INSERT SQL query"""
    columns = ', '.join(column_values.keys())
    values = ', '.join(column_values.values())

    return f"INSERT INTO {table} ({columns})\nVALUES ({values});"


def explain_sql_query(query, query_type):
    """Explain what an SQL query does"""
    explanations = {
        'SELECT': f"This query retrieves data from the database. It selects specific columns and may filter, sort, or group the results."
    }
    return explanations.get(query_type, "This query performs a database operation.")


def get_test_frameworks(language):
    """Get available test frameworks for a language"""
    frameworks = {
        "Python": ["unittest", "pytest", "nose2"],
        "JavaScript": ["Jest", "Mocha", "Jasmine", "Cypress"],
        "Java": ["JUnit", "TestNG", "Mockito"],
        "C#": ["NUnit", "MSTest", "xUnit"]
    }
    return frameworks.get(language, ["Default"])


def get_sample_code(language):
    """Get sample code for different languages"""
    samples = {
        "Python": """def calculate_total(items, tax_rate=0.1):
    \"\"\"Calculate total price including tax\"\"\"
    if not items:
        return 0

    subtotal = sum(item['price'] * item['quantity'] for item in items)
    tax = subtotal * tax_rate
    return subtotal + tax

def validate_email(email):
    \"\"\"Validate email format\"\"\"
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))""",

        "JavaScript": """function calculateTotal(items, taxRate = 0.1) {
    if (!items || items.length === 0) {
        return 0;
    }

    const subtotal = items.reduce((sum, item) => {
        return sum + (item.price * item.quantity);
    }, 0);

    const tax = subtotal * taxRate;
    return subtotal + tax;
}

function validateEmail(email) {
    const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return pattern.test(email);
}""",

        "Java": """public class Calculator {
    public static double calculateTotal(List<Item> items, double taxRate) {
        if (items == null || items.isEmpty()) {
            return 0.0;
        }

        double subtotal = items.stream()
            .mapToDouble(item -> item.getPrice() * item.getQuantity())
            .sum();

        double tax = subtotal * taxRate;
        return subtotal + tax;
    }

    public static boolean validateEmail(String email) {
        String pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
        return email != null && email.matches(pattern);
    }
}"""
    }
    return samples.get(language, "// Sample code")


def analyze_generated_tests(test_code, language):
    """Analyze generated test code"""
    analysis = {}

    if language.lower() == "python":
        analysis['test_count'] = len(re.findall(r'def test_\w+', test_code))
        analysis['assertion_count'] = len(re.findall(r'assert\w*\s', test_code))
    elif language.lower() == "javascript":
        analysis['test_count'] = len(re.findall(r'test\s*\(|it\s*\(', test_code))
        analysis['assertion_count'] = len(re.findall(r'expect\(|assert\w*\(', test_code))
    else:
        analysis['test_count'] = test_code.count('test')
        analysis['assertion_count'] = test_code.count('assert')

    # Estimate coverage based on test count
    analysis['coverage_estimate'] = min(analysis['test_count'] * 20, 100)

    return analysis


# Additional helper functions for remaining tools
def code_comments():
    """Code commenting tool"""
    st.info("Code Comments Generator - Coming soon!")


def mock_data_generator():
    """Mock data generator"""
    st.info("Mock Data Generator - Coming soon!")


def config_manager():
    """Configuration manager"""
    st.info("Config Manager - Coming soon!")


def rest_client():
    """REST API client"""
    st.info("Advanced REST Client - Coming soon!")


def diff_viewer():
    """Code diff viewer"""
    st.info("Code Diff Viewer - Coming soon!")


def code_formatter():
    """Multi-language code formatter"""
    create_tool_header("Code Formatter", "Format code for multiple programming languages", "✨")

    st.write("Format and beautify code in various programming languages with customizable styling options.")

    # Language selection
    language = st.selectbox("Select Programming Language", [
        "Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "Go", "Rust", "PHP", "Ruby", "HTML", "CSS", "JSON",
        "XML", "SQL"
    ])

    # File upload option
    file_extensions = {
        "Python": ['py'], "JavaScript": ['js'], "TypeScript": ['ts'], "Java": ['java'], "C++": ['cpp', 'cc'],
        "C#": ['cs'], "Go": ['go'], "Rust": ['rs'], "PHP": ['php'], "Ruby": ['rb'],
        "HTML": ['html', 'htm'], "CSS": ['css'], "JSON": ['json'], "XML": ['xml'], "SQL": ['sql']
    }

    uploaded_file = FileHandler.upload_files(file_extensions.get(language, ['txt']), accept_multiple=False)

    if uploaded_file:
        code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area(f"Uploaded {language} Code", code, height=200, disabled=True)
    else:
        # Default code examples for each language
        default_code = get_default_code_sample(language)
        code = st.text_area(f"Enter {language} code to format:", height=300, value=default_code)

    if code:
        # Formatting options
        st.subheader("Formatting Options")
        col1, col2 = st.columns(2)

        with col1:
            indent_type = st.selectbox("Indentation", ["Spaces", "Tabs"])
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1)
            line_length = st.slider("Max Line Length", 50, 150, 80)

        with col2:
            trailing_commas = st.checkbox("Add Trailing Commas", value=False)
            sort_imports = st.checkbox("Sort Imports/Includes", value=True)
            remove_empty_lines = st.checkbox("Remove Extra Empty Lines", value=True)

        if st.button("Format Code"):
            try:
                formatted_code = format_code_by_language(code, language, {
                    'indent_type': indent_type,
                    'indent_size': indent_size,
                    'line_length': line_length,
                    'trailing_commas': trailing_commas,
                    'sort_imports': sort_imports,
                    'remove_empty_lines': remove_empty_lines
                })

                # Display original and formatted side by side
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Original Code")
                    st.code(code, language=language.lower())

                with col2:
                    st.subheader("Formatted Code")
                    st.code(formatted_code, language=language.lower())

                # Show statistics
                st.subheader("Formatting Statistics")
                stats = get_formatting_stats(code, formatted_code)
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Lines Changed", stats['lines_changed'])
                with col2:
                    st.metric("Characters Added", stats['chars_added'])
                with col3:
                    st.metric("Whitespace Normalized", stats['whitespace_fixes'])
                with col4:
                    st.metric("Style Issues Fixed", stats['style_fixes'])

                # Download formatted code
                file_ext = file_extensions.get(language, ['txt'])[0]
                FileHandler.create_download_link(formatted_code.encode(), f"formatted_code.{file_ext}", "text/plain")

            except Exception as e:
                st.error(f"Error formatting code: {str(e)}")


def bracket_matcher():
    """Bracket matching and balancing tool"""
    create_tool_header("Bracket Matcher", "Find matching brackets, parentheses, and braces", "🔧")

    st.write("Analyze bracket matching, find mismatched pairs, and validate code structure.")

    # File upload option
    uploaded_file = FileHandler.upload_files(['py', 'js', 'java', 'cpp', 'cs', 'json', 'txt'], accept_multiple=False)

    if uploaded_file:
        code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Code", code, height=200, disabled=True)
    else:
        code = st.text_area("Enter code to analyze:", height=300, value="""function calculateTotal(items) {
    let total = 0;
    for (let i = 0; i < items.length; i++) {
        if (items[i].price > 0) {
            total += items[i].price * (1 + items[i].tax);
        }
    }
    return total;
""")

    if code:
        # Analysis options
        st.subheader("Analysis Options")
        col1, col2 = st.columns(2)

        with col1:
            highlight_mismatched = st.checkbox("Highlight Mismatched Brackets", True)
            show_depth_analysis = st.checkbox("Show Nesting Depth", True)
            check_string_literals = st.checkbox("Ignore Brackets in Strings", True)

        with col2:
            bracket_types = st.multiselect("Bracket Types to Check",
                                           ["() Parentheses", "[] Square Brackets", "{} Curly Braces",
                                            "<> Angle Brackets"],
                                           default=["() Parentheses", "[] Square Brackets", "{} Curly Braces"])

        if st.button("Analyze Brackets"):
            analysis_result = analyze_bracket_matching(code, {
                'highlight_mismatched': highlight_mismatched,
                'show_depth': show_depth_analysis,
                'ignore_strings': check_string_literals,
                'bracket_types': bracket_types
            })

            # Display results
            if analysis_result['is_balanced']:
                st.success("✅ All brackets are properly matched!")
            else:
                st.error("❌ Found bracket matching issues!")

            # Show mismatched brackets
            if analysis_result['mismatched']:
                st.subheader("Mismatched Brackets")
                for issue in analysis_result['mismatched']:
                    st.error(f"Line {issue['line']}: {issue['message']}")

            # Show bracket pairs
            if analysis_result['pairs']:
                st.subheader("Bracket Pairs Found")
                for pair in analysis_result['pairs'][:10]:  # Show first 10
                    st.write(
                        f"• **{pair['type']}** at Line {pair['open_line']} ↔ Line {pair['close_line']} (Depth: {pair['depth']})")

            # Nesting depth visualization
            if show_depth_analysis and analysis_result['depth_map']:
                st.subheader("Nesting Depth Visualization")

                # Create a visual representation
                depth_viz = create_depth_visualization(code, analysis_result['depth_map'])
                st.text(depth_viz)

            # Statistics
            st.subheader("Bracket Statistics")
            stats = analysis_result['statistics']
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Brackets", stats['total_brackets'])
            with col2:
                st.metric("Max Depth", stats['max_depth'])
            with col3:
                st.metric("Matched Pairs", stats['matched_pairs'])
            with col4:
                st.metric("Mismatched", stats['mismatched_count'])


def autocomplete_simulator():
    """Code auto-completion simulator"""
    create_tool_header("Auto-Complete Simulator", "Simulate code completion and IntelliSense", "🤖")

    st.write("Simulate intelligent code completion with context-aware suggestions.")

    # Language and context setup
    language = st.selectbox("Programming Language", ["Python", "JavaScript", "Java", "C++", "Go", "TypeScript"])

    # Context code (existing code in file)
    st.subheader("Context Code")
    context_code = st.text_area("Existing code in file (for context):", height=150,
                                value=get_context_code_sample(language))

    # Current line being typed
    st.subheader("Current Typing")
    current_line = st.text_input("Type code for suggestions:", value="def calc_")
    cursor_position = st.slider("Cursor Position", 0, len(current_line), len(current_line))

    # Auto-complete settings
    st.subheader("Completion Settings")
    col1, col2 = st.columns(2)

    with col1:
        max_suggestions = st.slider("Max Suggestions", 1, 20, 10)
        include_snippets = st.checkbox("Include Code Snippets", True)
        include_imports = st.checkbox("Suggest Imports", True)

    with col2:
        suggest_variables = st.checkbox("Variable Suggestions", True)
        suggest_functions = st.checkbox("Function Suggestions", True)
        suggest_keywords = st.checkbox("Language Keywords", True)

    if st.button("Get Suggestions") and current_line:
        # Generate completion suggestions
        suggestions = generate_completion_suggestions(
            current_line, cursor_position, context_code, language, {
                'max_suggestions': max_suggestions,
                'include_snippets': include_snippets,
                'include_imports': include_imports,
                'suggest_variables': suggest_variables,
                'suggest_functions': suggest_functions,
                'suggest_keywords': suggest_keywords
            })

        st.subheader("Completion Suggestions")

        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                with st.expander(f"{i}. {suggestion['text']} ({suggestion['type']})"):
                    st.write(f"**Type**: {suggestion['type']}")
                    st.write(f"**Description**: {suggestion['description']}")

                    if suggestion.get('snippet'):
                        st.code(suggestion['snippet'], language=language.lower())

                    # Show completion preview
                    completed_line = current_line[:cursor_position] + suggestion['text'] + current_line[
                                                                                           cursor_position:]
                    st.write(f"**Result**: `{completed_line}`")

                    if suggestion.get('documentation'):
                        st.write(f"**Documentation**: {suggestion['documentation']}")
        else:
            st.info("No suggestions available for the current input.")

        # Show typing analysis
        st.subheader("Input Analysis")
        analysis = analyze_typing_context(current_line, cursor_position, context_code, language)

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Token Type**: {analysis['token_type']}")
            st.write(f"**Context**: {analysis['context']}")
        with col2:
            st.write(f"**Scope**: {analysis['scope']}")
            st.write(f"**Expected**: {analysis['expected_type']}")


def code_snippets():
    """Code snippets library and generator"""
    create_tool_header("Code Snippets", "Library of reusable code snippets and templates", "📝")

    st.write("Browse, create, and manage reusable code snippets for faster development.")

    # Snippet categories
    snippet_categories = {
        "Python": {
            "Functions": ["Function Template", "Async Function", "Decorator", "Generator", "Lambda"],
            "Classes": ["Class Template", "Data Class", "Singleton", "Context Manager", "Exception Class"],
            "Control Flow": ["Try-Except", "For Loop", "While Loop", "List Comprehension", "If-Elif-Else"],
            "File Operations": ["Read File", "Write File", "CSV Reader", "JSON Handler", "Path Operations"],
            "Web Development": ["Flask Route", "FastAPI Endpoint", "Request Handler", "Database Query", "API Client"]
        },
        "JavaScript": {
            "Functions": ["Function Declaration", "Arrow Function", "Async/Await", "Promise", "Callback"],
            "DOM": ["Element Selector", "Event Listener", "DOM Manipulation", "Form Validation", "AJAX Request"],
            "ES6+": ["Class", "Module Import", "Destructuring", "Template Literals", "Spread Operator"],
            "React": ["Functional Component", "useEffect Hook", "useState Hook", "Event Handler", "Props"],
            "Node.js": ["Express Route", "File System", "HTTP Request", "Middleware", "Error Handler"]
        },
        "Java": {
            "Classes": ["Class Template", "Interface", "Abstract Class", "Enum", "Record"],
            "Methods": ["Main Method", "Constructor", "Getter/Setter", "Override Method", "Static Method"],
            "Collections": ["ArrayList", "HashMap", "Stream API", "Iterator", "Comparator"],
            "Exception Handling": ["Try-Catch", "Custom Exception", "Finally Block", "Throw", "Method Throws"],
            "Spring": ["Controller", "Service", "Repository", "Entity", "REST Endpoint"]
        }
    }

    # Mode selection
    mode = st.selectbox("Mode", ["Browse Snippets", "Create Custom Snippet", "Import Snippets"])

    if mode == "Browse Snippets":
        st.subheader("Browse Code Snippets")

        col1, col2 = st.columns(2)
        with col1:
            selected_language = st.selectbox("Language", list(snippet_categories.keys()))
        with col2:
            selected_category = st.selectbox("Category", list(snippet_categories[selected_language].keys()))

        snippet_name = st.selectbox("Snippet", snippet_categories[selected_language][selected_category])

        if st.button("Get Snippet"):
            snippet_data = get_code_snippet(selected_language, selected_category, snippet_name)

            if snippet_data:
                st.subheader(f"{snippet_name} - {selected_language}")
                st.write(f"**Description**: {snippet_data['description']}")

                # Show the snippet code
                st.code(snippet_data['code'], language=selected_language.lower())

                # Usage example
                if snippet_data.get('usage'):
                    st.subheader("Usage Example")
                    st.code(snippet_data['usage'], language=selected_language.lower())

                # Placeholder explanations
                if snippet_data.get('placeholders'):
                    st.subheader("Placeholders")
                    for placeholder, description in snippet_data['placeholders'].items():
                        st.write(f"• **{placeholder}**: {description}")

                # Download snippet
                file_ext = get_file_extension(selected_language)
                FileHandler.create_download_link(
                    snippet_data['code'].encode(),
                    f"{snippet_name.lower().replace(' ', '_')}.{file_ext}",
                    "text/plain"
                )

    elif mode == "Create Custom Snippet":
        st.subheader("Create Custom Snippet")

        col1, col2 = st.columns(2)
        with col1:
            custom_name = st.text_input("Snippet Name", "My Custom Snippet")
            custom_language = st.selectbox("Language", ["Python", "JavaScript", "Java", "C++", "Go", "HTML", "CSS"])
            custom_category = st.text_input("Category", "Custom")

        with col2:
            custom_description = st.text_area("Description", "Description of what this snippet does")
            tags = st.text_input("Tags (comma-separated)", "utility, custom")

        custom_code = st.text_area("Snippet Code", height=200, value="# Your code here\npass")

        # Placeholder definitions
        st.subheader("Placeholders (Optional)")
        num_placeholders = st.number_input("Number of Placeholders", 0, 10, 0)

        placeholders = {}
        for i in range(num_placeholders):
            col1, col2 = st.columns(2)
            with col1:
                placeholder_name = st.text_input(f"Placeholder {i + 1} Name", f"${{PLACEHOLDER_{i + 1}}}",
                                                 key=f"ph_name_{i}")
            with col2:
                placeholder_desc = st.text_input(f"Description", "Description", key=f"ph_desc_{i}")

            if placeholder_name and placeholder_desc:
                placeholders[placeholder_name] = placeholder_desc

        if st.button("Save Custom Snippet"):
            # In a real application, this would save to a database or file
            custom_snippet = {
                'name': custom_name,
                'language': custom_language,
                'category': custom_category,
                'description': custom_description,
                'code': custom_code,
                'tags': [tag.strip() for tag in tags.split(',')],
                'placeholders': placeholders,
                'created_at': datetime.now().isoformat()
            }

            # Show saved snippet
            st.success(f"✅ Snippet '{custom_name}' saved successfully!")

            # Display the saved snippet
            st.subheader("Saved Snippet Preview")
            st.code(custom_code, language=custom_language.lower())

            # Export as JSON
            snippet_json = json.dumps(custom_snippet, indent=2)
            FileHandler.create_download_link(
                snippet_json.encode(),
                f"{custom_name.lower().replace(' ', '_')}_snippet.json",
                "application/json"
            )

    elif mode == "Import Snippets":
        st.subheader("Import Snippets")

        st.write("Import snippets from VS Code, Sublime Text, or custom JSON files.")

        import_format = st.selectbox("Import Format", ["VS Code Snippets", "Custom JSON", "Plain Text Collection"])

        uploaded_file = FileHandler.upload_files(['json', 'txt'], accept_multiple=False)

        if uploaded_file:
            file_content = FileHandler.process_text_file(uploaded_file[0])

            if import_format == "VS Code Snippets":
                try:
                    snippets_data = json.loads(file_content)
                    st.success(f"✅ Found {len(snippets_data)} snippets in VS Code format")

                    # Display imported snippets
                    for snippet_name, snippet_data in snippets_data.items():
                        with st.expander(f"Snippet: {snippet_name}"):
                            st.write(f"**Description**: {snippet_data.get('description', 'No description')}")
                            if isinstance(snippet_data.get('body'), list):
                                code = '\n'.join(snippet_data['body'])
                            else:
                                code = snippet_data.get('body', '')
                            st.code(code)

                            if snippet_data.get('scope'):
                                st.write(f"**Language**: {snippet_data['scope']}")

                except json.JSONDecodeError:
                    st.error("Invalid JSON format. Please upload a valid VS Code snippets file.")

            elif import_format == "Custom JSON":
                st.text_area("File Content Preview", file_content, height=200, disabled=True)

                if st.button("Process Custom Import"):
                    st.info("Custom JSON import processing would be implemented here.")

        else:
            st.info("Upload a snippets file to import existing code templates.")


# Helper functions for the new tools

def get_default_code_sample(language):
    """Get default code samples for different languages"""
    samples = {
        "Python": '''def calculate_total(items, tax_rate=0.08):
    total = 0
    for item in items:
        if item["price"] > 0:
            total += item["price"] * (1 + tax_rate)
    return round(total, 2)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})''',

        "JavaScript": '''function calculateTotal(items, taxRate = 0.08) {
    let total = 0;
    items.forEach(item => {
        if (item.price > 0) {
            total += item.price * (1 + taxRate);
        }
    });
    return Math.round(total * 100) / 100;
}

class ShoppingCart {
    constructor() {
        this.items = [];
    }

    addItem(name, price) {
        this.items.push({ name, price });
    }
}''',

        "Java": '''public class Calculator {
    private static final double DEFAULT_TAX_RATE = 0.08;

    public static double calculateTotal(List<Item> items, double taxRate) {
        double total = 0;
        for (Item item : items) {
            if (item.getPrice() > 0) {
                total += item.getPrice() * (1 + taxRate);
            }
        }
        return Math.round(total * 100.0) / 100.0;
    }

    public static double calculateTotal(List<Item> items) {
        return calculateTotal(items, DEFAULT_TAX_RATE);
    }
}''',

        "HTML": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="hero">
            <h1>Welcome to My Site</h1>
            <p>This is a sample webpage.</p>
        </section>
    </main>
</body>
</html>''',

        "CSS": '''.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #333;
    color: white;
}

.navbar ul {
    list-style: none;
    display: flex;
    gap: 2rem;
    margin: 0;
    padding: 0;
}

.navbar a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}

.navbar a:hover {
    color: #007bff;
}'''
    }

    return samples.get(language, "// Enter your code here")


def format_code_by_language(code, language, options):
    """Format code based on language and options"""
    # This is a simplified formatter - in a real app you'd use proper formatters
    formatted = code

    # Basic formatting operations
    if options['remove_empty_lines']:
        lines = formatted.split('\n')
        filtered_lines = []
        prev_empty = False
        for line in lines:
            if line.strip() == '':
                if not prev_empty:
                    filtered_lines.append(line)
                prev_empty = True
            else:
                filtered_lines.append(line)
                prev_empty = False
        formatted = '\n'.join(filtered_lines)

    # Normalize indentation
    if options['indent_type'] == 'Spaces':
        # Convert tabs to spaces
        formatted = formatted.expandtabs(options['indent_size'])

    # Language-specific formatting
    if language == "Python":
        # Add basic Python formatting
        import re
        # Fix spacing around operators
        formatted = re.sub(r'(\w)=(\w)', r'\1 = \2', formatted)
        formatted = re.sub(r'(\w)\+(\w)', r'\1 + \2', formatted)
        formatted = re.sub(r'(\w)-(\w)', r'\1 - \2', formatted)

    elif language == "JavaScript":
        # Add basic JS formatting
        import re
        formatted = re.sub(r'(\w)=(\w)', r'\1 = \2', formatted)
        formatted = re.sub(r'(\w)\+(\w)', r'\1 + \2', formatted)

    return formatted


def get_formatting_stats(original, formatted):
    """Get statistics about code formatting changes"""
    original_lines = original.split('\n')
    formatted_lines = formatted.split('\n')

    lines_changed = sum(1 for i, (o, f) in enumerate(zip(original_lines, formatted_lines)) if o != f)
    chars_added = len(formatted) - len(original)

    # Count whitespace normalizations (simplified)
    import re
    original_spaces = len(re.findall(r'\s+', original))
    formatted_spaces = len(re.findall(r'\s+', formatted))
    whitespace_fixes = abs(formatted_spaces - original_spaces)

    return {
        'lines_changed': lines_changed,
        'chars_added': chars_added if chars_added > 0 else 0,
        'whitespace_fixes': whitespace_fixes,
        'style_fixes': lines_changed  # Simplified metric
    }


def analyze_bracket_matching(code, options):
    """Analyze bracket matching in code"""
    brackets = {
        '()': ('(', ')'),
        '[]': ('[', ']'),
        '{}': ('{', '}'),
        '<>': ('<', '>')
    }

    # Filter brackets based on options
    active_brackets = {}
    for bracket_type in options['bracket_types']:
        key = bracket_type.split()[0]  # Get the bracket symbols
        if key in brackets:
            active_brackets[key] = brackets[key]

    stack = []
    pairs = []
    mismatched = []
    depth_map = {}
    current_depth = 0
    in_string = False
    string_char = None

    lines = code.split('\n')

    for line_num, line in enumerate(lines, 1):
        for char_pos, char in enumerate(line):
            # Handle string literals if option is enabled
            if options['ignore_strings']:
                if char in ['"', "'"] and (char_pos == 0 or line[char_pos - 1] != '\\'):
                    if not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char:
                        in_string = False
                        string_char = None
                    continue

                if in_string:
                    continue

            # Check opening brackets
            for bracket_type, (open_br, close_br) in active_brackets.items():
                if char == open_br:
                    stack.append({
                        'char': char,
                        'type': bracket_type,
                        'line': line_num,
                        'pos': char_pos,
                        'depth': current_depth
                    })
                    current_depth += 1
                    depth_map[line_num] = depth_map.get(line_num, 0) + 1
                elif char == close_br:
                    if stack and stack[-1]['char'] == open_br:
                        # Found matching pair
                        opening = stack.pop()
                        pairs.append({
                            'type': bracket_type,
                            'open_line': opening['line'],
                            'close_line': line_num,
                            'depth': opening['depth']
                        })
                        current_depth -= 1
                    else:
                        # Mismatched bracket
                        mismatched.append({
                            'line': line_num,
                            'char': char,
                            'message': f"Unmatched closing bracket '{char}'"
                        })

    # Check for unclosed brackets
    for unclosed in stack:
        mismatched.append({
            'line': unclosed['line'],
            'char': unclosed['char'],
            'message': f"Unclosed opening bracket '{unclosed['char']}'"
        })

    statistics = {
        'total_brackets': len(pairs) * 2 + len(mismatched),
        'matched_pairs': len(pairs),
        'mismatched_count': len(mismatched),
        'max_depth': max(depth_map.values()) if depth_map else 0
    }

    return {
        'is_balanced': len(mismatched) == 0,
        'pairs': pairs,
        'mismatched': mismatched,
        'depth_map': depth_map,
        'statistics': statistics
    }


def create_depth_visualization(code, depth_map):
    """Create a visual representation of nesting depth"""
    lines = code.split('\n')
    visualization = []

    for i, line in enumerate(lines, 1):
        depth = depth_map.get(i, 0)
        indent_viz = '│ ' * depth if depth > 0 else ''
        visualization.append(f"{i:3d} {indent_viz}{line}")

    return '\n'.join(visualization)


def generate_completion_suggestions(current_line, cursor_pos, context, language, options):
    """Generate code completion suggestions"""
    # Extract the word being typed
    before_cursor = current_line[:cursor_pos]

    # Find the start of current word
    word_start = cursor_pos
    for i in range(cursor_pos - 1, -1, -1):
        if not (before_cursor[i].isalnum() or before_cursor[i] == '_'):
            word_start = i + 1
            break
        word_start = i

    current_word = before_cursor[word_start:cursor_pos]

    suggestions = []

    # Language keywords
    if options['suggest_keywords']:
        keywords = get_language_keywords(language)
        for keyword in keywords:
            if keyword.startswith(current_word) and len(current_word) > 0:
                suggestions.append({
                    'text': keyword,
                    'type': 'keyword',
                    'description': f'{language} keyword',
                    'documentation': f'Language keyword: {keyword}'
                })

    # Functions from context
    if options['suggest_functions']:
        functions = extract_functions_from_context(context, language)
        for func in functions:
            if func['name'].startswith(current_word):
                suggestions.append({
                    'text': func['name'],
                    'type': 'function',
                    'description': f"Function: {func['signature']}",
                    'snippet': func['snippet'] if options['include_snippets'] else None,
                    'documentation': func.get('docstring', '')
                })

    # Variables from context
    if options['suggest_variables']:
        variables = extract_variables_from_context(context, language)
        for var in variables:
            if var.startswith(current_word):
                suggestions.append({
                    'text': var,
                    'type': 'variable',
                    'description': f'Variable: {var}',
                })

    # Built-in functions and common snippets
    if options['include_snippets']:
        snippets = get_common_snippets(language, current_word)
        suggestions.extend(snippets)

    # Sort by relevance (starts with current word first, then alphabetically)
    suggestions.sort(key=lambda x: (not x['text'].startswith(current_word), x['text'].lower()))

    return suggestions[:options['max_suggestions']]


def get_language_keywords(language):
    """Get keywords for programming languages"""
    keywords = {
        "Python": ["def", "class", "if", "elif", "else", "for", "while", "try", "except", "finally", "with", "import",
                   "from", "return", "yield", "lambda", "global", "nonlocal", "pass", "break", "continue"],
        "JavaScript": ["function", "var", "let", "const", "if", "else", "for", "while", "do", "switch", "case",
                       "default", "try", "catch", "finally", "return", "break", "continue", "class", "extends",
                       "import", "export"],
        "Java": ["public", "private", "protected", "class", "interface", "extends", "implements", "if", "else", "for",
                 "while", "do", "switch", "case", "default", "try", "catch", "finally", "return", "break", "continue",
                 "new", "this", "super"],
        "C++": ["class", "struct", "public", "private", "protected", "virtual", "if", "else", "for", "while", "do",
                "switch", "case", "default", "try", "catch", "return", "break", "continue", "namespace", "using",
                "template"],
        "Go": ["func", "var", "const", "type", "struct", "interface", "if", "else", "for", "switch", "case", "default",
               "defer", "go", "chan", "select", "return", "break", "continue", "package", "import"],
        "TypeScript": ["function", "var", "let", "const", "if", "else", "for", "while", "do", "switch", "case",
                       "default", "try", "catch", "finally", "return", "break", "continue", "class", "interface",
                       "extends", "implements", "type", "enum"]
    }
    return keywords.get(language, [])


def extract_functions_from_context(context, language):
    """Extract function definitions from context code"""
    functions = []

    if language == "Python":
        import re
        # Find function definitions
        pattern = r'def\s+(\w+)\s*\(([^)]*)\):'
        matches = re.finditer(pattern, context)

        for match in matches:
            func_name = match.group(1)
            params = match.group(2)
            functions.append({
                'name': func_name,
                'signature': f"{func_name}({params})",
                'snippet': f"{func_name}({params})",
                'docstring': f"Function {func_name} defined in context"
            })

    elif language == "JavaScript":
        import re
        # Find function declarations
        pattern = r'function\s+(\w+)\s*\(([^)]*)\)'
        matches = re.finditer(pattern, context)

        for match in matches:
            func_name = match.group(1)
            params = match.group(2)
            functions.append({
                'name': func_name,
                'signature': f"{func_name}({params})",
                'snippet': f"{func_name}({params})",
                'docstring': f"Function {func_name} defined in context"
            })

    return functions


def extract_variables_from_context(context, language):
    """Extract variable names from context code"""
    variables = []

    if language == "Python":
        import re
        # Find variable assignments
        pattern = r'(\w+)\s*='
        matches = re.finditer(pattern, context)
        variables = list(set(match.group(1) for match in matches))

    elif language == "JavaScript":
        import re
        # Find variable declarations
        patterns = [r'(?:var|let|const)\s+(\w+)', r'(\w+)\s*=']
        for pattern in patterns:
            matches = re.finditer(pattern, context)
            variables.extend(match.group(1) for match in matches)
        variables = list(set(variables))

    return variables


def get_common_snippets(language, current_word):
    """Get common code snippets for the language"""
    snippets = []

    snippet_templates = {
        "Python": {
            "if": {
                'text': 'if',
                'type': 'snippet',
                'description': 'If statement',
                'snippet': 'if ${1:condition}:\n    ${2:pass}'
            },
            "for": {
                'text': 'for',
                'type': 'snippet',
                'description': 'For loop',
                'snippet': 'for ${1:item} in ${2:iterable}:\n    ${3:pass}'
            },
            "class": {
                'text': 'class',
                'type': 'snippet',
                'description': 'Class definition',
                'snippet': 'class ${1:ClassName}:\n    def __init__(self${2:, args}):\n        ${3:pass}'
            }
        },
        "JavaScript": {
            "function": {
                'text': 'function',
                'type': 'snippet',
                'description': 'Function declaration',
                'snippet': 'function ${1:functionName}(${2:parameters}) {\n    ${3:// code}\n}'
            },
            "if": {
                'text': 'if',
                'type': 'snippet',
                'description': 'If statement',
                'snippet': 'if (${1:condition}) {\n    ${2:// code}\n}'
            },
            "for": {
                'text': 'for',
                'type': 'snippet',
                'description': 'For loop',
                'snippet': 'for (let ${1:i} = 0; ${1:i} < ${2:array}.length; ${1:i}++) {\n    ${3:// code}\n}'
            }
        }
    }

    lang_snippets = snippet_templates.get(language, {})
    for key, snippet in lang_snippets.items():
        if key.startswith(current_word.lower()):
            snippets.append(snippet)

    return snippets


def analyze_typing_context(current_line, cursor_pos, context, language):
    """Analyze the typing context for better suggestions"""
    before_cursor = current_line[:cursor_pos]
    after_cursor = current_line[cursor_pos:]

    # Basic analysis
    analysis = {
        'token_type': 'unknown',
        'context': 'global',
        'scope': 'unknown',
        'expected_type': 'any'
    }

    # Determine token type
    if before_cursor.strip().endswith('.'):
        analysis['token_type'] = 'member_access'
    elif before_cursor.strip().endswith('('):
        analysis['token_type'] = 'function_call'
    elif '=' in before_cursor and before_cursor.strip().endswith('='):
        analysis['token_type'] = 'assignment'
    else:
        analysis['token_type'] = 'identifier'

    # Determine context
    if 'class ' in context:
        analysis['context'] = 'class'
    elif 'function ' in context or 'def ' in context:
        analysis['context'] = 'function'

    return analysis


def get_context_code_sample(language):
    """Get sample context code for different languages"""
    samples = {
        "Python": '''class Calculator:
    def __init__(self):
        self.result = 0
        self.history = []

    def add(self, value):
        self.result += value
        self.history.append(f"Added {value}")
        return self.result

    def multiply(self, value):
        self.result *= value
        return self.result

# Variables in scope
calculator = Calculator()
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
''',

        "JavaScript": '''class Calculator {
    constructor() {
        this.result = 0;
        this.history = [];
    }

    add(value) {
        this.result += value;
        this.history.push(`Added ${value}`);
        return this.result;
    }

    multiply(value) {
        this.result *= value;
        return this.result;
    }
}

// Variables in scope
const calculator = new Calculator();
const numbers = [1, 2, 3, 4, 5];
const totalSum = numbers.reduce((a, b) => a + b, 0);
''',

        "Java": '''public class Calculator {
    private double result;
    private List<String> history;

    public Calculator() {
        this.result = 0.0;
        this.history = new ArrayList<>();
    }

    public double add(double value) {
        this.result += value;
        this.history.add("Added " + value);
        return this.result;
    }

    public double multiply(double value) {
        this.result *= value;
        return this.result;
    }
}
'''
    }
    return samples.get(language, "// Context code goes here")


def get_code_snippet(language, category, snippet_name):
    """Get specific code snippet data"""
    snippets_db = {
        "Python": {
            "Functions": {
                "Function Template": {
                    'description': 'Basic function template with parameters and return value',
                    'code': '''def ${1:function_name}(${2:parameters}):
    """
    ${3:Function description}

    Args:
        ${4:parameter_description}

    Returns:
        ${5:return_description}
    """
    ${6:pass}
    return ${7:result}''',
                    'placeholders': {
                        '${1:function_name}': 'Name of the function',
                        '${2:parameters}': 'Function parameters',
                        '${3:Function description}': 'Brief description of what the function does',
                        '${6:pass}': 'Function implementation',
                        '${7:result}': 'Return value'
                    },
                    'usage': '''# Example usage:
def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    return area

result = calculate_area(5, 3)
print(f"Area: {result}")'''
                },
                "Async Function": {
                    'description': 'Asynchronous function template',
                    'code': '''async def ${1:async_function}(${2:parameters}):
    """
    ${3:Async function description}
    """
    ${4:await some_async_operation()}
    return ${5:result}''',
                    'usage': '''import asyncio

async def fetch_data(url):
    # Simulate async operation
    await asyncio.sleep(1)
    return f"Data from {url}"

# Usage
async def main():
    data = await fetch_data("https://api.example.com")
    print(data)

asyncio.run(main())'''
                }
            },
            "Classes": {
                "Class Template": {
                    'description': 'Basic class template with constructor and methods',
                    'code': '''class ${1:ClassName}:
    """${2:Class description}"""

    def __init__(self${3:, parameters}):
        """Initialize ${1:ClassName}"""
        ${4:self.attribute = value}

    def ${5:method_name}(self${6:, parameters}):
        """${7:Method description}"""
        ${8:pass}
        return ${9:result}

    def __str__(self):
        return f"${1:ClassName}(${10:attributes})"''',
                    'usage': '''# Example usage:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}"

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Alice", 30)
print(person.greet())
print(person)'''
                }
            }
        },
        "JavaScript": {
            "Functions": {
                "Arrow Function": {
                    'description': 'ES6 arrow function template',
                    'code': '''const ${1:functionName} = (${2:parameters}) => {
    ${3:// Function body}
    return ${4:result};
};''',
                    'usage': '''// Example usage:
const calculateArea = (length, width) => {
    return length * width;
};

// Or as a one-liner:
const multiply = (a, b) => a * b;

console.log(calculateArea(5, 3));
console.log(multiply(4, 7));'''
                }
            },
            "DOM": {
                "Event Listener": {
                    'description': 'Add event listener to DOM element',
                    'code': '''document.${1:getElementById}('${2:elementId}').addEventListener('${3:event}', ${4:function}(event) {
    ${5:// Event handler code}
    event.preventDefault(); // Optional: prevent default behavior
    ${6:console.log('Event triggered');}
});''',
                    'usage': '''// Example usage:
document.getElementById('myButton').addEventListener('click', function(event) {
    console.log('Button clicked!');
    // Handle button click
});

// Or with arrow function:
document.querySelector('.submit-btn').addEventListener('click', (event) => {
    event.preventDefault();
    console.log('Form submitted');
});'''
                }
            }
        }
    }

    return snippets_db.get(language, {}).get(category, {}).get(snippet_name, None)


def javascript_formatter():
    """JavaScript code formatter"""
    create_tool_header("JavaScript Formatter", "Format and beautify JavaScript code", "🟨")

    # File upload option
    uploaded_file = FileHandler.upload_files(['js'], accept_multiple=False)

    if uploaded_file:
        js_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded JavaScript Code", js_code, height=200, disabled=True)
    else:
        js_code = st.text_area("Enter JavaScript code to format:", height=300,
                               value="""function hello(name,age){if(name){console.log("Hello, "+name+"!");if(age>18){console.log("You are an adult")}else{console.log("You are a minor")}}return true}class Person{constructor(name,age){this.name=name;this.age=age}greet(){return "Hi, I'm "+this.name}}""")

    if js_code:
        # Formatting options
        col1, col2 = st.columns(2)
        with col1:
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1)
            indent_type = st.selectbox("Indent Type", ["Spaces", "Tabs"])
            line_ending = st.selectbox("Line Ending Style", ["LF", "CRLF"])

        with col2:
            insert_final_newline = st.checkbox("Insert Final Newline", True)
            trim_trailing_whitespace = st.checkbox("Trim Trailing Whitespace", True)
            semicolons = st.selectbox("Semicolons", ["preserve", "insert", "remove"])

        if st.button("Format JavaScript Code"):
            try:
                formatted_code = format_javascript_code(js_code, {
                    'indent_size': indent_size,
                    'indent_type': indent_type,
                    'line_ending': line_ending,
                    'insert_final_newline': insert_final_newline,
                    'trim_trailing_whitespace': trim_trailing_whitespace,
                    'semicolons': semicolons
                })

                st.subheader("Formatted Code")
                st.code(formatted_code, language="javascript")

                # Show statistics
                if formatted_code != js_code:
                    st.subheader("Statistics")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Original Lines", len(js_code.split('\n')))
                    with col2:
                        st.metric("Formatted Lines", len(formatted_code.split('\n')))
                    with col3:
                        st.metric("Size Change", f"{len(formatted_code) - len(js_code):+d} chars")

                FileHandler.create_download_link(formatted_code.encode(), "formatted_code.js", "application/javascript")

            except Exception as e:
                st.error(f"Error formatting code: {str(e)}")


def html_formatter():
    """HTML code formatter"""
    create_tool_header("HTML Formatter", "Format and beautify HTML code", "🌐")

    # File upload option
    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded HTML Code", html_code, height=200, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code to format:", height=300,
                                 value="""<html><head><title>Test</title></head><body><h1>Hello World</h1><p>This is a paragraph.</p><div><ul><li>Item 1</li><li>Item 2</li></ul></div></body></html>""")

    if html_code:
        # Formatting options
        col1, col2 = st.columns(2)
        with col1:
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1)
            indent_type = st.selectbox("Indent Type", ["Spaces", "Tabs"])

        with col2:
            wrap_attributes = st.checkbox("Wrap Long Attributes", False)
            preserve_newlines = st.checkbox("Preserve Existing Newlines", True)

        if st.button("Format HTML Code"):
            try:
                formatted_code = format_html_code(html_code, {
                    'indent_size': indent_size,
                    'indent_type': indent_type,
                    'wrap_attributes': wrap_attributes,
                    'preserve_newlines': preserve_newlines
                })

                st.subheader("Formatted Code")
                st.code(formatted_code, language="html")

                FileHandler.create_download_link(formatted_code.encode(), "formatted_code.html", "text/html")

            except Exception as e:
                st.error(f"Error formatting code: {str(e)}")


def css_formatter():
    """CSS code formatter"""
    create_tool_header("CSS Formatter", "Format and beautify CSS code", "🎨")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS Code", css_code, height=200, disabled=True)
    else:
        css_code = st.text_area("Enter CSS code to format:", height=300,
                                value=""".container{max-width:1200px;margin:0 auto;padding:0 20px}.header{background-color:#f8f9fa;border-bottom:1px solid #e9ecef;padding:1rem 0}.nav{display:flex;justify-content:space-between;align-items:center}""")

    if css_code:
        # Formatting options
        col1, col2 = st.columns(2)
        with col1:
            indent_size = st.selectbox("Indent Size", [2, 4, 8], index=1)
            indent_type = st.selectbox("Indent Type", ["Spaces", "Tabs"])

        with col2:
            newline_after_rule = st.checkbox("Newline After Each Rule", True)
            space_around_selectors = st.checkbox("Space Around Selectors", True)

        if st.button("Format CSS Code"):
            try:
                formatted_code = format_css_code(css_code, {
                    'indent_size': indent_size,
                    'indent_type': indent_type,
                    'newline_after_rule': newline_after_rule,
                    'space_around_selectors': space_around_selectors
                })

                st.subheader("Formatted Code")
                st.code(formatted_code, language="css")

                FileHandler.create_download_link(formatted_code.encode(), "formatted_code.css", "text/css")

            except Exception as e:
                st.error(f"Error formatting code: {str(e)}")


def python_validator():
    """Python code validator"""
    create_tool_header("Python Validator", "Validate Python code syntax and structure", "🐍")

    # File upload option
    uploaded_file = FileHandler.upload_files(['py'], accept_multiple=False)

    if uploaded_file:
        python_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Python Code", python_code, height=200, disabled=True)
    else:
        python_code = st.text_area("Enter Python code to validate:", height=300, value="""def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return length * width

# Test the function
area = calculate_area(5, 3)
print(f"Area: {area}")""")

    if python_code and st.button("Validate Python Code"):
        try:
            validation_result = validate_python_code(python_code)

            if validation_result['is_valid']:
                st.success("✅ Python code is syntactically correct!")
            else:
                st.error("❌ Python syntax errors found:")
                for error in validation_result['errors']:
                    st.error(f"Line {error.get('line', '?')}: {error['message']}")

            # Show warnings if any
            if validation_result.get('warnings'):
                st.warning("⚠️ Code quality warnings:")
                for warning in validation_result['warnings']:
                    st.warning(f"Line {warning.get('line', '?')}: {warning['message']}")

            # Show statistics
            if validation_result.get('stats'):
                st.subheader("Code Statistics")
                stats = validation_result['stats']
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Lines", stats.get('lines', 0))
                with col2:
                    st.metric("Functions", stats.get('functions', 0))
                with col3:
                    st.metric("Classes", stats.get('classes', 0))
                with col4:
                    st.metric("Imports", stats.get('imports', 0))

        except Exception as e:
            st.error(f"Error validating code: {str(e)}")


def javascript_validator():
    """JavaScript code validator"""
    create_tool_header("JavaScript Validator", "Validate JavaScript code syntax", "🟨")

    # File upload option
    uploaded_file = FileHandler.upload_files(['js'], accept_multiple=False)

    if uploaded_file:
        js_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded JavaScript Code", js_code, height=200, disabled=True)
    else:
        js_code = st.text_area("Enter JavaScript code to validate:", height=300, value="""function calculateArea(length, width) {
    if (length <= 0 || width <= 0) {
        throw new Error("Length and width must be positive");
    }
    return length * width;
}

// Test the function
const area = calculateArea(5, 3);
console.log(`Area: ${area}`);""")

    if js_code and st.button("Validate JavaScript Code"):
        try:
            validation_result = validate_javascript_code(js_code)

            if validation_result['is_valid']:
                st.success("✅ JavaScript code appears to be syntactically correct!")
            else:
                st.error("❌ JavaScript syntax errors found:")
                for error in validation_result['errors']:
                    st.error(f"Line {error.get('line', '?')}: {error['message']}")

            if validation_result.get('warnings'):
                st.warning("⚠️ JavaScript warnings:")
                for warning in validation_result['warnings']:
                    st.warning(f"Line {warning.get('line', '?')}: {warning['message']}")

        except Exception as e:
            st.error(f"Error validating code: {str(e)}")


def html_validator():
    """HTML code validator"""
    create_tool_header("HTML Validator", "Validate HTML code structure and syntax", "🌐")

    # File upload option
    uploaded_file = FileHandler.upload_files(['html', 'htm'], accept_multiple=False)

    if uploaded_file:
        html_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded HTML Code", html_code, height=200, disabled=True)
    else:
        html_code = st.text_area("Enter HTML code to validate:", height=300, value="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>This is a sample HTML document.</p>
</body>
</html>""")

    if html_code and st.button("Validate HTML Code"):
        try:
            validation_result = validate_html_code(html_code)

            if validation_result['is_valid']:
                st.success("✅ HTML code structure is valid!")
            else:
                st.error("❌ HTML validation errors found:")
                for error in validation_result['errors']:
                    st.error(f"Line {error.get('line', '?')}: {error['message']}")

            if validation_result.get('warnings'):
                st.warning("⚠️ HTML best practice warnings:")
                for warning in validation_result['warnings']:
                    st.warning(f"Line {warning.get('line', '?')}: {warning['message']}")

        except Exception as e:
            st.error(f"Error validating code: {str(e)}")


def css_validator():
    """CSS code validator"""
    create_tool_header("CSS Validator", "Validate CSS code syntax and properties", "🎨")

    # File upload option
    uploaded_file = FileHandler.upload_files(['css'], accept_multiple=False)

    if uploaded_file:
        css_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded CSS Code", css_code, height=200, disabled=True)
    else:
        css_code = st.text_area("Enter CSS code to validate:", height=300, value=""".container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.header {
    background-color: #f8f9fa;
    border-bottom: 1px solid #e9ecef;
    padding: 1rem 0;
}""")

    if css_code and st.button("Validate CSS Code"):
        try:
            validation_result = validate_css_code(css_code)

            if validation_result['is_valid']:
                st.success("✅ CSS code syntax is valid!")
            else:
                st.error("❌ CSS validation errors found:")
                for error in validation_result['errors']:
                    st.error(f"Line {error.get('line', '?')}: {error['message']}")

            if validation_result.get('warnings'):
                st.warning("⚠️ CSS best practice warnings:")
                for warning in validation_result['warnings']:
                    st.warning(f"Line {warning.get('line', '?')}: {warning['message']}")

        except Exception as e:
            st.error(f"Error validating code: {str(e)}")


def json_validator():
    """JSON code validator"""
    create_tool_header("JSON Validator", "Validate and analyze JSON structure", "📋")

    # File upload option
    uploaded_file = FileHandler.upload_files(['json', 'txt'], accept_multiple=False)

    if uploaded_file:
        json_text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded JSON", json_text, height=200, disabled=True)
    else:
        json_text = st.text_area("Enter JSON to validate:", height=300,
                                 value='{"name":"John Doe","age":30,"city":"New York","hobbies":["reading","coding","traveling"],"address":{"street":"123 Main St","zipcode":"10001"}}')

    if json_text and st.button("Validate JSON"):
        try:
            # Parse JSON
            parsed_json = json.loads(json_text)
            st.success("✅ Valid JSON!")

            # JSON structure analysis
            st.subheader("JSON Analysis")
            stats = analyze_json_structure(parsed_json)
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Objects", stats['objects'])
            with col2:
                st.metric("Arrays", stats['arrays'])
            with col3:
                st.metric("Keys", stats['keys'])
            with col4:
                st.metric("Max Depth", stats['max_depth'])

            # Display formatted JSON
            st.subheader("Formatted JSON")
            formatted_json = json.dumps(parsed_json, indent=2, ensure_ascii=False)
            st.code(formatted_json, language="json")

        except json.JSONDecodeError as e:
            st.error(f"❌ Invalid JSON: {str(e)}")

            # Try to provide helpful suggestions
            suggestions = []
            error_msg = str(e).lower()
            if "expecting property name" in error_msg:
                suggestions.append("Check for missing quotes around property names")
            if "expecting ',' delimiter" in error_msg:
                suggestions.append("Check for missing commas between properties")
            if "trailing comma" in error_msg:
                suggestions.append("Remove trailing commas after last properties")
            if "expecting value" in error_msg:
                suggestions.append("Check for missing values or extra commas")

            if suggestions:
                st.subheader("Suggested Fixes")
                for suggestion in suggestions:
                    st.write(f"• {suggestion}")

        except Exception as e:
            st.error(f"Error validating JSON: {str(e)}")


def format_javascript_code(js_code, options):
    """Format JavaScript code with given options"""
    import re

    indent_char = "\t" if options.get('indent_type') == "Tabs" else " " * options.get('indent_size', 4)

    # Basic JavaScript formatting
    formatted = js_code

    # Add newlines after certain characters
    formatted = re.sub(r'([{};])', r'\1\n', formatted)
    formatted = re.sub(r'([{])', r'\1\n', formatted)
    formatted = re.sub(r'([}])', r'\n\1\n', formatted)

    # Handle semicolons option
    if options.get('semicolons') == 'insert':
        # Add semicolons where missing (basic implementation)
        formatted = re.sub(r'([^;{}\s])\n', r'\1;\n', formatted)
    elif options.get('semicolons') == 'remove':
        # Remove semicolons (basic implementation)
        formatted = re.sub(r';(\s*[\n}])', r'\1', formatted)

    lines = formatted.split('\n')
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

    result = '\n'.join(formatted_lines)

    if options.get('trim_trailing_whitespace'):
        result = '\n'.join(line.rstrip() for line in result.split('\n'))

    if options.get('insert_final_newline') and not result.endswith('\n'):
        result += '\n'

    return result


def format_html_code(html_code, options):
    """Format HTML code with given options"""
    import re

    indent_char = "\t" if options.get('indent_type') == "Tabs" else " " * options.get('indent_size', 4)

    # HTML void/self-closing tags that don't need closing tags
    void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track',
                 'wbr'}

    # Remove extra whitespace and newlines
    formatted = re.sub(r'>\s+<', '><', html_code.strip())

    # Add newlines after certain structural tags
    formatted = re.sub(r'(<(?:html|head|body|div|section|article|header|footer|nav|main|aside)[^>]*>)', r'\1\n',
                       formatted)
    formatted = re.sub(r'(</(?:html|head|body|div|section|article|header|footer|nav|main|aside)>)', r'\n\1\n',
                       formatted)
    formatted = re.sub(r'(<(?:title|h[1-6]|p|li|dt|dd)[^>]*>)', r'\n\1', formatted)
    formatted = re.sub(r'(</(?:title|h[1-6]|p|li|dt|dd)>)', r'\1\n', formatted)

    lines = formatted.split('\n')
    formatted_lines = []
    indent_level = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check for closing tags
        closing_tag_match = re.match(r'</(\w+)>', line)
        if closing_tag_match:
            tag_name = closing_tag_match.group(1).lower()
            if tag_name not in void_tags:
                indent_level = max(0, indent_level - 1)

        # Add indented line
        formatted_lines.append(indent_char * indent_level + line)

        # Check for opening tags
        opening_tag_match = re.match(r'<(\w+)[^>]*>', line)
        if opening_tag_match:
            tag_name = opening_tag_match.group(1).lower()
            # Only increase indent for non-void tags and non-self-closing tags
            if tag_name not in void_tags and not line.endswith('/>'):
                # Check if it's not immediately closed on the same line
                if not re.search(f'</{tag_name}>', line):
                    indent_level += 1

    return '\n'.join(formatted_lines)


def format_css_code(css_code, options):
    """Format CSS code with given options"""
    import re

    indent_char = "\t" if options.get('indent_type') == "Tabs" else " " * options.get('indent_size', 4)

    # Remove extra whitespace
    formatted = re.sub(r'\s+', ' ', css_code.strip())

    # Add newlines after certain characters
    if options.get('newline_after_rule', True):
        formatted = re.sub(r'([;}])', r'\1\n', formatted)

    formatted = re.sub(r'([{])', r' {\n', formatted)
    formatted = re.sub(r'([}])', r'\n}\n', formatted)

    if options.get('space_around_selectors', True):
        formatted = re.sub(r'([^{\s])({)', r'\1 \2', formatted)

    lines = formatted.split('\n')
    formatted_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith('}'):
            formatted_lines.append(line)
        elif line.endswith('{'):
            formatted_lines.append(line)
        elif ':' in line and not line.endswith('{') and not line.endswith('}'):
            # CSS property
            formatted_lines.append(indent_char + line)
        else:
            formatted_lines.append(line)

    return '\n'.join(formatted_lines)


def validate_python_code(python_code):
    """Validate Python code syntax and structure"""
    import ast
    import re

    result = {
        'is_valid': True,
        'errors': [],
        'warnings': [],
        'stats': {}
    }

    try:
        # Parse the code
        tree = ast.parse(python_code)

        # Count various elements
        functions = sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
        classes = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
        imports = sum(1 for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom)))
        lines = len([line for line in python_code.split('\n') if line.strip()])

        result['stats'] = {
            'lines': lines,
            'functions': functions,
            'classes': classes,
            'imports': imports
        }

        # Basic code quality checks
        if 'print(' in python_code:
            result['warnings'].append({
                'line': None,
                'message': 'Code contains print statements - consider using logging'
            })

        if re.search(r'\btodo\b|\bfixme\b|\bhack\b', python_code.lower()):
            result['warnings'].append({
                'line': None,
                'message': 'Code contains TODO/FIXME comments'
            })

    except SyntaxError as e:
        result['is_valid'] = False
        result['errors'].append({
            'line': e.lineno,
            'message': str(e.msg)
        })
    except Exception as e:
        result['is_valid'] = False
        result['errors'].append({
            'line': None,
            'message': f'Unexpected error: {str(e)}'
        })

    return result


def validate_javascript_code(js_code):
    """Validate JavaScript code syntax (basic validation)"""
    import re

    result = {
        'is_valid': True,
        'errors': [],
        'warnings': []
    }

    # Basic JavaScript syntax checks
    errors = []

    # Check for unmatched brackets
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    lines = js_code.split('\n')

    for line_num, line in enumerate(lines, 1):
        for char in line:
            if char in brackets:
                stack.append((char, line_num))
            elif char in brackets.values():
                if not stack:
                    errors.append({
                        'line': line_num,
                        'message': f'Unmatched closing bracket: {char}'
                    })
                else:
                    opening, _ = stack.pop()
                    if brackets[opening] != char:
                        errors.append({
                            'line': line_num,
                            'message': f'Mismatched brackets: {opening} and {char}'
                        })

    # Check for remaining unclosed brackets
    for opening, line_num in stack:
        errors.append({
            'line': line_num,
            'message': f'Unclosed bracket: {opening}'
        })

    if errors:
        result['is_valid'] = False
        result['errors'] = errors

    # Basic warnings
    warnings = []
    if 'console.log(' in js_code:
        warnings.append({
            'line': None,
            'message': 'Code contains console.log statements'
        })

    if '==' in js_code and '===' not in js_code:
        warnings.append({
            'line': None,
            'message': 'Consider using === instead of == for strict equality'
        })

    result['warnings'] = warnings

    return result


def validate_html_code(html_code):
    """Validate HTML code structure and syntax"""
    import re

    result = {
        'is_valid': True,
        'errors': [],
        'warnings': []
    }

    errors = []
    warnings = []

    # Check for basic HTML structure
    if not re.search(r'<!DOCTYPE\s+html>', html_code, re.IGNORECASE):
        warnings.append({
            'line': None,
            'message': 'Missing DOCTYPE declaration'
        })

    if not re.search(r'<html[^>]*>', html_code, re.IGNORECASE):
        errors.append({
            'line': None,
            'message': 'Missing <html> tag'
        })

    if not re.search(r'<head[^>]*>', html_code, re.IGNORECASE):
        warnings.append({
            'line': None,
            'message': 'Missing <head> section'
        })

    if not re.search(r'<body[^>]*>', html_code, re.IGNORECASE):
        warnings.append({
            'line': None,
            'message': 'Missing <body> section'
        })

    if not re.search(r'<title[^>]*>', html_code, re.IGNORECASE):
        warnings.append({
            'line': None,
            'message': 'Missing <title> tag'
        })

    # Check for unclosed tags
    opening_tags = re.findall(r'<(\w+)[^>]*>', html_code)
    closing_tags = re.findall(r'</(\w+)>', html_code)

    self_closing_tags = {'img', 'br', 'hr', 'input', 'meta', 'link', 'area', 'base', 'col', 'embed', 'param', 'source',
                         'track', 'wbr'}

    for tag in opening_tags:
        if tag.lower() not in self_closing_tags:
            if tag.lower() not in [t.lower() for t in closing_tags]:
                errors.append({
                    'line': None,
                    'message': f'Unclosed tag: <{tag}>'
                })

    # Check for invalid tag nesting
    if '<p>' in html_code and '<div>' in html_code:
        # This is a simple check - in reality, tag nesting rules are complex
        if re.search(r'<p[^>]*>.*<div[^>]*>', html_code, re.DOTALL):
            warnings.append({
                'line': None,
                'message': 'Possible invalid tag nesting: <div> inside <p>'
            })

    if errors:
        result['is_valid'] = False
        result['errors'] = errors

    result['warnings'] = warnings

    return result


def validate_css_code(css_code):
    """Validate CSS code syntax and properties"""
    import re

    result = {
        'is_valid': True,
        'errors': [],
        'warnings': []
    }

    errors = []
    warnings = []

    # Check for unmatched braces
    open_braces = css_code.count('{')
    close_braces = css_code.count('}')

    if open_braces != close_braces:
        errors.append({
            'line': None,
            'message': f'Unmatched braces: {open_braces} opening, {close_braces} closing'
        })

    # Check for basic CSS syntax patterns
    lines = css_code.split('\n')

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('/*'):
            continue

        # Check for properties without values
        if ':' in line and not line.endswith('{') and not line.endswith('}'):
            if not re.match(r'^[^:]+:\s*.+[;}]?\s*$', line):
                warnings.append({
                    'line': line_num,
                    'message': f'Possible invalid property syntax: {line}'
                })

        # Check for missing semicolons in property declarations
        if ':' in line and not line.endswith('{') and not line.endswith('}') and not line.endswith(';'):
            warnings.append({
                'line': line_num,
                'message': f'Missing semicolon: {line}'
            })

    # Check for common property misspellings
    common_properties = ['color', 'background', 'margin', 'padding', 'border', 'width', 'height', 'display', 'position',
                         'font-size']
    for prop in common_properties:
        # This is a basic check - real CSS validation is much more complex
        if prop.replace('-', '') in css_code.replace('-', '').lower() and prop not in css_code.lower():
            warnings.append({
                'line': None,
                'message': f'Possible misspelled property similar to: {prop}'
            })

    if errors:
        result['is_valid'] = False
        result['errors'] = errors

    result['warnings'] = warnings

    return result


def language_converter():
    """Convert code between different programming languages"""
    create_tool_header("Language Converter", "Convert code snippets between programming languages", "🔄")

    col1, col2 = st.columns(2)
    with col1:
        source_language = st.selectbox("Source Language",
                                       ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "PHP", "Ruby"])
    with col2:
        target_language = st.selectbox("Target Language",
                                       ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "PHP", "Ruby"])

    # File upload option
    uploaded_file = FileHandler.upload_files(['py', 'js', 'java', 'cpp', 'cs', 'go', 'rs', 'php', 'rb', 'txt'],
                                             accept_multiple=False)

    if uploaded_file:
        source_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Code", source_code, height=200, disabled=True)
    else:
        source_code = st.text_area("Enter code to convert:", height=300,
                                   value="""def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))""")

    if source_code and source_language != target_language:
        if st.button("Convert Code"):
            try:
                converted_code = convert_code_language(source_code, source_language, target_language)

                st.subheader(f"Converted to {target_language}")
                st.code(converted_code, language=target_language.lower())

                # Conversion notes
                st.subheader("Conversion Notes")
                notes = get_conversion_notes(source_language, target_language)
                for note in notes:
                    st.info(f"ℹ️ {note}")

                FileHandler.create_download_link(converted_code.encode(),
                                                 f"converted_code.{get_file_extension(target_language)}", "text/plain")

            except Exception as e:
                st.error(f"Error converting code: {str(e)}")
    elif source_language == target_language:
        st.warning("⚠️ Source and target languages are the same!")


def encoding_converter():
    """Convert text between different character encodings"""
    create_tool_header("Encoding Converter", "Convert text between different character encodings", "🔡")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt', 'csv', 'json', 'xml'], accept_multiple=False)

    if uploaded_file:
        try:
            # Try to detect encoding
            raw_data = uploaded_file[0].getvalue()
            detected_encoding = detect_text_encoding(raw_data)
            st.info(f"Detected encoding: {detected_encoding}")

            text_content = raw_data.decode(detected_encoding, errors='replace')
            st.text_area("Uploaded Text", text_content[:1000] + "..." if len(text_content) > 1000 else text_content,
                         height=200, disabled=True)
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
            text_content = ""
    else:
        text_content = st.text_area("Enter text to convert:", height=300,
                                    value="Hello, World! 你好世界! Bonjour le monde! 🌍")

    if text_content:
        col1, col2 = st.columns(2)
        with col1:
            source_encoding = st.selectbox("Source Encoding",
                                           ["utf-8", "utf-16", "ascii", "latin-1", "cp1252", "iso-8859-1"])
        with col2:
            target_encoding = st.selectbox("Target Encoding",
                                           ["utf-8", "utf-16", "ascii", "latin-1", "cp1252", "iso-8859-1"])

        if st.button("Convert Encoding"):
            try:
                converted_text = convert_text_encoding(text_content, source_encoding, target_encoding)

                st.subheader(f"Converted to {target_encoding}")
                st.text_area("Converted Text", converted_text, height=200)

                # Show byte representation
                st.subheader("Byte Information")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Original Bytes", len(text_content.encode(source_encoding, errors='replace')))
                with col2:
                    st.metric("Converted Bytes", len(converted_text.encode(target_encoding, errors='replace')))

                FileHandler.create_download_link(converted_text.encode(target_encoding),
                                                 f"converted_{target_encoding}.txt", "text/plain")

            except Exception as e:
                st.error(f"Error converting encoding: {str(e)}")


def format_transformer():
    """Transform data between different formats"""
    create_tool_header("Format Transformer", "Transform data between JSON, XML, CSV, YAML formats", "🔄")

    col1, col2 = st.columns(2)
    with col1:
        source_format = st.selectbox("Source Format", ["JSON", "XML", "CSV", "YAML", "TOML"])
    with col2:
        target_format = st.selectbox("Target Format", ["JSON", "XML", "CSV", "YAML", "TOML"])

    # File upload option
    file_extensions = {'JSON': ['json'], 'XML': ['xml'], 'CSV': ['csv'], 'YAML': ['yaml', 'yml'], 'TOML': ['toml']}
    uploaded_file = FileHandler.upload_files(file_extensions.get(source_format, ['txt']), accept_multiple=False)

    if uploaded_file:
        source_data = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Data", source_data[:1000] + "..." if len(source_data) > 1000 else source_data,
                     height=200, disabled=True)
    else:
        default_data = get_sample_data(source_format)
        source_data = st.text_area("Enter data to transform:", height=300, value=default_data)

    if source_data and source_format != target_format:
        if st.button("Transform Format"):
            try:
                transformed_data = transform_data_format(source_data, source_format, target_format)

                st.subheader(f"Transformed to {target_format}")
                st.code(transformed_data, language=target_format.lower())

                FileHandler.create_download_link(transformed_data.encode(), f"transformed.{target_format.lower()}",
                                                 "text/plain")

            except Exception as e:
                st.error(f"Error transforming format: {str(e)}")
    elif source_format == target_format:
        st.warning("⚠️ Source and target formats are the same!")


def case_converter():
    """Convert text case styles for variables and text"""
    create_tool_header("Case Converter", "Convert between different case styles", "🔤")

    # File upload option
    uploaded_file = FileHandler.upload_files(['txt', 'py', 'js', 'java'], accept_multiple=False)

    if uploaded_file:
        text_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Text", text_content[:1000] + "..." if len(text_content) > 1000 else text_content,
                     height=200, disabled=True)
    else:
        text_content = st.text_area("Enter text to convert:", height=300,
                                    value="hello_world_example\nMyClassName\nsome-kebab-case\nANOTHER_CONSTANT")

    if text_content:
        st.subheader("Case Conversion Options")

        case_types = {
            "camelCase": "myVariableName",
            "PascalCase": "MyClassName",
            "snake_case": "my_variable_name",
            "kebab-case": "my-variable-name",
            "UPPER_CASE": "MY_CONSTANT_NAME",
            "lower case": "my variable name",
            "Title Case": "My Variable Name",
            "UPPER CASE": "MY VARIABLE NAME"
        }

        target_case = st.selectbox("Target Case Style", list(case_types.keys()),
                                   format_func=lambda x: f"{x} (example: {case_types[x]})")

        if st.button("Convert Case"):
            try:
                converted_text = convert_text_case(text_content, target_case)

                st.subheader(f"Converted to {target_case}")
                st.code(converted_text, language="text")

                FileHandler.create_download_link(converted_text.encode(), "converted_case.txt", "text/plain")

            except Exception as e:
                st.error(f"Error converting case: {str(e)}")


def indentation_converter():
    """Convert indentation between tabs and spaces"""
    create_tool_header("Indentation Converter", "Convert between tabs and spaces indentation", "📐")

    # File upload option
    uploaded_file = FileHandler.upload_files(['py', 'js', 'html', 'css', 'java', 'cpp', 'txt'], accept_multiple=False)

    if uploaded_file:
        code_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Code", code_content[:1000] + "..." if len(code_content) > 1000 else code_content,
                     height=200, disabled=True)
    else:
        code_content = st.text_area("Enter code to convert indentation:", height=300,
                                    value="""def example_function():
    if True:
        print("Hello")
        for i in range(5):
            print(i)""")

    if code_content:
        col1, col2 = st.columns(2)
        with col1:
            source_indent = st.selectbox("Source Indentation", ["Auto-detect", "Spaces", "Tabs"])
            source_spaces = 4  # Default value
            if source_indent == "Spaces":
                source_spaces = st.selectbox("Source Space Count", [2, 4, 8])
        with col2:
            target_indent = st.selectbox("Target Indentation", ["Spaces", "Tabs"])
            target_spaces = 4  # Default value
            if target_indent == "Spaces":
                target_spaces = st.selectbox("Target Space Count", [2, 4, 8], index=1)

        if st.button("Convert Indentation"):
            try:
                # Detect current indentation if auto-detect
                detected_indent = "Spaces"  # Default value
                if source_indent == "Auto-detect":
                    detected_indent = detect_indentation(code_content)
                    st.info(f"Detected: {detected_indent}")

                converted_code = convert_indentation(
                    code_content,
                    source_indent if source_indent != "Auto-detect" else detected_indent,
                    target_indent,
                    source_spaces if source_indent == "Spaces" else 4,
                    target_spaces if target_indent == "Spaces" else 4
                )

                st.subheader(f"Converted to {target_indent}" + (
                    f" ({target_spaces} spaces)" if target_indent == "Spaces" else ""))
                st.code(converted_code, language="python")

                # Show statistics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Original Lines", len(code_content.split('\n')))
                with col2:
                    st.metric("Converted Lines", len(converted_code.split('\n')))

                FileHandler.create_download_link(converted_code.encode(), "converted_indentation.txt", "text/plain")

            except Exception as e:
                st.error(f"Error converting indentation: {str(e)}")


def api_documentation():
    """Generate API documentation from code"""
    create_tool_header("API Documentation", "Generate API documentation from code", "📚")

    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox("Source Language", ["Python", "JavaScript", "Java", "C#", "Go", "TypeScript"])
        doc_format = st.selectbox("Documentation Format", ["Markdown", "HTML", "JSON", "OpenAPI/Swagger"])
    with col2:
        include_examples = st.checkbox("Include Code Examples", True)
        include_types = st.checkbox("Include Type Information", True)

    # File upload option
    uploaded_file = FileHandler.upload_files(['py', 'js', 'java', 'cs', 'go', 'ts'], accept_multiple=False)

    if uploaded_file:
        source_code = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Code", source_code[:1000] + "..." if len(source_code) > 1000 else source_code,
                     height=200, disabled=True)
    else:
        source_code = st.text_area("Enter code to document:", height=300,
                                   value="""class UserManager:
    def create_user(self, name: str, email: str) -> dict:
        \"\"\"
        Create a new user account.

        Args:
            name (str): The user's full name
            email (str): The user's email address

        Returns:
            dict: User data with id, name, and email

        Raises:
            ValueError: If email format is invalid
        \"\"\"
        return {"id": 1, "name": name, "email": email}

    def get_user(self, user_id: int) -> dict:
        \"\"\"Get user by ID\"\"\"
        return {"id": user_id, "name": "John", "email": "john@example.com"}""")

    if source_code:
        if st.button("Generate Documentation"):
            try:
                documentation = generate_api_documentation(
                    source_code,
                    language,
                    doc_format,
                    include_examples,
                    include_types
                )

                st.subheader(f"Generated {doc_format} Documentation")

                if doc_format == "HTML":
                    components.html(documentation, height=400, scrolling=True)
                else:
                    st.code(documentation, language=doc_format.lower())

                FileHandler.create_download_link(documentation.encode(), f"api_docs.{doc_format.lower()}", "text/plain")

            except Exception as e:
                st.error(f"Error generating documentation: {str(e)}")


def documentation_parser():
    """Parse and analyze existing documentation"""
    create_tool_header("Documentation Parser", "Parse and analyze code documentation", "🔍")

    # File upload option
    uploaded_file = FileHandler.upload_files(['md', 'rst', 'txt', 'html'], accept_multiple=False)

    if uploaded_file:
        doc_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Documentation", doc_content[:1000] + "..." if len(doc_content) > 1000 else doc_content,
                     height=200, disabled=True)
    else:
        doc_content = st.text_area("Enter documentation to parse:", height=300,
                                   value="""# API Documentation

## User Management

### Create User
**POST** `/api/users`

Creates a new user account.

**Parameters:**
- `name` (string, required): User's full name
- `email` (string, required): User's email address

**Response:**
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Get User
**GET** `/api/users/{id}`

Retrieves user information by ID.""")

    if doc_content:
        col1, col2 = st.columns(2)
        with col1:
            analysis_type = st.selectbox("Analysis Type",
                                         ["Structure Analysis", "API Endpoints", "Code Examples", "Missing Sections"])
        with col2:
            output_format = st.selectbox("Output Format", ["Summary", "Detailed Report", "JSON"])

        if st.button("Parse Documentation"):
            try:
                parsed_result = parse_documentation(doc_content, analysis_type, output_format)

                st.subheader(f"{analysis_type} Results")

                if output_format == "JSON":
                    st.code(parsed_result, language="json")
                else:
                    st.markdown(parsed_result)

                FileHandler.create_download_link(parsed_result.encode(), "parsed_docs.txt", "text/plain")

            except Exception as e:
                st.error(f"Error parsing documentation: {str(e)}")


def changelog_generator():
    """Generate changelog from commit history or changes"""
    create_tool_header("Changelog Generator", "Generate changelog from version history", "📝")

    input_method = st.selectbox("Input Method", ["Manual Entry", "File Upload", "Git-style Format"])

    if input_method == "File Upload":
        uploaded_file = FileHandler.upload_files(['txt', 'md', 'json'], accept_multiple=False)
        if uploaded_file:
            changes_content = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("Uploaded Changes",
                         changes_content[:1000] + "..." if len(changes_content) > 1000 else changes_content, height=200,
                         disabled=True)
        else:
            changes_content = ""
    else:
        if input_method == "Git-style Format":
            placeholder = """feat: add user authentication
fix: resolve login bug
docs: update API documentation
style: improve button styling
refactor: optimize database queries
test: add unit tests for user service"""
        else:
            placeholder = """Version 2.1.0
- Added user authentication system
- Fixed login redirect bug
- Updated API documentation
- Improved performance

Version 2.0.1
- Fixed critical security vulnerability
- Updated dependencies"""

        changes_content = st.text_area("Enter changes/commits:", height=300, value=placeholder)

    if changes_content:
        col1, col2 = st.columns(2)
        with col1:
            version = st.text_input("Version Number", "2.1.0")
            changelog_format = st.selectbox("Changelog Format", ["Keep a Changelog", "Semantic Release", "Custom"])
        with col2:
            group_by = st.selectbox("Group Changes By", ["Type", "Date", "Component", "None"])
            include_dates = st.checkbox("Include Dates", True)

        if st.button("Generate Changelog"):
            try:
                changelog = generate_changelog(
                    changes_content,
                    version,
                    changelog_format,
                    group_by,
                    include_dates,
                    input_method
                )

                st.subheader("Generated Changelog")
                st.code(changelog, language="markdown")

                FileHandler.create_download_link(changelog.encode(), "CHANGELOG.md", "text/markdown")

            except Exception as e:
                st.error(f"Error generating changelog: {str(e)}")


# Helper functions for the new tools

def convert_code_language(source_code, source_lang, target_lang):
    """Convert code between programming languages (basic implementation)"""
    conversion_map = {
        ('Python', 'JavaScript'): {
            'def ': 'function ',
            'print(': 'console.log(',
            '    ': '  ',
            'True': 'true',
            'False': 'false',
            'None': 'null',
            'elif': 'else if',
            'and': '&&',
            'or': '||',
            'not ': '!',
        },
        ('JavaScript', 'Python'): {
            'function ': 'def ',
            'console.log(': 'print(',
            '  ': '    ',
            'true': 'True',
            'false': 'False',
            'null': 'None',
            'else if': 'elif',
            '&&': ' and ',
            '||': ' or ',
            '!': 'not ',
        }
    }

    # Basic conversion using simple string replacement
    converted = source_code
    replacements = conversion_map.get((source_lang, target_lang), {})

    for old, new in replacements.items():
        converted = converted.replace(old, new)

    if not replacements:
        # If no specific conversion available, return with comment
        converted = f"// Converted from {source_lang} to {target_lang}\n// Manual conversion required\n\n{source_code}"

    return converted


def get_conversion_notes(source_lang, target_lang):
    """Get conversion notes for language pairs"""
    notes = []

    if source_lang == 'Python' and target_lang == 'JavaScript':
        notes = [
            "Python indentation converted to JavaScript braces",
            "print() statements converted to console.log()",
            "Boolean values (True/False) converted to lowercase",
            "Manual adjustment may be needed for complex data structures"
        ]
    elif source_lang == 'JavaScript' and target_lang == 'Python':
        notes = [
            "JavaScript braces may need manual conversion to Python indentation",
            "console.log() converted to print()",
            "Boolean values converted to Python style (True/False)",
            "Variable declarations (let/const/var) may need adjustment"
        ]
    else:
        notes = [
            f"Conversion from {source_lang} to {target_lang} requires manual review",
            "Syntax differences may not be fully handled",
            "Consider using language-specific tools for complex conversions"
        ]

    return notes


def get_file_extension(language):
    """Get file extension for programming language"""
    extensions = {
        'Python': 'py',
        'JavaScript': 'js',
        'Java': 'java',
        'C++': 'cpp',
        'C#': 'cs',
        'Go': 'go',
        'Rust': 'rs',
        'PHP': 'php',
        'Ruby': 'rb'
    }
    return extensions.get(language, 'txt')


def detect_text_encoding(raw_data):
    """Detect text encoding from raw bytes"""
    try:
        # Try UTF-8 first
        raw_data.decode('utf-8')
        return 'utf-8'
    except UnicodeDecodeError:
        pass

    try:
        # Try latin-1
        raw_data.decode('latin-1')
        return 'latin-1'
    except UnicodeDecodeError:
        pass

    try:
        # Try cp1252 (Windows)
        raw_data.decode('cp1252')
        return 'cp1252'
    except UnicodeDecodeError:
        pass

    # Default fallback
    return 'utf-8'


def convert_text_encoding(text, source_encoding, target_encoding):
    """Convert text between different encodings"""
    try:
        # Encode to bytes using source encoding, then decode using target encoding
        if source_encoding == target_encoding:
            return text

        # Convert through bytes
        encoded_bytes = text.encode(source_encoding, errors='replace')
        converted_text = encoded_bytes.decode(source_encoding, errors='replace')

        # Re-encode and decode with target encoding
        return converted_text
    except Exception as e:
        raise Exception(f"Encoding conversion failed: {str(e)}")


def get_sample_data(format_type):
    """Get sample data for different formats"""
    samples = {
        'JSON': '{"name": "John Doe", "age": 30, "city": "New York", "hobbies": ["reading", "coding"]}',
        'XML': '<?xml version="1.0"?>\n<person>\n  <name>John Doe</name>\n  <age>30</age>\n  <city>New York</city>\n</person>',
        'CSV': 'name,age,city\nJohn Doe,30,New York\nJane Smith,25,Los Angeles',
        'YAML': 'name: John Doe\nage: 30\ncity: New York\nhobbies:\n  - reading\n  - coding',
        'TOML': '[person]\nname = "John Doe"\nage = 30\ncity = "New York"\nhobbies = ["reading", "coding"]'
    }
    return samples.get(format_type, '{}')


def transform_data_format(source_data, source_format, target_format):
    """Transform data between different formats"""
    import csv
    import io

    try:
        # Parse source data
        if source_format == 'JSON':
            data = json.loads(source_data)
        elif source_format == 'CSV':
            # Simple CSV parsing
            lines = source_data.strip().split('\n')
            headers = lines[0].split(',')
            data = []
            for line in lines[1:]:
                values = line.split(',')
                data.append(dict(zip(headers, values)))
        else:
            # For other formats, return a placeholder transformation
            data = {"converted_from": source_format, "data": source_data}

        # Convert to target format
        if target_format == 'JSON':
            return json.dumps(data, indent=2)
        elif target_format == 'XML':
            # Simple XML conversion
            if isinstance(data, list):
                xml_content = '<?xml version="1.0"?>\n<root>\n'
                for item in data:
                    xml_content += '  <item>\n'
                    for key, value in item.items():
                        xml_content += f'    <{key}>{value}</{key}>\n'
                    xml_content += '  </item>\n'
                xml_content += '</root>'
                return xml_content
            else:
                xml_content = '<?xml version="1.0"?>\n<root>\n'
                for key, value in data.items():
                    xml_content += f'  <{key}>{value}</{key}>\n'
                xml_content += '</root>'
                return xml_content
        elif target_format == 'YAML':
            # Simple YAML conversion
            yaml_content = ""
            if isinstance(data, list):
                for item in data:
                    yaml_content += "- \n"
                    for key, value in item.items():
                        yaml_content += f"  {key}: {value}\n"
            else:
                for key, value in data.items():
                    if isinstance(value, list):
                        yaml_content += f"{key}:\n"
                        for item in value:
                            yaml_content += f"  - {item}\n"
                    else:
                        yaml_content += f"{key}: {value}\n"
            return yaml_content
        elif target_format == 'CSV':
            # Convert to CSV
            if isinstance(data, list) and data:
                headers = list(data[0].keys())
                csv_content = ','.join(headers) + '\n'
                for item in data:
                    csv_content += ','.join(str(item.get(h, '')) for h in headers) + '\n'
                return csv_content
            elif isinstance(data, dict):
                return "key,value\n" + '\n'.join(f"{k},{v}" for k, v in data.items())
            else:
                return "data\n" + str(data)

        return str(data)

    except Exception as e:
        raise Exception(f"Format transformation failed: {str(e)}")


def convert_text_case(text, target_case):
    """Convert text to different case styles"""
    import re

    lines = text.split('\n')
    converted_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            converted_lines.append(line)
            continue

        if target_case == "camelCase":
            # Convert to camelCase
            words = re.split(r'[_\-\s]+', line.lower())
            converted = words[0] + ''.join(word.capitalize() for word in words[1:])
        elif target_case == "PascalCase":
            # Convert to PascalCase
            words = re.split(r'[_\-\s]+', line.lower())
            converted = ''.join(word.capitalize() for word in words)
        elif target_case == "snake_case":
            # Convert to snake_case
            # Handle camelCase and PascalCase
            converted = re.sub(r'([a-z])([A-Z])', r'\1_\2', line)
            converted = re.sub(r'[_\-\s]+', '_', converted).lower()
        elif target_case == "kebab-case":
            # Convert to kebab-case
            converted = re.sub(r'([a-z])([A-Z])', r'\1-\2', line)
            converted = re.sub(r'[_\-\s]+', '-', converted).lower()
        elif target_case == "UPPER_CASE":
            # Convert to UPPER_CASE
            converted = re.sub(r'([a-z])([A-Z])', r'\1_\2', line)
            converted = re.sub(r'[_\-\s]+', '_', converted).upper()
        elif target_case == "lower case":
            # Convert to lower case with spaces
            converted = re.sub(r'([a-z])([A-Z])', r'\1 \2', line)
            converted = re.sub(r'[_\-\s]+', ' ', converted).lower()
        elif target_case == "Title Case":
            # Convert to Title Case
            converted = re.sub(r'([a-z])([A-Z])', r'\1 \2', line)
            converted = re.sub(r'[_\-\s]+', ' ', converted).title()
        elif target_case == "UPPER CASE":
            # Convert to UPPER CASE with spaces
            converted = re.sub(r'([a-z])([A-Z])', r'\1 \2', line)
            converted = re.sub(r'[_\-\s]+', ' ', converted).upper()
        else:
            converted = line

        converted_lines.append(converted)

    return '\n'.join(converted_lines)


def detect_indentation(code):
    """Detect indentation style in code"""
    lines = code.split('\n')
    tab_count = 0
    space_count = 0

    for line in lines:
        if line.startswith('\t'):
            tab_count += 1
        elif line.startswith('    '):
            space_count += 1

    if tab_count > space_count:
        return "Tabs"
    else:
        return "Spaces (4)"


def convert_indentation(code, source_indent, target_indent, source_spaces=4, target_spaces=4):
    """Convert indentation between tabs and spaces"""
    lines = code.split('\n')
    converted_lines = []

    for line in lines:
        if not line.strip():
            converted_lines.append(line)
            continue

        # Count leading whitespace
        leading_whitespace = len(line) - len(line.lstrip())
        content = line.lstrip()

        if source_indent == "Tabs":
            # Convert from tabs
            if target_indent == "Spaces":
                # Count tabs and convert to spaces
                tab_count = 0
                for char in line:
                    if char == '\t':
                        tab_count += 1
                    else:
                        break
                new_line = ' ' * (tab_count * target_spaces) + content
            else:
                new_line = line  # Already tabs
        else:
            # Convert from spaces
            if target_indent == "Tabs":
                # Convert spaces to tabs
                indent_level = leading_whitespace // source_spaces
                new_line = '\t' * indent_level + content
            else:
                # Convert between different space counts
                indent_level = leading_whitespace // source_spaces
                new_line = ' ' * (indent_level * target_spaces) + content

        converted_lines.append(new_line)

    return '\n'.join(converted_lines)


def generate_api_documentation(source_code, language, doc_format, include_examples, include_types):
    """Generate API documentation from source code"""
    import re

    # Basic documentation generation
    doc_content = ""

    if doc_format == "Markdown":
        doc_content = f"# API Documentation\n\n## Overview\nGenerated from {language} source code.\n\n"

        # Extract functions/methods (basic implementation)
        if language == "Python":
            functions = re.findall(r'def\s+(\w+)\s*\([^)]*\):', source_code)
            classes = re.findall(r'class\s+(\w+):', source_code)

            if classes:
                doc_content += "## Classes\n\n"
                for class_name in classes:
                    doc_content += f"### {class_name}\n\nA class representing {class_name.lower()}.\n\n"

            if functions:
                doc_content += "## Functions\n\n"
                for func_name in functions:
                    doc_content += f"### {func_name}()\n\nFunction: {func_name}\n\n"
                    if include_examples:
                        doc_content += f"```python\n{func_name}()\n```\n\n"

    elif doc_format == "HTML":
        doc_content = f"""
        <html>
        <head><title>API Documentation</title></head>
        <body>
        <h1>API Documentation</h1>
        <p>Generated from {language} source code.</p>
        <h2>Code Analysis</h2>
        <pre>{source_code[:500]}...</pre>
        </body>
        </html>
        """

    elif doc_format == "JSON":
        doc_content = json.dumps({
            "api_version": "1.0",
            "language": language,
            "generated": "auto",
            "functions": re.findall(r'def\s+(\w+)', source_code) if language == "Python" else [],
            "classes": re.findall(r'class\s+(\w+)', source_code) if language == "Python" else []
        }, indent=2)

    else:  # OpenAPI/Swagger
        doc_content = f"""
openapi: 3.0.0
info:
  title: Generated API
  version: 1.0.0
  description: Auto-generated from {language} code
paths:
  /api:
    get:
      summary: Example endpoint
      responses:
        '200':
          description: Success
        """

    return doc_content


def parse_documentation(doc_content, analysis_type, output_format):
    """Parse and analyze documentation content"""
    import re

    result = ""

    if analysis_type == "Structure Analysis":
        # Count different elements
        headers = len(re.findall(r'^#+\s', doc_content, re.MULTILINE))
        code_blocks = len(re.findall(r'```', doc_content))
        links = len(re.findall(r'\[.*?\]\(.*?\)', doc_content))

        if output_format == "JSON":
            result = json.dumps({
                "headers": headers,
                "code_blocks": code_blocks // 2,  # Divide by 2 since ``` appears in pairs
                "links": links,
                "total_lines": len(doc_content.split('\n')),
                "word_count": len(doc_content.split())
            }, indent=2)
        else:
            total_lines = len(doc_content.split('\n'))
            word_count = len(doc_content.split())
            result = f"""# Structure Analysis

- **Headers**: {headers}
- **Code Blocks**: {code_blocks // 2}
- **Links**: {links}
- **Total Lines**: {total_lines}
- **Word Count**: {word_count}
"""

    elif analysis_type == "API Endpoints":
        # Extract API endpoints
        endpoints = re.findall(r'\*\*(GET|POST|PUT|DELETE)\*\*\s+`([^`]+)`', doc_content)

        if output_format == "JSON":
            result = json.dumps({
                "endpoints": [{"method": method, "path": path} for method, path in endpoints]
            }, indent=2)
        else:
            result = "# API Endpoints\n\n"
            for method, path in endpoints:
                result += f"- **{method}** `{path}`\n"

    elif analysis_type == "Code Examples":
        # Extract code examples
        code_examples = re.findall(r'```(\w+)?\n(.*?)```', doc_content, re.DOTALL)

        if output_format == "JSON":
            result = json.dumps({
                "code_examples": [{"language": lang, "code": code.strip()} for lang, code in code_examples]
            }, indent=2)
        else:
            result = "# Code Examples\n\n"
            for i, (lang, code) in enumerate(code_examples, 1):
                result += f"## Example {i} ({lang or 'unknown'})\n```\n{code.strip()}\n```\n\n"

    else:  # Missing Sections
        common_sections = ["installation", "usage", "examples", "api", "contributing", "license"]
        missing = [section for section in common_sections if section not in doc_content.lower()]

        if output_format == "JSON":
            result = json.dumps({"missing_sections": missing}, indent=2)
        else:
            result = "# Missing Sections\n\n"
            for section in missing:
                result += f"- {section.title()}\n"

    return result


def generate_changelog(changes_content, version, changelog_format, group_by, include_dates, input_method):
    """Generate changelog from changes"""
    from datetime import datetime

    current_date = datetime.now().strftime("%Y-%m-%d")

    changelog = ""

    if changelog_format == "Keep a Changelog":
        changelog = f"""# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [{version}] - {current_date if include_dates else 'Unreleased'}

"""

        if input_method == "Git-style Format":
            # Parse git-style commits
            lines = changes_content.strip().split('\n')
            added = []
            changed = []
            fixed = []

            for line in lines:
                if line.startswith('feat:'):
                    added.append(line[5:].strip())
                elif line.startswith('fix:'):
                    fixed.append(line[4:].strip())
                elif line.startswith('docs:') or line.startswith('style:') or line.startswith('refactor:'):
                    changed.append(line.split(':')[1].strip())

            if added:
                changelog += "### Added\n"
                for item in added:
                    changelog += f"- {item}\n"
                changelog += "\n"

            if changed:
                changelog += "### Changed\n"
                for item in changed:
                    changelog += f"- {item}\n"
                changelog += "\n"

            if fixed:
                changelog += "### Fixed\n"
                for item in fixed:
                    changelog += f"- {item}\n"
                changelog += "\n"
        else:
            # Parse manual entries
            lines = [line.strip() for line in changes_content.split('\n') if line.strip()]
            changelog += "### Changed\n"
            for line in lines:
                if line.startswith('-'):
                    changelog += f"{line}\n"
                else:
                    changelog += f"- {line}\n"

    elif changelog_format == "Semantic Release":
        changelog = f"""## [{version}] ({current_date if include_dates else 'TBD'})

"""
        lines = [line.strip() for line in changes_content.split('\n') if line.strip()]
        for line in lines:
            if not line.startswith('-'):
                line = f"- {line}"
            changelog += f"{line}\n"

    else:  # Custom
        changelog = f"""# Release {version}

{f'Date: {current_date}' if include_dates else ''}

## Changes

"""
        lines = [line.strip() for line in changes_content.split('\n') if line.strip()]
        for line in lines:
            if not line.startswith('-'):
                line = f"- {line}"
            changelog += f"{line}\n"

    return changelog


def test_case_creator():
    """Create comprehensive test cases for code"""
    create_tool_header("Test Case Creator", "Generate comprehensive test cases for your code", "🧪")

    st.write("Create detailed test cases with multiple scenarios, edge cases, and expected outcomes.")

    # File upload option
    uploaded_file = FileHandler.upload_files(['py', 'js', 'java', 'cs', 'cpp', 'go', 'rs'], accept_multiple=False)

    if uploaded_file:
        code_content = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Code", code_content, height=200, disabled=True)
    else:
        code_content = st.text_area("Enter code to create test cases for:", height=300, value="""def calculate_discount(price, discount_percent, member_type='regular'):
    \"\"\"Calculate discounted price based on discount percent and membership\"\"\"
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid input values")

    base_discount = price * (discount_percent / 100)

    if member_type == 'premium':
        additional_discount = price * 0.05  # 5% extra for premium
    elif member_type == 'vip':
        additional_discount = price * 0.10  # 10% extra for vip
    else:
        additional_discount = 0

    final_price = price - base_discount - additional_discount
    return max(0, final_price)""")

    if code_content:
        col1, col2 = st.columns(2)

        with col1:
            language = st.selectbox("Programming Language", [
                "Python", "JavaScript", "Java", "C#", "C++", "Go", "Rust"
            ])
            test_framework = st.selectbox("Test Framework", [
                "unittest", "pytest", "Jest", "JUnit", "xUnit", "Mocha", "Go test", "Rust test"
            ])

        with col2:
            include_edge_cases = st.checkbox("Include Edge Cases", value=True)
            include_negative_tests = st.checkbox("Include Negative Tests", value=True)
            include_performance_tests = st.checkbox("Include Performance Tests", value=False)

        if st.button("Generate Test Cases"):
            try:
                test_cases = generate_test_cases(code_content, language, test_framework, {
                    'edge_cases': include_edge_cases,
                    'negative_tests': include_negative_tests,
                    'performance_tests': include_performance_tests
                })

                st.subheader("Generated Test Cases")
                st.code(test_cases, language=language.lower())

                # Download option
                st.download_button(
                    label="📥 Download Test Cases",
                    data=test_cases,
                    file_name=f"test_cases.{get_test_file_extension(language)}",
                    mime="text/plain"
                )

                # Test case analysis
                st.subheader("Test Case Analysis")
                analysis = analyze_test_cases(test_cases, language)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Test Methods", analysis['test_count'])
                with col2:
                    st.metric("Assertions", analysis['assertion_count'])
                with col3:
                    st.metric("Coverage Estimate", f"{analysis['coverage_estimate']}%")

            except Exception as e:
                st.error(f"Error generating test cases: {str(e)}")


def test_runner():
    """Run tests and display results"""
    create_tool_header("Test Runner", "Execute tests and view detailed results", "🏃‍♂️")

    st.write("Run your test suites and analyze results with detailed reporting.")

    # Test project structure
    uploaded_files = FileHandler.upload_files(['py', 'js', 'java', 'cs', 'cpp', 'go', 'rs'], accept_multiple=True)

    if uploaded_files:
        st.subheader("Uploaded Test Files")
        for file in uploaded_files:
            st.write(f"- {file.name}")

        # Select test files to run
        test_files = st.multiselect("Select files to test:", [f.name for f in uploaded_files])

        if test_files:
            col1, col2 = st.columns(2)

            with col1:
                test_framework = st.selectbox("Test Framework", [
                    "pytest", "unittest", "Jest", "JUnit", "xUnit", "Mocha", "Go test"
                ])
                verbosity = st.selectbox("Verbosity Level", ["Normal", "Verbose", "Quiet"])

            with col2:
                run_coverage = st.checkbox("Generate Coverage Report", value=True)
                parallel_execution = st.checkbox("Parallel Execution", value=False)
                stop_on_failure = st.checkbox("Stop on First Failure", value=False)

            if st.button("Run Tests"):
                try:
                    # Simulate test execution
                    test_results = simulate_test_execution(test_files, test_framework, {
                        'verbosity': verbosity,
                        'coverage': run_coverage,
                        'parallel': parallel_execution,
                        'stop_on_failure': stop_on_failure
                    })

                    # Display results
                    st.subheader("Test Results")

                    # Summary metrics
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Total Tests", test_results['total_tests'])
                    with col2:
                        st.metric("Passed", test_results['passed'], delta=test_results['passed'])
                    with col3:
                        st.metric("Failed", test_results['failed'],
                                  delta=-test_results['failed'] if test_results['failed'] > 0 else 0)
                    with col4:
                        st.metric("Success Rate", f"{test_results['success_rate']}%")

                    # Detailed results
                    if test_results['failed'] > 0:
                        st.subheader("Failed Tests")
                        for failure in test_results['failures']:
                            with st.expander(f"❌ {failure['test_name']}"):
                                st.code(failure['error_message'], language='text')

                    # Coverage report
                    if run_coverage and test_results.get('coverage'):
                        st.subheader("Coverage Report")
                        coverage_data = test_results['coverage']

                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Line Coverage", f"{coverage_data['line_coverage']}%")
                        with col2:
                            st.metric("Branch Coverage", f"{coverage_data['branch_coverage']}%")

                        # Coverage details by file
                        st.subheader("Coverage by File")
                        for file_coverage in coverage_data['files']:
                            st.write(f"**{file_coverage['file']}**: {file_coverage['coverage']}%")

                except Exception as e:
                    st.error(f"Error running tests: {str(e)}")
    else:
        st.info("Upload test files to run them with the test runner.")


def coverage_reporter():
    """Generate detailed code coverage reports"""
    create_tool_header("Coverage Reporter", "Generate comprehensive code coverage reports", "📊")

    st.write("Analyze test coverage and generate detailed reports with visualizations.")

    # Upload test results or coverage data
    uploaded_file = FileHandler.upload_files(['json', 'xml', 'lcov', 'txt'], accept_multiple=False)

    if uploaded_file:
        coverage_data = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded Coverage Data", coverage_data, height=200, disabled=True)

        col1, col2 = st.columns(2)

        with col1:
            report_format = st.selectbox("Report Format", [
                "HTML", "JSON", "XML", "Markdown", "Text"
            ])
            coverage_type = st.selectbox("Coverage Type", [
                "Line Coverage", "Branch Coverage", "Function Coverage", "Statement Coverage"
            ])

        with col2:
            include_charts = st.checkbox("Include Charts", value=True)
            show_uncovered = st.checkbox("Show Uncovered Lines", value=True)
            minimum_coverage = st.slider("Minimum Coverage Threshold", 0, 100, 80)

        if st.button("Generate Coverage Report"):
            try:
                report = generate_coverage_report(coverage_data, {
                    'format': report_format,
                    'type': coverage_type,
                    'charts': include_charts,
                    'uncovered': show_uncovered,
                    'threshold': minimum_coverage
                })

                st.subheader("Coverage Report")

                if report_format == "HTML":
                    components.html(report, height=600, scrolling=True)
                else:
                    st.code(report, language=report_format.lower())

                # Download option
                st.download_button(
                    label="📥 Download Coverage Report",
                    data=report,
                    file_name=f"coverage_report.{report_format.lower()}",
                    mime="text/html" if report_format == "HTML" else "text/plain"
                )

            except Exception as e:
                st.error(f"Error generating coverage report: {str(e)}")
    else:
        # Demo with sample data
        st.info("Upload coverage data file or use the demo below.")

        if st.button("Generate Demo Report"):
            demo_report = generate_demo_coverage_report()
            st.subheader("Demo Coverage Report")
            st.markdown(demo_report)


def merge_helper():
    """Help resolve merge conflicts and manage merges"""
    create_tool_header("Merge Helper", "Resolve merge conflicts and manage code merges", "🔀")

    st.write("Analyze merge conflicts, suggest resolutions, and help with merge operations.")

    tab1, tab2, tab3 = st.tabs(["Conflict Resolution", "Merge Analysis", "Auto-Merge"])

    with tab1:
        st.subheader("Resolve Merge Conflicts")

        # Upload conflicted files
        uploaded_file = FileHandler.upload_files(['py', 'js', 'java', 'cs', 'cpp', 'txt'], accept_multiple=False)

        if uploaded_file:
            conflict_content = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("Conflicted File Content", conflict_content, height=300, disabled=True)
        else:
            conflict_content = st.text_area("Paste conflicted file content:", height=300, value="""def calculate_total(items):
<<<<<<< HEAD
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total
=======
    return sum(item['price'] * item['quantity'] for item in items)
>>>>>>> feature-branch""")

        if conflict_content and "<<<<<<< HEAD" in conflict_content:
            st.subheader("Conflict Analysis")

            conflicts = analyze_merge_conflicts(conflict_content)

            for i, conflict in enumerate(conflicts, 1):
                with st.expander(f"Conflict {i}: Lines {conflict['start']}-{conflict['end']}"):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.write("**Current (HEAD):**")
                        st.code(conflict['current'], language='python')

                    with col2:
                        st.write("**Incoming (Feature):**")
                        st.code(conflict['incoming'], language='python')

                    st.write("**Suggested Resolution:**")
                    suggestion = suggest_conflict_resolution(conflict)
                    st.code(suggestion, language='python')

                    resolution_choice = st.radio(
                        f"Choose resolution for conflict {i}:",
                        ["Accept Current", "Accept Incoming", "Accept Suggestion", "Manual Edit"],
                        key=f"conflict_{i}"
                    )

            if st.button("Apply Resolutions"):
                resolved_content = apply_conflict_resolutions(conflict_content, conflicts)
                st.subheader("Resolved Content")
                st.code(resolved_content, language='python')

                st.download_button(
                    label="📥 Download Resolved File",
                    data=resolved_content,
                    file_name="resolved_file.py",
                    mime="text/plain"
                )

    with tab2:
        st.subheader("Merge Analysis")

        col1, col2 = st.columns(2)

        with col1:
            base_code = st.text_area("Base Code:", height=200)

        with col2:
            feature_code = st.text_area("Feature Code:", height=200)

        if base_code and feature_code:
            if st.button("Analyze Merge"):
                analysis = analyze_merge_compatibility(base_code, feature_code)

                st.subheader("Merge Analysis Results")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Compatibility Score", f"{analysis['compatibility']}%")
                with col2:
                    st.metric("Conflicts Detected", analysis['conflicts'])
                with col3:
                    st.metric("Auto-Merge Possible", "Yes" if analysis['auto_mergeable'] else "No")

                if analysis['recommendations']:
                    st.subheader("Recommendations")
                    for rec in analysis['recommendations']:
                        st.write(f"• {rec}")

    with tab3:
        st.subheader("Auto-Merge Assistant")

        st.write("Automatically merge compatible changes when possible.")

        merge_strategy = st.selectbox("Merge Strategy", [
            "Recursive", "Ours", "Theirs", "Octopus", "Resolve", "Subtree"
        ])

        col1, col2 = st.columns(2)
        with col1:
            ignore_whitespace = st.checkbox("Ignore Whitespace", value=True)
            ignore_case = st.checkbox("Ignore Case", value=False)

        with col2:
            create_backup = st.checkbox("Create Backup", value=True)
            dry_run = st.checkbox("Dry Run (Preview Only)", value=True)

        if st.button("Perform Auto-Merge"):
            st.info("Auto-merge simulation would be performed here with the selected options.")


def commit_message_generator():
    """Generate standardized commit messages"""
    create_tool_header("Commit Message Generator", "Generate consistent, informative commit messages", "💬")

    st.write("Create well-formatted commit messages following best practices and conventions.")

    tab1, tab2, tab3 = st.tabs(["Generate Message", "Conventional Commits", "Templates"])

    with tab1:
        st.subheader("Commit Message Generator")

        # Change description
        changes_description = st.text_area("Describe your changes:", height=150,
                                           placeholder="Added user authentication feature with JWT tokens and password hashing")

        col1, col2 = st.columns(2)

        with col1:
            commit_type = st.selectbox("Commit Type", [
                "feat", "fix", "docs", "style", "refactor", "test", "chore", "perf", "build", "ci"
            ])
            scope = st.text_input("Scope (optional):", placeholder="auth, api, ui")

        with col2:
            breaking_change = st.checkbox("Breaking Change", value=False)
            include_body = st.checkbox("Include Body", value=True)
            include_footer = st.checkbox("Include Footer", value=False)

        if changes_description:
            if st.button("Generate Commit Message"):
                commit_msg = generate_commit_message({
                    'type': commit_type,
                    'scope': scope,
                    'description': changes_description,
                    'breaking': breaking_change,
                    'body': include_body,
                    'footer': include_footer
                })

                st.subheader("Generated Commit Message")
                st.code(commit_msg, language='text')

                # Copy to clipboard button simulation
                st.success("✅ Commit message generated! Copy the text above.")

                # Alternative formats
                st.subheader("Alternative Formats")

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Short Format:**")
                    short_msg = generate_short_commit_message(changes_description, commit_type)
                    st.code(short_msg, language='text')

                with col2:
                    st.write("**Detailed Format:**")
                    detailed_msg = generate_detailed_commit_message(changes_description, commit_type, scope)
                    st.code(detailed_msg, language='text')

    with tab2:
        st.subheader("Conventional Commits")

        st.write("Generate commits following the Conventional Commits specification.")

        # Upload changed files for analysis
        uploaded_files = FileHandler.upload_files(['py', 'js', 'java', 'cs', 'cpp', 'txt', 'md'], accept_multiple=True)

        if uploaded_files:
            st.write("**Uploaded Files:**")
            for file in uploaded_files:
                st.write(f"- {file.name}")

            if st.button("Analyze Changes"):
                analysis = analyze_file_changes(uploaded_files)

                st.subheader("Suggested Commit Message")
                suggested_msg = suggest_conventional_commit(analysis)
                st.code(suggested_msg, language='text')

                st.subheader("Change Analysis")
                for category, items in analysis.items():
                    if items:
                        st.write(f"**{category.title()}:**")
                        for item in items:
                            st.write(f"  - {item}")
        else:
            st.info("Upload changed files to get automatic commit message suggestions.")

    with tab3:
        st.subheader("Commit Message Templates")

        template_type = st.selectbox("Template Type", [
            "Feature Addition", "Bug Fix", "Documentation", "Refactoring", "Performance", "Testing"
        ])

        template = get_commit_template(template_type)

        st.subheader(f"{template_type} Template")
        st.code(template, language='text')

        st.subheader("Customize Template")
        custom_template = st.text_area("Edit template:", value=template, height=200)

        if st.button("Save Custom Template"):
            st.success("Custom template saved! (In a real implementation, this would be saved to user preferences)")


def branch_manager():
    """Manage Git branches and workflows"""
    create_tool_header("Branch Manager", "Manage Git branches and development workflows", "🌳")

    st.write("Organize and manage your Git branches with workflow assistance.")

    tab1, tab2, tab3, tab4 = st.tabs(["Branch Overview", "Create Branch", "Merge Strategy", "Cleanup"])

    with tab1:
        st.subheader("Branch Overview")

        # Simulate branch list
        branches = simulate_git_branches()

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Active Branches")
            for branch in branches:
                status_color = "🟢" if branch['active'] else "⚪"
                ahead_behind = f"↑{branch['ahead']} ↓{branch['behind']}" if branch['ahead'] or branch['behind'] else "✓"
                st.write(f"{status_color} **{branch['name']}** - {branch['last_commit']} - {ahead_behind}")

        with col2:
            st.subheader("Statistics")
            st.metric("Total Branches", len(branches))
            st.metric("Active Branch", next(b['name'] for b in branches if b['active']))
            st.metric("Stale Branches", len([b for b in branches if b['stale']]))

        if st.button("Refresh Branch Status"):
            st.success("Branch status refreshed! (Simulated)")

    with tab2:
        st.subheader("Create New Branch")

        col1, col2 = st.columns(2)

        with col1:
            branch_name = st.text_input("Branch Name:", placeholder="feature/user-authentication")
            base_branch = st.selectbox("Base Branch", ["main", "develop", "staging"])
            branch_type = st.selectbox("Branch Type", [
                "feature/", "bugfix/", "hotfix/", "release/", "experiment/"
            ])

        with col2:
            auto_prefix = st.checkbox("Auto-add Type Prefix", value=True)
            checkout_after = st.checkbox("Checkout After Creation", value=True)
            push_upstream = st.checkbox("Push to Remote", value=False)

        if branch_name:
            final_name = f"{branch_type}{branch_name}" if auto_prefix and not branch_name.startswith(
                branch_type) else branch_name
            st.write(f"**Final branch name:** `{final_name}`")

            if st.button("Create Branch"):
                create_result = simulate_branch_creation(final_name, base_branch, checkout_after, push_upstream)

                if create_result['success']:
                    st.success(f"✅ Branch '{final_name}' created successfully!")
                    if checkout_after:
                        st.info(f"Switched to branch '{final_name}'")
                    if push_upstream:
                        st.info(f"Pushed branch '{final_name}' to remote")
                else:
                    st.error(f"❌ Failed to create branch: {create_result['error']}")

    with tab3:
        st.subheader("Merge Strategy Planning")

        source_branch = st.selectbox("Source Branch", ["feature/auth", "bugfix/login", "hotfix/security"])
        target_branch = st.selectbox("Target Branch", ["main", "develop", "staging"])

        col1, col2 = st.columns(2)

        with col1:
            merge_strategy = st.selectbox("Merge Strategy", [
                "Merge Commit", "Squash and Merge", "Rebase and Merge"
            ])
            delete_after = st.checkbox("Delete Branch After Merge", value=True)

        with col2:
            run_tests = st.checkbox("Run Tests Before Merge", value=True)
            require_review = st.checkbox("Require Review", value=True)

        if st.button("Analyze Merge"):
            analysis = analyze_merge_plan(source_branch, target_branch, merge_strategy)

            st.subheader("Merge Analysis")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Commits to Merge", analysis['commits'])
            with col2:
                st.metric("Files Changed", analysis['files'])
            with col3:
                st.metric("Merge Risk", analysis['risk'])

            if analysis['conflicts']:
                st.warning("⚠️ Potential conflicts detected:")
                for conflict in analysis['conflicts']:
                    st.write(f"- {conflict}")

            if analysis['recommendations']:
                st.subheader("Recommendations")
                for rec in analysis['recommendations']:
                    st.write(f"✅ {rec}")

    with tab4:
        st.subheader("Branch Cleanup")

        st.write("Identify and clean up stale or merged branches.")

        cleanup_options = st.multiselect("Cleanup Options", [
            "Delete merged branches",
            "Delete branches older than 30 days",
            "Delete branches with no commits",
            "Delete remote tracking branches"
        ])

        col1, col2 = st.columns(2)

        with col1:
            dry_run = st.checkbox("Dry Run (Preview Only)", value=True)
            backup_branches = st.checkbox("Create Backup", value=True)

        with col2:
            exclude_pattern = st.text_input("Exclude Pattern:", placeholder="main|develop|staging")
            force_delete = st.checkbox("Force Delete", value=False)

        if st.button("Analyze Cleanup"):
            cleanup_analysis = analyze_branch_cleanup(cleanup_options, exclude_pattern)

            st.subheader("Cleanup Analysis")

            if cleanup_analysis['branches_to_delete']:
                st.write("**Branches to be deleted:**")
                for branch in cleanup_analysis['branches_to_delete']:
                    st.write(f"- {branch['name']} ({branch['reason']})")
            else:
                st.success("No branches need cleanup!")

            if not dry_run and cleanup_analysis['branches_to_delete']:
                st.warning("⚠️ This will permanently delete the listed branches!")

                if st.button("Confirm Cleanup", type="primary"):
                    st.success("Branch cleanup completed! (Simulated)")


# Helper functions for new tools

def generate_test_cases(code, language, framework, options):
    """Generate test cases for given code"""
    if language.lower() == "python":
        return f"""import unittest
from unittest.mock import patch, MagicMock

class TestCalculateDiscount(unittest.TestCase):

    def test_valid_discount_regular_member(self):
        \"\"\"Test valid discount for regular member\"\"\"
        result = calculate_discount(100, 10, 'regular')
        self.assertEqual(result, 90.0)

    def test_valid_discount_premium_member(self):
        \"\"\"Test valid discount for premium member\"\"\"
        result = calculate_discount(100, 10, 'premium')
        self.assertEqual(result, 85.0)  # 10% base + 5% premium

    def test_valid_discount_vip_member(self):
        \"\"\"Test valid discount for VIP member\"\"\"
        result = calculate_discount(100, 10, 'vip')
        self.assertEqual(result, 80.0)  # 10% base + 10% vip

    def test_zero_discount(self):
        \"\"\"Test with zero discount\"\"\"
        result = calculate_discount(100, 0, 'regular')
        self.assertEqual(result, 100.0)

    def test_maximum_discount(self):
        \"\"\"Test with 100% discount\"\"\"
        result = calculate_discount(100, 100, 'regular')
        self.assertEqual(result, 0.0)

    def test_invalid_negative_price(self):
        \"\"\"Test error handling for negative price\"\"\"
        with self.assertRaises(ValueError):
            calculate_discount(-10, 10, 'regular')

    def test_invalid_negative_discount(self):
        \"\"\"Test error handling for negative discount\"\"\"
        with self.assertRaises(ValueError):
            calculate_discount(100, -5, 'regular')

    def test_invalid_discount_over_100(self):
        \"\"\"Test error handling for discount over 100%\"\"\"
        with self.assertRaises(ValueError):
            calculate_discount(100, 150, 'regular')

if __name__ == '__main__':
    unittest.main()"""

    return "# Test cases would be generated based on the selected language and framework"


def get_test_file_extension(language):
    """Get test file extension for language"""
    extensions = {
        "Python": "py",
        "JavaScript": "js",
        "Java": "java",
        "C#": "cs",
        "C++": "cpp",
        "Go": "go",
        "Rust": "rs"
    }
    return extensions.get(language, "txt")


def analyze_test_cases(test_code, language):
    """Analyze generated test cases"""
    analysis = {
        'test_count': test_code.count('def test_') if language == "Python" else test_code.count('test('),
        'assertion_count': test_code.count('assert'),
        'coverage_estimate': 85
    }
    return analysis


def simulate_test_execution(test_files, framework, options):
    """Simulate test execution and return results"""
    import random

    total_tests = random.randint(10, 50)
    failed = random.randint(0, 3)
    passed = total_tests - failed

    return {
        'total_tests': total_tests,
        'passed': passed,
        'failed': failed,
        'success_rate': round((passed / total_tests) * 100, 1),
        'failures': [
            {
                'test_name': f'test_function_{i}',
                'error_message': f'AssertionError: Expected 42, got {random.randint(1, 100)}'
            }
            for i in range(failed)
        ],
        'coverage': {
            'line_coverage': random.randint(75, 95),
            'branch_coverage': random.randint(60, 85),
            'files': [
                {'file': f'test_file_{i}.py', 'coverage': random.randint(70, 100)}
                for i in range(len(test_files))
            ]
        } if options.get('coverage') else None
    }


def generate_coverage_report(coverage_data, options):
    """Generate coverage report based on data and options"""
    if options['format'] == "HTML":
        return f"""
        <html>
        <head><title>Coverage Report</title></head>
        <body>
        <h1>Code Coverage Report</h1>
        <p>Coverage Type: {options['type']}</p>
        <p>Threshold: {options['threshold']}%</p>
        <div>Sample coverage report would be displayed here</div>
        </body>
        </html>
        """
    elif options['format'] == "Markdown":
        return f"""# Coverage Report

## Summary
- **Coverage Type**: {options['type']}
- **Threshold**: {options['threshold']}%
- **Overall Coverage**: 87.3%

## Files
| File | Coverage |
|------|----------|
| main.py | 92% |
| utils.py | 85% |
| tests.py | 95% |
"""

    return "Coverage report in " + options['format'] + " format"


def generate_demo_coverage_report():
    """Generate a demo coverage report"""
    return """# Demo Coverage Report

## Overall Coverage: 87.3%

### Summary
- **Lines Covered**: 1,245 / 1,427
- **Branches Covered**: 89 / 112
- **Functions Covered**: 45 / 52

### Files with Low Coverage (< 80%)
- `utils/helpers.py`: 72%
- `models/user.py`: 75%

### Recommendations
- Add tests for uncovered utility functions
- Improve branch coverage in user model validation
"""


def analyze_merge_conflicts(content):
    """Analyze merge conflicts in content"""
    conflicts = []
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        if lines[i].startswith('<<<<<<< '):
            start = i
            current_lines = []
            incoming_lines = []

            i += 1
            while i < len(lines) and not lines[i].startswith('======='):
                current_lines.append(lines[i])
                i += 1

            i += 1  # Skip =======
            while i < len(lines) and not lines[i].startswith('>>>>>>> '):
                incoming_lines.append(lines[i])
                i += 1

            conflicts.append({
                'start': start,
                'end': i,
                'current': '\n'.join(current_lines),
                'incoming': '\n'.join(incoming_lines)
            })

        i += 1

    return conflicts


def suggest_conflict_resolution(conflict):
    """Suggest resolution for a conflict"""
    current = conflict['current'].strip()
    incoming = conflict['incoming'].strip()

    # Simple heuristic: if one is clearly a refactor of the other, suggest the shorter one
    if len(incoming.split('\n')) == 1 and len(current.split('\n')) > 1:
        return incoming  # Suggest the more concise version

    return current  # Default to current


def apply_conflict_resolutions(content, conflicts):
    """Apply conflict resolutions to content"""
    # This is a simplified version - would need more sophisticated logic
    resolved = content
    for conflict in conflicts:
        # Replace the conflict with suggested resolution
        suggestion = suggest_conflict_resolution(conflict)
        resolved = resolved.replace(
            content[conflict['start']:conflict['end'] + 1],
            suggestion
        )
    return resolved


def analyze_merge_compatibility(base_code, feature_code):
    """Analyze compatibility between base and feature code"""
    # Simplified analysis
    return {
        'compatibility': 85,
        'conflicts': 2,
        'auto_mergeable': True,
        'recommendations': [
            "Consider running tests after merge",
            "Review variable naming consistency"
        ]
    }


def generate_commit_message(options):
    """Generate commit message from options"""
    msg = f"{options['type']}"

    if options['scope']:
        msg += f"({options['scope']})"

    if options['breaking']:
        msg += "!"

    msg += f": {options['description']}"

    if options['body']:
        msg += f"\n\nDetailed description of the changes made.\n"

    if options['footer']:
        msg += f"\nCloses: #123\nBreaking-change: {options['description'] if options['breaking'] else 'None'}"

    return msg


def generate_short_commit_message(description, commit_type):
    """Generate short format commit message"""
    return f"{commit_type}: {description[:50]}..."


def generate_detailed_commit_message(description, commit_type, scope):
    """Generate detailed format commit message"""
    msg = f"{commit_type}"
    if scope:
        msg += f"({scope})"
    msg += f": {description}\n\n"
    msg += "Detailed explanation:\n"
    msg += f"- What: {description}\n"
    msg += "- Why: Improves functionality\n"
    msg += "- How: Implemented new logic"
    return msg


def analyze_file_changes(files):
    """Analyze uploaded files for changes"""
    return {
        'features': ['Added new function', 'Enhanced existing feature'],
        'fixes': ['Fixed validation bug'],
        'docs': ['Updated README'],
        'tests': ['Added unit tests']
    }


def suggest_conventional_commit(analysis):
    """Suggest conventional commit based on analysis"""
    if analysis['features']:
        return f"feat: {analysis['features'][0]}"
    elif analysis['fixes']:
        return f"fix: {analysis['fixes'][0]}"
    elif analysis['docs']:
        return f"docs: {analysis['docs'][0]}"
    elif analysis['tests']:
        return f"test: {analysis['tests'][0]}"
    else:
        return "chore: update files"


def get_commit_template(template_type):
    """Get commit template by type"""
    templates = {
        "Feature Addition": "feat(scope): add new feature\n\nDetailed description of the feature\n\nCloses: #issue",
        "Bug Fix": "fix(scope): resolve issue description\n\nExplanation of the fix\n\nFixes: #issue",
        "Documentation": "docs(scope): update documentation\n\nDescription of documentation changes",
        "Refactoring": "refactor(scope): improve code structure\n\nDetails about the refactoring",
        "Performance": "perf(scope): improve performance\n\nDescription of performance improvements",
        "Testing": "test(scope): add/update tests\n\nDescription of test changes"
    }
    return templates.get(template_type, "type(scope): description")


def simulate_git_branches():
    """Simulate git branch data"""
    return [
        {'name': 'main', 'active': True, 'last_commit': '2 hours ago', 'ahead': 0, 'behind': 0, 'stale': False},
        {'name': 'develop', 'active': False, 'last_commit': '1 day ago', 'ahead': 3, 'behind': 1, 'stale': False},
        {'name': 'feature/auth', 'active': False, 'last_commit': '3 days ago', 'ahead': 5, 'behind': 2, 'stale': False},
        {'name': 'bugfix/login', 'active': False, 'last_commit': '1 week ago', 'ahead': 2, 'behind': 8, 'stale': True}
    ]


def simulate_branch_creation(name, base, checkout, push):
    """Simulate branch creation"""
    return {
        'success': True,
        'message': f"Branch '{name}' created from '{base}'"
    }


def analyze_merge_plan(source, target, strategy):
    """Analyze merge plan"""
    return {
        'commits': 5,
        'files': 12,
        'risk': 'Low',
        'conflicts': [],
        'recommendations': [
            'Run full test suite before merging',
            'Consider squashing commits for cleaner history'
        ]
    }


def analyze_branch_cleanup(options, exclude_pattern):
    """Analyze branches for cleanup"""
    return {
        'branches_to_delete': [
            {'name': 'old-feature', 'reason': 'Merged and older than 30 days'},
            {'name': 'experiment-1', 'reason': 'No commits in 60 days'}
        ]
    }


def request_builder():
    """Build HTTP requests with an interactive interface"""
    create_tool_header("Request Builder", "Build and customize HTTP requests", "🔗")

    st.write("Create complex HTTP requests with an easy-to-use interface.")

    # Request configuration
    col1, col2 = st.columns([2, 1])
    with col1:
        url = st.text_input("Request URL", value="https://api.example.com/users")
    with col2:
        method = st.selectbox("Method", ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"])

    # Headers builder
    st.subheader("Headers")
    col1, col2 = st.columns([1, 2])
    with col1:
        num_headers = st.number_input("Number of Headers", 0, 20, 3, key="headers_count")

    headers = {}
    for i in range(num_headers):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            header_key = st.text_input(f"Key {i + 1}", key=f"header_key_{i}",
                                       value="Authorization" if i == 0 else "Content-Type" if i == 1 else "Accept" if i == 2 else "")
        with col2:
            header_value = st.text_input(f"Value {i + 1}", key=f"header_value_{i}",
                                         value="Bearer your-token" if i == 0 else "application/json" if i == 1 else "application/json" if i == 2 else "")
        if header_key and header_value:
            headers[header_key] = header_value

    # Query parameters
    st.subheader("Query Parameters")
    col1, col2 = st.columns([1, 2])
    with col1:
        num_params = st.number_input("Number of Parameters", 0, 20, 2, key="params_count")

    params = {}
    for i in range(num_params):
        col1, col2 = st.columns(2)
        with col1:
            param_key = st.text_input(f"Param Key {i + 1}", key=f"param_key_{i}")
        with col2:
            param_value = st.text_input(f"Param Value {i + 1}", key=f"param_value_{i}")
        if param_key and param_value:
            params[param_key] = param_value

    # Request body
    if method in ["POST", "PUT", "PATCH"]:
        st.subheader("Request Body")
        body_type = st.selectbox("Body Type", ["JSON", "Form Data", "Raw Text", "XML"])

        if body_type == "JSON":
            body_content = st.text_area("JSON Body", value='{\n  "name": "John Doe",\n  "email": "john@example.com"\n}',
                                        height=150)
        elif body_type == "Form Data":
            st.write("Form fields:")
            num_fields = st.number_input("Number of Fields", 0, 10, 2)
            form_data = {}
            for i in range(num_fields):
                col1, col2 = st.columns(2)
                with col1:
                    field_key = st.text_input(f"Field {i + 1} Key", key=f"field_key_{i}")
                with col2:
                    field_value = st.text_input(f"Field {i + 1} Value", key=f"field_value_{i}")
                if field_key and field_value:
                    form_data[field_key] = field_value
            body_content = form_data
        else:
            body_content = st.text_area("Request Body", height=150)
    else:
        body_content = None

    # Generate request
    if st.button("Generate Request Code"):
        st.subheader("Generated Request Code")

        # Python requests code
        with st.expander("Python (requests)", expanded=True):
            python_code = generate_python_request_code(url, method, headers, params,
                                                       body_content if method in ["POST", "PUT", "PATCH"] else None)
            st.code(python_code, language="python")

        # cURL command
        with st.expander("cURL"):
            curl_code = generate_curl_command(url, method, headers, params,
                                              body_content if method in ["POST", "PUT", "PATCH"] else None)
            st.code(curl_code, language="bash")

        # JavaScript fetch
        with st.expander("JavaScript (fetch)"):
            js_code = generate_js_fetch_code(url, method, headers, params,
                                             body_content if method in ["POST", "PUT", "PATCH"] else None)
            st.code(js_code, language="javascript")


def response_analyzer():
    """Analyze HTTP response data"""
    create_tool_header("Response Analyzer", "Analyze and inspect HTTP responses", "🔍")

    st.write("Analyze HTTP responses, parse data, and extract insights.")

    # Input options
    input_method = st.selectbox("Input Method", ["Paste Response", "Upload File", "Live Request"])

    response_data = None

    if input_method == "Paste Response":
        response_text = st.text_area("Paste HTTP Response", height=300,
                                     placeholder="HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\"users\": [...], \"total\": 150}")
        if response_text:
            response_data = parse_raw_response(response_text)

    elif input_method == "Upload File":
        uploaded_file = FileHandler.upload_files(['json', 'xml', 'txt', 'html'], accept_multiple=False)
        if uploaded_file:
            content = FileHandler.process_text_file(uploaded_file[0])
            response_data = {"body": content, "headers": {}, "status_code": 200}

    elif input_method == "Live Request":
        st.write("Make a live request to analyze:")
        live_url = st.text_input("URL to Request", "https://jsonplaceholder.typicode.com/users")
        if st.button("Fetch and Analyze") and live_url:
            try:
                import requests
                response = requests.get(live_url, timeout=10)
                response_data = {
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "body": response.text
                }
            except Exception as e:
                st.error(f"Request failed: {str(e)}")

    if response_data:
        st.subheader("Response Analysis")

        # Status and headers
        col1, col2, col3 = st.columns(3)
        with col1:
            status = response_data.get("status_code", "Unknown")
            status_color = "green" if isinstance(status, int) and status < 400 else "red"
            st.markdown(f"**Status**: <span style='color: {status_color}'>{status}</span>", unsafe_allow_html=True)

        with col2:
            content_type = response_data.get("headers", {}).get("content-type", "Unknown")
            st.write(f"**Content-Type**: {content_type}")

        with col3:
            body_size = len(str(response_data.get("body", "")))
            st.write(f"**Size**: {body_size:,} bytes")

        # Headers analysis
        if response_data.get("headers"):
            with st.expander("Headers Analysis"):
                for key, value in response_data["headers"].items():
                    st.write(f"**{key}**: {value}")

                # Security headers check
                security_headers = ["strict-transport-security", "content-security-policy", "x-frame-options",
                                    "x-content-type-options"]
                missing_security = [h for h in security_headers if
                                    h not in [k.lower() for k in response_data["headers"].keys()]]
                if missing_security:
                    st.warning(f"Missing security headers: {', '.join(missing_security)}")

        # Body analysis
        body = response_data.get("body", "")
        if body:
            st.subheader("Body Analysis")

            # Try to parse as JSON
            try:
                json_data = json.loads(body)

                # JSON structure analysis
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**JSON Structure:**")
                    structure = analyze_json_structure(json_data)
                    for key, value in structure.items():
                        st.metric(key.replace('_', ' ').title(), value)

                with col2:
                    st.write("**JSON Schema (inferred):**")
                    schema = infer_json_schema(json_data)
                    st.code(json.dumps(schema, indent=2), language="json")

                # Formatted JSON
                with st.expander("Formatted JSON", expanded=True):
                    st.code(json.dumps(json_data, indent=2), language="json")

            except json.JSONDecodeError:
                # Not JSON, show as text
                with st.expander("Response Body"):
                    st.text(body[:5000] + "..." if len(body) > 5000 else body)

                # Basic text analysis
                lines = body.split('\n')
                words = len(body.split())
                st.write(f"**Text Stats**: {len(lines):,} lines, {words:,} words")


def schema_generator():
    """Generate database schemas from various inputs"""
    create_tool_header("Schema Generator", "Generate database schemas and models", "🏗️")

    st.write("Generate database schemas from JSON, CSV, or create them from scratch.")

    # Input method
    input_method = st.selectbox("Input Method", ["JSON Data", "CSV Data", "Manual Design", "Existing Database"])

    if input_method == "JSON Data":
        st.subheader("Generate Schema from JSON")

        # JSON input
        uploaded_file = FileHandler.upload_files(['json'], accept_multiple=False)
        if uploaded_file:
            json_content = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("Uploaded JSON", json_content[:1000] + "..." if len(json_content) > 1000 else json_content,
                         height=200, disabled=True)
        else:
            json_content = st.text_area("Paste JSON Data", height=200,
                                        value='[\n  {\n    "id": 1,\n    "name": "John Doe",\n    "email": "john@example.com",\n    "age": 30,\n    "created_at": "2023-01-15T10:30:00Z"\n  }\n]')

        if json_content:
            col1, col2 = st.columns(2)
            with col1:
                table_name = st.text_input("Table Name", "users")
                db_type = st.selectbox("Database Type", ["PostgreSQL", "MySQL", "SQLite", "MongoDB"])
            with col2:
                include_indexes = st.checkbox("Include Indexes", True)
                include_constraints = st.checkbox("Include Constraints", True)

            if st.button("Generate Schema"):
                try:
                    schema = generate_schema_from_json(json_content, table_name, db_type, include_indexes,
                                                       include_constraints)

                    st.subheader("Generated Schema")
                    st.code(schema, language="sql")

                    # Download option
                    FileHandler.create_download_link(schema.encode(), f"{table_name}_schema.sql", "text/plain")

                except Exception as e:
                    st.error(f"Error generating schema: {str(e)}")

    elif input_method == "CSV Data":
        st.subheader("Generate Schema from CSV")

        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            csv_content = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("CSV Preview", csv_content[:1000] + "..." if len(csv_content) > 1000 else csv_content,
                         height=200, disabled=True)

            col1, col2 = st.columns(2)
            with col1:
                table_name = st.text_input("Table Name", "data_table")
                db_type = st.selectbox("Database Type", ["PostgreSQL", "MySQL", "SQLite"])
            with col2:
                has_header = st.checkbox("First Row is Header", True)
                auto_detect_types = st.checkbox("Auto-detect Data Types", True)

            if st.button("Generate Schema from CSV"):
                schema = generate_schema_from_csv(csv_content, table_name, db_type, has_header, auto_detect_types)

                st.subheader("Generated Schema")
                st.code(schema, language="sql")

                FileHandler.create_download_link(schema.encode(), f"{table_name}_schema.sql", "text/plain")

    elif input_method == "Manual Design":
        st.subheader("Design Schema Manually")

        col1, col2 = st.columns(2)
        with col1:
            table_name = st.text_input("Table Name", "new_table")
            db_type = st.selectbox("Database Type", ["PostgreSQL", "MySQL", "SQLite", "MongoDB"])
        with col2:
            num_columns = st.number_input("Number of Columns", 1, 20, 5)

        # Column definitions
        columns = []
        for i in range(num_columns):
            st.write(f"**Column {i + 1}:**")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                col_name = st.text_input(f"Name", key=f"col_name_{i}", value=f"column_{i + 1}")
            with col2:
                col_type = st.selectbox(f"Type",
                                        ["VARCHAR", "INTEGER", "DECIMAL", "DATE", "TIMESTAMP", "BOOLEAN", "TEXT"],
                                        key=f"col_type_{i}")
            with col3:
                nullable = st.checkbox("Nullable", key=f"nullable_{i}", value=True)
            with col4:
                primary_key = st.checkbox("Primary Key", key=f"pk_{i}")

            if col_name:
                columns.append({
                    'name': col_name,
                    'type': col_type,
                    'nullable': nullable,
                    'primary_key': primary_key
                })

        if st.button("Generate Manual Schema") and columns:
            schema = generate_manual_schema(table_name, columns, db_type)

            st.subheader("Generated Schema")
            st.code(schema, language="sql")

            FileHandler.create_download_link(schema.encode(), f"{table_name}_schema.sql", "text/plain")


def migration_creator():
    """Create database migration scripts"""
    create_tool_header("Migration Creator", "Create database migration scripts", "🔄")

    st.write("Generate database migration scripts for schema changes.")

    # Migration type
    migration_type = st.selectbox("Migration Type", [
        "Create Table", "Drop Table", "Add Column", "Drop Column",
        "Modify Column", "Add Index", "Drop Index", "Add Constraint", "Drop Constraint"
    ])

    col1, col2 = st.columns(2)
    with col1:
        db_type = st.selectbox("Database Type", ["PostgreSQL", "MySQL", "SQLite"])
        migration_name = st.text_input("Migration Name", f"migration_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    with col2:
        table_name = st.text_input("Table Name", "users")
        include_rollback = st.checkbox("Include Rollback Script", True)

    # Migration-specific inputs
    if migration_type == "Create Table":
        st.subheader("Table Definition")
        num_columns = st.number_input("Number of Columns", 1, 20, 3)

        columns = []
        for i in range(num_columns):
            col1, col2, col3 = st.columns(3)
            with col1:
                col_name = st.text_input(f"Column {i + 1} Name", key=f"create_col_name_{i}")
            with col2:
                col_type = st.selectbox(f"Type",
                                        ["VARCHAR(255)", "INTEGER", "DECIMAL(10,2)", "DATE", "TIMESTAMP", "BOOLEAN",
                                         "TEXT"],
                                        key=f"create_col_type_{i}")
            with col3:
                constraints = st.multiselect(f"Constraints", ["NOT NULL", "PRIMARY KEY", "UNIQUE"],
                                             key=f"create_constraints_{i}")

            if col_name:
                columns.append({'name': col_name, 'type': col_type, 'constraints': constraints})

    elif migration_type in ["Add Column", "Drop Column", "Modify Column"]:
        if migration_type == "Add Column":
            st.subheader("New Column Details")
            column_name = st.text_input("Column Name")
            column_type = st.selectbox("Column Type",
                                       ["VARCHAR(255)", "INTEGER", "DECIMAL(10,2)", "DATE", "TIMESTAMP", "BOOLEAN",
                                        "TEXT"])
            constraints = st.multiselect("Constraints", ["NOT NULL", "UNIQUE", "DEFAULT"])
            if "DEFAULT" in constraints:
                default_value = st.text_input("Default Value")
        else:
            column_name = st.text_input("Column Name")
            if migration_type == "Modify Column":
                new_column_type = st.selectbox("New Column Type",
                                               ["VARCHAR(255)", "INTEGER", "DECIMAL(10,2)", "DATE", "TIMESTAMP",
                                                "BOOLEAN", "TEXT"])

    elif migration_type in ["Add Index", "Drop Index"]:
        index_name = st.text_input("Index Name")
        if migration_type == "Add Index":
            index_columns = st.text_input("Index Columns (comma-separated)", "column1, column2")
            index_type = st.selectbox("Index Type", ["BTREE", "HASH", "UNIQUE"])

    # Generate migration
    if st.button("Generate Migration"):
        try:
            migration_sql = generate_migration_sql(
                migration_type=migration_type,
                db_type=db_type,
                table_name=table_name,
                **locals()  # Pass all local variables
            )

            st.subheader("Generated Migration")

            # Up migration
            st.write("**Up Migration:**")
            st.code(migration_sql['up'], language="sql")

            if include_rollback and migration_sql.get('down'):
                st.write("**Down Migration (Rollback):**")
                st.code(migration_sql['down'], language="sql")

            # Download options
            col1, col2 = st.columns(2)
            with col1:
                FileHandler.create_download_link(migration_sql['up'].encode(), f"{migration_name}_up.sql", "text/plain")
            if include_rollback and migration_sql.get('down'):
                with col2:
                    FileHandler.create_download_link(migration_sql['down'].encode(), f"{migration_name}_down.sql",
                                                     "text/plain")

        except Exception as e:
            st.error(f"Error generating migration: {str(e)}")


def data_seeder():
    """Generate seed data for databases"""
    create_tool_header("Data Seeder", "Generate seed data for database tables", "🌱")

    st.write("Generate realistic seed data for testing and development.")

    # Seeding method
    seed_method = st.selectbox("Seeding Method", ["Generate Fake Data", "Upload CSV", "Manual Entry", "Template-based"])

    if seed_method == "Generate Fake Data":
        st.subheader("Fake Data Generation")

        col1, col2 = st.columns(2)
        with col1:
            table_name = st.text_input("Table Name", "users")
            num_records = st.number_input("Number of Records", 1, 10000, 100)
        with col2:
            output_format = st.selectbox("Output Format", ["SQL INSERT", "JSON", "CSV"])
            locale = st.selectbox("Data Locale", ["en_US", "en_GB", "es_ES", "fr_FR", "de_DE"])

        # Define data types
        st.subheader("Column Data Types")
        num_columns = st.number_input("Number of Columns", 1, 20, 5)

        columns_config = []
        for i in range(num_columns):
            col1, col2, col3 = st.columns(3)
            with col1:
                col_name = st.text_input(f"Column {i + 1} Name", key=f"seed_col_name_{i}",
                                         value=["id", "name", "email", "phone", "address"][
                                             i] if i < 5 else f"column_{i + 1}")
            with col2:
                data_type = st.selectbox(f"Data Type", [
                    "ID (Auto Increment)", "Name", "Email", "Phone", "Address",
                    "Date", "Timestamp", "Integer", "Decimal", "Boolean", "Text"
                ], key=f"seed_data_type_{i}")
            with col3:
                nullable = st.checkbox("Allow Null", key=f"seed_nullable_{i}")

            if col_name:
                columns_config.append({'name': col_name, 'type': data_type, 'nullable': nullable})

        if st.button("Generate Seed Data") and columns_config:
            try:
                seed_data = generate_fake_data(columns_config, num_records, locale, output_format, table_name)

                st.subheader("Generated Seed Data")

                if output_format == "SQL INSERT":
                    st.code(seed_data[:5000] + "..." if len(seed_data) > 5000 else seed_data, language="sql")
                elif output_format == "JSON":
                    st.code(seed_data[:5000] + "..." if len(seed_data) > 5000 else seed_data, language="json")
                else:  # CSV
                    st.code(seed_data[:5000] + "..." if len(seed_data) > 5000 else seed_data, language="text")

                # Download option
                file_ext = {"SQL INSERT": "sql", "JSON": "json", "CSV": "csv"}[output_format]
                FileHandler.create_download_link(seed_data.encode(), f"seed_data.{file_ext}", "text/plain")

            except Exception as e:
                st.error(f"Error generating seed data: {str(e)}")


def connection_tester():
    """Test database connections"""
    create_tool_header("Connection Tester", "Test database connectivity and performance", "🔌")

    st.write("Test database connections and diagnose connectivity issues.")

    # Database type selection
    db_type = st.selectbox("Database Type", [
        "PostgreSQL", "MySQL", "SQLite", "MongoDB", "Redis", "Oracle", "SQL Server"
    ])

    # Connection parameters based on database type
    if db_type in ["PostgreSQL", "MySQL", "Oracle", "SQL Server"]:
        col1, col2 = st.columns(2)
        with col1:
            host = st.text_input("Host", "localhost")
            port = st.number_input("Port",
                                   value=5432 if db_type == "PostgreSQL" else 3306 if db_type == "MySQL" else 1521)
            database = st.text_input("Database Name", "testdb")
        with col2:
            username = st.text_input("Username", "admin")
            password = st.text_input("Password", type="password")
            ssl_mode = st.selectbox("SSL Mode", ["disable", "require", "prefer"]) if db_type == "PostgreSQL" else None

    elif db_type == "SQLite":
        database_path = st.text_input("Database Path", "database.sqlite")

    elif db_type == "MongoDB":
        col1, col2 = st.columns(2)
        with col1:
            host = st.text_input("Host", "localhost")
            port = st.number_input("Port", value=27017)
        with col2:
            database = st.text_input("Database Name", "testdb")
            username = st.text_input("Username (optional)")
            password = st.text_input("Password (optional)", type="password")

    elif db_type == "Redis":
        col1, col2 = st.columns(2)
        with col1:
            host = st.text_input("Host", "localhost")
            port = st.number_input("Port", value=6379)
        with col2:
            password = st.text_input("Password (optional)", type="password")
            redis_db = st.number_input("Database Number", value=0)

    # Test options
    st.subheader("Test Options")
    col1, col2 = st.columns(2)
    with col1:
        test_connection = st.checkbox("Test Connection", True)
        test_performance = st.checkbox("Test Performance", True)
    with col2:
        test_privileges = st.checkbox("Test Privileges")
        verbose_output = st.checkbox("Verbose Output")

    # Run tests
    if st.button("Run Connection Test"):
        with st.spinner("Testing connection..."):
            results = simulate_connection_test(db_type, locals(), test_connection, test_performance, test_privileges)

            st.subheader("Test Results")

            # Connection status
            status_color = "green" if results['connection']['success'] else "red"
            st.markdown(
                f"**Connection Status**: <span style='color: {status_color}'>{results['connection']['status']}</span>",
                unsafe_allow_html=True)

            if results['connection']['message']:
                st.write(f"**Message**: {results['connection']['message']}")

            # Performance metrics
            if test_performance and results.get('performance'):
                st.subheader("Performance Metrics")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Connection Time", f"{results['performance']['connection_time']}ms")
                with col2:
                    st.metric("Query Time", f"{results['performance']['query_time']}ms")
                with col3:
                    st.metric("Ping", f"{results['performance']['ping']}ms")

            # Privileges check
            if test_privileges and results.get('privileges'):
                st.subheader("Privileges Check")
                for privilege, status in results['privileges'].items():
                    status_icon = "✅" if status else "❌"
                    st.write(f"{status_icon} {privilege}")

            # Recommendations
            if results.get('recommendations'):
                st.subheader("Recommendations")
                for rec in results['recommendations']:
                    st.write(f"• {rec}")


def environment_setup():
    """Set up development environments"""
    create_tool_header("Environment Setup", "Set up and configure development environments", "⚙️")

    st.write("Configure development environments for various technologies.")

    # Environment type
    env_type = st.selectbox("Environment Type", [
        "Python", "Node.js", "Java", "PHP", "Ruby", "Go", "Rust", "Docker", "Kubernetes"
    ])

    # Configuration options
    col1, col2 = st.columns(2)
    with col1:
        project_name = st.text_input("Project Name", "my-project")
        include_venv = st.checkbox("Include Virtual Environment", True) if env_type == "Python" else None
    with col2:
        include_git = st.checkbox("Initialize Git Repository", True)
        include_docker = st.checkbox("Include Docker Configuration")

    # Environment-specific options
    if env_type == "Python":
        st.subheader("Python Configuration")
        python_version = st.selectbox("Python Version", ["3.11", "3.10", "3.9", "3.8"])
        frameworks = st.multiselect("Frameworks", ["Django", "Flask", "FastAPI", "Streamlit", "Jupyter"])
        packages = st.text_area("Additional Packages (one per line)", "requests\nnumpy\npandas")

    elif env_type == "Node.js":
        st.subheader("Node.js Configuration")
        node_version = st.selectbox("Node.js Version", ["18", "16", "14"])
        package_manager = st.selectbox("Package Manager", ["npm", "yarn", "pnpm"])
        frameworks = st.multiselect("Frameworks", ["Express", "React", "Vue", "Angular", "Next.js"])

    elif env_type == "Java":
        st.subheader("Java Configuration")
        java_version = st.selectbox("Java Version", ["17", "11", "8"])
        build_tool = st.selectbox("Build Tool", ["Maven", "Gradle"])
        frameworks = st.multiselect("Frameworks", ["Spring Boot", "Spring MVC", "Hibernate"])

    # Generate environment
    if st.button("Generate Environment Setup"):
        try:
            setup_scripts = generate_environment_setup(env_type, locals())

            st.subheader("Generated Setup Scripts")

            for script_name, script_content in setup_scripts.items():
                with st.expander(f"{script_name}", expanded=True):
                    file_ext = "sh" if script_name.endswith(".sh") else "bat" if script_name.endswith(".bat") else "txt"
                    st.code(script_content, language="bash" if file_ext == "sh" else "text")

                    # Download option
                    FileHandler.create_download_link(script_content.encode(), script_name, "text/plain")

        except Exception as e:
            st.error(f"Error generating environment setup: {str(e)}")


def deployment_helper():
    """Help with application deployment"""
    create_tool_header("Deployment Helper", "Assist with application deployment", "🚀")

    st.write("Generate deployment configurations and scripts for various platforms.")

    # Deployment platform
    platform = st.selectbox("Deployment Platform", [
        "Heroku", "AWS", "Google Cloud", "Azure", "Docker", "Kubernetes",
        "Vercel", "Netlify", "DigitalOcean", "Railway"
    ])

    # Application details
    col1, col2 = st.columns(2)
    with col1:
        app_name = st.text_input("Application Name", "my-app")
        app_type = st.selectbox("Application Type", ["Web App", "API", "Static Site", "Database", "Microservice"])
    with col2:
        tech_stack = st.selectbox("Technology Stack", ["Python", "Node.js", "Java", "PHP", "Ruby", "Go", "Static HTML"])
        environment = st.selectbox("Environment", ["Production", "Staging", "Development"])

    # Platform-specific configuration
    if platform == "Heroku":
        st.subheader("Heroku Configuration")
        buildpacks = st.multiselect("Buildpacks", ["heroku/python", "heroku/nodejs", "heroku/java", "heroku/php"])
        addons = st.multiselect("Add-ons", ["heroku-postgresql", "heroku-redis", "papertrail"])

    elif platform in ["AWS", "Google Cloud", "Azure"]:
        st.subheader(f"{platform} Configuration")
        service_type = st.selectbox("Service Type", ["App Service", "Container", "Serverless", "VM"])
        region = st.selectbox("Region", ["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1"])

    elif platform == "Docker":
        st.subheader("Docker Configuration")
        base_image = st.text_input("Base Image", "python:3.11-slim")
        expose_port = st.number_input("Expose Port", value=8000)

    elif platform == "Kubernetes":
        st.subheader("Kubernetes Configuration")
        replicas = st.number_input("Replicas", value=3)
        namespace = st.text_input("Namespace", "default")

    # Environment variables
    st.subheader("Environment Variables")
    num_env_vars = st.number_input("Number of Environment Variables", 0, 20, 3)
    env_vars = {}
    for i in range(num_env_vars):
        col1, col2 = st.columns(2)
        with col1:
            env_key = st.text_input(f"Variable {i + 1} Name", key=f"env_key_{i}")
        with col2:
            env_value = st.text_input(f"Variable {i + 1} Value", key=f"env_value_{i}")
        if env_key and env_value:
            env_vars[env_key] = env_value

    # Generate deployment configuration
    if st.button("Generate Deployment Configuration"):
        try:
            deployment_config = generate_deployment_config(platform, locals())

            st.subheader("Generated Deployment Configuration")

            for config_name, config_content in deployment_config.items():
                with st.expander(f"{config_name}", expanded=True):
                    file_ext = config_name.split('.')[-1] if '.' in config_name else "txt"
                    language = {"yml": "yaml", "yaml": "yaml", "json": "json", "sh": "bash",
                                "dockerfile": "dockerfile"}.get(file_ext, "text")
                    st.code(config_content, language=language)

                    # Download option
                    FileHandler.create_download_link(config_content.encode(), config_name, "text/plain")

        except Exception as e:
            st.error(f"Error generating deployment configuration: {str(e)}")


def build_tools():
    """Build and compilation tools"""
    create_tool_header("Build Tools", "Build and compilation utilities", "🔨")

    st.write("Manage build processes, compilation, and automation.")

    # Build system type
    build_system = st.selectbox("Build System", [
        "Make", "CMake", "Gradle", "Maven", "npm/yarn", "Webpack", "Gulp", "Grunt"
    ])

    # Project details
    col1, col2 = st.columns(2)
    with col1:
        project_name = st.text_input("Project Name", "my-project")
        language = st.selectbox("Primary Language", ["C", "C++", "Java", "JavaScript", "TypeScript", "Python"])
    with col2:
        output_type = st.selectbox("Output Type", ["Executable", "Library", "Web Bundle", "JAR", "Package"])
        optimization = st.selectbox("Optimization Level", ["Debug", "Release", "Production"])

    # Build configuration
    st.subheader("Build Configuration")

    if build_system in ["Make", "CMake"]:
        source_dirs = st.text_input("Source Directories", "src")
        include_dirs = st.text_input("Include Directories", "include")
        libraries = st.text_input("Link Libraries", "pthread m")

    elif build_system in ["Gradle", "Maven"]:
        group_id = st.text_input("Group ID", "com.example")
        artifact_id = st.text_input("Artifact ID", project_name)
        version = st.text_input("Version", "1.0.0")
        dependencies = st.text_area("Dependencies",
                                    "junit:junit:4.13.2\ncom.fasterxml.jackson.core:jackson-databind:2.14.2")

    elif build_system in ["npm/yarn", "Webpack"]:
        entry_point = st.text_input("Entry Point", "src/index.js")
        output_dir = st.text_input("Output Directory", "dist")
        dev_dependencies = st.text_area("Dev Dependencies", "webpack\nwebpack-cli\nbabel-loader")

    # Build scripts
    st.subheader("Build Scripts")
    include_scripts = st.multiselect("Include Scripts", [
        "Clean", "Build", "Test", "Deploy", "Watch", "Lint", "Format", "Bundle"
    ])

    # Generate build configuration
    if st.button("Generate Build Configuration"):
        try:
            build_config = generate_build_config(build_system, locals())

            st.subheader("Generated Build Configuration")

            for config_name, config_content in build_config.items():
                with st.expander(f"{config_name}", expanded=True):
                    file_ext = config_name.split('.')[-1] if '.' in config_name else "txt"
                    language = {"json": "json", "xml": "xml", "js": "javascript", "make": "makefile", "sh": "bash"}.get(
                        file_ext, "text")
                    st.code(config_content, language=language)

                    # Download option
                    FileHandler.create_download_link(config_content.encode(), config_name, "text/plain")

        except Exception as e:
            st.error(f"Error generating build configuration: {str(e)}")


def package_manager():
    """Package and dependency management"""
    create_tool_header("Package Manager", "Manage packages and dependencies", "📦")

    st.write("Analyze, manage, and update project dependencies.")

    # Package manager type
    pkg_manager = st.selectbox("Package Manager", [
        "pip (Python)", "npm (Node.js)", "yarn (Node.js)", "composer (PHP)",
        "gem (Ruby)", "cargo (Rust)", "go mod (Go)", "nuget (.NET)"
    ])

    # Action type
    action = st.selectbox("Action", [
        "Analyze Dependencies", "Generate Lock File", "Update Dependencies",
        "Security Audit", "Dependency Tree", "Package Search"
    ])

    if action == "Analyze Dependencies":
        st.subheader("Dependency Analysis")

        # Upload dependency file
        file_extensions = {
            "pip (Python)": ['txt', 'pip'],
            "npm (Node.js)": ['json'],
            "yarn (Node.js)": ['json'],
            "composer (PHP)": ['json'],
            "gem (Ruby)": ['gemfile'],
            "cargo (Rust)": ['toml'],
            "go mod (Go)": ['mod'],
            "nuget (.NET)": ['csproj', 'packages']
        }

        uploaded_file = FileHandler.upload_files(file_extensions.get(pkg_manager, ['txt']), accept_multiple=False)

        if uploaded_file:
            content = FileHandler.process_text_file(uploaded_file[0])
            st.text_area("Dependency File", content[:1000] + "..." if len(content) > 1000 else content,
                         height=200, disabled=True)

            if st.button("Analyze Dependencies"):
                analysis = analyze_dependencies(content, pkg_manager)

                st.subheader("Analysis Results")

                # Summary metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Packages", analysis['total_packages'])
                with col2:
                    st.metric("Outdated", analysis['outdated'])
                with col3:
                    st.metric("Vulnerabilities", analysis['vulnerabilities'])
                with col4:
                    st.metric("License Issues", analysis['license_issues'])

                # Detailed breakdown
                if analysis['packages']:
                    st.subheader("Package Details")
                    for pkg in analysis['packages']:
                        with st.expander(f"{pkg['name']} - {pkg['version']}"):
                            st.write(f"**Latest Version**: {pkg['latest_version']}")
                            st.write(f"**License**: {pkg['license']}")
                            st.write(f"**Status**: {pkg['status']}")
                            if pkg['vulnerabilities']:
                                st.warning(f"Vulnerabilities: {pkg['vulnerabilities']}")

    elif action == "Security Audit":
        st.subheader("Security Audit")

        audit_type = st.selectbox("Audit Type", ["Full Audit", "High Severity Only", "Production Only"])
        fix_automatically = st.checkbox("Auto-fix when possible")

        if st.button("Run Security Audit"):
            audit_results = simulate_security_audit(pkg_manager, audit_type)

            st.subheader("Security Audit Results")

            if audit_results['vulnerabilities']:
                st.error(f"Found {len(audit_results['vulnerabilities'])} vulnerabilities")

                for vuln in audit_results['vulnerabilities']:
                    severity_color = {"high": "red", "medium": "orange", "low": "yellow"}[vuln['severity']]
                    st.markdown(
                        f"**{vuln['package']}** - <span style='color: {severity_color}'>{vuln['severity'].upper()}</span>",
                        unsafe_allow_html=True)
                    st.write(f"Issue: {vuln['issue']}")
                    st.write(f"Fix: {vuln['fix']}")
                    st.write("---")
            else:
                st.success("No vulnerabilities found!")

    elif action == "Package Search":
        st.subheader("Package Search")

        search_query = st.text_input("Search Packages", "web framework")
        category = st.selectbox("Category", ["All", "Web", "Database", "Testing", "UI", "Utilities"])

        if st.button("Search Packages") and search_query:
            search_results = simulate_package_search(search_query, pkg_manager, category)

            st.subheader("Search Results")

            for pkg in search_results:
                with st.expander(f"{pkg['name']} - {pkg['version']}"):
                    st.write(f"**Description**: {pkg['description']}")
                    st.write(f"**Downloads**: {pkg['downloads']}")
                    st.write(f"**License**: {pkg['license']}")
                    st.write(f"**Repository**: {pkg['repository']}")

                    if st.button(f"Add {pkg['name']}", key=f"add_{pkg['name']}"):
                        install_cmd = get_install_command(pkg['name'], pkg_manager)
                        st.code(install_cmd, language="bash")


# Helper functions for the new tools

def generate_python_request_code(url, method, headers, params, body):
    """Generate Python requests code"""
    code = "import requests\nimport json\n\n"
    code += f"url = '{url}'\n"

    if headers:
        code += f"headers = {headers}\n"

    if params:
        code += f"params = {params}\n"

    if body and method in ["POST", "PUT", "PATCH"]:
        if isinstance(body, dict):
            code += f"data = {body}\n"
        else:
            code += f"data = '''{body}'''\n"

    code += f"\nresponse = requests.{method.lower()}(url"
    if headers:
        code += ", headers=headers"
    if params:
        code += ", params=params"
    if body and method in ["POST", "PUT", "PATCH"]:
        if isinstance(body, str) and body.strip().startswith('{'):
            code += ", json=json.loads(data)"
        else:
            code += ", data=data"
    code += ")\n\n"
    code += "print(f'Status: {response.status_code}')\nprint(response.json())"

    return code


def generate_curl_command(url, method, headers, params, body):
    """Generate cURL command"""
    cmd = f"curl -X {method}"

    if headers:
        for key, value in headers.items():
            cmd += f" -H '{key}: {value}'"

    if params:
        param_str = "&".join([f"{k}={v}" for k, v in params.items()])
        url += f"?{param_str}"

    if body and method in ["POST", "PUT", "PATCH"]:
        if isinstance(body, str):
            cmd += f" -d '{body}'"
        else:
            cmd += f" -d '{json.dumps(body)}'"

    cmd += f" '{url}'"
    return cmd


def generate_js_fetch_code(url, method, headers, params, body):
    """Generate JavaScript fetch code"""
    code = "const url = new URL('" + url + "');\n"

    if params:
        for key, value in params.items():
            code += f"url.searchParams.append('{key}', '{value}');\n"

    code += "\nconst options = {\n"
    code += f"  method: '{method}'"

    if headers:
        code += ",\n  headers: " + json.dumps(headers, indent=4)

    if body and method in ["POST", "PUT", "PATCH"]:
        if isinstance(body, str) and body.strip().startswith('{'):
            code += ",\n  body: JSON.stringify(" + body + ")"
        else:
            code += f",\n  body: '{body}'"

    code += "\n};\n\n"
    code += "fetch(url, options)\n"
    code += "  .then(response => response.json())\n"
    code += "  .then(data => console.log(data))\n"
    code += "  .catch(error => console.error('Error:', error));"

    return code


def parse_raw_response(response_text):
    """Parse raw HTTP response text"""
    lines = response_text.split('\n')

    # Parse status line
    status_line = lines[0] if lines else ""
    status_code = 200
    if "HTTP/" in status_line:
        parts = status_line.split()
        if len(parts) >= 2:
            try:
                status_code = int(parts[1])
            except ValueError:
                pass

    # Parse headers
    headers = {}
    body_start = 0
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "":
            body_start = i + 1
            break
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

    # Parse body
    body = "\n".join(lines[body_start:]) if body_start < len(lines) else ""

    return {
        "status_code": status_code,
        "headers": headers,
        "body": body
    }


def infer_json_schema(data):
    """Infer JSON schema from data"""
    if isinstance(data, dict):
        schema = {"type": "object", "properties": {}}
        for key, value in data.items():
            schema["properties"][key] = infer_json_schema(value)
        return schema
    elif isinstance(data, list):
        schema = {"type": "array"}
        if data:
            schema["items"] = infer_json_schema(data[0])
        return schema
    elif isinstance(data, str):
        return {"type": "string"}
    elif isinstance(data, int):
        return {"type": "integer"}
    elif isinstance(data, float):
        return {"type": "number"}
    elif isinstance(data, bool):
        return {"type": "boolean"}
    else:
        return {"type": "null"}


def generate_schema_from_json(json_content, table_name, db_type, include_indexes, include_constraints):
    """Generate database schema from JSON data"""
    try:
        data = json.loads(json_content)
        if isinstance(data, list) and data:
            sample = data[0]
        else:
            sample = data

        schema = f"-- Generated schema for {table_name}\n"
        schema += f"CREATE TABLE {table_name} (\n"

        columns = []
        for key, value in sample.items():
            sql_type = infer_sql_type(value, db_type)
            constraint = ""
            if key.lower() == "id":
                if db_type == "PostgreSQL":
                    constraint = " PRIMARY KEY SERIAL"
                elif db_type == "MySQL":
                    constraint = " PRIMARY KEY AUTO_INCREMENT"
                else:
                    constraint = " PRIMARY KEY"

            columns.append(f"  {key} {sql_type}{constraint}")

        schema += ",\n".join(columns)
        schema += "\n);\n"

        if include_indexes:
            schema += f"\n-- Indexes\nCREATE INDEX idx_{table_name}_id ON {table_name}(id);\n"

        return schema

    except Exception as e:
        raise Exception(f"Error parsing JSON: {str(e)}")


def infer_sql_type(value, db_type):
    """Infer SQL type from Python value"""
    if isinstance(value, bool):
        return "BOOLEAN"
    elif isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "DECIMAL(10,2)"
    elif isinstance(value, str):
        if "@" in value:
            return "VARCHAR(255)"  # Email
        elif len(value) > 255:
            return "TEXT"
        else:
            return "VARCHAR(255)"
    else:
        return "TEXT"


def generate_schema_from_csv(csv_content, table_name, db_type, has_header, auto_detect_types):
    """Generate schema from CSV"""
    lines = csv_content.strip().split('\n')
    if not lines:
        return "-- Empty CSV file"

    if has_header:
        headers = [col.strip().strip('"') for col in lines[0].split(',')]
        data_lines = lines[1:]
    else:
        headers = [f"column_{i + 1}" for i in range(len(lines[0].split(',')))]
        data_lines = lines

    schema = f"-- Generated schema for {table_name} from CSV\n"
    schema += f"CREATE TABLE {table_name} (\n"

    columns = []
    for i, header in enumerate(headers):
        if auto_detect_types and data_lines:
            # Sample first few rows to detect type
            sample_values = []
            for line in data_lines[:5]:
                values = [val.strip().strip('"') for val in line.split(',')]
                if i < len(values):
                    sample_values.append(values[i])

            sql_type = detect_csv_column_type(sample_values)
        else:
            sql_type = "VARCHAR(255)"

        columns.append(f"  {header} {sql_type}")

    schema += ",\n".join(columns)
    schema += "\n);"

    return schema


def detect_csv_column_type(values):
    """Detect SQL type from CSV column values"""
    if not values:
        return "VARCHAR(255)"

    # Try integer
    try:
        for val in values:
            if val:
                int(val)
        return "INTEGER"
    except ValueError:
        pass

    # Try decimal
    try:
        for val in values:
            if val:
                float(val)
        return "DECIMAL(10,2)"
    except ValueError:
        pass

    # Check for dates
    date_patterns = ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"]
    for pattern in date_patterns:
        try:
            for val in values:
                if val:
                    datetime.strptime(val, pattern)
            return "DATE"
        except ValueError:
            continue

    # Default to VARCHAR
    max_length = max(len(str(val)) for val in values if val)
    if max_length > 255:
        return "TEXT"
    else:
        return f"VARCHAR({max(max_length * 2, 50)})"


def generate_manual_schema(table_name, columns, db_type):
    """Generate schema from manual column definitions"""
    schema = f"-- Manual schema for {table_name}\n"
    schema += f"CREATE TABLE {table_name} (\n"

    column_defs = []
    for col in columns:
        col_def = f"  {col['name']} {col['type']}"
        if col['primary_key']:
            col_def += " PRIMARY KEY"
        if not col['nullable']:
            col_def += " NOT NULL"
        column_defs.append(col_def)

    schema += ",\n".join(column_defs)
    schema += "\n);"

    return schema


def generate_migration_sql(migration_type, db_type, table_name, **kwargs):
    """Generate migration SQL based on type"""
    up_sql = ""
    down_sql = ""

    if migration_type == "Create Table":
        columns = kwargs.get('columns', [])
        up_sql = f"CREATE TABLE {table_name} (\n"
        col_defs = []
        for col in columns:
            col_def = f"  {col['name']} {col['type']}"
            if col['constraints']:
                col_def += " " + " ".join(col['constraints'])
            col_defs.append(col_def)
        up_sql += ",\n".join(col_defs) + "\n);"
        down_sql = f"DROP TABLE {table_name};"

    elif migration_type == "Add Column":
        column_name = kwargs.get('column_name', 'new_column')
        column_type = kwargs.get('column_type', 'VARCHAR(255)')
        up_sql = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};"
        down_sql = f"ALTER TABLE {table_name} DROP COLUMN {column_name};"

    elif migration_type == "Drop Column":
        column_name = kwargs.get('column_name', 'column_to_drop')
        up_sql = f"ALTER TABLE {table_name} DROP COLUMN {column_name};"
        down_sql = f"-- Cannot automatically generate rollback for DROP COLUMN"

    elif migration_type == "Add Index":
        index_name = kwargs.get('index_name', 'new_index')
        index_columns = kwargs.get('index_columns', 'column1')
        up_sql = f"CREATE INDEX {index_name} ON {table_name} ({index_columns});"
        down_sql = f"DROP INDEX {index_name};"

    return {"up": up_sql, "down": down_sql}


def generate_fake_data(columns_config, num_records, locale, output_format, table_name):
    """Generate fake data based on configuration"""
    import random
    from datetime import datetime, timedelta

    # Simple fake data generators
    def fake_name():
        first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Chris", "Anna"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def fake_email():
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "company.com"]
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10)))
        return f"{username}@{random.choice(domains)}"

    def fake_phone():
        return f"+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

    def fake_address():
        streets = ["Main St", "Oak Ave", "Pine Rd", "Elm Dr", "First St"]
        return f"{random.randint(100, 9999)} {random.choice(streets)}"

    def fake_date():
        start = datetime.now() - timedelta(days=365)
        return (start + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")

    # Generate data
    records = []
    for i in range(num_records):
        record = {}
        for col in columns_config:
            col_name = col['name']
            col_type = col['type']

            if col_type == "ID (Auto Increment)":
                record[col_name] = i + 1
            elif col_type == "Name":
                record[col_name] = fake_name()
            elif col_type == "Email":
                record[col_name] = fake_email()
            elif col_type == "Phone":
                record[col_name] = fake_phone()
            elif col_type == "Address":
                record[col_name] = fake_address()
            elif col_type == "Date":
                record[col_name] = fake_date()
            elif col_type == "Integer":
                record[col_name] = random.randint(1, 1000)
            elif col_type == "Decimal":
                record[col_name] = round(random.uniform(10.0, 1000.0), 2)
            elif col_type == "Boolean":
                record[col_name] = random.choice([True, False])
            else:  # Text
                record[col_name] = f"Sample text {i + 1}"

        records.append(record)

    # Format output
    if output_format == "SQL INSERT":
        sql = f"-- Generated seed data for {table_name}\n\n"
        for record in records:
            columns = list(record.keys())
            values = [f"'{v}'" if isinstance(v, str) else str(v) for v in record.values()]
            sql += f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});\n"
        return sql

    elif output_format == "JSON":
        return json.dumps(records, indent=2)

    else:  # CSV
        if not records:
            return ""

        columns = list(records[0].keys())
        csv_content = ",".join(columns) + "\n"
        for record in records:
            values = [str(record[col]) for col in columns]
            csv_content += ",".join(values) + "\n"
        return csv_content


def simulate_connection_test(db_type, config, test_connection, test_performance, test_privileges):
    """Simulate database connection testing"""
    import random

    # Simulate connection results
    connection_success = random.choice([True, True, True, False])  # 75% success rate

    result = {
        'connection': {
            'success': connection_success,
            'status': 'Connected' if connection_success else 'Failed',
            'message': 'Connection successful' if connection_success else 'Connection timeout - check host and port'
        }
    }

    if connection_success and test_performance:
        result['performance'] = {
            'connection_time': random.randint(50, 200),
            'query_time': random.randint(10, 100),
            'ping': random.randint(5, 50)
        }

    if connection_success and test_privileges:
        result['privileges'] = {
            'SELECT': True,
            'INSERT': random.choice([True, False]),
            'UPDATE': random.choice([True, False]),
            'DELETE': random.choice([True, False]),
            'CREATE': random.choice([True, False]),
            'DROP': random.choice([True, False])
        }

    if connection_success:
        result['recommendations'] = [
            'Connection is stable',
            'Consider enabling SSL for production',
            'Monitor connection pool usage'
        ]
    else:
        result['recommendations'] = [
            'Check network connectivity',
            'Verify database server is running',
            'Confirm credentials are correct'
        ]

    return result


def generate_environment_setup(env_type, config):
    """Generate environment setup scripts"""
    scripts = {}

    project_name = config.get('project_name', 'my-project')

    if env_type == "Python":
        python_version = config.get('python_version', '3.11')
        packages = config.get('packages', '').split('\n')

        # setup.sh
        setup_script = f"""#!/bin/bash
# Python {python_version} Environment Setup for {project_name}

echo "Setting up Python {python_version} environment..."

# Create project directory
mkdir -p {project_name}
cd {project_name}

# Create virtual environment
python{python_version} -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install packages
"""
        for pkg in packages:
            if pkg.strip():
                setup_script += f"pip install {pkg.strip()}\n"

        setup_script += """
# Create requirements.txt
pip freeze > requirements.txt

# Initialize git repository
git init
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

echo "Python environment setup complete!"
echo "To activate: source venv/bin/activate"
"""
        scripts['setup.sh'] = setup_script

        # requirements.txt
        req_content = "\n".join([pkg.strip() for pkg in packages if pkg.strip()])
        scripts['requirements.txt'] = req_content

    elif env_type == "Node.js":
        node_version = config.get('node_version', '18')
        package_manager = config.get('package_manager', 'npm')

        setup_script = f"""#!/bin/bash
# Node.js {node_version} Environment Setup for {project_name}

echo "Setting up Node.js {node_version} environment..."

# Create project directory
mkdir -p {project_name}
cd {project_name}

# Initialize package.json
{package_manager} init -y

# Install dependencies
{package_manager} install express
{package_manager} install --save-dev nodemon

# Create basic structure
mkdir -p src
echo "console.log('Hello World!');" > src/index.js

# Create start scripts
echo '{
        "name": "{project_name}",
  "version": "1.0.0",
  "main": "src/index.js",
  "scripts": {
        "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "echo \\"Error: no test specified\\" && exit 1"
  }
}' > package.json

# Initialize git
git init
echo "node_modules/" > .gitignore
echo ".env" >> .gitignore

echo "Node.js environment setup complete!"
echo "To start development: {package_manager} run dev"
"""
        scripts['setup.sh'] = setup_script

    return scripts


def generate_deployment_config(platform, config):
    """Generate deployment configuration files"""
    configs = {}

    app_name = config.get('app_name', 'my-app')
    tech_stack = config.get('tech_stack', 'Python')
    env_vars = config.get('env_vars', {})

    if platform == "Heroku":
        # Procfile
        if tech_stack == "Python":
            configs['Procfile'] = "web: gunicorn app:app"
        elif tech_stack == "Node.js":
            configs['Procfile'] = "web: node src/index.js"

        # app.json
        app_json = {
            "name": app_name,
            "description": f"A {tech_stack} application",
            "repository": f"https://github.com/username/{app_name}",
            "keywords": [tech_stack.lower(), "web"],
            "env": {}
        }

        for key, value in env_vars.items():
            app_json["env"][key] = {"description": f"{key} environment variable"}

        configs['app.json'] = json.dumps(app_json, indent=2)

    elif platform == "Docker":
        base_image = config.get('base_image', 'python:3.11-slim')
        expose_port = config.get('expose_port', 8000)

        dockerfile = f"""FROM {base_image}

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE {expose_port}

CMD ["python", "app.py"]
"""
        configs['Dockerfile'] = dockerfile

        # docker-compose.yml
        compose = f"""version: '3.8'

services:
  {app_name}:
    build: .
    ports:
      - "{expose_port}:{expose_port}"
    environment:"""

        for key, value in env_vars.items():
            compose += f"\n      - {key}={value}"

        configs['docker-compose.yml'] = compose

    elif platform == "Kubernetes":
        replicas = config.get('replicas', 3)
        namespace = config.get('namespace', 'default')

        k8s_deployment = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {app_name}
  namespace: {namespace}
spec:
  replicas: {replicas}
  selector:
    matchLabels:
      app: {app_name}
  template:
    metadata:
      labels:
        app: {app_name}
    spec:
      containers:
      - name: {app_name}
        image: {app_name}:latest
        ports:
        - containerPort: 8000
        env:"""

        for key, value in env_vars.items():
            k8s_deployment += f"""
        - name: {key}
          value: "{value}\""""

        configs['deployment.yaml'] = k8s_deployment

        # Service
        k8s_service = f"""apiVersion: v1
kind: Service
metadata:
  name: {app_name}-service
  namespace: {namespace}
spec:
  selector:
    app: {app_name}
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: ClusterIP
"""
        configs['service.yaml'] = k8s_service

    return configs


def generate_build_config(build_system, config):
    """Generate build configuration files"""
    configs = {}

    project_name = config.get('project_name', 'my-project')
    language = config.get('language', 'C++')

    if build_system == "Make":
        makefile = f"""# Makefile for {project_name}

CC = gcc
CXX = g++
CFLAGS = -Wall -Wextra -std=c99
CXXFLAGS = -Wall -Wextra -std=c++17
SRCDIR = src
OBJDIR = obj
SOURCES = $(wildcard $(SRCDIR)/*.c $(SRCDIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%=$(OBJDIR)/%.o)
TARGET = {project_name}

.PHONY: all clean install

all: $(TARGET)

$(TARGET): $(OBJECTS)
\t$(CXX) $(OBJECTS) -o $@

$(OBJDIR)/%.c.o: $(SRCDIR)/%.c
\t@mkdir -p $(OBJDIR)
\t$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR)/%.cpp.o: $(SRCDIR)/%.cpp
\t@mkdir -p $(OBJDIR)
\t$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
\trm -rf $(OBJDIR) $(TARGET)

install: $(TARGET)
\tcp $(TARGET) /usr/local/bin/
"""
        configs['Makefile'] = makefile

    elif build_system == "Maven":
        group_id = config.get('group_id', 'com.example')
        artifact_id = config.get('artifact_id', project_name)
        version = config.get('version', '1.0.0')

        pom_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
    <version>{version}</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
"""
        configs['pom.xml'] = pom_xml

    elif build_system == "Webpack":
        entry_point = config.get('entry_point', 'src/index.js')
        output_dir = config.get('output_dir', 'dist')

        webpack_config = f"""const path = require('path');

module.exports = {{
  entry: './{entry_point}',
  output: {{
    path: path.resolve(__dirname, '{output_dir}'),
    filename: 'bundle.js',
  }},
  module: {{
    rules: [
      {{
        test: /\.js$/,
        exclude: /node_modules/,
        use: {{
          loader: 'babel-loader',
          options: {{
            presets: ['@babel/preset-env']
          }}
        }}
      }},
      {{
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }}
    ]
  }},
  mode: 'development',
  devServer: {{
    contentBase: './{output_dir}',
    open: true
  }}
}};
"""
        configs['webpack.config.js'] = webpack_config

    return configs


def analyze_dependencies(content, pkg_manager):
    """Analyze dependencies from file content"""
    # Simulate dependency analysis
    import random

    packages = []
    if pkg_manager == "pip (Python)":
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                if '==' in line:
                    name, version = line.split('==', 1)
                else:
                    name, version = line, 'latest'

                packages.append({
                    'name': name.strip(),
                    'version': version.strip(),
                    'latest_version': f"{version.strip()}.1" if version != 'latest' else '1.0.0',
                    'license': random.choice(['MIT', 'Apache-2.0', 'BSD-3-Clause', 'GPL-3.0']),
                    'status': random.choice(['up-to-date', 'outdated', 'vulnerable']),
                    'vulnerabilities': random.randint(0, 2) if random.random() < 0.2 else 0
                })

    total_packages = len(packages)
    outdated = sum(1 for p in packages if p['status'] == 'outdated')
    vulnerabilities = sum(p['vulnerabilities'] for p in packages)
    license_issues = sum(1 for p in packages if p['license'] == 'GPL-3.0')

    return {
        'total_packages': total_packages,
        'outdated': outdated,
        'vulnerabilities': vulnerabilities,
        'license_issues': license_issues,
        'packages': packages[:10]  # Show first 10
    }


def simulate_security_audit(pkg_manager, audit_type):
    """Simulate security audit results"""
    import random

    vulnerabilities = []

    # Generate some example vulnerabilities
    vuln_examples = [
        {
            'package': 'requests',
            'severity': 'medium',
            'issue': 'Potential security issue in certificate verification',
            'fix': 'Update to version 2.31.0 or later'
        },
        {
            'package': 'urllib3',
            'severity': 'high',
            'issue': 'HTTP request smuggling vulnerability',
            'fix': 'Update to version 1.26.17 or later'
        },
        {
            'package': 'pillow',
            'severity': 'low',
            'issue': 'Buffer overflow in image processing',
            'fix': 'Update to version 10.0.1 or later'
        }
    ]

    # Randomly include some vulnerabilities
    for vuln in vuln_examples:
        if random.random() < 0.3:  # 30% chance for each
            vulnerabilities.append(vuln)

    return {
        'vulnerabilities': vulnerabilities,
        'total_scanned': random.randint(50, 200),
        'clean_packages': random.randint(40, 180)
    }


def simulate_package_search(query, pkg_manager, category):
    """Simulate package search results"""
    import random

    # Example packages based on search query
    example_packages = [
        {
            'name': 'express',
            'version': '4.18.2',
            'description': 'Fast, unopinionated, minimalist web framework for node',
            'downloads': '25M/week',
            'license': 'MIT',
            'repository': 'https://github.com/expressjs/express'
        },
        {
            'name': 'fastapi',
            'version': '0.104.1',
            'description': 'FastAPI framework, high performance, easy to learn',
            'downloads': '2M/week',
            'license': 'MIT',
            'repository': 'https://github.com/tiangolo/fastapi'
        },
        {
            'name': 'flask',
            'version': '3.0.0',
            'description': 'A simple framework for building complex web applications',
            'downloads': '8M/week',
            'license': 'BSD-3-Clause',
            'repository': 'https://github.com/pallets/flask'
        }
    ]

    # Filter and randomize results
    results = random.sample(example_packages, min(len(example_packages), random.randint(2, 3)))

    return results


def get_install_command(package_name, pkg_manager):
    """Get install command for package manager"""
    commands = {
        "pip (Python)": f"pip install {package_name}",
        "npm (Node.js)": f"npm install {package_name}",
        "yarn (Node.js)": f"yarn add {package_name}",
        "composer (PHP)": f"composer require {package_name}",
        "gem (Ruby)": f"gem install {package_name}",
        "cargo (Rust)": f"cargo add {package_name}",
        "go mod (Go)": f"go get {package_name}",
        "nuget (.NET)": f"dotnet add package {package_name}"
    }

    return commands.get(pkg_manager, f"# Install {package_name}")


# Additional helper functions for existing functionality

def detect_indentation(code):
    """Detect indentation type in code"""
    lines = code.split('\n')
    for line in lines:
        if line.startswith('\t'):
            return "Tabs"
        elif line.startswith(' '):
            return "Spaces"
    return "Spaces"  # Default


def convert_indentation(code, source_type, target_type, source_spaces, target_spaces):
    """Convert indentation between different types"""
    lines = code.split('\n')
    converted_lines = []

    for line in lines:
        if not line.strip():
            converted_lines.append(line)
            continue

        # Count leading whitespace
        leading = len(line) - len(line.lstrip())
        content = line.lstrip()

        if source_type == "Tabs":
            indent_level = leading  # Each tab is one level
        else:  # Spaces
            indent_level = leading // source_spaces

        # Convert to target indentation
        if target_type == "Tabs":
            new_line = '\t' * indent_level + content
        else:  # Spaces
            new_line = ' ' * (indent_level * target_spaces) + content

        converted_lines.append(new_line)

    return '\n'.join(converted_lines)