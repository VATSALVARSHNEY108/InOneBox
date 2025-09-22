import streamlit as st
import pandas as pd
import numpy as np
import json
import csv
from io import StringIO, BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler
from utils.ai_client import ai_client
import sqlite3
import tempfile
import os
import io
import re
from collections import Counter, defaultdict
import string
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans


def display_tools():
    """Display all data analysis tools"""

    tool_categories = {
        "Data Import/Export": [
            "CSV Converter", "JSON Converter", "Excel Reader", "Data Format Converter", "Database Connector"
        ],
        "Data Cleaning": [
            "Missing Value Handler", "Duplicate Remover", "Data Validator", "Data Type Converter", "Outlier Detector"
        ],
        "Data Analysis": [
            "Statistical Summary", "Correlation Analysis", "Data Profiling", "Distribution Analysis", "Trend Analysis",
            "Data Insights", "Statistical Analysis"
        ],
        "Data Visualization": [
            "Chart Generator", "Heatmap Creator", "Scatter Plot", "Time Series Plot", "Dashboard Builder"
        ],
        "Data Transformation": [
            "Pivot Table Creator", "Data Aggregator", "Column Calculator", "Data Merger", "Data Splitter"
        ],
        "Machine Learning": [
            "Linear Regression", "Advanced Regression", "Classification Models", "Ensemble Methods",
            "Clustering Analysis", "Feature Selection", "Model Evaluator", "Cross Validation", "Pattern Recognition",
            "Predictive Modeling"
        ],
        "Text Analytics": [
            "Text Mining", "Sentiment Analysis", "Word Frequency", "N-gram Analysis", "Topic Modeling"
        ],
        "Time Series": [
            "Trend Decomposition", "Seasonality Analysis", "Forecasting", "Time Series Plot", "Moving Averages"
        ],
        "Statistical Tests": [
            "T-Test", "Chi-Square Test", "ANOVA", "Normality Test", "Hypothesis Testing"
        ],
        "Data Quality": [
            "Data Profiling", "Quality Assessment", "Completeness Check", "Consistency Validator", "Accuracy Measure"
        ]
    }

    selected_category = st.selectbox("Select Data Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Data Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "CSV Converter":
        csv_converter()
    elif selected_tool == "JSON Converter":
        json_converter()
    elif selected_tool == "Statistical Summary":
        statistical_summary()
    elif selected_tool == "Chart Generator":
        chart_generator()
    elif selected_tool == "Missing Value Handler":
        missing_value_handler()
    elif selected_tool == "Correlation Analysis":
        correlation_analysis()
    elif selected_tool == "Data Validator":
        data_validator()
    elif selected_tool == "Duplicate Remover":
        duplicate_remover()
    elif selected_tool == "Data Type Converter":
        data_type_converter()
    elif selected_tool == "Outlier Detector":
        outlier_detector()
    elif selected_tool == "Pivot Table Creator":
        pivot_table_creator()
    elif selected_tool == "Linear Regression":
        linear_regression()
    elif selected_tool == "Advanced Regression":
        advanced_regression()
    elif selected_tool == "Classification Models":
        classification_models()
    elif selected_tool == "Ensemble Methods":
        ensemble_methods()
    elif selected_tool == "Feature Selection":
        feature_selection()
    elif selected_tool == "Model Evaluator":
        model_evaluator()
    elif selected_tool == "Cross Validation":
        cross_validation()
    elif selected_tool == "Trend Analysis":
        trend_analysis()
    elif selected_tool == "Data Profiling":
        data_profiling()
    elif selected_tool == "Distribution Analysis":
        distribution_analysis()
    elif selected_tool == "Forecasting":
        forecasting()
    elif selected_tool == "Clustering Analysis":
        clustering_analysis()
    elif selected_tool == "T-Test":
        t_test_analysis()
    elif selected_tool == "ANOVA":
        anova_analysis()
    elif selected_tool == "Moving Averages":
        moving_averages()
    elif selected_tool == "Trend Decomposition":
        trend_decomposition()
    elif selected_tool == "Seasonality Analysis":
        seasonality_analysis()
    elif selected_tool == "Excel Reader":
        excel_reader()
    elif selected_tool == "Data Format Converter":
        data_format_converter()
    elif selected_tool == "Database Connector":
        database_connector()
    elif selected_tool == "Heatmap Creator":
        heatmap_creator()
    elif selected_tool == "Scatter Plot":
        scatter_plot()
    elif selected_tool == "Time Series Plot":
        time_series_plot()
    elif selected_tool == "Dashboard Builder":
        dashboard_builder()
    elif selected_tool == "Data Aggregator":
        data_aggregator()
    elif selected_tool == "Column Calculator":
        column_calculator()
    elif selected_tool == "Data Merger":
        data_merger()
    elif selected_tool == "Data Splitter":
        data_splitter()
    elif selected_tool == "Text Mining":
        text_mining()
    elif selected_tool == "Sentiment Analysis":
        sentiment_analysis()
    elif selected_tool == "Word Frequency":
        word_frequency()
    elif selected_tool == "N-gram Analysis":
        ngram_analysis()
    elif selected_tool == "Topic Modeling":
        topic_modeling()
    elif selected_tool == "Quality Assessment":
        quality_assessment()
    elif selected_tool == "Completeness Check":
        completeness_check()
    elif selected_tool == "Consistency Validator":
        consistency_validator()
    elif selected_tool == "Accuracy Measure":
        accuracy_measure()
    elif selected_tool == "Data Insights":
        data_insights()
    elif selected_tool == "Statistical Analysis":
        statistical_analysis()
    elif selected_tool == "Pattern Recognition":
        pattern_recognition()
    elif selected_tool == "Predictive Modeling":
        predictive_modeling()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def csv_converter():
    """Convert between different data formats"""
    create_tool_header("CSV Converter", "Convert CSV to other formats and vice versa", "📊")

    conversion_type = st.selectbox("Conversion Type:", [
        "CSV to JSON", "JSON to CSV", "CSV to Excel", "Excel to CSV"
    ])

    if conversion_type in ["CSV to JSON", "CSV to Excel"]:
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                st.dataframe(df.head())

                if conversion_type == "CSV to JSON":
                    convert_csv_to_json(df)
                else:
                    convert_csv_to_excel(df)

    elif conversion_type == "JSON to CSV":
        uploaded_file = FileHandler.upload_files(['json'], accept_multiple=False)
        if uploaded_file:
            json_data = FileHandler.process_text_file(uploaded_file[0])
            convert_json_to_csv(json_data)

    elif conversion_type == "Excel to CSV":
        uploaded_file = FileHandler.upload_files(['xlsx', 'xls'], accept_multiple=False)
        if uploaded_file:
            try:
                df = pd.read_excel(uploaded_file[0])
                st.dataframe(df.head())
                convert_excel_to_csv(df)
            except Exception as e:
                st.error(f"Error reading Excel file: {str(e)}")


def convert_csv_to_json(df):
    """Convert CSV DataFrame to JSON"""
    json_format = st.selectbox("JSON Format:", ["Records", "Index", "Values"])

    if st.button("Convert to JSON"):
        try:
            if json_format == "Records":
                json_data = df.to_json(orient='records', indent=2)
            elif json_format == "Index":
                json_data = df.to_json(orient='index', indent=2)
            else:
                json_data = df.to_json(orient='values', indent=2)

            st.code(json_data, language='json')
            FileHandler.create_download_link(json_data.encode(), "converted_data.json", "application/json")
            st.success("✅ Conversion completed!")
        except Exception as e:
            st.error(f"Conversion error: {str(e)}")


def convert_csv_to_excel(df):
    """Convert CSV DataFrame to Excel"""
    if st.button("Convert to Excel"):
        try:
            # Create a temporary file path for Excel conversion
            import tempfile
            import os

            with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp_file:
                temp_path = tmp_file.name

            # Write Excel file to temp path
            with pd.ExcelWriter(temp_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Data', index=False)

            # Read the file and create download
            with open(temp_path, 'rb') as f:
                excel_data = f.read()

            # Clean up temp file
            os.unlink(temp_path)

            FileHandler.create_download_link(excel_data, "converted_data.xlsx",
                                             "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            st.success("✅ Conversion completed!")
        except Exception as e:
            st.error(f"Conversion error: {str(e)}")


def convert_json_to_csv(json_data):
    """Convert JSON to CSV"""
    try:
        data = json.loads(json_data)

        if isinstance(data, list):
            df = pd.DataFrame(data)
        elif isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            st.error("JSON format not supported for CSV conversion")
            return

        st.dataframe(df.head())

        if st.button("Convert to CSV"):
            csv_data = df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "converted_data.csv", "text/csv")
            st.success("✅ Conversion completed!")

    except json.JSONDecodeError:
        st.error("Invalid JSON format")
    except Exception as e:
        st.error(f"Conversion error: {str(e)}")


def convert_excel_to_csv(df):
    """Convert Excel DataFrame to CSV"""
    if st.button("Convert to CSV"):
        try:
            csv_data = df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "converted_data.csv", "text/csv")
            st.success("✅ Conversion completed!")
        except Exception as e:
            st.error(f"Conversion error: {str(e)}")


def json_converter():
    """Convert and format JSON data"""
    create_tool_header("JSON Converter", "Format, validate, and convert JSON data", "📋")

    uploaded_file = FileHandler.upload_files(['json'], accept_multiple=False)

    if uploaded_file:
        json_text = FileHandler.process_text_file(uploaded_file[0])
        st.text_area("Uploaded JSON:", json_text[:500] + "..." if len(json_text) > 500 else json_text, height=150,
                     disabled=True)
    else:
        json_text = st.text_area("Enter JSON data:", height=200,
                                 placeholder='{"name": "John", "age": 30, "city": "New York"}')

    if json_text:
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Validate JSON"):
                validate_json(json_text)

        with col2:
            if st.button("Format JSON"):
                format_json(json_text)

        with col3:
            if st.button("Minify JSON"):
                minify_json(json_text)


def validate_json(json_text):
    """Validate JSON format"""
    try:
        data = json.loads(json_text)
        st.success("✅ Valid JSON!")

        # Show structure info
        if isinstance(data, dict):
            st.info(f"Object with {len(data)} keys")
        elif isinstance(data, list):
            st.info(f"Array with {len(data)} items")
        else:
            st.info(f"Simple value: {type(data).__name__}")

    except json.JSONDecodeError as e:
        st.error(f"❌ Invalid JSON: {str(e)}")


def format_json(json_text):
    """Format JSON with indentation"""
    try:
        data = json.loads(json_text)
        formatted = json.dumps(data, indent=2, ensure_ascii=False)
        st.code(formatted, language='json')
        FileHandler.create_download_link(formatted.encode(), "formatted.json", "application/json")
    except json.JSONDecodeError as e:
        st.error(f"❌ Invalid JSON: {str(e)}")


def minify_json(json_text):
    """Minify JSON by removing whitespace"""
    try:
        data = json.loads(json_text)
        minified = json.dumps(data, separators=(',', ':'))
        st.code(minified)
        FileHandler.create_download_link(minified.encode(), "minified.json", "application/json")
    except json.JSONDecodeError as e:
        st.error(f"❌ Invalid JSON: {str(e)}")


def statistical_summary():
    """Generate statistical summary of data"""
    create_tool_header("Statistical Summary", "Generate comprehensive statistical analysis", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            if st.button("Generate Summary"):
                generate_summary(df)


def generate_summary(df):
    """Generate enhanced statistical summary with automated insights"""
    st.markdown("### 📊 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Rows", len(df))
    with col2:
        st.metric("Columns", len(df.columns))
    with col3:
        missing_pct = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
        st.metric("Missing %", f"{missing_pct:.1f}%")
    with col4:
        memory_usage = df.memory_usage(deep=True).sum() / 1024 ** 2
        st.metric("Memory (MB)", f"{memory_usage:.1f}")

    # Enhanced Data Quality Score
    data_quality_score = calculate_data_quality_score(df)

    # Auto-generated insights
    insights = generate_automated_insights(df)

    # Data types with enhanced info
    st.markdown("### 📋 Enhanced Column Information")
    info_df = create_enhanced_column_info(df)
    st.dataframe(info_df)

    # Data Quality Assessment
    st.markdown("### 🎯 Data Quality Assessment")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Quality Score", f"{data_quality_score:.1f}/100",
                  delta=None if data_quality_score >= 80 else "Needs Improvement")
    with col2:
        completeness = ((len(df) * len(df.columns) - df.isnull().sum().sum()) / (len(df) * len(df.columns))) * 100
        st.metric("Completeness", f"{completeness:.1f}%")

    # Automated Insights
    if insights:
        st.markdown("### 🔍 Automated Insights")
        for insight in insights:
            if insight['type'] == 'warning':
                st.warning(f"⚠️ {insight['message']}")
            elif insight['type'] == 'info':
                st.info(f"ℹ️ {insight['message']}")
            elif insight['type'] == 'success':
                st.success(f"✅ {insight['message']}")

    # Enhanced Numerical Analysis
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        st.markdown("### 📊 Enhanced Numerical Analysis")

        # Standard descriptive stats
        desc_stats = df[numeric_cols].describe()
        st.dataframe(desc_stats)

        # Additional statistical measures
        enhanced_stats = calculate_enhanced_statistics(df, numeric_cols)
        st.dataframe(enhanced_stats)

        # Distribution analysis
        st.markdown("### 📈 Distribution Analysis")
        show_distribution_analysis(df, numeric_cols)

    # Enhanced Categorical Analysis
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        st.markdown("### 📝 Enhanced Categorical Analysis")
        show_enhanced_categorical_analysis(df, categorical_cols)

    # Outlier Detection
    if len(numeric_cols) > 0:
        st.markdown("### 🎯 Outlier Detection & Recommendations")
        outlier_analysis = detect_outliers_advanced(df, numeric_cols)
        display_outlier_analysis(outlier_analysis)

    # Correlation insights
    if len(numeric_cols) > 1:
        st.markdown("### 🔗 Quick Correlation Insights")
        show_correlation_insights(df, numeric_cols)


def calculate_data_quality_score(df):
    """Calculate a comprehensive data quality score (0-100)"""
    score = 100

    # Completeness (40% weight)
    missing_pct = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    completeness_score = max(0, 100 - missing_pct * 2)
    score = score * 0.4 + completeness_score * 0.4

    # Consistency (30% weight) - check for data type issues
    consistency_score = 100
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                pd.to_numeric(df[col], errors='raise')
                consistency_score -= 10  # Penalty for mixed types
            except:
                pass

    score = score * 0.7 + consistency_score * 0.3

    # Uniqueness (20% weight) - check for duplicates
    duplicates_pct = (df.duplicated().sum() / len(df)) * 100
    uniqueness_score = max(0, 100 - duplicates_pct * 5)
    score = score * 0.8 + uniqueness_score * 0.2

    # Validity (10% weight) - basic checks
    validity_score = 100
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if (df[col] < 0).any() and col.lower() in ['age', 'count', 'quantity', 'amount']:
            validity_score -= 5  # Penalty for negative values where they shouldn't be

    score = score * 0.9 + validity_score * 0.1

    return max(0, min(100, score))


def generate_automated_insights(df):
    """Generate automated insights about the dataset"""
    insights = []

    # Dataset size insights
    if len(df) < 100:
        insights.append({
            'type': 'warning',
            'message': f"Small dataset ({len(df)} rows) - statistical analysis may be limited"
        })
    elif len(df) > 100000:
        insights.append({
            'type': 'info',
            'message': f"Large dataset ({len(df):,} rows) - consider sampling for faster analysis"
        })

    # Missing data insights
    missing_pct = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    if missing_pct > 20:
        insights.append({
            'type': 'warning',
            'message': f"High missing data rate ({missing_pct:.1f}%) - consider data imputation strategies"
        })
    elif missing_pct == 0:
        insights.append({
            'type': 'success',
            'message': "Complete dataset with no missing values - excellent data quality!"
        })

    # Duplicate insights
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        dup_pct = (duplicates / len(df)) * 100
        insights.append({
            'type': 'warning',
            'message': f"Found {duplicates} duplicate rows ({dup_pct:.1f}%) - consider deduplication"
        })

    # Column insights
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    if len(numeric_cols) == 0:
        insights.append({
            'type': 'info',
            'message': "No numeric columns detected - limited statistical analysis available"
        })

    if len(categorical_cols) > len(numeric_cols) * 2:
        insights.append({
            'type': 'info',
            'message': "Dataset is primarily categorical - consider encoding for ML applications"
        })

    # High cardinality insights
    for col in categorical_cols:
        unique_pct = (df[col].nunique() / len(df)) * 100
        if unique_pct > 80:
            insights.append({
                'type': 'warning',
                'message': f"Column '{col}' has very high cardinality ({unique_pct:.1f}%) - may need aggregation"
            })

    return insights


def create_enhanced_column_info(df):
    """Create enhanced column information with additional metrics"""
    info_data = []

    for col in df.columns:
        col_data = df[col]
        info = {
            'Column': col,
            'Data Type': str(col_data.dtype),
            'Non-Null Count': col_data.count(),
            'Null Count': col_data.isnull().sum(),
            'Null %': (col_data.isnull().sum() / len(df)) * 100,
            'Unique Values': col_data.nunique(),
            'Unique %': (col_data.nunique() / len(df)) * 100
        }

        # Add type-specific metrics
        if pd.api.types.is_numeric_dtype(col_data):
            info['Min'] = col_data.min()
            info['Max'] = col_data.max()
            info['Mean'] = col_data.mean()
            info['Std'] = col_data.std()
        else:
            most_common = col_data.mode()
            info['Most Common'] = most_common.iloc[0] if len(most_common) > 0 else 'N/A'
            info['Mode Frequency'] = (col_data == info['Most Common']).sum() if info['Most Common'] != 'N/A' else 0

        info_data.append(info)

    return pd.DataFrame(info_data).round(2)


def calculate_enhanced_statistics(df, numeric_cols):
    """Calculate additional statistical measures beyond basic describe()"""
    stats_data = []

    for col in numeric_cols:
        data = df[col].dropna()
        if len(data) > 0:
            from scipy import stats

            # Basic stats
            stats_info = {
                'Column': col,
                'Skewness': stats.skew(data),
                'Kurtosis': stats.kurtosis(data),
                'Variance': data.var(),
                'CV (%)': (data.std() / data.mean()) * 100 if data.mean() != 0 else 0,
                'IQR': data.quantile(0.75) - data.quantile(0.25),
                'Outliers (IQR)': ((data < (data.quantile(0.25) - 1.5 * (data.quantile(0.75) - data.quantile(0.25)))) |
                                   (data > (data.quantile(0.75) + 1.5 * (
                                               data.quantile(0.75) - data.quantile(0.25))))).sum()
            }

            # Normality test (if sample size is appropriate)
            if 8 <= len(data) <= 5000:
                try:
                    _, p_value = stats.normaltest(data)
                    stats_info['Normality p-value'] = p_value
                    stats_info['Likely Normal'] = 'Yes' if p_value > 0.05 else 'No'
                except:
                    stats_info['Normality p-value'] = 'N/A'
                    stats_info['Likely Normal'] = 'N/A'
            else:
                stats_info['Normality p-value'] = 'N/A (sample size)'
                stats_info['Likely Normal'] = 'N/A'

            stats_data.append(stats_info)

    return pd.DataFrame(stats_data).round(4)


def show_distribution_analysis(df, numeric_cols):
    """Show distribution analysis for numeric columns"""
    if len(numeric_cols) > 6:
        selected_cols = st.multiselect(
            "Select columns for distribution analysis:",
            numeric_cols,
            default=list(numeric_cols[:4])
        )
    else:
        selected_cols = numeric_cols

    if selected_cols:
        # Create subplots
        n_cols = min(2, len(selected_cols))
        n_rows = (len(selected_cols) + n_cols - 1) // n_cols

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 4 * n_rows))
        if n_rows == 1 and n_cols == 1:
            axes = [axes]
        elif n_rows == 1:
            axes = axes
        else:
            axes = axes.flatten()

        for i, col in enumerate(selected_cols):
            if i < len(axes):
                data = df[col].dropna()
                axes[i].hist(data, bins=30, alpha=0.7, edgecolor='black')
                axes[i].set_title(f'Distribution: {col}')
                axes[i].set_xlabel(col)
                axes[i].set_ylabel('Frequency')

                # Add normal distribution overlay if data looks normal
                try:
                    from scipy import stats
                    if len(data) > 0:
                        mu, sigma = data.mean(), data.std()
                        x = np.linspace(data.min(), data.max(), 100)
                        normal_curve = stats.norm.pdf(x, mu, sigma) * len(data) * (data.max() - data.min()) / 30
                        axes[i].plot(x, normal_curve, 'r-', alpha=0.8, label='Normal fit')
                        axes[i].legend()
                except:
                    pass

        # Hide empty subplots
        for i in range(len(selected_cols), len(axes)):
            axes[i].set_visible(False)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


def show_enhanced_categorical_analysis(df, categorical_cols):
    """Show enhanced analysis for categorical columns"""
    for col in categorical_cols[:3]:  # Show first 3 categorical columns
        st.write(f"**{col}**")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Unique Values", df[col].nunique())
        with col2:
            cardinality_pct = (df[col].nunique() / len(df)) * 100
            st.metric("Cardinality %", f"{cardinality_pct:.1f}%")
        with col3:
            most_common = df[col].mode()
            if len(most_common) > 0:
                mode_freq = (df[col] == most_common.iloc[0]).sum()
                mode_pct = (mode_freq / len(df)) * 100
                st.metric("Mode Frequency", f"{mode_pct:.1f}%")

        # Show value distribution
        if df[col].nunique() <= 20:  # Only show for reasonable number of categories
            value_counts = df[col].value_counts().head(10)
            st.bar_chart(value_counts)
        else:
            st.info(f"Too many unique values ({df[col].nunique()}) to display distribution chart")


def detect_outliers_advanced(df, numeric_cols):
    """Detect outliers using multiple methods"""
    outlier_results = {}

    for col in numeric_cols:
        data = df[col].dropna()
        if len(data) > 0:
            results = {
                'column': col,
                'total_values': len(data),
                'outliers_iqr': 0,
                'outliers_zscore': 0,
                'outliers_modified_zscore': 0,
                'recommendations': []
            }

            # IQR Method
            Q1, Q3 = data.quantile(0.25), data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers_iqr = ((data < lower_bound) | (data > upper_bound)).sum()
            results['outliers_iqr'] = outliers_iqr

            # Z-Score Method
            if data.std() > 0:
                z_scores = np.abs((data - data.mean()) / data.std())
                outliers_zscore = (z_scores > 3).sum()
                results['outliers_zscore'] = outliers_zscore

            # Modified Z-Score Method
            try:
                median = data.median()
                mad = np.median(np.abs(data - median))
                if mad > 0:
                    modified_z_scores = 0.6745 * (data - median) / mad
                    outliers_modified_zscore = (np.abs(modified_z_scores) > 3.5).sum()
                    results['outliers_modified_zscore'] = outliers_modified_zscore
            except:
                pass

            # Generate recommendations
            outlier_pct = (outliers_iqr / len(data)) * 100
            if outlier_pct > 10:
                results['recommendations'].append("High outlier rate - investigate data collection process")
            elif outlier_pct > 5:
                results['recommendations'].append("Moderate outliers - consider robust statistical methods")
            elif outlier_pct > 0:
                results['recommendations'].append("Few outliers detected - investigate individual cases")
            else:
                results['recommendations'].append("No significant outliers detected")

            outlier_results[col] = results

    return outlier_results


def display_outlier_analysis(outlier_analysis):
    """Display outlier analysis results"""
    if not outlier_analysis:
        st.info("No numeric columns available for outlier analysis")
        return

    # Summary table
    summary_data = []
    for col, results in outlier_analysis.items():
        summary_data.append({
            'Column': col,
            'Total Values': results['total_values'],
            'IQR Outliers': results['outliers_iqr'],
            'Z-Score Outliers': results['outliers_zscore'],
            'Modified Z-Score Outliers': results['outliers_modified_zscore'],
            'Outlier Rate %': f"{(results['outliers_iqr'] / results['total_values']) * 100:.1f}%"
        })

    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df)

    # Recommendations
    st.markdown("#### 🎯 Recommendations")
    for col, results in outlier_analysis.items():
        for recommendation in results['recommendations']:
            st.write(f"**{col}:** {recommendation}")


def show_correlation_insights(df, numeric_cols):
    """Show quick correlation insights"""
    if len(numeric_cols) < 2:
        return

    corr_matrix = df[numeric_cols].corr()

    # Find strongest correlations
    strong_correlations = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i + 1, len(corr_matrix.columns)):
            corr_value = corr_matrix.iloc[i, j]
            if abs(corr_value) > 0.5:  # Moderate to strong correlation
                strong_correlations.append({
                    'Variable 1': corr_matrix.columns[i],
                    'Variable 2': corr_matrix.columns[j],
                    'Correlation': corr_value,
                    'Strength': 'Strong' if abs(corr_value) > 0.7 else 'Moderate'
                })

    if strong_correlations:
        strong_corr_df = pd.DataFrame(strong_correlations)
        strong_corr_df['Correlation'] = strong_corr_df['Correlation'].round(3)
        st.dataframe(strong_corr_df)

        # Insights
        positive_strong = len([c for c in strong_correlations if c['Correlation'] > 0.7])
        negative_strong = len([c for c in strong_correlations if c['Correlation'] < -0.7])

        if positive_strong > 0:
            st.info(f"Found {positive_strong} strong positive correlations - variables tend to increase together")
        if negative_strong > 0:
            st.info(
                f"Found {negative_strong} strong negative correlations - variables tend to move in opposite directions")
    else:
        st.info("No strong correlations (|r| > 0.5) found between numeric variables")


def chart_generator():
    """Generate various charts from data"""
    create_tool_header("Chart Generator", "Create beautiful charts from your data", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            chart_type = st.selectbox("Chart Type:", [
                "Line Chart", "Bar Chart", "Histogram", "Scatter Plot", "Box Plot", "Heatmap"
            ])

            if chart_type in ["Line Chart", "Bar Chart"]:
                x_col = st.selectbox("X-axis column:", df.columns)
                y_col = st.selectbox("Y-axis column:", df.select_dtypes(include=[np.number]).columns)

                if st.button("Generate Chart"):
                    create_chart(df, chart_type, x_col, y_col)

            elif chart_type == "Histogram":
                col = st.selectbox("Column:", df.select_dtypes(include=[np.number]).columns)
                if st.button("Generate Chart"):
                    create_histogram(df, col)

            elif chart_type == "Scatter Plot":
                x_col = st.selectbox("X-axis:", df.select_dtypes(include=[np.number]).columns)
                y_col = st.selectbox("Y-axis:", df.select_dtypes(include=[np.number]).columns)
                if st.button("Generate Chart"):
                    create_scatter_plot(df, x_col, y_col)


def create_chart(df, chart_type, x_col, y_col):
    """Create line or bar chart"""
    plt.figure(figsize=(10, 6))

    if chart_type == "Line Chart":
        plt.plot(df[x_col], df[y_col])
        plt.title(f"Line Chart: {y_col} vs {x_col}")
    else:  # Bar Chart
        plt.bar(df[x_col], df[y_col])
        plt.title(f"Bar Chart: {y_col} vs {x_col}")

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot()
    plt.close()


def create_histogram(df, col):
    """Create histogram"""
    plt.figure(figsize=(10, 6))
    plt.hist(df[col], bins=30, alpha=0.7)
    plt.title(f"Histogram: {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()

    st.pyplot()
    plt.close()


def create_scatter_plot(df, x_col, y_col):
    """Create scatter plot"""
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], alpha=0.6)
    plt.title(f"Scatter Plot: {y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()

    st.pyplot()
    plt.close()


def missing_value_handler():
    """Handle missing values in dataset"""
    create_tool_header("Missing Value Handler", "Detect and handle missing values", "🔍")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Show missing values
            missing_stats = show_missing_values(df)

            if missing_stats['total_missing'] > 0:
                handle_missing_values(df)
            else:
                st.success("✅ No missing values found in the dataset!")


def show_missing_values(df):
    """Show missing value statistics"""
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    missing_df = pd.DataFrame({
        'Column': df.columns,
        'Missing Count': missing_count,
        'Missing Percentage': missing_percent.round(2)
    })

    missing_df = missing_df[missing_df['Missing Count'] > 0]
    if len(missing_df) > 0:
        missing_df = missing_df.sort_values(by='Missing Count', ascending=False)

    if len(missing_df) > 0:
        st.markdown("### 🚨 Missing Values Summary")
        st.dataframe(missing_df)

        # Visualize missing values
        if len(missing_df) > 0:
            st.bar_chart(missing_df.set_index('Column')['Missing Count'])

    return {'total_missing': missing_count.sum(), 'columns_with_missing': len(missing_df)}


def handle_missing_values(df):
    """Provide options to handle missing values"""
    st.markdown("### 🔧 Handle Missing Values")

    strategy = st.selectbox("Choose strategy:", [
        "Remove rows with missing values",
        "Remove columns with missing values",
        "Fill with mean (numeric only)",
        "Fill with median (numeric only)",
        "Fill with mode",
        "Forward fill",
        "Backward fill"
    ])

    if st.button("Apply Strategy"):
        try:
            cleaned_df = None
            if strategy == "Remove rows with missing values":
                cleaned_df = df.dropna()
            elif strategy == "Remove columns with missing values":
                cleaned_df = df.dropna(axis=1)
            elif strategy == "Fill with mean (numeric only)":
                cleaned_df = df.copy()
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(cleaned_df[numeric_cols].mean())
            elif strategy == "Fill with median (numeric only)":
                cleaned_df = df.copy()
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(cleaned_df[numeric_cols].median())
            elif strategy == "Fill with mode":
                cleaned_df = df.fillna(df.mode().iloc[0])
            elif strategy == "Forward fill":
                cleaned_df = df.fillna(method='ffill')
            elif strategy == "Backward fill":
                cleaned_df = df.fillna(method='bfill')

            if cleaned_df is not None:
                st.success(f"✅ Strategy applied! Rows before: {len(df)}, Rows after: {len(cleaned_df)}")
                st.dataframe(cleaned_df.head())

                # Download cleaned data
                csv_data = cleaned_df.to_csv(index=False)
                FileHandler.create_download_link(csv_data.encode(), "cleaned_data.csv", "text/csv")
            else:
                st.error("Unknown strategy selected")

        except Exception as e:
            st.error(f"Error applying strategy: {str(e)}")


def correlation_analysis():
    """Analyze correlations between variables"""
    create_tool_header("Correlation Analysis", "Analyze relationships between variables", "🔗")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            numeric_df = df.select_dtypes(include=[np.number])

            if len(numeric_df.columns) < 2:
                st.error("Need at least 2 numeric columns for correlation analysis")
                return

            st.dataframe(numeric_df.head())

            if st.button("Calculate Correlations"):
                calculate_correlations(numeric_df)


def calculate_correlations(df):
    """Calculate and display correlations"""
    corr_matrix = df.corr()

    st.markdown("### 📊 Correlation Matrix")
    st.dataframe(corr_matrix)

    # Heatmap
    st.markdown("### 🔥 Correlation Heatmap")
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    st.pyplot()
    plt.close()

    # Strong correlations
    st.markdown("### 🔍 Strong Correlations")
    strong_corr = []

    for i in range(len(corr_matrix.columns)):
        for j in range(i + 1, len(corr_matrix.columns)):
            corr_value = corr_matrix.iloc[i, j]
            if abs(corr_value) > 0.7:  # Strong correlation threshold
                strong_corr.append({
                    'Variable 1': corr_matrix.columns[i],
                    'Variable 2': corr_matrix.columns[j],
                    'Correlation': round(corr_value, 3)
                })

    if strong_corr:
        strong_corr_df = pd.DataFrame(strong_corr)
        st.dataframe(strong_corr_df)
    else:
        st.info("No strong correlations (|r| > 0.7) found")


def data_validator():
    """Validate data quality"""
    create_tool_header("Data Validator", "Validate data quality and identify issues", "✅")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            if st.button("Validate Data"):
                validate_data_quality(df)


def validate_data_quality(df):
    """Perform comprehensive data validation"""
    st.markdown("### 📋 Data Quality Report")

    # Basic statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        duplicate_rows = df.duplicated().sum()
        st.metric("Duplicate Rows", duplicate_rows)

    # Missing values
    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        st.warning(f"⚠️ Found {missing_values} missing values")
    else:
        st.success("✅ No missing values found")

    # Data type issues
    st.markdown("### 🔍 Potential Data Type Issues")
    for col in df.columns:
        if df[col].dtype == 'object':
            # Check if numeric values are stored as text
            try:
                pd.to_numeric(df[col], errors='raise')
                st.warning(f"⚠️ Column '{col}' contains numeric data but is stored as text")
            except:
                # Check for mixed types
                sample = df[col].dropna().head(100)
                if len(sample) > 0:
                    numeric_count = sum(1 for x in sample if str(x).replace('.', '').replace('-', '').isdigit())
                    if 0 < numeric_count < len(sample):
                        st.warning(f"⚠️ Column '{col}' has mixed data types")

    # Outlier detection for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        st.markdown("### 📊 Outlier Detection")
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()

            if outliers > 0:
                st.write(f"**{col}:** {outliers} potential outliers found")


def pivot_table_creator():
    """Create pivot tables from data"""
    create_tool_header("Pivot Table Creator", "Create interactive pivot tables", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            create_pivot_table(df)


def create_pivot_table(df):
    """Create pivot table interface"""
    st.markdown("### ⚙️ Pivot Table Configuration")

    col1, col2 = st.columns(2)

    with col1:
        index_cols = st.multiselect("Row Labels (Index):", df.columns)
        values_cols = st.multiselect("Values:", df.select_dtypes(include=[np.number]).columns)

    with col2:
        column_cols = st.multiselect("Column Labels:", df.columns)
        aggfunc = st.selectbox("Aggregation Function:", ["sum", "mean", "count", "min", "max"])

    if index_cols and values_cols and st.button("Create Pivot Table"):
        try:
            pivot_kwargs = {
                'data': df,
                'index': index_cols,
                'values': values_cols,
                'aggfunc': aggfunc
            }

            if column_cols:
                pivot_kwargs['columns'] = column_cols

            pivot_table = pd.pivot_table(**pivot_kwargs)

            st.markdown("### 📊 Pivot Table Results")
            st.dataframe(pivot_table)

            # Download option
            csv_data = pivot_table.to_csv()
            FileHandler.create_download_link(csv_data.encode(), "pivot_table.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating pivot table: {str(e)}")


def linear_regression():
    """Perform linear regression analysis"""
    create_tool_header("Linear Regression", "Perform linear regression analysis", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            numeric_cols = df.select_dtypes(include=[np.number]).columns

            if len(numeric_cols) < 2:
                st.error("Need at least 2 numeric columns for linear regression")
                return

            st.dataframe(df.head())

            perform_linear_regression(df, numeric_cols)


def perform_linear_regression(df, numeric_cols):
    """Perform linear regression analysis"""
    col1, col2 = st.columns(2)

    with col1:
        x_col = st.selectbox("Independent Variable (X):", numeric_cols)
    with col2:
        y_col = st.selectbox("Dependent Variable (Y):", numeric_cols)

    if x_col != y_col and st.button("Run Regression"):
        try:
            from sklearn.linear_model import LinearRegression
            from sklearn.metrics import r2_score

            # Prepare data
            X = df[[x_col]].dropna()
            y = df[y_col].dropna()

            # Align the data
            common_index = X.index.intersection(y.index)
            X = X.loc[common_index]
            y = y.loc[common_index]

            # Fit model
            model = LinearRegression()
            model.fit(X, y)

            # Predictions
            y_pred = model.predict(X)

            # Results
            st.markdown("### 📊 Regression Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("R-squared", f"{r2_score(y, y_pred):.4f}")
            with col2:
                st.metric("Slope", f"{model.coef_[0]:.4f}")
            with col3:
                st.metric("Intercept", f"{model.intercept_:.4f}")

            # Equation
            st.markdown(f"### 📝 Regression Equation")
            st.latex(f"y = {model.coef_[0]:.4f}x + {model.intercept_:.4f}")

            # Plot
            st.markdown("### 📈 Regression Plot")
            plt.figure(figsize=(10, 6))
            plt.scatter(X, y, alpha=0.6, label='Data points')
            plt.plot(X, y_pred, color='red', linewidth=2, label='Regression line')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f"Linear Regression: {y_col} vs {x_col}")
            plt.legend()
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

        except Exception as e:
            st.error(f"Error in regression analysis: {str(e)}")


def advanced_regression():
    """Perform advanced regression analysis with multiple algorithms"""
    create_tool_header("Advanced Regression", "Advanced regression models with feature analysis", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(numeric_cols) < 2:
                st.error("Need at least 2 numeric columns for regression analysis")
                return

            st.dataframe(df.head())

            # Model selection
            regression_type = st.selectbox("Regression Type:", [
                "Multiple Linear Regression", "Polynomial Regression",
                "Ridge Regression", "Lasso Regression", "ElasticNet Regression"
            ])

            # Feature and target selection
            col1, col2 = st.columns(2)
            with col1:
                feature_cols = st.multiselect("Feature Variables (X):", numeric_cols,
                                              default=numeric_cols[:-1] if len(numeric_cols) > 1 else [])
            with col2:
                target_col = st.selectbox("Target Variable (Y):", numeric_cols)

            if feature_cols and target_col not in feature_cols:
                perform_advanced_regression(df, feature_cols, target_col, regression_type)


def perform_advanced_regression(df, feature_cols, target_col, regression_type):
    """Perform advanced regression analysis"""
    if st.button("Run Advanced Regression"):
        try:
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import StandardScaler, PolynomialFeatures
            from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
            from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
            from sklearn.pipeline import Pipeline
            import numpy as np

            # Prepare data
            X = df[feature_cols].dropna()
            y = df[target_col].dropna()

            # Align data
            common_index = X.index.intersection(y.index)
            X = X.loc[common_index]
            y = y.loc[common_index]

            if len(X) < 10:
                st.error("Need at least 10 samples for reliable regression analysis")
                return

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Initialize variables
            model = None
            X_train_scaled = X_train
            X_test_scaled = X_test

            # Create model based on type
            if regression_type == "Multiple Linear Regression":
                model = LinearRegression()
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)

            elif regression_type == "Polynomial Regression":
                degree = st.slider("Polynomial Degree:", 2, 5, 2)
                model = Pipeline([
                    ('scaler', StandardScaler()),
                    ('poly', PolynomialFeatures(degree=degree)),
                    ('regressor', LinearRegression())
                ])
                X_train_scaled = X_train
                X_test_scaled = X_test

            elif regression_type == "Ridge Regression":
                alpha = st.slider("Alpha (Regularization):", 0.1, 10.0, 1.0, 0.1)
                model = Ridge(alpha=alpha)
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)

            elif regression_type == "Lasso Regression":
                alpha = st.slider("Alpha (Regularization):", 0.1, 10.0, 1.0, 0.1)
                model = Lasso(alpha=alpha)
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)

            elif regression_type == "ElasticNet Regression":
                alpha = st.slider("Alpha (Regularization):", 0.1, 10.0, 1.0, 0.1)
                l1_ratio = st.slider("L1 Ratio:", 0.1, 0.9, 0.5, 0.1)
                model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
            else:
                st.error("Invalid regression type selected")
                return

            # Fit model
            if regression_type == "Polynomial Regression":
                model.fit(X_train_scaled, y_train)
                y_pred_train = model.predict(X_train_scaled)
                y_pred_test = model.predict(X_test_scaled)
            else:
                model.fit(X_train_scaled, y_train)
                y_pred_train = model.predict(X_train_scaled)
                y_pred_test = model.predict(X_test_scaled)

            # Calculate metrics
            train_r2 = r2_score(y_train, y_pred_train)
            test_r2 = r2_score(y_test, y_pred_test)
            train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
            test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
            train_mae = mean_absolute_error(y_train, y_pred_train)
            test_mae = mean_absolute_error(y_test, y_pred_test)

            # Display results
            st.markdown("### 📊 Model Performance")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Training Set:**")
                st.metric("R² Score", f"{train_r2:.4f}")
                st.metric("RMSE", f"{train_rmse:.4f}")
                st.metric("MAE", f"{train_mae:.4f}")

            with col2:
                st.markdown("**Test Set:**")
                st.metric("R² Score", f"{test_r2:.4f}")
                st.metric("RMSE", f"{test_rmse:.4f}")
                st.metric("MAE", f"{test_mae:.4f}")

            # Model interpretation
            st.markdown("### 🔍 Model Analysis")

            # Feature importance (for linear models)
            if regression_type in ["Multiple Linear Regression", "Ridge Regression", "Lasso Regression",
                                   "ElasticNet Regression"]:
                # Get coefficients from model or pipeline
                coef_values = None
                if hasattr(model, 'coef_'):
                    coef_values = model.coef_
                elif hasattr(model, 'named_steps'):
                    regressor_step = model.named_steps.get('regressor')
                    if regressor_step and hasattr(regressor_step, 'coef_'):
                        coef_values = regressor_step.coef_

                if coef_values is not None:
                    feature_importance = pd.DataFrame({
                        'Feature': feature_cols,
                        'Coefficient': coef_values,
                        'Abs_Coefficient': np.abs(coef_values)
                    }).sort_values('Abs_Coefficient', ascending=False)

                    st.dataframe(feature_importance)

                    # Feature importance plot
                    plt.figure(figsize=(10, 6))
                    plt.barh(feature_importance['Feature'], feature_importance['Coefficient'])
                    plt.xlabel('Coefficient Value')
                    plt.title('Feature Importance (Coefficients)')
                    plt.tight_layout()
                    st.pyplot()
                    plt.close()

            # Prediction vs Actual plot
            st.markdown("### 📈 Prediction vs Actual")
            plt.figure(figsize=(12, 5))

            plt.subplot(1, 2, 1)
            plt.scatter(y_train, y_pred_train, alpha=0.6)
            y_train_array = np.array(y_train)
            y_min, y_max = float(y_train_array.min()), float(y_train_array.max())
            plt.plot([y_min, y_max], [y_min, y_max], 'r--', lw=2)
            plt.xlabel('Actual')
            plt.ylabel('Predicted')
            plt.title(f'Training Set (R² = {train_r2:.3f})')

            plt.subplot(1, 2, 2)
            plt.scatter(y_test, y_pred_test, alpha=0.6)
            y_test_array = np.array(y_test)
            y_min, y_max = float(y_test_array.min()), float(y_test_array.max())
            plt.plot([y_min, y_max], [y_min, y_max], 'r--', lw=2)
            plt.xlabel('Actual')
            plt.ylabel('Predicted')
            plt.title(f'Test Set (R² = {test_r2:.3f})')

            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Model recommendations
            st.markdown("### 💡 Model Recommendations")
            if test_r2 < 0.5:
                st.warning("⚠️ Low R² score - consider feature engineering or different algorithms")
            elif test_r2 > 0.8:
                st.success("✅ Good model performance")

            if abs(float(train_r2) - float(test_r2)) > 0.2:
                st.warning("⚠️ Large performance gap between training and test - possible overfitting")

            if regression_type == "Lasso Regression":
                # Get coefficients for Lasso analysis
                coef_values = None
                if hasattr(model, 'coef_'):
                    coef_values = model.coef_
                elif hasattr(model, 'named_steps'):
                    regressor_step = model.named_steps.get('regressor')
                    if regressor_step and hasattr(regressor_step, 'coef_'):
                        coef_values = regressor_step.coef_

                if coef_values is not None:
                    zero_coefs = np.sum(np.abs(coef_values) < 1e-10)
                    if zero_coefs > 0:
                        st.info(
                            f"ℹ️ Lasso regression eliminated {zero_coefs} features - automatic feature selection performed")

        except Exception as e:
            st.error(f"Error in advanced regression: {str(e)}")


def classification_models():
    """Perform classification analysis"""
    create_tool_header("Classification Models", "Advanced classification algorithms", "🎯")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

            if len(numeric_cols) < 1 or len(categorical_cols) < 1:
                st.error("Need at least 1 numeric column (features) and 1 categorical column (target)")
                return

            # Model and feature selection
            classifier_type = st.selectbox("Classification Algorithm:", [
                "Logistic Regression", "Random Forest", "Support Vector Machine",
                "Gradient Boosting", "Decision Tree"
            ])

            col1, col2 = st.columns(2)
            with col1:
                feature_cols = st.multiselect("Feature Variables:", numeric_cols,
                                              default=numeric_cols[:5] if len(numeric_cols) >= 5 else numeric_cols)
            with col2:
                target_col = st.selectbox("Target Variable:", categorical_cols)

            if feature_cols and target_col:
                perform_classification(df, feature_cols, target_col, classifier_type)


def perform_classification(df, feature_cols, target_col, classifier_type):
    """Perform classification analysis"""
    if st.button("Run Classification"):
        try:
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import StandardScaler, LabelEncoder
            from sklearn.linear_model import LogisticRegression
            from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
            from sklearn.svm import SVC
            from sklearn.tree import DecisionTreeClassifier
            from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
            from sklearn.metrics import precision_score, recall_score, f1_score
            import seaborn as sns

            # Prepare data
            X = df[feature_cols].dropna()
            y = df[target_col].dropna()

            # Align data
            common_index = X.index.intersection(y.index)
            X = X.loc[common_index]
            y = y.loc[common_index]

            # Encode target variable
            le = LabelEncoder()
            y_encoded = le.fit_transform(y)

            # Check for class balance
            unique_classes, class_counts = np.unique(y_encoded, return_counts=True)
            class_balance = dict(zip(le.classes_, class_counts))

            st.markdown("### 📊 Class Distribution")
            st.bar_chart(pd.Series(class_balance))

            if len(unique_classes) < 2:
                st.error("Need at least 2 classes for classification")
                return

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2,
                                                                random_state=42, stratify=y_encoded)

            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Initialize model
            model = None

            # Create model
            if classifier_type == "Logistic Regression":
                model = LogisticRegression(random_state=42, max_iter=1000)
            elif classifier_type == "Random Forest":
                n_estimators = st.slider("Number of Trees:", 10, 200, 100, 10)
                model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
            elif classifier_type == "Support Vector Machine":
                kernel = st.selectbox("Kernel:", ['rbf', 'linear', 'poly'])
                model = SVC(kernel=kernel, random_state=42, probability=True)
            elif classifier_type == "Gradient Boosting":
                n_estimators = st.slider("Number of Boosting Stages:", 50, 300, 100, 25)
                model = GradientBoostingClassifier(n_estimators=n_estimators, random_state=42)
            elif classifier_type == "Decision Tree":
                max_depth = st.slider("Max Depth:", 3, 20, 5)
                model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
            else:
                st.error("Invalid classification algorithm selected")
                return

            if model is None:
                st.error("Model initialization failed")
                return

            # Fit model
            if classifier_type == "Support Vector Machine":
                model.fit(X_train_scaled, y_train)
                y_pred_train = model.predict(X_train_scaled)
                y_pred_test = model.predict(X_test_scaled)
                y_pred_proba = model.predict_proba(X_test_scaled)
            else:
                model.fit(X_train, y_train)
                y_pred_train = model.predict(X_train)
                y_pred_test = model.predict(X_test)
                y_pred_proba = model.predict_proba(X_test)

            # Calculate metrics
            train_accuracy = accuracy_score(y_train, y_pred_train)
            test_accuracy = accuracy_score(y_test, y_pred_test)

            # Multi-class metrics
            avg_method = 'weighted' if len(unique_classes) > 2 else 'binary'
            test_precision = precision_score(y_test, y_pred_test, average=avg_method)
            test_recall = recall_score(y_test, y_pred_test, average=avg_method)
            test_f1 = f1_score(y_test, y_pred_test, average=avg_method)

            # Display results
            st.markdown("### 📊 Model Performance")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Test Accuracy", f"{test_accuracy:.3f}")
            with col2:
                st.metric("Precision", f"{test_precision:.3f}")
            with col3:
                st.metric("Recall", f"{test_recall:.3f}")
            with col4:
                st.metric("F1-Score", f"{test_f1:.3f}")

            # Confusion Matrix
            st.markdown("### 🔥 Confusion Matrix")
            cm = confusion_matrix(y_test, y_pred_test)

            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                        xticklabels=le.classes_, yticklabels=le.classes_)
            plt.xlabel('Predicted')
            plt.ylabel('Actual')
            plt.title('Confusion Matrix')
            st.pyplot()
            plt.close()

            # Feature importance
            if hasattr(model, 'feature_importances_'):
                st.markdown("### 🎯 Feature Importance")
                feature_importance = pd.DataFrame({
                    'Feature': feature_cols,
                    'Importance': model.feature_importances_
                }).sort_values('Importance', ascending=False)

                st.dataframe(feature_importance)

                plt.figure(figsize=(10, 6))
                plt.barh(feature_importance['Feature'][:10], feature_importance['Importance'][:10])
                plt.xlabel('Importance')
                plt.title('Top 10 Feature Importances')
                plt.tight_layout()
                st.pyplot()
                plt.close()

            # Classification report
            st.markdown("### 📋 Detailed Classification Report")
            report = classification_report(y_test, y_pred_test, target_names=le.classes_, output_dict=True)
            report_df = pd.DataFrame(report).transpose()
            st.dataframe(report_df.round(3))

            # Model recommendations
            st.markdown("### 💡 Model Recommendations")
            if test_accuracy < 0.7:
                st.warning("⚠️ Low accuracy - consider feature engineering or different algorithms")
            elif test_accuracy > 0.9:
                st.success("✅ Excellent model performance")

            if abs(train_accuracy - test_accuracy) > 0.15:
                st.warning("⚠️ Large performance gap - possible overfitting")

            # Class imbalance warning
            min_class_ratio = min(class_counts) / max(class_counts)
            if min_class_ratio < 0.1:
                st.warning("⚠️ Severe class imbalance detected - consider resampling techniques")

        except Exception as e:
            st.error(f"Error in classification: {str(e)}")


def ensemble_methods():
    """Advanced ensemble methods for prediction"""
    create_tool_header("Ensemble Methods", "Advanced ensemble algorithms", "🎪")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

            # Task type selection
            task_type = st.selectbox("Task Type:", ["Classification", "Regression"])

            if task_type == "Classification" and len(categorical_cols) == 0:
                st.error("Need categorical columns for classification tasks")
                return
            if task_type == "Regression" and len(numeric_cols) < 2:
                st.error("Need at least 2 numeric columns for regression tasks")
                return

            # Ensemble method selection
            ensemble_type = st.selectbox("Ensemble Method:", [
                "Random Forest", "Extra Trees", "Gradient Boosting",
                "AdaBoost", "Voting Classifier/Regressor", "Stacking"
            ])

            col1, col2 = st.columns(2)
            with col1:
                feature_cols = st.multiselect("Feature Variables:", numeric_cols,
                                              default=numeric_cols[:-1] if len(numeric_cols) > 1 else [])
            with col2:
                if task_type == "Classification":
                    target_col = st.selectbox("Target Variable:", categorical_cols)
                else:
                    target_col = st.selectbox("Target Variable:", numeric_cols)

            if feature_cols and target_col:
                perform_ensemble_analysis(df, feature_cols, target_col, ensemble_type, task_type)


def perform_ensemble_analysis(df, feature_cols, target_col, ensemble_type, task_type):
    """Perform ensemble analysis"""
    if st.button("Run Ensemble Analysis"):
        try:
            from sklearn.model_selection import train_test_split, cross_val_score
            from sklearn.preprocessing import StandardScaler, LabelEncoder
            from sklearn.ensemble import (RandomForestClassifier, RandomForestRegressor,
                                          ExtraTreesClassifier, ExtraTreesRegressor,
                                          GradientBoostingClassifier, GradientBoostingRegressor,
                                          AdaBoostClassifier, AdaBoostRegressor,
                                          VotingClassifier, VotingRegressor,
                                          StackingClassifier, StackingRegressor)
            from sklearn.linear_model import LogisticRegression, LinearRegression
            from sklearn.svm import SVC, SVR
            from sklearn.metrics import accuracy_score, r2_score, mean_squared_error
            import numpy as np

            # Prepare data
            X = df[feature_cols].dropna()
            y = df[target_col].dropna()

            # Align data
            common_index = X.index.intersection(y.index)
            X = X.loc[common_index]
            y = y.loc[common_index]

            # Encode target if classification
            if task_type == "Classification":
                le = LabelEncoder()
                y_encoded = le.fit_transform(y)
                y_to_use = y_encoded
                classes = le.classes_
            else:
                y_to_use = y
                classes = None

            # Split data
            test_size = 0.2
            X_train, X_test, y_train, y_test = train_test_split(
                X, y_to_use, test_size=test_size, random_state=42,
                stratify=y_to_use if task_type == "Classification" and len(np.unique(y_to_use)) > 1 else None
            )

            # Scale features for some algorithms
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Initialize model
            model = None

            # Create ensemble model
            if ensemble_type == "Random Forest":
                n_estimators = st.slider("Number of Trees:", 10, 300, 100, 10)
                max_depth = st.slider("Max Depth:", 3, 20, None)
                max_depth = None if max_depth == 20 else max_depth

                if task_type == "Classification":
                    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth,
                                                   random_state=42)
                else:
                    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth,
                                                  random_state=42)

            elif ensemble_type == "Extra Trees":
                n_estimators = st.slider("Number of Trees:", 10, 300, 100, 10)

                if task_type == "Classification":
                    model = ExtraTreesClassifier(n_estimators=n_estimators, random_state=42)
                else:
                    model = ExtraTreesRegressor(n_estimators=n_estimators, random_state=42)

            elif ensemble_type == "Gradient Boosting":
                n_estimators = st.slider("Number of Boosting Stages:", 50, 300, 100, 25)
                learning_rate = st.slider("Learning Rate:", 0.01, 0.3, 0.1, 0.01)

                if task_type == "Classification":
                    model = GradientBoostingClassifier(n_estimators=n_estimators,
                                                       learning_rate=learning_rate, random_state=42)
                else:
                    model = GradientBoostingRegressor(n_estimators=n_estimators,
                                                      learning_rate=learning_rate, random_state=42)

            elif ensemble_type == "AdaBoost":
                n_estimators = st.slider("Number of Estimators:", 10, 200, 50, 10)
                learning_rate = st.slider("Learning Rate:", 0.1, 2.0, 1.0, 0.1)

                if task_type == "Classification":
                    model = AdaBoostClassifier(n_estimators=n_estimators,
                                               learning_rate=learning_rate, random_state=42)
                else:
                    model = AdaBoostRegressor(n_estimators=n_estimators,
                                              learning_rate=learning_rate, random_state=42)

            elif ensemble_type == "Voting Classifier/Regressor":
                if task_type == "Classification":
                    estimators = [
                        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
                        ('lr', LogisticRegression(random_state=42, max_iter=1000)),
                        ('svc', SVC(probability=True, random_state=42))
                    ]
                    voting = st.selectbox("Voting Type:", ['hard', 'soft'])
                    model = VotingClassifier(estimators=estimators, voting=voting)
                else:
                    estimators = [
                        ('rf', RandomForestRegressor(n_estimators=100, random_state=42)),
                        ('lr', LinearRegression()),
                        ('svr', SVR())
                    ]
                    model = VotingRegressor(estimators=estimators)

            elif ensemble_type == "Stacking":
                if task_type == "Classification":
                    estimators = [
                        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
                        ('lr', LogisticRegression(random_state=42, max_iter=1000))
                    ]
                    final_estimator = LogisticRegression(random_state=42)
                    model = StackingClassifier(estimators=estimators, final_estimator=final_estimator)
                else:
                    estimators = [
                        ('rf', RandomForestRegressor(n_estimators=100, random_state=42)),
                        ('lr', LinearRegression())
                    ]
                    final_estimator = LinearRegression()
                    model = StackingRegressor(estimators=estimators, final_estimator=final_estimator)
            else:
                st.error("Invalid ensemble method selected")
                return

            if model is None:
                st.error("Model initialization failed")
                return

            # Fit model
            if ensemble_type in ["Voting Classifier/Regressor", "Stacking"] and task_type == "Classification":
                model.fit(X_train_scaled, y_train)
                y_pred_train = model.predict(X_train_scaled)
                y_pred_test = model.predict(X_test_scaled)
            else:
                model.fit(X_train, y_train)
                y_pred_train = model.predict(X_train)
                y_pred_test = model.predict(X_test)

            # Calculate metrics and display results
            st.markdown("### 📊 Ensemble Model Performance")

            if task_type == "Classification":
                train_accuracy = accuracy_score(y_train, y_pred_train)
                test_accuracy = accuracy_score(y_test, y_pred_test)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Training Accuracy", f"{train_accuracy:.4f}")
                with col2:
                    st.metric("Test Accuracy", f"{test_accuracy:.4f}")

            else:
                train_r2 = r2_score(y_train, y_pred_train)
                test_r2 = r2_score(y_test, y_pred_test)
                test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Training R²", f"{train_r2:.4f}")
                with col2:
                    st.metric("Test R²", f"{test_r2:.4f}")
                with col3:
                    st.metric("Test RMSE", f"{test_rmse:.4f}")

            # Cross-validation
            st.markdown("### 🔄 Cross-Validation Results")
            cv_scoring = 'accuracy' if task_type == "Classification" else 'r2'

            if ensemble_type in ["Voting Classifier/Regressor", "Stacking"] and task_type == "Classification":
                cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring=cv_scoring)
            else:
                cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring=cv_scoring)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("CV Mean", f"{cv_scores.mean():.4f}")
            with col2:
                st.metric("CV Std", f"{cv_scores.std():.4f}")
            with col3:
                st.metric("CV Range", f"{cv_scores.max() - cv_scores.min():.4f}")

            # Feature importance (if available)
            if hasattr(model, 'feature_importances_'):
                st.markdown("### 🎯 Feature Importance")
                feature_importance = pd.DataFrame({
                    'Feature': feature_cols,
                    'Importance': model.feature_importances_
                }).sort_values('Importance', ascending=False)

                st.dataframe(feature_importance)

                plt.figure(figsize=(10, 6))
                top_features = feature_importance.head(10)
                plt.barh(top_features['Feature'], top_features['Importance'])
                plt.xlabel('Importance')
                plt.title('Top 10 Feature Importances')
                plt.tight_layout()
                st.pyplot()
                plt.close()

            # Ensemble insights
            st.markdown("### 💡 Ensemble Insights")

            if ensemble_type == "Random Forest":
                st.info("🌲 Random Forest uses bootstrap sampling and random feature selection for diversity")
            elif ensemble_type == "Gradient Boosting":
                st.info("🚀 Gradient Boosting builds models sequentially, each correcting previous errors")
            elif ensemble_type == "Voting Classifier/Regressor":
                st.info("🗳️ Voting combines multiple different algorithms for robust predictions")
            elif ensemble_type == "Stacking":
                st.info("📚 Stacking uses a meta-learner to combine base model predictions")

            # Performance assessment
            if task_type == "Classification":
                if test_accuracy > 0.85:
                    st.success("✅ Excellent ensemble performance!")
                elif test_accuracy < 0.7:
                    st.warning("⚠️ Consider feature engineering or different base models")
            else:
                if test_r2 > 0.8:
                    st.success("✅ Excellent ensemble performance!")
                elif test_r2 < 0.5:
                    st.warning("⚠️ Consider feature engineering or different base models")

        except Exception as e:
            st.error(f"Error in ensemble analysis: {str(e)}")


def feature_selection():
    """Advanced feature selection techniques"""
    create_tool_header("Feature Selection", "Select the most important features for modeling", "🎯")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

            if len(numeric_cols) < 2:
                st.error("Need at least 2 numeric columns for feature selection")
                return

            # Task type and target selection
            task_type = st.selectbox("Task Type:", ["Regression", "Classification"])

            col1, col2 = st.columns(2)
            with col1:
                feature_cols = st.multiselect("Feature Variables:", numeric_cols,
                                              default=numeric_cols[:-1] if len(numeric_cols) > 1 else [])
            with col2:
                if task_type == "Classification" and len(categorical_cols) > 0:
                    target_col = st.selectbox("Target Variable:", categorical_cols)
                else:
                    target_col = st.selectbox("Target Variable:", numeric_cols)

            if feature_cols and target_col:
                # Feature selection method
                selection_method = st.selectbox("Feature Selection Method:", [
                    "Correlation Analysis", "Mutual Information", "Univariate Selection",
                    "Recursive Feature Elimination", "Feature Importance (Tree-based)",
                    "Lasso Feature Selection"
                ])

                perform_feature_selection(df, feature_cols, target_col, selection_method, task_type)


def perform_feature_selection(df, feature_cols, target_col, selection_method, task_type):
    """Perform feature selection analysis"""
    if st.button("Run Feature Selection"):
        try:
            from sklearn.feature_selection import (mutual_info_regression, mutual_info_classif,
                                                   SelectKBest, f_regression, f_classif,
                                                   RFE, SelectFromModel)
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
            from sklearn.linear_model import LassoCV, LogisticRegression
            from sklearn.preprocessing import LabelEncoder
            import numpy as np

            # Prepare data
            X = df[feature_cols].dropna()
            y = df[target_col].dropna()

            # Align data
            common_index = X.index.intersection(y.index)
            X = X.loc[common_index]
            y = y.loc[common_index]

            # Encode target if classification
            if task_type == "Classification":
                le = LabelEncoder()
                y_encoded = le.fit_transform(y)
                y_to_use = y_encoded
            else:
                y_to_use = y

            st.markdown("### 🎯 Feature Selection Results")

            if selection_method == "Correlation Analysis":
                # Simple correlation analysis
                correlations = []
                for col in feature_cols:
                    if task_type == "Classification":
                        # For classification, compute correlation with encoded target
                        corr = np.corrcoef(X[col], y_to_use)[0, 1]
                    else:
                        corr = np.corrcoef(X[col], y_to_use)[0, 1]
                    correlations.append(abs(corr))

                feature_scores = pd.DataFrame({
                    'Feature': feature_cols,
                    'Absolute_Correlation': correlations
                }).sort_values('Absolute_Correlation', ascending=False)

                st.dataframe(feature_scores)

                # Plot correlation scores
                plt.figure(figsize=(10, 6))
                plt.barh(feature_scores['Feature'], feature_scores['Absolute_Correlation'])
                plt.xlabel('Absolute Correlation')
                plt.title('Feature Correlation with Target')
                plt.tight_layout()
                st.pyplot()
                plt.close()

            elif selection_method == "Mutual Information":
                if task_type == "Classification":
                    mi_scores = mutual_info_classif(X, y_to_use, random_state=42)
                else:
                    mi_scores = mutual_info_regression(X, y_to_use, random_state=42)

                feature_scores = pd.DataFrame({
                    'Feature': feature_cols,
                    'Mutual_Information': mi_scores
                }).sort_values('Mutual_Information', ascending=False)

                st.dataframe(feature_scores)

                plt.figure(figsize=(10, 6))
                plt.barh(feature_scores['Feature'], feature_scores['Mutual_Information'])
                plt.xlabel('Mutual Information Score')
                plt.title('Feature Mutual Information with Target')
                plt.tight_layout()
                st.pyplot()
                plt.close()

            elif selection_method == "Univariate Selection":
                k_best = st.slider("Number of Top Features:", 1, len(feature_cols), min(5, len(feature_cols)))

                if task_type == "Classification":
                    selector = SelectKBest(score_func=f_classif, k=k_best)
                else:
                    selector = SelectKBest(score_func=f_regression, k=k_best)

                X_selected = selector.fit_transform(X, y_to_use)
                selected_features = [feature_cols[i] for i in selector.get_support(indices=True)]

                feature_scores = pd.DataFrame({
                    'Feature': feature_cols,
                    'F_Score': selector.scores_,
                    'P_Value': selector.pvalues_,
                    'Selected': [col in selected_features for col in feature_cols]
                }).sort_values('F_Score', ascending=False)

                st.dataframe(feature_scores)
                st.info(f"Selected {len(selected_features)} features: {', '.join(selected_features)}")

            elif selection_method == "Recursive Feature Elimination":
                n_features = st.slider("Target Number of Features:", 1, len(feature_cols), min(5, len(feature_cols)))

                if task_type == "Classification":
                    estimator = RandomForestClassifier(n_estimators=100, random_state=42)
                else:
                    estimator = RandomForestRegressor(n_estimators=100, random_state=42)

                rfe = RFE(estimator=estimator, n_features_to_select=n_features)
                rfe.fit(X, y_to_use)

                selected_features = [feature_cols[i] for i in range(len(feature_cols)) if rfe.support_[i]]

                feature_ranking = pd.DataFrame({
                    'Feature': feature_cols,
                    'Ranking': rfe.ranking_,
                    'Selected': rfe.support_
                }).sort_values('Ranking')

                st.dataframe(feature_ranking)
                st.info(f"Selected {len(selected_features)} features: {', '.join(selected_features)}")

            elif selection_method == "Feature Importance (Tree-based)":
                if task_type == "Classification":
                    model = RandomForestClassifier(n_estimators=100, random_state=42)
                else:
                    model = RandomForestRegressor(n_estimators=100, random_state=42)

                model.fit(X, y_to_use)

                feature_importance = pd.DataFrame({
                    'Feature': feature_cols,
                    'Importance': model.feature_importances_
                }).sort_values('Importance', ascending=False)

                st.dataframe(feature_importance)

                # Feature importance plot
                plt.figure(figsize=(10, 6))
                plt.barh(feature_importance['Feature'], feature_importance['Importance'])
                plt.xlabel('Feature Importance')
                plt.title('Tree-based Feature Importance')
                plt.tight_layout()
                st.pyplot()
                plt.close()

                # Top features recommendation
                top_n = st.slider("Top N Features to Recommend:", 1, len(feature_cols), min(5, len(feature_cols)))
                top_features = feature_importance.head(top_n)['Feature'].tolist()
                st.info(f"Top {top_n} features: {', '.join(top_features)}")

            elif selection_method == "Lasso Feature Selection":
                if task_type == "Classification":
                    st.warning("Lasso feature selection works better for regression tasks")
                    model = LogisticRegression(penalty='l1', solver='liblinear', random_state=42)
                    model.fit(X, y_to_use)
                    coefs = np.abs(model.coef_[0])
                else:
                    model = LassoCV(cv=5, random_state=42)
                    model.fit(X, y_to_use)
                    coefs = np.abs(model.coef_)

                feature_importance = pd.DataFrame({
                    'Feature': feature_cols,
                    'Lasso_Coefficient': coefs
                }).sort_values('Lasso_Coefficient', ascending=False)

                # Features with non-zero coefficients
                selected_features = feature_importance[feature_importance['Lasso_Coefficient'] > 1e-10]

                st.dataframe(feature_importance)

                if len(selected_features) > 0:
                    st.info(
                        f"Lasso selected {len(selected_features)} features: {', '.join(selected_features['Feature'].tolist())}")
                else:
                    st.warning("Lasso eliminated all features - try reducing regularization")

            # General recommendations
            st.markdown("### 💡 Feature Selection Recommendations")

            if len(feature_cols) > 20:
                st.info("🎯 Large feature set detected - consider dimensionality reduction techniques")

            if selection_method == "Correlation Analysis":
                st.info(
                    "📊 Correlation shows linear relationships - consider mutual information for non-linear relationships")
            elif selection_method == "Mutual Information":
                st.info("🔄 Mutual information captures both linear and non-linear relationships")
            elif selection_method == "Feature Importance (Tree-based)":
                st.info("🌲 Tree-based importance considers feature interactions")

        except Exception as e:
            st.error(f"Error in feature selection: {str(e)}")


def model_evaluator():
    """Comprehensive model evaluation and comparison"""
    create_tool_header("Model Evaluator", "Compare multiple models with comprehensive metrics", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

            # Task type selection
            task_type = st.selectbox("Task Type:", ["Classification", "Regression"])

            if task_type == "Classification" and len(categorical_cols) == 0:
                st.error("Need categorical columns for classification tasks")
                return
            if task_type == "Regression" and len(numeric_cols) < 2:
                st.error("Need at least 2 numeric columns for regression tasks")
                return

            col1, col2 = st.columns(2)
            with col1:
                feature_cols = st.multiselect("Feature Variables:", numeric_cols,
                                              default=numeric_cols[:-1] if len(numeric_cols) > 1 else [])
            with col2:
                if task_type == "Classification":
                    target_col = st.selectbox("Target Variable:", categorical_cols)
                else:
                    target_col = st.selectbox("Target Variable:", numeric_cols)

            if feature_cols and target_col:
                perform_model_evaluation(df, feature_cols, target_col, task_type)


def perform_model_evaluation(df, feature_cols, target_col, task_type):
    """Perform comprehensive model evaluation"""
    if st.button("Run Model Evaluation"):
        try:
            from sklearn.model_selection import train_test_split, cross_val_score
            from sklearn.preprocessing import StandardScaler, LabelEncoder
            from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                                         r2_score, mean_squared_error, mean_absolute_error,
                                         classification_report, confusion_matrix)
            from sklearn.linear_model import LinearRegression, LogisticRegression
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
            from sklearn.svm import SVR, SVC
            from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
            import numpy as np
            import time

            # Prepare data
            X = df[feature_cols].dropna()
            y = df[target_col].dropna()

            # Align data
            common_index = X.index.intersection(y.index)
            X = X.loc[common_index]
            y = y.loc[common_index]

            # Encode target if classification
            if task_type == "Classification":
                le = LabelEncoder()
                y_encoded = le.fit_transform(y)
                y_to_use = y_encoded
                classes = le.classes_
            else:
                y_to_use = y
                classes = None

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y_to_use, test_size=0.2, random_state=42,
                stratify=y_to_use if task_type == "Classification" and len(np.unique(y_to_use)) > 1 else None
            )

            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Define models to compare
            if task_type == "Classification":
                models = {
                    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
                    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
                    'Decision Tree': DecisionTreeClassifier(random_state=42),
                    'SVM': SVC(random_state=42, probability=True)
                }
                scoring_metric = 'accuracy'
            else:
                models = {
                    'Linear Regression': LinearRegression(),
                    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
                    'Decision Tree': DecisionTreeRegressor(random_state=42),
                    'SVM': SVR()
                }
                scoring_metric = 'r2'

            # Evaluate each model
            results = []

            st.markdown("### 📊 Model Comparison Results")

            progress_bar = st.progress(0)
            status_text = st.empty()

            for i, (name, model) in enumerate(models.items()):
                status_text.text(f"Evaluating {name}...")
                progress_bar.progress((i + 1) / len(models))

                start_time = time.time()

                # Use scaled data for SVM, original for tree-based
                if 'SVM' in name:
                    X_train_model = X_train_scaled
                    X_test_model = X_test_scaled
                else:
                    X_train_model = X_train
                    X_test_model = X_test

                # Fit model
                model.fit(X_train_model, y_train)

                # Predictions
                y_pred_train = model.predict(X_train_model)
                y_pred_test = model.predict(X_test_model)

                # Cross-validation
                cv_scores = cross_val_score(model, X_train_model, y_train, cv=5, scoring=scoring_metric)

                training_time = time.time() - start_time

                # Calculate metrics
                if task_type == "Classification":
                    train_acc = accuracy_score(y_train, y_pred_train)
                    test_acc = accuracy_score(y_test, y_pred_test)

                    avg_method = 'weighted' if len(np.unique(y_to_use)) > 2 else 'binary'
                    test_precision = precision_score(y_test, y_pred_test, average=avg_method)
                    test_recall = recall_score(y_test, y_pred_test, average=avg_method)
                    test_f1 = f1_score(y_test, y_pred_test, average=avg_method)

                    results.append({
                        'Model': name,
                        'Train Accuracy': train_acc,
                        'Test Accuracy': test_acc,
                        'Precision': test_precision,
                        'Recall': test_recall,
                        'F1-Score': test_f1,
                        'CV Mean': cv_scores.mean(),
                        'CV Std': cv_scores.std(),
                        'Training Time (s)': training_time
                    })
                else:
                    train_r2 = r2_score(y_train, y_pred_train)
                    test_r2 = r2_score(y_test, y_pred_test)
                    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
                    test_mae = mean_absolute_error(y_test, y_pred_test)

                    results.append({
                        'Model': name,
                        'Train R²': train_r2,
                        'Test R²': test_r2,
                        'RMSE': test_rmse,
                        'MAE': test_mae,
                        'CV Mean': cv_scores.mean(),
                        'CV Std': cv_scores.std(),
                        'Training Time (s)': training_time
                    })

            progress_bar.empty()
            status_text.empty()

            # Display results
            results_df = pd.DataFrame(results).round(4)
            st.dataframe(results_df)

            # Best model analysis
            if task_type == "Classification":
                best_model_idx = results_df['Test Accuracy'].idxmax()
                best_metric = 'Test Accuracy'
            else:
                best_model_idx = results_df['Test R²'].idxmax()
                best_metric = 'Test R²'

            best_model_name = results_df.loc[best_model_idx, 'Model']
            best_score = results_df.loc[best_model_idx, best_metric]

            st.success(f"🏆 Best Model: {best_model_name} ({best_metric}: {best_score:.4f})")

            # Performance visualization
            st.markdown("### 📈 Model Performance Comparison")

            if task_type == "Classification":
                metric_col = 'Test Accuracy'
            else:
                metric_col = 'Test R²'

            plt.figure(figsize=(10, 6))
            plt.barh(results_df['Model'], results_df[metric_col])
            plt.xlabel(metric_col)
            plt.title(f'Model Comparison - {metric_col}')
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Training time comparison
            st.markdown("### ⏱️ Training Time Comparison")
            plt.figure(figsize=(10, 6))
            plt.barh(results_df['Model'], results_df['Training Time (s)'])
            plt.xlabel('Training Time (seconds)')
            plt.title('Model Training Time Comparison')
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Model recommendations
            st.markdown("### 💡 Model Selection Recommendations")

            # Find best performing models
            top_models = results_df.nlargest(2, metric_col)

            st.write(f"**Top performing models:**")
            for idx, row in top_models.iterrows():
                st.write(f"- {row['Model']}: {row[metric_col]:.4f}")

            # Speed vs accuracy tradeoff
            fastest_model = results_df.loc[results_df['Training Time (s)'].idxmin()]
            st.write(f"**Fastest model:** {fastest_model['Model']} ({fastest_model['Training Time (s)']:.3f}s)")

            # Consistency analysis
            most_consistent = results_df.loc[results_df['CV Std'].idxmin()]
            st.write(f"**Most consistent model:** {most_consistent['Model']} (CV Std: {most_consistent['CV Std']:.4f})")

            # General recommendations
            if task_type == "Classification":
                if best_score > 0.9:
                    st.success("✅ Excellent classification performance achieved!")
                elif best_score < 0.7:
                    st.warning("⚠️ Consider feature engineering or more complex models")
            else:
                if best_score > 0.8:
                    st.success("✅ Excellent regression performance achieved!")
                elif best_score < 0.5:
                    st.warning("⚠️ Consider feature engineering or more complex models")

        except Exception as e:
            st.error(f"Error in model evaluation: {str(e)}")


def cross_validation():
    """Advanced cross-validation strategies"""
    create_tool_header("Cross Validation", "Robust model validation with multiple strategies", "🔄")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

            # Task configuration
            task_type = st.selectbox("Task Type:", ["Classification", "Regression"])

            col1, col2 = st.columns(2)
            with col1:
                feature_cols = st.multiselect("Feature Variables:", numeric_cols,
                                              default=numeric_cols[:-1] if len(numeric_cols) > 1 else [])
            with col2:
                if task_type == "Classification" and len(categorical_cols) > 0:
                    target_col = st.selectbox("Target Variable:", categorical_cols)
                else:
                    target_col = st.selectbox("Target Variable:", numeric_cols)

            if feature_cols and target_col:
                # CV strategy selection
                cv_strategy = st.selectbox("Cross-Validation Strategy:", [
                    "K-Fold", "Stratified K-Fold", "Time Series Split",
                    "Leave-One-Out", "ShuffleSplit", "Group K-Fold"
                ])

                # Model selection
                if task_type == "Classification":
                    model_options = ["Logistic Regression", "Random Forest", "SVM", "Gradient Boosting"]
                else:
                    model_options = ["Linear Regression", "Random Forest", "SVM", "Gradient Boosting"]

                selected_model = st.selectbox("Model to Validate:", model_options)

                perform_cross_validation(df, feature_cols, target_col, task_type, cv_strategy, selected_model)


def perform_cross_validation(df, feature_cols, target_col, task_type, cv_strategy, selected_model):
    """Perform cross-validation analysis"""
    if st.button("Run Cross-Validation"):
        try:
            from sklearn.model_selection import (cross_val_score, cross_validate,
                                                 KFold, StratifiedKFold, TimeSeriesSplit,
                                                 LeaveOneOut, ShuffleSplit, GroupKFold)
            from sklearn.preprocessing import StandardScaler, LabelEncoder
            from sklearn.linear_model import LinearRegression, LogisticRegression
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor, \
                GradientBoostingClassifier
            from sklearn.svm import SVR, SVC
            import numpy as np

            # Prepare data
            X = df[feature_cols].dropna()
            y = df[target_col].dropna()

            # Align data
            common_index = X.index.intersection(y.index)
            X = X.loc[common_index]
            y = y.loc[common_index]

            # Encode target if classification
            if task_type == "Classification":
                le = LabelEncoder()
                y_encoded = le.fit_transform(y)
                y_to_use = y_encoded
            else:
                y_to_use = y

            # Create model
            if task_type == "Classification":
                if selected_model == "Logistic Regression":
                    model = LogisticRegression(random_state=42, max_iter=1000)
                elif selected_model == "Random Forest":
                    model = RandomForestClassifier(n_estimators=100, random_state=42)
                elif selected_model == "SVM":
                    model = SVC(random_state=42)
                elif selected_model == "Gradient Boosting":
                    model = GradientBoostingClassifier(random_state=42)
            else:
                if selected_model == "Linear Regression":
                    model = LinearRegression()
                elif selected_model == "Random Forest":
                    model = RandomForestRegressor(n_estimators=100, random_state=42)
                elif selected_model == "SVM":
                    model = SVR()
                elif selected_model == "Gradient Boosting":
                    model = GradientBoostingRegressor(random_state=42)

            # Create cross-validation strategy
            if cv_strategy == "K-Fold":
                n_splits = st.slider("Number of Folds:", 3, 10, 5)
                cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)

            elif cv_strategy == "Stratified K-Fold":
                if task_type != "Classification":
                    st.warning("Stratified K-Fold is designed for classification tasks")
                n_splits = st.slider("Number of Folds:", 3, 10, 5)
                cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

            elif cv_strategy == "Time Series Split":
                n_splits = st.slider("Number of Splits:", 3, 10, 5)
                cv = TimeSeriesSplit(n_splits=n_splits)

            elif cv_strategy == "Leave-One-Out":
                if len(X) > 100:
                    st.warning("Leave-One-Out can be slow for large datasets")
                cv = LeaveOneOut()

            elif cv_strategy == "ShuffleSplit":
                n_splits = st.slider("Number of Splits:", 10, 100, 20)
                test_size = st.slider("Test Size:", 0.1, 0.5, 0.2, 0.05)
                cv = ShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=42)

            elif cv_strategy == "Group K-Fold":
                # For simplicity, create random groups
                st.info("Using random groups for demonstration - in practice, use meaningful groups")
                groups = np.random.randint(0, 5, len(X))
                n_splits = st.slider("Number of Folds:", 3, 5, 3)
                cv = GroupKFold(n_splits=n_splits)

            # Scale features if needed
            if selected_model == "SVM":
                from sklearn.pipeline import Pipeline
                model = Pipeline([
                    ('scaler', StandardScaler()),
                    ('model', model)
                ])

            # Define scoring metrics
            if task_type == "Classification":
                scoring = ['accuracy', 'precision_weighted', 'recall_weighted', 'f1_weighted']
            else:
                scoring = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error']

            # Perform cross-validation
            st.markdown("### 🔄 Cross-Validation Results")

            with st.spinner("Running cross-validation..."):
                if cv_strategy == "Group K-Fold":
                    cv_results = cross_validate(model, X, y_to_use, cv=cv, scoring=scoring,
                                                groups=groups, return_train_score=True)
                else:
                    cv_results = cross_validate(model, X, y_to_use, cv=cv, scoring=scoring,
                                                return_train_score=True)

            # Display results
            results_summary = []

            for metric in scoring:
                test_scores = cv_results[f'test_{metric}']
                train_scores = cv_results[f'train_{metric}']

                # Convert negative scores to positive for display
                if metric.startswith('neg_'):
                    test_scores = -test_scores
                    train_scores = -train_scores
                    display_metric = metric.replace('neg_', '').replace('_', ' ').title()
                else:
                    display_metric = metric.replace('_', ' ').title()

                results_summary.append({
                    'Metric': display_metric,
                    'CV Mean': test_scores.mean(),
                    'CV Std': test_scores.std(),
                    'CV Min': test_scores.min(),
                    'CV Max': test_scores.max(),
                    'Train Mean': train_scores.mean(),
                    'Overfitting': train_scores.mean() - test_scores.mean()
                })

            results_df = pd.DataFrame(results_summary).round(4)
            st.dataframe(results_df)

            # Visualization
            st.markdown("### 📊 Cross-Validation Score Distribution")

            main_metric = scoring[0]
            test_scores = cv_results[f'test_{main_metric}']
            if main_metric.startswith('neg_'):
                test_scores = -test_scores

            plt.figure(figsize=(10, 6))
            plt.hist(test_scores, bins=min(10, len(test_scores) // 2), alpha=0.7, edgecolor='black')
            plt.axvline(test_scores.mean(), color='red', linestyle='--',
                        label=f'Mean: {test_scores.mean():.4f}')
            plt.xlabel(scoring[0].replace('_', ' ').title())
            plt.ylabel('Frequency')
            plt.title(f'Distribution of {cv_strategy} Scores')
            plt.legend()
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Fold-by-fold analysis
            st.markdown("### 📈 Fold-by-Fold Performance")

            fold_data = []
            for i, score in enumerate(test_scores):
                fold_data.append({'Fold': i + 1, 'Score': score})

            fold_df = pd.DataFrame(fold_data)

            plt.figure(figsize=(10, 6))
            plt.plot(fold_df['Fold'], fold_df['Score'], 'o-', markersize=8)
            plt.axhline(test_scores.mean(), color='red', linestyle='--',
                        label=f'Mean: {test_scores.mean():.4f}')
            plt.fill_between(fold_df['Fold'],
                             test_scores.mean() - test_scores.std(),
                             test_scores.mean() + test_scores.std(),
                             alpha=0.2, color='red', label=f'±1 Std: {test_scores.std():.4f}')
            plt.xlabel('Fold')
            plt.ylabel(scoring[0].replace('_', ' ').title())
            plt.title('Performance Across Folds')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Cross-validation insights
            st.markdown("### 💡 Cross-Validation Insights")

            # Stability analysis
            cv_coefficient_variation = test_scores.std() / test_scores.mean()
            if cv_coefficient_variation < 0.1:
                st.success("✅ Very stable model performance across folds")
            elif cv_coefficient_variation < 0.2:
                st.info("ℹ️ Reasonably stable model performance")
            else:
                st.warning("⚠️ High variance in performance across folds - model may be unstable")

            # Overfitting analysis
            main_overfitting = results_df.loc[0, 'Overfitting']
            if main_overfitting > 0.1:
                st.warning("⚠️ Significant overfitting detected - consider regularization")
            elif main_overfitting > 0.05:
                st.info("ℹ️ Mild overfitting - monitor model complexity")
            else:
                st.success("✅ No significant overfitting detected")

            # CV strategy recommendations
            if cv_strategy == "K-Fold":
                st.info("📝 K-Fold provides good general estimate of model performance")
            elif cv_strategy == "Stratified K-Fold":
                st.info("📝 Stratified K-Fold maintains class distribution across folds")
            elif cv_strategy == "Time Series Split":
                st.info("📝 Time Series Split respects temporal order in data")
            elif cv_strategy == "Leave-One-Out":
                st.info("📝 Leave-One-Out provides maximum training data but can be noisy")

        except Exception as e:
            st.error(f"Error in cross-validation: {str(e)}")


def trend_analysis():
    """Analyze trends in time series data"""
    create_tool_header("Trend Analysis", "Identify and analyze trends in your data", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Select columns
            date_cols = []
            for col in df.columns:
                if df[col].dtype == 'object':
                    try:
                        pd.to_datetime(df[col])
                        date_cols.append(col)
                    except:
                        continue

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(date_cols) > 0 and len(numeric_cols) > 0:
                col1, col2 = st.columns(2)
                with col1:
                    date_col = st.selectbox("Date Column:", date_cols)
                with col2:
                    value_col = st.selectbox("Value Column:", numeric_cols)

                if st.button("Analyze Trend"):
                    analyze_trend_data(df, date_col, value_col)
            else:
                st.error("Need at least one date column and one numeric column for trend analysis")


def analyze_trend_data(df, date_col, value_col):
    """Perform trend analysis"""
    try:
        from scipy import stats

        # Prepare data
        df_clean = df[[date_col, value_col]].dropna()
        df_clean[date_col] = pd.to_datetime(df_clean[date_col])
        df_clean = df_clean.sort_values(date_col)

        # Calculate trend
        x = np.arange(len(df_clean))
        y = df_clean[value_col].values

        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

        # Results
        st.markdown("### 📊 Trend Analysis Results")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            trend_direction = "📈 Increasing" if slope > 0 else "📉 Decreasing" if slope < 0 else "➡️ Flat"
            st.metric("Trend Direction", trend_direction)
        with col2:
            st.metric("Slope", f"{slope:.6f}")
        with col3:
            st.metric("R-squared", f"{r_value ** 2:.4f}")
        with col4:
            significance = "Significant" if p_value < 0.05 else "Not Significant"
            st.metric("Significance (p<0.05)", significance)

        # Plot
        st.markdown("### 📈 Trend Visualization")
        plt.figure(figsize=(12, 6))
        plt.plot(df_clean[date_col], df_clean[value_col], 'o-', alpha=0.7, label='Data')

        # Trend line
        trend_line = intercept + slope * x
        plt.plot(df_clean[date_col], trend_line, 'r--', linewidth=2, label='Trend Line')

        plt.xlabel(date_col)
        plt.ylabel(value_col)
        plt.title(f"Trend Analysis: {value_col} over time")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()
        plt.close()

        # Statistical insights
        st.markdown("### 📝 Statistical Insights")
        st.write(f"**Trend Equation:** y = {slope:.6f}x + {intercept:.2f}")
        st.write(f"**Correlation Coefficient:** {r_value:.4f}")
        st.write(f"**P-value:** {p_value:.6f}")
        st.write(f"**Standard Error:** {std_err:.6f}")

        if p_value < 0.05:
            st.success("✅ The trend is statistically significant")
        else:
            st.warning("⚠️ The trend is not statistically significant")

    except Exception as e:
        st.error(f"Error in trend analysis: {str(e)}")


def forecasting():
    """Time series forecasting"""
    create_tool_header("Forecasting", "Predict future values using time series analysis", "🔮")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Select columns
            date_cols = []
            for col in df.columns:
                if df[col].dtype == 'object':
                    try:
                        pd.to_datetime(df[col])
                        date_cols.append(col)
                    except:
                        continue

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(date_cols) > 0 and len(numeric_cols) > 0:
                col1, col2, col3 = st.columns(3)
                with col1:
                    date_col = st.selectbox("Date Column:", date_cols)
                with col2:
                    value_col = st.selectbox("Value Column:", numeric_cols)
                with col3:
                    forecast_periods = st.number_input("Forecast Periods:", min_value=1, max_value=50, value=10)

                forecast_method = st.selectbox("Forecasting Method:",
                                               ["Linear Trend", "Moving Average", "Exponential Smoothing"])

                if st.button("Generate Forecast"):
                    perform_forecasting(df, date_col, value_col, forecast_periods, forecast_method)
            else:
                st.error("Need at least one date column and one numeric column for forecasting")


def perform_forecasting(df, date_col, value_col, forecast_periods, method):
    """Perform time series forecasting"""
    try:
        # Prepare data
        df_clean = df[[date_col, value_col]].dropna()
        df_clean[date_col] = pd.to_datetime(df_clean[date_col])
        df_clean = df_clean.sort_values(date_col)

        values = df_clean[value_col].values
        dates = df_clean[date_col].values

        # Generate future dates
        last_date = pd.to_datetime(dates[-1])
        date_freq = pd.infer_freq(df_clean[date_col])
        if date_freq is None:
            # Estimate frequency from data
            time_diff = (pd.to_datetime(dates[-1]) - pd.to_datetime(dates[0])) / (len(dates) - 1)
            future_dates = [last_date + time_diff * i for i in range(1, forecast_periods + 1)]
        else:
            future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1),
                                         periods=forecast_periods, freq=date_freq)

        # Forecasting
        forecast_values = []
        if method == "Linear Trend":
            from scipy import stats
            x = np.arange(len(values))
            slope, intercept, _, _, _ = stats.linregress(x, values)
            forecast_x = np.arange(len(values), len(values) + forecast_periods)
            forecast_values = intercept + slope * forecast_x

        elif method == "Moving Average":
            window = min(5, len(values))
            last_avg = np.mean(values[-window:])
            forecast_values = [last_avg] * forecast_periods

        elif method == "Exponential Smoothing":
            alpha = 0.3
            smoothed = [values[0]]
            for i in range(1, len(values)):
                smoothed.append(alpha * values[i] + (1 - alpha) * smoothed[i - 1])

            # Forecast using last smoothed value and trend
            if len(values) > 1:
                trend = smoothed[-1] - smoothed[-2]
                forecast_values = [smoothed[-1] + trend * i for i in range(1, forecast_periods + 1)]
            else:
                forecast_values = [smoothed[-1]] * forecast_periods
        else:
            # Default fallback
            forecast_values = [values[-1]] * forecast_periods

        # Display results
        st.markdown("### 📊 Forecast Results")

        # Create forecast dataframe
        forecast_df = pd.DataFrame({
            'Date': future_dates,
            'Forecast': forecast_values
        })

        st.dataframe(forecast_df)

        # Plot
        st.markdown("### 📈 Forecast Visualization")
        plt.figure(figsize=(12, 6))

        # Historical data
        plt.plot(dates, values, 'o-', label='Historical Data', alpha=0.7)

        # Forecast
        plt.plot(future_dates, forecast_values, 'r--', label=f'{method} Forecast', linewidth=2)

        plt.xlabel(date_col)
        plt.ylabel(value_col)
        plt.title(f"Time Series Forecast: {value_col}")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()
        plt.close()

        # Download forecast
        csv_data = forecast_df.to_csv(index=False)
        FileHandler.create_download_link(csv_data.encode(), "forecast.csv", "text/csv")

    except Exception as e:
        st.error(f"Error in forecasting: {str(e)}")


def clustering_analysis():
    """Perform clustering analysis on data"""
    create_tool_header("Clustering Analysis", "Find patterns and groups in your data", "🎯")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(numeric_cols) >= 2:
                selected_cols = st.multiselect("Select columns for clustering:", numeric_cols,
                                               default=numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols)

                if len(selected_cols) >= 2:
                    col1, col2 = st.columns(2)
                    with col1:
                        n_clusters = st.slider("Number of clusters:", 2, 10, 3)
                    with col2:
                        algorithm = st.selectbox("Clustering Algorithm:", ["K-Means", "Hierarchical"])

                    if st.button("Perform Clustering"):
                        perform_clustering(df, selected_cols, n_clusters, algorithm)
                else:
                    st.warning("Please select at least 2 columns for clustering")
            else:
                st.error("Need at least 2 numeric columns for clustering analysis")


def perform_clustering(df, selected_cols, n_clusters, algorithm):
    """Perform clustering analysis"""
    try:
        # Import with error handling
        try:
            from sklearn.cluster import KMeans, AgglomerativeClustering
            from sklearn.preprocessing import StandardScaler
            from sklearn.metrics import silhouette_score
        except ImportError:
            st.error("scikit-learn is required for clustering analysis. Please install it.")
            return

        # Prepare data
        data = df[selected_cols].dropna()

        if len(data) < n_clusters:
            st.error(f"Not enough data points ({len(data)}) for {n_clusters} clusters")
            return

        # Standardize features
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)

        # Perform clustering
        if algorithm == "K-Means":
            model = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
        else:
            model = AgglomerativeClustering(n_clusters=n_clusters)

        clusters = model.fit_predict(data_scaled)

        # Calculate silhouette score
        silhouette_avg = silhouette_score(data_scaled, clusters)

        # Add cluster labels to original data
        data_with_clusters = data.copy()
        data_with_clusters['Cluster'] = clusters

        # Display results
        st.markdown("### 📊 Clustering Results")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Number of Clusters", n_clusters)
        with col2:
            st.metric("Silhouette Score", f"{silhouette_avg:.3f}")
        with col3:
            st.metric("Data Points", len(data))

        # Cluster summary
        st.markdown("### 📈 Cluster Summary")
        cluster_summary = data_with_clusters.groupby('Cluster').agg(['mean', 'count']).round(3)
        st.dataframe(cluster_summary)

        # Visualization
        st.markdown("### 📊 Cluster Visualization")

        if len(selected_cols) >= 2:
            plt.figure(figsize=(10, 8))
            scatter = plt.scatter(data[selected_cols[0]], data[selected_cols[1]],
                                  c=clusters, cmap='viridis', alpha=0.7)
            plt.xlabel(selected_cols[0])
            plt.ylabel(selected_cols[1])
            plt.title(f"{algorithm} Clustering Results")
            plt.colorbar(scatter, label='Cluster')
            st.pyplot()
            plt.close()

        # Download results
        csv_data = data_with_clusters.to_csv(index=False)
        FileHandler.create_download_link(csv_data.encode(), "clustering_results.csv", "text/csv")

        # Interpretation
        st.markdown("### 💡 Interpretation")
        if silhouette_avg > 0.5:
            st.success("✅ Excellent clustering structure")
        elif silhouette_avg > 0.3:
            st.info("ℹ️ Reasonable clustering structure")
        else:
            st.warning("⚠️ Weak clustering structure - consider different parameters")

    except Exception as e:
        st.error(f"Error in clustering analysis: {str(e)}")


def t_test_analysis():
    """Perform t-test statistical analysis"""
    create_tool_header("T-Test Analysis", "Compare means between groups", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            test_type = st.selectbox("T-Test Type:",
                                     ["One-Sample T-Test", "Two-Sample T-Test", "Paired T-Test"])

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

            if test_type == "One-Sample T-Test":
                perform_one_sample_ttest(df, numeric_cols)
            elif test_type == "Two-Sample T-Test":
                perform_two_sample_ttest(df, numeric_cols, categorical_cols)
            elif test_type == "Paired T-Test":
                perform_paired_ttest(df, numeric_cols)


def perform_one_sample_ttest(df, numeric_cols):
    """Perform one-sample t-test"""
    if len(numeric_cols) > 0:
        col1, col2 = st.columns(2)
        with col1:
            test_col = st.selectbox("Test Column:", numeric_cols)
        with col2:
            test_value = st.number_input("Test Value (μ₀):", value=0.0)

        if st.button("Perform One-Sample T-Test"):
            try:
                try:
                    from scipy.stats import ttest_1samp
                except ImportError:
                    st.error("scipy is required for statistical tests. Please install it.")
                    return

                data = df[test_col].dropna()

                if len(data) < 2:
                    st.error("Need at least 2 data points for t-test")
                    return

                statistic, p_value = ttest_1samp(data, test_value)

                st.markdown("### 📊 One-Sample T-Test Results")

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Sample Mean", f"{data.mean():.4f}")
                with col2:
                    st.metric("Test Value", f"{test_value:.4f}")
                with col3:
                    st.metric("T-Statistic", f"{statistic:.4f}")
                with col4:
                    st.metric("P-Value", f"{p_value:.6f}")

                # Interpretation
                alpha = 0.05
                if p_value < alpha:
                    st.success(f"✅ Reject null hypothesis (p < {alpha})")
                    st.write(f"The sample mean is significantly different from {test_value}")
                else:
                    st.info(f"ℹ️ Fail to reject null hypothesis (p ≥ {alpha})")
                    st.write(f"The sample mean is not significantly different from {test_value}")

            except Exception as e:
                st.error(f"Error in one-sample t-test: {str(e)}")
    else:
        st.error("No numeric columns found for t-test")


def perform_two_sample_ttest(df, numeric_cols, categorical_cols):
    """Perform two-sample t-test"""
    if len(numeric_cols) > 0 and len(categorical_cols) > 0:
        col1, col2 = st.columns(2)
        with col1:
            test_col = st.selectbox("Test Column:", numeric_cols)
        with col2:
            group_col = st.selectbox("Group Column:", categorical_cols)

        # Check if grouping column has exactly 2 groups
        unique_groups = df[group_col].unique()
        if len(unique_groups) == 2:
            if st.button("Perform Two-Sample T-Test"):
                try:
                    try:
                        from scipy.stats import ttest_ind
                    except ImportError:
                        st.error("scipy is required for statistical tests. Please install it.")
                        return

                    group1_data = df[df[group_col] == unique_groups[0]][test_col].dropna()
                    group2_data = df[df[group_col] == unique_groups[1]][test_col].dropna()

                    if len(group1_data) < 2 or len(group2_data) < 2:
                        st.error("Each group needs at least 2 data points for two-sample t-test")
                        return

                    statistic, p_value = ttest_ind(group1_data, group2_data)

                    st.markdown("### 📊 Two-Sample T-Test Results")

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric(f"Mean {unique_groups[0]}", f"{group1_data.mean():.4f}")
                    with col2:
                        st.metric(f"Mean {unique_groups[1]}", f"{group2_data.mean():.4f}")
                    with col3:
                        st.metric("T-Statistic", f"{statistic:.4f}")
                    with col4:
                        st.metric("P-Value", f"{p_value:.6f}")

                    # Sample sizes
                    st.write(
                        f"**Sample Sizes:** {unique_groups[0]}: {len(group1_data)}, {unique_groups[1]}: {len(group2_data)}")

                    # Interpretation
                    alpha = 0.05
                    if p_value < alpha:
                        st.success(f"✅ Reject null hypothesis (p < {alpha})")
                        st.write(f"There is a significant difference between {unique_groups[0]} and {unique_groups[1]}")
                    else:
                        st.info(f"ℹ️ Fail to reject null hypothesis (p ≥ {alpha})")
                        st.write(f"No significant difference between {unique_groups[0]} and {unique_groups[1]}")

                except Exception as e:
                    st.error(f"Error in two-sample t-test: {str(e)}")
        else:
            st.error(f"Group column must have exactly 2 unique values. Found: {len(unique_groups)}")
    else:
        st.error("Need at least one numeric column and one categorical column")


def perform_paired_ttest(df, numeric_cols):
    """Perform paired t-test"""
    if len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            col1_name = st.selectbox("First Column:", numeric_cols)
        with col2:
            col2_name = st.selectbox("Second Column:", [col for col in numeric_cols if col != col1_name])

        if st.button("Perform Paired T-Test"):
            try:
                try:
                    from scipy.stats import ttest_rel
                except ImportError:
                    st.error("scipy is required for statistical tests. Please install it.")
                    return

                # Get paired data (remove rows with missing values in either column)
                paired_data = df[[col1_name, col2_name]].dropna()

                if len(paired_data) < 2:
                    st.error("Need at least 2 paired observations for paired t-test")
                    return

                statistic, p_value = ttest_rel(paired_data[col1_name], paired_data[col2_name])

                st.markdown("### 📊 Paired T-Test Results")

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric(f"Mean {col1_name}", f"{paired_data[col1_name].mean():.4f}")
                with col2:
                    st.metric(f"Mean {col2_name}", f"{paired_data[col2_name].mean():.4f}")
                with col3:
                    st.metric("T-Statistic", f"{statistic:.4f}")
                with col4:
                    st.metric("P-Value", f"{p_value:.6f}")

                # Difference statistics
                differences = paired_data[col1_name] - paired_data[col2_name]
                st.write(f"**Mean Difference:** {differences.mean():.4f}")
                st.write(f"**Sample Size:** {len(paired_data)} pairs")

                # Interpretation
                alpha = 0.05
                if p_value < alpha:
                    st.success(f"✅ Reject null hypothesis (p < {alpha})")
                    st.write(f"There is a significant difference between {col1_name} and {col2_name}")
                else:
                    st.info(f"ℹ️ Fail to reject null hypothesis (p ≥ {alpha})")
                    st.write(f"No significant difference between {col1_name} and {col2_name}")

            except Exception as e:
                st.error(f"Error in paired t-test: {str(e)}")
    else:
        st.error("Need at least 2 numeric columns for paired t-test")


def anova_analysis():
    """Perform ANOVA analysis"""
    create_tool_header("ANOVA Analysis", "Compare means across multiple groups", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

            if len(numeric_cols) > 0 and len(categorical_cols) > 0:
                col1, col2 = st.columns(2)
                with col1:
                    dependent_var = st.selectbox("Dependent Variable:", numeric_cols)
                with col2:
                    independent_var = st.selectbox("Independent Variable (Groups):", categorical_cols)

                if st.button("Perform ANOVA"):
                    perform_anova_test(df, dependent_var, independent_var)
            else:
                st.error("Need at least one numeric column and one categorical column")


def perform_anova_test(df, dependent_var, independent_var):
    """Perform ANOVA test"""
    try:
        try:
            from scipy.stats import f_oneway
        except ImportError:
            st.error("scipy is required for ANOVA analysis. Please install it.")
            return

        # Group data
        groups = []
        group_names = df[independent_var].unique()

        for group in group_names:
            group_data = df[df[independent_var] == group][dependent_var].dropna()
            if len(group_data) > 0:
                groups.append(group_data)

        if len(groups) < 2:
            st.error("Need at least 2 groups for ANOVA")
            return

        # Perform ANOVA
        f_statistic, p_value = f_oneway(*groups)

        st.markdown("### 📊 ANOVA Results")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("F-Statistic", f"{f_statistic:.4f}")
        with col2:
            st.metric("P-Value", f"{p_value:.6f}")
        with col3:
            st.metric("Number of Groups", len(groups))

        # Group statistics
        st.markdown("### 📈 Group Statistics")
        group_stats = []
        for i, (group_name, group_data) in enumerate(zip(group_names, groups)):
            if len(group_data) > 0:
                group_stats.append({
                    'Group': group_name,
                    'Count': len(group_data),
                    'Mean': group_data.mean(),
                    'Std Dev': group_data.std(),
                    'Min': group_data.min(),
                    'Max': group_data.max()
                })

        group_stats_df = pd.DataFrame(group_stats)
        st.dataframe(group_stats_df.round(4))

        # Interpretation
        alpha = 0.05
        if p_value < alpha:
            st.success(f"✅ Reject null hypothesis (p < {alpha})")
            st.write("There are significant differences between group means")
        else:
            st.info(f"ℹ️ Fail to reject null hypothesis (p ≥ {alpha})")
            st.write("No significant differences between group means")

        # Box plot visualization
        st.markdown("### 📊 Box Plot by Groups")
        plt.figure(figsize=(10, 6))

        plot_data = []
        plot_labels = []
        for group_name, group_data in zip(group_names, groups):
            if len(group_data) > 0:
                plot_data.append(group_data)
                plot_labels.append(group_name)

        plt.boxplot(plot_data)
        plt.xticks(range(1, len(plot_labels) + 1), plot_labels)
        plt.xlabel(independent_var)
        plt.ylabel(dependent_var)
        plt.title(f"ANOVA: {dependent_var} by {independent_var}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()
        plt.close()

    except Exception as e:
        st.error(f"Error in ANOVA analysis: {str(e)}")


def moving_averages():
    """Calculate moving averages for time series"""
    create_tool_header("Moving Averages", "Smooth time series data with moving averages", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(numeric_cols) > 0:
                col1, col2, col3 = st.columns(3)
                with col1:
                    value_col = st.selectbox("Value Column:", numeric_cols)
                with col2:
                    window_size = st.slider("Window Size:", 3, 50, 7)
                with col3:
                    ma_type = st.selectbox("Moving Average Type:", ["Simple", "Exponential"])

                if st.button("Calculate Moving Average"):
                    calculate_moving_average(df, value_col, window_size, ma_type)
            else:
                st.error("Need at least one numeric column")


def calculate_moving_average(df, value_col, window_size, ma_type):
    """Calculate and display moving averages"""
    try:
        data = df[value_col].dropna()

        if len(data) < window_size:
            st.error(f"Need at least {window_size} data points for moving average calculation")
            return

        if ma_type == "Simple":
            ma = data.rolling(window=window_size).mean()
        else:  # Exponential
            ma = data.ewm(span=window_size).mean()

        # Create results dataframe
        results_df = pd.DataFrame({
            'Original': data,
            f'{ma_type}_MA_{window_size}': ma
        })

        st.markdown("### 📊 Moving Average Results")
        st.dataframe(results_df.head(20))

        # Plot
        st.markdown("### 📈 Moving Average Visualization")
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data.values, label='Original Data', alpha=0.7)
        plt.plot(ma.index, ma.values, label=f'{ma_type} MA ({window_size})', linewidth=2)
        plt.xlabel('Index')
        plt.ylabel(value_col)
        plt.title(f'{ma_type} Moving Average: {value_col}')
        plt.legend()
        plt.tight_layout()
        st.pyplot()
        plt.close()

        # Statistics
        st.markdown("### 📈 Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Original Mean", f"{data.mean():.4f}")
        with col2:
            st.metric("MA Mean", f"{ma.mean():.4f}")
        with col3:
            smoothing = (1 - ma.std() / data.std()) * 100
            st.metric("Smoothing Effect", f"{smoothing:.1f}%")

        # Download results
        csv_data = results_df.to_csv()
        FileHandler.create_download_link(csv_data.encode(), "moving_average_results.csv", "text/csv")

    except Exception as e:
        st.error(f"Error calculating moving average: {str(e)}")


def trend_decomposition():
    """Decompose time series into trend, seasonal, and residual components"""
    create_tool_header("Trend Decomposition", "Decompose time series into components", "🔍")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Select columns
            date_cols = []
            for col in df.columns:
                if df[col].dtype == 'object':
                    try:
                        pd.to_datetime(df[col])
                        date_cols.append(col)
                    except:
                        continue

            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(date_cols) > 0 and len(numeric_cols) > 0:
                col1, col2, col3 = st.columns(3)
                with col1:
                    date_col = st.selectbox("Date Column:", date_cols)
                with col2:
                    value_col = st.selectbox("Value Column:", numeric_cols)
                with col3:
                    period = st.number_input("Seasonal Period:", min_value=2, max_value=365, value=12)

                decomp_model = st.selectbox("Decomposition Model:", ["Additive", "Multiplicative"])

                if st.button("Decompose Time Series"):
                    perform_decomposition(df, date_col, value_col, period, decomp_model)
            else:
                st.error("Need at least one date column and one numeric column")


def perform_decomposition(df, date_col, value_col, period, model):
    """Perform time series decomposition"""
    try:
        from scipy import signal

        # Prepare data
        df_clean = df[[date_col, value_col]].dropna()
        df_clean[date_col] = pd.to_datetime(df_clean[date_col])
        df_clean = df_clean.sort_values(date_col)

        if len(df_clean) < 2 * period:
            st.error(f"Need at least {2 * period} data points for decomposition with period {period}")
            return

        values = df_clean[value_col].values

        # Simple trend extraction using moving average
        trend_series = pd.Series(values).rolling(window=period, center=True).mean()
        trend = np.array(trend_series)

        # Detrend
        if model == "Additive":
            detrended = values - trend
        else:  # Multiplicative
            # Handle NaN and zero values in trend for safe division
            trend_safe = np.where(np.isnan(trend) | (trend == 0), 1.0, trend)
            detrended = np.divide(values, trend_safe, out=np.zeros_like(values), where=(trend_safe != 0))

        # Simple seasonal component (average by period position)
        seasonal = np.zeros_like(values)
        for i in range(period):
            mask = np.arange(i, len(values), period)
            if len(mask) > 0:
                period_avg = np.nanmean(detrended[mask])
                seasonal[mask] = period_avg

        # Residual
        if model == "Additive":
            residual = values - trend - seasonal
        else:  # Multiplicative
            residual = values / (trend * seasonal)

        # Create results dataframe
        results_df = pd.DataFrame({
            'Date': df_clean[date_col],
            'Original': values,
            'Trend': trend,
            'Seasonal': seasonal,
            'Residual': residual
        })

        st.markdown("### 📊 Decomposition Results")
        st.dataframe(results_df.head(20))

        # Plots
        st.markdown("### 📈 Decomposition Visualization")

        fig, axes = plt.subplots(4, 1, figsize=(12, 12))

        # Original
        axes[0].plot(results_df['Date'], results_df['Original'])
        axes[0].set_title('Original Time Series')
        axes[0].set_ylabel(value_col)

        # Trend
        axes[1].plot(results_df['Date'], results_df['Trend'])
        axes[1].set_title('Trend Component')
        axes[1].set_ylabel('Trend')

        # Seasonal
        axes[2].plot(results_df['Date'], results_df['Seasonal'])
        axes[2].set_title('Seasonal Component')
        axes[2].set_ylabel('Seasonal')

        # Residual
        axes[3].plot(results_df['Date'], results_df['Residual'])
        axes[3].set_title('Residual Component')
        axes[3].set_ylabel('Residual')
        axes[3].set_xlabel('Date')

        for ax in axes:
            ax.tick_params(axis='x', rotation=45)

        plt.tight_layout()
        st.pyplot()
        plt.close()

        # Statistics
        st.markdown("### 📈 Component Statistics")

        col1, col2, col3 = st.columns(3)
        with col1:
            trend_var = np.nanvar(trend[~np.isnan(trend)])
            st.metric("Trend Variance", f"{trend_var:.4f}")
        with col2:
            seasonal_var = np.nanvar(seasonal)
            st.metric("Seasonal Variance", f"{seasonal_var:.4f}")
        with col3:
            residual_var = np.nanvar(residual)
            st.metric("Residual Variance", f"{residual_var:.4f}")

        # Download results
        csv_data = results_df.to_csv(index=False)
        FileHandler.create_download_link(csv_data.encode(), "decomposition_results.csv", "text/csv")

    except Exception as e:
        st.error(f"Error in trend decomposition: {str(e)}")


def excel_reader():
    """Advanced Excel file reader with sheet selection and analysis"""
    create_tool_header("Excel Reader", "Read and analyze Excel files with multiple sheets", "📊")

    uploaded_file = FileHandler.upload_files(['xlsx', 'xls'], accept_multiple=False)

    if uploaded_file:
        try:
            # Read Excel file to get sheet names
            excel_file = pd.ExcelFile(uploaded_file[0])
            sheet_names = excel_file.sheet_names

            if len(sheet_names) > 1:
                selected_sheet = st.selectbox("Select Sheet:", sheet_names)
            else:
                selected_sheet = sheet_names[0]
                st.info(f"Reading sheet: {selected_sheet}")

            # Read options
            st.markdown("### 📋 Reading Options")
            col1, col2, col3 = st.columns(3)

            with col1:
                header_row = st.number_input("Header Row (0-indexed):", min_value=0, value=0)
                skip_rows = st.number_input("Skip Rows:", min_value=0, value=0)

            with col2:
                max_rows = st.number_input("Max Rows (0 = all):", min_value=0, value=0)
                index_col = st.number_input("Index Column (None = -1):", min_value=-1, value=-1)

            with col3:
                na_values = st.text_input("Additional NA Values (comma-separated):", "")

            if st.button("Read Excel File"):
                read_excel_file(uploaded_file[0], selected_sheet, header_row, skip_rows,
                                max_rows, index_col, na_values)

        except Exception as e:
            st.error(f"Error reading Excel file: {str(e)}")


def read_excel_file(uploaded_file, sheet_name, header_row, skip_rows, max_rows, index_col, na_values):
    """Read Excel file with specified parameters"""
    try:
        # Prepare parameters
        read_params = {
            'sheet_name': sheet_name,
            'header': header_row if header_row >= 0 else None
        }

        if skip_rows > 0:
            read_params['skiprows'] = skip_rows
        if max_rows > 0:
            read_params['nrows'] = max_rows
        if index_col >= 0:
            read_params['index_col'] = index_col
        if na_values.strip():
            custom_na = [val.strip() for val in na_values.split(',')]
            read_params['na_values'] = custom_na

        # Read the Excel file
        df = pd.read_excel(uploaded_file, **read_params)

        # Display file information
        st.markdown("### 📁 File Information")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Rows", len(df))
        with col2:
            st.metric("Columns", len(df.columns))
        with col3:
            memory_usage = df.memory_usage(deep=True).sum() / 1024 ** 2
            st.metric("Memory (MB)", f"{memory_usage:.2f}")
        with col4:
            missing_pct = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
            st.metric("Missing %", f"{missing_pct:.1f}%")

        # Display data preview
        st.markdown("### 👀 Data Preview")

        preview_rows = st.slider("Preview Rows:", 5, min(50, len(df)), 10)
        st.dataframe(df.head(preview_rows))

        # Data summary
        st.markdown("### 📊 Quick Summary")

        # Column information
        col_info = []
        for col in df.columns:
            col_data = {
                'Column': col,
                'Type': str(df[col].dtype),
                'Non-Null': df[col].count(),
                'Null': df[col].isnull().sum(),
                'Unique': df[col].nunique()
            }

            if pd.api.types.is_numeric_dtype(df[col]):
                col_data['Min'] = df[col].min()
                col_data['Max'] = df[col].max()
                col_data['Mean'] = df[col].mean()
            else:
                most_common = df[col].mode()
                col_data['Most Common'] = most_common.iloc[0] if len(most_common) > 0 else 'N/A'

            col_info.append(col_data)

        info_df = pd.DataFrame(col_info)
        st.dataframe(info_df)

        # Quick analysis options
        st.markdown("### ⚡ Quick Analysis")

        analysis_cols = st.columns(3)

        with analysis_cols[0]:
            if st.button("📈 Generate Charts"):
                generate_quick_charts(df)

        with analysis_cols[1]:
            if st.button("📊 Statistical Summary"):
                show_statistical_summary(df)

        with analysis_cols[2]:
            if st.button("🔍 Data Quality Check"):
                perform_quality_check(df)

        # Download options
        st.markdown("### 💾 Export Options")

        export_cols = st.columns(3)

        with export_cols[0]:
            if st.button("📄 Export as CSV"):
                csv_data = df.to_csv(index=False)
                FileHandler.create_download_link(csv_data.encode(), f"{sheet_name}_export.csv", "text/csv")
                st.success("CSV export ready!")

        with export_cols[1]:
            if st.button("📋 Export as JSON"):
                json_data = df.to_json(orient='records', indent=2)
                FileHandler.create_download_link(json_data.encode(), f"{sheet_name}_export.json", "application/json")
                st.success("JSON export ready!")

        with export_cols[2]:
            if st.button("📊 Export Summary"):
                summary_data = info_df.to_csv(index=False)
                FileHandler.create_download_link(summary_data.encode(), f"{sheet_name}_summary.csv", "text/csv")
                st.success("Summary export ready!")

    except Exception as e:
        st.error(f"Error processing Excel file: {str(e)}")


def generate_quick_charts(df):
    """Generate quick charts for Excel data"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(numeric_cols) > 0:
        st.markdown("#### 📈 Numeric Data Visualization")

        # Select columns for visualization
        viz_cols = st.multiselect("Select columns to visualize:", numeric_cols,
                                  default=list(numeric_cols[:3]))

        if viz_cols:
            chart_type = st.selectbox("Chart Type:", ["Histogram", "Box Plot", "Line Chart", "Scatter Matrix"])

            if chart_type == "Histogram":
                fig, axes = plt.subplots(len(viz_cols), 1, figsize=(10, 4 * len(viz_cols)))
                if len(viz_cols) == 1:
                    axes = [axes]

                for i, col in enumerate(viz_cols):
                    if i < len(axes):
                        axes[i].hist(df[col].dropna(), bins=30, alpha=0.7)
                        axes[i].set_title(f'Distribution of {col}')
                        axes[i].set_xlabel(col)
                        axes[i].set_ylabel('Frequency')

                plt.tight_layout()
                st.pyplot()
                plt.close()

            elif chart_type == "Box Plot":
                fig, ax = plt.subplots(figsize=(12, 6))
                df[viz_cols].boxplot(ax=ax)
                plt.title('Box Plot Comparison')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot()
                plt.close()

            elif chart_type == "Line Chart":
                st.line_chart(df[viz_cols])

            elif chart_type == "Scatter Matrix" and len(viz_cols) > 1:
                from pandas.plotting import scatter_matrix
                fig, axes = plt.subplots(figsize=(12, 12))
                scatter_matrix(df[viz_cols], alpha=0.6, diagonal='hist', ax=axes)
                plt.tight_layout()
                st.pyplot()
                plt.close()

    # Categorical data visualization
    categorical_cols = df.select_dtypes(include=['object']).columns

    if len(categorical_cols) > 0:
        st.markdown("#### 📊 Categorical Data Visualization")

        cat_col = st.selectbox("Select categorical column:", categorical_cols)

        if cat_col:
            value_counts = df[cat_col].value_counts().head(20)

            if len(value_counts) > 0:
                st.bar_chart(value_counts)


def show_statistical_summary(df):
    """Show detailed statistical summary"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(numeric_cols) > 0:
        st.markdown("#### 📊 Descriptive Statistics")
        st.dataframe(df[numeric_cols].describe())

        if len(numeric_cols) > 1:
            st.markdown("#### 🔗 Correlation Analysis")
            corr_matrix = df[numeric_cols].corr()

            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
            plt.title('Correlation Matrix')
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()


def perform_quality_check(df):
    """Perform data quality assessment"""
    st.markdown("#### 🔍 Data Quality Assessment")

    # Missing values analysis
    missing_data = df.isnull().sum()
    missing_pct = (missing_data / len(df)) * 100

    quality_df = pd.DataFrame({
        'Column': missing_data.index,
        'Missing Count': missing_data.values,
        'Missing %': missing_pct.values
    })
    quality_df = quality_df[quality_df['Missing Count'] > 0].sort_values('Missing %', ascending=False)

    if len(quality_df) > 0:
        st.warning("⚠️ Columns with missing values:")
        st.dataframe(quality_df)
    else:
        st.success("✅ No missing values found!")

    # Duplicate rows
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        st.warning(f"⚠️ Found {duplicates} duplicate rows ({(duplicates / len(df) * 100):.1f}%)")
    else:
        st.success("✅ No duplicate rows found!")

    # Data type suggestions
    st.markdown("#### 💡 Data Type Suggestions")
    suggestions = []

    for col in df.columns:
        if df[col].dtype == 'object':
            # Check if it could be numeric
            try:
                pd.to_numeric(df[col], errors='raise')
                suggestions.append(f"Column '{col}' could be converted to numeric")
            except:
                # Check if it could be datetime
                try:
                    pd.to_datetime(df[col], errors='raise')
                    suggestions.append(f"Column '{col}' could be converted to datetime")
                except:
                    pass

    if suggestions:
        for suggestion in suggestions:
            st.info(f"💡 {suggestion}")
    else:
        st.success("✅ Data types look appropriate!")


def data_format_converter():
    """Advanced data format converter supporting multiple formats"""
    create_tool_header("Data Format Converter", "Convert between multiple data formats", "🔄")

    # Format selection
    col1, col2 = st.columns(2)

    with col1:
        input_format = st.selectbox("Input Format:", [
            "CSV", "Excel", "JSON", "XML", "Parquet", "TSV", "Fixed Width"
        ])

    with col2:
        output_format = st.selectbox("Output Format:", [
            "CSV", "Excel", "JSON", "XML", "Parquet", "TSV", "HTML", "LaTeX"
        ])

    if input_format == output_format:
        st.warning("⚠️ Input and output formats are the same!")
        return

    # File upload based on input format
    file_extensions = {
        "CSV": ['csv'], "Excel": ['xlsx', 'xls'], "JSON": ['json'],
        "XML": ['xml'], "Parquet": ['parquet'], "TSV": ['tsv', 'txt'],
        "Fixed Width": ['txt', 'dat']
    }

    uploaded_file = FileHandler.upload_files(file_extensions[input_format], accept_multiple=False)

    if uploaded_file:
        st.markdown("### ⚙️ Conversion Settings")

        # Input-specific settings
        input_settings = get_input_settings(input_format)

        # Output-specific settings
        output_settings = get_output_settings(output_format)

        if st.button("🔄 Convert Data"):
            convert_data_format(uploaded_file[0], input_format, output_format,
                                input_settings, output_settings)


def get_input_settings(input_format):
    """Get input-specific settings"""
    settings = {}

    if input_format == "CSV":
        col1, col2 = st.columns(2)
        with col1:
            settings['separator'] = st.text_input("Separator:", ",")
            settings['encoding'] = st.selectbox("Encoding:", ["utf-8", "latin-1", "cp1252"])
        with col2:
            settings['header'] = st.number_input("Header Row:", 0, 10, 0)
            settings['skip_rows'] = st.number_input("Skip Rows:", 0, 10, 0)

    elif input_format == "Excel":
        settings['sheet_name'] = st.text_input("Sheet Name (optional):", "")
        settings['header'] = st.number_input("Header Row:", 0, 10, 0)

    elif input_format == "JSON":
        settings['orient'] = st.selectbox("JSON Orientation:",
                                          ["records", "index", "values", "columns"])

    elif input_format == "Fixed Width":
        settings['widths'] = st.text_input("Column Widths (comma-separated):", "10,15,20")
        settings['names'] = st.text_input("Column Names (comma-separated):", "")

    return settings


def get_output_settings(output_format):
    """Get output-specific settings"""
    settings = {}

    if output_format == "CSV":
        col1, col2 = st.columns(2)
        with col1:
            settings['separator'] = st.text_input("Output Separator:", ",")
            settings['index'] = st.checkbox("Include Index", False)
        with col2:
            settings['encoding'] = st.selectbox("Output Encoding:", ["utf-8", "latin-1", "cp1252"])

    elif output_format == "Excel":
        settings['sheet_name'] = st.text_input("Output Sheet Name:", "Sheet1")
        settings['index'] = st.checkbox("Include Index", False)

    elif output_format == "JSON":
        settings['orient'] = st.selectbox("Output JSON Orientation:",
                                          ["records", "index", "values", "columns"])
        settings['indent'] = st.number_input("Indentation:", 0, 8, 2)

    elif output_format == "XML":
        settings['root_name'] = st.text_input("Root Element Name:", "data")
        settings['row_name'] = st.text_input("Row Element Name:", "row")

    return settings


def convert_data_format(uploaded_file, input_format, output_format, input_settings, output_settings):
    """Convert data between formats"""
    try:
        # Read input data
        df = read_input_data(uploaded_file, input_format, input_settings)

        if df is not None:
            st.markdown("### 📊 Data Preview")
            st.dataframe(df.head())

            st.markdown(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

            # Convert to output format
            output_data, filename, mime_type = convert_to_output(df, output_format, output_settings)

            if output_data:
                st.success(f"✅ Successfully converted to {output_format}!")

                # Show preview for text formats
                if output_format in ["CSV", "JSON", "XML", "HTML", "LaTeX"]:
                    preview = output_data[:1000] if isinstance(output_data, str) else str(output_data)[:1000]
                    st.text_area("Output Preview:", preview, height=200)

                # Create download link
                if isinstance(output_data, str):
                    FileHandler.create_download_link(output_data.encode(), filename, mime_type)
                else:
                    FileHandler.create_download_link(output_data, filename, mime_type)

    except Exception as e:
        st.error(f"Conversion error: {str(e)}")


def read_input_data(uploaded_file, input_format, settings):
    """Read data from various input formats"""
    try:
        if input_format == "CSV":
            sep = settings.get('separator', ',')
            encoding = settings.get('encoding', 'utf-8')
            header = settings.get('header', 0)
            skip_rows = settings.get('skip_rows', 0)

            df = pd.read_csv(uploaded_file, sep=sep, encoding=encoding,
                             header=header if header >= 0 else None,
                             skiprows=skip_rows if skip_rows > 0 else None)

        elif input_format == "Excel":
            sheet_name = settings.get('sheet_name', 0) or 0
            header = settings.get('header', 0)
            df = pd.read_excel(uploaded_file, sheet_name=sheet_name, header=header)

        elif input_format == "JSON":
            orient = settings.get('orient', 'records')
            df = pd.read_json(uploaded_file, orient=orient)

        elif input_format == "Parquet":
            df = pd.read_parquet(uploaded_file)

        elif input_format == "TSV":
            df = pd.read_csv(uploaded_file, sep='\t')

        elif input_format == "XML":
            # Basic XML reading (requires lxml)
            try:
                df = pd.read_xml(uploaded_file)
            except ImportError:
                st.error("XML support requires lxml package")
                return None

        elif input_format == "Fixed Width":
            widths_str = settings.get('widths', '10,15,20')
            widths = [int(w.strip()) for w in widths_str.split(',')]
            names_str = settings.get('names', '')
            names = [n.strip() for n in names_str.split(',')] if names_str else None

            df = pd.read_fwf(uploaded_file, widths=widths, names=names)

        return df

    except Exception as e:
        st.error(f"Error reading {input_format} file: {str(e)}")
        return None


def convert_to_output(df, output_format, settings):
    """Convert DataFrame to various output formats"""
    try:
        if output_format == "CSV":
            sep = settings.get('separator', ',')
            include_index = settings.get('index', False)
            encoding = settings.get('encoding', 'utf-8')

            output_data = df.to_csv(index=include_index, sep=sep, encoding=encoding)
            return output_data, "converted_data.csv", "text/csv"

        elif output_format == "Excel":
            sheet_name = settings.get('sheet_name', 'Sheet1')
            include_index = settings.get('index', False)

            # Create Excel file in memory
            import io
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=include_index)

            output_data = output.getvalue()
            return output_data, "converted_data.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        elif output_format == "JSON":
            orient = settings.get('orient', 'records')
            indent = settings.get('indent', 2)

            output_data = df.to_json(orient=orient, indent=indent)
            return output_data, "converted_data.json", "application/json"

        elif output_format == "Parquet":
            import io
            output = io.BytesIO()
            df.to_parquet(output, index=False)

            output_data = output.getvalue()
            return output_data, "converted_data.parquet", "application/octet-stream"

        elif output_format == "TSV":
            output_data = df.to_csv(index=False, sep='\t')
            return output_data, "converted_data.tsv", "text/tab-separated-values"

        elif output_format == "HTML":
            output_data = df.to_html(index=False, table_id="data_table", classes="table table-striped")
            return output_data, "converted_data.html", "text/html"

        elif output_format == "LaTeX":
            output_data = df.to_latex(index=False)
            return output_data, "converted_data.tex", "text/plain"

        elif output_format == "XML":
            root_name = settings.get('root_name', 'data')
            row_name = settings.get('row_name', 'row')

            try:
                output_data = df.to_xml(root_name=root_name, row_name=row_name)
                return output_data, "converted_data.xml", "application/xml"
            except AttributeError:
                st.error("XML output requires pandas >= 1.3.0")
                return None, None, None

    except Exception as e:
        st.error(f"Error converting to {output_format}: {str(e)}")
        return None, None, None


def database_connector():
    """Database connector tool for querying and analyzing database data"""
    create_tool_header("Database Connector", "Connect to databases and execute queries", "🗄️")

    # Database type selection
    db_type = st.selectbox("Database Type:", [
        "SQLite", "PostgreSQL", "MySQL", "SQL Server", "Custom Connection String"
    ])

    # Connection settings based on database type
    if db_type == "SQLite":
        st.markdown("### 📁 SQLite Database")
        uploaded_db = FileHandler.upload_files(['db', 'sqlite', 'sqlite3'], accept_multiple=False)

        if uploaded_db:
            connect_to_sqlite(uploaded_db[0])

    elif db_type == "Custom Connection String":
        st.markdown("### 🔗 Custom Connection")

        connection_string = st.text_input(
            "Connection String:",
            placeholder="sqlite:///database.db or postgresql://user:pass@host:port/db",
            type="password"
        )

        if connection_string and st.button("Connect to Database"):
            connect_to_custom_db(connection_string)

    else:
        st.markdown(f"### 🔗 {db_type} Connection")

        col1, col2 = st.columns(2)

        with col1:
            host = st.text_input("Host:", "localhost")
            port = st.number_input("Port:", 1, 65535, get_default_port(db_type))
            database = st.text_input("Database Name:")

        with col2:
            username = st.text_input("Username:")
            password = st.text_input("Password:", type="password")

        if all([host, database, username]) and st.button("Connect to Database"):
            connect_to_standard_db(db_type, host, port, database, username, password)


def get_default_port(db_type):
    """Get default port for database type"""
    ports = {
        "PostgreSQL": 5432,
        "MySQL": 3306,
        "SQL Server": 1433
    }
    return ports.get(db_type, 5432)


def connect_to_sqlite(uploaded_db):
    """Connect to SQLite database"""
    try:
        import sqlite3
        import tempfile
        import os

        # Save uploaded file to temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp_file:
            tmp_file.write(uploaded_db.getvalue())
            temp_path = tmp_file.name

        # Connect to database
        conn = sqlite3.connect(temp_path)

        st.success("✅ Connected to SQLite database!")

        # Get table list
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]

        if tables:
            st.markdown("### 📋 Available Tables")

            selected_table = st.selectbox("Select Table:", tables)

            if selected_table:
                show_table_info(conn, selected_table)

            # Custom query interface
            st.markdown("### 💻 Custom Query")

            query = st.text_area(
                "SQL Query:",
                f"SELECT * FROM {selected_table} LIMIT 100;" if selected_table else "SELECT * FROM table_name LIMIT 100;",
                height=100
            )

            if st.button("Execute Query") and query.strip():
                execute_database_query(conn, query)
        else:
            st.warning("No tables found in the database")

        # Cleanup
        conn.close()
        os.unlink(temp_path)

    except Exception as e:
        st.error(f"Error connecting to SQLite database: {str(e)}")


def connect_to_custom_db(connection_string):
    """Connect to database using custom connection string"""
    try:
        import sqlalchemy as sa

        engine = sa.create_engine(connection_string)

        # Test connection
        with engine.connect() as conn:
            st.success("✅ Connected to database!")

            # Get tables
            inspector = sa.inspect(engine)
            tables = inspector.get_table_names()

            if tables:
                st.markdown("### 📋 Available Tables")

                selected_table = st.selectbox("Select Table:", tables)

                if selected_table:
                    show_table_info_sqlalchemy(engine, selected_table)

                # Custom query interface
                st.markdown("### 💻 Custom Query")

                query = st.text_area(
                    "SQL Query:",
                    f"SELECT * FROM {selected_table} LIMIT 100;" if selected_table else "SELECT * FROM table_name LIMIT 100;",
                    height=100
                )

                if st.button("Execute Query") and query.strip():
                    execute_sqlalchemy_query(engine, query)
            else:
                st.warning("No tables found in the database")

    except ImportError:
        st.error("SQLAlchemy is required for database connections. Please install it first.")
    except Exception as e:
        st.error(f"Error connecting to database: {str(e)}")


def connect_to_standard_db(db_type, host, port, database, username, password):
    """Connect to standard database types"""
    try:
        import sqlalchemy as sa

        # Build connection string
        if db_type == "PostgreSQL":
            connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"
        elif db_type == "MySQL":
            connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        elif db_type == "SQL Server":
            connection_string = f"mssql+pyodbc://{username}:{password}@{host}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

        engine = sa.create_engine(connection_string)

        # Test connection
        with engine.connect() as conn:
            st.success(f"✅ Connected to {db_type} database!")

            # Get tables
            inspector = sa.inspect(engine)
            tables = inspector.get_table_names()

            if tables:
                st.markdown("### 📋 Available Tables")

                selected_table = st.selectbox("Select Table:", tables)

                if selected_table:
                    show_table_info_sqlalchemy(engine, selected_table)

                # Custom query interface
                st.markdown("### 💻 Custom Query")

                query = st.text_area(
                    "SQL Query:",
                    f"SELECT * FROM {selected_table} LIMIT 100;" if selected_table else "SELECT * FROM table_name LIMIT 100;",
                    height=100
                )

                if st.button("Execute Query") and query.strip():
                    execute_sqlalchemy_query(engine, query)
            else:
                st.warning("No tables found in the database")

    except ImportError:
        st.error(f"Required packages for {db_type} are not installed. Please install the appropriate drivers.")
    except Exception as e:
        st.error(f"Error connecting to {db_type} database: {str(e)}")


def show_table_info(conn, table_name):
    """Show table information for SQLite"""
    try:
        # Get column info
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        st.markdown(f"#### 📊 Table: {table_name}")

        # Column information
        col_df = pd.DataFrame(columns, columns=['ID', 'Name', 'Type', 'NotNull', 'DefaultValue', 'PrimaryKey'])
        st.dataframe(col_df)

        # Row count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        row_count = cursor.fetchone()[0]
        st.metric("Total Rows", row_count)

        # Sample data
        if st.button(f"Preview {table_name}"):
            df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 10;", conn)
            st.dataframe(df)

    except Exception as e:
        st.error(f"Error getting table info: {str(e)}")


def show_table_info_sqlalchemy(engine, table_name):
    """Show table information using SQLAlchemy"""
    try:
        import sqlalchemy as sa

        inspector = sa.inspect(engine)
        columns = inspector.get_columns(table_name)

        st.markdown(f"#### 📊 Table: {table_name}")

        # Column information
        col_data = []
        for col in columns:
            col_data.append({
                'Name': col['name'],
                'Type': str(col['type']),
                'Nullable': col['nullable'],
                'Default': col.get('default', None)
            })

        col_df = pd.DataFrame(col_data)
        st.dataframe(col_df)

        # Sample data
        if st.button(f"Preview {table_name}"):
            df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 10;", engine)
            st.dataframe(df)

    except Exception as e:
        st.error(f"Error getting table info: {str(e)}")


def execute_database_query(conn, query):
    """Execute database query for SQLite"""
    try:
        df = pd.read_sql_query(query, conn)

        st.markdown("### 📊 Query Results")

        if len(df) > 0:
            st.dataframe(df)

            # Basic analysis for numeric data
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                st.markdown("#### 📈 Quick Analysis")

                analysis_type = st.selectbox("Analysis Type:", [
                    "Summary Statistics", "Data Visualization", "Export Data"
                ])

                if analysis_type == "Summary Statistics":
                    st.dataframe(df[numeric_cols].describe())

                elif analysis_type == "Data Visualization" and len(numeric_cols) > 0:
                    viz_col = st.selectbox("Select column to visualize:", numeric_cols)
                    chart_type = st.selectbox("Chart type:", ["Histogram", "Box Plot", "Line Chart"])

                    if chart_type == "Histogram":
                        st.bar_chart(df[viz_col].value_counts().head(20))
                    elif chart_type == "Box Plot":
                        fig, ax = plt.subplots()
                        ax.boxplot(df[viz_col].dropna())
                        ax.set_ylabel(viz_col)
                        st.pyplot()
                        plt.close()
                    elif chart_type == "Line Chart":
                        st.line_chart(df[viz_col])

                elif analysis_type == "Export Data":
                    # Export options
                    export_cols = st.columns(2)

                    with export_cols[0]:
                        if st.button("📄 Export as CSV"):
                            csv_data = df.to_csv(index=False)
                            FileHandler.create_download_link(csv_data.encode(), "query_results.csv", "text/csv")
                            st.success("CSV export ready!")

                    with export_cols[1]:
                        if st.button("📋 Export as JSON"):
                            json_data = df.to_json(orient='records', indent=2)
                            FileHandler.create_download_link(json_data.encode(), "query_results.json",
                                                             "application/json")
                            st.success("JSON export ready!")
        else:
            st.info("Query executed successfully but returned no results.")

    except Exception as e:
        st.error(f"Error executing query: {str(e)}")


def execute_sqlalchemy_query(engine, query):
    """Execute database query using SQLAlchemy"""
    try:
        df = pd.read_sql_query(query, engine)

        st.markdown("### 📊 Query Results")

        if len(df) > 0:
            st.dataframe(df)

            # Basic analysis for numeric data
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                st.markdown("#### 📈 Quick Analysis")

                analysis_type = st.selectbox("Analysis Type:", [
                    "Summary Statistics", "Data Visualization", "Export Data"
                ])

                if analysis_type == "Summary Statistics":
                    st.dataframe(df[numeric_cols].describe())

                elif analysis_type == "Data Visualization" and len(numeric_cols) > 0:
                    viz_col = st.selectbox("Select column to visualize:", numeric_cols)
                    chart_type = st.selectbox("Chart type:", ["Histogram", "Box Plot", "Line Chart"])

                    if chart_type == "Histogram":
                        st.bar_chart(df[viz_col].value_counts().head(20))
                    elif chart_type == "Box Plot":
                        fig, ax = plt.subplots()
                        ax.boxplot(df[viz_col].dropna())
                        ax.set_ylabel(viz_col)
                        st.pyplot()
                        plt.close()
                    elif chart_type == "Line Chart":
                        st.line_chart(df[viz_col])

                elif analysis_type == "Export Data":
                    # Export options
                    export_cols = st.columns(2)

                    with export_cols[0]:
                        if st.button("📄 Export as CSV"):
                            csv_data = df.to_csv(index=False)
                            FileHandler.create_download_link(csv_data.encode(), "query_results.csv", "text/csv")
                            st.success("CSV export ready!")

                    with export_cols[1]:
                        if st.button("📋 Export as JSON"):
                            json_data = df.to_json(orient='records', indent=2)
                            FileHandler.create_download_link(json_data.encode(), "query_results.json",
                                                             "application/json")
                            st.success("JSON export ready!")
        else:
            st.info("Query executed successfully but returned no results.")

    except Exception as e:
        st.error(f"Error executing query: {str(e)}")


def duplicate_remover():
    """Remove duplicate rows from dataset"""
    create_tool_header("Duplicate Remover", "Detect and remove duplicate rows from your data", "🔄")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Show initial statistics
            st.markdown("### 📊 Dataset Overview")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Rows", len(df))
            with col2:
                duplicates = df.duplicated().sum()
                st.metric("Duplicate Rows", duplicates)
            with col3:
                unique_pct = ((len(df) - duplicates) / len(df)) * 100
                st.metric("Unique %", f"{unique_pct:.1f}%")

            if duplicates > 0:
                st.warning(f"⚠️ Found {duplicates} duplicate rows ({(duplicates / len(df) * 100):.1f}% of data)")

                # Duplicate detection options
                st.markdown("### ⚙️ Duplicate Detection Options")

                col1, col2 = st.columns(2)

                with col1:
                    subset_option = st.selectbox("Check duplicates based on:", [
                        "All columns", "Selected columns", "First few columns"
                    ])

                    keep_option = st.selectbox("Keep which duplicate:", [
                        "First occurrence", "Last occurrence", "None (remove all)"
                    ])

                with col2:
                    if subset_option == "Selected columns":
                        selected_cols = st.multiselect("Select columns to check:", df.columns.tolist())
                    elif subset_option == "First few columns":
                        num_cols = st.slider("Number of columns:", 1, len(df.columns), min(5, len(df.columns)))
                        selected_cols = df.columns[:num_cols].tolist()
                    else:
                        selected_cols = None

                    case_sensitive = st.checkbox("Case sensitive (for text columns)", value=True)

                # Show duplicate analysis
                if st.button("🔍 Analyze Duplicates"):
                    analyze_duplicates(df, selected_cols, case_sensitive)

                # Remove duplicates
                if st.button("🗑️ Remove Duplicates"):
                    remove_duplicates(df, selected_cols, keep_option, case_sensitive)

            else:
                st.success("✅ No duplicate rows found in your dataset!")

                # Still offer column-specific duplicate analysis
                st.markdown("### 🔍 Column-Specific Duplicate Analysis")

                col = st.selectbox("Analyze duplicates in specific column:", df.columns.tolist())

                if st.button("Analyze Column Duplicates"):
                    analyze_column_duplicates(df, col)


def analyze_duplicates(df, subset_cols, case_sensitive):
    """Analyze duplicate rows in detail"""
    try:
        # Prepare data for duplicate detection
        if subset_cols:
            check_df = df[subset_cols].copy()
        else:
            check_df = df.copy()

        # Handle case sensitivity for text columns
        if not case_sensitive:
            for col in check_df.columns:
                if check_df[col].dtype == 'object':
                    check_df[col] = check_df[col].astype(str).str.lower()

        # Find duplicates
        duplicated_mask = check_df.duplicated(keep=False)
        duplicate_rows = df[duplicated_mask]

        if len(duplicate_rows) > 0:
            st.markdown("### 🔍 Duplicate Analysis Results")

            # Summary statistics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Duplicate Rows", len(duplicate_rows))
            with col2:
                unique_groups = check_df[duplicated_mask].drop_duplicates().shape[0]
                st.metric("Unique Duplicate Groups", unique_groups)
            with col3:
                avg_duplicates = len(duplicate_rows) / unique_groups if unique_groups > 0 else 0
                st.metric("Avg Duplicates per Group", f"{avg_duplicates:.1f}")

            # Show sample duplicate groups
            st.markdown("#### 📝 Sample Duplicate Groups")

            # Group duplicates and show examples
            grouped = []
            seen_groups = set()

            for idx, row in check_df[duplicated_mask].iterrows():
                row_tuple = tuple(row.values)
                if row_tuple not in seen_groups:
                    seen_groups.add(row_tuple)
                    group_mask = (check_df == row).all(axis=1)
                    group_df = df[group_mask]
                    grouped.append(group_df)

                    if len(grouped) >= 5:  # Show max 5 groups
                        break

            for i, group in enumerate(grouped, 1):
                st.markdown(f"**Group {i}:**")
                st.dataframe(group)

            if len(grouped) < unique_groups:
                st.info(f"Showing {len(grouped)} of {unique_groups} duplicate groups")
        else:
            st.success("✅ No duplicates found with current settings!")

    except Exception as e:
        st.error(f"Error analyzing duplicates: {str(e)}")


def remove_duplicates(df, subset_cols, keep_option, case_sensitive):
    """Remove duplicate rows from dataframe"""
    try:
        # Prepare data for duplicate detection
        original_len = len(df)

        if subset_cols:
            subset = subset_cols
        else:
            subset = None

        # Map keep option
        keep_map = {
            "First occurrence": "first",
            "Last occurrence": "last",
            "None (remove all)": False
        }
        keep_value = keep_map[keep_option]

        # Handle case sensitivity
        work_df = df.copy()
        if not case_sensitive and subset:
            for col in subset:
                if work_df[col].dtype == 'object':
                    work_df[col] = work_df[col].astype(str).str.lower()

        # Remove duplicates
        if not case_sensitive and subset:
            # Need to identify duplicates based on modified data but remove from original
            duplicated_mask = work_df.duplicated(subset=subset, keep=keep_value)
            cleaned_df = df[~duplicated_mask].copy()
        else:
            cleaned_df = df.drop_duplicates(subset=subset, keep=keep_value)

        removed_count = original_len - len(cleaned_df)

        st.markdown("### ✅ Duplicate Removal Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Original Rows", original_len)
        with col2:
            st.metric("Rows Removed", removed_count)
        with col3:
            st.metric("Final Rows", len(cleaned_df))

        if removed_count > 0:
            st.success(f"✅ Successfully removed {removed_count} duplicate rows!")

            # Show cleaned data preview
            st.markdown("#### 📋 Cleaned Data Preview")
            st.dataframe(cleaned_df.head(10))

            # Download options
            st.markdown("#### 💾 Download Cleaned Data")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("📄 Download as CSV"):
                    csv_data = cleaned_df.to_csv(index=False)
                    FileHandler.create_download_link(csv_data.encode(), "cleaned_data.csv", "text/csv")
                    st.success("CSV download ready!")

            with col2:
                if st.button("📊 Download as Excel"):
                    import io
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        cleaned_df.to_excel(writer, sheet_name='CleanedData', index=False)

                    excel_data = output.getvalue()
                    FileHandler.create_download_link(excel_data, "cleaned_data.xlsx",
                                                     "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                    st.success("Excel download ready!")
        else:
            st.info("No duplicates were removed.")

    except Exception as e:
        st.error(f"Error removing duplicates: {str(e)}")


def analyze_column_duplicates(df, column):
    """Analyze duplicates in a specific column"""
    try:
        col_data = df[column]

        # Basic statistics
        total_values = len(col_data)
        unique_values = col_data.nunique()
        duplicate_values = total_values - unique_values

        st.markdown(f"### 📊 Column '{column}' Duplicate Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Values", total_values)
        with col2:
            st.metric("Unique Values", unique_values)
        with col3:
            st.metric("Duplicate Values", duplicate_values)

        if duplicate_values > 0:
            # Show most frequent duplicates
            value_counts = col_data.value_counts()
            duplicated_values = value_counts[value_counts > 1]

            st.markdown("#### 🔍 Most Frequent Duplicate Values")
            st.dataframe(duplicated_values.head(20))

            # Show rows with most common duplicate
            most_common = duplicated_values.index[0]
            st.markdown(f"#### 📝 Rows with most common duplicate value: '{most_common}'")
            matching_rows = df[df[column] == most_common]
            st.dataframe(matching_rows)
        else:
            st.success(f"✅ No duplicate values found in column '{column}'!")

    except Exception as e:
        st.error(f"Error analyzing column duplicates: {str(e)}")


def data_type_converter():
    """Convert data types with automatic detection and suggestions"""
    create_tool_header("Data Type Converter", "Convert and optimize data types automatically", "🔄")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Show current data types
            st.markdown("### 📋 Current Data Types")

            # Create detailed type information
            type_info = analyze_current_types(df)
            st.dataframe(type_info)

            # Automatic type suggestions
            st.markdown("### 💡 Type Conversion Suggestions")

            suggestions = generate_type_suggestions(df)

            if suggestions:
                st.markdown("#### 🎯 Recommended Conversions")

                for suggestion in suggestions:
                    if suggestion['confidence'] == 'High':
                        st.success(f"✅ {suggestion['message']}")
                    elif suggestion['confidence'] == 'Medium':
                        st.info(f"ℹ️ {suggestion['message']}")
                    else:
                        st.warning(f"⚠️ {suggestion['message']}")

                # Apply automatic conversions
                if st.button("🚀 Apply Recommended Conversions"):
                    apply_automatic_conversions(df, suggestions)
            else:
                st.success("✅ Data types are already optimized!")

            # Manual conversion interface
            st.markdown("### ⚙️ Manual Type Conversion")

            col1, col2 = st.columns(2)

            with col1:
                selected_column = st.selectbox("Select Column:", df.columns.tolist())

            with col2:
                target_type = st.selectbox("Convert to:", [
                    "int64", "float64", "object", "datetime64", "bool", "category", "string"
                ])

            # Conversion options
            st.markdown("#### 🔧 Conversion Options")

            error_handling = st.selectbox("Error Handling:", [
                "coerce (convert invalid to NaN)",
                "raise (stop on error)",
                "ignore (keep original)"
            ])

            if target_type == "datetime64":
                date_format = st.text_input("Date Format (optional):", placeholder="%Y-%m-%d")
            else:
                date_format = None

            if st.button("🔄 Convert Column"):
                convert_column_type(df, selected_column, target_type, error_handling, date_format)


def analyze_current_types(df):
    """Analyze current data types and provide detailed information"""
    type_info = []

    for col in df.columns:
        col_data = df[col]

        info = {
            'Column': col,
            'Current Type': str(col_data.dtype),
            'Non-Null Count': col_data.count(),
            'Null Count': col_data.isnull().sum(),
            'Memory Usage (bytes)': col_data.memory_usage(deep=True),
            'Unique Values': col_data.nunique()
        }

        # Add type-specific information
        if pd.api.types.is_numeric_dtype(col_data):
            info['Min'] = col_data.min()
            info['Max'] = col_data.max()
        elif col_data.dtype == 'object':
            # Check if it could be numeric or datetime
            sample = col_data.dropna().head(100)
            if len(sample) > 0:
                # Test numeric conversion
                try:
                    pd.to_numeric(sample, errors='raise')
                    info['Convertible to'] = 'Numeric'
                except:
                    # Test datetime conversion
                    try:
                        pd.to_datetime(sample, errors='raise')
                        info['Convertible to'] = 'Datetime'
                    except:
                        info['Convertible to'] = 'Keep as Text'

        type_info.append(info)

    return pd.DataFrame(type_info)


def generate_type_suggestions(df):
    """Generate automatic type conversion suggestions"""
    suggestions = []

    for col in df.columns:
        col_data = df[col]

        # Skip if already optimal type
        if col_data.dtype in ['int64', 'float64', 'bool', 'datetime64[ns]']:
            continue

        # Object columns that could be optimized
        if col_data.dtype == 'object':
            # Check for numeric conversion
            non_null_data = col_data.dropna()
            if len(non_null_data) > 0:
                # Test numeric conversion
                try:
                    numeric_data = pd.to_numeric(non_null_data, errors='raise')

                    # Check if integers
                    if all(numeric_data == numeric_data.astype(int)):
                        suggestions.append({
                            'column': col,
                            'from_type': 'object',
                            'to_type': 'int64',
                            'confidence': 'High',
                            'message': f"Column '{col}' contains integers stored as text → convert to int64"
                        })
                    else:
                        suggestions.append({
                            'column': col,
                            'from_type': 'object',
                            'to_type': 'float64',
                            'confidence': 'High',
                            'message': f"Column '{col}' contains numbers stored as text → convert to float64"
                        })

                except ValueError:
                    # Test datetime conversion
                    try:
                        pd.to_datetime(non_null_data, errors='raise')
                        suggestions.append({
                            'column': col,
                            'from_type': 'object',
                            'to_type': 'datetime64',
                            'confidence': 'High',
                            'message': f"Column '{col}' contains dates stored as text → convert to datetime"
                        })
                    except:
                        # Check for categorical
                        if col_data.nunique() < len(col_data) * 0.5:  # Less than 50% unique
                            suggestions.append({
                                'column': col,
                                'from_type': 'object',
                                'to_type': 'category',
                                'confidence': 'Medium',
                                'message': f"Column '{col}' has repeated values → consider converting to category for memory efficiency"
                            })

        # Large integer columns that could use smaller types
        elif col_data.dtype == 'int64':
            min_val, max_val = col_data.min(), col_data.max()

            if -128 <= min_val and max_val <= 127:
                suggestions.append({
                    'column': col,
                    'from_type': 'int64',
                    'to_type': 'int8',
                    'confidence': 'Medium',
                    'message': f"Column '{col}' values fit in int8 → reduce memory usage"
                })
            elif -32768 <= min_val and max_val <= 32767:
                suggestions.append({
                    'column': col,
                    'from_type': 'int64',
                    'to_type': 'int16',
                    'confidence': 'Medium',
                    'message': f"Column '{col}' values fit in int16 → reduce memory usage"
                })
            elif -2147483648 <= min_val and max_val <= 2147483647:
                suggestions.append({
                    'column': col,
                    'from_type': 'int64',
                    'to_type': 'int32',
                    'confidence': 'Medium',
                    'message': f"Column '{col}' values fit in int32 → reduce memory usage"
                })

        # Float columns with no decimals
        elif col_data.dtype == 'float64':
            if col_data.dropna().apply(lambda x: x.is_integer()).all():
                suggestions.append({
                    'column': col,
                    'from_type': 'float64',
                    'to_type': 'int64',
                    'confidence': 'High',
                    'message': f"Column '{col}' contains only whole numbers → convert to int64"
                })

    return suggestions


def outlier_detector():
    """Detect outliers using multiple methods"""
    create_tool_header("Outlier Detector", "Detect and analyze outliers in your data", "🎯")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Get numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(numeric_cols) == 0:
                st.error("No numeric columns found for outlier detection!")
                return

            # Column selection
            st.markdown("### 📊 Column Selection")

            if len(numeric_cols) > 1:
                selected_cols = st.multiselect(
                    "Select columns for outlier detection:",
                    numeric_cols,
                    default=numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols
                )
            else:
                selected_cols = numeric_cols
                st.info(f"Using column: {numeric_cols[0]}")

            if not selected_cols:
                st.warning("Please select at least one column.")
                return

            # Detection method selection
            st.markdown("### ⚙️ Detection Methods")

            col1, col2 = st.columns(2)

            with col1:
                methods = st.multiselect("Select detection methods:", [
                    "IQR (Interquartile Range)",
                    "Z-Score",
                    "Modified Z-Score"
                ], default=["IQR (Interquartile Range)", "Z-Score"])

            with col2:
                # Method-specific parameters
                if "Z-Score" in methods:
                    z_threshold = st.slider("Z-Score Threshold:", 1.0, 5.0, 3.0, 0.1)
                else:
                    z_threshold = 3.0

                if "Modified Z-Score" in methods:
                    mad_threshold = st.slider("Modified Z-Score Threshold:", 1.0, 5.0, 3.5, 0.1)
                else:
                    mad_threshold = 3.5

            if st.button("🔍 Detect Outliers"):
                detect_outliers_comprehensive(df, selected_cols, methods, z_threshold, mad_threshold)


def detect_outliers_comprehensive(df, columns, methods, z_threshold, mad_threshold):
    """Comprehensive outlier detection using multiple methods"""
    try:
        outlier_results = {}

        for col in columns:
            data = df[col].dropna()
            col_outliers = {}

            # IQR Method
            if "IQR (Interquartile Range)" in methods:
                Q1 = data.quantile(0.25)
                Q3 = data.quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                iqr_outliers = data[(data < lower_bound) | (data > upper_bound)]
                col_outliers['IQR'] = {
                    'outliers': iqr_outliers.index.tolist(),
                    'count': len(iqr_outliers),
                    'lower_bound': lower_bound,
                    'upper_bound': upper_bound
                }

            # Z-Score Method
            if "Z-Score" in methods:
                mean = data.mean()
                std = data.std()
                z_scores = np.abs((data - mean) / std)

                z_outliers = data[z_scores > z_threshold]
                col_outliers['Z-Score'] = {
                    'outliers': z_outliers.index.tolist(),
                    'count': len(z_outliers),
                    'threshold': z_threshold
                }

            # Modified Z-Score Method
            if "Modified Z-Score" in methods:
                median = data.median()
                mad = np.median(np.abs(data - median))
                modified_z_scores = 0.6745 * (data - median) / mad

                mad_outliers = data[np.abs(modified_z_scores) > mad_threshold]
                col_outliers['Modified Z-Score'] = {
                    'outliers': mad_outliers.index.tolist(),
                    'count': len(mad_outliers),
                    'threshold': mad_threshold
                }

            outlier_results[col] = col_outliers

        # Display results
        display_outlier_results(df, outlier_results, columns, methods)

    except Exception as e:
        st.error(f"Error detecting outliers: {str(e)}")


def display_outlier_results(df, outlier_results, columns, methods):
    """Display comprehensive outlier detection results"""
    st.markdown("### 🎯 Outlier Detection Results")

    # Summary table
    summary_data = []
    for col in columns:
        row = {'Column': col}
        for method in methods:
            method_key = method
            if method_key in outlier_results[col]:
                count = outlier_results[col][method_key]['count']
                percentage = (count / len(df)) * 100
                row[f'{method} Count'] = count
                row[f'{method} %'] = f"{percentage:.1f}%"
            else:
                row[f'{method} Count'] = 0
                row[f'{method} %'] = "0.0%"
        summary_data.append(row)

    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df)

    # Detailed analysis for each column
    for col in columns:
        st.markdown(f"#### 📊 Column: {col}")

        col_data = df[col].dropna()

        # Basic statistics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Mean", f"{col_data.mean():.2f}")
        with col2:
            st.metric("Median", f"{col_data.median():.2f}")
        with col3:
            st.metric("Std Dev", f"{col_data.std():.2f}")
        with col4:
            st.metric("Range", f"{col_data.max() - col_data.min():.2f}")

        # Visualization
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # Box plot
        axes[0].boxplot(col_data)
        axes[0].set_title(f'Box Plot: {col}')
        axes[0].set_ylabel(col)

        # Histogram
        axes[1].hist(col_data, bins=30, alpha=0.7, edgecolor='black')
        axes[1].set_title(f'Distribution: {col}')
        axes[1].set_xlabel(col)
        axes[1].set_ylabel('Frequency')

        plt.tight_layout()
        st.pyplot()
        plt.close()

        # Show outliers for each method
        for method in methods:
            if method in outlier_results[col] and outlier_results[col][method]['count'] > 0:
                st.markdown(f"**{method} Outliers:**")

                outlier_indices = outlier_results[col][method]['outliers']
                outlier_rows = df.loc[outlier_indices]

                # Show outlier values
                st.dataframe(outlier_rows[[col]].head(10))

                if len(outlier_rows) > 10:
                    st.info(f"Showing first 10 of {len(outlier_rows)} outliers")

    # Export options
    st.markdown("### 💾 Export Outlier Analysis")

    if st.button("📊 Export Outlier Report"):
        export_outlier_report(df, outlier_results, columns, methods)


def export_outlier_report(df, outlier_results, columns, methods):
    """Export comprehensive outlier analysis report"""
    try:
        # Create summary report
        report_data = []

        for col in columns:
            for method in methods:
                if method in outlier_results[col]:
                    result = outlier_results[col][method]

                    for outlier_idx in result['outliers']:
                        report_data.append({
                            'Column': col,
                            'Method': method,
                            'Row_Index': outlier_idx,
                            'Value': df.loc[outlier_idx, col],
                            'Outlier_Count_This_Method': result['count']
                        })

        if report_data:
            report_df = pd.DataFrame(report_data)

            # Export as CSV
            csv_data = report_df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "outlier_analysis_report.csv", "text/csv")
            st.success("📊 Outlier analysis report ready for download!")
        else:
            st.info("No outliers found to export.")

    except Exception as e:
        st.error(f"Error exporting outlier report: {str(e)}")


def data_profiling():
    """Comprehensive data profiling and quality assessment"""
    create_tool_header("Data Profiling", "Comprehensive analysis of data quality and characteristics", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            if st.button("🔍 Generate Data Profile"):
                generate_comprehensive_profile(df)


def generate_comprehensive_profile(df):
    """Generate comprehensive data profile"""
    try:
        # Dataset Overview
        st.markdown("### 📊 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Rows", f"{len(df):,}")
        with col2:
            st.metric("Columns", len(df.columns))
        with col3:
            memory_usage = df.memory_usage(deep=True).sum() / 1024 ** 2
            st.metric("Memory (MB)", f"{memory_usage:.2f}")
        with col4:
            missing_cells = df.isnull().sum().sum()
            total_cells = len(df) * len(df.columns)
            completeness = ((total_cells - missing_cells) / total_cells) * 100
            st.metric("Completeness", f"{completeness:.1f}%")

        # Data Quality Score
        quality_score = calculate_comprehensive_quality_score(df)

        if quality_score >= 90:
            st.success(f"✅ Excellent Data Quality: {quality_score:.1f}/100")
        elif quality_score >= 75:
            st.info(f"ℹ️ Good Data Quality: {quality_score:.1f}/100")
        elif quality_score >= 60:
            st.warning(f"⚠️ Fair Data Quality: {quality_score:.1f}/100")
        else:
            st.error(f"❌ Poor Data Quality: {quality_score:.1f}/100")

        # Column-by-Column Analysis
        st.markdown("### 📋 Column Analysis")

        profile_data = []

        for col in df.columns:
            col_data = df[col]

            # Basic stats
            profile = {
                'Column': col,
                'Type': str(col_data.dtype),
                'Count': col_data.count(),
                'Missing': col_data.isnull().sum(),
                'Missing %': (col_data.isnull().sum() / len(df)) * 100,
                'Unique': col_data.nunique(),
                'Unique %': (col_data.nunique() / len(df)) * 100
            }

            # Type-specific analysis
            if pd.api.types.is_numeric_dtype(col_data):
                profile.update({
                    'Min': col_data.min(),
                    'Max': col_data.max(),
                    'Mean': col_data.mean(),
                    'Median': col_data.median(),
                    'Std': col_data.std(),
                    'Skewness': col_data.skew()
                })

                # Detect potential issues
                issues = []
                if col_data.min() == col_data.max():
                    issues.append("Constant values")
                if abs(col_data.skew()) > 2:
                    issues.append("Highly skewed")
                if (col_data < 0).any() and col.lower() in ['age', 'count', 'quantity', 'amount', 'price']:
                    issues.append("Negative values in non-negative field")

                profile['Issues'] = ', '.join(issues) if issues else 'None'

            elif col_data.dtype == 'object':
                # Text analysis
                non_null = col_data.dropna()
                if len(non_null) > 0:
                    avg_length = non_null.astype(str).str.len().mean()
                    profile['Avg Length'] = f"{avg_length:.1f}"

                    # Most common value
                    mode_val = col_data.mode()
                    if len(mode_val) > 0:
                        profile['Most Common'] = str(mode_val.iloc[0])[:50]
                        mode_freq = (col_data == mode_val.iloc[0]).sum()
                        profile['Mode Frequency'] = f"{mode_freq} ({(mode_freq / len(df) * 100):.1f}%)"

                    # Check for potential data type issues
                    issues = []
                    try:
                        pd.to_numeric(non_null.head(100), errors='raise')
                        issues.append("Could be numeric")
                    except:
                        try:
                            pd.to_datetime(non_null.head(100), errors='raise')
                            issues.append("Could be datetime")
                        except:
                            pass

                    if col_data.nunique() < len(col_data) * 0.1:
                        issues.append("Low cardinality - consider category")

                    profile['Suggestions'] = ', '.join(issues) if issues else 'None'

            profile_data.append(profile)

        # Display profile table
        profile_df = pd.DataFrame(profile_data)
        st.dataframe(profile_df, use_container_width=True)

        # Data Type Distribution
        st.markdown("### 📊 Data Type Distribution")

        type_counts = df.dtypes.value_counts()
        col1, col2 = st.columns(2)

        with col1:
            st.bar_chart(type_counts)

        with col2:
            st.markdown("**Data Type Summary:**")
            for dtype, count in type_counts.items():
                percentage = (count / len(df.columns)) * 100
                st.write(f"- {dtype}: {count} columns ({percentage:.1f}%)")

        # Missing Data Pattern Analysis
        st.markdown("### 🕳️ Missing Data Patterns")

        missing_summary = df.isnull().sum()
        columns_with_missing = missing_summary[missing_summary > 0]

        if len(columns_with_missing) > 0:
            st.warning(f"⚠️ {len(columns_with_missing)} columns have missing data")

            # Missing data heatmap visualization
            if len(columns_with_missing) <= 20:  # Only show for reasonable number of columns
                missing_df = df[columns_with_missing.index].isnull()

                if len(missing_df.columns) > 1:
                    # Create correlation matrix of missing data patterns
                    missing_corr = missing_df.corr()

                    fig, ax = plt.subplots(figsize=(10, 8))
                    sns.heatmap(missing_corr, annot=True, cmap='coolwarm', center=0, ax=ax)
                    plt.title('Missing Data Pattern Correlations')
                    plt.tight_layout()
                    st.pyplot()
                    plt.close()

            # Missing data summary table
            missing_analysis = pd.DataFrame({
                'Column': columns_with_missing.index,
                'Missing Count': columns_with_missing.values,
                'Missing %': (columns_with_missing.values / len(df)) * 100
            }).sort_values('Missing %', ascending=False)

            st.dataframe(missing_analysis)
        else:
            st.success("✅ No missing data found!")

        # Duplicate Analysis
        st.markdown("### 🔄 Duplicate Analysis")

        total_duplicates = df.duplicated().sum()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Duplicates", total_duplicates)
        with col2:
            dup_percentage = (total_duplicates / len(df)) * 100
            st.metric("Duplicate %", f"{dup_percentage:.1f}%")
        with col3:
            unique_rows = len(df) - total_duplicates
            st.metric("Unique Rows", unique_rows)

        if total_duplicates > 0:
            st.warning(f"⚠️ Found {total_duplicates} duplicate rows")
        else:
            st.success("✅ No duplicate rows found")

        # Column-specific duplicate analysis
        st.markdown("#### Column-Specific Duplicates")

        col_duplicate_data = []
        for col in df.columns:
            col_data = df[col]
            total_vals = len(col_data)
            unique_vals = col_data.nunique()
            duplicated_vals = total_vals - unique_vals

            col_duplicate_data.append({
                'Column': col,
                'Total Values': total_vals,
                'Unique Values': unique_vals,
                'Duplicated Values': duplicated_vals,
                'Duplicate %': (duplicated_vals / total_vals) * 100
            })

        dup_df = pd.DataFrame(col_duplicate_data)
        dup_df = dup_df.sort_values('Duplicate %', ascending=False)
        st.dataframe(dup_df)

        # Data Quality Recommendations
        st.markdown("### 💡 Data Quality Recommendations")

        recommendations = generate_quality_recommendations(df, profile_df)

        for rec in recommendations:
            if rec['level'] == 'error':
                st.error(f"❌ {rec['message']}")
            elif rec['level'] == 'warning':
                st.warning(f"⚠️ {rec['message']}")
            else:
                st.info(f"ℹ️ {rec['message']}")

        # Export Profile Report
        st.markdown("### 💾 Export Profile Report")

        if st.button("📄 Export Detailed Profile Report"):
            export_profile_report(df, profile_df, quality_score)

    except Exception as e:
        st.error(f"Error generating data profile: {str(e)}")


def calculate_comprehensive_quality_score(df):
    """Calculate comprehensive data quality score"""
    score = 100

    # Completeness (30%)
    missing_pct = (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    completeness_score = max(0, 100 - missing_pct * 2)
    score = score * 0.7 + completeness_score * 0.3

    # Uniqueness (25%) - check for duplicates
    duplicates_pct = (df.duplicated().sum() / len(df)) * 100
    uniqueness_score = max(0, 100 - duplicates_pct * 3)
    score = score * 0.75 + uniqueness_score * 0.25

    # Consistency (25%) - data type consistency
    consistency_score = 100
    inconsistent_cols = 0

    for col in df.columns:
        if df[col].dtype == 'object':
            non_null_data = df[col].dropna()
            if len(non_null_data) > 0:
                try:
                    pd.to_numeric(non_null_data.head(100), errors='raise')
                    inconsistent_cols += 1  # Could be numeric but stored as text
                except:
                    pass

    if len(df.columns) > 0:
        consistency_score = max(0, 100 - (inconsistent_cols / len(df.columns)) * 50)

    score = score * 0.75 + consistency_score * 0.25

    # Validity (20%) - domain-specific checks
    validity_score = 100
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        col_name_lower = col.lower()
        col_data = df[col]

        # Check for negative values in fields that shouldn't have them
        if any(keyword in col_name_lower for keyword in ['age', 'count', 'quantity', 'amount', 'price']) and (
                col_data < 0).any():
            validity_score -= 10

        # Check for extremely large values that might be errors
        if col_data.max() > col_data.median() * 1000 and col_data.median() > 0:
            validity_score -= 5

    score = score * 0.8 + max(0, validity_score) * 0.2

    return max(0, min(100, score))


def generate_quality_recommendations(df, profile_df):
    """Generate data quality recommendations"""
    recommendations = []

    # Missing data recommendations
    missing_cols = profile_df[profile_df['Missing %'] > 0]
    if len(missing_cols) > 0:
        high_missing = missing_cols[missing_cols['Missing %'] > 50]
        if len(high_missing) > 0:
            recommendations.append({
                'level': 'error',
                'message': f"Columns with >50% missing data: {', '.join(high_missing['Column'].tolist())}. Consider removing or investigating."
            })

        moderate_missing = missing_cols[(missing_cols['Missing %'] > 10) & (missing_cols['Missing %'] <= 50)]
        if len(moderate_missing) > 0:
            recommendations.append({
                'level': 'warning',
                'message': f"Columns with moderate missing data (10-50%): {', '.join(moderate_missing['Column'].tolist())}. Consider imputation strategies."
            })

    # Data type recommendations
    if 'Suggestions' in profile_df.columns:
        type_suggestions = profile_df[profile_df['Suggestions'] != 'None']
        if len(type_suggestions) > 0:
            for _, row in type_suggestions.iterrows():
                recommendations.append({
                    'level': 'info',
                    'message': f"Column '{row['Column']}': {row['Suggestions']}"
                })

    # Duplicate recommendations
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        dup_pct = (duplicates / len(df)) * 100
        if dup_pct > 10:
            recommendations.append({
                'level': 'warning',
                'message': f"High duplicate rate ({dup_pct:.1f}%). Consider deduplication."
            })
        else:
            recommendations.append({
                'level': 'info',
                'message': f"Found {duplicates} duplicate rows ({dup_pct:.1f}%). Review if intended."
            })

    # Constant columns
    constant_cols = profile_df[profile_df['Unique'] == 1]
    if len(constant_cols) > 0:
        recommendations.append({
            'level': 'warning',
            'message': f"Constant value columns (consider removing): {', '.join(constant_cols['Column'].tolist())}"
        })

    # High cardinality recommendations
    high_cardinality = profile_df[profile_df['Unique %'] > 95]
    if len(high_cardinality) > 0:
        recommendations.append({
            'level': 'info',
            'message': f"Very high cardinality columns: {', '.join(high_cardinality['Column'].tolist())}. Consider if this is expected."
        })

    return recommendations


def export_profile_report(df, profile_df, quality_score):
    """Export comprehensive profile report"""
    try:
        # Create summary report
        summary_data = {
            'Dataset_Name': 'Data Profile Report',
            'Total_Rows': len(df),
            'Total_Columns': len(df.columns),
            'Memory_Usage_MB': df.memory_usage(deep=True).sum() / 1024 ** 2,
            'Data_Quality_Score': quality_score,
            'Missing_Cells': df.isnull().sum().sum(),
            'Completeness_Percentage': ((len(df) * len(df.columns) - df.isnull().sum().sum()) / (
                        len(df) * len(df.columns))) * 100,
            'Duplicate_Rows': df.duplicated().sum(),
            'Generated_Date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        summary_df = pd.DataFrame([summary_data])

        # Export using ExcelWriter for multiple sheets
        import io
        output = io.BytesIO()

        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
            profile_df.to_excel(writer, sheet_name='Column_Analysis', index=False)

            # Missing data analysis if any
            missing_summary = df.isnull().sum()
            if missing_summary.sum() > 0:
                missing_df = pd.DataFrame({
                    'Column': missing_summary.index,
                    'Missing_Count': missing_summary.values,
                    'Missing_Percentage': (missing_summary.values / len(df)) * 100
                })
                missing_df.to_excel(writer, sheet_name='Missing_Data', index=False)

        excel_data = output.getvalue()
        FileHandler.create_download_link(excel_data, "data_profile_report.xlsx",
                                         "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        st.success("📄 Comprehensive profile report ready for download!")

    except Exception as e:
        st.error(f"Error exporting profile report: {str(e)}")


def distribution_analysis():
    """Analyze statistical distributions of data"""
    create_tool_header("Distribution Analysis", "Analyze statistical distributions and patterns", "📉")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            # Get numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

            if len(numeric_cols) == 0:
                st.error("No numeric columns found for distribution analysis!")
                return

            # Column selection
            st.markdown("### 📊 Column Selection")

            if len(numeric_cols) > 1:
                selected_cols = st.multiselect(
                    "Select columns for distribution analysis:",
                    numeric_cols,
                    default=numeric_cols[:4] if len(numeric_cols) >= 4 else numeric_cols
                )
            else:
                selected_cols = numeric_cols
                st.info(f"Analyzing column: {numeric_cols[0]}")

            if not selected_cols:
                st.warning("Please select at least one column.")
                return

            # Analysis options
            st.markdown("### ⚙️ Analysis Options")

            col1, col2 = st.columns(2)

            with col1:
                analysis_type = st.selectbox("Analysis Type:", [
                    "Basic Distribution", "Advanced Distribution", "Distribution Comparison", "Normality Testing"
                ])

            with col2:
                if analysis_type == "Distribution Comparison" and len(selected_cols) > 1:
                    comparison_method = st.selectbox("Comparison Method:", [
                        "Side by Side", "Overlaid Histograms", "Box Plot Comparison", "Q-Q Plots"
                    ])
                else:
                    comparison_method = "Side by Side"

            if st.button("📉 Analyze Distributions"):
                if analysis_type == "Basic Distribution":
                    basic_distribution_analysis(df, selected_cols)
                elif analysis_type == "Advanced Distribution":
                    advanced_distribution_analysis(df, selected_cols)
                elif analysis_type == "Distribution Comparison":
                    distribution_comparison(df, selected_cols, comparison_method)
                elif analysis_type == "Normality Testing":
                    normality_testing(df, selected_cols)


def basic_distribution_analysis(df, columns):
    """Basic distribution analysis with histograms and summary stats"""
    try:
        for col in columns:
            st.markdown(f"### 📈 Distribution Analysis: {col}")

            col_data = df[col].dropna()

            if len(col_data) == 0:
                st.warning(f"No data available for column '{col}'")
                continue

            # Basic statistics
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Count", len(col_data))
                st.metric("Mean", f"{col_data.mean():.2f}")
            with col2:
                st.metric("Median", f"{col_data.median():.2f}")
                st.metric("Mode", f"{col_data.mode().iloc[0]:.2f}" if len(col_data.mode()) > 0 else "N/A")
            with col3:
                st.metric("Std Dev", f"{col_data.std():.2f}")
                st.metric("Variance", f"{col_data.var():.2f}")
            with col4:
                st.metric("Min", f"{col_data.min():.2f}")
                st.metric("Max", f"{col_data.max():.2f}")

            # Distribution shape metrics
            st.markdown("#### 📁 Distribution Shape")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                skewness = col_data.skew()
                st.metric("Skewness", f"{skewness:.3f}")
                if abs(skewness) < 0.5:
                    st.success("Approximately symmetric")
                elif abs(skewness) < 1:
                    st.info("Moderately skewed")
                else:
                    st.warning("Highly skewed")

            with col2:
                kurtosis = col_data.kurtosis()
                st.metric("Kurtosis", f"{kurtosis:.3f}")
                if abs(kurtosis) < 1:
                    st.success("Mesokurtic (normal-like)")
                elif kurtosis > 1:
                    st.info("Leptokurtic (heavy tails)")
                else:
                    st.info("Platykurtic (light tails)")

            with col3:
                range_val = col_data.max() - col_data.min()
                st.metric("Range", f"{range_val:.2f}")

            with col4:
                iqr = col_data.quantile(0.75) - col_data.quantile(0.25)
                st.metric("IQR", f"{iqr:.2f}")

            # Visualizations
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))

            # Histogram
            axes[0, 0].hist(col_data, bins=30, alpha=0.7, edgecolor='black')
            axes[0, 0].set_title(f'Histogram: {col}')
            axes[0, 0].set_xlabel(col)
            axes[0, 0].set_ylabel('Frequency')

            # Box plot
            axes[0, 1].boxplot(col_data)
            axes[0, 1].set_title(f'Box Plot: {col}')
            axes[0, 1].set_ylabel(col)

            # Q-Q plot for normality
            from scipy import stats
            stats.probplot(col_data, dist="norm", plot=axes[1, 0])
            axes[1, 0].set_title(f'Q-Q Plot (Normal): {col}')

            # Density plot
            axes[1, 1].hist(col_data, bins=30, density=True, alpha=0.7, label='Data')

            # Overlay normal distribution
            x = np.linspace(col_data.min(), col_data.max(), 100)
            normal_dist = stats.norm.pdf(x, col_data.mean(), col_data.std())
            axes[1, 1].plot(x, normal_dist, 'r-', label='Normal fit')
            axes[1, 1].set_title(f'Density Plot with Normal Overlay: {col}')
            axes[1, 1].legend()

            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Percentiles
            st.markdown("#### 📅 Percentiles")

            percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99]
            perc_values = [col_data.quantile(p / 100) for p in percentiles]

            perc_df = pd.DataFrame({
                'Percentile': [f"{p}%" for p in percentiles],
                'Value': perc_values
            })

            st.dataframe(perc_df.T)

    except Exception as e:
        st.error(f"Error in basic distribution analysis: {str(e)}")


def advanced_distribution_analysis(df, columns):
    """Advanced distribution analysis with distribution fitting"""
    try:
        from scipy import stats

        for col in columns:
            st.markdown(f"### 🔬 Advanced Distribution Analysis: {col}")

            col_data = df[col].dropna()

            if len(col_data) < 10:
                st.warning(f"Insufficient data for advanced analysis of column '{col}' (need at least 10 values)")
                continue

            # Test multiple distributions
            distributions = {
                'Normal': stats.norm,
                'Log-Normal': stats.lognorm,
                'Exponential': stats.expon,
                'Gamma': stats.gamma,
                'Beta': stats.beta,
                'Uniform': stats.uniform
            }

            fit_results = []

            for dist_name, distribution in distributions.items():
                try:
                    # Fit distribution
                    if dist_name == 'Beta':
                        # Beta distribution requires data to be in [0,1]
                        normalized_data = (col_data - col_data.min()) / (col_data.max() - col_data.min())
                        if (normalized_data >= 0).all() and (normalized_data <= 1).all():
                            params = distribution.fit(normalized_data)
                            # Kolmogorov-Smirnov test
                            ks_stat, p_value = stats.kstest(normalized_data, lambda x: distribution.cdf(x, *params))
                        else:
                            continue
                    else:
                        params = distribution.fit(col_data)
                        # Kolmogorov-Smirnov test
                        ks_stat, p_value = stats.kstest(col_data, lambda x: distribution.cdf(x, *params))

                    # Calculate AIC/BIC
                    log_likelihood = np.sum(
                        distribution.logpdf(col_data if dist_name != 'Beta' else normalized_data, *params))
                    aic = 2 * len(params) - 2 * log_likelihood
                    bic = len(params) * np.log(len(col_data)) - 2 * log_likelihood

                    fit_results.append({
                        'Distribution': dist_name,
                        'KS Statistic': ks_stat,
                        'P-value': p_value,
                        'AIC': aic,
                        'BIC': bic,
                        'Parameters': params
                    })

                except Exception:
                    continue

            if fit_results:
                # Display fit results
                st.markdown("#### 🎯 Distribution Fitting Results")

                fit_df = pd.DataFrame(fit_results)
                fit_df = fit_df.sort_values('AIC')  # Sort by AIC (lower is better)

                # Format the display
                display_df = fit_df[['Distribution', 'KS Statistic', 'P-value', 'AIC', 'BIC']].copy()
                display_df = display_df.round(4)

                st.dataframe(display_df)

                # Best fit recommendation
                best_fit = fit_df.iloc[0]
                if best_fit['P-value'] > 0.05:
                    st.success(f"✅ Best fit: {best_fit['Distribution']} (p-value: {best_fit['P-value']:.4f} > 0.05)")
                else:
                    st.warning(
                        f"⚠️ Best available fit: {best_fit['Distribution']} (p-value: {best_fit['P-value']:.4f} < 0.05 - poor fit)")

                # Visualization of best fits
                st.markdown("#### 📈 Distribution Comparison")

                fig, axes = plt.subplots(2, 2, figsize=(15, 10))

                # Original histogram
                axes[0, 0].hist(col_data, bins=30, density=True, alpha=0.7, label='Data')
                axes[0, 0].set_title(f'Data vs Best Fit Distributions: {col}')
                axes[0, 0].set_xlabel(col)
                axes[0, 0].set_ylabel('Density')

                # Overlay top 3 distributions
                x = np.linspace(col_data.min(), col_data.max(), 100)
                colors = ['red', 'blue', 'green']

                for i, (_, row) in enumerate(fit_df.head(3).iterrows()):
                    dist = distributions[row['Distribution']]
                    params = row['Parameters']

                    if row['Distribution'] == 'Beta':
                        # For beta, we need to transform back
                        x_norm = (x - col_data.min()) / (col_data.max() - col_data.min())
                        y = dist.pdf(x_norm, *params) / (col_data.max() - col_data.min())
                    else:
                        y = dist.pdf(x, *params)

                    axes[0, 0].plot(x, y, color=colors[i], label=f'{row["Distribution"]} (AIC: {row["AIC"]:.1f})')

                axes[0, 0].legend()

                # Q-Q plot for best fit
                best_dist = distributions[best_fit['Distribution']]
                if best_fit['Distribution'] != 'Beta':
                    stats.probplot(col_data, dist=best_dist, sparams=best_fit['Parameters'], plot=axes[0, 1])
                    axes[0, 1].set_title(f'Q-Q Plot: {best_fit["Distribution"]}')

                # Empirical CDF vs fitted CDF
                sorted_data = np.sort(col_data)
                empirical_cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

                axes[1, 0].plot(sorted_data, empirical_cdf, 'o-', label='Empirical CDF', alpha=0.7)

                if best_fit['Distribution'] != 'Beta':
                    fitted_cdf = best_dist.cdf(sorted_data, *best_fit['Parameters'])
                    axes[1, 0].plot(sorted_data, fitted_cdf, 'r-', label=f'{best_fit["Distribution"]} CDF')

                axes[1, 0].set_title('Empirical vs Fitted CDF')
                axes[1, 0].legend()

                # Residuals plot
                if best_fit['Distribution'] != 'Beta':
                    fitted_cdf = best_dist.cdf(sorted_data, *best_fit['Parameters'])
                    residuals = empirical_cdf - fitted_cdf
                    axes[1, 1].scatter(sorted_data, residuals, alpha=0.7)
                    axes[1, 1].axhline(y=0, color='r', linestyle='--')
                    axes[1, 1].set_title('CDF Residuals')
                    axes[1, 1].set_xlabel(col)
                    axes[1, 1].set_ylabel('Empirical - Fitted')

                plt.tight_layout()
                st.pyplot()
                plt.close()

    except Exception as e:
        st.error(f"Error in advanced distribution analysis: {str(e)}")


def distribution_comparison(df, columns, method):
    """Compare distributions between multiple columns"""
    try:
        if len(columns) < 2:
            st.warning("Need at least 2 columns for comparison")
            return

        st.markdown("### 🔄 Distribution Comparison")

        if method == "Side by Side":
            # Create subplots for each column
            n_cols = min(3, len(columns))
            n_rows = (len(columns) + n_cols - 1) // n_cols

            fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
            if n_rows == 1 and n_cols == 1:
                axes = [axes]
            elif n_rows == 1:
                axes = axes
            else:
                axes = axes.flatten()

            for i, col in enumerate(columns):
                if i < len(axes):
                    col_data = df[col].dropna()
                    axes[i].hist(col_data, bins=30, alpha=0.7)
                    axes[i].set_title(f'{col}')
                    axes[i].set_xlabel(col)
                    axes[i].set_ylabel('Frequency')

            # Hide empty subplots
            for i in range(len(columns), len(axes)):
                axes[i].set_visible(False)

            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

        elif method == "Overlaid Histograms":
            # Overlaid histograms
            plt.figure(figsize=(12, 6))

            colors = plt.cm.Set3(np.linspace(0, 1, len(columns)))

            for i, col in enumerate(columns):
                col_data = df[col].dropna()
                plt.hist(col_data, bins=30, alpha=0.6, label=col, color=colors[i])

            plt.title('Distribution Comparison')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.legend()
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

        elif method == "Box Plot Comparison":
            # Box plot comparison
            data_for_boxplot = [df[col].dropna() for col in columns]

            plt.figure(figsize=(12, 6))
            plt.boxplot(data_for_boxplot, labels=columns)
            plt.title('Box Plot Comparison')
            plt.ylabel('Value')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

        elif method == "Q-Q Plots":
            # Q-Q plots comparing to first column
            if len(columns) >= 2:
                reference_col = columns[0]
                reference_data = df[reference_col].dropna()

                n_comparisons = len(columns) - 1
                n_cols = min(3, n_comparisons)
                n_rows = (n_comparisons + n_cols - 1) // n_cols

                fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
                if n_rows == 1 and n_cols == 1:
                    axes = [axes]
                elif n_rows == 1:
                    axes = axes
                else:
                    axes = axes.flatten()

                for i, col in enumerate(columns[1:]):
                    if i < len(axes):
                        col_data = df[col].dropna()

                        # Create Q-Q plot
                        min_len = min(len(reference_data), len(col_data))
                        if min_len > 0:
                            ref_quantiles = np.quantile(reference_data, np.linspace(0, 1, min_len))
                            col_quantiles = np.quantile(col_data, np.linspace(0, 1, min_len))

                            axes[i].scatter(ref_quantiles, col_quantiles, alpha=0.7)

                            # Add diagonal line
                            min_val = min(ref_quantiles.min(), col_quantiles.min())
                            max_val = max(ref_quantiles.max(), col_quantiles.max())
                            axes[i].plot([min_val, max_val], [min_val, max_val], 'r--')

                            axes[i].set_xlabel(f'{reference_col} Quantiles')
                            axes[i].set_ylabel(f'{col} Quantiles')
                            axes[i].set_title(f'Q-Q: {reference_col} vs {col}')

                plt.tight_layout()
                st.pyplot()
                plt.close()

        # Summary statistics comparison
        st.markdown("#### 📊 Summary Statistics Comparison")

        summary_data = []
        for col in columns:
            col_data = df[col].dropna()
            summary_data.append({
                'Column': col,
                'Count': len(col_data),
                'Mean': col_data.mean(),
                'Median': col_data.median(),
                'Std Dev': col_data.std(),
                'Skewness': col_data.skew(),
                'Kurtosis': col_data.kurtosis(),
                'Min': col_data.min(),
                'Max': col_data.max()
            })

        comparison_df = pd.DataFrame(summary_data)
        st.dataframe(comparison_df.round(3))

    except Exception as e:
        st.error(f"Error in distribution comparison: {str(e)}")


def normality_testing(df, columns):
    """Comprehensive normality testing"""
    try:
        from scipy import stats

        st.markdown("### 🔬 Normality Testing")

        test_results = []

        for col in columns:
            col_data = df[col].dropna()

            if len(col_data) < 8:
                st.warning(f"Insufficient data for normality testing of column '{col}' (need at least 8 values)")
                continue

            # Shapiro-Wilk test (best for small samples)
            if len(col_data) <= 5000:
                shapiro_stat, shapiro_p = stats.shapiro(col_data)
            else:
                shapiro_stat, shapiro_p = None, None

            # D'Agostino's test
            if len(col_data) >= 20:
                dagostino_stat, dagostino_p = stats.normaltest(col_data)
            else:
                dagostino_stat, dagostino_p = None, None

            # Kolmogorov-Smirnov test
            ks_stat, ks_p = stats.kstest(col_data, 'norm', args=(col_data.mean(), col_data.std()))

            # Anderson-Darling test
            ad_result = stats.anderson(col_data, dist='norm')

            test_results.append({
                'Column': col,
                'Shapiro-Wilk Stat': shapiro_stat,
                'Shapiro-Wilk p-value': shapiro_p,
                'D\'Agostino Stat': dagostino_stat,
                'D\'Agostino p-value': dagostino_p,
                'KS Stat': ks_stat,
                'KS p-value': ks_p,
                'Anderson-Darling Stat': ad_result.statistic,
                'AD Critical Value (5%)': ad_result.critical_values[2],  # 5% significance
                'Sample Size': len(col_data)
            })

        if test_results:
            # Display results table
            results_df = pd.DataFrame(test_results)

            # Format for display
            display_df = results_df.round(6)
            st.dataframe(display_df)

            # Interpretation
            st.markdown("#### 📋 Test Interpretations")

            alpha = 0.05

            for _, row in results_df.iterrows():
                col_name = row['Column']
                st.markdown(f"**{col_name}:**")

                interpretations = []

                # Shapiro-Wilk
                if row['Shapiro-Wilk p-value'] is not None:
                    if row['Shapiro-Wilk p-value'] > alpha:
                        interpretations.append("✅ Shapiro-Wilk: Normal (fail to reject H0)")
                    else:
                        interpretations.append("❌ Shapiro-Wilk: Not normal (reject H0)")

                # D'Agostino
                if row['D\'Agostino p-value'] is not None:
                    if row['D\'Agostino p-value'] > alpha:
                        interpretations.append("✅ D'Agostino: Normal (fail to reject H0)")
                    else:
                        interpretations.append("❌ D'Agostino: Not normal (reject H0)")

                # KS test
                if row['KS p-value'] > alpha:
                    interpretations.append("✅ Kolmogorov-Smirnov: Normal (fail to reject H0)")
                else:
                    interpretations.append("❌ Kolmogorov-Smirnov: Not normal (reject H0)")

                # Anderson-Darling
                if row['Anderson-Darling Stat'] < row['AD Critical Value (5%)']:
                    interpretations.append("✅ Anderson-Darling: Normal (test statistic < critical value)")
                else:
                    interpretations.append("❌ Anderson-Darling: Not normal (test statistic > critical value)")

                for interpretation in interpretations:
                    st.write(f"  - {interpretation}")

                # Overall conclusion
                normal_tests = sum(1 for interp in interpretations if "✅" in interp)
                total_tests = len(interpretations)

                if normal_tests >= total_tests * 0.75:
                    st.success(
                        f"  → **Overall: Likely normal distribution** ({normal_tests}/{total_tests} tests support normality)")
                elif normal_tests >= total_tests * 0.5:
                    st.info(
                        f"  → **Overall: Possibly normal distribution** ({normal_tests}/{total_tests} tests support normality)")
                else:
                    st.error(
                        f"  → **Overall: Likely not normal distribution** ({normal_tests}/{total_tests} tests support normality)")

                st.write("")

            # Visual normality assessment
            st.markdown("#### 📈 Visual Normality Assessment")

            for col in columns:
                col_data = df[col].dropna()

                if len(col_data) == 0:
                    continue

                st.markdown(f"**{col}**")

                fig, axes = plt.subplots(1, 3, figsize=(18, 5))

                # Histogram with normal overlay
                axes[0].hist(col_data, bins=30, density=True, alpha=0.7, label='Data')
                x = np.linspace(col_data.min(), col_data.max(), 100)
                normal_dist = stats.norm.pdf(x, col_data.mean(), col_data.std())
                axes[0].plot(x, normal_dist, 'r-', linewidth=2, label='Normal fit')
                axes[0].set_title(f'Histogram vs Normal: {col}')
                axes[0].legend()

                # Q-Q plot
                stats.probplot(col_data, dist="norm", plot=axes[1])
                axes[1].set_title(f'Q-Q Plot: {col}')

                # Box plot
                axes[2].boxplot(col_data)
                axes[2].set_title(f'Box Plot: {col}')
                axes[2].set_ylabel(col)

                plt.tight_layout()
                st.pyplot()
                plt.close()

    except Exception as e:
        st.error(f"Error in normality testing: {str(e)}")


def heatmap_creator():
    """Create customizable heatmaps from data"""
    create_tool_header("Heatmap Creator", "Create beautiful correlation and data heatmaps", "🔥")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())

            heatmap_type = st.selectbox("Heatmap Type:", [
                "Correlation Heatmap", "Data Heatmap", "Pivot Table Heatmap"
            ])

            if heatmap_type == "Correlation Heatmap":
                create_correlation_heatmap(df)
            elif heatmap_type == "Data Heatmap":
                create_data_heatmap(df)
            elif heatmap_type == "Pivot Table Heatmap":
                create_pivot_heatmap(df)


def create_correlation_heatmap(df):
    """Create correlation heatmap"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(numeric_cols) < 2:
        st.error("Need at least 2 numeric columns for correlation heatmap")
        return

    # Configuration options
    col1, col2 = st.columns(2)
    with col1:
        color_scheme = st.selectbox("Color Scheme:", [
            "coolwarm", "viridis", "plasma", "inferno", "RdYlBu", "RdBu", "Spectral"
        ])
        show_annotations = st.checkbox("Show Values", value=True)

    with col2:
        method = st.selectbox("Correlation Method:", ["pearson", "spearman", "kendall"])
        figure_size = st.slider("Figure Size:", 6, 16, 10)

    if st.button("Create Heatmap"):
        try:
            # Calculate correlation matrix
            corr_matrix = df[numeric_cols].corr(method=method)

            # Create heatmap
            plt.figure(figsize=(figure_size, figure_size))
            sns.heatmap(corr_matrix,
                        annot=show_annotations,
                        cmap=color_scheme,
                        center=0,
                        square=True,
                        linewidths=0.5,
                        cbar_kws={"shrink": .8})

            plt.title(f"{method.title()} Correlation Heatmap", fontsize=16, pad=20)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Show strongest correlations
            st.markdown("### 🔍 Strongest Correlations")
            correlations = []
            for i in range(len(corr_matrix.columns)):
                for j in range(i + 1, len(corr_matrix.columns)):
                    corr_value = corr_matrix.iloc[i, j]
                    correlations.append({
                        'Variable 1': corr_matrix.columns[i],
                        'Variable 2': corr_matrix.columns[j],
                        'Correlation': corr_value,
                        'Strength': 'Strong' if abs(corr_value) > 0.7 else 'Moderate' if abs(
                            corr_value) > 0.3 else 'Weak'
                    })

            corr_df = pd.DataFrame(correlations).sort_values('Correlation', key=abs, ascending=False)
            st.dataframe(corr_df.head(10))

        except Exception as e:
            st.error(f"Error creating correlation heatmap: {str(e)}")


def create_data_heatmap(df):
    """Create data heatmap"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(numeric_cols) == 0:
        st.error("Need numeric columns for data heatmap")
        return

    # Configuration
    col1, col2 = st.columns(2)
    with col1:
        selected_cols = st.multiselect("Select Columns:", numeric_cols, default=list(numeric_cols[:5]))
        color_scheme = st.selectbox("Color Scheme:", [
            "viridis", "plasma", "inferno", "magma", "Blues", "Reds", "Greens"
        ])

    with col2:
        normalize_data = st.checkbox("Normalize Data", value=True)
        show_annotations = st.checkbox("Show Values", value=False)

    if selected_cols and st.button("Create Data Heatmap"):
        try:
            data_subset = df[selected_cols].head(50)  # Limit rows for visibility

            if normalize_data:
                from sklearn.preprocessing import StandardScaler
                scaler = StandardScaler()
                data_normalized = pd.DataFrame(
                    scaler.fit_transform(data_subset),
                    columns=data_subset.columns,
                    index=data_subset.index
                )
                data_to_plot = data_normalized
                title = "Normalized Data Heatmap"
            else:
                data_to_plot = data_subset
                title = "Data Heatmap"

            plt.figure(figsize=(12, 8))
            sns.heatmap(data_to_plot.T,
                        annot=show_annotations,
                        cmap=color_scheme,
                        cbar_kws={"shrink": .8})

            plt.title(title, fontsize=16, pad=20)
            plt.xlabel("Samples")
            plt.ylabel("Features")
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

        except Exception as e:
            st.error(f"Error creating data heatmap: {str(e)}")


def create_pivot_heatmap(df):
    """Create pivot table heatmap"""
    categorical_cols = df.select_dtypes(include=['object']).columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(categorical_cols) < 1 or len(numeric_cols) < 1:
        st.error("Need at least 1 categorical and 1 numeric column for pivot heatmap")
        return

    # Configuration
    col1, col2 = st.columns(2)
    with col1:
        index_col = st.selectbox("Row Variable:", categorical_cols)
        value_col = st.selectbox("Value Variable:", numeric_cols)

    with col2:
        column_col = st.selectbox("Column Variable (optional):", ['None'] + list(categorical_cols))
        agg_func = st.selectbox("Aggregation:", ["mean", "sum", "count", "median", "max", "min"])

    if st.button("Create Pivot Heatmap"):
        try:
            # Create pivot table
            if column_col == 'None':
                pivot_data = df.groupby(index_col)[value_col].agg(agg_func).reset_index()
                pivot_data = pivot_data.set_index(index_col).T
            else:
                pivot_data = df.pivot_table(
                    index=index_col,
                    columns=column_col,
                    values=value_col,
                    aggfunc=agg_func
                )

            plt.figure(figsize=(12, 8))
            sns.heatmap(pivot_data,
                        annot=True,
                        cmap="YlOrRd",
                        cbar_kws={"shrink": .8})

            plt.title(f"Pivot Heatmap: {agg_func.title()} of {value_col}", fontsize=16, pad=20)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Show pivot table
            st.markdown("### 📊 Pivot Table Data")
            st.dataframe(pivot_data)

        except Exception as e:
            st.error(f"Error creating pivot heatmap: {str(e)}")


def scatter_plot():
    """Create advanced scatter plots"""
    create_tool_header("Scatter Plot", "Create advanced scatter plots with customization", "⚡")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())
            create_advanced_scatter(df)


def create_advanced_scatter(df):
    """Create advanced scatter plot"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    if len(numeric_cols) < 2:
        st.error("Need at least 2 numeric columns for scatter plot")
        return

    # Basic configuration
    col1, col2 = st.columns(2)
    with col1:
        x_col = st.selectbox("X-axis:", numeric_cols)
        y_col = st.selectbox("Y-axis:", numeric_cols)

    with col2:
        color_col = st.selectbox("Color by (optional):", ['None'] + list(categorical_cols) + list(numeric_cols))
        size_col = st.selectbox("Size by (optional):", ['None'] + list(numeric_cols))

    # Advanced options
    st.markdown("### ⚙️ Advanced Options")
    col1, col2, col3 = st.columns(3)

    with col1:
        add_trendline = st.checkbox("Add Trend Line", value=False)
        show_correlation = st.checkbox("Show Correlation", value=True)

    with col2:
        transparency = st.slider("Transparency:", 0.1, 1.0, 0.7, 0.1)
        point_size = st.slider("Point Size:", 10, 200, 50, 10)

    with col3:
        color_scheme = st.selectbox("Color Scheme:", [
            "viridis", "plasma", "inferno", "magma", "tab10", "Set1", "Set2"
        ])

    if st.button("Create Scatter Plot"):
        try:
            plt.figure(figsize=(12, 8))

            # Prepare data
            plot_data = df[[x_col, y_col]].dropna()

            if color_col != 'None':
                color_data = df[color_col].dropna()
                # Align indices
                common_idx = plot_data.index.intersection(color_data.index)
                plot_data = plot_data.loc[common_idx]
                color_data = color_data.loc[common_idx]
            else:
                color_data = None

            if size_col != 'None':
                size_data = df[size_col].dropna()
                # Align indices
                if color_data is not None:
                    common_idx = plot_data.index.intersection(size_data.index).intersection(color_data.index)
                    plot_data = plot_data.loc[common_idx]
                    color_data = color_data.loc[common_idx]
                    size_data = size_data.loc[common_idx]
                else:
                    common_idx = plot_data.index.intersection(size_data.index)
                    plot_data = plot_data.loc[common_idx]
                    size_data = size_data.loc[common_idx]
                # Normalize size data
                size_data = (size_data - size_data.min()) / (size_data.max() - size_data.min()) * 200 + 50
            else:
                size_data = point_size

            # Create scatter plot
            scatter = plt.scatter(
                plot_data[x_col],
                plot_data[y_col],
                c=color_data if color_data is not None else 'blue',
                s=size_data,
                alpha=transparency,
                cmap=color_scheme
            )

            # Add colorbar if color mapping is used
            if color_col != 'None':
                cbar = plt.colorbar(scatter)
                cbar.set_label(color_col)

            # Add trend line
            if add_trendline:
                z = np.polyfit(plot_data[x_col], plot_data[y_col], 1)
                p = np.poly1d(z)
                plt.plot(plot_data[x_col].sort_values(), p(plot_data[x_col].sort_values()),
                         "r--", alpha=0.8, linewidth=2, label='Trend Line')
                plt.legend()

            plt.xlabel(x_col, fontsize=12)
            plt.ylabel(y_col, fontsize=12)
            plt.title(f"Scatter Plot: {y_col} vs {x_col}", fontsize=14, pad=20)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Show correlation if requested
            if show_correlation:
                correlation = plot_data[x_col].corr(plot_data[y_col])
                st.metric("Correlation Coefficient", f"{correlation:.4f}")

                if abs(correlation) > 0.7:
                    st.success("Strong correlation detected!")
                elif abs(correlation) > 0.3:
                    st.info("Moderate correlation detected.")
                else:
                    st.warning("Weak correlation detected.")

        except Exception as e:
            st.error(f"Error creating scatter plot: {str(e)}")


def time_series_plot():
    """Create time series visualizations"""
    create_tool_header("Time Series Plot", "Create time series visualizations with trends", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())
            create_time_series_visualization(df)


def create_time_series_visualization(df):
    """Create time series visualization"""
    # Identify potential date columns
    date_cols = []
    for col in df.columns:
        try:
            pd.to_datetime(df[col].dropna().head(100))
            date_cols.append(col)
        except:
            continue

    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(date_cols) == 0:
        st.error("No date columns detected. Please ensure your data has date/time columns.")
        return

    if len(numeric_cols) == 0:
        st.error("Need at least 1 numeric column for time series plot")
        return

    # Configuration
    col1, col2 = st.columns(2)
    with col1:
        date_col = st.selectbox("Date Column:", date_cols)
        value_cols = st.multiselect("Value Columns:", numeric_cols, default=list(numeric_cols[:3]))

    with col2:
        plot_type = st.selectbox("Plot Type:", ["Line Plot", "Area Plot", "Multiple Series"])
        show_trend = st.checkbox("Show Trend Line", value=False)

    # Advanced options
    st.markdown("### ⚙️ Advanced Options")
    col1, col2 = st.columns(2)
    with col1:
        resample_freq = st.selectbox("Resample Frequency (optional):", [
            "None", "Daily (D)", "Weekly (W)", "Monthly (M)", "Quarterly (Q)", "Yearly (Y)"
        ])
    with col2:
        moving_avg = st.selectbox("Moving Average (optional):", [
            "None", "7 days", "30 days", "90 days"
        ])

    if value_cols and st.button("Create Time Series Plot"):
        try:
            # Prepare data
            ts_data = df[[date_col] + value_cols].copy()
            ts_data[date_col] = pd.to_datetime(ts_data[date_col])
            ts_data = ts_data.dropna().sort_values(date_col)
            ts_data.set_index(date_col, inplace=True)

            # Resample if requested
            if resample_freq != "None":
                freq_map = {
                    "Daily (D)": "D", "Weekly (W)": "W",
                    "Monthly (M)": "M", "Quarterly (Q)": "Q", "Yearly (Y)": "Y"
                }
                ts_data = ts_data.resample(freq_map[resample_freq]).mean()

            # Create plot
            plt.figure(figsize=(14, 8))

            if plot_type == "Area Plot":
                ts_data[value_cols].plot(kind='area', alpha=0.7, stacked=False)
            elif plot_type == "Multiple Series":
                for i, col in enumerate(value_cols):
                    plt.subplot(len(value_cols), 1, i + 1)
                    plt.plot(ts_data.index, ts_data[col], linewidth=2)
                    plt.title(f"{col} over Time")
                    plt.ylabel(col)
                    if i == len(value_cols) - 1:
                        plt.xlabel("Date")
            else:  # Line Plot
                for col in value_cols:
                    plt.plot(ts_data.index, ts_data[col], linewidth=2, label=col)

                # Add moving average if requested
                if moving_avg != "None":
                    window_map = {"7 days": 7, "30 days": 30, "90 days": 90}
                    window = window_map[moving_avg]
                    for col in value_cols:
                        ma = ts_data[col].rolling(window=window).mean()
                        plt.plot(ts_data.index, ma, '--', alpha=0.8,
                                 label=f"{col} ({moving_avg} MA)")

                # Add trend line if requested
                if show_trend and len(value_cols) == 1:
                    x_numeric = (ts_data.index - ts_data.index[0]).days
                    z = np.polyfit(x_numeric, ts_data[value_cols[0]], 1)
                    p = np.poly1d(z)
                    plt.plot(ts_data.index, p(x_numeric), 'r--', alpha=0.8,
                             linewidth=2, label='Trend')

                plt.legend()

            if plot_type != "Multiple Series":
                plt.title(f"Time Series: {', '.join(value_cols)}", fontsize=14, pad=20)
                plt.xlabel("Date")
                plt.ylabel("Value")

            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Show summary statistics
            st.markdown("### 📊 Time Series Summary")
            summary_stats = ts_data[value_cols].describe()
            st.dataframe(summary_stats)

            # Show period information
            date_range = ts_data.index.max() - ts_data.index.min()
            st.info(
                f"📅 Time period: {ts_data.index.min().strftime('%Y-%m-%d')} to {ts_data.index.max().strftime('%Y-%m-%d')} ({date_range.days} days)")

        except Exception as e:
            st.error(f"Error creating time series plot: {str(e)}")


def dashboard_builder():
    """Create multi-chart dashboards"""
    create_tool_header("Dashboard Builder", "Create comprehensive data dashboards", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())
            create_dashboard(df)


def create_dashboard(df):
    """Create comprehensive dashboard"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    if len(numeric_cols) == 0:
        st.error("Need at least some numeric columns for dashboard")
        return

    # Dashboard configuration
    st.markdown("### ⚙️ Dashboard Configuration")
    dashboard_type = st.selectbox("Dashboard Type:", [
        "Overview Dashboard", "Correlation Analysis", "Distribution Analysis", "Custom Dashboard"
    ])

    if dashboard_type == "Overview Dashboard":
        create_overview_dashboard(df, numeric_cols, categorical_cols)
    elif dashboard_type == "Correlation Analysis":
        create_correlation_dashboard(df, numeric_cols)
    elif dashboard_type == "Distribution Analysis":
        create_distribution_dashboard(df, numeric_cols)
    elif dashboard_type == "Custom Dashboard":
        create_custom_dashboard(df, numeric_cols, categorical_cols)


def create_overview_dashboard(df, numeric_cols, categorical_cols):
    """Create overview dashboard"""
    if st.button("Generate Overview Dashboard"):
        try:
            st.markdown("## 📊 Data Overview Dashboard")

            # Summary statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Rows", f"{len(df):,}")
            with col2:
                st.metric("Total Columns", len(df.columns))
            with col3:
                st.metric("Numeric Columns", len(numeric_cols))
            with col4:
                st.metric("Missing Values", f"{df.isnull().sum().sum():,}")

            # Distribution plots
            if len(numeric_cols) > 0:
                st.markdown("### 📈 Distribution Overview")
                fig, axes = plt.subplots(2, 2, figsize=(15, 10))

                # Select up to 4 numeric columns
                cols_to_plot = list(numeric_cols[:4])

                for i, col in enumerate(cols_to_plot):
                    row, col_idx = i // 2, i % 2
                    data = df[col].dropna()

                    axes[row, col_idx].hist(data, bins=30, alpha=0.7, edgecolor='black')
                    axes[row, col_idx].set_title(f'Distribution: {col}')
                    axes[row, col_idx].set_xlabel(col)
                    axes[row, col_idx].set_ylabel('Frequency')

                # Hide empty subplots
                for i in range(len(cols_to_plot), 4):
                    row, col_idx = i // 2, i % 2
                    axes[row, col_idx].set_visible(False)

                plt.tight_layout()
                st.pyplot()
                plt.close()

            # Correlation heatmap if multiple numeric columns
            if len(numeric_cols) > 1:
                st.markdown("### 🔥 Correlation Overview")
                plt.figure(figsize=(10, 8))
                corr_matrix = df[numeric_cols].corr()
                sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                            square=True, linewidths=0.5)
                plt.title("Correlation Heatmap")
                plt.tight_layout()
                st.pyplot()
                plt.close()

            # Categorical analysis
            if len(categorical_cols) > 0:
                st.markdown("### 📝 Categorical Overview")
                for col in categorical_cols[:3]:  # Show first 3 categorical columns
                    value_counts = df[col].value_counts().head(10)
                    st.write(f"**{col}** - Top 10 values:")
                    st.bar_chart(value_counts)

        except Exception as e:
            st.error(f"Error creating overview dashboard: {str(e)}")


def create_correlation_dashboard(df, numeric_cols):
    """Create correlation analysis dashboard"""
    if len(numeric_cols) < 2:
        st.error("Need at least 2 numeric columns for correlation analysis")
        return

    if st.button("Generate Correlation Dashboard"):
        try:
            st.markdown("## 🔗 Correlation Analysis Dashboard")

            # Correlation matrix
            corr_matrix = df[numeric_cols].corr()

            # Main heatmap
            st.markdown("### 🔥 Correlation Heatmap")
            plt.figure(figsize=(12, 10))
            sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r', center=0,
                        square=True, linewidths=0.5)
            plt.title("Correlation Matrix", fontsize=16, pad=20)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Top correlations
            st.markdown("### 📊 Strongest Correlations")
            correlations = []
            for i in range(len(corr_matrix.columns)):
                for j in range(i + 1, len(corr_matrix.columns)):
                    corr_value = corr_matrix.iloc[i, j]
                    correlations.append({
                        'Variable 1': corr_matrix.columns[i],
                        'Variable 2': corr_matrix.columns[j],
                        'Correlation': corr_value
                    })

            corr_df = pd.DataFrame(correlations).sort_values('Correlation', key=abs, ascending=False)
            st.dataframe(corr_df.head(10))

            # Scatter plots for top correlations
            st.markdown("### ⚡ Scatter Plots - Top Correlations")
            top_pairs = corr_df.head(4)

            if len(top_pairs) > 0:
                fig, axes = plt.subplots(2, 2, figsize=(15, 12))
                axes = axes.flatten()

                for i, (_, row) in enumerate(top_pairs.iterrows()):
                    if i < 4:
                        var1, var2, corr = row['Variable 1'], row['Variable 2'], row['Correlation']
                        axes[i].scatter(df[var1], df[var2], alpha=0.6)
                        axes[i].set_xlabel(var1)
                        axes[i].set_ylabel(var2)
                        axes[i].set_title(f'{var1} vs {var2}\nCorr: {corr:.3f}')

                # Hide empty subplots
                for i in range(len(top_pairs), 4):
                    axes[i].set_visible(False)

                plt.tight_layout()
                st.pyplot()
                plt.close()

        except Exception as e:
            st.error(f"Error creating correlation dashboard: {str(e)}")


def create_distribution_dashboard(df, numeric_cols):
    """Create distribution analysis dashboard"""
    if st.button("Generate Distribution Dashboard"):
        try:
            st.markdown("## 📊 Distribution Analysis Dashboard")

            # Summary statistics
            st.markdown("### 📋 Summary Statistics")
            st.dataframe(df[numeric_cols].describe())

            # Distribution plots
            st.markdown("### 📈 Distribution Plots")
            n_cols = min(3, len(numeric_cols))
            n_rows = (len(numeric_cols) + n_cols - 1) // n_cols

            fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
            if n_rows == 1:
                axes = [axes] if n_cols == 1 else axes
            else:
                axes = axes.flatten()

            for i, col in enumerate(numeric_cols):
                if i < len(axes):
                    data = df[col].dropna()
                    axes[i].hist(data, bins=30, alpha=0.7, edgecolor='black')
                    axes[i].set_title(f'Distribution: {col}')
                    axes[i].set_xlabel(col)
                    axes[i].set_ylabel('Frequency')

            # Hide empty subplots
            for i in range(len(numeric_cols), len(axes)):
                axes[i].set_visible(False)

            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Box plots
            st.markdown("### 📦 Box Plots")
            plt.figure(figsize=(15, 6))
            df[numeric_cols].boxplot()
            plt.title("Box Plot Overview")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.close()

            # Statistical insights
            st.markdown("### 🔍 Statistical Insights")
            for col in numeric_cols:
                data = df[col].dropna()
                if len(data) > 0:
                    skewness = data.skew()
                    kurtosis = data.kurtosis()

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric(f"{col} - Skewness", f"{skewness:.3f}")
                    with col2:
                        st.metric(f"{col} - Kurtosis", f"{kurtosis:.3f}")
                    with col3:
                        outliers = ((data < (data.quantile(0.25) - 1.5 * (data.quantile(0.75) - data.quantile(0.25)))) |
                                    (data > (data.quantile(0.75) + 1.5 * (
                                                data.quantile(0.75) - data.quantile(0.25))))).sum()
                        st.metric(f"{col} - Outliers", outliers)

        except Exception as e:
            st.error(f"Error creating distribution dashboard: {str(e)}")


def create_custom_dashboard(df, numeric_cols, categorical_cols):
    """Create custom dashboard"""
    st.markdown("### 🎛️ Custom Dashboard Builder")

    # Let user select charts
    col1, col2 = st.columns(2)
    with col1:
        chart_types = st.multiselect("Select Chart Types:", [
            "Histogram", "Scatter Plot", "Box Plot", "Correlation Heatmap", "Bar Chart"
        ])

    with col2:
        max_charts = st.slider("Maximum Charts:", 1, 8, 4)

    if chart_types and st.button("Generate Custom Dashboard"):
        try:
            st.markdown("## 🎨 Custom Dashboard")

            charts_created = 0
            n_cols = 2

            if "Histogram" in chart_types and charts_created < max_charts:
                st.markdown("### 📊 Histograms")
                cols_to_plot = list(numeric_cols[:4])

                if len(cols_to_plot) > 0:
                    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
                    axes = axes.flatten()

                    for i, col in enumerate(cols_to_plot):
                        if i < 4:
                            data = df[col].dropna()
                            axes[i].hist(data, bins=30, alpha=0.7)
                            axes[i].set_title(f'Histogram: {col}')

                    for i in range(len(cols_to_plot), 4):
                        axes[i].set_visible(False)

                    plt.tight_layout()
                    st.pyplot()
                    plt.close()
                    charts_created += 1

            if "Correlation Heatmap" in chart_types and charts_created < max_charts and len(numeric_cols) > 1:
                st.markdown("### 🔥 Correlation Heatmap")
                plt.figure(figsize=(10, 8))
                corr_matrix = df[numeric_cols].corr()
                sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
                plt.title("Correlation Heatmap")
                plt.tight_layout()
                st.pyplot()
                plt.close()
                charts_created += 1

            if "Scatter Plot" in chart_types and charts_created < max_charts and len(numeric_cols) > 1:
                st.markdown("### ⚡ Scatter Plots")
                cols_pairs = [(numeric_cols[i], numeric_cols[i + 1]) for i in range(0, len(numeric_cols) - 1, 2)][:2]

                if cols_pairs:
                    fig, axes = plt.subplots(1, len(cols_pairs), figsize=(15, 6))
                    if len(cols_pairs) == 1:
                        axes = [axes]

                    for i, (x_col, y_col) in enumerate(cols_pairs):
                        axes[i].scatter(df[x_col], df[y_col], alpha=0.6)
                        axes[i].set_xlabel(x_col)
                        axes[i].set_ylabel(y_col)
                        axes[i].set_title(f'{x_col} vs {y_col}')

                    plt.tight_layout()
                    st.pyplot()
                    plt.close()
                    charts_created += 1

            if "Box Plot" in chart_types and charts_created < max_charts:
                st.markdown("### 📦 Box Plots")
                plt.figure(figsize=(12, 6))
                df[numeric_cols[:5]].boxplot()
                plt.title("Box Plot Overview")
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot()
                plt.close()
                charts_created += 1

            if "Bar Chart" in chart_types and charts_created < max_charts and len(categorical_cols) > 0:
                st.markdown("### 📊 Bar Charts")
                for col in categorical_cols[:2]:
                    value_counts = df[col].value_counts().head(10)
                    st.write(f"**{col}**")
                    st.bar_chart(value_counts)
                charts_created += 1

        except Exception as e:
            st.error(f"Error creating custom dashboard: {str(e)}")


def data_aggregator():
    """Aggregate data using groupby operations"""
    create_tool_header("Data Aggregator", "Aggregate and summarize data by groups", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())
            perform_data_aggregation(df)


def perform_data_aggregation(df):
    """Perform data aggregation operations"""
    categorical_cols = df.select_dtypes(include=['object']).columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(categorical_cols) == 0:
        st.error("Need at least 1 categorical column for grouping")
        return

    if len(numeric_cols) == 0:
        st.error("Need at least 1 numeric column for aggregation")
        return

    # Configuration
    col1, col2 = st.columns(2)
    with col1:
        group_cols = st.multiselect("Group by columns:", categorical_cols, default=[categorical_cols[0]])
        agg_cols = st.multiselect("Columns to aggregate:", numeric_cols, default=list(numeric_cols[:3]))

    with col2:
        agg_functions = st.multiselect("Aggregation functions:", [
            "sum", "mean", "count", "median", "min", "max", "std", "var"
        ], default=["sum", "mean", "count"])

    # Advanced options
    st.markdown("### ⚙️ Advanced Options")
    col1, col2 = st.columns(2)
    with col1:
        include_totals = st.checkbox("Include totals row", value=False)
        sort_by = st.selectbox("Sort results by:", ["None"] + agg_cols)

    with col2:
        filter_groups = st.checkbox("Filter small groups", value=False)
        if filter_groups:
            min_group_size = st.number_input("Minimum group size:", min_value=1, value=5)

    if group_cols and agg_cols and agg_functions and st.button("Aggregate Data"):
        try:
            # Perform aggregation
            agg_dict = {col: agg_functions for col in agg_cols}
            result = df.groupby(group_cols).agg(agg_dict)

            # Flatten column names
            result.columns = ['_'.join(col).strip() for col in result.columns.values]
            result = result.reset_index()

            # Filter small groups if requested
            if filter_groups:
                group_sizes = df.groupby(group_cols).size()
                valid_groups = group_sizes[group_sizes >= min_group_size].index
                if isinstance(valid_groups, pd.MultiIndex):
                    result = result[result.set_index(group_cols).index.isin(valid_groups)]
                else:
                    result = result[result[group_cols[0]].isin(valid_groups)]

            # Sort results
            if sort_by != "None":
                sort_cols = [col for col in result.columns if sort_by in col]
                if sort_cols:
                    result = result.sort_values(sort_cols[0], ascending=False)

            # Display results
            st.markdown("### 📊 Aggregated Results")
            st.dataframe(result)

            # Add totals row if requested
            if include_totals:
                numeric_result_cols = result.select_dtypes(include=[np.number]).columns
                totals = result[numeric_result_cols].sum()
                totals_row = pd.DataFrame([totals], index=['TOTAL'])
                st.markdown("### 🔢 Totals")
                st.dataframe(totals_row)

            # Summary statistics
            st.markdown("### 📋 Summary")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Groups", len(result))
            with col2:
                st.metric("Aggregated Columns", len(agg_cols))
            with col3:
                st.metric("Functions Applied", len(agg_functions))

            # Download option
            csv_data = result.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "aggregated_data.csv", "text/csv")

        except Exception as e:
            st.error(f"Error in data aggregation: {str(e)}")


def column_calculator():
    """Create calculated columns with custom formulas"""
    create_tool_header("Column Calculator", "Create new calculated columns", "🧮")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())
            create_calculated_columns(df)


def create_calculated_columns(df):
    """Create calculated columns interface"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(numeric_cols) == 0:
        st.error("Need at least 1 numeric column for calculations")
        return

    st.markdown("### 🧮 Column Calculator")

    # Choose calculation type
    calc_type = st.selectbox("Calculation Type:", [
        "Basic Arithmetic", "Statistical Operations", "Custom Formula", "Date Calculations"
    ])

    if calc_type == "Basic Arithmetic":
        create_arithmetic_column(df, numeric_cols)
    elif calc_type == "Statistical Operations":
        create_statistical_column(df, numeric_cols)
    elif calc_type == "Custom Formula":
        create_custom_formula_column(df)
    elif calc_type == "Date Calculations":
        create_date_calculation_column(df)


def create_arithmetic_column(df, numeric_cols):
    """Create arithmetic calculated columns"""
    st.markdown("#### ➕ Basic Arithmetic")

    col1, col2, col3 = st.columns(3)
    with col1:
        col1_name = st.selectbox("First Column:", numeric_cols, key="arith_col1")
        operation = st.selectbox("Operation:", ["+", "-", "*", "/", "**", "%"])

    with col2:
        operation_type = st.radio("Second operand:", ["Column", "Constant"], key="arith_type")
        if operation_type == "Column":
            col2_name = st.selectbox("Second Column:", numeric_cols, key="arith_col2")
        else:
            constant_value = st.number_input("Constant Value:", value=1.0, key="arith_const")

    with col3:
        new_col_name = st.text_input("New Column Name:", value=f"calculated_column", key="arith_name")

    if st.button("Create Arithmetic Column"):
        try:
            if operation_type == "Column":
                if operation == "+":
                    df[new_col_name] = df[col1_name] + df[col2_name]
                elif operation == "-":
                    df[new_col_name] = df[col1_name] - df[col2_name]
                elif operation == "*":
                    df[new_col_name] = df[col1_name] * df[col2_name]
                elif operation == "/":
                    df[new_col_name] = df[col1_name] / df[col2_name]
                elif operation == "**":
                    df[new_col_name] = df[col1_name] ** df[col2_name]
                elif operation == "%":
                    df[new_col_name] = df[col1_name] % df[col2_name]
                formula = f"{col1_name} {operation} {col2_name}"
            else:
                if operation == "+":
                    df[new_col_name] = df[col1_name] + constant_value
                elif operation == "-":
                    df[new_col_name] = df[col1_name] - constant_value
                elif operation == "*":
                    df[new_col_name] = df[col1_name] * constant_value
                elif operation == "/":
                    df[new_col_name] = df[col1_name] / constant_value
                elif operation == "**":
                    df[new_col_name] = df[col1_name] ** constant_value
                elif operation == "%":
                    df[new_col_name] = df[col1_name] % constant_value
                formula = f"{col1_name} {operation} {constant_value}"

            st.success(f"✅ Created column '{new_col_name}' with formula: {formula}")
            st.dataframe(df[[col1_name, new_col_name]].head())

            # Download option
            csv_data = df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "data_with_calculated_column.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating arithmetic column: {str(e)}")


def create_statistical_column(df, numeric_cols):
    """Create statistical calculated columns"""
    st.markdown("#### 📊 Statistical Operations")

    col1, col2 = st.columns(2)
    with col1:
        selected_cols = st.multiselect("Select Columns:", numeric_cols, default=list(numeric_cols[:2]))
        stat_operation = st.selectbox("Statistical Operation:", [
            "sum", "mean", "median", "min", "max", "std", "var", "rolling_mean", "cumsum"
        ])

    with col2:
        new_col_name = st.text_input("New Column Name:", value=f"{stat_operation}_column")
        if stat_operation == "rolling_mean":
            window_size = st.number_input("Rolling Window Size:", min_value=2, value=5)

    if selected_cols and st.button("Create Statistical Column"):
        try:
            if stat_operation == "sum":
                df[new_col_name] = df[selected_cols].sum(axis=1)
            elif stat_operation == "mean":
                df[new_col_name] = df[selected_cols].mean(axis=1)
            elif stat_operation == "median":
                df[new_col_name] = df[selected_cols].median(axis=1)
            elif stat_operation == "min":
                df[new_col_name] = df[selected_cols].min(axis=1)
            elif stat_operation == "max":
                df[new_col_name] = df[selected_cols].max(axis=1)
            elif stat_operation == "std":
                df[new_col_name] = df[selected_cols].std(axis=1)
            elif stat_operation == "var":
                df[new_col_name] = df[selected_cols].var(axis=1)
            elif stat_operation == "rolling_mean":
                if len(selected_cols) == 1:
                    df[new_col_name] = df[selected_cols[0]].rolling(window=window_size).mean()
                else:
                    df[new_col_name] = df[selected_cols].mean(axis=1).rolling(window=window_size).mean()
            elif stat_operation == "cumsum":
                if len(selected_cols) == 1:
                    df[new_col_name] = df[selected_cols[0]].cumsum()
                else:
                    df[new_col_name] = df[selected_cols].sum(axis=1).cumsum()

            st.success(f"✅ Created column '{new_col_name}' using {stat_operation} of {selected_cols}")
            st.dataframe(df[selected_cols + [new_col_name]].head())

            # Download option
            csv_data = df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "data_with_statistical_column.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating statistical column: {str(e)}")


def create_custom_formula_column(df):
    """Create custom formula calculated columns"""
    st.markdown("#### 🔧 Custom Formula")

    col1, col2 = st.columns(2)
    with col1:
        new_col_name = st.text_input("New Column Name:", value="custom_column")
        formula = st.text_area(
            "Python Formula (use column names):",
            value="df['column_name'] * 2 + 1",
            help="Example: df['price'] * df['quantity'], np.sqrt(df['value']), df['col1'] + df['col2']"
        )

    with col2:
        st.markdown("**Available columns:**")
        for col in df.columns:
            st.write(f"- {col}")

        st.markdown("**Available functions:**")
        st.write("- np.sqrt, np.log, np.exp")
        st.write("- np.sin, np.cos, np.tan")
        st.write("- abs, round")

    if st.button("Create Custom Column"):
        try:
            # Safety check - only allow certain operations
            import numpy as np
            allowed_functions = {
                'np': np, 'sqrt': np.sqrt, 'log': np.log, 'exp': np.exp,
                'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                'abs': abs, 'round': round, 'df': df
            }

            # Execute the formula
            result = eval(formula, {"__builtins__": {}}, allowed_functions)
            df[new_col_name] = result

            st.success(f"✅ Created column '{new_col_name}' with custom formula")
            st.dataframe(df[[new_col_name]].head())

            # Download option
            csv_data = df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "data_with_custom_column.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating custom column: {str(e)}")
            st.warning("Make sure your formula uses valid Python syntax and references existing columns.")


def create_date_calculation_column(df):
    """Create date-based calculated columns"""
    st.markdown("#### 📅 Date Calculations")

    # Find date columns
    date_cols = []
    for col in df.columns:
        try:
            pd.to_datetime(df[col].dropna().head(10))
            date_cols.append(col)
        except:
            continue

    if len(date_cols) == 0:
        st.error("No date columns detected in the dataset")
        return

    col1, col2 = st.columns(2)
    with col1:
        date_col = st.selectbox("Date Column:", date_cols)
        date_operation = st.selectbox("Date Operation:", [
            "year", "month", "day", "weekday", "quarter", "days_since", "age_in_years"
        ])

    with col2:
        new_col_name = st.text_input("New Column Name:", value=f"{date_operation}_column")
        if date_operation in ["days_since", "age_in_years"]:
            reference_date = st.date_input("Reference Date:", value=pd.Timestamp.now().date())

    if st.button("Create Date Column"):
        try:
            date_series = pd.to_datetime(df[date_col])

            if date_operation == "year":
                df[new_col_name] = date_series.dt.year
            elif date_operation == "month":
                df[new_col_name] = date_series.dt.month
            elif date_operation == "day":
                df[new_col_name] = date_series.dt.day
            elif date_operation == "weekday":
                df[new_col_name] = date_series.dt.day_name()
            elif date_operation == "quarter":
                df[new_col_name] = date_series.dt.quarter
            elif date_operation == "days_since":
                ref_date = pd.Timestamp(reference_date)
                df[new_col_name] = (ref_date - date_series).dt.days
            elif date_operation == "age_in_years":
                ref_date = pd.Timestamp(reference_date)
                df[new_col_name] = (ref_date - date_series).dt.days / 365.25

            st.success(f"✅ Created column '{new_col_name}' from date column '{date_col}'")
            st.dataframe(df[[date_col, new_col_name]].head())

            # Download option
            csv_data = df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "data_with_date_column.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating date column: {str(e)}")


def data_merger():
    """Merge multiple datasets"""
    create_tool_header("Data Merger", "Merge and join multiple datasets", "🔗")

    # Allow multiple file uploads for merging
    uploaded_files = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=True)

    if uploaded_files and len(uploaded_files) >= 2:
        datasets = {}

        # Load all datasets
        for i, file in enumerate(uploaded_files):
            try:
                if file.name.endswith('.csv'):
                    df = FileHandler.process_csv_file(file)
                else:
                    df = pd.read_excel(file)

                if df is not None:
                    dataset_name = f"Dataset_{i + 1} ({file.name})"
                    datasets[dataset_name] = df

                    st.markdown(f"### {dataset_name}")
                    st.dataframe(df.head())
            except Exception as e:
                st.error(f"Error loading {file.name}: {str(e)}")

        if len(datasets) >= 2:
            perform_data_merge(datasets)
    else:
        st.info("Please upload at least 2 files to merge datasets")


def perform_data_merge(datasets):
    """Perform dataset merging operations"""
    dataset_names = list(datasets.keys())

    # Merge configuration
    st.markdown("### 🔗 Merge Configuration")
    col1, col2 = st.columns(2)

    with col1:
        left_dataset = st.selectbox("Left Dataset:", dataset_names)
        right_dataset = st.selectbox("Right Dataset:", [name for name in dataset_names if name != left_dataset])

    with col2:
        merge_type = st.selectbox("Merge Type:", ["inner", "left", "right", "outer"])

    # Column selection for joining
    left_df = datasets[left_dataset]
    right_df = datasets[right_dataset]

    st.markdown("### 🔑 Join Keys")
    col1, col2 = st.columns(2)

    with col1:
        left_key = st.selectbox("Left Join Key:", left_df.columns)

    with col2:
        right_key = st.selectbox("Right Join Key:", right_df.columns)

    # Advanced options
    st.markdown("### ⚙️ Advanced Options")
    col1, col2 = st.columns(2)

    with col1:
        handle_duplicates = st.selectbox("Handle Duplicate Columns:", ["suffix", "drop_right", "keep_both"])
        if handle_duplicates == "suffix":
            left_suffix = st.text_input("Left Suffix:", value="_left")
            right_suffix = st.text_input("Right Suffix:", value="_right")

    with col2:
        validate_merge = st.selectbox("Validate Merge:", ["one_to_one", "one_to_many", "many_to_one", "many_to_many"])

    if st.button("Merge Datasets"):
        try:
            # Prepare merge parameters
            merge_params = {
                'left': left_df,
                'right': right_df,
                'left_on': left_key,
                'right_on': right_key,
                'how': merge_type
            }

            # Handle duplicate columns
            if handle_duplicates == "suffix":
                merge_params['suffixes'] = (left_suffix, right_suffix)
            elif handle_duplicates == "drop_right":
                # Find common columns (except join keys) and drop from right
                common_cols = set(left_df.columns).intersection(set(right_df.columns))
                common_cols.discard(left_key)
                common_cols.discard(right_key)
                if common_cols:
                    right_df_filtered = right_df.drop(columns=list(common_cols))
                    merge_params['right'] = right_df_filtered

            # Perform merge
            merged_df = pd.merge(**merge_params)

            # Display results
            st.markdown("### 📊 Merged Dataset")
            st.dataframe(merged_df.head())

            # Merge statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Left Dataset Rows", len(left_df))
            with col2:
                st.metric("Right Dataset Rows", len(right_df))
            with col3:
                st.metric("Merged Rows", len(merged_df))
            with col4:
                st.metric("Total Columns", len(merged_df.columns))

            # Merge quality assessment
            st.markdown("### 📋 Merge Quality Assessment")
            left_matches = merged_df[left_key].notna().sum()
            total_left = len(left_df)
            match_rate = (left_matches / total_left) * 100 if total_left > 0 else 0

            st.info(f"Match Rate: {match_rate:.1f}% ({left_matches:,} out of {total_left:,} records from left dataset)")

            if merge_type in ['left', 'outer']:
                null_right = merged_df[right_df.columns].isnull().all(axis=1).sum()
                if null_right > 0:
                    st.warning(f"⚠️ {null_right:,} rows from left dataset have no match in right dataset")

            # Download option
            csv_data = merged_df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "merged_dataset.csv", "text/csv")

        except Exception as e:
            st.error(f"Error merging datasets: {str(e)}")


def data_splitter():
    """Split datasets into multiple parts"""
    create_tool_header("Data Splitter", "Split datasets into multiple parts", "✂️")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        else:
            df = pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head())
            perform_data_split(df)


def perform_data_split(df):
    """Perform dataset splitting operations"""

    st.markdown("### ✂️ Split Configuration")
    split_type = st.selectbox("Split Type:", [
        "Random Split", "Sequential Split", "Conditional Split", "Column-based Split"
    ])

    if split_type == "Random Split":
        create_random_split(df)
    elif split_type == "Sequential Split":
        create_sequential_split(df)
    elif split_type == "Conditional Split":
        create_conditional_split(df)
    elif split_type == "Column-based Split":
        create_column_based_split(df)


def create_random_split(df):
    """Create random data splits"""
    st.markdown("#### 🎲 Random Split")

    col1, col2 = st.columns(2)
    with col1:
        split_ratio = st.slider("Train/Test Split Ratio:", 0.1, 0.9, 0.8, 0.05)
        random_seed = st.number_input("Random Seed:", value=42, help="For reproducible splits")

    with col2:
        stratify_col = st.selectbox("Stratify by column (optional):",
                                    ['None'] + list(df.select_dtypes(include=['object']).columns))
        create_validation = st.checkbox("Create validation set", value=False)
        if create_validation:
            val_ratio = st.slider("Validation Ratio:", 0.05, 0.3, 0.2, 0.05)

    if st.button("Create Random Split"):
        try:
            from sklearn.model_selection import train_test_split

            if stratify_col != 'None':
                stratify_data = df[stratify_col]
            else:
                stratify_data = None

            if create_validation:
                # Three-way split
                train_df, temp_df = train_test_split(
                    df, test_size=(1 - split_ratio), random_state=random_seed, stratify=stratify_data
                )

                if stratify_col != 'None':
                    temp_stratify = temp_df[stratify_col]
                else:
                    temp_stratify = None

                val_size = val_ratio / (1 - split_ratio)
                val_df, test_df = train_test_split(
                    temp_df, test_size=(1 - val_size), random_state=random_seed + 1, stratify=temp_stratify
                )

                # Display results
                st.markdown("### 📊 Split Results")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Training Set", f"{len(train_df):,} rows ({len(train_df) / len(df) * 100:.1f}%)")
                    st.dataframe(train_df.head())
                with col2:
                    st.metric("Validation Set", f"{len(val_df):,} rows ({len(val_df) / len(df) * 100:.1f}%)")
                    st.dataframe(val_df.head())
                with col3:
                    st.metric("Test Set", f"{len(test_df):,} rows ({len(test_df) / len(df) * 100:.1f}%)")
                    st.dataframe(test_df.head())

                # Download options
                train_csv = train_df.to_csv(index=False)
                val_csv = val_df.to_csv(index=False)
                test_csv = test_df.to_csv(index=False)

                col1, col2, col3 = st.columns(3)
                with col1:
                    FileHandler.create_download_link(train_csv.encode(), "train_data.csv", "text/csv")
                with col2:
                    FileHandler.create_download_link(val_csv.encode(), "validation_data.csv", "text/csv")
                with col3:
                    FileHandler.create_download_link(test_csv.encode(), "test_data.csv", "text/csv")

            else:
                # Two-way split
                train_df, test_df = train_test_split(
                    df, test_size=(1 - split_ratio), random_state=random_seed, stratify=stratify_data
                )

                # Display results
                st.markdown("### 📊 Split Results")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Training Set", f"{len(train_df):,} rows ({len(train_df) / len(df) * 100:.1f}%)")
                    st.dataframe(train_df.head())
                with col2:
                    st.metric("Test Set", f"{len(test_df):,} rows ({len(test_df) / len(df) * 100:.1f}%)")
                    st.dataframe(test_df.head())

                # Download options
                train_csv = train_df.to_csv(index=False)
                test_csv = test_df.to_csv(index=False)

                col1, col2 = st.columns(2)
                with col1:
                    FileHandler.create_download_link(train_csv.encode(), "train_data.csv", "text/csv")
                with col2:
                    FileHandler.create_download_link(test_csv.encode(), "test_data.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating random split: {str(e)}")


def create_sequential_split(df):
    """Create sequential data splits"""
    st.markdown("#### 📅 Sequential Split")

    col1, col2 = st.columns(2)
    with col1:
        split_point = st.slider("Split Point (% for training):", 10, 90, 80, 5)
        split_direction = st.selectbox("Split Direction:", ["Top rows for training", "Bottom rows for training"])

    with col2:
        date_col = st.selectbox("Date column (optional):", ['None'] + list(df.columns))
        if date_col != 'None':
            st.info("Data will be sorted by date before splitting")

    if st.button("Create Sequential Split"):
        try:
            # Sort by date if specified
            if date_col != 'None':
                df_sorted = df.sort_values(date_col)
            else:
                df_sorted = df.copy()

            split_index = int(len(df_sorted) * split_point / 100)

            if split_direction == "Top rows for training":
                train_df = df_sorted.iloc[:split_index]
                test_df = df_sorted.iloc[split_index:]
            else:
                train_df = df_sorted.iloc[-split_index:]
                test_df = df_sorted.iloc[:-split_index]

            # Display results
            st.markdown("### 📊 Sequential Split Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Training Set", f"{len(train_df):,} rows")
                st.dataframe(train_df.head())
            with col2:
                st.metric("Test Set", f"{len(test_df):,} rows")
                st.dataframe(test_df.head())

            # Download options
            train_csv = train_df.to_csv(index=False)
            test_csv = test_df.to_csv(index=False)

            col1, col2 = st.columns(2)
            with col1:
                FileHandler.create_download_link(train_csv.encode(), "train_sequential.csv", "text/csv")
            with col2:
                FileHandler.create_download_link(test_csv.encode(), "test_sequential.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating sequential split: {str(e)}")


def create_conditional_split(df):
    """Create conditional data splits"""
    st.markdown("#### 🔍 Conditional Split")

    # Select column and condition
    col1, col2 = st.columns(2)
    with col1:
        filter_col = st.selectbox("Filter Column:", df.columns)

    with col2:
        if df[filter_col].dtype in ['object']:
            condition_type = st.selectbox("Condition Type:", ["equals", "contains", "in_list"])
        else:
            condition_type = st.selectbox("Condition Type:", ["equals", "greater_than", "less_than", "between"])

    # Condition value(s)
    if condition_type == "equals":
        if df[filter_col].dtype in ['object']:
            unique_values = df[filter_col].unique()
            condition_value = st.selectbox("Value:", unique_values)
        else:
            condition_value = st.number_input("Value:", value=float(df[filter_col].mean()))
    elif condition_type == "contains":
        condition_value = st.text_input("Contains text:")
    elif condition_type == "in_list":
        unique_values = df[filter_col].unique()
        condition_value = st.multiselect("Values:", unique_values)
    elif condition_type == "greater_than":
        condition_value = st.number_input("Greater than:", value=float(df[filter_col].median()))
    elif condition_type == "less_than":
        condition_value = st.number_input("Less than:", value=float(df[filter_col].median()))
    elif condition_type == "between":
        min_val, max_val = float(df[filter_col].min()), float(df[filter_col].max())
        condition_value = st.slider("Between:", min_val, max_val, (min_val, max_val))

    if st.button("Create Conditional Split"):
        try:
            # Apply condition
            if condition_type == "equals":
                mask = df[filter_col] == condition_value
            elif condition_type == "contains":
                mask = df[filter_col].astype(str).str.contains(condition_value, na=False)
            elif condition_type == "in_list":
                mask = df[filter_col].isin(condition_value)
            elif condition_type == "greater_than":
                mask = df[filter_col] > condition_value
            elif condition_type == "less_than":
                mask = df[filter_col] < condition_value
            elif condition_type == "between":
                mask = (df[filter_col] >= condition_value[0]) & (df[filter_col] <= condition_value[1])

            subset1 = df[mask]
            subset2 = df[~mask]

            # Display results
            st.markdown("### 📊 Conditional Split Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Subset 1 (Condition True)", f"{len(subset1):,} rows")
                st.dataframe(subset1.head())
            with col2:
                st.metric("Subset 2 (Condition False)", f"{len(subset2):,} rows")
                st.dataframe(subset2.head())

            # Download options
            subset1_csv = subset1.to_csv(index=False)
            subset2_csv = subset2.to_csv(index=False)

            col1, col2 = st.columns(2)
            with col1:
                FileHandler.create_download_link(subset1_csv.encode(), "subset_condition_true.csv", "text/csv")
            with col2:
                FileHandler.create_download_link(subset2_csv.encode(), "subset_condition_false.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating conditional split: {str(e)}")


def create_column_based_split(df):
    """Create column-based data splits"""
    st.markdown("#### 📊 Column-based Split")

    categorical_cols = df.select_dtypes(include=['object']).columns

    if len(categorical_cols) == 0:
        st.error("Need at least 1 categorical column for column-based split")
        return

    col1, col2 = st.columns(2)
    with col1:
        split_col = st.selectbox("Split by Column:", categorical_cols)

    with col2:
        unique_values = df[split_col].unique()
        st.write(f"Unique values in {split_col}: {len(unique_values)}")
        if len(unique_values) <= 10:
            for val in unique_values:
                count = (df[split_col] == val).sum()
                st.write(f"- {val}: {count:,} rows")

    if st.button("Create Column-based Split"):
        try:
            unique_values = df[split_col].unique()
            splits = {}

            for value in unique_values:
                subset = df[df[split_col] == value]
                splits[str(value)] = subset

            # Display results
            st.markdown("### 📊 Column-based Split Results")

            for value, subset in splits.items():
                st.markdown(f"#### {split_col} = {value}")
                st.metric("Rows", f"{len(subset):,}")
                st.dataframe(subset.head(3))

                # Download option
                subset_csv = subset.to_csv(index=False)
                safe_filename = "".join(c for c in str(value) if c.isalnum() or c in (' ', '-', '_')).rstrip()
                FileHandler.create_download_link(subset_csv.encode(), f"subset_{safe_filename}.csv", "text/csv")

        except Exception as e:
            st.error(f"Error creating column-based split: {str(e)}")


def text_mining():
    """Extract and analyze text data from various sources"""
    create_tool_header("Text Mining", "Extract key information and patterns from text data", "📄")

    # Input options
    input_method = st.selectbox("Choose input method:", [
        "Upload Text File", "Paste Text", "Upload CSV with Text Column"
    ])

    text_data = None

    if input_method == "Upload Text File":
        uploaded_file = FileHandler.upload_files(['txt', 'csv'], accept_multiple=False)
        if uploaded_file:
            text_data = FileHandler.process_text_file(uploaded_file[0])

    elif input_method == "Paste Text":
        text_data = st.text_area("Enter your text:", height=200,
                                 placeholder="Paste your text here for analysis...")

    elif input_method == "Upload CSV with Text Column":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                text_cols = df.select_dtypes(include=['object']).columns
                if len(text_cols) > 0:
                    selected_col = st.selectbox("Select text column:", text_cols)
                    text_data = " ".join(df[selected_col].dropna().astype(str))

    if text_data:
        st.markdown("### 📊 Text Analysis Results")

        # Basic statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Characters", len(text_data))
        with col2:
            word_count = len(text_data.split())
            st.metric("Total Words", word_count)
        with col3:
            sentence_count = len([s for s in text_data.split('.') if s.strip()])
            st.metric("Sentences", sentence_count)
        with col4:
            avg_word_length = np.mean([len(word) for word in text_data.split()])
            st.metric("Avg Word Length", f"{avg_word_length:.1f}")

        # Text cleaning options
        st.markdown("### 🧹 Text Preprocessing")
        cleaning_options = st.multiselect("Select preprocessing options:", [
            "Remove punctuation", "Convert to lowercase", "Remove extra whitespace", "Remove numbers"
        ], default=["Convert to lowercase", "Remove extra whitespace"])

        processed_text = preprocess_text(text_data, cleaning_options)

        # Key phrase extraction
        st.markdown("### 🔍 Key Phrases & Entities")

        col1, col2 = st.columns(2)

        with col1:
            # Extract key terms using TF-IDF
            key_terms = extract_key_terms(processed_text)
            st.markdown("**Top Key Terms:**")
            for term, score in key_terms[:10]:
                st.write(f"• {term}: {score:.3f}")

        with col2:
            # Extract entities (basic regex-based)
            entities = extract_entities(text_data)
            st.markdown("**Extracted Entities:**")
            for entity_type, items in entities.items():
                if items:
                    st.write(f"**{entity_type}:** {', '.join(items[:5])}")

        # Text summary using AI
        if st.button("Generate AI Summary"):
            try:
                summary = generate_text_summary(text_data)
                st.markdown("### 📋 AI-Generated Summary")
                st.write(summary)
            except Exception as e:
                st.error(f"Error generating summary: {str(e)}")


def sentiment_analysis():
    """Analyze sentiment and emotions in text data"""
    create_tool_header("Sentiment Analysis", "Analyze emotional tone and sentiment in text", "😊")

    # Input options
    input_method = st.selectbox("Choose input method:", [
        "Upload Text File", "Paste Text", "Upload CSV with Text Column"
    ])

    text_data = None

    if input_method == "Upload Text File":
        uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)
        if uploaded_file:
            text_data = FileHandler.process_text_file(uploaded_file[0])

    elif input_method == "Paste Text":
        text_data = st.text_area("Enter your text:", height=200,
                                 placeholder="Paste your text here for sentiment analysis...")

    elif input_method == "Upload CSV with Text Column":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                text_cols = df.select_dtypes(include=['object']).columns
                if len(text_cols) > 0:
                    selected_col = st.selectbox("Select text column:", text_cols)
                    perform_batch_sentiment_analysis(df, selected_col)
                    return

    if text_data:
        st.markdown("### 📊 Sentiment Analysis Results")

        # Basic sentiment analysis using AI
        try:
            sentiment_result = analyze_sentiment_with_ai(text_data)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Overall Sentiment", sentiment_result.get("sentiment", "Unknown"))

            with col2:
                confidence = sentiment_result.get("confidence", 0)
                st.metric("Confidence", f"{confidence:.1%}")

            with col3:
                polarity = sentiment_result.get("polarity", 0)
                st.metric("Polarity Score", f"{polarity:.2f}")

            # Emotion analysis
            emotions = sentiment_result.get("emotions", {})
            if emotions:
                st.markdown("### 😊 Emotion Breakdown")
                emotion_data = list(emotions.items())
                emotion_df = pd.DataFrame(emotion_data, columns=['Emotion', 'Score'])
                emotion_df = emotion_df.sort_values('Score', ascending=False)

                # Create emotion chart
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.barh(emotion_df['Emotion'], emotion_df['Score'])
                ax.set_xlabel('Emotion Score')
                ax.set_title('Emotion Analysis Results')
                st.pyplot(fig)
                plt.close()

            # Detailed analysis
            st.markdown("### 📝 Detailed Analysis")
            st.write(sentiment_result.get("explanation", "No detailed analysis available."))

        except Exception as e:
            st.error(f"Error performing sentiment analysis: {str(e)}")
            # Fallback to basic analysis
            basic_sentiment = perform_basic_sentiment_analysis(text_data)
            st.write("**Basic Sentiment Analysis:**")
            st.json(basic_sentiment)


def word_frequency():
    """Analyze word frequency and create visualizations"""
    create_tool_header("Word Frequency Analysis", "Analyze word usage patterns and frequencies", "📊")

    # Input options
    input_method = st.selectbox("Choose input method:", [
        "Upload Text File", "Paste Text", "Upload CSV with Text Column"
    ])

    text_data = None

    if input_method == "Upload Text File":
        uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)
        if uploaded_file:
            text_data = FileHandler.process_text_file(uploaded_file[0])

    elif input_method == "Paste Text":
        text_data = st.text_area("Enter your text:", height=200,
                                 placeholder="Paste your text here for word frequency analysis...")

    elif input_method == "Upload CSV with Text Column":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                text_cols = df.select_dtypes(include=['object']).columns
                if len(text_cols) > 0:
                    selected_col = st.selectbox("Select text column:", text_cols)
                    text_data = " ".join(df[selected_col].dropna().astype(str))

    if text_data:
        # Analysis options
        st.markdown("### ⚙️ Analysis Options")

        col1, col2 = st.columns(2)
        with col1:
            min_word_length = st.slider("Minimum word length:", 1, 10, 3)
            top_n = st.slider("Number of top words to show:", 10, 100, 25)

        with col2:
            remove_stopwords = st.checkbox("Remove common words (stopwords)", True)
            case_sensitive = st.checkbox("Case sensitive analysis", False)

        # Process text
        processed_words = process_text_for_frequency(text_data, min_word_length,
                                                     remove_stopwords, case_sensitive)

        if processed_words:
            # Calculate frequencies
            word_freq = Counter(processed_words)

            st.markdown("### 📊 Word Frequency Results")

            # Display metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Words", len(processed_words))
            with col2:
                st.metric("Unique Words", len(word_freq))
            with col3:
                st.metric("Most Common Word", word_freq.most_common(1)[0][0])
            with col4:
                st.metric("Highest Frequency", word_freq.most_common(1)[0][1])

            # Top words table
            st.markdown("### 📋 Top Words")
            top_words = word_freq.most_common(top_n)
            freq_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
            freq_df['Percentage'] = (freq_df['Frequency'] / len(processed_words) * 100).round(2)
            st.dataframe(freq_df)

            # Visualizations
            st.markdown("### 📈 Visualizations")

            visualization_type = st.selectbox("Choose visualization:", [
                "Bar Chart", "Word Cloud", "Frequency Distribution"
            ])

            if visualization_type == "Bar Chart":
                create_frequency_bar_chart(freq_df.head(20))
            elif visualization_type == "Word Cloud":
                create_word_cloud(dict(top_words))
            elif visualization_type == "Frequency Distribution":
                create_frequency_distribution(word_freq)

            # Download results
            csv_data = freq_df.to_csv(index=False)
            FileHandler.create_download_link(csv_data.encode(), "word_frequency_analysis.csv", "text/csv")


def ngram_analysis():
    """Perform N-gram analysis to find common word sequences"""
    create_tool_header("N-gram Analysis", "Analyze word sequences and phrases", "🔗")

    # Input options
    input_method = st.selectbox("Choose input method:", [
        "Upload Text File", "Paste Text", "Upload CSV with Text Column"
    ])

    text_data = None

    if input_method == "Upload Text File":
        uploaded_file = FileHandler.upload_files(['txt'], accept_multiple=False)
        if uploaded_file:
            text_data = FileHandler.process_text_file(uploaded_file[0])

    elif input_method == "Paste Text":
        text_data = st.text_area("Enter your text:", height=200,
                                 placeholder="Paste your text here for n-gram analysis...")

    elif input_method == "Upload CSV with Text Column":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                text_cols = df.select_dtypes(include=['object']).columns
                if len(text_cols) > 0:
                    selected_col = st.selectbox("Select text column:", text_cols)
                    text_data = " ".join(df[selected_col].dropna().astype(str))

    if text_data:
        # Analysis options
        st.markdown("### ⚙️ Analysis Options")

        col1, col2, col3 = st.columns(3)

        with col1:
            n_value = st.selectbox("N-gram size:", [2, 3, 4, 5], index=0)

        with col2:
            top_n = st.slider("Number of top n-grams:", 10, 100, 20)

        with col3:
            min_frequency = st.slider("Minimum frequency:", 1, 10, 2)

        # Advanced options
        with st.expander("Advanced Options"):
            remove_stopwords = st.checkbox("Remove stopwords", True)
            case_sensitive = st.checkbox("Case sensitive", False)
            include_punctuation = st.checkbox("Include punctuation", False)

        if st.button("Analyze N-grams"):
            # Process text and extract n-grams
            ngrams = extract_ngrams(text_data, n_value, remove_stopwords,
                                    case_sensitive, include_punctuation)

            # Filter by minimum frequency
            filtered_ngrams = {ngram: freq for ngram, freq in ngrams.items()
                               if freq >= min_frequency}

            if filtered_ngrams:
                # Sort by frequency
                sorted_ngrams = sorted(filtered_ngrams.items(), key=lambda x: x[1], reverse=True)
                top_ngrams = sorted_ngrams[:top_n]

                st.markdown(f"### 📊 Top {n_value}-grams Results")

                # Display metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total N-grams", len(filtered_ngrams))
                with col2:
                    st.metric("Most Common", f'"{top_ngrams[0][0]}"')
                with col3:
                    st.metric("Highest Frequency", top_ngrams[0][1])
                with col4:
                    avg_freq = np.mean(list(filtered_ngrams.values()))
                    st.metric("Average Frequency", f"{avg_freq:.1f}")

                # Results table
                ngram_df = pd.DataFrame(top_ngrams, columns=[f'{n_value}-gram', 'Frequency'])
                st.dataframe(ngram_df)

                # Visualization
                st.markdown("### 📈 Visualization")
                create_ngram_chart(ngram_df.head(15), n_value)

                # Context analysis
                if st.button("Show Context Examples"):
                    st.markdown("### 📝 Context Examples")
                    show_ngram_contexts(text_data, top_ngrams[:5])

                # Download results
                csv_data = ngram_df.to_csv(index=False)
                FileHandler.create_download_link(csv_data.encode(), f"{n_value}gram_analysis.csv", "text/csv")

            else:
                st.warning(f"No {n_value}-grams found with minimum frequency of {min_frequency}")


def topic_modeling():
    """Perform topic modeling to discover hidden themes in text"""
    create_tool_header("Topic Modeling", "Discover hidden topics and themes in text collections", "🎯")

    # Input options
    input_method = st.selectbox("Choose input method:", [
        "Upload Multiple Text Files", "Upload CSV with Text Column", "Paste Multiple Texts"
    ])

    documents = []

    if input_method == "Upload Multiple Text Files":
        uploaded_files = FileHandler.upload_files(['txt'], accept_multiple=True)
        if uploaded_files:
            for file in uploaded_files:
                text = FileHandler.process_text_file(file)
                if text:
                    documents.append(text)

    elif input_method == "Upload CSV with Text Column":
        uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
        if uploaded_file:
            df = FileHandler.process_csv_file(uploaded_file[0])
            if df is not None:
                text_cols = df.select_dtypes(include=['object']).columns
                if len(text_cols) > 0:
                    selected_col = st.selectbox("Select text column:", text_cols)
                    documents = df[selected_col].dropna().astype(str).tolist()

    elif input_method == "Paste Multiple Texts":
        st.info("Enter multiple texts separated by '---' on a new line")
        text_input = st.text_area("Enter your texts:", height=300,
                                  placeholder="Text 1\n---\nText 2\n---\nText 3")
        if text_input:
            documents = [doc.strip() for doc in text_input.split('---') if doc.strip()]

    if documents and len(documents) >= 2:
        st.info(f"Loaded {len(documents)} documents for topic modeling")

        # Modeling options
        st.markdown("### ⚙️ Topic Modeling Options")

        col1, col2, col3 = st.columns(3)

        with col1:
            num_topics = st.slider("Number of topics:", 2, 20, 5)

        with col2:
            max_features = st.slider("Max features:", 100, 2000, 500)

        with col3:
            min_df = st.slider("Min document frequency:", 1, 10, 2)

        # Advanced options
        with st.expander("Advanced Options"):
            algorithm = st.selectbox("Algorithm:", ["Latent Dirichlet Allocation (LDA)", "K-Means Clustering"])
            remove_stopwords = st.checkbox("Remove stopwords", True)
            max_iter = st.slider("Max iterations:", 10, 100, 20)

        if st.button("Run Topic Modeling"):
            with st.spinner("Running topic modeling analysis..."):
                try:
                    if algorithm == "Latent Dirichlet Allocation (LDA)":
                        results = perform_lda_topic_modeling(documents, num_topics, max_features,
                                                             min_df, remove_stopwords, max_iter)
                    else:
                        results = perform_kmeans_topic_modeling(documents, num_topics, max_features,
                                                                min_df, remove_stopwords)

                    display_topic_modeling_results(results, num_topics)

                except Exception as e:
                    st.error(f"Error in topic modeling: {str(e)}")

    elif documents:
        st.warning("Need at least 2 documents for meaningful topic modeling.")

    else:
        st.info("Please provide text documents to analyze.")


# Helper functions for text analytics

def preprocess_text(text, options):
    """Preprocess text based on selected options"""
    processed = text

    if "Convert to lowercase" in options:
        processed = processed.lower()

    if "Remove punctuation" in options:
        processed = processed.translate(str.maketrans('', '', string.punctuation))

    if "Remove numbers" in options:
        processed = re.sub(r'\d+', '', processed)

    if "Remove extra whitespace" in options:
        processed = re.sub(r'\s+', ' ', processed).strip()

    return processed


def extract_key_terms(text, max_features=20):
    """Extract key terms using TF-IDF"""
    try:
        vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([text])

        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]

        terms_scores = list(zip(feature_names, scores))
        return sorted(terms_scores, key=lambda x: x[1], reverse=True)
    except:
        return []


def extract_entities(text):
    """Basic entity extraction using regex patterns"""
    entities = {
        'Emails': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text),
        'Phone Numbers': re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text),
        'URLs': re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text),
        'Dates': re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', text)
    }

    return entities


def generate_text_summary(text):
    """Generate text summary using AI"""
    try:
        prompt = f"""Please provide a concise summary of the following text in 2-3 sentences:

{text[:2000]}...

Summary:"""

        response = ai_client.generate_text(prompt)
        return response
    except Exception as e:
        return f"Error generating summary: {str(e)}"


def analyze_sentiment_with_ai(text):
    """Analyze sentiment using AI"""
    try:
        prompt = f"""Analyze the sentiment of the following text and provide:
1. Overall sentiment (Positive/Negative/Neutral)
2. Confidence score (0-1)
3. Polarity score (-1 to 1, where -1 is very negative, 0 is neutral, 1 is very positive)
4. Emotion breakdown (joy, anger, fear, sadness, surprise, disgust) with scores 0-1
5. Brief explanation

Text: {text[:1000]}

Please respond in JSON format:
{{
    "sentiment": "Positive/Negative/Neutral",
    "confidence": 0.85,
    "polarity": 0.6,
    "emotions": {{"joy": 0.7, "anger": 0.1, "fear": 0.0, "sadness": 0.1, "surprise": 0.1, "disgust": 0.0}},
    "explanation": "Brief explanation of the analysis"
}}"""

        response = ai_client.generate_text(prompt)

        # Try to parse JSON response
        try:
            import json
            return json.loads(response)
        except:
            # Fallback response
            return {
                "sentiment": "Neutral",
                "confidence": 0.5,
                "polarity": 0.0,
                "emotions": {"joy": 0.2, "anger": 0.2, "fear": 0.2, "sadness": 0.2, "surprise": 0.1, "disgust": 0.1},
                "explanation": response
            }

    except Exception as e:
        return perform_basic_sentiment_analysis(text)


def perform_basic_sentiment_analysis(text):
    """Basic sentiment analysis fallback"""
    # Simple word-based sentiment analysis
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'like', 'happy', 'joy']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'dislike', 'sad', 'angry', 'disappointed', 'frustrated']

    words = text.lower().split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    total_sentiment_words = positive_count + negative_count

    if total_sentiment_words == 0:
        return {"sentiment": "Neutral", "positive_count": 0, "negative_count": 0, "confidence": 0.5}

    polarity = (positive_count - negative_count) / total_sentiment_words

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    confidence = min(total_sentiment_words / len(words), 1.0)

    return {
        "sentiment": sentiment,
        "polarity": polarity,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "confidence": confidence
    }


def perform_batch_sentiment_analysis(df, text_column):
    """Perform sentiment analysis on a DataFrame column"""
    st.markdown("### 📊 Batch Sentiment Analysis Results")

    with st.spinner("Analyzing sentiment for all texts..."):
        sentiments = []
        polarities = []
        confidences = []

        for text in df[text_column].dropna():
            result = perform_basic_sentiment_analysis(str(text))
            sentiments.append(result['sentiment'])
            polarities.append(result['polarity'])
            confidences.append(result['confidence'])

        # Add results to dataframe
        results_df = df.copy()
        results_df['Sentiment'] = sentiments
        results_df['Polarity'] = polarities
        results_df['Confidence'] = confidences

        st.dataframe(results_df)

        # Summary statistics
        col1, col2, col3 = st.columns(3)

        with col1:
            sentiment_counts = pd.Series(sentiments).value_counts()
            st.markdown("**Sentiment Distribution:**")
            st.write(sentiment_counts)

        with col2:
            avg_polarity = np.mean(polarities)
            st.metric("Average Polarity", f"{avg_polarity:.3f}")

        with col3:
            avg_confidence = np.mean(confidences)
            st.metric("Average Confidence", f"{avg_confidence:.3f}")

        # Download results
        csv_data = results_df.to_csv(index=False)
        FileHandler.create_download_link(csv_data.encode(), "sentiment_analysis_results.csv", "text/csv")


def process_text_for_frequency(text, min_length, remove_stopwords, case_sensitive):
    """Process text for frequency analysis"""
    # Basic cleaning
    if not case_sensitive:
        text = text.lower()

    # Remove punctuation and split into words
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    # Filter by minimum length
    words = [word for word in words if len(word) >= min_length]

    # Remove stopwords if requested
    if remove_stopwords:
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                        'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
                        'before', 'after', 'above', 'below', 'between', 'among', 'is', 'are',
                        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does',
                        'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this',
                        'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'}
        words = [word for word in words if word not in common_words]

    return words


def create_frequency_bar_chart(freq_df):
    """Create a bar chart for word frequencies"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(freq_df['Word'], freq_df['Frequency'])
    ax.set_xlabel('Frequency')
    ax.set_title('Top Words by Frequency')
    ax.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()


def create_word_cloud(word_freq_dict):
    """Create a word cloud visualization"""
    st.info("Word cloud functionality requires additional libraries. Showing text-based representation instead.")

    # Create a simple text-based word cloud representation
    sorted_words = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)

    word_cloud_text = ""
    for word, freq in sorted_words[:30]:
        size = min(freq * 2, 20)  # Scale frequency to text repetition
        word_cloud_text += (word + " ") * max(1, size // 5)

    st.text_area("Word Cloud (Text Representation):", word_cloud_text, height=200)


def create_frequency_distribution(word_freq):
    """Create frequency distribution chart"""
    frequencies = list(word_freq.values())

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(frequencies, bins=20, edgecolor='black')
    ax.set_xlabel('Word Frequency')
    ax.set_ylabel('Number of Words')
    ax.set_title('Distribution of Word Frequencies')
    st.pyplot(fig)
    plt.close()


def extract_ngrams(text, n, remove_stopwords, case_sensitive, include_punctuation):
    """Extract n-grams from text"""
    # Preprocess text
    if not case_sensitive:
        text = text.lower()

    if not include_punctuation:
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    # Remove stopwords if requested
    if remove_stopwords:
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        words = [word for word in words if word not in common_words]

    # Generate n-grams
    ngrams = {}
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i + n])
        ngrams[ngram] = ngrams.get(ngram, 0) + 1

    return ngrams


def create_ngram_chart(ngram_df, n_value):
    """Create visualization for n-gram analysis"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(ngram_df.iloc[::-1][f'{n_value}-gram'], ngram_df.iloc[::-1]['Frequency'])
    ax.set_xlabel('Frequency')
    ax.set_title(f'Top {n_value}-grams by Frequency')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()


def show_ngram_contexts(text, top_ngrams):
    """Show context examples for n-grams"""
    for ngram, freq in top_ngrams:
        st.markdown(f"**{ngram}** (appears {freq} times)")

        # Find contexts where this n-gram appears
        sentences = text.split('.')
        contexts = []

        for sentence in sentences:
            if ngram.lower() in sentence.lower():
                # Highlight the n-gram in the sentence
                highlighted = sentence.replace(ngram, f"**{ngram}**")
                contexts.append(highlighted.strip())
                if len(contexts) >= 3:  # Show max 3 contexts
                    break

        for context in contexts:
            st.write(f"• {context}")

        st.markdown("---")


def perform_lda_topic_modeling(documents, num_topics, max_features, min_df, remove_stopwords, max_iter):
    """Perform LDA topic modeling"""
    # Prepare text data
    if remove_stopwords:
        stop_words = 'english'
    else:
        stop_words = None

    # Vectorize the documents
    vectorizer = CountVectorizer(max_features=max_features, min_df=min_df,
                                 stop_words=stop_words, lowercase=True)
    doc_term_matrix = vectorizer.fit_transform(documents)

    # Run LDA
    lda = LatentDirichletAllocation(n_components=num_topics, max_iter=max_iter,
                                    random_state=42)
    lda.fit(doc_term_matrix)

    # Extract results
    feature_names = vectorizer.get_feature_names_out()

    # Get top words for each topic
    topics = []
    for topic_idx, topic in enumerate(lda.components_):
        top_words_idx = topic.argsort()[-10:][::-1]
        top_words = [feature_names[i] for i in top_words_idx]
        topics.append({
            'topic_id': topic_idx,
            'top_words': top_words,
            'word_weights': [topic[i] for i in top_words_idx]
        })

    # Get document-topic assignments
    doc_topic_probs = lda.transform(doc_term_matrix)

    return {
        'topics': topics,
        'doc_topic_probs': doc_topic_probs,
        'documents': documents,
        'algorithm': 'LDA'
    }


def perform_kmeans_topic_modeling(documents, num_topics, max_features, min_df, remove_stopwords):
    """Perform K-means clustering for topic modeling"""
    # Prepare text data
    if remove_stopwords:
        stop_words = 'english'
    else:
        stop_words = None

    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer(max_features=max_features, min_df=min_df,
                                 stop_words=stop_words, lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_topics, random_state=42)
    clusters = kmeans.fit_predict(tfidf_matrix)

    # Extract top terms for each cluster
    feature_names = vectorizer.get_feature_names_out()

    topics = []
    for i in range(num_topics):
        # Get centroid for this cluster
        centroid = kmeans.cluster_centers_[i]
        # Get indices of top terms
        top_indices = centroid.argsort()[-10:][::-1]
        top_words = [feature_names[idx] for idx in top_indices]

        topics.append({
            'topic_id': i,
            'top_words': top_words,
            'word_weights': [centroid[idx] for idx in top_indices]
        })

    return {
        'topics': topics,
        'doc_assignments': clusters,
        'documents': documents,
        'algorithm': 'K-Means'
    }


def display_topic_modeling_results(results, num_topics):
    """Display topic modeling results"""
    st.markdown(f"### 🎯 Topic Modeling Results ({results['algorithm']})")

    # Display topics
    for topic in results['topics']:
        with st.expander(f"Topic {topic['topic_id']} - {', '.join(topic['top_words'][:3])}"):
            st.markdown(f"**Top words:** {', '.join(topic['top_words'])}")

            # Create word importance chart
            word_df = pd.DataFrame({
                'Word': topic['top_words'],
                'Weight': topic['word_weights']
            })

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.barh(word_df['Word'][::-1], word_df['Weight'][::-1])
            ax.set_xlabel('Word Importance')
            ax.set_title(f'Topic {topic["topic_id"]} - Word Weights')
            st.pyplot(fig)
            plt.close()

    # Document assignments
    if 'doc_topic_probs' in results:
        st.markdown("### 📄 Document-Topic Assignments")

        # Show top documents for each topic
        doc_topic_probs = results['doc_topic_probs']
        documents = results['documents']

        for topic_idx in range(num_topics):
            topic_docs = []
            for doc_idx, probs in enumerate(doc_topic_probs):
                if probs[topic_idx] > 0.3:  # Threshold for topic assignment
                    topic_docs.append((doc_idx, probs[topic_idx], documents[doc_idx][:200] + "..."))

            if topic_docs:
                st.markdown(f"**Topic {topic_idx} Documents:**")
                for doc_idx, prob, preview in sorted(topic_docs, key=lambda x: x[1], reverse=True)[:3]:
                    st.write(f"Doc {doc_idx} (prob: {prob:.3f}): {preview}")

    elif 'doc_assignments' in results:
        st.markdown("### 📄 Document Cluster Assignments")

        assignments = results['doc_assignments']
        documents = results['documents']

        for topic_idx in range(num_topics):
            topic_docs = [i for i, cluster in enumerate(assignments) if cluster == topic_idx]

            if topic_docs:
                st.markdown(f"**Topic {topic_idx} ({len(topic_docs)} documents):**")
                for doc_idx in topic_docs[:3]:  # Show first 3 documents
                    preview = documents[doc_idx][:200] + "..."
                    st.write(f"Doc {doc_idx}: {preview}")


def seasonality_analysis():
    """Analyze seasonal patterns in time series data"""
    create_tool_header("Seasonality Analysis", "Analyze seasonal patterns in time series data", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        try:
            if uploaded_file[0].name.endswith('.csv'):
                df = FileHandler.process_csv_file(uploaded_file[0])
            else:
                df = pd.read_excel(uploaded_file[0])

            if df is not None:
                st.dataframe(df.head())

                # Find date and numeric columns
                date_cols = []
                for col in df.columns:
                    if df[col].dtype == 'object':
                        try:
                            pd.to_datetime(df[col], errors='raise')
                            date_cols.append(col)
                        except:
                            continue
                    elif pd.api.types.is_datetime64_any_dtype(df[col]):
                        date_cols.append(col)

                numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

                if len(date_cols) > 0 and len(numeric_cols) > 0:
                    # Column selection
                    col1, col2 = st.columns(2)
                    with col1:
                        date_col = st.selectbox("📅 Date/Time Column:", date_cols)
                    with col2:
                        value_col = st.selectbox("📊 Value Column:", numeric_cols)

                    # Analysis parameters
                    st.markdown("### 🔧 Analysis Parameters")
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        period_method = st.selectbox(
                            "📊 Period Detection:",
                            ["Auto-detect", "Manual"]
                        )

                    with col2:
                        if period_method == "Manual":
                            seasonal_period = st.number_input(
                                "Seasonal Period:",
                                min_value=2, max_value=365, value=12,
                                help="E.g., 12 for monthly, 4 for quarterly, 7 for weekly"
                            )
                        else:
                            seasonal_period = None

                    with col3:
                        decomp_model = st.selectbox(
                            "📈 Decomposition Model:",
                            ["Additive", "Multiplicative"]
                        )

                    # Analysis options
                    st.markdown("### 🎯 Analysis Options")
                    col1, col2 = st.columns(2)

                    with col1:
                        show_autocorr = st.checkbox("Show Autocorrelation Analysis", value=True)
                        show_subseries = st.checkbox("Show Seasonal Subseries Plots", value=True)

                    with col2:
                        show_strength = st.checkbox("Calculate Seasonal Strength", value=True)
                        show_patterns = st.checkbox("Show Seasonal Patterns by Period", value=True)

                    if st.button("🚀 Analyze Seasonality", type="primary"):
                        perform_seasonality_analysis(
                            df, date_col, value_col, seasonal_period, decomp_model,
                            show_autocorr, show_subseries, show_strength, show_patterns
                        )

                else:
                    if len(date_cols) == 0:
                        st.error("❌ No date/time columns found. Please ensure your data has at least one date column.")
                    if len(numeric_cols) == 0:
                        st.error("❌ No numeric columns found. Please ensure your data has at least one numeric column.")

        except Exception as e:
            st.error(f"❌ Error loading data: {str(e)}")
    else:
        st.info("📁 Please upload a CSV or Excel file to begin seasonality analysis.")


def perform_seasonality_analysis(df, date_col, value_col, seasonal_period, decomp_model,
                                 show_autocorr, show_subseries, show_strength, show_patterns):
    """Perform comprehensive seasonality analysis"""
    try:
        # Prepare data
        df_clean = df[[date_col, value_col]].copy().dropna()
        df_clean[date_col] = pd.to_datetime(df_clean[date_col])
        df_clean = df_clean.sort_values(date_col).reset_index(drop=True)

        if len(df_clean) < 10:
            st.error("❌ Need at least 10 data points for seasonality analysis.")
            return

        values = df_clean[value_col].values
        dates = df_clean[date_col]

        st.markdown("### 📊 Data Overview")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Data Points", len(df_clean))
        with col2:
            st.metric("Date Range", f"{(dates.max() - dates.min()).days} days")
        with col3:
            st.metric("Mean Value", f"{np.mean(values):.2f}")
        with col4:
            st.metric("Std Deviation", f"{np.std(values):.2f}")

        # Auto-detect seasonal period if requested
        if seasonal_period is None:
            seasonal_period = detect_seasonal_period(values, dates)
            st.info(f"🔍 Auto-detected seasonal period: {seasonal_period}")

        # Original time series plot
        st.markdown("### 📈 Original Time Series")
        plot_original_series(dates, values, value_col)

        # Autocorrelation analysis
        if show_autocorr:
            st.markdown("### 🔗 Autocorrelation Analysis")
            plot_autocorrelation(values, seasonal_period)

        # Classical decomposition
        st.markdown("### 🧩 Seasonal Decomposition")
        trend, seasonal, residual = perform_classical_decomposition(
            values, seasonal_period, decomp_model.lower()
        )
        plot_decomposition(dates, values, trend, seasonal, residual, decomp_model)

        # Seasonal patterns by period
        if show_patterns:
            st.markdown("### 📅 Seasonal Patterns Analysis")
            analyze_seasonal_patterns(dates, values, seasonal, seasonal_period)

        # Seasonal subseries plots
        if show_subseries:
            st.markdown("### 📊 Seasonal Subseries Analysis")
            plot_seasonal_subseries(dates, values, seasonal_period)

        # Seasonal strength metrics
        if show_strength:
            st.markdown("### 💪 Seasonal Strength Metrics")
            calculate_seasonal_strength(values, trend, seasonal, residual, decomp_model)

        # Generate downloadable results
        st.markdown("### 📥 Download Results")
        create_seasonality_download(df_clean, trend, seasonal, residual, seasonal_period, decomp_model)

        st.success("✅ Seasonality analysis completed successfully!")

    except Exception as e:
        st.error(f"❌ Error in seasonality analysis: {str(e)}")
        import traceback
        st.error(f"Debug info: {traceback.format_exc()}")


def detect_seasonal_period(values, dates):
    """Auto-detect seasonal period using autocorrelation"""
    try:
        from scipy import signal
        from scipy.stats import pearsonr

        # Calculate autocorrelation for different lags
        max_lag = min(len(values) // 3, 100)  # Reasonable maximum lag
        autocorr_values = []

        for lag in range(1, max_lag):
            if lag < len(values):
                corr, _ = pearsonr(values[:-lag], values[lag:])
                autocorr_values.append(abs(corr))
            else:
                autocorr_values.append(0)

        if not autocorr_values:
            return 12  # Default fallback

        # Find peaks in autocorrelation
        peaks, _ = signal.find_peaks(autocorr_values, height=0.1)

        if len(peaks) > 0:
            # Return the first significant peak + 1 (accounting for 0-indexing)
            return int(peaks[0] + 1)

        # Fallback: check common periods based on data frequency
        time_diff = (dates.max() - dates.min()).days / len(dates)
        if time_diff <= 1:  # Daily data
            return 7  # Weekly seasonality
        elif time_diff <= 7:  # Weekly data
            return 4  # Monthly seasonality (4 weeks)
        else:  # Monthly or longer
            return 12  # Yearly seasonality

    except Exception:
        return 12  # Safe fallback


def plot_original_series(dates, values, value_col):
    """Plot the original time series"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, values, linewidth=1.5, color='#2E86AB')
    ax.set_xlabel('Date')
    ax.set_ylabel(value_col)
    ax.set_title(f'Original Time Series: {value_col}')
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()


def plot_autocorrelation(values, seasonal_period):
    """Plot autocorrelation function"""
    try:
        from scipy.stats import pearsonr

        max_lag = min(len(values) // 2, seasonal_period * 3)
        lags = list(range(1, max_lag + 1))
        autocorr_values = []

        for lag in lags:
            if lag < len(values):
                corr, _ = pearsonr(values[:-lag], values[lag:])
                autocorr_values.append(corr)
            else:
                autocorr_values.append(0)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(lags, autocorr_values, 'b-', linewidth=1.5)
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axhline(y=0.2, color='r', linestyle='--', alpha=0.5, label='Significance threshold')
        ax.axhline(y=-0.2, color='r', linestyle='--', alpha=0.5)

        # Highlight seasonal period
        if seasonal_period <= max_lag:
            ax.axvline(x=seasonal_period, color='orange', linestyle=':', linewidth=2,
                       label=f'Seasonal period ({seasonal_period})')

        ax.set_xlabel('Lag')
        ax.set_ylabel('Autocorrelation')
        ax.set_title('Autocorrelation Function')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        # Show interpretation
        max_autocorr = max(autocorr_values) if autocorr_values else 0
        if max_autocorr > 0.3:
            st.success(f"🔍 Strong seasonal pattern detected (max autocorr: {max_autocorr:.3f})")
        elif max_autocorr > 0.15:
            st.info(f"🔍 Moderate seasonal pattern detected (max autocorr: {max_autocorr:.3f})")
        else:
            st.warning(f"🔍 Weak or no seasonal pattern detected (max autocorr: {max_autocorr:.3f})")

    except Exception as e:
        st.error(f"Error in autocorrelation analysis: {str(e)}")


def perform_classical_decomposition(values, period, model='additive'):
    """Perform classical seasonal decomposition"""
    try:
        # Simple moving average for trend
        if period % 2 == 0:  # Even period
            trend = pd.Series(values).rolling(window=period, center=True).mean()
            # Additional smoothing for even periods
            trend = trend.rolling(window=2, center=True).mean()
        else:  # Odd period
            trend = pd.Series(values).rolling(window=period, center=True).mean()

        trend = trend.fillna(method='bfill').fillna(method='ffill')

        # Calculate seasonal component
        if model == 'additive':
            detrended = values - trend
        else:  # multiplicative
            detrended = values / trend
            detrended = detrended.fillna(1)  # Handle division by zero

        # Extract seasonal pattern
        seasonal_pattern = []
        for i in range(period):
            season_values = [detrended[j] for j in range(i, len(detrended), period)]
            if model == 'additive':
                seasonal_pattern.append(np.mean(season_values))
            else:
                seasonal_pattern.append(np.mean(season_values))

        # Normalize seasonal pattern
        if model == 'additive':
            seasonal_pattern = np.array(seasonal_pattern)
            seasonal_pattern = seasonal_pattern - np.mean(seasonal_pattern)
        else:
            seasonal_pattern = np.array(seasonal_pattern)
            seasonal_pattern = seasonal_pattern / np.mean(seasonal_pattern)

        # Create full seasonal series
        seasonal = np.tile(seasonal_pattern, len(values) // period + 1)[:len(values)]

        # Calculate residual
        if model == 'additive':
            residual = values - trend - seasonal
        else:
            residual = values / (trend * seasonal)
            residual = np.where(np.isfinite(residual), residual, 1)

        return trend.values, seasonal, residual

    except Exception as e:
        st.error(f"Error in decomposition: {str(e)}")
        # Return simple fallbacks
        trend = pd.Series(values).rolling(window=min(period, len(values) // 2), center=True).mean().fillna(
            method='bfill').fillna(method='ffill')
        seasonal = np.zeros_like(values)
        residual = values - trend
        return trend.values, seasonal, residual


def plot_decomposition(dates, original, trend, seasonal, residual, model):
    """Plot decomposition components"""
    fig, axes = plt.subplots(4, 1, figsize=(14, 12))

    # Original
    axes[0].plot(dates, original, color='#2E86AB', linewidth=1.5)
    axes[0].set_title('Original Time Series')
    axes[0].grid(True, alpha=0.3)

    # Trend
    axes[1].plot(dates, trend, color='#A23B72', linewidth=2)
    axes[1].set_title('Trend Component')
    axes[1].grid(True, alpha=0.3)

    # Seasonal
    axes[2].plot(dates, seasonal, color='#F18F01', linewidth=1.5)
    axes[2].set_title('Seasonal Component')
    axes[2].grid(True, alpha=0.3)

    # Residual
    axes[3].plot(dates, residual, color='#C73E1D', linewidth=1)
    axes[3].set_title('Residual Component')
    axes[3].grid(True, alpha=0.3)
    axes[3].set_xlabel('Date')

    for ax in axes:
        ax.tick_params(axis='x', rotation=45)

    plt.suptitle(f'{model.title()} Decomposition', fontsize=16, y=0.98)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()


def analyze_seasonal_patterns(dates, values, seasonal, period):
    """Analyze seasonal patterns by different time periods"""
    try:
        df_analysis = pd.DataFrame({
            'Date': dates,
            'Value': values,
            'Seasonal': seasonal
        })

        # Monthly patterns
        if len(df_analysis) > 30:
            st.markdown("#### 📅 Monthly Patterns")
            df_analysis['Month'] = df_analysis['Date'].dt.month
            monthly_stats = df_analysis.groupby('Month').agg({
                'Value': ['mean', 'std', 'count'],
                'Seasonal': 'mean'
            }).round(3)

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

            # Monthly averages
            monthly_means = df_analysis.groupby('Month')['Value'].mean()
            ax1.bar(monthly_means.index, monthly_means.values, color='skyblue', alpha=0.7)
            ax1.set_xlabel('Month')
            ax1.set_ylabel('Average Value')
            ax1.set_title('Average Values by Month')
            ax1.set_xticks(range(1, 13))

            # Seasonal component by month
            monthly_seasonal = df_analysis.groupby('Month')['Seasonal'].mean()
            ax2.plot(monthly_seasonal.index, monthly_seasonal.values, 'o-', color='orange', linewidth=2)
            ax2.set_xlabel('Month')
            ax2.set_ylabel('Seasonal Component')
            ax2.set_title('Seasonal Component by Month')
            ax2.set_xticks(range(1, 13))
            ax2.grid(True, alpha=0.3)

            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

            st.dataframe(monthly_stats)

        # Quarterly patterns (if enough data)
        if len(df_analysis) > 90:
            st.markdown("#### 📊 Quarterly Patterns")
            df_analysis['Quarter'] = df_analysis['Date'].dt.quarter
            quarterly_stats = df_analysis.groupby('Quarter').agg({
                'Value': ['mean', 'std', 'count'],
                'Seasonal': 'mean'
            }).round(3)

            fig, ax = plt.subplots(figsize=(10, 5))
            quarterly_means = df_analysis.groupby('Quarter')['Value'].mean()
            ax.bar(quarterly_means.index, quarterly_means.values, color='lightcoral', alpha=0.7)
            ax.set_xlabel('Quarter')
            ax.set_ylabel('Average Value')
            ax.set_title('Average Values by Quarter')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

            st.dataframe(quarterly_stats)

        # Day of week patterns (if daily data)
        time_diff = (dates.max() - dates.min()).days / len(dates)
        if time_diff <= 2:  # Likely daily or sub-daily data
            st.markdown("#### 📅 Day of Week Patterns")
            df_analysis['DayOfWeek'] = df_analysis['Date'].dt.dayofweek
            dow_stats = df_analysis.groupby('DayOfWeek').agg({
                'Value': ['mean', 'std', 'count'],
                'Seasonal': 'mean'
            }).round(3)

            fig, ax = plt.subplots(figsize=(10, 5))
            dow_means = df_analysis.groupby('DayOfWeek')['Value'].mean()
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            ax.bar(range(7), dow_means.values, color='lightgreen', alpha=0.7)
            ax.set_xlabel('Day of Week')
            ax.set_ylabel('Average Value')
            ax.set_title('Average Values by Day of Week')
            ax.set_xticks(range(7))
            ax.set_xticklabels(days)
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

            st.dataframe(dow_stats)

    except Exception as e:
        st.error(f"Error in seasonal pattern analysis: {str(e)}")


def plot_seasonal_subseries(dates, values, period):
    """Create seasonal subseries plots"""
    try:
        df = pd.DataFrame({'Date': dates, 'Value': values})
        df['Period'] = range(len(df))
        df['Season'] = df['Period'] % period

        # Create subseries plot
        fig, ax = plt.subplots(figsize=(14, 8))

        colors = plt.cm.Set3(np.linspace(0, 1, period))

        for season in range(period):
            season_data = df[df['Season'] == season]
            if len(season_data) > 1:
                ax.plot(season_data.index // period, season_data['Value'],
                        'o-', color=colors[season], label=f'Period {season}', alpha=0.7)

        ax.set_xlabel('Cycle Number')
        ax.set_ylabel('Value')
        ax.set_title(f'Seasonal Subseries Plot (Period = {period})')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        # Box plot by season
        fig, ax = plt.subplots(figsize=(12, 6))
        season_data = [df[df['Season'] == s]['Value'].values for s in range(period)]
        bp = ax.boxplot(season_data, patch_artist=True)

        # Color the boxes
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        ax.set_xlabel('Season/Period')
        ax.set_ylabel('Value')
        ax.set_title('Distribution by Season')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    except Exception as e:
        st.error(f"Error in subseries plot: {str(e)}")


def calculate_seasonal_strength(values, trend, seasonal, residual, model):
    """Calculate and display seasonal strength metrics"""
    try:
        # Calculate seasonal strength
        if model.lower() == 'additive':
            seasonal_var = np.var(seasonal)
            residual_var = np.var(residual)
            total_var = np.var(values)

            seasonal_strength = seasonal_var / (seasonal_var + residual_var) if (seasonal_var + residual_var) > 0 else 0
            trend_strength = 1 - residual_var / (total_var) if total_var > 0 else 0
        else:  # multiplicative
            log_values = np.log(np.maximum(values, 1e-10))
            log_trend = np.log(np.maximum(trend, 1e-10))
            log_seasonal = np.log(np.maximum(seasonal, 1e-10))
            log_residual = np.log(np.maximum(residual, 1e-10))

            seasonal_var = np.var(log_seasonal)
            residual_var = np.var(log_residual)
            total_var = np.var(log_values)

            seasonal_strength = seasonal_var / (seasonal_var + residual_var) if (seasonal_var + residual_var) > 0 else 0
            trend_strength = 1 - residual_var / total_var if total_var > 0 else 0

        # Ensure values are between 0 and 1
        seasonal_strength = max(0, min(1, seasonal_strength))
        trend_strength = max(0, min(1, trend_strength))

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Seasonal Strength",
                f"{seasonal_strength:.3f}",
                help="Proportion of variation explained by seasonality (0-1)"
            )

        with col2:
            st.metric(
                "Trend Strength",
                f"{trend_strength:.3f}",
                help="Proportion of variation explained by trend (0-1)"
            )

        with col3:
            residual_strength = 1 - seasonal_strength - trend_strength
            residual_strength = max(0, residual_strength)
            st.metric(
                "Residual Strength",
                f"{residual_strength:.3f}",
                help="Proportion of variation that is irregular/random"
            )

        # Interpretation
        st.markdown("#### 📊 Strength Interpretation")

        if seasonal_strength > 0.6:
            st.success("🟢 **Strong seasonal pattern** - Clear and consistent seasonal effects")
        elif seasonal_strength > 0.3:
            st.info("🟡 **Moderate seasonal pattern** - Noticeable seasonal effects")
        else:
            st.warning("🔴 **Weak seasonal pattern** - Limited seasonal effects")

        if trend_strength > 0.6:
            st.success("🟢 **Strong trend component** - Clear directional movement")
        elif trend_strength > 0.3:
            st.info("🟡 **Moderate trend component** - Some directional movement")
        else:
            st.warning("🔴 **Weak trend component** - Limited directional movement")

        # Additional metrics
        st.markdown("#### 📈 Additional Metrics")

        # Signal-to-noise ratio
        signal_var = seasonal_var + np.var(trend - np.mean(trend))
        noise_var = np.var(residual)
        snr = signal_var / noise_var if noise_var > 0 else float('inf')

        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Signal-to-Noise Ratio",
                f"{snr:.2f}",
                help="Ratio of signal (trend+seasonal) to noise (residual)"
            )

        with col2:
            # Regularity of seasonal pattern
            if len(seasonal) >= 2:
                seasonal_cv = np.std(seasonal) / (np.abs(np.mean(seasonal)) + 1e-10)
                st.metric(
                    "Seasonal Regularity",
                    f"{1 / (1 + seasonal_cv):.3f}",
                    help="How regular/consistent the seasonal pattern is (0-1)"
                )

    except Exception as e:
        st.error(f"Error in seasonal strength calculation: {str(e)}")


def create_seasonality_download(df_clean, trend, seasonal, residual, period, model):
    """Create downloadable results"""
    try:
        # Create results dataframe
        results_df = df_clean.copy()
        results_df['Trend'] = trend
        results_df['Seasonal'] = seasonal
        results_df['Residual'] = residual
        results_df['Seasonal_Period'] = period
        results_df['Decomposition_Model'] = model

        # Create summary statistics
        summary_stats = {
            'Metric': [
                'Seasonal Period', 'Decomposition Model', 'Data Points',
                'Mean Value', 'Trend Variance', 'Seasonal Variance', 'Residual Variance'
            ],
            'Value': [
                period, model, len(df_clean),
                f"{np.mean(df_clean.iloc[:, 1]):.4f}",
                f"{np.var(trend):.4f}",
                f"{np.var(seasonal):.4f}",
                f"{np.var(residual):.4f}"
            ]
        }
        summary_df = pd.DataFrame(summary_stats)

        col1, col2 = st.columns(2)

        with col1:
            # Download detailed results
            csv_data = results_df.to_csv(index=False)
            FileHandler.create_download_link(
                csv_data.encode(),
                "seasonality_analysis_results.csv",
                "text/csv"
            )

        with col2:
            # Download summary
            summary_csv = summary_df.to_csv(index=False)
            FileHandler.create_download_link(
                summary_csv.encode(),
                "seasonality_summary.csv",
                "text/csv"
            )

        st.markdown("#### 📋 Analysis Summary")
        st.dataframe(summary_df)

    except Exception as e:
        st.error(f"Error creating download files: {str(e)}")


def quality_assessment():
    """Comprehensive data quality assessment tool"""
    create_tool_header("Quality Assessment", "Evaluate overall data quality with comprehensive metrics", "📊")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx', 'json'], accept_multiple=False)

    if uploaded_file:
        # Load data
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        elif uploaded_file[0].name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file[0])
        elif uploaded_file[0].name.endswith('.json'):
            json_data = FileHandler.process_text_file(uploaded_file[0])
            try:
                import json
                data = json.loads(json_data)
                df = pd.DataFrame(data) if isinstance(data, list) else pd.json_normalize(data)
            except:
                st.error("Invalid JSON format")
                return
        else:
            st.error("Unsupported file format")
            return

        if df is not None and not df.empty:
            st.markdown("### 📊 Dataset Overview")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Rows", f"{len(df):,}")
            with col2:
                st.metric("Total Columns", len(df.columns))
            with col3:
                st.metric("Data Types", len(df.dtypes.unique()))
            with col4:
                memory_usage = df.memory_usage(deep=True).sum() / 1024 ** 2
                st.metric("Memory Usage", f"{memory_usage:.2f} MB")

            # Calculate comprehensive quality scores
            quality_scores = calculate_comprehensive_quality_scores(df)

            # Display overall quality score
            st.markdown("### 🎯 Overall Quality Score")
            overall_score = (quality_scores['completeness'] + quality_scores['consistency'] +
                             quality_scores['validity'] + quality_scores['uniqueness']) / 4

            # Color-coded score display
            if overall_score >= 0.8:
                score_color = "🟢"
                score_status = "Excellent"
            elif overall_score >= 0.6:
                score_color = "🟡"
                score_status = "Good"
            elif overall_score >= 0.4:
                score_color = "🟠"
                score_status = "Fair"
            else:
                score_color = "🔴"
                score_status = "Poor"

            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(overall_score)
            with col2:
                st.metric("Quality Score", f"{overall_score:.1%}")

            st.markdown(f"**Quality Status:** {score_color} {score_status}")

            # Detailed quality metrics
            st.markdown("### 📈 Quality Metrics Breakdown")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Completeness", f"{quality_scores['completeness']:.1%}",
                          help="Percentage of non-missing values")
                st.progress(quality_scores['completeness'])

            with col2:
                st.metric("Consistency", f"{quality_scores['consistency']:.1%}",
                          help="Data type and format consistency")
                st.progress(quality_scores['consistency'])

            with col3:
                st.metric("Validity", f"{quality_scores['validity']:.1%}",
                          help="Valid data within expected ranges")
                st.progress(quality_scores['validity'])

            with col4:
                st.metric("Uniqueness", f"{quality_scores['uniqueness']:.1%}",
                          help="Percentage of unique values where expected")
                st.progress(quality_scores['uniqueness'])

            # Column-level quality assessment
            st.markdown("### 🔍 Column-Level Quality Assessment")
            column_quality = assess_column_quality(df)
            st.dataframe(column_quality, use_container_width=True)

            # Quality issues identification
            st.markdown("### ⚠️ Quality Issues Identified")
            quality_issues = identify_quality_issues(df)

            if quality_issues:
                for issue in quality_issues:
                    if issue['severity'] == 'high':
                        st.error(f"🔴 **{issue['type']}**: {issue['description']}")
                    elif issue['severity'] == 'medium':
                        st.warning(f"🟠 **{issue['type']}**: {issue['description']}")
                    else:
                        st.info(f"🟡 **{issue['type']}**: {issue['description']}")
            else:
                st.success("🎉 No significant quality issues detected!")

            # Recommendations
            st.markdown("### 💡 Quality Improvement Recommendations")
            recommendations = generate_quality_recommendations(df, quality_scores, quality_issues)

            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"**{i}.** {rec}")

            # Export quality report
            if st.button("📄 Generate Quality Report"):
                quality_report = create_quality_report(df, quality_scores, quality_issues, recommendations)
                st.download_button(
                    label="Download Quality Report",
                    data=quality_report,
                    file_name=f"quality_assessment_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )


def completeness_check():
    """Check data completeness and missing value patterns"""
    create_tool_header("Completeness Check", "Analyze missing values and data completeness patterns", "📋")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx', 'json'], accept_multiple=False)

    if uploaded_file:
        # Load data
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        elif uploaded_file[0].name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file[0])
        elif uploaded_file[0].name.endswith('.json'):
            json_data = FileHandler.process_text_file(uploaded_file[0])
            try:
                import json
                data = json.loads(json_data)
                df = pd.DataFrame(data) if isinstance(data, list) else pd.json_normalize(data)
            except:
                st.error("Invalid JSON format")
                return

        if df is not None and not df.empty:
            st.markdown("### 📊 Completeness Overview")

            # Overall completeness metrics
            total_cells = df.shape[0] * df.shape[1]
            missing_cells = df.isnull().sum().sum()
            completeness_rate = (total_cells - missing_cells) / total_cells

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Cells", f"{total_cells:,}")
            with col2:
                st.metric("Missing Cells", f"{missing_cells:,}")
            with col3:
                st.metric("Completeness Rate", f"{completeness_rate:.1%}")
            with col4:
                missing_rows = df.isnull().any(axis=1).sum()
                st.metric("Rows with Missing Data", f"{missing_rows:,}")

            # Completeness visualization
            st.markdown("### 📈 Missing Data Pattern")

            missing_data = df.isnull().sum().sort_values(ascending=False)
            missing_percent = (missing_data / len(df) * 100).round(2)

            # Create completeness chart
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # Missing data count
            missing_data[missing_data > 0].plot(kind='bar', ax=ax1, color='coral')
            ax1.set_title('Missing Values by Column')
            ax1.set_xlabel('Columns')
            ax1.set_ylabel('Count of Missing Values')
            ax1.tick_params(axis='x', rotation=45)

            # Missing data percentage
            missing_percent[missing_percent > 0].plot(kind='bar', ax=ax2, color='lightblue')
            ax2.set_title('Missing Data Percentage by Column')
            ax2.set_xlabel('Columns')
            ax2.set_ylabel('Percentage Missing (%)')
            ax2.tick_params(axis='x', rotation=45)

            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)

            # Column-wise completeness analysis
            st.markdown("### 🔍 Column-wise Completeness Analysis")

            completeness_df = pd.DataFrame({
                'Column': df.columns,
                'Missing Count': missing_data,
                'Missing %': missing_percent,
                'Complete Count': len(df) - missing_data,
                'Complete %': 100 - missing_percent,
                'Data Type': df.dtypes,
                'Completeness Status': missing_percent.apply(lambda x:
                                                             '🟢 Complete' if x == 0 else
                                                             '🟡 Mostly Complete' if x < 10 else
                                                             '🟠 Incomplete' if x < 50 else
                                                             '🔴 Severely Incomplete')
            })

            st.dataframe(completeness_df, use_container_width=True)

            # Missing data patterns
            st.markdown("### 🔍 Missing Data Patterns")

            if missing_cells > 0:
                # Pattern analysis
                missing_patterns = analyze_missing_patterns(df)

                if missing_patterns:
                    st.markdown("**Common Missing Data Patterns:**")
                    for pattern in missing_patterns:
                        st.write(f"• {pattern}")

                # Missing data heatmap
                if len(df.columns) <= 20 and len(df) <= 1000:  # Limit for performance
                    st.markdown("**Missing Data Heatmap:**")
                    fig, ax = plt.subplots(figsize=(12, 8))

                    # Create missing data matrix
                    missing_matrix = df.isnull()

                    # Plot heatmap
                    import seaborn as sns
                    sns.heatmap(missing_matrix.T, cbar=True, ax=ax, cmap='RdYlBu_r')
                    ax.set_title('Missing Data Heatmap')
                    ax.set_xlabel('Row Index')
                    ax.set_ylabel('Columns')

                    plt.tight_layout()
                    st.pyplot(fig)
                    plt.close(fig)
                else:
                    st.info("Dataset too large for heatmap visualization (>20 columns or >1000 rows)")

            # Completeness recommendations
            st.markdown("### 💡 Completeness Improvement Recommendations")

            recommendations = generate_completeness_recommendations(df, missing_data, missing_percent)
            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"**{i}.** {rec}")

            # Export completeness report
            if st.button("📄 Generate Completeness Report"):
                report = create_completeness_report(df, completeness_df, missing_patterns, recommendations)
                st.download_button(
                    label="Download Completeness Report",
                    data=report,
                    file_name=f"completeness_check_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )


def consistency_validator():
    """Validate data consistency across columns and detect inconsistencies"""
    create_tool_header("Consistency Validator", "Detect and analyze data consistency issues", "🔍")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx', 'json'], accept_multiple=False)

    if uploaded_file:
        # Load data
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        elif uploaded_file[0].name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file[0])
        elif uploaded_file[0].name.endswith('.json'):
            json_data = FileHandler.process_text_file(uploaded_file[0])
            try:
                import json
                data = json.loads(json_data)
                df = pd.DataFrame(data) if isinstance(data, list) else pd.json_normalize(data)
            except:
                st.error("Invalid JSON format")
                return

        if df is not None and not df.empty:
            st.markdown("### 📊 Consistency Analysis Overview")

            # Basic consistency metrics
            col1, col2, col3, col4 = st.columns(4)

            consistency_issues = detect_consistency_issues(df)
            total_issues = sum(len(issues) for issues in consistency_issues.values())

            with col1:
                st.metric("Total Columns", len(df.columns))
            with col2:
                st.metric("Consistency Issues", total_issues)
            with col3:
                data_types = len(df.dtypes.unique())
                st.metric("Data Types Used", data_types)
            with col4:
                consistent_cols = len(df.columns) - len([col for col, issues in consistency_issues.items() if issues])
                consistency_rate = consistent_cols / len(df.columns)
                st.metric("Consistency Rate", f"{consistency_rate:.1%}")

            # Data type consistency
            st.markdown("### 🔍 Data Type Consistency")

            dtype_analysis = analyze_data_type_consistency(df)
            st.dataframe(dtype_analysis, use_container_width=True)

            # Format consistency checks
            st.markdown("### 📝 Format Consistency Analysis")

            format_issues = check_format_consistency(df)

            if format_issues:
                for column, issues in format_issues.items():
                    if issues:
                        st.markdown(f"**Column: {column}**")
                        for issue in issues:
                            if issue['severity'] == 'high':
                                st.error(f"🔴 {issue['description']}")
                            elif issue['severity'] == 'medium':
                                st.warning(f"🟠 {issue['description']}")
                            else:
                                st.info(f"🟡 {issue['description']}")
            else:
                st.success("🎉 No format consistency issues detected!")

            # Value consistency checks
            st.markdown("### 🔢 Value Consistency Analysis")

            value_consistency = check_value_consistency(df)

            for check_type, results in value_consistency.items():
                if results:
                    st.markdown(f"**{check_type}:**")
                    for result in results:
                        st.write(f"• {result}")

            # Cross-column consistency
            st.markdown("### 🔄 Cross-Column Consistency")

            cross_column_issues = check_cross_column_consistency(df)

            if cross_column_issues:
                for issue in cross_column_issues:
                    if issue['severity'] == 'high':
                        st.error(f"🔴 **{issue['type']}**: {issue['description']}")
                    elif issue['severity'] == 'medium':
                        st.warning(f"🟠 **{issue['type']}**: {issue['description']}")
                    else:
                        st.info(f"🟡 **{issue['type']}**: {issue['description']}")
            else:
                st.success("🎉 No cross-column consistency issues detected!")

            # Consistency recommendations
            st.markdown("### 💡 Consistency Improvement Recommendations")

            recommendations = generate_consistency_recommendations(df, consistency_issues, format_issues,
                                                                   cross_column_issues)

            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"**{i}.** {rec}")

            # Export consistency report
            if st.button("📄 Generate Consistency Report"):
                report = create_consistency_report(df, consistency_issues, format_issues, cross_column_issues,
                                                   recommendations)
                st.download_button(
                    label="Download Consistency Report",
                    data=report,
                    file_name=f"consistency_validation_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )


def accuracy_measure():
    """Measure and assess data accuracy against expected patterns and rules"""
    create_tool_header("Accuracy Measure", "Assess data accuracy and identify potential errors", "🎯")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx', 'json'], accept_multiple=False)

    if uploaded_file:
        # Load data
        if uploaded_file[0].name.endswith('.csv'):
            df = FileHandler.process_csv_file(uploaded_file[0])
        elif uploaded_file[0].name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file[0])
        elif uploaded_file[0].name.endswith('.json'):
            json_data = FileHandler.process_text_file(uploaded_file[0])
            try:
                import json
                data = json.loads(json_data)
                df = pd.DataFrame(data) if isinstance(data, list) else pd.json_normalize(data)
            except:
                st.error("Invalid JSON format")
                return

        if df is not None and not df.empty:
            st.markdown("### 📊 Accuracy Assessment Overview")

            # Calculate accuracy metrics
            accuracy_results = calculate_accuracy_metrics(df)

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Total Values", f"{accuracy_results['total_values']:,}")
            with col2:
                st.metric("Potential Errors", f"{accuracy_results['potential_errors']:,}")
            with col3:
                st.metric("Accuracy Rate", f"{accuracy_results['accuracy_rate']:.1%}")
            with col4:
                st.metric("Confidence Level", f"{accuracy_results['confidence_level']:.1%}")

            # Accuracy score visualization
            st.markdown("### 🎯 Accuracy Score")

            accuracy_score = accuracy_results['accuracy_rate']
            if accuracy_score >= 0.95:
                accuracy_status = "🟢 Excellent"
                accuracy_color = "green"
            elif accuracy_score >= 0.85:
                accuracy_status = "🟡 Good"
                accuracy_color = "yellow"
            elif accuracy_score >= 0.70:
                accuracy_status = "🟠 Fair"
                accuracy_color = "orange"
            else:
                accuracy_status = "🔴 Poor"
                accuracy_color = "red"

            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(accuracy_score)
            with col2:
                st.metric("Status", accuracy_status)

            # Column-level accuracy analysis
            st.markdown("### 🔍 Column-Level Accuracy Analysis")

            column_accuracy = assess_column_accuracy(df)
            st.dataframe(column_accuracy, use_container_width=True)

            # Data validation rules
            st.markdown("### ✅ Data Validation Rules")

            validation_results = apply_validation_rules(df)

            if validation_results:
                for rule_type, results in validation_results.items():
                    if results:
                        st.markdown(f"**{rule_type}:**")
                        for result in results:
                            if result['status'] == 'passed':
                                st.success(f"✅ {result['description']}")
                            elif result['status'] == 'warning':
                                st.warning(f"⚠️ {result['description']}")
                            else:
                                st.error(f"❌ {result['description']}")

            # Outlier detection for accuracy
            st.markdown("### 🔍 Outlier Detection (Accuracy Impact)")

            outlier_analysis = detect_accuracy_outliers(df)

            if outlier_analysis['outliers_found']:
                st.warning(f"Found {outlier_analysis['total_outliers']} potential outliers that may affect accuracy")

                for column, outlier_info in outlier_analysis['column_outliers'].items():
                    if outlier_info['count'] > 0:
                        st.write(f"• **{column}**: {outlier_info['count']} outliers detected "
                                 f"({outlier_info['percentage']:.1f}% of column)")
            else:
                st.success("🎉 No significant outliers detected!")

            # Pattern accuracy analysis
            st.markdown("### 📊 Pattern Accuracy Analysis")

            pattern_accuracy = analyze_pattern_accuracy(df)

            for pattern_type, analysis in pattern_accuracy.items():
                if analysis['issues']:
                    st.markdown(f"**{pattern_type}:**")
                    for issue in analysis['issues']:
                        st.write(f"• {issue}")
                else:
                    st.success(f"✅ {pattern_type}: No issues detected")

            # Accuracy improvement recommendations
            st.markdown("### 💡 Accuracy Improvement Recommendations")

            recommendations = generate_accuracy_recommendations(df, accuracy_results, validation_results,
                                                                outlier_analysis)

            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"**{i}.** {rec}")

            # Export accuracy report
            if st.button("📄 Generate Accuracy Report"):
                report = create_accuracy_report(df, accuracy_results, validation_results, outlier_analysis,
                                                recommendations)
                st.download_button(
                    label="Download Accuracy Report",
                    data=report,
                    file_name=f"accuracy_assessment_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )


# Helper functions for data quality assessments

def calculate_comprehensive_quality_scores(df):
    """Calculate comprehensive quality scores"""
    scores = {}

    # Completeness score
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    scores['completeness'] = (total_cells - missing_cells) / total_cells

    # Consistency score (based on data types and format consistency)
    consistency_issues = 0
    for col in df.columns:
        if df[col].dtype == 'object':
            # Check for mixed types in string columns
            non_null_values = df[col].dropna()
            if len(non_null_values) > 0:
                string_count = sum(isinstance(x, str) for x in non_null_values)
                consistency_issues += abs(string_count - len(non_null_values))

    scores['consistency'] = max(0, 1 - (consistency_issues / total_cells))

    # Validity score (based on data type appropriateness)
    valid_cells = 0
    for col in df.columns:
        col_data = df[col].dropna()
        if len(col_data) > 0:
            if pd.api.types.is_numeric_dtype(col_data):
                # Check for reasonable numeric ranges
                if col_data.min() >= 0 and col_data.max() < 1e10:
                    valid_cells += len(col_data)
                else:
                    valid_cells += len(col_data) * 0.8  # Penalize extreme values
            else:
                # For non-numeric, assume valid if not empty
                valid_cells += len(col_data)

    scores['validity'] = valid_cells / (total_cells - missing_cells) if total_cells > missing_cells else 0

    # Uniqueness score (penalize excessive duplicates)
    duplicate_penalty = 0
    for col in df.columns:
        if df[col].dtype in ['object', 'string']:
            unique_ratio = df[col].nunique() / len(df[col].dropna())
            if unique_ratio < 0.1:  # Very low uniqueness might indicate data quality issues
                duplicate_penalty += (0.1 - unique_ratio)

    scores['uniqueness'] = max(0, 1 - duplicate_penalty)

    return scores


def assess_column_quality(df):
    """Assess quality metrics for each column"""
    quality_data = []

    for col in df.columns:
        col_data = df[col]

        # Basic metrics
        total_count = len(col_data)
        null_count = col_data.isnull().sum()
        completeness = (total_count - null_count) / total_count

        # Uniqueness
        unique_count = col_data.nunique()
        uniqueness = unique_count / total_count

        # Consistency (basic check)
        consistency = 1.0  # Default
        if col_data.dtype == 'object':
            # Check for mixed content types
            non_null = col_data.dropna()
            if len(non_null) > 0:
                numeric_like = sum(str(x).replace('.', '').isdigit() for x in non_null)
                if 0 < numeric_like < len(non_null):
                    consistency = 0.7  # Mixed numeric/text content

        # Overall column quality score
        column_quality = (completeness + consistency + min(uniqueness * 2, 1)) / 3

        quality_data.append({
            'Column': col,
            'Data Type': str(col_data.dtype),
            'Completeness': f"{completeness:.1%}",
            'Uniqueness': f"{uniqueness:.1%}",
            'Consistency': f"{consistency:.1%}",
            'Quality Score': f"{column_quality:.1%}",
            'Status': '🟢 Good' if column_quality >= 0.8 else '🟡 Fair' if column_quality >= 0.6 else '🔴 Poor'
        })

    return pd.DataFrame(quality_data)


def identify_quality_issues(df):
    """Identify specific quality issues in the dataset"""
    issues = []

    # Check for excessive missing data
    missing_pct = (df.isnull().sum() / len(df)) * 100
    for col in missing_pct.index:
        if missing_pct[col] > 50:
            issues.append({
                'type': 'High Missing Data',
                'description': f"Column '{col}' has {missing_pct[col]:.1f}% missing values",
                'severity': 'high'
            })
        elif missing_pct[col] > 20:
            issues.append({
                'type': 'Moderate Missing Data',
                'description': f"Column '{col}' has {missing_pct[col]:.1f}% missing values",
                'severity': 'medium'
            })

    # Check for duplicate rows
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        dup_pct = (duplicates / len(df)) * 100
        severity = 'high' if dup_pct > 10 else 'medium' if dup_pct > 5 else 'low'
        issues.append({
            'type': 'Duplicate Rows',
            'description': f"Found {duplicates} duplicate rows ({dup_pct:.1f}% of data)",
            'severity': severity
        })

    # Check for mixed data types in object columns
    for col in df.select_dtypes(include=['object']).columns:
        non_null = df[col].dropna()
        if len(non_null) > 0:
            numeric_like = sum(str(x).replace('.', '').replace('-', '').isdigit() for x in non_null)
            if 0 < numeric_like < len(non_null):
                issues.append({
                    'type': 'Mixed Data Types',
                    'description': f"Column '{col}' contains mixed numeric and text data",
                    'severity': 'medium'
                })

    return issues


def generate_quality_recommendations(df, quality_scores, quality_issues):
    """Generate recommendations for improving data quality"""
    recommendations = []

    # Completeness recommendations
    if quality_scores['completeness'] < 0.8:
        recommendations.append("Address missing data through imputation, collection, or explicit handling strategies")

    # Consistency recommendations
    if quality_scores['consistency'] < 0.8:
        recommendations.append("Standardize data formats and types across columns to improve consistency")

    # Issue-specific recommendations
    for issue in quality_issues:
        if issue['type'] == 'High Missing Data':
            recommendations.append(f"Consider removing or imputing data for columns with excessive missing values")
        elif issue['type'] == 'Duplicate Rows':
            recommendations.append("Remove duplicate rows to improve data uniqueness and accuracy")
        elif issue['type'] == 'Mixed Data Types':
            recommendations.append("Standardize data types within columns for better consistency")

    # General recommendations
    recommendations.append("Implement data validation rules at the point of data collection")
    recommendations.append("Regular data quality monitoring and reporting")

    return recommendations


def create_quality_report(df, quality_scores, quality_issues, recommendations):
    """Create a comprehensive quality assessment report"""
    report = f"""DATA QUALITY ASSESSMENT REPORT
Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

DATASET OVERVIEW:
- Total Rows: {len(df):,}
- Total Columns: {len(df.columns)}
- Total Cells: {df.shape[0] * df.shape[1]:,}

QUALITY SCORES:
- Overall Quality: {(sum(quality_scores.values()) / len(quality_scores)):.1%}
- Completeness: {quality_scores['completeness']:.1%}
- Consistency: {quality_scores['consistency']:.1%}
- Validity: {quality_scores['validity']:.1%}
- Uniqueness: {quality_scores['uniqueness']:.1%}

QUALITY ISSUES IDENTIFIED:
"""

    if quality_issues:
        for issue in quality_issues:
            report += f"- [{issue['severity'].upper()}] {issue['type']}: {issue['description']}\n"
    else:
        report += "- No significant quality issues detected\n"

    report += "\nRECOMMENDATIONS:\n"
    for i, rec in enumerate(recommendations, 1):
        report += f"{i}. {rec}\n"

    return report


def analyze_missing_patterns(df):
    """Analyze patterns in missing data"""
    patterns = []

    missing_by_row = df.isnull().sum(axis=1)

    # Check for rows with all missing data
    completely_missing = (missing_by_row == len(df.columns)).sum()
    if completely_missing > 0:
        patterns.append(f"{completely_missing} rows have all values missing")

    # Check for rows with most data missing
    mostly_missing = (missing_by_row > len(df.columns) * 0.8).sum()
    if mostly_missing > 0:
        patterns.append(f"{mostly_missing} rows have >80% of values missing")

    # Check for columns that are always missing together
    missing_matrix = df.isnull()
    for i, col1 in enumerate(df.columns):
        for col2 in df.columns[i + 1:]:
            both_missing = (missing_matrix[col1] & missing_matrix[col2]).sum()
            if both_missing > len(df) * 0.1:  # More than 10% missing together
                patterns.append(f"Columns '{col1}' and '{col2}' often missing together ({both_missing} cases)")

    return patterns


def generate_completeness_recommendations(df, missing_data, missing_percent):
    """Generate recommendations for improving completeness"""
    recommendations = []

    # High missing data columns
    high_missing = missing_percent[missing_percent > 50]
    if not high_missing.empty:
        recommendations.append(f"Consider removing columns with >50% missing data: {', '.join(high_missing.index)}")

    # Moderate missing data
    moderate_missing = missing_percent[(missing_percent > 10) & (missing_percent <= 50)]
    if not moderate_missing.empty:
        recommendations.append("Implement data imputation strategies for moderately incomplete columns")

    # If very few missing values
    if missing_data.sum() < len(df) * 0.05:
        recommendations.append("Consider removing rows with missing values (small impact on dataset)")

    recommendations.append("Improve data collection processes to reduce future missing data")
    recommendations.append("Document missing data patterns and reasons when possible")

    return recommendations


def create_completeness_report(df, completeness_df, missing_patterns, recommendations):
    """Create a completeness assessment report"""
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    completeness_rate = (total_cells - missing_cells) / total_cells

    report = f"""COMPLETENESS ASSESSMENT REPORT
Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERVIEW:
- Dataset Dimensions: {df.shape[0]:,} rows × {df.shape[1]} columns
- Total Cells: {total_cells:,}
- Missing Cells: {missing_cells:,}
- Completeness Rate: {completeness_rate:.1%}

MISSING DATA PATTERNS:
"""

    if missing_patterns:
        for pattern in missing_patterns:
            report += f"- {pattern}\n"
    else:
        report += "- No significant missing data patterns detected\n"

    report += f"\nCOLUMN COMPLETENESS:\n"
    for _, row in completeness_df.iterrows():
        report += f"- {row['Column']}: {row['Complete %']:.1f}% complete ({row['Missing Count']} missing)\n"

    report += "\nRECOMMENDATIONS:\n"
    for i, rec in enumerate(recommendations, 1):
        report += f"{i}. {rec}\n"

    return report


def detect_consistency_issues(df):
    """Detect various consistency issues in the dataset"""
    issues = {}

    for col in df.columns:
        col_issues = []
        col_data = df[col].dropna()

        if len(col_data) == 0:
            continue

        # Check for mixed data types in object columns
        if df[col].dtype == 'object':
            # Check for numeric values in string columns
            numeric_values = 0
            string_values = 0

            for value in col_data:
                if isinstance(value, (int, float)):
                    numeric_values += 1
                elif isinstance(value, str):
                    if value.replace('.', '').replace('-', '').isdigit():
                        numeric_values += 1
                    else:
                        string_values += 1

            if numeric_values > 0 and string_values > 0:
                col_issues.append(f"Mixed numeric and text data detected")

        issues[col] = col_issues

    return issues


def analyze_data_type_consistency(df):
    """Analyze data type consistency across the dataset"""
    dtype_data = []

    for col in df.columns:
        col_data = df[col]

        # Basic type info
        dtype_info = {
            'Column': col,
            'Declared Type': str(col_data.dtype),
            'Non-Null Count': col_data.count(),
            'Null Count': col_data.isnull().sum(),
        }

        # Infer actual content type for object columns
        if col_data.dtype == 'object':
            non_null = col_data.dropna()
            if len(non_null) > 0:
                numeric_like = sum(str(x).replace('.', '').replace('-', '').isdigit() for x in non_null.head(100))
                if numeric_like > len(non_null) * 0.8:
                    dtype_info['Inferred Type'] = 'Numeric (stored as text)'
                    dtype_info['Consistency Issue'] = 'Yes'
                else:
                    dtype_info['Inferred Type'] = 'Text'
                    dtype_info['Consistency Issue'] = 'No'
            else:
                dtype_info['Inferred Type'] = 'Unknown'
                dtype_info['Consistency Issue'] = 'Unknown'
        else:
            dtype_info['Inferred Type'] = str(col_data.dtype)
            dtype_info['Consistency Issue'] = 'No'

        dtype_data.append(dtype_info)

    return pd.DataFrame(dtype_data)


def check_format_consistency(df):
    """Check for format consistency issues within columns"""
    format_issues = {}

    for col in df.select_dtypes(include=['object']).columns:
        col_issues = []
        col_data = df[col].dropna().astype(str)

        if len(col_data) == 0:
            continue

        # Check for common format inconsistencies

        # Date-like patterns
        date_patterns = col_data.str.contains(r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}', regex=True)
        if date_patterns.any() and not date_patterns.all():
            col_issues.append({
                'description': f"Inconsistent date formats detected",
                'severity': 'medium'
            })

        # Email patterns
        email_patterns = col_data.str.contains(r'[^@]+@[^@]+\.[^@]+', regex=True)
        if email_patterns.any() and not email_patterns.all():
            col_issues.append({
                'description': f"Mixed email and non-email values",
                'severity': 'medium'
            })

        # Phone number patterns
        phone_patterns = col_data.str.contains(r'\(\d{3}\)\s*\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10}', regex=True)
        if phone_patterns.any() and not phone_patterns.all():
            col_issues.append({
                'description': f"Inconsistent phone number formats",
                'severity': 'medium'
            })

        format_issues[col] = col_issues

    return format_issues


def check_value_consistency(df):
    """Check for value consistency issues"""
    consistency_results = {}

    # Check numeric ranges
    numeric_issues = []
    for col in df.select_dtypes(include=[np.number]).columns:
        col_data = df[col].dropna()
        if len(col_data) > 0:
            # Check for extreme outliers
            q1 = col_data.quantile(0.25)
            q3 = col_data.quantile(0.75)
            iqr = q3 - q1

            extreme_outliers = ((col_data < q1 - 3 * iqr) | (col_data > q3 + 3 * iqr)).sum()
            if extreme_outliers > 0:
                numeric_issues.append(f"Column '{col}' has {extreme_outliers} extreme outliers")

    consistency_results['Numeric Range Issues'] = numeric_issues

    # Check categorical consistency
    categorical_issues = []
    for col in df.select_dtypes(include=['object']).columns:
        col_data = df[col].dropna()
        if len(col_data) > 0:
            # Check for similar values that might be duplicates
            unique_values = col_data.unique()
            if len(unique_values) > 1:
                for i, val1 in enumerate(unique_values):
                    for val2 in unique_values[i + 1:]:
                        if isinstance(val1, str) and isinstance(val2, str):
                            if val1.lower().strip() == val2.lower().strip() and val1 != val2:
                                categorical_issues.append(f"Column '{col}' has similar values: '{val1}' and '{val2}'")

    consistency_results['Categorical Consistency Issues'] = categorical_issues

    return consistency_results


def check_cross_column_consistency(df):
    """Check for consistency issues across multiple columns"""
    cross_issues = []

    # Look for columns that might be related
    date_columns = []
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            date_columns.append(col)

    # Check date column consistency
    if len(date_columns) >= 2:
        for i, col1 in enumerate(date_columns):
            for col2 in date_columns[i + 1:]:
                # Simple check - if both contain date-like strings
                col1_dates = df[col1].dropna().astype(str).str.contains(r'\d{4}|\d{2}', regex=True)
                col2_dates = df[col2].dropna().astype(str).str.contains(r'\d{4}|\d{2}', regex=True)

                if col1_dates.any() and col2_dates.any():
                    cross_issues.append({
                        'type': 'Date Relationship',
                        'description': f"Check relationship between date columns '{col1}' and '{col2}'",
                        'severity': 'low'
                    })

    # Check for potential ID columns
    id_columns = [col for col in df.columns if 'id' in col.lower()]
    for col in id_columns:
        if df[col].nunique() != len(df[col].dropna()):
            cross_issues.append({
                'type': 'ID Uniqueness',
                'description': f"ID column '{col}' contains duplicate values",
                'severity': 'high'
            })

    return cross_issues


def generate_consistency_recommendations(df, consistency_issues, format_issues, cross_column_issues):
    """Generate recommendations for improving consistency"""
    recommendations = []

    # Address data type inconsistencies
    has_mixed_types = any(issues for issues in consistency_issues.values())
    if has_mixed_types:
        recommendations.append("Standardize data types - convert numeric strings to proper numeric types")

    # Address format inconsistencies
    has_format_issues = any(issues for issues in format_issues.values())
    if has_format_issues:
        recommendations.append(
            "Implement consistent formatting rules for dates, phone numbers, and other structured data")

    # Address cross-column issues
    if cross_column_issues:
        recommendations.append("Review and validate relationships between related columns")

    recommendations.extend([
        "Establish data entry standards and validation rules",
        "Implement data cleaning pipelines for consistent formatting",
        "Regular consistency monitoring and reporting"
    ])

    return recommendations


def create_consistency_report(df, consistency_issues, format_issues, cross_column_issues, recommendations):
    """Create a consistency validation report"""
    total_issues = sum(len(issues) for issues in consistency_issues.values()) + \
                   sum(len(issues) for issues in format_issues.values()) + \
                   len(cross_column_issues)

    report = f"""CONSISTENCY VALIDATION REPORT
Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERVIEW:
- Dataset Dimensions: {df.shape[0]:,} rows × {df.shape[1]} columns
- Total Consistency Issues: {total_issues}
- Data Types Used: {len(df.dtypes.unique())}

CONSISTENCY ISSUES:
"""

    # Data type issues
    for col, issues in consistency_issues.items():
        if issues:
            report += f"- Column '{col}': {', '.join(issues)}\n"

    # Format issues
    for col, issues in format_issues.items():
        if issues:
            for issue in issues:
                report += f"- Column '{col}': {issue['description']}\n"

    # Cross-column issues
    for issue in cross_column_issues:
        report += f"- {issue['type']}: {issue['description']}\n"

    if total_issues == 0:
        report += "- No significant consistency issues detected\n"

    report += "\nRECOMMENDATIONS:\n"
    for i, rec in enumerate(recommendations, 1):
        report += f"{i}. {rec}\n"

    return report


def calculate_accuracy_metrics(df):
    """Calculate comprehensive accuracy metrics"""
    total_values = df.shape[0] * df.shape[1] - df.isnull().sum().sum()
    potential_errors = 0

    # Check for obvious errors
    for col in df.columns:
        col_data = df[col].dropna()

        if len(col_data) == 0:
            continue

        # For numeric columns, check for impossible values
        if pd.api.types.is_numeric_dtype(col_data):
            # Check for negative values where they shouldn't be (if column name suggests positive values)
            if any(keyword in col.lower() for keyword in ['age', 'count', 'quantity', 'amount', 'price']):
                negative_values = (col_data < 0).sum()
                potential_errors += negative_values

            # Check for extreme outliers
            if len(col_data) > 10:
                q1 = col_data.quantile(0.25)
                q3 = col_data.quantile(0.75)
                iqr = q3 - q1
                extreme_outliers = ((col_data < q1 - 3 * iqr) | (col_data > q3 + 3 * iqr)).sum()
                potential_errors += extreme_outliers * 0.5  # Weight as partial errors

        # For text columns, check for obvious formatting issues
        elif col_data.dtype == 'object':
            text_data = col_data.astype(str)

            # Check for excessive whitespace
            whitespace_issues = (text_data != text_data.str.strip()).sum()
            potential_errors += whitespace_issues * 0.3

            # Check for inconsistent capitalization
            if any(keyword in col.lower() for keyword in ['name', 'title', 'category']):
                mixed_case = text_data.str.contains(r'[a-z][A-Z]|[A-Z][a-z][A-Z]', regex=True).sum()
                potential_errors += mixed_case * 0.2

    accuracy_rate = max(0, (total_values - potential_errors) / total_values) if total_values > 0 else 0
    confidence_level = min(1.0, accuracy_rate + 0.1)  # Add confidence buffer

    return {
        'total_values': int(total_values),
        'potential_errors': int(potential_errors),
        'accuracy_rate': accuracy_rate,
        'confidence_level': confidence_level
    }


def assess_column_accuracy(df):
    """Assess accuracy metrics for each column"""
    accuracy_data = []

    for col in df.columns:
        col_data = df[col].dropna()

        if len(col_data) == 0:
            accuracy_data.append({
                'Column': col,
                'Data Type': str(df[col].dtype),
                'Valid Values': 0,
                'Questionable Values': 0,
                'Accuracy Score': 'N/A',
                'Issues': 'No data'
            })
            continue

        valid_values = len(col_data)
        questionable_values = 0
        issues = []

        # Numeric column checks
        if pd.api.types.is_numeric_dtype(col_data):
            # Check for negative values in positive-expected columns
            if any(keyword in col.lower() for keyword in ['age', 'count', 'quantity', 'price']):
                negative_count = (col_data < 0).sum()
                if negative_count > 0:
                    questionable_values += negative_count
                    issues.append(f"{negative_count} negative values")

            # Check for outliers
            if len(col_data) > 10:
                q1 = col_data.quantile(0.25)
                q3 = col_data.quantile(0.75)
                iqr = q3 - q1
                outliers = ((col_data < q1 - 2 * iqr) | (col_data > q3 + 2 * iqr)).sum()
                if outliers > 0:
                    questionable_values += outliers
                    issues.append(f"{outliers} outliers")

        # Text column checks
        elif col_data.dtype == 'object':
            text_data = col_data.astype(str)

            # Whitespace issues
            whitespace_count = (text_data != text_data.str.strip()).sum()
            if whitespace_count > 0:
                questionable_values += whitespace_count
                issues.append(f"{whitespace_count} whitespace issues")

            # Empty strings
            empty_strings = (text_data.str.len() == 0).sum()
            if empty_strings > 0:
                questionable_values += empty_strings
                issues.append(f"{empty_strings} empty strings")

        accuracy_score = (valid_values - questionable_values) / valid_values if valid_values > 0 else 0

        accuracy_data.append({
            'Column': col,
            'Data Type': str(df[col].dtype),
            'Valid Values': valid_values,
            'Questionable Values': questionable_values,
            'Accuracy Score': f"{accuracy_score:.1%}",
            'Issues': ', '.join(issues) if issues else 'None detected'
        })

    return pd.DataFrame(accuracy_data)


def apply_validation_rules(df):
    """Apply various validation rules to assess accuracy"""
    validation_results = {}

    # Numeric validation rules
    numeric_rules = []
    for col in df.select_dtypes(include=[np.number]).columns:
        col_data = df[col].dropna()

        if len(col_data) == 0:
            continue

        # Rule: Age should be reasonable (if column name suggests age)
        if 'age' in col.lower():
            reasonable_ages = ((col_data >= 0) & (col_data <= 120)).all()
            numeric_rules.append({
                'description': f"Age values in '{col}' are within reasonable range (0-120)",
                'status': 'passed' if reasonable_ages else 'failed'
            })

        # Rule: Percentages should be 0-100 or 0-1
        if any(keyword in col.lower() for keyword in ['percent', 'rate', 'ratio']):
            if col_data.max() <= 1:
                valid_range = ((col_data >= 0) & (col_data <= 1)).all()
                numeric_rules.append({
                    'description': f"Percentage values in '{col}' are in valid range (0-1)",
                    'status': 'passed' if valid_range else 'failed'
                })
            else:
                valid_range = ((col_data >= 0) & (col_data <= 100)).all()
                numeric_rules.append({
                    'description': f"Percentage values in '{col}' are in valid range (0-100)",
                    'status': 'passed' if valid_range else 'failed'
                })

    validation_results['Numeric Rules'] = numeric_rules

    # Text validation rules
    text_rules = []
    for col in df.select_dtypes(include=['object']).columns:
        col_data = df[col].dropna().astype(str)

        if len(col_data) == 0:
            continue

        # Rule: Email format validation
        if 'email' in col.lower():
            email_pattern = r'^[^@]+@[^@]+\.[^@]+$'
            valid_emails = col_data.str.match(email_pattern).all()
            text_rules.append({
                'description': f"Email addresses in '{col}' follow valid format",
                'status': 'passed' if valid_emails else 'failed'
            })

        # Rule: No excessive whitespace
        clean_strings = (col_data == col_data.str.strip()).all()
        text_rules.append({
            'description': f"Text values in '{col}' have no leading/trailing whitespace",
            'status': 'passed' if clean_strings else 'warning'
        })

    validation_results['Text Rules'] = text_rules

    return validation_results


def detect_accuracy_outliers(df):
    """Detect outliers that may indicate accuracy issues"""
    outlier_info = {
        'outliers_found': False,
        'total_outliers': 0,
        'column_outliers': {}
    }

    for col in df.select_dtypes(include=[np.number]).columns:
        col_data = df[col].dropna()

        if len(col_data) < 10:  # Need sufficient data for outlier detection
            continue

        # Use IQR method
        q1 = col_data.quantile(0.25)
        q3 = col_data.quantile(0.75)
        iqr = q3 - q1

        # Define outliers as values beyond 1.5 * IQR
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = ((col_data < lower_bound) | (col_data > upper_bound))
        outlier_count = outliers.sum()

        if outlier_count > 0:
            outlier_info['outliers_found'] = True
            outlier_info['total_outliers'] += outlier_count
            outlier_info['column_outliers'][col] = {
                'count': outlier_count,
                'percentage': (outlier_count / len(col_data)) * 100
            }

    return outlier_info


def analyze_pattern_accuracy(df):
    """Analyze accuracy of common data patterns"""
    pattern_analysis = {}

    # Date pattern analysis
    date_patterns = {}
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            col_data = df[col].dropna().astype(str)

            if len(col_data) == 0:
                continue

            # Check for consistent date formats
            common_formats = [
                r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
                r'\d{2}/\d{2}/\d{4}',  # MM/DD/YYYY
                r'\d{2}-\d{2}-\d{4}',  # MM-DD-YYYY
            ]

            format_matches = {}
            for pattern in common_formats:
                matches = col_data.str.contains(pattern, regex=True).sum()
                format_matches[pattern] = matches

            total_matches = sum(format_matches.values())
            if total_matches != len(col_data):
                date_patterns[
                    col] = f"Inconsistent date formats detected ({total_matches}/{len(col_data)} match common patterns)"

    pattern_analysis['Date Patterns'] = {
        'issues': list(date_patterns.values()) if date_patterns else []
    }

    # Identifier pattern analysis
    id_patterns = {}
    for col in df.columns:
        if 'id' in col.lower() and df[col].dtype == 'object':
            col_data = df[col].dropna().astype(str)

            if len(col_data) == 0:
                continue

            # Check for consistent ID length
            lengths = col_data.str.len()
            if lengths.nunique() > 1:
                id_patterns[col] = f"Inconsistent ID lengths (range: {lengths.min()}-{lengths.max()})"

    pattern_analysis['ID Patterns'] = {
        'issues': list(id_patterns.values()) if id_patterns else []
    }

    return pattern_analysis


def generate_accuracy_recommendations(df, accuracy_results, validation_results, outlier_analysis):
    """Generate recommendations for improving accuracy"""
    recommendations = []

    # Based on accuracy score
    if accuracy_results['accuracy_rate'] < 0.8:
        recommendations.append("Implement comprehensive data validation at point of entry")

    # Based on validation rule failures
    for rule_type, rules in validation_results.items():
        failed_rules = [rule for rule in rules if rule['status'] == 'failed']
        if failed_rules:
            recommendations.append(f"Address {len(failed_rules)} failed validation rules in {rule_type}")

    # Based on outliers
    if outlier_analysis['outliers_found']:
        recommendations.append("Review and validate outlier values for potential data entry errors")

    # General recommendations
    recommendations.extend([
        "Establish data quality monitoring and alerting systems",
        "Train data entry personnel on accuracy standards",
        "Implement automated data validation pipelines",
        "Regular accuracy audits and corrections"
    ])

    return recommendations


def create_accuracy_report(df, accuracy_results, validation_results, outlier_analysis, recommendations):
    """Create an accuracy assessment report"""
    report = f"""ACCURACY ASSESSMENT REPORT
Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERVIEW:
- Dataset Dimensions: {df.shape[0]:,} rows × {df.shape[1]} columns
- Total Values Assessed: {accuracy_results['total_values']:,}
- Potential Errors Detected: {accuracy_results['potential_errors']:,}
- Accuracy Rate: {accuracy_results['accuracy_rate']:.1%}
- Confidence Level: {accuracy_results['confidence_level']:.1%}

VALIDATION RESULTS:
"""

    for rule_type, rules in validation_results.items():
        report += f"\n{rule_type}:\n"
        for rule in rules:
            status_symbol = "✅" if rule['status'] == 'passed' else "⚠️" if rule['status'] == 'warning' else "❌"
            report += f"  {status_symbol} {rule['description']}\n"

    report += f"\nOUTLIER ANALYSIS:\n"
    if outlier_analysis['outliers_found']:
        report += f"- Total outliers detected: {outlier_analysis['total_outliers']}\n"
        for col, info in outlier_analysis['column_outliers'].items():
            report += f"- Column '{col}': {info['count']} outliers ({info['percentage']:.1f}%)\n"
    else:
        report += "- No significant outliers detected\n"

    report += "\nRECOMMENDATIONS:\n"
    for i, rec in enumerate(recommendations, 1):
        report += f"{i}. {rec}\n"

    return report


def data_insights():
    """AI-powered data insights and recommendations"""
    create_tool_header("Data Insights", "Generate intelligent insights from your data using AI", "💡")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        df = FileHandler.process_csv_file(uploaded_file[0]) if uploaded_file[0].name.endswith(
            '.csv') else pd.read_excel(uploaded_file[0])

        if df is not None:
            st.subheader("📊 Dataset Overview")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Rows", f"{len(df):,}")
            col2.metric("Columns", len(df.columns))
            col3.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024 ** 2:.2f} MB")
            col4.metric("Missing Values", df.isnull().sum().sum())

            st.dataframe(df.head(), use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                insight_type = st.selectbox("Insight Type:", [
                    "General Overview", "Business Intelligence", "Data Quality Assessment",
                    "Anomaly Detection", "Correlation Analysis", "Predictive Opportunities"
                ])

            with col2:
                analysis_depth = st.selectbox("Analysis Depth:",
                                              ["Quick Analysis", "Detailed Analysis", "Comprehensive Report"])

            target_column = st.selectbox("Focus Column (optional):", ["None"] + list(df.columns))
            business_context = st.text_area("Business Context (optional):",
                                            placeholder="Describe your business domain, goals, or specific questions...")

            if st.button("Generate Insights"):
                with st.spinner("Analyzing data and generating insights..."):
                    # Prepare data summary for AI
                    data_summary = prepare_data_summary(df, target_column if target_column != "None" else None)

                    prompt = f"""Analyze this dataset and provide {insight_type.lower()} insights:

Dataset Summary:
{data_summary}

Business Context: {business_context if business_context else 'General business analysis'}
Analysis Type: {insight_type}
Analysis Depth: {analysis_depth}

Please provide:
1. Key findings and patterns
2. Data quality observations
3. Business recommendations
4. Potential opportunities for improvement
5. Next steps for analysis

Format the response in clear sections with actionable insights."""

                    result = ai_client.generate_text(prompt)

                    if result and not result.startswith("Error"):
                        st.subheader("🔍 AI-Generated Insights")
                        st.text_area("Insights Report:", result, height=500)
                        FileHandler.create_download_link(result.encode(), "data_insights_report.txt", "text/plain")
                    else:
                        st.error(f"Error generating insights: {result}")


def statistical_analysis():
    """Comprehensive statistical analysis tool"""
    create_tool_header("Statistical Analysis", "Perform comprehensive statistical analysis", "📈")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        df = FileHandler.process_csv_file(uploaded_file[0]) if uploaded_file[0].name.endswith(
            '.csv') else pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head(), use_container_width=True)

            # Select analysis type
            analysis_types = st.multiselect("Select Analysis Types:", [
                "Descriptive Statistics", "Distribution Analysis", "Correlation Analysis",
                "Hypothesis Testing", "Regression Analysis", "ANOVA", "Chi-Square Test",
                "Outlier Detection", "Normality Tests", "Variance Analysis"
            ], default=["Descriptive Statistics", "Distribution Analysis"])

            # Select columns for analysis
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

            col1, col2 = st.columns(2)
            with col1:
                selected_numeric = st.multiselect("Numeric Columns:", numeric_cols, default=numeric_cols[:5])
            with col2:
                selected_categorical = st.multiselect("Categorical Columns:", categorical_cols,
                                                      default=categorical_cols[:3])

            confidence_level = st.slider("Confidence Level:", 0.90, 0.99, 0.95, 0.01)

            if st.button("Run Statistical Analysis"):
                with st.spinner("Performing statistical analysis..."):
                    results = {}

                    # Descriptive Statistics
                    if "Descriptive Statistics" in analysis_types and selected_numeric:
                        st.subheader("📊 Descriptive Statistics")
                        desc_stats = df[selected_numeric].describe()
                        st.dataframe(desc_stats, use_container_width=True)
                        results['descriptive'] = desc_stats.to_dict()

                    # Distribution Analysis
                    if "Distribution Analysis" in analysis_types and selected_numeric:
                        st.subheader("📈 Distribution Analysis")
                        for col in selected_numeric[:3]:  # Limit to first 3 columns
                            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

                            # Histogram
                            df[col].hist(bins=30, ax=ax1)
                            ax1.set_title(f'{col} - Histogram')
                            ax1.set_xlabel(col)
                            ax1.set_ylabel('Frequency')

                            # Box plot
                            df.boxplot(column=col, ax=ax2)
                            ax2.set_title(f'{col} - Box Plot')

                            plt.tight_layout()
                            st.pyplot(fig)
                            plt.close()

                    # Correlation Analysis
                    if "Correlation Analysis" in analysis_types and len(selected_numeric) > 1:
                        st.subheader("🔗 Correlation Analysis")
                        corr_matrix = df[selected_numeric].corr()

                        fig, ax = plt.subplots(figsize=(10, 8))
                        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
                        ax.set_title('Correlation Matrix')
                        st.pyplot(fig)
                        plt.close()

                        # Strong correlations
                        strong_corrs = []
                        for i in range(len(corr_matrix.columns)):
                            for j in range(i + 1, len(corr_matrix.columns)):
                                corr_val = corr_matrix.iloc[i, j]
                                if abs(corr_val) > 0.7:
                                    strong_corrs.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_val))

                        if strong_corrs:
                            st.write("**Strong Correlations (|r| > 0.7):**")
                            for col1, col2, corr in strong_corrs:
                                st.write(f"• {col1} ↔ {col2}: {corr:.3f}")

                    # Generate AI summary
                    if results:
                        prompt = f"""Provide a comprehensive statistical analysis summary:

Dataset: {df.shape[0]} rows, {df.shape[1]} columns
Analyzed columns: {selected_numeric + selected_categorical}
Analysis types performed: {', '.join(analysis_types)}
Confidence level: {confidence_level}

Key observations:
- Descriptive statistics patterns
- Distribution characteristics
- Correlation findings
- Data quality issues
- Statistical significance

Provide actionable insights and recommendations."""

                        ai_summary = ai_client.generate_text(prompt)

                        if ai_summary and not ai_summary.startswith("Error"):
                            st.subheader("🤖 AI Statistical Summary")
                            st.text_area("Analysis Summary:", ai_summary, height=300)
                            FileHandler.create_download_link(ai_summary.encode(), "statistical_analysis_summary.txt",
                                                             "text/plain")


def pattern_recognition():
    """AI-powered pattern recognition in data"""
    create_tool_header("Pattern Recognition", "Discover hidden patterns in your data using AI", "🔍")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        df = FileHandler.process_csv_file(uploaded_file[0]) if uploaded_file[0].name.endswith(
            '.csv') else pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head(), use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                pattern_types = st.multiselect("Pattern Types to Detect:", [
                    "Temporal Patterns", "Clustering Patterns", "Anomaly Patterns",
                    "Sequential Patterns", "Correlation Patterns", "Frequency Patterns",
                    "Trend Patterns", "Seasonal Patterns"
                ], default=["Temporal Patterns", "Clustering Patterns"])

            with col2:
                target_column = st.selectbox("Primary Analysis Column:", df.columns)
                secondary_columns = st.multiselect("Secondary Columns:",
                                                   [col for col in df.columns if col != target_column])

            pattern_context = st.text_area("Domain Context:",
                                           placeholder="Describe the type of patterns you're looking for or the business domain...")

            if st.button("Detect Patterns"):
                with st.spinner("Analyzing data for patterns..."):
                    pattern_results = {}

                    # Basic pattern analysis
                    if "Temporal Patterns" in pattern_types:
                        # Check if there are date columns
                        date_cols = [col for col in df.columns if
                                     df[col].dtype == 'datetime64[ns]' or 'date' in col.lower()]
                        if date_cols:
                            st.subheader("⏰ Temporal Patterns")
                            date_col = date_cols[0]

                            # Time series plot
                            if target_column in df.select_dtypes(include=[np.number]).columns:
                                fig, ax = plt.subplots(figsize=(12, 6))
                                df.plot(x=date_col, y=target_column, ax=ax)
                                ax.set_title(f'Temporal Pattern: {target_column} over {date_col}')
                                st.pyplot(fig)
                                plt.close()

                    if "Clustering Patterns" in pattern_types:
                        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
                        if len(numeric_cols) >= 2:
                            st.subheader("🎯 Clustering Patterns")

                            # K-means clustering on first two numeric columns
                            try:
                                from sklearn.cluster import KMeans
                                from sklearn.preprocessing import StandardScaler

                                # Prepare data
                                cluster_data = df[numeric_cols[:2]].dropna()
                                scaler = StandardScaler()
                                scaled_data = scaler.fit_transform(cluster_data)

                                # Perform clustering
                                kmeans = KMeans(n_clusters=3, random_state=42)
                                clusters = kmeans.fit_predict(scaled_data)

                                # Plot clusters
                                fig, ax = plt.subplots(figsize=(10, 6))
                                scatter = ax.scatter(cluster_data.iloc[:, 0], cluster_data.iloc[:, 1], c=clusters,
                                                     cmap='viridis')
                                ax.set_xlabel(numeric_cols[0])
                                ax.set_ylabel(numeric_cols[1])
                                ax.set_title('K-Means Clustering Pattern')
                                plt.colorbar(scatter)
                                st.pyplot(fig)
                                plt.close()

                                pattern_results['clustering'] = {
                                    'n_clusters': 3,
                                    'features': numeric_cols[:2],
                                    'cluster_centers': kmeans.cluster_centers_.tolist()
                                }
                            except Exception as e:
                                st.error(f"Clustering analysis failed: {str(e)}")

                    if "Anomaly Patterns" in pattern_types:
                        st.subheader("⚠️ Anomaly Patterns")

                        if target_column in df.select_dtypes(include=[np.number]).columns:
                            # Simple anomaly detection using IQR
                            Q1 = df[target_column].quantile(0.25)
                            Q3 = df[target_column].quantile(0.75)
                            IQR = Q3 - Q1
                            lower_bound = Q1 - 1.5 * IQR
                            upper_bound = Q3 + 1.5 * IQR

                            anomalies = df[(df[target_column] < lower_bound) | (df[target_column] > upper_bound)]

                            st.write(f"**Anomalies detected in {target_column}:** {len(anomalies)}")
                            if len(anomalies) > 0:
                                st.dataframe(anomalies[[target_column]], use_container_width=True)

                                pattern_results['anomalies'] = {
                                    'count': len(anomalies),
                                    'column': target_column,
                                    'bounds': [lower_bound, upper_bound]
                                }

                    # AI Pattern Analysis
                    prompt = f"""Analyze the following dataset for patterns:

Dataset Information:
- Shape: {df.shape[0]} rows × {df.shape[1]} columns
- Target Column: {target_column}
- Pattern Types Requested: {', '.join(pattern_types)}
- Domain Context: {pattern_context if pattern_context else 'General analysis'}

Column Information:
{df.dtypes.to_string()}

Sample Data:
{df.head().to_string()}

Based on this data, provide insights about:
1. Hidden patterns you can identify
2. Relationships between variables
3. Unusual patterns or anomalies
4. Recommendations for further analysis
5. Business implications of discovered patterns

Be specific and actionable in your recommendations."""

                    ai_patterns = ai_client.generate_text(prompt)

                    if ai_patterns and not ai_patterns.startswith("Error"):
                        st.subheader("🤖 AI Pattern Analysis")
                        st.text_area("Pattern Insights:", ai_patterns, height=400)
                        FileHandler.create_download_link(ai_patterns.encode(), "pattern_recognition_report.txt",
                                                         "text/plain")
                    else:
                        st.error(f"Error in pattern analysis: {ai_patterns}")


def predictive_modeling():
    """AI-powered predictive modeling assistant"""
    create_tool_header("Predictive Modeling", "Build and evaluate predictive models using AI guidance", "🔮")

    uploaded_file = FileHandler.upload_files(['csv', 'xlsx'], accept_multiple=False)

    if uploaded_file:
        df = FileHandler.process_csv_file(uploaded_file[0]) if uploaded_file[0].name.endswith(
            '.csv') else pd.read_excel(uploaded_file[0])

        if df is not None:
            st.dataframe(df.head(), use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                model_type = st.selectbox("Prediction Type:", [
                    "Regression (Predict Numbers)", "Classification (Predict Categories)",
                    "Time Series Forecasting", "Clustering Analysis"
                ])

                target_column = st.selectbox("Target Variable:", df.columns)

            with col2:
                feature_columns = st.multiselect("Feature Columns:",
                                                 [col for col in df.columns if col != target_column],
                                                 default=[col for col in df.columns if col != target_column][:5])

                test_size = st.slider("Test Set Size (%):", 10, 40, 20)

            prediction_goal = st.text_area("Prediction Goal:",
                                           placeholder="Describe what you want to predict and why...")

            if st.button("Build Predictive Model"):
                with st.spinner("Building and evaluating predictive model..."):
                    try:
                        # Data preparation
                        if feature_columns:
                            # Select relevant columns
                            model_data = df[[target_column] + feature_columns].dropna()

                            if len(model_data) > 10:  # Minimum data requirement
                                X = model_data[feature_columns]
                                y = model_data[target_column]

                                # Handle categorical variables
                                from sklearn.preprocessing import LabelEncoder, StandardScaler
                                from sklearn.model_selection import train_test_split
                                from sklearn.metrics import mean_squared_error, accuracy_score

                                # Encode categorical variables
                                le_dict = {}
                                X_processed = X.copy()

                                for col in X.columns:
                                    if X[col].dtype == 'object':
                                        le = LabelEncoder()
                                        X_processed[col] = le.fit_transform(X[col].astype(str))
                                        le_dict[col] = le

                                # Split data
                                X_train, X_test, y_train, y_test = train_test_split(
                                    X_processed, y, test_size=test_size / 100, random_state=42
                                )

                                if model_type.startswith("Regression"):
                                    from sklearn.ensemble import RandomForestRegressor
                                    from sklearn.linear_model import LinearRegression

                                    # Train multiple models
                                    models = {
                                        'Linear Regression': LinearRegression(),
                                        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
                                    }

                                    results = {}
                                    best_model = None
                                    best_score = float('inf')

                                    for name, model in models.items():
                                        model.fit(X_train, y_train)
                                        y_pred = model.predict(X_test)
                                        mse = mean_squared_error(y_test, y_pred)
                                        results[name] = {
                                            'MSE': mse,
                                            'RMSE': np.sqrt(mse),
                                            'R²': model.score(X_test, y_test)
                                        }

                                        if mse < best_score:
                                            best_score = mse
                                            best_model = (name, model)

                                    # Display results
                                    st.subheader("📊 Model Performance")
                                    results_df = pd.DataFrame(results).T
                                    st.dataframe(results_df, use_container_width=True)

                                    # Feature importance (for Random Forest)
                                    if 'Random Forest' in models:
                                        rf_model = models['Random Forest']
                                        feature_importance = pd.DataFrame({
                                            'feature': feature_columns,
                                            'importance': rf_model.feature_importances_
                                        }).sort_values('importance', ascending=False)

                                        st.subheader("🎯 Feature Importance")
                                        fig, ax = plt.subplots(figsize=(10, 6))
                                        sns.barplot(data=feature_importance.head(10), x='importance', y='feature',
                                                    ax=ax)
                                        ax.set_title('Top 10 Most Important Features')
                                        st.pyplot(fig)
                                        plt.close()

                                elif model_type.startswith("Classification"):
                                    from sklearn.ensemble import RandomForestClassifier
                                    from sklearn.linear_model import LogisticRegression

                                    # Encode target if it's categorical
                                    if y.dtype == 'object':
                                        le_target = LabelEncoder()
                                        y_train_encoded = le_target.fit_transform(y_train)
                                        y_test_encoded = le_target.transform(y_test)
                                    else:
                                        y_train_encoded = y_train
                                        y_test_encoded = y_test
                                        le_target = None

                                    # Train models
                                    models = {
                                        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
                                        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
                                    }

                                    results = {}
                                    for name, model in models.items():
                                        model.fit(X_train, y_train_encoded)
                                        y_pred = model.predict(X_test)
                                        accuracy = accuracy_score(y_test_encoded, y_pred)
                                        results[name] = {'Accuracy': accuracy}

                                    st.subheader("📊 Model Performance")
                                    results_df = pd.DataFrame(results).T
                                    st.dataframe(results_df, use_container_width=True)

                                # AI Model Analysis
                                prompt = f"""Analyze this predictive modeling experiment:

Model Configuration:
- Type: {model_type}
- Target Variable: {target_column}
- Features: {', '.join(feature_columns)}
- Dataset Size: {model_data.shape[0]} rows
- Test Set: {test_size}%
- Goal: {prediction_goal if prediction_goal else 'General prediction'}

Data Characteristics:
{model_data.describe().to_string()}

Provide analysis on:
1. Model appropriateness for the problem
2. Feature selection quality
3. Performance interpretation
4. Recommendations for improvement
5. Next steps for model deployment
6. Potential limitations and risks

Be specific and actionable."""

                                ai_analysis = ai_client.generate_text(prompt)

                                if ai_analysis and not ai_analysis.startswith("Error"):
                                    st.subheader("🤖 AI Model Analysis")
                                    st.text_area("Model Analysis:", ai_analysis, height=400)
                                    FileHandler.create_download_link(ai_analysis.encode(),
                                                                     "predictive_model_analysis.txt", "text/plain")
                                else:
                                    st.error(f"Error in model analysis: {ai_analysis}")

                            else:
                                st.error("Insufficient data for modeling. Need at least 10 complete rows.")
                        else:
                            st.error("Please select at least one feature column.")

                    except Exception as e:
                        st.error(f"Error in predictive modeling: {str(e)}")


def prepare_data_summary(df, target_column=None):
    """Prepare a comprehensive data summary for AI analysis"""
    summary = f"""Dataset Overview:
- Shape: {df.shape[0]} rows × {df.shape[1]} columns
- Memory usage: {df.memory_usage(deep=True).sum() / 1024 ** 2:.2f} MB

Column Information:
{df.dtypes.to_frame('Type').to_string()}

Missing Values:
{df.isnull().sum().to_frame('Missing').to_string()}

Numeric Column Statistics:
{df.describe().to_string()}

Sample Data (first 5 rows):
{df.head().to_string()}
"""

    if target_column:
        summary += f"""

Target Column Analysis ({target_column}):
{df[target_column].describe().to_string()}
"""

    return summary
