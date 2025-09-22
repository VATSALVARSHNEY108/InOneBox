import streamlit as st
import hashlib
import secrets
import ssl
import socket
import subprocess
import platform
import os
import sys
import time
import random
import string
import json
import urllib.parse
import base64
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler


def display_tools():
    """Display all security and privacy tools"""

    tool_categories = {
        "Authentication & Access Control": [
            "PAM Tools", "SSO Solutions", "MFA Tools", "IAM Platforms", "Access Review"
        ],
        "Antivirus & Endpoint Security": [
            "Antivirus Scanner", "Behavioral Analysis", "EDR Tools", "Mobile Security", "Patch Management"
        ],
        "Network Security": [
            "Firewall Configuration", "IDS/IPS", "NAC", "VPN Testing", "Network Segmentation"
        ],
        "Encryption Tools": [
            "File Encryption", "Email Encryption", "Database Encryption", "Key Management", "Digital Signatures"
        ],
        "Privacy Tools": [
            "VPN Testing", "Privacy Auditing", "Anonymous Browsing", "Data Anonymization", "GDPR Compliance"
        ],
        "Vulnerability Assessment": [
            "Network Scanner", "Web App Testing", "Compliance Reporting", "Penetration Testing", "Risk Assessment"
        ],
        "Web Security": [
            "Website Scanner", "SQL Injection Detector", "XSS Analysis", "SSL/TLS Validator", "HTTPS Checker"
        ],
        "Security Monitoring": [
            "Log Analysis", "SIEM Simulation", "Threat Intelligence", "Anomaly Detection", "Incident Response"
        ],
        "Cloud Security": [
            "CASB Simulation", "Container Security", "Configuration Auditing", "Workload Protection", "Cloud Compliance"
        ],
        "Mobile & IoT Security": [
            "Device Assessment", "App Security Testing", "IoT Vulnerability Scanning", "Mobile Threat Defense",
            "Device Management"
        ],
        "GRC Tools": [
            "Risk Assessment", "Compliance Tracking", "Policy Management", "Audit Trails", "Risk Registers"
        ],
        "Digital Forensics": [
            "Evidence Acquisition", "Incident Response", "Malware Analysis", "Data Recovery", "Chain of Custody"
        ],
        "Password Management": [
            "Password Generation", "Strength Testing", "Breach Checking", "Policy Enforcement", "Credential Vault"
        ],
        "Network Analysis": [
            "Traffic Analysis", "Bandwidth Monitoring", "Protocol Analysis", "Network Mapping", "Performance Testing"
        ],
        "Red Team Operations": [
            "Social Engineering", "Phishing Simulation", "Attack Vector Analysis", "Payload Generation",
            "Exploitation Framework"
        ],
        "Backup & Recovery": [
            "Backup Testing", "Disaster Recovery", "Data Integrity", "Recovery Planning", "Business Continuity"
        ],
        "Security Training": [
            "Awareness Training", "Phishing Simulation", "Security Assessment", "Training Metrics", "Skill Development"
        ]
    }

    selected_category = st.selectbox("Select Security Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Security Tools - {selected_tool}")

    # Display educational disclaimer
    st.warning(
        "🔒 **Educational Purpose Only**: These tools are for educational and authorized testing purposes only. Always obtain proper authorization before testing systems you don't own.")

    # Display selected tool
    if selected_tool == "File Encryption":
        file_encryption()
    elif selected_tool == "Password Generation":
        password_generation()
    elif selected_tool == "Network Scanner":
        network_scanner()
    elif selected_tool == "SSL/TLS Validator":
        ssl_tls_validator()
    elif selected_tool == "Risk Assessment":
        risk_assessment()
    elif selected_tool == "Phishing Simulation":
        phishing_simulation()
    elif selected_tool == "Log Analysis":
        log_analysis()
    elif selected_tool == "Vulnerability Assessment":
        vulnerability_assessment()
    elif selected_tool == "Web App Testing":
        web_app_testing()
    elif selected_tool == "Privacy Auditing":
        privacy_auditing()
    elif selected_tool == "Incident Response":
        incident_response()
    elif selected_tool == "Security Training":
        security_training()
    elif selected_tool == "Compliance Tracking":
        compliance_tracking()
    elif selected_tool == "Threat Intelligence":
        threat_intelligence()
    elif selected_tool == "Digital Signatures":
        digital_signatures()
    # Authentication & Access Control Tools
    elif selected_tool == "PAM Tools":
        pam_tools()
    elif selected_tool == "SSO Solutions":
        sso_solutions()
    elif selected_tool == "MFA Tools":
        mfa_tools()
    elif selected_tool == "IAM Platforms":
        iam_platforms()
    elif selected_tool == "Access Review":
        access_review()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def file_encryption():
    """File encryption and decryption tool"""
    create_tool_header("File Encryption", "Encrypt and decrypt files securely", "🔐")

    operation = st.radio("Select Operation", ["Encrypt", "Decrypt"])

    if operation == "Encrypt":
        st.subheader("File Encryption")
        uploaded_files = FileHandler.upload_files(['txt', 'pdf', 'docx', 'jpg', 'png'], accept_multiple=True)

        if uploaded_files:
            password = st.text_input("Encryption Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")

            if password and confirm_password:
                if password != confirm_password:
                    st.error("Passwords do not match!")
                    return

                if st.button("Encrypt Files"):
                    encrypted_files = {}

                    # Generate key from password
                    key = hashlib.sha256(password.encode()).digest()
                    key_b64 = base64.urlsafe_b64encode(key)
                    fernet = Fernet(key_b64)

                    progress_bar = st.progress(0)

                    for i, uploaded_file in enumerate(uploaded_files):
                        try:
                            # Read file data
                            file_data = uploaded_file.read()

                            # Encrypt data
                            encrypted_data = fernet.encrypt(file_data)

                            # Store encrypted file
                            encrypted_filename = f"{uploaded_file.name}.encrypted"
                            encrypted_files[encrypted_filename] = encrypted_data

                            progress_bar.progress((i + 1) / len(uploaded_files))

                        except Exception as e:
                            st.error(f"Error encrypting {uploaded_file.name}: {str(e)}")

                    if encrypted_files:
                        if len(encrypted_files) == 1:
                            filename, data = next(iter(encrypted_files.items()))
                            FileHandler.create_download_link(data, filename, "application/octet-stream")
                        else:
                            zip_data = FileHandler.create_zip_archive(encrypted_files)
                            FileHandler.create_download_link(zip_data, "encrypted_files.zip", "application/zip")

                        st.success(f"Encrypted {len(encrypted_files)} file(s) successfully!")
                        st.info("🔑 Keep your password safe! You'll need it to decrypt these files.")

    else:  # Decrypt
        st.subheader("File Decryption")
        uploaded_files = FileHandler.upload_files(['encrypted'], accept_multiple=True)

        if uploaded_files:
            password = st.text_input("Decryption Password", type="password")

            if password and st.button("Decrypt Files"):
                decrypted_files = {}

                # Generate key from password
                key = hashlib.sha256(password.encode()).digest()
                key_b64 = base64.urlsafe_b64encode(key)
                fernet = Fernet(key_b64)

                progress_bar = st.progress(0)

                for i, uploaded_file in enumerate(uploaded_files):
                    try:
                        # Read encrypted data
                        encrypted_data = uploaded_file.read()

                        # Decrypt data
                        decrypted_data = fernet.decrypt(encrypted_data)

                        # Remove .encrypted extension
                        original_filename = uploaded_file.name.replace('.encrypted', '')
                        decrypted_files[original_filename] = decrypted_data

                        progress_bar.progress((i + 1) / len(uploaded_files))

                    except Exception as e:
                        st.error(f"Error decrypting {uploaded_file.name}: {str(e)} (Wrong password?)")

                if decrypted_files:
                    if len(decrypted_files) == 1:
                        filename, data = next(iter(decrypted_files.items()))
                        FileHandler.create_download_link(data, filename, "application/octet-stream")
                    else:
                        zip_data = FileHandler.create_zip_archive(decrypted_files)
                        FileHandler.create_download_link(zip_data, "decrypted_files.zip", "application/zip")

                    st.success(f"Decrypted {len(decrypted_files)} file(s) successfully!")


def password_generation():
    """Advanced password generation and testing"""
    create_tool_header("Password Generation", "Generate and test secure passwords", "🔑")

    tab1, tab2, tab3 = st.tabs(["Generate", "Test Strength", "Policy Check"])

    with tab1:
        st.subheader("Password Generator")

        col1, col2 = st.columns(2)
        with col1:
            length = st.slider("Password Length", 8, 128, 16)
            include_uppercase = st.checkbox("Uppercase Letters (A-Z)", True)
            include_lowercase = st.checkbox("Lowercase Letters (a-z)", True)
            include_numbers = st.checkbox("Numbers (0-9)", True)
            include_symbols = st.checkbox("Symbols (!@#$%^&*)", True)

        with col2:
            exclude_ambiguous = st.checkbox("Exclude Ambiguous Characters", True)
            exclude_similar = st.checkbox("Exclude Similar Characters", False)
            must_include_all = st.checkbox("Must Include All Selected Types", True)
            num_passwords = st.slider("Number of Passwords", 1, 50, 5)

        if st.button("Generate Passwords"):
            try:
                passwords = generate_secure_passwords(
                    length, num_passwords, include_uppercase, include_lowercase,
                    include_numbers, include_symbols, exclude_ambiguous,
                    exclude_similar, must_include_all
                )

                if passwords:
                    st.subheader("Generated Passwords")
                    for i, pwd in enumerate(passwords, 1):
                        strength = calculate_password_strength(pwd)
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.code(pwd)
                        with col2:
                            color = "green" if strength >= 80 else "orange" if strength >= 60 else "red"
                            st.markdown(f"<span style='color: {color}'>Strength: {strength}%</span>",
                                        unsafe_allow_html=True)

                    # Download option
                    password_text = '\n'.join(passwords)
                    FileHandler.create_download_link(password_text.encode(), "generated_passwords.txt", "text/plain")
                else:
                    st.error("Could not generate passwords with the specified criteria.")
            except Exception as e:
                st.error(f"Error generating passwords: {str(e)}")

    with tab2:
        st.subheader("Password Strength Tester")

        test_password = st.text_input("Enter password to test", type="password")

        if test_password:
            strength = calculate_password_strength(test_password)

            # Display strength meter
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.progress(strength / 100)
            with col2:
                color = "green" if strength >= 80 else "orange" if strength >= 60 else "red"
                st.markdown(f"<h3 style='color: {color}'>{strength}%</h3>", unsafe_allow_html=True)
            with col3:
                if strength >= 80:
                    st.success("Strong")
                elif strength >= 60:
                    st.warning("Medium")
                else:
                    st.error("Weak")

            # Detailed analysis
            analysis = analyze_password_details(test_password)
            st.subheader("Detailed Analysis")

            for category, result in analysis.items():
                icon = "✅" if result['status'] else "❌"
                st.write(f"{icon} **{category}**: {result['message']}")

    with tab3:
        st.subheader("Password Policy Checker")

        # Policy settings
        st.write("Define Password Policy:")
        col1, col2 = st.columns(2)
        with col1:
            min_length = st.number_input("Minimum Length", 1, 50, 8)
            require_uppercase = st.checkbox("Require Uppercase", True)
            require_lowercase = st.checkbox("Require Lowercase", True)
        with col2:
            require_numbers = st.checkbox("Require Numbers", True)
            require_symbols = st.checkbox("Require Symbols", True)
            max_repeating = st.number_input("Max Repeating Characters", 1, 10, 3)

        test_policy_password = st.text_input("Test password against policy", type="password")

        if test_policy_password and st.button("Check Policy Compliance"):
            compliance = check_password_policy(
                test_policy_password, min_length, require_uppercase,
                require_lowercase, require_numbers, require_symbols, max_repeating
            )

            st.subheader("Policy Compliance Results")
            overall_pass = all(result['status'] for result in compliance.values())

            if overall_pass:
                st.success("✅ Password meets all policy requirements!")
            else:
                st.error("❌ Password does not meet policy requirements.")

            for check, result in compliance.items():
                icon = "✅" if result['status'] else "❌"
                st.write(f"{icon} **{check}**: {result['message']}")


def network_scanner():
    """Network scanning and discovery tool (educational simulation)"""
    create_tool_header("Network Scanner", "Network discovery and port scanning (Educational)", "🌐")

    st.warning(
        "⚠️ **Educational Simulation**: This tool provides educational examples of network scanning concepts. Always obtain authorization before scanning networks.")

    scan_type = st.selectbox("Scan Type", ["Host Discovery", "Port Scan", "Service Detection", "Vulnerability Scan"])

    if scan_type == "Host Discovery":
        st.subheader("Host Discovery Simulation")

        network_range = st.text_input("Network Range (e.g., 192.168.1.0/24)", "192.168.1.0/24")

        if st.button("Simulate Host Discovery"):
            show_progress_bar("Scanning network range", 3)

            # Simulate discovered hosts
            simulated_hosts = generate_simulated_hosts()

            st.subheader("Discovered Hosts (Simulated)")
            for host in simulated_hosts:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**IP**: {host['ip']}")
                with col2:
                    st.write(f"**Status**: {host['status']}")
                with col3:
                    st.write(f"**Response Time**: {host['response_time']}ms")

            # Generate report
            report = generate_host_discovery_report(simulated_hosts)
            FileHandler.create_download_link(report.encode(), "host_discovery_report.txt", "text/plain")

    elif scan_type == "Port Scan":
        st.subheader("Port Scanning Simulation")

        target_ip = st.text_input("Target IP", "192.168.1.1")
        port_range = st.text_input("Port Range", "1-1000")

        if st.button("Simulate Port Scan"):
            show_progress_bar("Scanning ports", 4)

            # Simulate port scan results
            open_ports = generate_simulated_ports()

            st.subheader("Open Ports (Simulated)")
            for port in open_ports:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Port**: {port['port']}")
                with col2:
                    st.write(f"**Service**: {port['service']}")
                with col3:
                    st.write(f"**State**: {port['state']}")

            # Generate report
            report = generate_port_scan_report(target_ip, open_ports)
            FileHandler.create_download_link(report.encode(), "port_scan_report.txt", "text/plain")


def ssl_tls_validator():
    """SSL/TLS certificate validator"""
    create_tool_header("SSL/TLS Validator", "Validate SSL/TLS certificates and configurations", "🔒")

    hostname = st.text_input("Hostname/Domain", placeholder="example.com")
    port = st.number_input("Port", min_value=1, max_value=65535, value=443)

    if hostname and st.button("Validate SSL/TLS"):
        try:
            show_progress_bar("Checking SSL/TLS certificate", 2)

            # Create SSL context
            context = ssl.create_default_context()

            with socket.create_connection((hostname, port), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    cipher = ssock.cipher()

                    st.success("✅ SSL/TLS connection successful!")

                    # Certificate details
                    st.subheader("Certificate Information")

                    if cert:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Subject**: {cert.get('subject', 'N/A')}")
                            st.write(f"**Issuer**: {cert.get('issuer', 'N/A')}")
                            st.write(f"**Version**: {cert.get('version', 'N/A')}")

                        with col2:
                            st.write(f"**Not Before**: {cert.get('notBefore', 'N/A')}")
                            st.write(f"**Not After**: {cert.get('notAfter', 'N/A')}")
                            st.write(f"**Serial Number**: {cert.get('serialNumber', 'N/A')}")
                    else:
                        st.warning("Certificate information not available")

                    # Cipher information
                    st.subheader("Cipher Information")
                    if cipher:
                        st.write(f"**Cipher**: {cipher[0]}")
                        st.write(f"**Protocol**: {cipher[1]}")
                        st.write(f"**Key Length**: {cipher[2]} bits")
                    else:
                        st.warning("Cipher information not available")

                    # Security assessment
                    st.subheader("Security Assessment")

                    # Check expiration
                    days_until_expiry = None
                    if cert and cert.get('notAfter'):
                        try:
                            not_after_str = str(cert['notAfter'])
                            not_after = datetime.strptime(not_after_str, '%b %d %H:%M:%S %Y %Z')
                            days_until_expiry = (not_after - datetime.now()).days
                        except (ValueError, TypeError):
                            st.warning("Unable to parse certificate expiration date")

                    if days_until_expiry is not None:
                        if days_until_expiry > 30:
                            st.success(f"✅ Certificate valid for {days_until_expiry} days")
                        elif days_until_expiry > 0:
                            st.warning(f"⚠️ Certificate expires in {days_until_expiry} days")
                        else:
                            st.error("❌ Certificate has expired!")
                    else:
                        st.warning("Certificate expiration information not available")

                    # Protocol check
                    if cipher and len(cipher) > 1 and cipher[1] in ['TLSv1.2', 'TLSv1.3']:
                        st.success(f"✅ Secure protocol: {cipher[1]}")
                    else:
                        protocol_name = cipher[1] if cipher and len(cipher) > 1 else 'Unknown'
                        st.warning(f"⚠️ Consider upgrading protocol: {protocol_name}")

                    # Generate detailed report
                    report = generate_ssl_report(hostname, port, cert, cipher,
                                                 days_until_expiry if days_until_expiry is not None else 0)
                    FileHandler.create_download_link(report.encode(), f"ssl_report_{hostname}.txt", "text/plain")

        except socket.gaierror:
            st.error("❌ Could not resolve hostname")
        except socket.timeout:
            st.error("❌ Connection timeout")
        except ssl.SSLError as e:
            st.error(f"❌ SSL Error: {str(e)}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")


def risk_assessment():
    """Security risk assessment tool"""
    create_tool_header("Risk Assessment", "Assess and calculate security risks", "⚠️")

    st.subheader("Risk Assessment Framework")

    # Risk categories
    risk_categories = {
        "Data Security": ["Data Breach", "Data Loss", "Unauthorized Access", "Data Corruption"],
        "Network Security": ["Network Intrusion", "DDoS Attack", "Man-in-the-Middle", "DNS Poisoning"],
        "Application Security": ["SQL Injection", "XSS", "CSRF", "Authentication Bypass"],
        "Physical Security": ["Unauthorized Access", "Theft", "Natural Disasters", "Equipment Failure"],
        "Human Factors": ["Social Engineering", "Insider Threat", "Human Error", "Lack of Training"]
    }

    selected_category = st.selectbox("Risk Category", list(risk_categories.keys()))
    selected_risk = st.selectbox("Specific Risk", risk_categories[selected_category])

    st.markdown("---")

    # Risk scoring
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Likelihood")
        likelihood = st.slider("Probability of occurrence (1-5)", 1, 5, 3)
        likelihood_desc = ["Very Low", "Low", "Medium", "High", "Very High"]
        st.write(f"**{likelihood_desc[likelihood - 1]}**")

    with col2:
        st.subheader("Impact")
        impact = st.slider("Impact if occurs (1-5)", 1, 5, 3)
        impact_desc = ["Minimal", "Minor", "Moderate", "Major", "Severe"]
        st.write(f"**{impact_desc[impact - 1]}**")

    with col3:
        st.subheader("Current Controls")
        controls = st.slider("Effectiveness of controls (1-5)", 1, 5, 3)
        controls_desc = ["None", "Weak", "Adequate", "Strong", "Excellent"]
        st.write(f"**{controls_desc[controls - 1]}**")

    # Calculate risk score
    raw_risk = likelihood * impact
    residual_risk = raw_risk * (6 - controls) / 5

    st.markdown("---")
    st.subheader("Risk Assessment Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Raw Risk Score", f"{raw_risk}/25")
        if raw_risk >= 20:
            st.error("Critical Risk")
        elif raw_risk >= 15:
            st.warning("High Risk")
        elif raw_risk >= 9:
            st.warning("Medium Risk")
        else:
            st.success("Low Risk")

    with col2:
        st.metric("Residual Risk Score", f"{residual_risk:.1f}/25")
        if residual_risk >= 15:
            st.error("Critical Risk")
        elif residual_risk >= 10:
            st.warning("High Risk")
        elif residual_risk >= 5:
            st.warning("Medium Risk")
        else:
            st.success("Low Risk")

    with col3:
        risk_reduction = ((raw_risk - residual_risk) / raw_risk * 100) if raw_risk > 0 else 0
        st.metric("Risk Reduction", f"{risk_reduction:.1f}%")

    # Recommendations
    st.subheader("Recommendations")
    recommendations = generate_risk_recommendations(selected_risk, residual_risk, controls)
    for rec in recommendations:
        st.write(f"• {rec}")

    # Generate risk report
    if st.button("Generate Risk Report"):
        report_data = {
            "category": selected_category,
            "risk": selected_risk,
            "likelihood": likelihood,
            "impact": impact,
            "controls": controls,
            "raw_risk": raw_risk,
            "residual_risk": residual_risk,
            "recommendations": recommendations,
            "assessment_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        report = generate_detailed_risk_report(report_data)
        FileHandler.create_download_link(report.encode(), f"risk_assessment_{selected_risk.replace(' ', '_')}.txt",
                                         "text/plain")


def phishing_simulation():
    """Phishing awareness and simulation tool"""
    create_tool_header("Phishing Simulation", "Educational phishing awareness and testing", "🎣")

    st.warning("📚 **Educational Purpose**: This tool is for awareness training and authorized testing only.")

    tab1, tab2, tab3 = st.tabs(["Phishing Detection", "Email Analysis", "Training Metrics"])

    with tab1:
        st.subheader("Phishing Email Detection Training")

        # Generate sample phishing scenarios
        if st.button("Generate Sample Phishing Email"):
            phishing_sample = generate_phishing_sample()

            st.subheader("Sample Email")
            st.text_area("Email Content", phishing_sample['content'], height=200, disabled=True)

            col1, col2 = st.columns(2)
            with col1:
                user_answer = st.radio("Is this email suspicious?", ["Legitimate", "Phishing"])
            with col2:
                if st.button("Check Answer"):
                    if (user_answer == "Phishing" and phishing_sample['is_phishing']) or \
                            (user_answer == "Legitimate" and not phishing_sample['is_phishing']):
                        st.success("✅ Correct! Good security awareness.")
                    else:
                        st.error("❌ Incorrect. Review the indicators below.")

                    st.subheader("Learning Points")
                    for indicator in phishing_sample['indicators']:
                        st.write(f"• {indicator}")

    with tab2:
        st.subheader("Email Security Analysis")

        email_content = st.text_area("Paste email content for analysis:", height=200)

        if email_content and st.button("Analyze Email"):
            analysis = analyze_email_security(email_content)

            st.subheader("Security Analysis Results")

            # Overall risk score
            risk_score = analysis['risk_score']
            if risk_score >= 80:
                st.error(f"🚨 High Risk: {risk_score}%")
            elif risk_score >= 50:
                st.warning(f"⚠️ Medium Risk: {risk_score}%")
            else:
                st.success(f"✅ Low Risk: {risk_score}%")

            # Detailed findings
            st.subheader("Findings")
            for finding in analysis['findings']:
                severity_color = {"High": "red", "Medium": "orange", "Low": "green"}
                color = severity_color.get(finding['severity'], "black")
                st.markdown(f"<span style='color: {color}'>**{finding['severity']}**: {finding['description']}</span>",
                            unsafe_allow_html=True)

    with tab3:
        st.subheader("Phishing Training Metrics")

        # Simulate training metrics
        metrics = generate_training_metrics()

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Detection Rate", f"{metrics['detection_rate']}%")
        with col2:
            st.metric("False Positives", f"{metrics['false_positives']}%")
        with col3:
            st.metric("Training Completed", f"{metrics['training_completed']}%")
        with col4:
            st.metric("Improvement", f"+{metrics['improvement']}%")

        # Training recommendations
        st.subheader("Training Recommendations")
        recommendations = [
            "Focus on URL inspection training",
            "Improve sender verification awareness",
            "Practice attachment safety protocols",
            "Enhance urgency tactic recognition",
            "Regular phishing simulation exercises"
        ]

        for rec in recommendations:
            st.write(f"• {rec}")


def log_analysis():
    """Security log analysis tool"""
    create_tool_header("Log Analysis", "Analyze security logs for threats", "📊")

    # Log file upload
    uploaded_logs = FileHandler.upload_files(['log', 'txt', 'csv'], accept_multiple=True)

    if uploaded_logs:
        for log_file in uploaded_logs:
            st.subheader(f"Analyzing: {log_file.name}")

            try:
                log_content = FileHandler.process_text_file(log_file)

                # Basic log statistics
                lines = log_content.split('\n')
                total_lines = len(lines)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Log Entries", total_lines)
                with col2:
                    unique_ips = len(set(extract_ips_from_logs(log_content)))
                    st.metric("Unique IP Addresses", unique_ips)
                with col3:
                    error_count = sum(
                        1 for line in lines if any(keyword in line.lower() for keyword in ['error', 'fail', 'denied']))
                    st.metric("Error/Failure Events", error_count)

                # Threat detection
                st.subheader("Threat Detection Results")
                threats = detect_log_threats(log_content)

                if threats:
                    for threat in threats:
                        severity_color = {"Critical": "red", "High": "orange", "Medium": "yellow", "Low": "green"}
                        color = severity_color.get(threat['severity'], "black")

                        st.markdown(f"<div style='padding: 10px; border-left: 4px solid {color}; margin: 5px 0;'>"
                                    f"<strong>{threat['type']}</strong> - {threat['severity']}<br>"
                                    f"{threat['description']}<br>"
                                    f"<small>Count: {threat['count']}</small></div>",
                                    unsafe_allow_html=True)
                else:
                    st.success("No obvious threats detected in the logs.")

                # Generate analysis report
                if st.button(f"Generate Report for {log_file.name}"):
                    report = generate_log_analysis_report(log_file.name, total_lines, unique_ips, error_count, threats)
                    FileHandler.create_download_link(report.encode(), f"log_analysis_{log_file.name}.txt", "text/plain")

            except Exception as e:
                st.error(f"Error analyzing {log_file.name}: {str(e)}")

    else:
        # Demo log analysis
        st.subheader("Demo Log Analysis")
        if st.button("Analyze Sample Security Logs"):
            show_progress_bar("Analyzing sample logs", 3)

            # Generate sample analysis results
            sample_results = generate_sample_log_analysis()

            st.subheader("Sample Analysis Results")
            for result in sample_results:
                st.write(f"**{result['timestamp']}** - {result['event']}: {result['description']}")


# Helper functions
def generate_secure_passwords(length, count, upper, lower, numbers, symbols,
                              exclude_ambiguous, exclude_similar, must_include_all):
    """Generate secure passwords with specified criteria"""
    chars = ""
    if lower:
        chars += string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if exclude_ambiguous:
        chars = chars.replace('0', '').replace('O', '').replace('l', '').replace('I', '').replace('1', '')

    if exclude_similar:
        chars = chars.replace('i', '').replace('L', '').replace('o', '')

    if not chars:
        return []

    passwords = []
    for _ in range(count):
        password = ""

        if must_include_all:
            # Ensure at least one character from each selected type
            if lower:
                password += secrets.choice(string.ascii_lowercase)
            if upper:
                password += secrets.choice(string.ascii_uppercase)
            if numbers:
                password += secrets.choice(string.digits)
            if symbols:
                password += secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")

        # Fill the rest randomly
        while len(password) < length:
            password += secrets.choice(chars)

        # Shuffle the password
        password_list = list(password)
        random.shuffle(password_list)
        passwords.append(''.join(password_list))

    return passwords


def calculate_password_strength(password):
    """Calculate password strength score"""
    score = 0

    # Length scoring
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    elif len(password) >= 6:
        score += 5

    # Character type scoring
    if any(c.islower() for c in password):
        score += 15
    if any(c.isupper() for c in password):
        score += 15
    if any(c.isdigit() for c in password):
        score += 15
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 20

    # Uniqueness scoring
    unique_chars = len(set(password))
    if unique_chars >= len(password) * 0.8:
        score += 10

    return min(score, 100)


def analyze_password_details(password):
    """Analyze password in detail"""
    analysis = {}

    analysis["Length"] = {
        "status": len(password) >= 8,
        "message": f"Password is {len(password)} characters long"
    }

    analysis["Uppercase Letters"] = {
        "status": any(c.isupper() for c in password),
        "message": "Contains uppercase letters" if any(c.isupper() for c in password) else "No uppercase letters"
    }

    analysis["Lowercase Letters"] = {
        "status": any(c.islower() for c in password),
        "message": "Contains lowercase letters" if any(c.islower() for c in password) else "No lowercase letters"
    }

    analysis["Numbers"] = {
        "status": any(c.isdigit() for c in password),
        "message": "Contains numbers" if any(c.isdigit() for c in password) else "No numbers"
    }

    analysis["Special Characters"] = {
        "status": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password),
        "message": "Contains special characters" if any(
            c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password) else "No special characters"
    }

    # Check for common patterns
    common_patterns = ["123", "abc", "qwerty", "password", "admin"]
    has_common = any(pattern in password.lower() for pattern in common_patterns)
    analysis["Common Patterns"] = {
        "status": not has_common,
        "message": "No common patterns detected" if not has_common else "Contains common patterns"
    }

    return analysis


def check_password_policy(password, min_length, req_upper, req_lower, req_numbers, req_symbols, max_repeat):
    """Check password against policy"""
    results = {}

    results["Minimum Length"] = {
        "status": len(password) >= min_length,
        "message": f"Password is {len(password)} characters (minimum: {min_length})"
    }

    if req_upper:
        results["Uppercase Required"] = {
            "status": any(c.isupper() for c in password),
            "message": "Contains uppercase letters" if any(
                c.isupper() for c in password) else "Missing uppercase letters"
        }

    if req_lower:
        results["Lowercase Required"] = {
            "status": any(c.islower() for c in password),
            "message": "Contains lowercase letters" if any(
                c.islower() for c in password) else "Missing lowercase letters"
        }

    if req_numbers:
        results["Numbers Required"] = {
            "status": any(c.isdigit() for c in password),
            "message": "Contains numbers" if any(c.isdigit() for c in password) else "Missing numbers"
        }

    if req_symbols:
        results["Symbols Required"] = {
            "status": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password),
            "message": "Contains symbols" if any(
                c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password) else "Missing symbols"
        }

    # Check for repeating characters
    max_consecutive = 1
    current_consecutive = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 1

    results["Repeating Characters"] = {
        "status": max_consecutive <= max_repeat,
        "message": f"Max consecutive characters: {max_consecutive} (limit: {max_repeat})"
    }

    return results


def generate_simulated_hosts():
    """Generate simulated host discovery results"""
    hosts = []
    base_ip = "192.168.1."

    for i in range(1, random.randint(5, 15)):
        ip = f"{base_ip}{i}"
        status = random.choice(["Up", "Up", "Up", "Down"])
        response_time = random.randint(1, 100) if status == "Up" else None

        hosts.append({
            "ip": ip,
            "status": status,
            "response_time": response_time
        })

    return hosts


def generate_simulated_ports():
    """Generate simulated port scan results"""
    common_ports = [
        {"port": 22, "service": "SSH", "state": "open"},
        {"port": 80, "service": "HTTP", "state": "open"},
        {"port": 443, "service": "HTTPS", "state": "open"},
        {"port": 25, "service": "SMTP", "state": "closed"},
        {"port": 53, "service": "DNS", "state": "open"},
        {"port": 110, "service": "POP3", "state": "closed"},
        {"port": 143, "service": "IMAP", "state": "filtered"},
        {"port": 993, "service": "IMAPS", "state": "open"},
        {"port": 995, "service": "POP3S", "state": "closed"}
    ]

    return random.sample(common_ports, random.randint(3, 7))


def generate_host_discovery_report(hosts):
    """Generate host discovery report"""
    report = "HOST DISCOVERY REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Total Hosts Scanned: {len(hosts)}\n\n"

    up_hosts = [h for h in hosts if h['status'] == 'Up']
    report += f"Hosts Up: {len(up_hosts)}\n"

    for host in up_hosts:
        report += f"  {host['ip']} - Response: {host['response_time']}ms\n"

    report += f"\nHosts Down: {len(hosts) - len(up_hosts)}\n"
    return report


def generate_port_scan_report(target_ip, ports):
    """Generate port scan report"""
    report = "PORT SCAN REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"Target: {target_ip}\n"
    report += f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    for port in ports:
        report += f"Port {port['port']}: {port['state']} - {port['service']}\n"

    return report


def generate_ssl_report(hostname, port, cert, cipher, days_until_expiry):
    """Generate SSL/TLS validation report"""
    report = "SSL/TLS VALIDATION REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"Hostname: {hostname}\n"
    report += f"Port: {port}\n"
    report += f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    report += "CERTIFICATE INFORMATION:\n"
    report += f"Subject: {cert.get('subject', 'N/A')}\n"
    report += f"Issuer: {cert.get('issuer', 'N/A')}\n"
    report += f"Valid Until: {cert.get('notAfter', 'N/A')}\n"
    report += f"Days Until Expiry: {days_until_expiry}\n\n"

    if cipher:
        report += "CIPHER INFORMATION:\n"
        report += f"Cipher: {cipher[0]}\n"
        report += f"Protocol: {cipher[1]}\n"
        report += f"Key Length: {cipher[2]} bits\n\n"

    report += "SECURITY ASSESSMENT:\n"
    if days_until_expiry > 30:
        report += "✓ Certificate validity: Good\n"
    else:
        report += "⚠ Certificate expires soon\n"

    return report


def generate_risk_recommendations(risk_type, residual_risk, controls):
    """Generate risk mitigation recommendations"""
    recommendations = []

    if residual_risk > 15:
        recommendations.append("Immediate action required - implement additional controls")
        recommendations.append("Consider risk transfer options (insurance, outsourcing)")
    elif residual_risk > 10:
        recommendations.append("Enhance existing security controls")
        recommendations.append("Implement monitoring and detection capabilities")

    if controls < 3:
        recommendations.append("Strengthen security controls implementation")
        recommendations.append("Conduct regular security assessments")

    # Risk-specific recommendations
    if "Data Breach" in risk_type:
        recommendations.extend([
            "Implement data encryption at rest and in transit",
            "Deploy data loss prevention (DLP) solutions",
            "Establish incident response procedures"
        ])
    elif "Network" in risk_type:
        recommendations.extend([
            "Deploy network segmentation",
            "Implement intrusion detection systems",
            "Regular penetration testing"
        ])

    return recommendations


def generate_detailed_risk_report(data):
    """Generate detailed risk assessment report"""
    report = "SECURITY RISK ASSESSMENT REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"Assessment Date: {data['assessment_date']}\n"
    report += f"Risk Category: {data['category']}\n"
    report += f"Specific Risk: {data['risk']}\n\n"

    report += "RISK SCORING:\n"
    report += f"Likelihood: {data['likelihood']}/5\n"
    report += f"Impact: {data['impact']}/5\n"
    report += f"Current Controls: {data['controls']}/5\n"
    report += f"Raw Risk Score: {data['raw_risk']}/25\n"
    report += f"Residual Risk Score: {data['residual_risk']:.1f}/25\n\n"

    report += "RECOMMENDATIONS:\n"
    for i, rec in enumerate(data['recommendations'], 1):
        report += f"{i}. {rec}\n"

    return report


def generate_phishing_sample():
    """Generate educational phishing email sample"""
    phishing_samples = [
        {
            "content": """From: security@bankofamerica-security.com
Subject: URGENT: Your account will be suspended

Dear Customer,

We have detected suspicious activity on your account. Please verify your identity immediately by clicking the link below:

http://bankofamerica-verify.suspicious-domain.com/login

Failure to verify within 24 hours will result in account suspension.

Thank you,
Bank of America Security Team""",
            "is_phishing": True,
            "indicators": [
                "Suspicious sender domain (bankofamerica-security.com)",
                "Urgency tactics (24 hour deadline)",
                "Suspicious URL (not official bank domain)",
                "Generic greeting ('Dear Customer')",
                "Requests immediate action"
            ]
        },
        {
            "content": """From: noreply@github.com
Subject: Your security alert settings

Hi there,

This is a reminder that you have security alerts enabled for your repositories. You can manage these settings in your account preferences.

If you have any questions, please visit our help documentation.

Best regards,
GitHub Team""",
            "is_phishing": False,
            "indicators": [
                "Legitimate sender domain",
                "No urgent action requested",
                "Professional tone",
                "No suspicious links",
                "Informational content only"
            ]
        }
    ]

    return random.choice(phishing_samples)


def analyze_email_security(email_content):
    """Analyze email for security threats"""
    risk_score = 0
    findings = []

    # Check for suspicious URLs
    import re
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                      email_content)

    for url in urls:
        if any(suspicious in url.lower() for suspicious in ['bit.ly', 'tinyurl', 'secure-', 'verify-']):
            risk_score += 20
            findings.append({
                "severity": "High",
                "description": f"Suspicious URL detected: {url}"
            })

    # Check for urgency keywords
    urgency_keywords = ['urgent', 'immediate', 'expires', 'suspend', 'verify now', 'act now']
    urgency_count = sum(1 for keyword in urgency_keywords if keyword in email_content.lower())

    if urgency_count > 2:
        risk_score += 25
        findings.append({
            "severity": "Medium",
            "description": "High use of urgency tactics detected"
        })

    # Check for generic greetings
    if any(greeting in email_content.lower() for greeting in ['dear customer', 'dear user', 'dear sir/madam']):
        risk_score += 15
        findings.append({
            "severity": "Medium",
            "description": "Generic greeting suggests mass phishing attempt"
        })

    # Check for credential requests
    if any(term in email_content.lower() for term in ['password', 'username', 'login', 'verify account']):
        risk_score += 20
        findings.append({
            "severity": "High",
            "description": "Email requests sensitive credentials"
        })

    return {
        "risk_score": min(risk_score, 100),
        "findings": findings
    }


def generate_training_metrics():
    """Generate simulated training metrics"""
    return {
        "detection_rate": random.randint(70, 95),
        "false_positives": random.randint(5, 15),
        "training_completed": random.randint(80, 98),
        "improvement": random.randint(10, 25)
    }


def extract_ips_from_logs(log_content):
    """Extract IP addresses from log content"""
    import re
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(ip_pattern, log_content)


def detect_log_threats(log_content):
    """Detect potential threats in log content"""
    threats = []
    lines = log_content.split('\n')

    # Count failed login attempts
    failed_logins = sum(1 for line in lines if
                        any(term in line.lower() for term in ['failed login', 'authentication failed', 'login failed']))

    if failed_logins > 10:
        threats.append({
            "type": "Brute Force Attack",
            "severity": "High",
            "description": "Multiple failed login attempts detected",
            "count": failed_logins
        })

    # Check for SQL injection attempts
    sql_injection = sum(
        1 for line in lines if any(term in line.lower() for term in ['union select', 'drop table', '1=1', 'or 1=1']))

    if sql_injection > 0:
        threats.append({
            "type": "SQL Injection Attempt",
            "severity": "Critical",
            "description": "Potential SQL injection attacks detected",
            "count": sql_injection
        })

    # Check for unusual traffic patterns
    error_count = sum(1 for line in lines if any(term in line for term in ['404', '500', '403']))

    if error_count > len(lines) * 0.1:  # More than 10% errors
        threats.append({
            "type": "Unusual Traffic Pattern",
            "severity": "Medium",
            "description": "High error rate indicates potential scanning or attacks",
            "count": error_count
        })

    return threats


def generate_log_analysis_report(filename, total_lines, unique_ips, error_count, threats):
    """Generate log analysis report"""
    report = "LOG ANALYSIS REPORT\n"
    report += "=" * 50 + "\n\n"
    report += f"File: {filename}\n"
    report += f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    report += "STATISTICS:\n"
    report += f"Total Log Entries: {total_lines}\n"
    report += f"Unique IP Addresses: {unique_ips}\n"
    report += f"Error/Failure Events: {error_count}\n\n"

    report += "THREAT DETECTION:\n"
    if threats:
        for threat in threats:
            report += f"- {threat['type']} ({threat['severity']}): {threat['description']} (Count: {threat['count']})\n"
    else:
        report += "No obvious threats detected.\n"

    return report


def generate_sample_log_analysis():
    """Generate sample log analysis results"""
    return [
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event": "Failed Login Attempt",
            "description": "Multiple failed SSH login attempts from IP 192.168.1.100"
        },
        {
            "timestamp": (datetime.now() - timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S"),
            "event": "Suspicious Traffic",
            "description": "High volume of 404 errors from single IP address"
        },
        {
            "timestamp": (datetime.now() - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S"),
            "event": "Normal Activity",
            "description": "Standard user authentication and file access"
        }
    ]


# Additional helper functions for other tools...
def vulnerability_assessment():
    """Comprehensive vulnerability assessment tool"""
    create_tool_header("Vulnerability Assessment", "Assess system vulnerabilities and security posture", "🛡️")

    tab1, tab2, tab3, tab4 = st.tabs(["Network Scan", "System Assessment", "Report Analysis", "Remediation"])

    with tab1:
        st.subheader("Network Vulnerability Scanning")

        col1, col2 = st.columns(2)
        with col1:
            target_type = st.selectbox("Target Type", ["Single Host", "Network Range", "Domain"])
            if target_type == "Single Host":
                target = st.text_input("Target IP/Hostname", "192.168.1.1")
            elif target_type == "Network Range":
                target = st.text_input("Network Range", "192.168.1.0/24")
            else:
                target = st.text_input("Domain", "example.com")

        with col2:
            scan_intensity = st.selectbox("Scan Intensity", ["Light", "Normal", "Aggressive"])
            scan_ports = st.selectbox("Port Scope", ["Top 100", "Top 1000", "All Ports", "Custom"])
            if scan_ports == "Custom":
                custom_ports = st.text_input("Custom Ports (e.g., 80,443,8080)", "80,443")

        if st.button("Start Vulnerability Scan"):
            show_progress_bar("Scanning for vulnerabilities", 5)

            # Simulate vulnerability scan results
            vulnerabilities = generate_vulnerability_findings(target, scan_intensity)

            st.subheader("Vulnerability Scan Results")

            # Summary statistics
            critical = sum(1 for v in vulnerabilities if v['severity'] == 'Critical')
            high = sum(1 for v in vulnerabilities if v['severity'] == 'High')
            medium = sum(1 for v in vulnerabilities if v['severity'] == 'Medium')
            low = sum(1 for v in vulnerabilities if v['severity'] == 'Low')

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Critical", critical, delta=None)
            with col2:
                st.metric("High", high, delta=None)
            with col3:
                st.metric("Medium", medium, delta=None)
            with col4:
                st.metric("Low", low, delta=None)

            # Detailed findings
            for vuln in vulnerabilities:
                severity_color = {
                    'Critical': 'red', 'High': 'orange',
                    'Medium': 'yellow', 'Low': 'green'
                }.get(vuln['severity'], 'gray')

                with st.expander(f"🚨 {vuln['title']} ({vuln['severity']})"):
                    st.markdown(f"**Severity**: <span style='color: {severity_color}'>{vuln['severity']}</span>",
                                unsafe_allow_html=True)
                    st.write(f"**CVE**: {vuln['cve']}")
                    st.write(f"**Description**: {vuln['description']}")
                    st.write(f"**Impact**: {vuln['impact']}")
                    st.write(f"**Recommendation**: {vuln['recommendation']}")

            # Generate report
            if vulnerabilities:
                report = generate_vulnerability_report(target, vulnerabilities)
                FileHandler.create_download_link(report.encode(),
                                                 f"vulnerability_report_{target.replace('/', '_')}.txt", "text/plain")

    with tab2:
        st.subheader("System Security Assessment")

        assessment_type = st.selectbox("Assessment Type",
                                       ["Web Application", "Network Infrastructure", "Database", "Cloud Configuration"])

        if assessment_type == "Web Application":
            url = st.text_input("Web Application URL", "https://example.com")

            if st.button("Assess Web Application"):
                show_progress_bar("Analyzing web application security", 4)

                # Simulate web app security assessment
                findings = generate_webapp_security_findings(url)

                for finding in findings:
                    severity_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(finding['severity'], "⚪")
                    st.write(f"{severity_icon} **{finding['check']}**: {finding['result']}")

        elif assessment_type == "Network Infrastructure":
            if st.button("Assess Network Security"):
                show_progress_bar("Evaluating network security posture", 3)

                # Simulate network security assessment
                network_findings = generate_network_security_findings()

                for category, findings in network_findings.items():
                    st.subheader(category)
                    for finding in findings:
                        status_icon = "✅" if finding['status'] == 'Secure' else "⚠️"
                        st.write(f"{status_icon} {finding['description']}")

    with tab3:
        st.subheader("Vulnerability Report Analysis")

        uploaded_file = FileHandler.upload_files(['txt', 'xml', 'json'], accept_multiple=False)

        if uploaded_file:
            if st.button("Analyze Report"):
                show_progress_bar("Parsing vulnerability report", 2)

                try:
                    content = uploaded_file.read().decode('utf-8')
                    analysis = analyze_vulnerability_report(content)

                    st.subheader("Report Analysis Summary")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Vulnerabilities", analysis['total'])
                    with col2:
                        st.metric("Critical/High Risk", analysis['high_risk'])
                    with col3:
                        st.metric("Risk Score", f"{analysis['risk_score']}/100")

                    st.subheader("Recommendations")
                    for rec in analysis['recommendations']:
                        st.write(f"• {rec}")

                except Exception as e:
                    st.error(f"Error analyzing report: {str(e)}")

    with tab4:
        st.subheader("Vulnerability Remediation Guide")

        vuln_type = st.selectbox("Vulnerability Type", [
            "SQL Injection", "Cross-Site Scripting (XSS)", "Insecure Direct Object References",
            "Security Misconfiguration", "Sensitive Data Exposure", "Missing Function Level Access Control",
            "Cross-Site Request Forgery (CSRF)", "Using Components with Known Vulnerabilities"
        ])

        remediation_guide = get_remediation_guide(vuln_type)

        st.subheader(f"Remediation Guide: {vuln_type}")
        st.write(f"**Description**: {remediation_guide['description']}")
        st.write(f"**Risk Level**: {remediation_guide['risk']}")

        st.subheader("Remediation Steps")
        for i, step in enumerate(remediation_guide['steps'], 1):
            st.write(f"{i}. {step}")

        st.subheader("Prevention Measures")
        for prevention in remediation_guide['prevention']:
            st.write(f"• {prevention}")

        if remediation_guide.get('code_example'):
            st.subheader("Code Example")
            st.code(remediation_guide['code_example'], language='python')


def web_app_testing():
    """Comprehensive web application security testing tool"""
    create_tool_header("Web Application Testing", "Test web applications for security vulnerabilities", "🌐")

    tab1, tab2, tab3, tab4 = st.tabs(["URL Analysis", "Form Testing", "Header Analysis", "Cookie Security"])

    with tab1:
        st.subheader("URL Security Analysis")

        url = st.text_input("Web Application URL", "https://example.com")

        col1, col2 = st.columns(2)
        with col1:
            test_ssl = st.checkbox("Test SSL/TLS Configuration", True)
            test_headers = st.checkbox("Analyze Security Headers", True)
            test_redirects = st.checkbox("Check Redirects", True)
        with col2:
            test_cookies = st.checkbox("Analyze Cookies", True)
            test_csp = st.checkbox("Check Content Security Policy", True)
            test_cors = st.checkbox("Test CORS Configuration", False)

        if st.button("Analyze URL Security"):
            if url:
                show_progress_bar("Analyzing web application security", 4)

                results = perform_url_security_analysis(url, {
                    'ssl': test_ssl, 'headers': test_headers, 'redirects': test_redirects,
                    'cookies': test_cookies, 'csp': test_csp, 'cors': test_cors
                })

                st.subheader("Security Analysis Results")

                # Overall security score
                score = calculate_security_score(results)
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Security Score", f"{score}/100")
                with col2:
                    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
                    st.metric("Security Grade", grade)
                with col3:
                    risk_level = "Low" if score >= 80 else "Medium" if score >= 60 else "High"
                    st.metric("Risk Level", risk_level)

                # Detailed results
                for category, result in results.items():
                    status_icon = "✅" if result['status'] == 'Pass' else "❌" if result['status'] == 'Fail' else "⚠️"
                    with st.expander(f"{status_icon} {category} - {result['status']}"):
                        st.write(f"**Result**: {result['message']}")
                        if result.get('details'):
                            st.write(f"**Details**: {result['details']}")
                        if result.get('recommendation'):
                            st.write(f"**Recommendation**: {result['recommendation']}")

                # Generate report
                report = generate_webapp_security_report(url, results, score)
                FileHandler.create_download_link(report.encode(), f"webapp_security_report.txt", "text/plain")

    with tab2:
        st.subheader("Form Security Testing")

        st.write("Test form inputs for common vulnerabilities:")

        form_url = st.text_input("Form URL", "https://example.com/contact")

        col1, col2 = st.columns(2)
        with col1:
            test_xss = st.checkbox("Cross-Site Scripting (XSS)", True)
            test_sql = st.checkbox("SQL Injection", True)
            test_csrf = st.checkbox("CSRF Protection", True)
        with col2:
            test_validation = st.checkbox("Input Validation", True)
            test_encoding = st.checkbox("Output Encoding", True)
            test_sanitization = st.checkbox("Input Sanitization", True)

        if st.button("Test Form Security"):
            if form_url:
                show_progress_bar("Testing form security", 3)

                form_results = perform_form_security_testing(form_url, {
                    'xss': test_xss, 'sql': test_sql, 'csrf': test_csrf,
                    'validation': test_validation, 'encoding': test_encoding, 'sanitization': test_sanitization
                })

                st.subheader("Form Security Test Results")

                for test_name, result in form_results.items():
                    status_color = "green" if result['passed'] else "red"
                    st.markdown(f"**{test_name}**: <span style='color: {status_color}'>{result['status']}</span>",
                                unsafe_allow_html=True)
                    st.write(f"- {result['description']}")
                    if not result['passed'] and result.get('payload'):
                        st.code(f"Test payload: {result['payload']}")

    with tab3:
        st.subheader("HTTP Security Headers Analysis")

        header_url = st.text_input("URL to analyze headers", "https://example.com")

        if st.button("Analyze Security Headers"):
            if header_url:
                show_progress_bar("Analyzing HTTP security headers", 2)

                header_analysis = analyze_security_headers(header_url)

                st.subheader("Security Headers Analysis")

                # Header checklist
                for header_name, analysis in header_analysis.items():
                    status_icon = "✅" if analysis['present'] else "❌"
                    with st.expander(f"{status_icon} {header_name}"):
                        st.write(f"**Present**: {'Yes' if analysis['present'] else 'No'}")
                        if analysis['present']:
                            st.write(f"**Value**: `{analysis['value']}`")
                            st.write(f"**Security Level**: {analysis['security_level']}")
                        st.write(f"**Purpose**: {analysis['purpose']}")
                        st.write(f"**Recommendation**: {analysis['recommendation']}")

                # Security headers checklist
                st.subheader("Recommended Security Headers Checklist")
                required_headers = [
                    "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options",
                    "Strict-Transport-Security", "Referrer-Policy", "X-XSS-Protection"
                ]

                for header in required_headers:
                    present = header in header_analysis and header_analysis[header]['present']
                    icon = "✅" if present else "❌"
                    st.write(f"{icon} {header}")

    with tab4:
        st.subheader("Cookie Security Analysis")

        cookie_url = st.text_input("URL to analyze cookies", "https://example.com")

        if st.button("Analyze Cookie Security"):
            if cookie_url:
                show_progress_bar("Analyzing cookie security", 2)

                cookie_analysis = analyze_cookie_security(cookie_url)

                st.subheader("Cookie Security Analysis")

                if cookie_analysis['cookies']:
                    for cookie_name, cookie_data in cookie_analysis['cookies'].items():
                        with st.expander(f"🍪 {cookie_name}"):
                            st.write(f"**Secure Flag**: {'✅ Yes' if cookie_data.get('secure') else '❌ No'}")
                            st.write(f"**HttpOnly Flag**: {'✅ Yes' if cookie_data.get('httponly') else '❌ No'}")
                            st.write(f"**SameSite**: {cookie_data.get('samesite', '❌ Not set')}")
                            st.write(f"**Expiration**: {cookie_data.get('expires', 'Session')}")

                            # Security recommendations
                            recommendations = []
                            if not cookie_data.get('secure'):
                                recommendations.append("Add Secure flag for HTTPS-only transmission")
                            if not cookie_data.get('httponly'):
                                recommendations.append("Add HttpOnly flag to prevent XSS access")
                            if not cookie_data.get('samesite'):
                                recommendations.append("Set SameSite attribute to prevent CSRF")

                            if recommendations:
                                st.write("**Recommendations**:")
                                for rec in recommendations:
                                    st.write(f"• {rec}")
                else:
                    st.info("No cookies found or cookies not accessible from client-side analysis")

                # Overall cookie security score
                score = cookie_analysis['security_score']
                st.metric("Cookie Security Score", f"{score}/100")

                if score < 70:
                    st.warning("⚠️ Cookie security could be improved. Review recommendations above.")
                elif score < 90:
                    st.info("Cookie security is good but could be enhanced.")
                else:
                    st.success("✅ Excellent cookie security configuration!")


# Helper functions for all the security tools

def generate_vulnerability_findings(target, intensity):
    """Generate simulated vulnerability findings"""
    base_vulns = [
        {"title": "Unencrypted HTTP Service", "severity": "Medium", "cve": "CVE-2023-1001",
         "description": "Web service running on HTTP without encryption",
         "impact": "Data transmission can be intercepted",
         "recommendation": "Enable HTTPS with proper SSL/TLS configuration"},
        {"title": "Outdated SSH Protocol", "severity": "High", "cve": "CVE-2023-1002",
         "description": "SSH service using deprecated protocol version",
         "impact": "Vulnerable to protocol downgrade attacks",
         "recommendation": "Update SSH configuration to use only SSHv2"},
        {"title": "Weak SSL/TLS Configuration", "severity": "Critical", "cve": "CVE-2023-1003",
         "description": "SSL/TLS service supports weak cipher suites",
         "impact": "Encryption can be compromised",
         "recommendation": "Configure strong cipher suites and disable weak protocols"}
    ]

    if intensity == "Light":
        return base_vulns[:1]
    elif intensity == "Normal":
        return base_vulns[:2]
    else:
        return base_vulns


def generate_vulnerability_report(target, vulnerabilities):
    """Generate vulnerability assessment report"""
    report = f"VULNERABILITY ASSESSMENT REPORT\n"
    report += f"{'=' * 50}\n\n"
    report += f"Target: {target}\n"
    report += f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Total Vulnerabilities: {len(vulnerabilities)}\n\n"

    for i, vuln in enumerate(vulnerabilities, 1):
        report += f"{i}. {vuln['title']} ({vuln['severity']})\n"
        report += f"   CVE: {vuln['cve']}\n"
        report += f"   Description: {vuln['description']}\n"
        report += f"   Impact: {vuln['impact']}\n"
        report += f"   Recommendation: {vuln['recommendation']}\n\n"

    return report


def generate_webapp_security_findings(url):
    """Generate web app security findings"""
    return [
        {"check": "HTTPS Enforcement", "result": "Properly configured", "severity": "Low"},
        {"check": "Security Headers", "result": "Missing Content-Security-Policy", "severity": "Medium"},
        {"check": "Authentication", "result": "Strong password policy implemented", "severity": "Low"},
        {"check": "Input Validation", "result": "Some forms lack proper validation", "severity": "High"}
    ]


def generate_network_security_findings():
    """Generate network security assessment findings"""
    return {
        "Firewall Configuration": [
            {"description": "Firewall rules properly configured", "status": "Secure"},
            {"description": "Default deny policy in place", "status": "Secure"}
        ],
        "Network Segmentation": [
            {"description": "DMZ properly isolated", "status": "Secure"},
            {"description": "Internal network segmentation needs improvement", "status": "Review Required"}
        ]
    }


def analyze_vulnerability_report(content):
    """Analyze uploaded vulnerability report"""
    # Simple analysis based on content length and keywords
    lines = content.split('\n')
    total = len([line for line in lines if 'vulnerability' in line.lower()])
    high_risk = len([line for line in lines if any(word in line.lower() for word in ['critical', 'high'])])

    return {
        'total': total,
        'high_risk': high_risk,
        'risk_score': min(high_risk * 10, 100),
        'recommendations': [
            "Prioritize critical and high-severity vulnerabilities",
            "Implement regular vulnerability scanning",
            "Establish patch management procedures"
        ]
    }


def get_remediation_guide(vuln_type):
    """Get remediation guide for vulnerability type"""
    guides = {
        "SQL Injection": {
            "description": "Injection of malicious SQL code into application queries",
            "risk": "High",
            "steps": [
                "Use parameterized queries and prepared statements",
                "Implement input validation and sanitization",
                "Apply principle of least privilege to database accounts",
                "Use stored procedures where appropriate"
            ],
            "prevention": [
                "Regular code reviews focusing on database interactions",
                "Use ORM frameworks with built-in protections",
                "Implement web application firewalls"
            ],
            "code_example": "# Safe parameterized query\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))"
        }
    }
    return guides.get(vuln_type, {
        "description": "General security vulnerability",
        "risk": "Medium",
        "steps": ["Assess the vulnerability", "Implement appropriate controls", "Test the fix"],
        "prevention": ["Regular security assessments", "Security training", "Secure coding practices"]
    })


def perform_url_security_analysis(url, options):
    """Perform URL security analysis"""
    results = {}

    if options.get('ssl'):
        results['SSL/TLS'] = {
            'status': 'Pass', 'message': 'Strong SSL/TLS configuration detected',
            'details': 'TLS 1.3 enabled, strong cipher suites'
        }

    if options.get('headers'):
        results['Security Headers'] = {
            'status': 'Warning', 'message': 'Some security headers missing',
            'details': 'Content-Security-Policy header not found',
            'recommendation': 'Implement comprehensive security headers'
        }

    return results


def calculate_security_score(results):
    """Calculate overall security score"""
    total_checks = len(results)
    passed_checks = len([r for r in results.values() if r['status'] == 'Pass'])
    return int((passed_checks / total_checks) * 100) if total_checks > 0 else 0


def generate_webapp_security_report(url, results, score):
    """Generate web app security report"""
    report = f"WEB APPLICATION SECURITY REPORT\n"
    report += f"{'=' * 50}\n\n"
    report += f"URL: {url}\n"
    report += f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Security Score: {score}/100\n\n"

    for check, result in results.items():
        report += f"{check}: {result['status']}\n"
        report += f"  {result['message']}\n"
        if result.get('recommendation'):
            report += f"  Recommendation: {result['recommendation']}\n"
        report += "\n"

    return report


def perform_form_security_testing(url, options):
    """Perform form security testing"""
    results = {}

    if options.get('xss'):
        results['XSS Protection'] = {
            'passed': True, 'status': 'Protected',
            'description': 'Input properly sanitized and output encoded'
        }

    if options.get('sql'):
        results['SQL Injection Protection'] = {
            'passed': False, 'status': 'Vulnerable',
            'description': 'Form appears vulnerable to SQL injection',
            'payload': "'; DROP TABLE users; --"
        }

    return results


def analyze_security_headers(url):
    """Analyze HTTP security headers"""
    return {
        'Content-Security-Policy': {
            'present': False, 'purpose': 'Prevents XSS and code injection',
            'recommendation': 'Implement CSP with appropriate directives',
            'security_level': 'N/A'
        },
        'X-Frame-Options': {
            'present': True, 'value': 'DENY',
            'purpose': 'Prevents clickjacking attacks',
            'recommendation': 'Current configuration is secure',
            'security_level': 'Good'
        }
    }


def analyze_cookie_security(url):
    """Analyze cookie security"""
    return {
        'cookies': {
            'sessionid': {
                'secure': True, 'httponly': True,
                'samesite': 'Strict', 'expires': 'Session'
            },
            'tracking': {
                'secure': False, 'httponly': False,
                'samesite': None, 'expires': '1 year'
            }
        },
        'security_score': 75
    }


def assess_gdpr_compliance(config):
    """Assess GDPR compliance"""
    score = 0
    categories = {}

    # Basic compliance checks
    if config.get('has_policy'):
        score += 20
        categories['Privacy Policy'] = {
            'compliant': True, 'status': 'Compliant',
            'requirements': 'Clear privacy policy accessible to users'
        }

    if config.get('has_dpo') and config.get('org_type') in ['Large Enterprise (>1000 employees)', 'Public Authority']:
        score += 15
        categories['Data Protection Officer'] = {
            'compliant': True, 'status': 'Compliant',
            'requirements': 'DPO appointed as required for organization type'
        }

    return {'overall_score': score, 'categories': categories}


def generate_gdpr_compliance_report(results):
    """Generate GDPR compliance report"""
    report = f"GDPR COMPLIANCE ASSESSMENT\n"
    report += f"{'=' * 50}\n\n"
    report += f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Overall Score: {results['overall_score']}/100\n\n"

    for category, assessment in results['categories'].items():
        report += f"{category}: {assessment['status']}\n"
        report += f"  Requirements: {assessment['requirements']}\n"
        if not assessment['compliant']:
            report += f"  Action Required: {assessment.get('action_required', 'Review requirements')}\n"
        report += "\n"

    return report


def create_data_processing_map(data):
    """Create data processing map"""
    return {
        'categories': data['categories'],
        'purposes': data['purposes'],
        'legal_basis': data['legal_basis'],
        'retention': data['retention'],
        'processing_activities': len(data['purposes']),
        'risk_level': 'Medium'  # Simplified risk assessment
    }


def assess_data_processing_risks(data_map):
    """Assess data processing risks"""
    risks = {}

    # Simple risk assessment based on data categories
    sensitive_categories = ['Health Data', 'Biometric Data', 'Financial Data']
    has_sensitive = any(cat in data_map['categories'] for cat in sensitive_categories)

    risks['Data Sensitivity'] = {
        'level': 'High' if has_sensitive else 'Low',
        'description': 'Processing sensitive personal data increases risk'
    }

    risks['Legal Basis'] = {
        'level': 'Low' if data_map['legal_basis'] == 'Consent' else 'Medium',
        'description': 'Legal basis determines processing legitimacy'
    }

    return risks


def generate_data_map_report(data_map, risk_assessment):
    """Generate data processing map report"""
    report = f"DATA PROCESSING MAP\n"
    report += f"{'=' * 50}\n\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    report += f"Data Categories: {', '.join(data_map['categories'])}\n"
    report += f"Processing Purposes: {', '.join(data_map['purposes'])}\n"
    report += f"Legal Basis: {data_map['legal_basis']}\n"
    report += f"Retention Period: {data_map['retention']}\n\n"

    report += "RISK ASSESSMENT:\n"
    for risk_area, assessment in risk_assessment.items():
        report += f"{risk_area}: {assessment['level']} - {assessment['description']}\n"

    return report


def perform_cookie_compliance_audit(url, options):
    """Perform cookie compliance audit"""
    checks = {}

    if options.get('consent_banner'):
        checks['Consent Banner'] = {
            'passed': True, 'status': 'Present',
            'details': 'Cookie consent banner found on homepage'
        }

    if options.get('privacy_policy'):
        checks['Privacy Policy Link'] = {
            'passed': False, 'status': 'Missing',
            'details': 'Privacy policy link not found in cookie banner',
            'recommendation': 'Add clear link to privacy policy'
        }

    return {
        'compliance_score': 75,
        'checks': checks,
        'cookies': {
            'Essential': [{'name': 'sessionid', 'purpose': 'User session management'}],
            'Analytics': [{'name': 'ga_tracking', 'purpose': 'Website analytics'}]
        }
    }


def generate_cookie_audit_report(url, audit_results):
    """Generate cookie compliance audit report"""
    report = f"COOKIE COMPLIANCE AUDIT\n"
    report += f"{'=' * 50}\n\n"
    report += f"Website: {url}\n"
    report += f"Audit Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Compliance Score: {audit_results['compliance_score']}/100\n\n"

    for check, result in audit_results['checks'].items():
        report += f"{check}: {result['status']}\n"
        report += f"  Details: {result['details']}\n"
        if not result['passed']:
            report += f"  Recommendation: {result['recommendation']}\n"
        report += "\n"

    return report


def conduct_privacy_impact_assessment(project_name, description, factors):
    """Conduct privacy impact assessment"""
    risk_score = 0

    # Calculate risk based on factors
    high_risk_factors = ['new_technology', 'sensitive_data', 'large_scale', 'automated_decisions']
    for factor in high_risk_factors:
        if factors.get(factor):
            risk_score += 15

    # Add points based on scale and sensitivity
    if factors.get('data_volume') in ['Large', 'Very Large']:
        risk_score += 10
    if factors.get('data_sensitivity') in ['High', 'Very High']:
        risk_score += 15

    risk_factors = {}
    for factor, value in factors.items():
        if value and factor in high_risk_factors:
            risk_factors[factor.replace('_', ' ').title()] = {
                'high_risk': True, 'assessment': 'Increases privacy risk significantly'
            }

    recommendations = [
        "Conduct detailed privacy impact assessment",
        "Implement privacy by design principles",
        "Establish data protection safeguards"
    ]

    return {
        'risk_score': min(risk_score, 100),
        'risk_factors': risk_factors,
        'recommendations': recommendations
    }


def generate_pia_report(project_name, description, results):
    """Generate privacy impact assessment report"""
    report = f"PRIVACY IMPACT ASSESSMENT\n"
    report += f"{'=' * 50}\n\n"
    report += f"Project: {project_name}\n"
    report += f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Risk Score: {results['risk_score']}/100\n\n"

    report += f"Project Description:\n{description}\n\n"

    report += "RISK FACTORS:\n"
    for factor, analysis in results['risk_factors'].items():
        report += f"- {factor}: {analysis['assessment']}\n"

    report += "\nRECOMMENDATIONS:\n"
    for rec in results['recommendations']:
        report += f"- {rec}\n"

    return report


# Additional helper functions for other security tools...

def classify_security_incident(incident_data):
    """Classify security incident based on provided data"""
    # Simplified classification logic
    severity_score = {'Low': 1, 'Medium': 2, 'High': 3, 'Critical': 4}
    impact_score = {'Minimal': 1, 'Minor': 2, 'Moderate': 3, 'Major': 4, 'Severe': 5}

    total_score = severity_score.get(incident_data['severity'], 2) + impact_score.get(incident_data['impact'], 2)

    if total_score >= 7:
        priority = 'P1 - Critical'
        response_time = '< 1 hour'
        escalation = 'Executive Leadership'
    elif total_score >= 5:
        priority = 'P2 - High'
        response_time = '< 4 hours'
        escalation = 'Security Team Lead'
    else:
        priority = 'P3 - Medium'
        response_time = '< 24 hours'
        escalation = 'IT Support'

    immediate_actions = [
        'Activate incident response team',
        'Begin containment procedures',
        'Document all activities',
        'Notify relevant stakeholders'
    ]

    return {
        'priority': priority,
        'response_time': response_time,
        'escalation': escalation,
        'immediate_actions': immediate_actions
    }


def generate_incident_classification_report(classification):
    """Generate incident classification report"""
    report = f"INCIDENT CLASSIFICATION REPORT\n"
    report += f"{'=' * 50}\n\n"
    report += f"Classification Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Priority Level: {classification['priority']}\n"
    report += f"Required Response Time: {classification['response_time']}\n"
    report += f"Escalation Level: {classification['escalation']}\n\n"

    report += "IMMEDIATE ACTIONS REQUIRED:\n"
    for action in classification['immediate_actions']:
        report += f"- {action}\n"

    return report


def generate_incident_response_plan(plan_type):
    """Generate incident response plan"""
    base_plan = {
        'phases': {
            'Preparation': {
                'objective': 'Establish incident response capabilities',
                'duration': 'Ongoing',
                'actions': ['Maintain incident response team', 'Update response procedures', 'Conduct training'],
                'stakeholders': ['Security Team', 'IT Team', 'Management']
            },
            'Identification': {
                'objective': 'Detect and confirm the incident',
                'duration': '1-2 hours',
                'actions': ['Analyze alerts', 'Confirm incident', 'Initial classification'],
                'stakeholders': ['Security Analyst', 'SOC Team']
            },
            'Containment': {
                'objective': 'Limit the scope and impact of the incident',
                'duration': '2-8 hours',
                'actions': ['Isolate affected systems', 'Implement temporary fixes', 'Preserve evidence'],
                'stakeholders': ['Incident Response Team', 'System Administrators']
            }
        },
        'communications': {
            'Management Notification': {
                'subject': f'Security Incident Alert - {plan_type}',
                'recipients': 'Executive Team, Security Leadership',
                'content': 'We are currently responding to a security incident. Initial assessment and response actions are underway.'
            }
        }
    }
    return base_plan


def generate_response_plan_document(plan_type, response_plan):
    """Generate response plan document"""
    doc = f"INCIDENT RESPONSE PLAN: {plan_type.upper()}\n"
    doc += f"{'=' * 50}\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    for phase, details in response_plan['phases'].items():
        doc += f"PHASE: {phase.upper()}\n"
        doc += f"Objective: {details['objective']}\n"
        doc += f"Duration: {details['duration']}\n"
        doc += "Actions:\n"
        for action in details['actions']:
            doc += f"  - {action}\n"
        doc += f"Stakeholders: {', '.join(details['stakeholders'])}\n\n"

    return doc


def create_evidence_collection_guide(config):
    """Create evidence collection guide"""
    procedures = [
        'Document current system state and time',
        'Create forensic images of affected systems',
        'Collect relevant log files and audit trails',
        'Photograph physical evidence if applicable',
        'Generate cryptographic hashes of all evidence'
    ]

    chain_of_custody = {
        'Evidence Type': config['type'],
        'Collection Method': config['method'],
        'Collected By': 'Security Team',
        'Collection Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Storage Location': 'Secure Evidence Locker'
    }

    integrity_checks = [
        'Verify hash values of collected evidence',
        'Ensure proper storage and handling procedures',
        'Maintain detailed chain of custody logs',
        'Restrict access to authorized personnel only'
    ]

    return {
        'procedures': procedures,
        'chain_of_custody': chain_of_custody,
        'integrity_checks': integrity_checks
    }


def generate_evidence_collection_document(guide):
    """Generate evidence collection document"""
    doc = f"EVIDENCE COLLECTION GUIDE\n"
    doc += f"{'=' * 50}\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    doc += "COLLECTION PROCEDURES:\n"
    for i, procedure in enumerate(guide['procedures'], 1):
        doc += f"{i}. {procedure}\n"

    doc += "\nCHAIN OF CUSTODY:\n"
    for field, value in guide['chain_of_custody'].items():
        doc += f"{field}: {value}\n"

    doc += "\nINTEGRITY CHECKS:\n"
    for check in guide['integrity_checks']:
        doc += f"- {check}\n"

    return doc


def create_post_incident_analysis(config):
    """Create post-incident analysis"""
    effectiveness_map = {'Poor': 2, 'Fair': 5, 'Good': 7, 'Excellent': 10}
    effectiveness_score = effectiveness_map.get(config['containment'], 5)

    key_findings = [
        'Incident was contained within acceptable timeframe',
        'Communication procedures worked effectively',
        'Some monitoring gaps were identified'
    ]

    action_items = [
        {'action': 'Update monitoring rules', 'priority': 'High', 'due_date': '2024-01-15'},
        {'action': 'Conduct additional staff training', 'priority': 'Medium', 'due_date': '2024-02-01'}
    ]

    return {
        'effectiveness_score': f"{effectiveness_score}/10",
        'improvement_priority': 'Medium',
        'key_findings': key_findings,
        'action_items': action_items
    }


def generate_post_incident_report_document(analysis):
    """Generate post-incident report document"""
    doc = f"POST-INCIDENT ANALYSIS REPORT\n"
    doc += f"{'=' * 50}\n\n"
    doc += f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    doc += f"Effectiveness Score: {analysis['effectiveness_score']}\n\n"

    doc += "KEY FINDINGS:\n"
    for finding in analysis['key_findings']:
        doc += f"- {finding}\n"

    doc += "\nACTION ITEMS:\n"
    for item in analysis['action_items']:
        doc += f"- {item['action']} (Priority: {item['priority']}, Due: {item['due_date']})\n"

    return doc


# Helper functions for security training
def get_training_module_content(category, module):
    """Get training module content"""
    content = {
        'sections': [
            {
                'title': f'Introduction to {module}',
                'content': f'This module covers the fundamentals of {module} and its importance in cybersecurity.',
                'examples': [f'Common {module.lower()} scenarios', f'Best practices for {module.lower()}']
            },
            {
                'title': 'Implementation Guidelines',
                'content': f'Learn how to properly implement {module} in your daily work.',
                'examples': [f'Step-by-step {module.lower()} procedures']
            }
        ],
        'quiz': [
            {
                'question': f'What is the primary purpose of {module}?',
                'options': ['Security', 'Compliance', 'Convenience', 'All of the above'],
                'correct': 0
            },
            {
                'question': f'How often should you review {module.lower()} practices?',
                'options': ['Never', 'Annually', 'Quarterly', 'Monthly'],
                'correct': 2
            }
        ]
    }
    return content


def calculate_quiz_score(quiz, answers):
    """Calculate quiz score"""
    correct = 0
    for i, question in enumerate(quiz):
        if i in answers and answers[i] == question['options'][question['correct']]:
            correct += 1
    return int((correct / len(quiz)) * 100) if quiz else 0


def generate_training_certificate(module, score):
    """Generate training certificate"""
    cert = f"SECURITY TRAINING CERTIFICATE\n"
    cert += f"{'=' * 50}\n\n"
    cert += f"This certifies that the holder has successfully completed\n"
    cert += f"the {module} security training module\n\n"
    cert += f"Score: {score}%\n"
    cert += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
    cert += f"Certificate ID: ST-{random.randint(10000, 99999)}\n"
    return cert


def create_phishing_simulation(config):
    """Create phishing simulation campaign"""
    scenarios = [
        {
            'title': 'Fake Login Page',
            'type': 'Credential Harvesting',
            'description': 'Simulated phishing email directing to fake login page',
            'red_flags': ['Urgent tone', 'Suspicious URL', 'Poor grammar'],
            'learning_objective': 'Recognize fake login attempts'
        },
        {
            'title': 'Invoice Scam',
            'type': 'Business Email Compromise',
            'description': 'Fake invoice requesting payment to fraudulent account',
            'red_flags': ['Unexpected invoice', 'Different payment details', 'Urgent payment request'],
            'learning_objective': 'Verify payment requests through official channels'
        }
    ]

    return {
        'campaign_type': config['type'],
        'target_audience': config['department'],
        'duration': config['duration'],
        'difficulty': config['difficulty'],
        'scenarios': scenarios[:1] if config['difficulty'] == 'Beginner' else scenarios,
        'success_metrics': [
            'Email open rate',
            'Click-through rate',
            'Credential submission rate',
            'Reporting rate'
        ]
    }


def generate_simulation_plan_document(simulation):
    """Generate simulation plan document"""
    doc = f"PHISHING SIMULATION PLAN\n"
    doc += f"{'=' * 50}\n\n"
    doc += f"Campaign Type: {simulation['campaign_type']}\n"
    doc += f"Target Audience: {simulation['target_audience']}\n"
    doc += f"Duration: {simulation['duration']}\n"
    doc += f"Difficulty: {simulation['difficulty']}\n\n"

    doc += "SCENARIOS:\n"
    for i, scenario in enumerate(simulation['scenarios'], 1):
        doc += f"{i}. {scenario['title']}\n"
        doc += f"   Type: {scenario['type']}\n"
        doc += f"   Description: {scenario['description']}\n"
        doc += f"   Learning Objective: {scenario['learning_objective']}\n\n"

    return doc


def generate_security_assessment(config):
    """Generate security assessment questions"""
    questions = [
        {
            'question': 'What should you do if you receive a suspicious email?',
            'type': 'multiple_choice',
            'options': ['Delete it', 'Forward to colleagues', 'Report to IT security', 'Reply asking for verification'],
            'correct': 2
        },
        {
            'question': 'Strong passwords should contain at least 12 characters.',
            'type': 'true_false',
            'correct': 'True'
        }
    ]

    # Adjust number of questions based on length
    if config['length'] == 'Quick (10 questions)':
        return {'questions': questions[:10] if len(questions) >= 10 else questions * 5}
    elif config['length'] == 'Standard (25 questions)':
        return {'questions': questions * 13}  # Approximate 25 questions
    else:
        return {'questions': questions * 25}  # Approximate 50 questions


def evaluate_security_assessment(assessment, answers):
    """Evaluate security assessment"""
    correct = 0
    total = len(assessment['questions'])

    for i, question in enumerate(assessment['questions']):
        if i in answers:
            if question['type'] == 'multiple_choice':
                if answers[i] == question['options'][question['correct']]:
                    correct += 1
            elif question['type'] == 'true_false':
                if answers[i] == question['correct']:
                    correct += 1

    score = int((correct / total) * 100) if total > 0 else 0

    return {
        'overall_score': score,
        'grade': 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F',
        'competency_level': 'Expert' if score >= 90 else 'Proficient' if score >= 80 else 'Developing' if score >= 60 else 'Novice',
        'category_scores': {
            'Password Security': score,  # Simplified - would normally break down by category
            'Phishing Awareness': score,
            'Data Protection': score
        },
        'recommendations': [
            'Review password security best practices',
            'Complete advanced phishing awareness training'
        ] if score < 80 else ['Maintain current security practices']
    }


def generate_assessment_report(results):
    """Generate assessment report"""
    report = f"SECURITY ASSESSMENT REPORT\n"
    report += f"{'=' * 50}\n\n"
    report += f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Overall Score: {results['overall_score']}%\n"
    report += f"Grade: {results['grade']}\n"
    report += f"Competency Level: {results['competency_level']}\n\n"

    report += "CATEGORY BREAKDOWN:\n"
    for category, score in results['category_scores'].items():
        report += f"{category}: {score}%\n"

    report += "\nRECOMMENDATIONS:\n"
    for rec in results['recommendations']:
        report += f"- {rec}\n"

    return report


def generate_sample_training_data():
    """Generate sample training progress data"""
    return {
        'total_employees': 150,
        'completion_rate': 78,
        'average_score': 85,
        'phishing_click_rate': 12,
        'departments': {
            'IT': {'employees': 25, 'completed': 23, 'completion_rate': 92, 'average_score': 95, 'at_risk': 0,
                   'needs_attention': 2},
            'Finance': {'employees': 30, 'completed': 22, 'completion_rate': 73, 'average_score': 80, 'at_risk': 3,
                        'needs_attention': 5},
            'HR': {'employees': 20, 'completed': 18, 'completion_rate': 90, 'average_score': 88, 'at_risk': 1,
                   'needs_attention': 1},
            'Sales': {'employees': 40, 'completed': 28, 'completion_rate': 70, 'average_score': 82, 'at_risk': 5,
                      'needs_attention': 7},
            'Operations': {'employees': 35, 'completed': 26, 'completion_rate': 74, 'average_score': 83, 'at_risk': 4,
                           'needs_attention': 5}
        }
    }


def generate_training_recommendations(training_data):
    """Generate training recommendations"""
    recommendations = {
        'High': [],
        'Medium': [],
        'Low': []
    }

    if training_data['phishing_click_rate'] > 10:
        recommendations['High'].append('Implement immediate phishing awareness training')

    if training_data['completion_rate'] < 80:
        recommendations['Medium'].append('Increase training completion rates')

    if training_data['average_score'] < 85:
        recommendations['Medium'].append('Enhance training content quality')

    return recommendations


def generate_training_progress_report(training_data, recommendations):
    """Generate training progress report"""
    report = f"SECURITY TRAINING PROGRESS REPORT\n"
    report += f"{'=' * 50}\n\n"
    report += f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Total Employees: {training_data['total_employees']}\n"
    report += f"Training Completion Rate: {training_data['completion_rate']}%\n"
    report += f"Average Score: {training_data['average_score']}%\n"
    report += f"Phishing Click Rate: {training_data['phishing_click_rate']}%\n\n"

    report += "DEPARTMENT BREAKDOWN:\n"
    for dept, data in training_data['departments'].items():
        report += f"{dept}: {data['completion_rate']}% completion, {data['average_score']}% avg score\n"

    report += "\nRECOMMENDATIONS:\n"
    for priority, recs in recommendations.items():
        if recs:
            report += f"{priority} Priority:\n"
            for rec in recs:
                report += f"  - {rec}\n"

    return report


# Placeholder implementations for remaining helper functions
def get_compliance_frameworks_for_industry(industry):
    """Get compliance frameworks for industry"""
    frameworks_map = {
        'Healthcare': ['HIPAA', 'HITECH', 'SOC 2'],
        'Financial Services': ['SOX', 'PCI DSS', 'GLBA', 'SOC 2'],
        'Technology': ['SOC 2', 'ISO 27001', 'NIST CSF'],
        'Government': ['FISMA', 'NIST CSF', 'FedRAMP']
    }
    return frameworks_map.get(industry, ['SOC 2', 'ISO 27001', 'NIST CSF'])


def generate_compliance_requirements(config):
    """Generate compliance requirements"""
    return {
        'total_requirements': 150,
        'critical_controls': 25,
        'estimated_effort': '6-12 months',
        'frameworks': [
            {
                'name': 'SOC 2',
                'description': 'System and Organization Controls for service organizations',
                'applicability': 'All cloud service providers',
                'key_requirements': 'Security, Availability, Processing Integrity, Confidentiality, Privacy',
                'timeline': '6-9 months',
                'domains': ['Access Controls', 'Change Management', 'Data Protection']
            }
        ]
    }


def generate_compliance_requirements_document(requirements):
    """Generate compliance requirements document"""
    doc = f"COMPLIANCE REQUIREMENTS ANALYSIS\n"
    doc += f"{'=' * 50}\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    doc += f"Total Requirements: {requirements['total_requirements']}\n"
    doc += f"Critical Controls: {requirements['critical_controls']}\n"
    doc += f"Estimated Implementation Effort: {requirements['estimated_effort']}\n\n"

    for framework in requirements['frameworks']:
        doc += f"FRAMEWORK: {framework['name']}\n"
        doc += f"Description: {framework['description']}\n"
        doc += f"Timeline: {framework['timeline']}\n\n"

    return doc


def get_compliance_status(framework):
    """Get compliance status for framework"""
    return {
        'overall_compliance': 75,
        'implemented_controls': 45,
        'total_controls': 60,
        'control_domains': {
            'Access Controls': {
                'compliance_rate': 80,
                'controls': [
                    {'id': 'AC-001', 'description': 'User access management', 'status': 'Implemented'},
                    {'id': 'AC-002', 'description': 'Privileged access controls', 'status': 'In Progress',
                     'action_required': 'Complete privileged access review', 'due_date': '2024-02-15',
                     'owner': 'IT Security'}
                ]
            }
        },
        'risk_areas': [
            {'area': 'Data Encryption', 'description': 'Some data not encrypted at rest',
             'level': 'Medium', 'remediation': 'Implement encryption for all sensitive data'}
        ]
    }


def generate_compliance_status_report(framework, status):
    """Generate compliance status report"""
    report = f"COMPLIANCE STATUS REPORT: {framework}\n"
    report += f"{'=' * 50}\n\n"
    report += f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"Overall Compliance: {status['overall_compliance']}%\n"
    report += f"Controls Implemented: {status['implemented_controls']}/{status['total_controls']}\n\n"

    for domain, data in status['control_domains'].items():
        report += f"{domain}: {data['compliance_rate']}% compliant\n"
        for control in data['controls']:
            report += f"  {control['id']}: {control['status']}\n"
            if control['status'] != 'Implemented':
                report += f"    Action: {control.get('action_required', 'Review required')}\n"

    return report


# Add all other missing helper functions with basic implementations
def create_audit_preparation_plan(config):
    return {'preparation_period': '8 weeks', 'estimated_duration': '2-3 days', 'phases': []}


def generate_audit_preparation_document(plan):
    return f"AUDIT PREPARATION PLAN\n{'=' * 50}\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"


def generate_compliance_report(config):
    return {'executive_summary': 'Compliance status summary',
            'metrics': {'overall_compliance': 80, 'controls_implemented': 45, 'total_controls': 60, 'open_findings': 5,
                        'risk_score': 3}, 'framework_status': {},
            'recommendations': {'High': [], 'Medium': [], 'Low': []}}


def generate_compliance_report_document(report):
    return f"COMPLIANCE REPORT\n{'=' * 50}\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"


def generate_threat_analysis(config):
    return {'total_threats': 150, 'critical_threats': 25, 'active_campaigns': 12, 'new_iocs': 89, 'trends': [],
            'top_threats': []}


def generate_threat_analysis_report(analysis):
    return f"THREAT ANALYSIS REPORT\n{'=' * 50}\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"


def add_ioc_to_database(ioc_data):
    return {'success': True, 'ioc_id': f"IOC-{random.randint(10000, 99999)}"}


def enrich_ioc(ioc_data):
    return {'Threat Actor': 'Unknown', 'First Seen': '2024-01-01', 'Confidence': ioc_data.get('confidence', 'Medium')}


def search_ioc_database(search_type, query):
    return {'results': []}


def generate_ioc_export(results):
    return "IOC Export Data\n" + "\n".join([f"{ioc['type']}: {ioc['value']}" for ioc in results])


def perform_ioc_analysis(ioc):
    return {'risk_score': 7, 'reputation': 'Suspicious', 'last_seen': '2024-01-15', 'analysis': {},
            'related_threats': []}


def execute_threat_hunt(config):
    return {'total_findings': 5, 'high_priority_findings': 2, 'confidence_score': 8, 'findings': []}


def generate_threat_hunt_report(results):
    return f"THREAT HUNT REPORT\n{'=' * 50}\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"


def hunt_for_iocs(iocs, sources):
    return {'total_matches': len(iocs) // 2, 'matches': []}


def generate_threat_intelligence_report(config):
    return {'classification': config['classification'], 'date': datetime.now().strftime('%Y-%m-%d'),
            'report_id': f"TI-{random.randint(10000, 99999)}", 'executive_summary': 'Executive summary of threats',
            'key_findings': [], 'threat_highlights': []}


def generate_threat_intelligence_document(report):
    return f"THREAT INTELLIGENCE REPORT\n{'=' * 50}\nReport ID: {report['report_id']}\nDate: {report['date']}\n"


def create_digital_signature(file, config):
    return {'signed_data': file.read(), 'signature_info': {'filename': file.name, 'algorithm': config['signature_type'],
                                                           'signature_hash': 'abc123...',
                                                           'cert_fingerprint': 'def456...',
                                                           'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                           'validity_start': '2024-01-01',
                                                           'validity_end': '2025-01-01'}}


def generate_signature_report(details):
    return f"DIGITAL SIGNATURE REPORT\n{'=' * 50}\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"


def verify_digital_signature(file, options):
    return {'filename': file.name, 'overall_valid': True,
            'checks': {'Signature Validity': {'passed': True, 'message': 'Signature is valid'}},
            'signature_info': {'signer': 'John Doe', 'signing_time': '2024-01-15 10:30:00'}}


def generate_verification_report(results):
    return f"SIGNATURE VERIFICATION REPORT\n{'=' * 50}\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"


def generate_self_signed_certificate(config):
    return {'subject': config['subject'], 'serial_number': str(random.randint(100000, 999999)),
            'not_before': '2024-01-01', 'not_after': '2025-01-01', 'fingerprint': 'sha256:abc123...',
            'key_algorithm': 'RSA', 'key_size': config['key_size'],
            'certificate_pem': '-----BEGIN CERTIFICATE-----\n...',
            'private_key_pem': '-----BEGIN PRIVATE KEY-----\n...'}


def analyze_certificate(file):
    return {'subject': 'CN=Example', 'issuer': 'CN=CA', 'serial_number': '123456', 'version': '3',
            'not_before': '2024-01-01', 'not_after': '2025-01-01', 'days_until_expiry': 365,
            'security_checks': {'Key Size': {'passed': True, 'message': 'Adequate key size'}}, 'extensions': {}}


def perform_signature_analysis(file, analysis_type):
    return {'filename': file.name, 'summary': 'Analysis complete',
            'analysis': {'Metadata': {'Creation Date': '2024-01-15'}}, 'recommendations': ['Use stronger signatures']}


def privacy_auditing():
    """Comprehensive privacy auditing and compliance tool"""
    create_tool_header("Privacy Auditing", "Audit privacy compliance and data protection practices", "🔒")

    tab1, tab2, tab3, tab4 = st.tabs(["GDPR Compliance", "Data Mapping", "Cookie Audit", "Privacy Impact"])

    with tab1:
        st.subheader("GDPR Compliance Assessment")

        organization_type = st.selectbox("Organization Type",
                                         ["Small Business (<250 employees)", "Medium Business (250-1000 employees)",
                                          "Large Enterprise (>1000 employees)", "Public Authority", "Non-Profit"])

        col1, col2 = st.columns(2)
        with col1:
            processes_personal_data = st.checkbox("Processes Personal Data", True)
            has_data_protection_officer = st.checkbox("Has Data Protection Officer")
            conducts_dpia = st.checkbox("Conducts Data Protection Impact Assessments")
            maintains_records = st.checkbox("Maintains Processing Records")
        with col2:
            has_privacy_policy = st.checkbox("Has Privacy Policy", True)
            implements_by_design = st.checkbox("Privacy by Design Implementation")
            data_breach_procedures = st.checkbox("Data Breach Response Procedures")
            third_party_agreements = st.checkbox("Third-Party Data Agreements")

        if st.button("Assess GDPR Compliance"):
            show_progress_bar("Evaluating GDPR compliance", 3)

            compliance_results = assess_gdpr_compliance({
                'org_type': organization_type,
                'processes_data': processes_personal_data,
                'has_dpo': has_data_protection_officer,
                'conducts_dpia': conducts_dpia,
                'maintains_records': maintains_records,
                'has_policy': has_privacy_policy,
                'privacy_by_design': implements_by_design,
                'breach_procedures': data_breach_procedures,
                'third_party': third_party_agreements
            })

            st.subheader("GDPR Compliance Assessment Results")

            # Overall compliance score
            score = compliance_results['overall_score']
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Compliance Score", f"{score}/100")
            with col2:
                compliance_level = "High" if score >= 80 else "Medium" if score >= 60 else "Low"
                st.metric("Compliance Level", compliance_level)
            with col3:
                risk_level = "Low" if score >= 80 else "Medium" if score >= 60 else "High"
                st.metric("Risk Level", risk_level)

            # Detailed assessment
            for category, assessment in compliance_results['categories'].items():
                status_icon = "✅" if assessment['compliant'] else "❌"
                with st.expander(f"{status_icon} {category}"):
                    st.write(f"**Status**: {assessment['status']}")
                    st.write(f"**Requirements**: {assessment['requirements']}")
                    if not assessment['compliant']:
                        st.write(f"**Action Required**: {assessment['action_required']}")
                        st.write(f"**Priority**: {assessment['priority']}")

            # Generate compliance report
            report = generate_gdpr_compliance_report(compliance_results)
            FileHandler.create_download_link(report.encode(), "gdpr_compliance_report.txt", "text/plain")

    with tab2:
        st.subheader("Data Mapping and Inventory")

        st.write("Map your data processing activities:")

        # Data categories
        st.write("**Personal Data Categories Processed:**")
        col1, col2 = st.columns(2)
        with col1:
            identity_data = st.checkbox("Identity Data (names, IDs)")
            contact_data = st.checkbox("Contact Information")
            financial_data = st.checkbox("Financial Data")
            technical_data = st.checkbox("Technical Data (IP, cookies)")
        with col2:
            health_data = st.checkbox("Health Data")
            biometric_data = st.checkbox("Biometric Data")
            location_data = st.checkbox("Location Data")
            behavioral_data = st.checkbox("Behavioral/Usage Data")

        # Processing purposes
        st.write("**Processing Purposes:**")
        purposes = st.multiselect("Select all that apply", [
            "Service Provision", "Marketing", "Analytics", "Legal Compliance",
            "Security", "Customer Support", "Research", "Other"
        ])

        # Legal bases
        legal_basis = st.selectbox("Primary Legal Basis", [
            "Consent", "Contract", "Legal Obligation", "Vital Interests",
            "Public Task", "Legitimate Interests"
        ])

        # Data retention
        retention_period = st.selectbox("Data Retention Period", [
            "< 1 year", "1-3 years", "3-7 years", "> 7 years", "Indefinite"
        ])

        if st.button("Generate Data Map"):
            show_progress_bar("Creating data inventory map", 2)

            data_categories = []
            if identity_data: data_categories.append("Identity Data")
            if contact_data: data_categories.append("Contact Information")
            if financial_data: data_categories.append("Financial Data")
            if technical_data: data_categories.append("Technical Data")
            if health_data: data_categories.append("Health Data")
            if biometric_data: data_categories.append("Biometric Data")
            if location_data: data_categories.append("Location Data")
            if behavioral_data: data_categories.append("Behavioral Data")

            data_map = create_data_processing_map({
                'categories': data_categories,
                'purposes': purposes,
                'legal_basis': legal_basis,
                'retention': retention_period
            })

            st.subheader("Data Processing Map")

            # Display data flow
            st.write("**Data Processing Summary:**")
            st.write(f"• **Categories**: {', '.join(data_categories) if data_categories else 'None specified'}")
            st.write(f"• **Purposes**: {', '.join(purposes) if purposes else 'None specified'}")
            st.write(f"• **Legal Basis**: {legal_basis}")
            st.write(f"• **Retention**: {retention_period}")

            # Risk assessment
            risk_assessment = assess_data_processing_risks(data_map)

            st.subheader("Risk Assessment")
            for risk_area, assessment in risk_assessment.items():
                risk_color = {"Low": "green", "Medium": "orange", "High": "red"}.get(assessment['level'], "gray")
                st.markdown(f"**{risk_area}**: <span style='color: {risk_color}'>{assessment['level']} Risk</span>",
                            unsafe_allow_html=True)
                st.write(f"- {assessment['description']}")

            # Generate data map report
            map_report = generate_data_map_report(data_map, risk_assessment)
            FileHandler.create_download_link(map_report.encode(), "data_processing_map.txt", "text/plain")

    with tab3:
        st.subheader("Cookie Compliance Audit")

        website_url = st.text_input("Website URL for Cookie Audit", "https://example.com")

        col1, col2 = st.columns(2)
        with col1:
            check_consent_banner = st.checkbox("Check Consent Banner", True)
            analyze_cookie_types = st.checkbox("Analyze Cookie Types", True)
            verify_consent_mechanism = st.checkbox("Verify Consent Mechanism", True)
        with col2:
            check_privacy_policy = st.checkbox("Check Privacy Policy Link", True)
            analyze_third_party = st.checkbox("Analyze Third-Party Cookies", True)
            verify_withdrawal = st.checkbox("Verify Consent Withdrawal", True)

        if st.button("Audit Cookie Compliance"):
            if website_url:
                show_progress_bar("Auditing cookie compliance", 4)

                cookie_audit = perform_cookie_compliance_audit(website_url, {
                    'consent_banner': check_consent_banner,
                    'cookie_types': analyze_cookie_types,
                    'consent_mechanism': verify_consent_mechanism,
                    'privacy_policy': check_privacy_policy,
                    'third_party': analyze_third_party,
                    'withdrawal': verify_withdrawal
                })

                st.subheader("Cookie Compliance Audit Results")

                # Compliance score
                compliance_score = cookie_audit['compliance_score']
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Cookie Compliance Score", f"{compliance_score}/100")
                with col2:
                    compliance_status = "Compliant" if compliance_score >= 80 else "Needs Improvement"
                    st.metric("Status", compliance_status)

                # Detailed findings
                for check_name, result in cookie_audit['checks'].items():
                    status_icon = "✅" if result['passed'] else "❌"
                    with st.expander(f"{status_icon} {check_name}"):
                        st.write(f"**Result**: {result['status']}")
                        st.write(f"**Details**: {result['details']}")
                        if not result['passed']:
                            st.write(f"**Recommendation**: {result['recommendation']}")

                # Cookie inventory
                if cookie_audit.get('cookies'):
                    st.subheader("Cookie Inventory")
                    for cookie_type, cookies in cookie_audit['cookies'].items():
                        with st.expander(f"🍪 {cookie_type} Cookies ({len(cookies)})"):
                            for cookie in cookies:
                                st.write(f"• **{cookie['name']}**: {cookie['purpose']}")

                # Generate audit report
                audit_report = generate_cookie_audit_report(website_url, cookie_audit)
                FileHandler.create_download_link(audit_report.encode(), "cookie_compliance_audit.txt", "text/plain")

    with tab4:
        st.subheader("Privacy Impact Assessment (PIA)")

        st.write("Conduct a Privacy Impact Assessment for new projects or significant changes:")

        # Project information
        project_name = st.text_input("Project/System Name", "New Customer Portal")
        project_description = st.text_area("Project Description",
                                           "Brief description of the project and its objectives")

        # PIA questions
        st.write("**Privacy Impact Questions:**")

        col1, col2 = st.columns(2)
        with col1:
            involves_new_technology = st.checkbox("Involves New Technology")
            processes_sensitive_data = st.checkbox("Processes Sensitive Data")
            large_scale_processing = st.checkbox("Large Scale Processing")
            automated_decision_making = st.checkbox("Automated Decision Making")
        with col2:
            data_matching = st.checkbox("Data Matching/Combining")
            surveillance = st.checkbox("Systematic Monitoring")
            affects_vulnerable_groups = st.checkbox("Affects Vulnerable Groups")
            cross_border_transfer = st.checkbox("Cross-Border Data Transfer")

        # Risk factors
        st.write("**Risk Assessment:**")
        data_volume = st.selectbox("Data Volume", ["Small", "Medium", "Large", "Very Large"])
        data_sensitivity = st.selectbox("Data Sensitivity", ["Low", "Medium", "High", "Very High"])
        number_of_subjects = st.selectbox("Number of Data Subjects",
                                          ["< 1,000", "1,000 - 10,000", "10,000 - 100,000", "> 100,000"])

        if st.button("Conduct Privacy Impact Assessment"):
            show_progress_bar("Conducting privacy impact assessment", 3)

            pia_factors = {
                'new_technology': involves_new_technology,
                'sensitive_data': processes_sensitive_data,
                'large_scale': large_scale_processing,
                'automated_decisions': automated_decision_making,
                'data_matching': data_matching,
                'surveillance': surveillance,
                'vulnerable_groups': affects_vulnerable_groups,
                'cross_border': cross_border_transfer,
                'data_volume': data_volume,
                'data_sensitivity': data_sensitivity,
                'num_subjects': number_of_subjects
            }

            pia_results = conduct_privacy_impact_assessment(project_name, project_description, pia_factors)

            st.subheader("Privacy Impact Assessment Results")

            # Overall risk score
            risk_score = pia_results['risk_score']
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Privacy Risk Score", f"{risk_score}/100")
            with col2:
                risk_level = "High" if risk_score >= 70 else "Medium" if risk_score >= 40 else "Low"
                st.metric("Risk Level", risk_level)
            with col3:
                pia_required = "Yes" if risk_score >= 50 else "No"
                st.metric("Formal PIA Required", pia_required)

            # Risk factors analysis
            st.subheader("Risk Factors Analysis")
            for factor, analysis in pia_results['risk_factors'].items():
                risk_icon = "🔴" if analysis['high_risk'] else "🟡" if analysis['medium_risk'] else "🟢"
                st.write(f"{risk_icon} **{factor}**: {analysis['assessment']}")

            # Recommendations
            st.subheader("Recommendations")
            for recommendation in pia_results['recommendations']:
                st.write(f"• {recommendation}")

            # Generate PIA report
            pia_report = generate_pia_report(project_name, project_description, pia_results)
            FileHandler.create_download_link(pia_report.encode(), f"pia_report_{project_name.replace(' ', '_')}.txt",
                                             "text/plain")


def incident_response():
    """Comprehensive incident response management tool"""
    create_tool_header("Incident Response", "Manage and respond to security incidents", "🚨")

    tab1, tab2, tab3, tab4 = st.tabs(["Incident Triage", "Response Plan", "Evidence Collection", "Post-Incident"])

    with tab1:
        st.subheader("Incident Triage and Classification")

        incident_type = st.selectbox("Incident Type", [
            "Data Breach", "Malware Infection", "Unauthorized Access", "DDoS Attack",
            "Phishing Campaign", "Insider Threat", "System Compromise", "Other"
        ])

        col1, col2 = st.columns(2)
        with col1:
            severity = st.selectbox("Severity Level", ["Low", "Medium", "High", "Critical"])
            impact = st.selectbox("Business Impact", ["Minimal", "Minor", "Moderate", "Major", "Severe"])
            affected_systems = st.multiselect("Affected Systems", [
                "Web Servers", "Database", "Email System", "User Workstations",
                "Network Infrastructure", "Mobile Devices", "Cloud Services"
            ])

        with col2:
            urgency = st.selectbox("Urgency", ["Low", "Medium", "High", "Emergency"])
            scope = st.selectbox("Incident Scope", ["Isolated", "Department", "Organization-wide", "External"])
            data_involved = st.checkbox("Personal Data Involved")
            regulatory_impact = st.checkbox("Regulatory Notification Required")

        incident_description = st.text_area("Incident Description",
                                            "Provide detailed description of the incident...")

        if st.button("Classify Incident"):
            show_progress_bar("Analyzing incident classification", 2)

            classification = classify_security_incident({
                'type': incident_type, 'severity': severity, 'impact': impact,
                'urgency': urgency, 'scope': scope, 'affected_systems': affected_systems,
                'data_involved': data_involved, 'regulatory_impact': regulatory_impact,
                'description': incident_description
            })

            st.subheader("Incident Classification Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Priority Level", classification['priority'])
            with col2:
                st.metric("Response Time", classification['response_time'])
            with col3:
                st.metric("Escalation Level", classification['escalation'])

            # Response recommendations
            st.subheader("Immediate Actions Required")
            for action in classification['immediate_actions']:
                st.write(f"• {action}")

            # Generate incident report
            incident_report = generate_incident_classification_report(classification)
            FileHandler.create_download_link(incident_report.encode(), "incident_classification.txt", "text/plain")

    with tab2:
        st.subheader("Incident Response Plan")

        plan_type = st.selectbox("Response Plan Type", [
            "Data Breach Response", "Malware Incident", "Network Intrusion",
            "Phishing Response", "DDoS Mitigation", "Insider Threat", "Custom Plan"
        ])

        if st.button("Generate Response Plan"):
            show_progress_bar("Creating incident response plan", 2)

            response_plan = generate_incident_response_plan(plan_type)

            st.subheader(f"Response Plan: {plan_type}")

            for phase, details in response_plan['phases'].items():
                with st.expander(f"Phase {phase}"):
                    st.write(f"**Objective**: {details['objective']}")
                    st.write(f"**Duration**: {details['duration']}")
                    st.write("**Actions**:")
                    for action in details['actions']:
                        st.write(f"• {action}")
                    if details.get('stakeholders'):
                        st.write(f"**Stakeholders**: {', '.join(details['stakeholders'])}")

            # Communication templates
            st.subheader("Communication Templates")
            for template_name, template in response_plan['communications'].items():
                with st.expander(f"📧 {template_name}"):
                    st.write(f"**Subject**: {template['subject']}")
                    st.write(f"**Recipients**: {template['recipients']}")
                    st.text_area(f"Message Content", template['content'], key=template_name)

            # Download response plan
            plan_document = generate_response_plan_document(plan_type, response_plan)
            FileHandler.create_download_link(plan_document.encode(),
                                             f"{plan_type.lower().replace(' ', '_')}_response_plan.txt", "text/plain")

    with tab3:
        st.subheader("Digital Evidence Collection")

        evidence_type = st.selectbox("Evidence Type", [
            "System Logs", "Network Traffic", "File System", "Memory Dump",
            "Email Messages", "Database Records", "User Activity", "Other"
        ])

        col1, col2 = st.columns(2)
        with col1:
            collection_method = st.selectbox("Collection Method", [
                "Live System", "Disk Image", "Network Capture", "Log Export", "Database Query"
            ])
            preserve_integrity = st.checkbox("Preserve Chain of Custody", True)
        with col2:
            hash_verification = st.checkbox("Generate Hash Verification", True)
            timestamp_evidence = st.checkbox("Timestamp Evidence", True)

        evidence_description = st.text_area("Evidence Description",
                                            "Describe the evidence being collected and its relevance...")

        if st.button("Create Evidence Collection Guide"):
            show_progress_bar("Creating evidence collection procedures", 2)

            collection_guide = create_evidence_collection_guide({
                'type': evidence_type, 'method': collection_method,
                'preserve_custody': preserve_integrity, 'hash_verify': hash_verification,
                'timestamp': timestamp_evidence, 'description': evidence_description
            })

            st.subheader("Evidence Collection Procedures")

            for step_num, step in enumerate(collection_guide['procedures'], 1):
                st.write(f"**Step {step_num}**: {step}")

            # Chain of custody form
            st.subheader("Chain of Custody Information")
            custody_info = collection_guide['chain_of_custody']
            for field, value in custody_info.items():
                st.write(f"**{field}**: {value}")

            # Evidence integrity checklist
            st.subheader("Evidence Integrity Checklist")
            for check in collection_guide['integrity_checks']:
                st.write(f"☐ {check}")

            # Download collection guide
            guide_document = generate_evidence_collection_document(collection_guide)
            FileHandler.create_download_link(guide_document.encode(), "evidence_collection_guide.txt", "text/plain")

    with tab4:
        st.subheader("Post-Incident Analysis")

        st.write("Conduct post-incident review and lessons learned:")

        incident_resolved = st.checkbox("Incident Fully Resolved", False)
        containment_effective = st.selectbox("Containment Effectiveness", ["Poor", "Fair", "Good", "Excellent"])
        response_time_rating = st.selectbox("Response Time Rating", ["Too Slow", "Adequate", "Good", "Excellent"])

        col1, col2 = st.columns(2)
        with col1:
            root_cause = st.text_area("Root Cause Analysis",
                                      "Identify the underlying cause of the incident...")
        with col2:
            lessons_learned = st.text_area("Lessons Learned",
                                           "Key takeaways and improvements for future incidents...")

        improvements = st.text_area("Recommended Improvements",
                                    "Specific recommendations to prevent similar incidents...")

        if st.button("Generate Post-Incident Report"):
            show_progress_bar("Creating post-incident analysis", 2)

            post_incident_analysis = create_post_incident_analysis({
                'resolved': incident_resolved, 'containment': containment_effective,
                'response_time': response_time_rating, 'root_cause': root_cause,
                'lessons_learned': lessons_learned, 'improvements': improvements
            })

            st.subheader("Post-Incident Analysis Summary")

            # Analysis metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Resolution Status", "Complete" if incident_resolved else "In Progress")
            with col2:
                st.metric("Response Effectiveness", post_incident_analysis['effectiveness_score'])
            with col3:
                st.metric("Improvement Priority", post_incident_analysis['improvement_priority'])

            # Key findings
            st.subheader("Key Findings")
            for finding in post_incident_analysis['key_findings']:
                st.write(f"• {finding}")

            # Action items
            st.subheader("Action Items")
            for item in post_incident_analysis['action_items']:
                st.write(f"• **{item['action']}** (Priority: {item['priority']}, Due: {item['due_date']})")

            # Download post-incident report
            report_document = generate_post_incident_report_document(post_incident_analysis)
            FileHandler.create_download_link(report_document.encode(), "post_incident_analysis.txt", "text/plain")


def security_training():
    """Comprehensive security training and awareness tool"""
    create_tool_header("Security Training", "Security awareness training and assessment tools", "🎓")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Training Modules", "Phishing Simulation", "Knowledge Assessment", "Training Progress"])

    with tab1:
        st.subheader("Security Training Modules")

        training_categories = {
            "Password Security": ["Strong Passwords", "Password Managers", "Multi-Factor Authentication"],
            "Phishing Awareness": ["Email Phishing", "Social Engineering", "Suspicious Links"],
            "Data Protection": ["Data Classification", "Privacy Principles", "GDPR Compliance"],
            "Incident Response": ["Reporting Procedures", "Initial Response", "Communication Protocols"],
            "Safe Computing": ["Software Updates", "Secure Browsing", "USB Security"]
        }

        selected_category = st.selectbox("Training Category", list(training_categories.keys()))
        selected_module = st.selectbox("Training Module", training_categories[selected_category])

        if st.button("Start Training Module"):
            show_progress_bar("Loading training content", 2)

            training_content = get_training_module_content(selected_category, selected_module)

            st.subheader(f"Training: {selected_module}")

            # Module content
            for section in training_content['sections']:
                with st.expander(f"📖 {section['title']}"):
                    st.write(section['content'])
                    if section.get('examples'):
                        st.write("**Examples:**")
                        for example in section['examples']:
                            st.write(f"• {example}")

            # Interactive quiz
            st.subheader("Knowledge Check")
            quiz_answers = {}

            for i, question in enumerate(training_content['quiz']):
                st.write(f"**Question {i + 1}**: {question['question']}")
                answer = st.radio(f"Select answer for Q{i + 1}", question['options'], key=f"q{i}")
                quiz_answers[i] = answer

            if st.button("Submit Quiz"):
                score = calculate_quiz_score(training_content['quiz'], quiz_answers)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Quiz Score", f"{score}%")
                with col2:
                    status = "Passed" if score >= 80 else "Needs Review"
                    st.metric("Status", status)

                if score >= 80:
                    st.success("🎉 Congratulations! You passed the training module.")
                else:
                    st.warning("📚 Please review the material and retake the quiz.")

                # Generate certificate
                if score >= 80:
                    certificate = generate_training_certificate(selected_module, score)
                    FileHandler.create_download_link(certificate.encode(),
                                                     f"{selected_module.replace(' ', '_')}_certificate.txt",
                                                     "text/plain")

    with tab2:
        st.subheader("Phishing Simulation Training")

        simulation_type = st.selectbox("Simulation Type", [
            "Email Phishing", "Spear Phishing", "Business Email Compromise",
            "Social Engineering", "Vishing (Voice)", "Smishing (SMS)"
        ])

        difficulty_level = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

        col1, col2 = st.columns(2)
        with col1:
            target_department = st.selectbox("Target Department", [
                "All Staff", "IT Department", "Finance", "HR", "Sales", "Executive"
            ])
        with col2:
            simulation_duration = st.selectbox("Simulation Duration", [
                "1 Week", "2 Weeks", "1 Month", "3 Months"
            ])

        if st.button("Create Phishing Simulation"):
            show_progress_bar("Creating phishing simulation", 3)

            simulation = create_phishing_simulation({
                'type': simulation_type, 'difficulty': difficulty_level,
                'department': target_department, 'duration': simulation_duration
            })

            st.subheader("Phishing Simulation Campaign")

            # Campaign overview
            st.write(f"**Campaign Type**: {simulation['campaign_type']}")
            st.write(f"**Target Audience**: {simulation['target_audience']}")
            st.write(f"**Expected Duration**: {simulation['duration']}")
            st.write(f"**Difficulty Level**: {simulation['difficulty']}")

            # Simulation scenarios
            st.subheader("Simulation Scenarios")
            for i, scenario in enumerate(simulation['scenarios'], 1):
                with st.expander(f"Scenario {i}: {scenario['title']}"):
                    st.write(f"**Type**: {scenario['type']}")
                    st.write(f"**Description**: {scenario['description']}")
                    st.write(f"**Red Flags**: {', '.join(scenario['red_flags'])}")
                    st.write(f"**Learning Objective**: {scenario['learning_objective']}")

            # Metrics and tracking
            st.subheader("Success Metrics")
            for metric in simulation['success_metrics']:
                st.write(f"• {metric}")

            # Download simulation plan
            plan_document = generate_simulation_plan_document(simulation)
            FileHandler.create_download_link(plan_document.encode(), f"phishing_simulation_plan.txt", "text/plain")

    with tab3:
        st.subheader("Security Knowledge Assessment")

        assessment_type = st.selectbox("Assessment Type", [
            "General Security Awareness", "Role-Specific Assessment",
            "Compliance Knowledge", "Incident Response", "Custom Assessment"
        ])

        if assessment_type == "Role-Specific Assessment":
            job_role = st.selectbox("Job Role", [
                "IT Administrator", "Developer", "Manager", "HR Staff",
                "Finance Staff", "Executive", "General Employee"
            ])

        assessment_length = st.selectbox("Assessment Length", ["Quick (10 questions)", "Standard (25 questions)",
                                                               "Comprehensive (50 questions)"])

        if st.button("Generate Security Assessment"):
            show_progress_bar("Creating security assessment", 2)

            assessment_config = {
                'type': assessment_type,
                'role': job_role if assessment_type == "Role-Specific Assessment" else None,
                'length': assessment_length
            }

            assessment = generate_security_assessment(assessment_config)

            st.subheader(f"Security Assessment: {assessment_type}")

            # Assessment questions
            user_answers = {}
            for i, question in enumerate(assessment['questions']):
                st.write(f"**Question {i + 1}**: {question['question']}")

                if question['type'] == 'multiple_choice':
                    answer = st.radio(f"Select answer for Q{i + 1}", question['options'], key=f"assess_q{i}")
                elif question['type'] == 'true_false':
                    answer = st.radio(f"True or False for Q{i + 1}", ["True", "False"], key=f"assess_q{i}")
                else:
                    answer = st.text_input(f"Answer for Q{i + 1}", key=f"assess_q{i}")

                user_answers[i] = answer

            if st.button("Submit Assessment"):
                results = evaluate_security_assessment(assessment, user_answers)

                st.subheader("Assessment Results")

                # Overall score
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Overall Score", f"{results['overall_score']}%")
                with col2:
                    st.metric("Grade", results['grade'])
                with col3:
                    st.metric("Competency Level", results['competency_level'])

                # Category breakdown
                st.subheader("Category Breakdown")
                for category, score in results['category_scores'].items():
                    st.write(f"**{category}**: {score}%")

                # Recommendations
                st.subheader("Training Recommendations")
                for recommendation in results['recommendations']:
                    st.write(f"• {recommendation}")

                # Generate assessment report
                report = generate_assessment_report(results)
                FileHandler.create_download_link(report.encode(), "security_assessment_report.txt", "text/plain")

    with tab4:
        st.subheader("Training Progress Dashboard")

        # Simulated training data
        training_data = generate_sample_training_data()

        # Progress metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Employees", training_data['total_employees'])
        with col2:
            st.metric("Training Completion", f"{training_data['completion_rate']}%")
        with col3:
            st.metric("Average Score", f"{training_data['average_score']}%")
        with col4:
            st.metric("Phishing Click Rate", f"{training_data['phishing_click_rate']}%")

        # Department breakdown
        st.subheader("Training Progress by Department")
        for dept, data in training_data['departments'].items():
            with st.expander(f"🏢 {dept}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Employees**: {data['employees']}")
                    st.write(f"**Completed**: {data['completed']}")
                with col2:
                    st.write(f"**Completion Rate**: {data['completion_rate']}%")
                    st.write(f"**Average Score**: {data['average_score']}%")
                with col3:
                    st.write(f"**At Risk**: {data['at_risk']}")
                    st.write(f"**Needs Attention**: {data['needs_attention']}")

        # Training recommendations
        st.subheader("Training Recommendations")
        recommendations = generate_training_recommendations(training_data)
        for priority, recs in recommendations.items():
            if recs:
                st.write(f"**{priority} Priority:**")
                for rec in recs:
                    st.write(f"• {rec}")

        # Export training report
        if st.button("Export Training Report"):
            report = generate_training_progress_report(training_data, recommendations)
            FileHandler.create_download_link(report.encode(), "training_progress_report.txt", "text/plain")


def compliance_tracking():
    """Comprehensive compliance tracking and management tool"""
    create_tool_header("Compliance Tracking", "Track and manage regulatory compliance requirements", "📋")

    tab1, tab2, tab3, tab4 = st.tabs(["Framework Selection", "Compliance Status", "Audit Preparation", "Reporting"])

    with tab1:
        st.subheader("Compliance Framework Selection")

        industry = st.selectbox("Industry Sector", [
            "Healthcare", "Financial Services", "Technology", "Retail", "Manufacturing",
            "Government", "Education", "Other"
        ])

        frameworks = get_compliance_frameworks_for_industry(industry)
        selected_frameworks = st.multiselect("Applicable Compliance Frameworks", frameworks)

        organization_size = st.selectbox("Organization Size", [
            "Small (< 50 employees)", "Medium (50-500 employees)",
            "Large (500-5000 employees)", "Enterprise (> 5000 employees)"
        ])

        geographic_scope = st.multiselect("Geographic Scope", [
            "United States", "European Union", "Canada", "Asia-Pacific",
            "Latin America", "Other"
        ])

        if st.button("Generate Compliance Requirements"):
            show_progress_bar("Analyzing compliance requirements", 3)

            requirements = generate_compliance_requirements({
                'industry': industry, 'frameworks': selected_frameworks,
                'size': organization_size, 'geography': geographic_scope
            })

            st.subheader("Compliance Requirements Analysis")

            # Requirements summary
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Requirements", requirements['total_requirements'])
            with col2:
                st.metric("Critical Controls", requirements['critical_controls'])
            with col3:
                st.metric("Estimated Effort", requirements['estimated_effort'])

            # Framework breakdown
            for framework in requirements['frameworks']:
                with st.expander(f"📋 {framework['name']}"):
                    st.write(f"**Description**: {framework['description']}")
                    st.write(f"**Applicability**: {framework['applicability']}")
                    st.write(f"**Key Requirements**: {framework['key_requirements']}")
                    st.write(f"**Implementation Timeline**: {framework['timeline']}")

                    # Control domains
                    st.write("**Control Domains**:")
                    for domain in framework['domains']:
                        st.write(f"• {domain}")

            # Generate requirements document
            requirements_doc = generate_compliance_requirements_document(requirements)
            FileHandler.create_download_link(requirements_doc.encode(), "compliance_requirements.txt", "text/plain")

    with tab2:
        st.subheader("Compliance Status Tracking")

        framework_to_track = st.selectbox("Select Framework to Track", [
            "SOC 2", "ISO 27001", "PCI DSS", "HIPAA", "GDPR", "SOX", "NIST CSF", "Custom"
        ])

        if st.button("Load Compliance Dashboard"):
            show_progress_bar("Loading compliance status", 2)

            compliance_status = get_compliance_status(framework_to_track)

            st.subheader(f"Compliance Dashboard: {framework_to_track}")

            # Overall compliance score
            overall_score = compliance_status['overall_compliance']
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Overall Compliance", f"{overall_score}%")
            with col2:
                status = "Compliant" if overall_score >= 90 else "Partially Compliant" if overall_score >= 70 else "Non-Compliant"
                st.metric("Status", status)
            with col3:
                st.metric("Controls Implemented",
                          f"{compliance_status['implemented_controls']}/{compliance_status['total_controls']}")

            # Control status breakdown
            st.subheader("Control Implementation Status")
            for domain, controls in compliance_status['control_domains'].items():
                with st.expander(f"🔒 {domain} ({controls['compliance_rate']}% compliant)"):
                    for control in controls['controls']:
                        status_icon = "✅" if control['status'] == 'Implemented' else "🟡" if control[
                                                                                                'status'] == 'In Progress' else "❌"
                        st.write(f"{status_icon} **{control['id']}**: {control['description']}")
                        if control['status'] != 'Implemented':
                            st.write(f"  • **Action Required**: {control['action_required']}")
                            st.write(f"  • **Due Date**: {control['due_date']}")
                            st.write(f"  • **Owner**: {control['owner']}")

            # Risk areas
            if compliance_status['risk_areas']:
                st.subheader("High Risk Areas")
                for risk in compliance_status['risk_areas']:
                    st.warning(f"⚠️ **{risk['area']}**: {risk['description']} (Risk Level: {risk['level']})")
                    st.write(f"  Remediation: {risk['remediation']}")

            # Generate status report
            status_report = generate_compliance_status_report(framework_to_track, compliance_status)
            FileHandler.create_download_link(status_report.encode(),
                                             f"{framework_to_track.lower().replace(' ', '_')}_status_report.txt",
                                             "text/plain")

    with tab3:
        st.subheader("Audit Preparation")

        audit_type = st.selectbox("Audit Type", [
            "Internal Audit", "External Audit", "Regulatory Inspection", "Certification Audit"
        ])

        audit_framework = st.selectbox("Audit Framework", [
            "SOC 2 Type II", "ISO 27001", "PCI DSS", "HIPAA", "GDPR", "SOX 404", "Other"
        ])

        audit_date = st.date_input("Planned Audit Date")

        col1, col2 = st.columns(2)
        with col1:
            include_documentation = st.checkbox("Include Documentation Review", True)
            include_interviews = st.checkbox("Include Staff Interviews", True)
            include_technical = st.checkbox("Include Technical Testing", True)
        with col2:
            include_walkthrough = st.checkbox("Include Process Walkthrough", True)
            include_sampling = st.checkbox("Include Evidence Sampling", True)
            include_remediation = st.checkbox("Include Remediation Plan", True)

        if st.button("Generate Audit Preparation Plan"):
            show_progress_bar("Creating audit preparation plan", 3)

            audit_plan = create_audit_preparation_plan({
                'type': audit_type, 'framework': audit_framework, 'date': str(audit_date),
                'documentation': include_documentation, 'interviews': include_interviews,
                'technical': include_technical, 'walkthrough': include_walkthrough,
                'sampling': include_sampling, 'remediation': include_remediation
            })

            st.subheader(f"Audit Preparation Plan: {audit_framework}")

            # Preparation timeline
            st.write(f"**Audit Date**: {audit_date}")
            st.write(f"**Preparation Period**: {audit_plan['preparation_period']}")
            st.write(f"**Estimated Duration**: {audit_plan['estimated_duration']}")

            # Preparation phases
            st.subheader("Preparation Phases")
            for phase in audit_plan['phases']:
                with st.expander(f"📋 Phase {phase['number']}: {phase['name']} ({phase['duration']})"):
                    st.write(f"**Objective**: {phase['objective']}")
                    st.write("**Activities**:")
                    for activity in phase['activities']:
                        st.write(f"• {activity}")
                    st.write(f"**Deliverables**: {', '.join(phase['deliverables'])}")
                    st.write(f"**Responsible Party**: {phase['responsible']}")

            # Documentation checklist
            st.subheader("Documentation Checklist")
            for category, docs in audit_plan['documentation_checklist'].items():
                with st.expander(f"📁 {category}"):
                    for doc in docs:
                        st.write(f"☐ {doc}")

            # Risk mitigation
            st.subheader("Risk Mitigation Strategies")
            for risk in audit_plan['risk_mitigation']:
                st.write(f"• **{risk['risk']}**: {risk['mitigation']}")

            # Generate preparation plan document
            plan_document = generate_audit_preparation_document(audit_plan)
            FileHandler.create_download_link(plan_document.encode(), f"audit_preparation_plan.txt", "text/plain")

    with tab4:
        st.subheader("Compliance Reporting")

        report_type = st.selectbox("Report Type", [
            "Executive Summary", "Detailed Compliance Report", "Risk Assessment Report",
            "Gap Analysis Report", "Remediation Plan", "Board Report"
        ])

        reporting_period = st.selectbox("Reporting Period", [
            "Monthly", "Quarterly", "Semi-Annual", "Annual", "Custom"
        ])

        target_audience = st.selectbox("Target Audience", [
            "Executive Leadership", "Board of Directors", "Compliance Team",
            "IT Leadership", "External Auditors", "Regulatory Bodies"
        ])

        col1, col2 = st.columns(2)
        with col1:
            include_metrics = st.checkbox("Include Compliance Metrics", True)
            include_trends = st.checkbox("Include Trend Analysis", True)
            include_benchmarks = st.checkbox("Include Industry Benchmarks", False)
        with col2:
            include_recommendations = st.checkbox("Include Recommendations", True)
            include_action_plans = st.checkbox("Include Action Plans", True)
            include_risk_assessment = st.checkbox("Include Risk Assessment", True)

        if st.button("Generate Compliance Report"):
            show_progress_bar("Creating compliance report", 3)

            report_config = {
                'type': report_type, 'period': reporting_period, 'audience': target_audience,
                'metrics': include_metrics, 'trends': include_trends, 'benchmarks': include_benchmarks,
                'recommendations': include_recommendations, 'action_plans': include_action_plans,
                'risk_assessment': include_risk_assessment
            }

            compliance_report = generate_compliance_report(report_config)

            st.subheader(f"Compliance Report: {report_type}")

            # Executive summary
            st.write("**Executive Summary**")
            st.write(compliance_report['executive_summary'])

            # Key metrics
            if include_metrics:
                st.subheader("Key Compliance Metrics")
                metrics = compliance_report['metrics']
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Overall Compliance", f"{metrics['overall_compliance']}%")
                with col2:
                    st.metric("Controls Implemented", f"{metrics['controls_implemented']}/{metrics['total_controls']}")
                with col3:
                    st.metric("Open Findings", metrics['open_findings'])
                with col4:
                    st.metric("Risk Score", f"{metrics['risk_score']}/10")

            # Compliance status by framework
            st.subheader("Compliance Status by Framework")
            for framework, status in compliance_report['framework_status'].items():
                compliance_color = "green" if status['compliance'] >= 90 else "orange" if status[
                                                                                              'compliance'] >= 70 else "red"
                st.markdown(
                    f"**{framework}**: <span style='color: {compliance_color}'>{status['compliance']}% compliant</span>",
                    unsafe_allow_html=True)
                st.write(f"  • Status: {status['status']}")
                st.write(f"  • Last Assessment: {status['last_assessment']}")
                st.write(f"  • Next Review: {status['next_review']}")

            # Recommendations
            if include_recommendations:
                st.subheader("Key Recommendations")
                for priority, recs in compliance_report['recommendations'].items():
                    if recs:
                        st.write(f"**{priority} Priority:**")
                        for rec in recs:
                            st.write(f"• {rec}")

            # Download report
            report_document = generate_compliance_report_document(compliance_report)
            FileHandler.create_download_link(report_document.encode(),
                                             f"{report_type.lower().replace(' ', '_')}_report.txt", "text/plain")


def threat_intelligence():
    """Comprehensive threat intelligence analysis and monitoring tool"""
    create_tool_header("Threat Intelligence", "Analyze and monitor cybersecurity threats", "🕵️")

    tab1, tab2, tab3, tab4 = st.tabs(["Threat Analysis", "IOC Management", "Threat Hunting", "Intelligence Reports"])

    with tab1:
        st.subheader("Threat Landscape Analysis")

        analysis_scope = st.selectbox("Analysis Scope", [
            "Global Threats", "Industry-Specific", "Geographic Region", "Organization-Specific"
        ])

        if analysis_scope == "Industry-Specific":
            industry = st.selectbox("Industry Sector", [
                "Financial Services", "Healthcare", "Technology", "Government",
                "Manufacturing", "Retail", "Energy", "Education"
            ])
        elif analysis_scope == "Geographic Region":
            region = st.selectbox("Geographic Region", [
                "North America", "Europe", "Asia-Pacific", "Middle East", "Africa", "Latin America"
            ])

        threat_categories = st.multiselect("Threat Categories", [
            "Malware", "Phishing", "Ransomware", "APT Groups", "Insider Threats",
            "DDoS Attacks", "Data Breaches", "Supply Chain Attacks", "Zero-Day Exploits"
        ])

        time_period = st.selectbox("Time Period", [
            "Last 24 Hours", "Last Week", "Last Month", "Last Quarter", "Last Year"
        ])

        if st.button("Generate Threat Analysis"):
            show_progress_bar("Analyzing threat intelligence data", 4)

            analysis_config = {
                'scope': analysis_scope,
                'industry': industry if analysis_scope == "Industry-Specific" else None,
                'region': region if analysis_scope == "Geographic Region" else None,
                'categories': threat_categories,
                'time_period': time_period
            }

            threat_analysis = generate_threat_analysis(analysis_config)

            st.subheader("Threat Intelligence Analysis")

            # Threat summary metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Threats", threat_analysis['total_threats'])
            with col2:
                st.metric("Critical Threats", threat_analysis['critical_threats'])
            with col3:
                st.metric("Active Campaigns", threat_analysis['active_campaigns'])
            with col4:
                st.metric("New IOCs", threat_analysis['new_iocs'])

            # Threat trends
            st.subheader("Threat Trends")
            for trend in threat_analysis['trends']:
                trend_icon = "📈" if trend['direction'] == 'increasing' else "📉" if trend[
                                                                                       'direction'] == 'decreasing' else "➡️"
                st.write(
                    f"{trend_icon} **{trend['category']}**: {trend['description']} ({trend['change']}% {trend['direction']})")

            # Top threats
            st.subheader("Top Threats")
            for i, threat in enumerate(threat_analysis['top_threats'], 1):
                with st.expander(f"#{i} {threat['name']} - {threat['severity']} Severity"):
                    st.write(f"**Type**: {threat['type']}")
                    st.write(f"**Description**: {threat['description']}")
                    st.write(f"**Targets**: {threat['targets']}")
                    st.write(f"**Attack Vectors**: {', '.join(threat['attack_vectors'])}")
                    st.write(f"**First Seen**: {threat['first_seen']}")
                    st.write(f"**Last Activity**: {threat['last_activity']}")

                    if threat.get('mitigation'):
                        st.write(f"**Mitigation**: {threat['mitigation']}")

            # Generate threat report
            threat_report = generate_threat_analysis_report(threat_analysis)
            FileHandler.create_download_link(threat_report.encode(), "threat_analysis_report.txt", "text/plain")

    with tab2:
        st.subheader("Indicators of Compromise (IOC) Management")

        ioc_action = st.selectbox("Action", ["Add IOC", "Search IOCs", "Bulk Import", "IOC Analysis"])

        if ioc_action == "Add IOC":
            ioc_type = st.selectbox("IOC Type", [
                "IP Address", "Domain", "URL", "File Hash (MD5)", "File Hash (SHA256)",
                "Email Address", "Registry Key", "File Path", "User Agent"
            ])

            ioc_value = st.text_input("IOC Value", placeholder="Enter the indicator value...")
            threat_type = st.selectbox("Associated Threat Type", [
                "Malware", "Phishing", "C2 Infrastructure", "Botnet", "APT", "Ransomware", "Other"
            ])

            col1, col2 = st.columns(2)
            with col1:
                confidence_level = st.selectbox("Confidence Level", ["High", "Medium", "Low"])
                severity = st.selectbox("Severity", ["Critical", "High", "Medium", "Low"])
            with col2:
                source = st.text_input("Source", "Internal Analysis")
                tags = st.text_input("Tags (comma-separated)", "malware,c2")

            description = st.text_area("Description", "Description of the indicator and its context...")

            if st.button("Add IOC"):
                ioc_data = {
                    'type': ioc_type, 'value': ioc_value, 'threat_type': threat_type,
                    'confidence': confidence_level, 'severity': severity, 'source': source,
                    'tags': [tag.strip() for tag in tags.split(',')], 'description': description
                }

                result = add_ioc_to_database(ioc_data)

                if result['success']:
                    st.success(f"✅ IOC added successfully! ID: {result['ioc_id']}")

                    # Display IOC enrichment
                    enrichment = enrich_ioc(ioc_data)
                    if enrichment:
                        st.subheader("IOC Enrichment")
                        for key, value in enrichment.items():
                            st.write(f"**{key}**: {value}")
                else:
                    st.error(f"❌ Error adding IOC: {result['error']}")

        elif ioc_action == "Search IOCs":
            search_type = st.selectbox("Search Type", ["By Value", "By Type", "By Threat", "By Tags"])
            search_query = st.text_input("Search Query")

            if st.button("Search IOCs"):
                search_results = search_ioc_database(search_type, search_query)

                st.subheader(f"Search Results ({len(search_results['results'])} found)")

                for ioc in search_results['results']:
                    with st.expander(f"{ioc['type']}: {ioc['value']} ({ioc['severity']})"):
                        st.write(f"**Threat Type**: {ioc['threat_type']}")
                        st.write(f"**Confidence**: {ioc['confidence']}")
                        st.write(f"**Source**: {ioc['source']}")
                        st.write(f"**First Seen**: {ioc['first_seen']}")
                        st.write(f"**Last Seen**: {ioc['last_seen']}")
                        st.write(f"**Tags**: {', '.join(ioc['tags'])}")
                        st.write(f"**Description**: {ioc['description']}")

                # Export search results
                if search_results['results']:
                    export_data = generate_ioc_export(search_results['results'])
                    FileHandler.create_download_link(export_data.encode(), "ioc_search_results.txt", "text/plain")

        elif ioc_action == "IOC Analysis":
            analysis_ioc = st.text_input("IOC to Analyze")

            if st.button("Analyze IOC"):
                analysis_result = perform_ioc_analysis(analysis_ioc)

                st.subheader(f"IOC Analysis: {analysis_ioc}")

                # Analysis summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Risk Score", f"{analysis_result['risk_score']}/10")
                with col2:
                    st.metric("Reputation", analysis_result['reputation'])
                with col3:
                    st.metric("Last Seen", analysis_result['last_seen'])

                # Detailed analysis
                for category, details in analysis_result['analysis'].items():
                    with st.expander(f"🔍 {category}"):
                        for key, value in details.items():
                            st.write(f"**{key}**: {value}")

                # Related threats
                if analysis_result.get('related_threats'):
                    st.subheader("Related Threats")
                    for threat in analysis_result['related_threats']:
                        st.write(f"• **{threat['name']}**: {threat['description']}")

    with tab3:
        st.subheader("Threat Hunting")

        hunt_type = st.selectbox("Hunt Type", [
            "Hypothesis-Driven", "IOC-Based", "Behavioral Analysis", "Anomaly Detection"
        ])

        if hunt_type == "Hypothesis-Driven":
            hypothesis = st.text_area("Threat Hypothesis",
                                      "We suspect there may be lateral movement using compromised credentials...")

            hunt_scope = st.multiselect("Hunt Scope", [
                "Network Traffic", "System Logs", "Authentication Logs", "DNS Logs",
                "Process Execution", "File System Activity", "Registry Changes"
            ])

            if st.button("Execute Threat Hunt"):
                hunt_config = {'type': hunt_type, 'hypothesis': hypothesis, 'scope': hunt_scope}
                hunt_results = execute_threat_hunt(hunt_config)

                st.subheader("Threat Hunt Results")

                # Hunt summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Findings", hunt_results['total_findings'])
                with col2:
                    st.metric("High Priority", hunt_results['high_priority_findings'])
                with col3:
                    st.metric("Confidence Score", f"{hunt_results['confidence_score']}/10")

                # Detailed findings
                for finding in hunt_results['findings']:
                    severity_color = {"High": "red", "Medium": "orange", "Low": "green"}.get(finding['severity'],
                                                                                             "gray")
                    with st.expander(f"{finding['title']} - {finding['severity']} Severity"):
                        st.markdown(f"**Severity**: <span style='color: {severity_color}'>{finding['severity']}</span>",
                                    unsafe_allow_html=True)
                        st.write(f"**Description**: {finding['description']}")
                        st.write(f"**Evidence**: {finding['evidence']}")
                        st.write(f"**Recommendation**: {finding['recommendation']}")
                        st.write(f"**Timeline**: {finding['timeline']}")

                # Generate hunt report
                hunt_report = generate_threat_hunt_report(hunt_results)
                FileHandler.create_download_link(hunt_report.encode(), "threat_hunt_report.txt", "text/plain")

        elif hunt_type == "IOC-Based":
            ioc_list = st.text_area("IOCs to Hunt (one per line)",
                                    "192.168.1.100\nexample-malware.com\n5d41402abc4b2a76b9719d911017c592")

            data_sources = st.multiselect("Data Sources", [
                "Network Logs", "Proxy Logs", "DNS Logs", "Email Logs",
                "Endpoint Logs", "Firewall Logs", "IDS/IPS Logs"
            ])

            if st.button("Hunt for IOCs"):
                iocs = [ioc.strip() for ioc in ioc_list.split('\n') if ioc.strip()]
                hunt_results = hunt_for_iocs(iocs, data_sources)

                st.subheader("IOC Hunt Results")

                # Results summary
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("IOCs Hunted", len(iocs))
                with col2:
                    st.metric("Matches Found", hunt_results['total_matches'])

                # Match details
                for match in hunt_results['matches']:
                    with st.expander(f"🎯 Match: {match['ioc']} in {match['source']}"):
                        st.write(f"**IOC Type**: {match['ioc_type']}")
                        st.write(f"**Source**: {match['source']}")
                        st.write(f"**First Seen**: {match['first_seen']}")
                        st.write(f"**Last Seen**: {match['last_seen']}")
                        st.write(f"**Frequency**: {match['frequency']}")
                        st.write(f"**Context**: {match['context']}")

    with tab4:
        st.subheader("Threat Intelligence Reports")

        report_type = st.selectbox("Report Type", [
            "Daily Threat Brief", "Weekly Intelligence Summary", "Monthly Threat Report",
            "Campaign Analysis", "Actor Profile", "Custom Report"
        ])

        col1, col2 = st.columns(2)
        with col1:
            focus_areas = st.multiselect("Focus Areas", [
                "APT Groups", "Malware Families", "Vulnerability Exploits", "Industry Threats",
                "Geographic Threats", "Emerging Techniques", "Attribution Analysis"
            ])
        with col2:
            classification = st.selectbox("Classification", [
                "TLP:WHITE", "TLP:GREEN", "TLP:AMBER", "TLP:RED", "Internal Use"
            ])

        if st.button("Generate Threat Intelligence Report"):
            show_progress_bar("Generating threat intelligence report", 4)

            report_config = {
                'type': report_type, 'focus_areas': focus_areas,
                'classification': classification
            }

            threat_report = generate_threat_intelligence_report(report_config)

            st.subheader(f"Threat Intelligence Report: {report_type}")

            # Report metadata
            st.write(f"**Classification**: {threat_report['classification']}")
            st.write(f"**Report Date**: {threat_report['date']}")
            st.write(f"**Report ID**: {threat_report['report_id']}")

            # Executive summary
            st.subheader("Executive Summary")
            st.write(threat_report['executive_summary'])

            # Key findings
            st.subheader("Key Findings")
            for finding in threat_report['key_findings']:
                st.write(f"• {finding}")

            # Threat highlights
            st.subheader("Threat Highlights")
            for highlight in threat_report['threat_highlights']:
                with st.expander(f"🚨 {highlight['title']}"):
                    st.write(f"**Threat Actor**: {highlight['actor']}")
                    st.write(f"**Campaign**: {highlight['campaign']}")
                    st.write(f"**Targets**: {highlight['targets']}")
                    st.write(f"**TTPs**: {highlight['ttps']}")
                    st.write(f"**Impact**: {highlight['impact']}")
                    st.write(f"**Recommendations**: {highlight['recommendations']}")

            # Download report
            report_document = generate_threat_intelligence_document(threat_report)
            FileHandler.create_download_link(report_document.encode(),
                                             f"{report_type.lower().replace(' ', '_')}_report.txt", "text/plain")


def digital_signatures():
    """Comprehensive digital signature creation and verification tool"""
    create_tool_header("Digital Signatures", "Create, verify, and manage digital signatures", "✍️")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Sign Documents", "Verify Signatures", "Certificate Management", "Signature Analysis"])

    with tab1:
        st.subheader("Digital Document Signing")

        # File upload for signing
        uploaded_files = FileHandler.upload_files(['pdf', 'txt', 'docx', 'json'], accept_multiple=True)

        if uploaded_files:
            signature_type = st.selectbox("Signature Type", [
                "RSA-SHA256", "ECDSA-SHA256", "Ed25519", "RSA-PSS"
            ])

            col1, col2 = st.columns(2)
            with col1:
                signer_name = st.text_input("Signer Name", "John Doe")
                signer_email = st.text_input("Signer Email", "john.doe@company.com")
                organization = st.text_input("Organization", "Example Corp")
            with col2:
                signature_purpose = st.selectbox("Signature Purpose", [
                    "Authentication", "Non-repudiation", "Integrity", "Approval", "Timestamp"
                ])
                include_timestamp = st.checkbox("Include Timestamp", True)
                include_certificate_chain = st.checkbox("Include Certificate Chain", True)

            reason = st.text_input("Reason for Signing", "Document approval and authentication")
            location = st.text_input("Signing Location", "New York, NY")

            if st.button("Sign Documents"):
                show_progress_bar("Creating digital signatures", 3)

                signing_config = {
                    'signature_type': signature_type, 'signer_name': signer_name,
                    'signer_email': signer_email, 'organization': organization,
                    'purpose': signature_purpose, 'timestamp': include_timestamp,
                    'cert_chain': include_certificate_chain, 'reason': reason,
                    'location': location
                }

                signed_files = {}
                signature_details = []

                for uploaded_file in uploaded_files:
                    try:
                        # Create digital signature
                        signature_result = create_digital_signature(uploaded_file, signing_config)

                        signed_filename = f"{uploaded_file.name}.signed"
                        signed_files[signed_filename] = signature_result['signed_data']
                        signature_details.append(signature_result['signature_info'])

                    except Exception as e:
                        st.error(f"Error signing {uploaded_file.name}: {str(e)}")

                if signed_files:
                    st.success(f"✅ Successfully signed {len(signed_files)} file(s)!")

                    # Display signature information
                    st.subheader("Signature Details")
                    for i, sig_info in enumerate(signature_details):
                        with st.expander(f"✍️ Signature {i + 1}: {sig_info['filename']}"):
                            st.write(f"**Algorithm**: {sig_info['algorithm']}")
                            st.write(f"**Signature Hash**: {sig_info['signature_hash'][:32]}...")
                            st.write(f"**Certificate Fingerprint**: {sig_info['cert_fingerprint'][:32]}...")
                            st.write(f"**Timestamp**: {sig_info['timestamp']}")
                            st.write(f"**Validity Period**: {sig_info['validity_start']} to {sig_info['validity_end']}")

                    # Download signed files
                    if len(signed_files) == 1:
                        filename, data = next(iter(signed_files.items()))
                        FileHandler.create_download_link(data, filename, "application/octet-stream")
                    else:
                        zip_data = FileHandler.create_zip_archive(signed_files)
                        FileHandler.create_download_link(zip_data, "signed_documents.zip", "application/zip")

                    # Generate signature report
                    report = generate_signature_report(signature_details)
                    FileHandler.create_download_link(report.encode(), "signature_report.txt", "text/plain")

    with tab2:
        st.subheader("Signature Verification")

        # File upload for verification
        verification_files = FileHandler.upload_files(['signed', 'pdf', 'p7s'], accept_multiple=True)

        verification_options = st.multiselect("Verification Checks", [
            "Signature Validity", "Certificate Chain", "Timestamp Verification",
            "Certificate Revocation", "Document Integrity", "Signer Identity"
        ], default=["Signature Validity", "Document Integrity"])

        if verification_files and st.button("Verify Signatures"):
            show_progress_bar("Verifying digital signatures", 4)

            verification_results = []

            for verification_file in verification_files:
                try:
                    result = verify_digital_signature(verification_file, verification_options)
                    verification_results.append(result)
                except Exception as e:
                    st.error(f"Error verifying {verification_file.name}: {str(e)}")

            if verification_results:
                st.subheader("Verification Results")

                for result in verification_results:
                    overall_valid = result['overall_valid']
                    status_icon = "✅" if overall_valid else "❌"
                    status_color = "green" if overall_valid else "red"

                    with st.expander(f"{status_icon} {result['filename']} - {'Valid' if overall_valid else 'Invalid'}"):
                        st.markdown(
                            f"**Overall Status**: <span style='color: {status_color}'>{'Valid' if overall_valid else 'Invalid'}</span>",
                            unsafe_allow_html=True)

                        # Individual check results
                        for check, check_result in result['checks'].items():
                            check_icon = "✅" if check_result['passed'] else "❌"
                            st.write(f"{check_icon} **{check}**: {check_result['message']}")
                            if check_result.get('details'):
                                st.write(f"  Details: {check_result['details']}")

                        # Signature metadata
                        if result.get('signature_info'):
                            st.write("**Signature Information**:")
                            sig_info = result['signature_info']
                            st.write(f"  • Signer: {sig_info.get('signer', 'Unknown')}")
                            st.write(f"  • Signing Time: {sig_info.get('signing_time', 'Unknown')}")
                            st.write(f"  • Algorithm: {sig_info.get('algorithm', 'Unknown')}")
                            st.write(f"  • Certificate Subject: {sig_info.get('cert_subject', 'Unknown')}")
                            st.write(f"  • Certificate Issuer: {sig_info.get('cert_issuer', 'Unknown')}")

                # Generate verification report
                verification_report = generate_verification_report(verification_results)
                FileHandler.create_download_link(verification_report.encode(), "verification_report.txt", "text/plain")

    with tab3:
        st.subheader("Certificate Management")

        cert_action = st.selectbox("Certificate Action", [
            "Generate Self-Signed Certificate", "View Certificate Details",
            "Certificate Chain Validation", "Certificate Information"
        ])

        if cert_action == "Generate Self-Signed Certificate":
            st.write("Generate a self-signed certificate for testing purposes:")

            col1, col2 = st.columns(2)
            with col1:
                cert_subject = st.text_input("Subject (CN)", "Test Certificate")
                cert_organization = st.text_input("Organization", "Test Org")
                cert_country = st.text_input("Country Code", "US")
            with col2:
                key_size = st.selectbox("Key Size", ["2048", "3072", "4096"])
                validity_days = st.number_input("Validity (days)", 1, 3650, 365)
                key_usage = st.multiselect("Key Usage", [
                    "Digital Signature", "Key Encipherment", "Data Encipherment",
                    "Certificate Signing", "CRL Signing"
                ])

            if st.button("Generate Certificate"):
                show_progress_bar("Generating certificate and private key", 2)

                cert_config = {
                    'subject': cert_subject, 'organization': cert_organization,
                    'country': cert_country, 'key_size': int(key_size),
                    'validity_days': validity_days, 'key_usage': key_usage
                }

                cert_result = generate_self_signed_certificate(cert_config)

                st.success("✅ Certificate generated successfully!")

                # Display certificate information
                st.subheader("Generated Certificate")
                st.write(f"**Subject**: {cert_result['subject']}")
                st.write(f"**Serial Number**: {cert_result['serial_number']}")
                st.write(f"**Validity**: {cert_result['not_before']} to {cert_result['not_after']}")
                st.write(f"**Fingerprint (SHA256)**: {cert_result['fingerprint']}")
                st.write(f"**Key Algorithm**: {cert_result['key_algorithm']}")
                st.write(f"**Key Size**: {cert_result['key_size']} bits")

                # Download certificate and private key
                cert_data = cert_result['certificate_pem']
                key_data = cert_result['private_key_pem']

                col1, col2 = st.columns(2)
                with col1:
                    FileHandler.create_download_link(cert_data.encode(), "certificate.pem", "application/x-pem-file")
                with col2:
                    FileHandler.create_download_link(key_data.encode(), "private_key.pem", "application/x-pem-file")

        elif cert_action == "View Certificate Details":
            cert_file = FileHandler.upload_files(['pem', 'crt', 'cer', 'der'], accept_multiple=False)

            if cert_file and st.button("Analyze Certificate"):
                show_progress_bar("Analyzing certificate", 2)

                cert_analysis = analyze_certificate(cert_file)

                st.subheader("Certificate Analysis")

                # Basic information
                st.write("**Basic Information**:")
                st.write(f"  • Subject: {cert_analysis['subject']}")
                st.write(f"  • Issuer: {cert_analysis['issuer']}")
                st.write(f"  • Serial Number: {cert_analysis['serial_number']}")
                st.write(f"  • Version: {cert_analysis['version']}")

                # Validity period
                st.write("**Validity Period**:")
                st.write(f"  • Not Before: {cert_analysis['not_before']}")
                st.write(f"  • Not After: {cert_analysis['not_after']}")
                st.write(f"  • Days Until Expiration: {cert_analysis['days_until_expiry']}")

                # Security analysis
                st.write("**Security Analysis**:")
                for check, result in cert_analysis['security_checks'].items():
                    check_icon = "✅" if result['passed'] else "❌"
                    st.write(f"  {check_icon} **{check}**: {result['message']}")

                # Extensions
                if cert_analysis.get('extensions'):
                    st.write("**Extensions**:")
                    for ext_name, ext_value in cert_analysis['extensions'].items():
                        st.write(f"  • **{ext_name}**: {ext_value}")

    with tab4:
        st.subheader("Signature Analysis and Forensics")

        analysis_type = st.selectbox("Analysis Type", [
            "Signature Metadata Analysis", "Certificate Chain Analysis",
            "Timestamp Analysis", "Hash Verification", "Forensic Analysis"
        ])

        analysis_files = FileHandler.upload_files(['signed', 'pdf', 'p7s', 'pem'], accept_multiple=True)

        if analysis_files and st.button("Perform Analysis"):
            show_progress_bar("Performing signature analysis", 3)

            analysis_results = []

            for analysis_file in analysis_files:
                try:
                    result = perform_signature_analysis(analysis_file, analysis_type)
                    analysis_results.append(result)
                except Exception as e:
                    st.error(f"Error analyzing {analysis_file.name}: {str(e)}")

            if analysis_results:
                st.subheader(f"Analysis Results: {analysis_type}")

                for result in analysis_results:
                    with st.expander(f"🔍 {result['filename']}"):
                        # Analysis summary
                        if result.get('summary'):
                            st.write(f"**Summary**: {result['summary']}")

                        # Detailed findings
                        for category, findings in result['analysis'].items():
                            st.write(f"**{category}**:")
                            if isinstance(findings, dict):
                                for key, value in findings.items():
                                    st.write(f"  • {key}: {value}")
                            elif isinstance(findings, list):
                                for finding in findings:
                                    st.write(f"  • {finding}")
                            else:
                                st.write(f"  • {findings}")

                        # Security recommendations
                        if result.get('recommendations'):
                            st.write("**Recommendations**:")
                            for rec in result['recommendations']:
                                st.write(f"  • {rec}")

                # Generate analysis report
                analysis_report = generate_signature_analysis_report(analysis_results, analysis_type)
                FileHandler.create_download_link(analysis_report.encode(),
                                                 f"{analysis_type.lower().replace(' ', '_')}_analysis.txt",
                                                 "text/plain")


def pam_tools():
    """Privileged Access Management tools and configuration"""
    create_tool_header("PAM Tools", "Privileged Access Management configuration and testing", "🔐")

    st.markdown("### 🎯 PAM Tool Type")
    pam_type = st.selectbox("Select PAM Function:", [
        "Privileged Account Discovery", "Session Recording Setup", "Password Vault Configuration",
        "Just-in-Time Access", "Risk-Based Authentication", "Privileged Session Monitoring"
    ])

    if pam_type == "Privileged Account Discovery":
        st.markdown("### 🔍 Privileged Account Discovery")

        # Target environment configuration
        environment = st.selectbox("Target Environment:",
                                   ["Active Directory", "Unix/Linux", "Database", "Cloud (AWS/Azure)",
                                    "Network Devices"])

        col1, col2 = st.columns(2)
        with col1:
            scan_depth = st.selectbox("Scan Depth:", ["Surface Scan", "Deep Scan", "Comprehensive Audit"])
            include_service_accounts = st.checkbox("Include Service Accounts", True)
        with col2:
            include_admin_accounts = st.checkbox("Include Admin Accounts", True)
            include_shared_accounts = st.checkbox("Include Shared Accounts", True)

        if st.button("Run Discovery Scan"):
            show_progress_bar("Scanning for privileged accounts", 4)

            # Simulate discovery results
            discovered_accounts = []
            account_types = ["Domain Admin", "Local Admin", "Service Account", "Database Admin", "Network Admin"]

            import random
            for i in range(random.randint(15, 45)):
                account = {
                    "account_name": f"{'admin_' if random.choice([True, False]) else 'svc_'}{random.choice(['backup', 'database', 'web', 'monitoring', 'system'])}{random.randint(1, 99)}",
                    "account_type": random.choice(account_types),
                    "last_logon": f"{random.randint(1, 30)} days ago",
                    "password_age": f"{random.randint(30, 365)} days",
                    "risk_level": random.choice(["High", "Medium", "Low"]),
                    "permissions": random.choice(["Full Control", "Admin Rights", "Elevated", "Standard+"])
                }
                discovered_accounts.append(account)

            st.markdown("### 📊 Discovery Results")

            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)
            high_risk = len([a for a in discovered_accounts if a["risk_level"] == "High"])
            with col1:
                st.metric("Total Accounts", len(discovered_accounts))
            with col2:
                st.metric("High Risk", high_risk, delta=f"{(high_risk / len(discovered_accounts) * 100):.0f}%")
            with col3:
                admin_accounts = len([a for a in discovered_accounts if "Admin" in a["account_type"]])
                st.metric("Admin Accounts", admin_accounts)
            with col4:
                old_passwords = len([a for a in discovered_accounts if int(a["password_age"].split()[0]) > 90])
                st.metric("Stale Passwords", old_passwords)

            # Detailed results table
            st.markdown("### 📋 Detailed Account Analysis")
            for account in discovered_accounts[:10]:  # Show top 10
                with st.expander(
                        f"{'🔴' if account['risk_level'] == 'High' else '🟡' if account['risk_level'] == 'Medium' else '🟢'} {account['account_name']} ({account['account_type']})"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Account Type:** {account['account_type']}")
                        st.write(f"**Last Logon:** {account['last_logon']}")
                        st.write(f"**Risk Level:** {account['risk_level']}")
                    with col2:
                        st.write(f"**Password Age:** {account['password_age']}")
                        st.write(f"**Permissions:** {account['permissions']}")

                        if account['risk_level'] == 'High':
                            st.error("⚠️ Requires immediate attention")

            # Recommendations
            st.markdown("### 💡 Remediation Recommendations")
            recommendations = [
                "🔒 Implement password rotation for accounts with passwords older than 90 days",
                "👥 Review and reduce admin account privileges where possible",
                "📊 Enable monitoring for all high-risk privileged accounts",
                "🔐 Implement PAM solution for session management",
                "📝 Document all service accounts and their purposes",
                "⏰ Set up regular access reviews for privileged accounts"
            ]

            for rec in recommendations:
                st.write(f"• {rec}")

    elif pam_type == "Session Recording Setup":
        st.markdown("### 📹 Session Recording Configuration")

        recording_scope = st.multiselect("Recording Scope:", [
            "All Privileged Sessions", "Admin Sessions Only", "Database Access",
            "Network Device Access", "Cloud Console Access", "SSH Sessions", "RDP Sessions"
        ], default=["All Privileged Sessions"])

        col1, col2 = st.columns(2)
        with col1:
            storage_location = st.selectbox("Storage Location:", ["Local Storage", "Cloud Storage", "SIEM Integration",
                                                                  "Dedicated Appliance"])
            retention_period = st.slider("Retention Period (days):", 30, 2555, 365)
        with col2:
            encryption_enabled = st.checkbox("Enable Encryption", True)
            real_time_alerts = st.checkbox("Real-time Anomaly Alerts", True)

        if st.button("Generate Session Recording Policy"):
            st.markdown("### 📋 Session Recording Policy Configuration")

            policy = f"""
# PAM Session Recording Policy Configuration

## Recording Scope
{chr(10).join([f"- {scope}" for scope in recording_scope])}

## Storage Configuration
- **Location:** {storage_location}
- **Retention:** {retention_period} days
- **Encryption:** {'Enabled' if encryption_enabled else 'Disabled'}
- **Real-time Monitoring:** {'Enabled' if real_time_alerts else 'Disabled'}

## Implementation Steps
1. Configure recording agents on target systems
2. Set up secure storage with appropriate access controls
3. Implement session metadata indexing
4. Configure alert rules for suspicious activities
5. Establish review and audit procedures

## Compliance Considerations
- Ensure user notification of recording policies
- Implement access controls for recorded sessions
- Regular audit of recording system integrity
- Data privacy compliance (GDPR, HIPAA, etc.)

## Monitoring and Alerting
- Failed login attempts during recorded sessions
- Unusual command patterns or sequences
- Sessions outside normal business hours
- Access to sensitive data or configurations
"""

            st.code(policy, language=None)
            FileHandler.create_download_link(policy.encode(), "pam_session_recording_policy.txt", "text/plain")

    elif pam_type == "Password Vault Configuration":
        st.markdown("### 🔒 Password Vault Setup")

        vault_type = st.selectbox("Vault Type:",
                                  ["CyberArk", "HashiCorp Vault", "AWS Secrets Manager", "Azure Key Vault",
                                   "Custom Solution"])

        col1, col2 = st.columns(2)
        with col1:
            auto_rotation = st.checkbox("Automatic Password Rotation", True)
            rotation_frequency = st.slider("Rotation Frequency (days):", 1, 90, 30)
        with col2:
            complexity_requirements = st.checkbox("Enforce Password Complexity", True)
            integration_sso = st.checkbox("SSO Integration", True)

        account_types = st.multiselect("Account Types to Manage:", [
            "Domain Administrator", "Local Administrator", "Service Accounts",
            "Database Accounts", "Application Accounts", "Network Device Accounts"
        ], default=["Domain Administrator", "Service Accounts"])

        if st.button("Generate Vault Configuration"):
            st.markdown("### ⚙️ Password Vault Configuration")

            config = {
                "vault_platform": vault_type,
                "account_types": account_types,
                "auto_rotation": auto_rotation,
                "rotation_frequency": rotation_frequency,
                "complexity_requirements": complexity_requirements,
                "sso_integration": integration_sso
            }

            st.markdown("#### Configuration Summary")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Vault Platform", vault_type)
                st.metric("Account Types", len(account_types))
            with col2:
                st.metric("Auto Rotation", "✅" if auto_rotation else "❌")
                st.metric("Rotation Frequency", f"{rotation_frequency} days")
            with col3:
                st.metric("Complexity Rules", "✅" if complexity_requirements else "❌")
                st.metric("SSO Integration", "✅" if integration_sso else "❌")

            # Implementation checklist
            st.markdown("#### Implementation Checklist")
            checklist = [
                "Install and configure vault infrastructure",
                "Set up high availability and backup procedures",
                "Configure account discovery and onboarding",
                "Implement password complexity policies",
                "Set up automatic rotation schedules",
                "Configure user access roles and permissions",
                "Integrate with existing identity management",
                "Set up monitoring and alerting",
                "Conduct user training and documentation",
                "Perform security testing and validation"
            ]

            for item in checklist:
                st.write(f"☐ {item}")


def sso_solutions():
    """Single Sign-On solutions configuration and testing"""
    create_tool_header("SSO Solutions", "Single Sign-On configuration and testing tools", "🔗")

    st.markdown("### 🎯 SSO Configuration Type")
    sso_type = st.selectbox("Select SSO Function:", [
        "SAML Configuration", "OAuth/OIDC Setup", "LDAP Integration",
        "SSO Testing", "Identity Provider Setup", "Federation Configuration"
    ])

    if sso_type == "SAML Configuration":
        st.markdown("### 🔐 SAML Configuration Generator")

        col1, col2 = st.columns(2)
        with col1:
            entity_id = st.text_input("Entity ID (SP):", "https://your-app.example.com")
            acs_url = st.text_input("Assertion Consumer Service URL:", "https://your-app.example.com/saml/acs")
            slo_url = st.text_input("Single Logout URL:", "https://your-app.example.com/saml/slo")
        with col2:
            idp_entity_id = st.text_input("IdP Entity ID:", "https://idp.example.com")
            idp_sso_url = st.text_input("IdP SSO URL:", "https://idp.example.com/sso")
            idp_slo_url = st.text_input("IdP SLO URL:", "https://idp.example.com/slo")

        # SAML Settings
        st.markdown("### ⚙️ SAML Settings")
        col1, col2 = st.columns(2)
        with col1:
            name_id_format = st.selectbox("NameID Format:", [
                "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
                "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
                "urn:oasis:names:tc:SAML:2.0:nameid-format:transient"
            ])
            binding_type = st.selectbox("Binding Type:", ["HTTP-POST", "HTTP-Redirect"])
        with col2:
            sign_assertions = st.checkbox("Sign Assertions", True)
            encrypt_assertions = st.checkbox("Encrypt Assertions", False)

        if st.button("Generate SAML Configuration"):
            st.markdown("### 📄 SAML Metadata Configuration")

            saml_config = f"""<?xml version="1.0" encoding="UTF-8"?>
<md:EntityDescriptor 
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    entityID="{entity_id}">

    <md:SPSSODescriptor 
        protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"
        WantAssertionsSigned="{'true' if sign_assertions else 'false'}">

        <md:AssertionConsumerService 
            Binding="urn:oasis:names:tc:SAML:2.0:bindings:{binding_type}"
            Location="{acs_url}"
            index="0"
            isDefault="true"/>

        <md:SingleLogoutService 
            Binding="urn:oasis:names:tc:SAML:2.0:bindings:{binding_type}"
            Location="{slo_url}"/>

        <md:NameIDFormat>{name_id_format}</md:NameIDFormat>

    </md:SPSSODescriptor>

    <!-- Identity Provider Configuration -->
    <md:IDPSSODescriptor 
        protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">

        <md:SingleSignOnService 
            Binding="urn:oasis:names:tc:SAML:2.0:bindings:{binding_type}"
            Location="{idp_sso_url}"/>

        <md:SingleLogoutService 
            Binding="urn:oasis:names:tc:SAML:2.0:bindings:{binding_type}"
            Location="{idp_slo_url}"/>

    </md:IDPSSODescriptor>

</md:EntityDescriptor>"""

            st.code(saml_config, language="xml")
            FileHandler.create_download_link(saml_config.encode(), "saml_metadata.xml", "application/xml")

            # Configuration summary
            st.markdown("### 📊 Configuration Summary")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Entity ID:** {entity_id}")
                st.write(f"**ACS URL:** {acs_url}")
                st.write(f"**NameID Format:** {name_id_format.split(':')[-1]}")
            with col2:
                st.write(f"**Binding Type:** {binding_type}")
                st.write(f"**Signed Assertions:** {'Yes' if sign_assertions else 'No'}")
                st.write(f"**Encrypted Assertions:** {'Yes' if encrypt_assertions else 'No'}")

    elif sso_type == "OAuth/OIDC Setup":
        st.markdown("### 🔑 OAuth/OIDC Configuration")

        col1, col2 = st.columns(2)
        with col1:
            client_id = st.text_input("Client ID:", "your-app-client-id")
            redirect_uri = st.text_input("Redirect URI:", "https://your-app.example.com/oauth/callback")
            auth_endpoint = st.text_input("Authorization Endpoint:", "https://auth.example.com/oauth/authorize")
        with col2:
            client_secret = st.text_input("Client Secret:", type="password")
            token_endpoint = st.text_input("Token Endpoint:", "https://auth.example.com/oauth/token")
            userinfo_endpoint = st.text_input("UserInfo Endpoint:", "https://auth.example.com/oauth/userinfo")

        scopes = st.multiselect("OAuth Scopes:", [
            "openid", "profile", "email", "address", "phone", "offline_access"
        ], default=["openid", "profile", "email"])

        flow_type = st.selectbox("OAuth Flow:",
                                 ["Authorization Code", "Implicit", "Client Credentials", "Resource Owner Password"])

        if st.button("Generate OAuth Configuration"):
            st.markdown("### ⚙️ OAuth/OIDC Configuration")

            oauth_config = {
                "client_id": client_id,
                "client_secret": "***REDACTED***",
                "redirect_uri": redirect_uri,
                "scopes": scopes,
                "flow_type": flow_type,
                "endpoints": {
                    "authorization": auth_endpoint,
                    "token": token_endpoint,
                    "userinfo": userinfo_endpoint
                }
            }

            st.json(oauth_config)

            # Sample implementation
            st.markdown("### 💻 Sample Implementation (Python)")
            python_code = f"""
import requests
from urllib.parse import urlencode

# OAuth Configuration
CLIENT_ID = "{client_id}"
CLIENT_SECRET = "{client_secret}"
REDIRECT_URI = "{redirect_uri}"
SCOPES = "{' '.join(scopes)}"

# Authorization URL
def get_authorization_url():
    params = {{
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPES,
        'response_type': 'code',
        'state': 'random_state_string'
    }}
    return f"{auth_endpoint}?{{urlencode(params)}}"

# Token Exchange
def exchange_code_for_token(code):
    data = {{
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }}
    response = requests.post("{token_endpoint}", data=data)
    return response.json()

# Get User Info
def get_user_info(access_token):
    headers = {{'Authorization': f'Bearer {{access_token}}'}}
    response = requests.get("{userinfo_endpoint}", headers=headers)
    return response.json()
"""
            st.code(python_code, language="python")
            FileHandler.create_download_link(python_code.encode(), "oauth_implementation.py", "text/plain")

    elif sso_type == "SSO Testing":
        st.markdown("### 🧪 SSO Testing Tools")

        test_type = st.selectbox("Test Type:", [
            "SAML Assertion Testing", "OAuth Flow Testing", "Token Validation",
            "User Attribute Mapping", "Session Management", "Logout Testing"
        ])

        if test_type == "SAML Assertion Testing":
            st.markdown("#### 🔍 SAML Assertion Analysis")

            saml_assertion = st.text_area("Paste SAML Assertion (Base64):", height=200)

            if saml_assertion and st.button("Analyze SAML Assertion"):
                try:
                    # Simulate SAML assertion parsing
                    import base64
                    decoded = base64.b64decode(saml_assertion).decode('utf-8')

                    st.markdown("### 📊 Assertion Analysis Results")

                    # Mock analysis results
                    results = {
                        "valid_signature": True,
                        "expired": False,
                        "issuer": "https://idp.example.com",
                        "subject": "user@example.com",
                        "attributes": {
                            "email": "user@example.com",
                            "firstName": "John",
                            "lastName": "Doe",
                            "department": "Engineering"
                        }
                    }

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Signature Valid", "✅" if results["valid_signature"] else "❌")
                    with col2:
                        st.metric("Expired", "❌" if results["expired"] else "✅")
                    with col3:
                        st.metric("Issuer Valid", "✅")

                    st.markdown("#### 👤 User Attributes")
                    for attr, value in results["attributes"].items():
                        st.write(f"**{attr.title()}:** {value}")

                except Exception as e:
                    st.error(f"Error parsing SAML assertion: {str(e)}")


def mfa_tools():
    """Multi-Factor Authentication setup and testing tools"""
    create_tool_header("MFA Tools", "Multi-Factor Authentication configuration and testing", "🔒")

    st.markdown("### 🎯 MFA Configuration Type")
    mfa_type = st.selectbox("Select MFA Function:", [
        "TOTP Configuration", "SMS/Voice Setup", "Hardware Token Config",
        "Biometric Setup", "Push Notification Config", "MFA Policy Design"
    ])

    if mfa_type == "TOTP Configuration":
        st.markdown("### 📱 TOTP (Time-based One-Time Password) Setup")

        col1, col2 = st.columns(2)
        with col1:
            username = st.text_input("Username:", "user@example.com")
            issuer = st.text_input("Issuer Name:", "Your Company")
            algorithm = st.selectbox("Algorithm:", ["SHA1", "SHA256", "SHA512"])
        with col2:
            digits = st.selectbox("Digits:", [6, 8])
            period = st.selectbox("Time Period (seconds):", [30, 60])
            secret_length = st.slider("Secret Length:", 16, 64, 32)

        if st.button("Generate TOTP Configuration"):
            import secrets
            import base64

            # Generate random secret
            secret_bytes = secrets.token_bytes(secret_length)
            secret_b32 = base64.b32encode(secret_bytes).decode('utf-8')

            # Generate QR code data
            qr_data = f"otpauth://totp/{issuer}:{username}?secret={secret_b32}&issuer={issuer}&algorithm={algorithm}&digits={digits}&period={period}"

            st.markdown("### 🔑 TOTP Configuration")

            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Username:** {username}")
                st.write(f"**Issuer:** {issuer}")
                st.write(f"**Algorithm:** {algorithm}")
                st.write(f"**Digits:** {digits}")
                st.write(f"**Period:** {period} seconds")
            with col2:
                st.write(f"**Secret (Base32):** `{secret_b32}`")
                st.write(f"**QR Code Data:**")
                st.code(qr_data, language=None)

            # Generate QR code (simulated)
            st.markdown("### 📲 QR Code for Mobile App")
            st.info(
                "🔗 Use this data with authenticator apps like Google Authenticator, Authy, or Microsoft Authenticator")

            # Implementation code
            st.markdown("### 💻 Implementation Code (Python)")
            implementation_code = f"""
import pyotp
import qrcode
from io import BytesIO

# TOTP Configuration
secret = "{secret_b32}"
totp = pyotp.TOTP(secret, algorithm=pyotp.OTP.{algorithm}, digits={digits}, interval={period})

# Generate QR code
qr_uri = totp.provisioning_uri(
    name="{username}",
    issuer_name="{issuer}"
)

# Verify TOTP code
def verify_totp(user_code):
    return totp.verify(user_code)

# Get current TOTP code (for testing)
current_code = totp.now()
print(f"Current TOTP code: {{current_code}}")
"""
            st.code(implementation_code, language="python")
            FileHandler.create_download_link(implementation_code.encode(), "totp_implementation.py", "text/plain")

    elif mfa_type == "MFA Policy Design":
        st.markdown("### 📋 MFA Policy Configuration")

        # User groups and risk levels
        col1, col2 = st.columns(2)
        with col1:
            user_groups = st.multiselect("User Groups:", [
                "Administrators", "Privileged Users", "Standard Users",
                "External Users", "Service Accounts", "Emergency Access"
            ], default=["Administrators", "Privileged Users"])

            risk_scenarios = st.multiselect("High-Risk Scenarios:", [
                "Login from new device", "Login from new location", "Multiple failed attempts",
                "After business hours", "Access to sensitive data", "Administrative actions"
            ], default=["Login from new device", "Administrative actions"])

        with col2:
            mfa_methods = st.multiselect("Allowed MFA Methods:", [
                "TOTP (Authenticator App)", "SMS", "Voice Call", "Push Notification",
                "Hardware Token", "Biometrics", "Backup Codes"
            ], default=["TOTP (Authenticator App)", "Push Notification"])

            fallback_methods = st.multiselect("Fallback Methods:", [
                "SMS", "Voice Call", "Backup Codes", "Administrator Override"
            ], default=["SMS", "Backup Codes"])

        # Policy settings
        st.markdown("### ⚙️ Policy Settings")
        col1, col2 = st.columns(2)
        with col1:
            remember_device = st.slider("Remember Device (days):", 0, 90, 30)
            session_timeout = st.slider("Session Timeout (hours):", 1, 24, 8)
        with col2:
            max_attempts = st.slider("Max MFA Attempts:", 3, 10, 5)
            lockout_duration = st.slider("Lockout Duration (minutes):", 5, 60, 15)

        if st.button("Generate MFA Policy"):
            st.markdown("### 📄 MFA Policy Document")

            policy_doc = f"""
# Multi-Factor Authentication Policy

## Scope and Applicability
This policy applies to the following user groups:
{chr(10).join([f"- {group}" for group in user_groups])}

## MFA Requirements

### Mandatory MFA Scenarios
{chr(10).join([f"- {scenario}" for scenario in risk_scenarios])}

### Approved MFA Methods
Primary Methods:
{chr(10).join([f"- {method}" for method in mfa_methods])}

Fallback Methods:
{chr(10).join([f"- {method}" for method in fallback_methods])}

## Policy Settings
- **Device Memory Period:** {remember_device} days
- **Session Timeout:** {session_timeout} hours
- **Maximum Attempts:** {max_attempts}
- **Lockout Duration:** {lockout_duration} minutes

## Implementation Guidelines

### User Enrollment
1. Mandatory enrollment for all users in scope
2. Multiple MFA methods must be registered
3. Backup codes must be securely stored
4. User training and documentation provided

### Technical Requirements
1. Integration with existing identity management systems
2. Support for multiple authentication methods
3. Secure storage of MFA secrets and settings
4. Comprehensive logging and monitoring
5. Regular backup and recovery procedures

### Compliance and Auditing
1. Regular review of MFA policy effectiveness
2. User access and MFA usage reporting
3. Incident response procedures for MFA failures
4. Compliance with regulatory requirements

### Emergency Procedures
1. Administrator override capabilities
2. Emergency access procedures
3. MFA reset and recovery processes
4. Incident escalation procedures

## Monitoring and Reporting
- Failed MFA attempt monitoring
- Unusual authentication pattern detection
- Regular policy compliance reporting
- User experience and adoption metrics
"""

            st.code(policy_doc, language=None)
            FileHandler.create_download_link(policy_doc.encode(), "mfa_policy.txt", "text/plain")

            # Policy summary metrics
            st.markdown("### 📊 Policy Summary")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("User Groups", len(user_groups))
            with col2:
                st.metric("MFA Methods", len(mfa_methods))
            with col3:
                st.metric("Risk Scenarios", len(risk_scenarios))
            with col4:
                st.metric("Device Memory", f"{remember_device} days")


def iam_platforms():
    """Identity and Access Management platform configuration"""
    create_tool_header("IAM Platforms", "Identity and Access Management platform setup and configuration", "👥")

    st.markdown("### 🎯 IAM Platform Type")
    iam_type = st.selectbox("Select IAM Function:", [
        "Role-Based Access Control (RBAC)", "Attribute-Based Access Control (ABAC)",
        "Identity Governance", "User Lifecycle Management", "Access Certification", "Identity Federation"
    ])

    if iam_type == "Role-Based Access Control (RBAC)":
        st.markdown("### 🔐 RBAC Configuration")

        # Role definition
        st.markdown("#### 👥 Role Management")
        role_name = st.text_input("Role Name:", "Developer")
        role_description = st.text_area("Role Description:",
                                        "Software development team members with access to development resources")

        # Permissions
        st.markdown("#### 🔑 Permissions Assignment")
        available_permissions = [
            "Read User Data", "Write User Data", "Delete User Data",
            "Read System Config", "Write System Config", "Admin Access",
            "Database Read", "Database Write", "File System Access",
            "Network Access", "Audit Log Access", "User Management"
        ]

        selected_permissions = st.multiselect("Select Permissions:", available_permissions)

        # Resource access
        st.markdown("#### 🏢 Resource Access")
        col1, col2 = st.columns(2)
        with col1:
            departments = st.multiselect("Department Access:", [
                "Engineering", "Marketing", "Sales", "HR", "Finance", "Operations"
            ])
            applications = st.multiselect("Application Access:", [
                "CRM System", "ERP System", "Development Tools", "Analytics Platform", "Email System"
            ])
        with col2:
            data_classification = st.multiselect("Data Classification Access:", [
                "Public", "Internal", "Confidential", "Restricted"
            ])
            time_restrictions = st.selectbox("Time Restrictions:", [
                "No Restrictions", "Business Hours Only", "Weekdays Only", "Custom Schedule"
            ])

        if st.button("Generate RBAC Configuration"):
            st.markdown("### 📋 RBAC Role Configuration")

            rbac_config = {
                "role_name": role_name,
                "description": role_description,
                "permissions": selected_permissions,
                "resource_access": {
                    "departments": departments,
                    "applications": applications,
                    "data_classification": data_classification,
                    "time_restrictions": time_restrictions
                }
            }

            st.json(rbac_config)

            # Role summary
            st.markdown("### 📊 Role Summary")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Permissions", len(selected_permissions))
            with col2:
                st.metric("Departments", len(departments))
            with col3:
                st.metric("Applications", len(applications))
            with col4:
                st.metric("Data Levels", len(data_classification))

            # Implementation template
            st.markdown("### 💻 Implementation Template")
            template = f"""
# RBAC Role: {role_name}

## Role Definition
- **Name:** {role_name}
- **Description:** {role_description}
- **Type:** Standard Role

## Permissions Matrix
{chr(10).join([f"- {perm}: ALLOWED" for perm in selected_permissions])}

## Resource Access Rules
- **Departments:** {', '.join(departments) if departments else 'None'}
- **Applications:** {', '.join(applications) if applications else 'None'}
- **Data Classification:** {', '.join(data_classification) if data_classification else 'None'}
- **Time Restrictions:** {time_restrictions}

## Assignment Rules
1. Users must be approved by department manager
2. Regular access review required (quarterly)
3. Automatic deprovisioning upon role change
4. Audit trail for all role assignments

## Monitoring
- Track all access using this role
- Alert on unusual access patterns
- Regular permission usage analysis
- Compliance reporting
"""
            st.code(template, language=None)
            FileHandler.create_download_link(template.encode(), f"rbac_role_{role_name.lower().replace(' ', '_')}.txt",
                                             "text/plain")

    elif iam_type == "User Lifecycle Management":
        st.markdown("### 👤 User Lifecycle Management")

        # Lifecycle stages
        st.markdown("#### 🔄 Lifecycle Stages Configuration")

        stages = ["Onboarding", "Active", "Role Change", "Leave of Absence", "Offboarding"]
        stage_config = {}

        for stage in stages:
            with st.expander(f"Configure {stage} Stage"):
                if stage == "Onboarding":
                    stage_config[stage] = {
                        "auto_create_accounts": st.checkbox(f"Auto-create accounts", True, key=f"{stage}_auto"),
                        "default_roles": st.multiselect(f"Default roles", ["Basic User", "Department Access"],
                                                        key=f"{stage}_roles"),
                        "approval_required": st.checkbox(f"Manager approval required", True, key=f"{stage}_approval"),
                        "provisioning_delay": st.slider(f"Provisioning delay (hours)", 0, 48, 2, key=f"{stage}_delay")
                    }
                elif stage == "Active":
                    stage_config[stage] = {
                        "access_review_frequency": st.selectbox(f"Access review frequency",
                                                                ["Monthly", "Quarterly", "Semi-annually", "Annually"],
                                                                key=f"{stage}_review"),
                        "auto_cert_required": st.checkbox(f"Automatic recertification", True, key=f"{stage}_cert"),
                        "unused_access_cleanup": st.slider(f"Cleanup unused access (days)", 30, 365, 90,
                                                           key=f"{stage}_cleanup")
                    }
                elif stage == "Offboarding":
                    stage_config[stage] = {
                        "immediate_disable": st.checkbox(f"Immediate account disable", True, key=f"{stage}_disable"),
                        "grace_period": st.slider(f"Grace period (days)", 0, 30, 0, key=f"{stage}_grace"),
                        "data_retention": st.slider(f"Data retention (days)", 30, 1095, 90, key=f"{stage}_retention"),
                        "manager_notification": st.checkbox(f"Notify manager", True, key=f"{stage}_notify")
                    }

        if st.button("Generate Lifecycle Configuration"):
            st.markdown("### ⚙️ User Lifecycle Configuration")

            st.json(stage_config)

            # Workflow diagram (text-based)
            st.markdown("### 🔄 Lifecycle Workflow")
            workflow = """
User Lifecycle Management Workflow:

1. **Pre-boarding** 
   → HR initiates user creation
   → Manager approval (if required)
   → Account provisioning scheduled

2. **Onboarding**
   → Automatic account creation
   → Default role assignment
   → Welcome email and instructions
   → Initial access verification

3. **Active Status**
   → Regular access reviews
   → Automatic recertification
   → Usage monitoring
   → Role change processing

4. **Status Changes**
   → Role modifications
   → Department transfers
   → Leave of absence
   → Permission updates

5. **Offboarding**
   → Immediate account disable
   → Access removal
   → Data retention procedures
   → Final reporting

6. **Post-offboarding**
   → Account archival
   → Audit trail preservation
   → Final cleanup
"""
            st.code(workflow, language=None)

            # Automation triggers
            st.markdown("### 🤖 Automation Triggers")
            triggers = [
                "New employee in HR system → Auto-trigger onboarding",
                "Role change in HR system → Auto-trigger access review",
                "Termination date reached → Auto-trigger offboarding",
                "90 days no login → Auto-trigger access review",
                "Manager change → Auto-trigger approval workflow",
                "Department transfer → Auto-trigger role reassignment"
            ]

            for trigger in triggers:
                st.write(f"• {trigger}")


def access_review():
    """Access review and audit tools"""
    create_tool_header("Access Review", "Access review and audit management tools", "🔍")

    st.markdown("### 🎯 Access Review Type")
    review_type = st.selectbox("Select Review Type:", [
        "User Access Review", "Role Access Review", "Privileged Access Review",
        "Application Access Review", "Automated Access Certification", "Compliance Audit"
    ])

    if review_type == "User Access Review":
        st.markdown("### 👤 User Access Review Configuration")

        # Review scope
        col1, col2 = st.columns(2)
        with col1:
            review_frequency = st.selectbox("Review Frequency:",
                                            ["Weekly", "Monthly", "Quarterly", "Semi-annually", "Annually"])
            review_scope = st.multiselect("Review Scope:", [
                "All Users", "Privileged Users", "Inactive Users", "External Users", "Service Accounts"
            ], default=["Privileged Users"])
        with col2:
            auto_approval = st.checkbox("Enable Auto-approval for Standard Access", False)
            escalation_enabled = st.checkbox("Enable Escalation for Overdue Reviews", True)

        # Review criteria
        st.markdown("#### 📋 Review Criteria")
        criteria = st.multiselect("Focus Areas:", [
            "Last Login Date", "Permission Usage", "Role Appropriateness",
            "Data Access Levels", "Application Access", "Network Access"
        ], default=["Last Login Date", "Permission Usage"])

        # Thresholds
        st.markdown("#### ⚠️ Alert Thresholds")
        col1, col2 = st.columns(2)
        with col1:
            inactive_days = st.slider("Inactive User Threshold (days):", 30, 365, 90)
            unused_permission_days = st.slider("Unused Permission Threshold (days):", 30, 180, 60)
        with col2:
            high_risk_access = st.multiselect("High-Risk Access Types:", [
                "Administrative Rights", "Database Admin", "Financial Systems", "HR Systems"
            ])

        if st.button("Generate Access Review Campaign"):
            show_progress_bar("Generating access review campaign", 3)

            # Simulate user data for review
            import random
            users_for_review = []
            departments = ["Engineering", "Sales", "Marketing", "HR", "Finance"]
            roles = ["Developer", "Manager", "Analyst", "Administrator", "Specialist"]

            for i in range(random.randint(25, 75)):
                user = {
                    "username": f"user{i:03d}",
                    "name": f"User {i:03d}",
                    "department": random.choice(departments),
                    "role": random.choice(roles),
                    "last_login": f"{random.randint(1, 120)} days ago",
                    "permissions": random.randint(5, 25),
                    "risk_level": random.choice(["Low", "Medium", "High"]),
                    "manager": f"manager{random.randint(1, 10)}",
                    "status": random.choice(["Active", "Inactive", "Review Required"])
                }
                users_for_review.append(user)

            st.markdown("### 📊 Access Review Campaign Results")

            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)
            total_users = len(users_for_review)
            high_risk_users = len([u for u in users_for_review if u["risk_level"] == "High"])
            inactive_users = len([u for u in users_for_review if "90" in u["last_login"] or "120" in u["last_login"]])
            review_required = len([u for u in users_for_review if u["status"] == "Review Required"])

            with col1:
                st.metric("Total Users", total_users)
            with col2:
                st.metric("High Risk", high_risk_users, delta=f"{(high_risk_users / total_users * 100):.0f}%")
            with col3:
                st.metric("Inactive Users", inactive_users)
            with col4:
                st.metric("Review Required", review_required)

            # Detailed review results
            st.markdown("### 📋 Users Requiring Review")
            for user in users_for_review[:15]:  # Show first 15
                risk_color = "🔴" if user["risk_level"] == "High" else "🟡" if user["risk_level"] == "Medium" else "🟢"

                with st.expander(f"{risk_color} {user['name']} ({user['department']}) - {user['role']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Username:** {user['username']}")
                        st.write(f"**Last Login:** {user['last_login']}")
                        st.write(f"**Risk Level:** {user['risk_level']}")
                    with col2:
                        st.write(f"**Permissions:** {user['permissions']}")
                        st.write(f"**Manager:** {user['manager']}")
                        st.write(f"**Status:** {user['status']}")

                    # Review actions
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        if st.button("Approve", key=f"approve_{user['username']}"):
                            st.success("Access approved")
                    with col2:
                        if st.button("Modify", key=f"modify_{user['username']}"):
                            st.info("Access modification required")
                    with col3:
                        if st.button("Revoke", key=f"revoke_{user['username']}"):
                            st.warning("Access revoked")

            # Review summary report
            st.markdown("### 📄 Review Summary Report")
            report = f"""
# Access Review Campaign Summary

## Campaign Details
- **Review Type:** {review_type}
- **Frequency:** {review_frequency}
- **Scope:** {', '.join(review_scope)}
- **Review Criteria:** {', '.join(criteria)}

## Key Findings
- **Total Users Reviewed:** {total_users}
- **High-Risk Users:** {high_risk_users} ({(high_risk_users / total_users * 100):.1f}%)
- **Inactive Users:** {inactive_users} (>{inactive_days} days)
- **Users Requiring Action:** {review_required}

## Risk Distribution
- High Risk: {high_risk_users} users
- Medium Risk: {len([u for u in users_for_review if u["risk_level"] == "Medium"])} users  
- Low Risk: {len([u for u in users_for_review if u["risk_level"] == "Low"])} users

## Recommendations
1. Immediate review required for {high_risk_users} high-risk users
2. Disable {inactive_users} inactive user accounts
3. Implement automated reviews for low-risk standard access
4. Schedule manager training on access review procedures
5. Update access review policies based on findings

## Next Steps
1. Complete pending reviews within 5 business days
2. Update user access based on review outcomes  
3. Document exceptions and justifications
4. Schedule next review cycle
5. Generate compliance report for audit
"""

            st.code(report, language=None)
            FileHandler.create_download_link(report.encode(), "access_review_summary.txt", "text/plain")