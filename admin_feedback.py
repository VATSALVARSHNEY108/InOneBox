import streamlit as st
import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime, timedelta


def display_admin_feedback_page():
    """Display admin page for viewing and managing user feedback"""

    st.title("🔧 Admin: User Feedback Management")
    st.markdown("---")

    # Admin authentication (simple for demo purposes)
    if 'admin_authenticated' not in st.session_state:
        st.session_state.admin_authenticated = False

    if not st.session_state.admin_authenticated:
        st.warning("🔐 Admin Access Required")
        admin_password = st.text_input("Enter Admin Password:", type="password")
        if st.button("🔓 Login"):
            # Simple password check (in production, use proper authentication)
            admin_secret = os.getenv('ADMIN_PASSWORD')
            if not admin_secret:
                st.error("❌ Admin password not configured. Please set ADMIN_PASSWORD environment variable.")
                return
            if admin_password == admin_secret:
                st.session_state.admin_authenticated = True
                st.success("✅ Admin access granted!")
                st.rerun()
            else:
                st.error("❌ Invalid password!")
        return

    # Admin is authenticated, show feedback management
    st.success("🔓 Logged in as Admin")

    # Logout button
    if st.button("🚪 Logout"):
        st.session_state.admin_authenticated = False
        st.rerun()

    st.markdown("---")

    # Fetch feedback data
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Get all feedback
        cursor.execute("""
            SELECT * FROM user_feedback 
            ORDER BY submitted_at DESC
        """)
        feedback_data = cursor.fetchall()

        # Get statistics
        cursor.execute("SELECT COUNT(*) as total_feedback FROM user_feedback")
        total_feedback = cursor.fetchone()['total_feedback']

        cursor.execute("""
            SELECT COUNT(*) as new_feedback 
            FROM user_feedback 
            WHERE status = 'new'
        """)
        new_feedback = cursor.fetchone()['new_feedback']

        cursor.execute("""
            SELECT COUNT(*) as today_feedback 
            FROM user_feedback 
            WHERE DATE(submitted_at) = CURRENT_DATE
        """)
        today_feedback = cursor.fetchone()['today_feedback']

        cursor.close()
        conn.close()

    except Exception as e:
        st.error(f"❌ Error fetching feedback data: {e}")
        return

    # Display statistics
    st.subheader("📊 Feedback Statistics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Feedback", total_feedback)
    with col2:
        st.metric("New/Unread", new_feedback)
    with col3:
        st.metric("Today", today_feedback)
    with col4:
        st.metric("This Week", len([f for f in feedback_data if
                                    datetime.fromisoformat(str(f['submitted_at'])) > datetime.now() - timedelta(
                                        days=7)]))

    st.markdown("---")

    # Filters and Search
    st.subheader("🔍 Filter & Search Feedback")

    # Search input
    search_query = st.text_input("🔍 Search in subject and message:", placeholder="Type keywords to search...")

    col1, col2, col3 = st.columns(3)

    with col1:
        feedback_types = ["All"] + list(set([f['feedback_type'] for f in feedback_data]))
        selected_type = st.selectbox("Feedback Type:", feedback_types)

    with col2:
        status_options = ["All", "new", "reviewed", "responded"]
        selected_status = st.selectbox("Status:", status_options)

    with col3:
        date_filter = st.selectbox("Date Range:", [
            "All Time", "Today", "Last 7 Days", "Last 30 Days"
        ])

    # Apply filters and search
    filtered_feedback = feedback_data

    # Apply search filter
    if search_query:
        search_lower = search_query.lower()
        filtered_feedback = [f for f in filtered_feedback
                             if search_lower in f['subject'].lower() or search_lower in f['message'].lower()]

    # Apply type filter
    if selected_type != "All":
        filtered_feedback = [f for f in filtered_feedback if f['feedback_type'] == selected_type]

    # Apply status filter
    if selected_status != "All":
        filtered_feedback = [f for f in filtered_feedback if f['status'] == selected_status]

    # Apply date filter
    if date_filter == "Today":
        filtered_feedback = [f for f in filtered_feedback if
                             datetime.fromisoformat(str(f['submitted_at'])).date() == datetime.now().date()]
    elif date_filter == "Last 7 Days":
        filtered_feedback = [f for f in filtered_feedback if
                             datetime.fromisoformat(str(f['submitted_at'])) > datetime.now() - timedelta(days=7)]
    elif date_filter == "Last 30 Days":
        filtered_feedback = [f for f in filtered_feedback if
                             datetime.fromisoformat(str(f['submitted_at'])) > datetime.now() - timedelta(days=30)]

    st.markdown("---")

    # Display feedback
    st.subheader(f"💬 Feedback Items ({len(filtered_feedback)} items)")

    if not filtered_feedback:
        st.info("📭 No feedback items match your filters.")
        return

    # Display each feedback item
    for i, feedback in enumerate(filtered_feedback):
        with st.expander(
                f"#{feedback['id']} - {feedback['feedback_type']} - {feedback['subject'][:50]}{'...' if len(feedback['subject']) > 50 else ''}"):

            # Basic info
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Type:** {feedback['feedback_type']}")
                st.write(f"**Status:** {feedback['status']}")
                st.write(f"**Submitted:** {feedback['submitted_at']}")

            with col2:
                st.write(f"**Name:** {feedback['name'] or 'Anonymous'}")
                st.write(f"**Email:** {feedback['email'] or 'Not provided'}")
                st.write(f"**ID:** {feedback['id']}")

            # Subject and Message
            st.write(f"**Subject:** {feedback['subject']}")
            st.text_area("Message:", feedback['message'], height=100, disabled=True, key=f"msg_{feedback['id']}")

            # Action buttons
            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button(f"Mark as Reviewed", key=f"review_{feedback['id']}"):
                    update_feedback_status(feedback['id'], 'reviewed')
                    st.success("✅ Marked as reviewed!")
                    st.rerun()

            with col2:
                if st.button(f"Mark as Responded", key=f"respond_{feedback['id']}"):
                    update_feedback_status(feedback['id'], 'responded')
                    st.success("✅ Marked as responded!")
                    st.rerun()

            with col3:
                if st.button(f"Mark as New", key=f"new_{feedback['id']}"):
                    update_feedback_status(feedback['id'], 'new')
                    st.success("✅ Marked as new!")
                    st.rerun()

    st.markdown("---")

    # Export functionality
    st.subheader("📤 Export Data")
    if st.button("📊 Export to CSV"):
        # Convert to DataFrame
        df = pd.DataFrame(filtered_feedback)
        csv = df.to_csv(index=False)
        st.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name=f"feedback_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        st.success("✅ CSV ready for download!")


def update_feedback_status(feedback_id: int, new_status: str):
    """Update the status of a feedback item"""
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE user_feedback SET status = %s WHERE id = %s",
            (new_status, feedback_id)
        )

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        st.error(f"Error updating feedback status: {e}")


def get_feedback_summary():
    """Get a summary of feedback for dashboard display"""
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Get basic counts
        cursor.execute("SELECT COUNT(*) as total FROM user_feedback")
        total = cursor.fetchone()['total']

        cursor.execute("SELECT COUNT(*) as new FROM user_feedback WHERE status = 'new'")
        new = cursor.fetchone()['new']

        cursor.close()
        conn.close()

        return {'total': total, 'new': new}

    except Exception as e:
        return {'total': 0, 'new': 0, 'error': str(e)}