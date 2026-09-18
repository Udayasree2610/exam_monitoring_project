import streamlit as st
import pandas as pd
import sqlite3
import json
import os
from analytics import calculate_integrity_scores, generate_analytics_visualizations

# Streamlit Page Configuration
st.set_page_config(
    page_title="ExamGuard Integrity Analytics",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Online Exam Monitoring & Integrity Analytics Dashboard")
st.markdown("---")

# Load Analytics and Clustering Data
@st.cache_data
def load_analytics():
    df_scores = calculate_integrity_scores()
    generate_analytics_visualizations()
    return df_scores

df_candidates = load_analytics()

# Sidebar Filters & Navigation
st.sidebar.header("📊 Dashboard Navigation")
option = st.sidebar.selectbox(
    "Choose View:", 
    ["Overview & Metrics", "Candidates Risk & Clusters", "Violation Logs", "Export Data Module"]
)

if option == "Overview & Metrics":
    st.subheader("📈 Live Session Overview & Data Science Visualizations")
    
    col1, col2, col3 = st.columns(3)
    total_candidates = len(df_candidates)
    high_risk_count = len(df_candidates[df_candidates['risk_label'] == 'High Risk']) if not df_candidates.empty else 0
    avg_score = int(df_candidates['integrity_score'].mean()) if not df_candidates.empty else 0

    col1.metric("Total Candidates Monitored", total_candidates)
    col2.metric("High Risk Violators", high_risk_count, delta_color="inverse")
    col3.metric("Average Integrity Score", f"{avg_score} / 100")
    
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Score Distribution")
        if os.path.exists("static/plots/score_distribution.png"):
            st.image("static/plots/score_distribution.png", use_container_width=True)
        else:
            st.info("Distribution plot not generated yet.")
            
    with c2:
        st.markdown("### Event Heatmap Matrix")
        if os.path.exists("static/plots/event_heatmap.png"):
            st.image("static/plots/event_heatmap.png", use_container_width=True)
        else:
            st.info("Heatmap plot not generated yet.")

elif option == "Candidates Risk & Clusters":
    st.subheader("👥 Candidates Risk Analysis & Machine Learning Clusters")
    if not df_candidates.empty:
        st.dataframe(df_candidates, use_container_width=True)
    else:
        st.warning("No candidate records found in database.")

elif option == "Violation Logs":
    st.subheader("🚨 Real-Time Proctoring Violation Logs")
    conn = sqlite3.connect("exam_monitor.db")
    logs_df = pd.read_sql_query("""
        SELECT s.username, e.event_type, e.timestamp 
        FROM event_logs e 
        JOIN sessions s ON e.session_id = s.session_id
    """, conn)
    conn.close()
    
    if not logs_df.empty:
        st.dataframe(logs_df, use_container_width=True)
    else:
        st.info("No violation logs recorded.")

elif option == "Export Data Module":
    st.subheader("📥 Export Session Logs, Scores & Cluster Assignments")
    st.markdown("Download candidate audit reports, risk profiles, and clustering metrics in standard formats.")
    
    if not df_candidates.empty:
        # CSV Export
        csv_data = df_candidates.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Complete Candidate Analytics (CSV)",
            data=csv_data,
            file_name="exam_integrity_analytics.csv",
            mime="text/csv"
        )
        
        # JSON Export
        json_data = df_candidates.to_json(orient='records', indent=4)
        st.download_button(
            label="Download Complete Candidate Analytics (JSON)",
            data=json_data,
            file_name="exam_integrity_analytics.json",
            mime="application/json"
        )
    else:
        st.warning("No data available for export.")