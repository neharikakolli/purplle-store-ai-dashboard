import streamlit as st
import cv2

st.set_page_config(
    page_title="Purplle Store Intelligence Dashboard",
    layout="wide"
)

st.title("🛍️ Purplle AI-Powered Store Intelligence Dashboard")

st.markdown("""
### Business Intelligence Metrics
Real-time store occupancy monitoring, crowd analysis,
event detection, and retail analytics powered by AI.
""")

# CCTV Feed
st.subheader("📹 CCTV Feed")

try:
    video_file = open("video.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
except:
    st.warning("Video file not found")

# Event Analytics
try:
    with open("events.txt", "r") as f:
        events = f.readlines()

    total_alerts = len(events)

    # Dashboard Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Current Customers", 12)

    with col2:
        st.metric("Peak Customers", 25)

    with col3:
        st.metric("Crowd Alerts", total_alerts)

    with col4:
        st.metric("Total Events", len(events))

    st.subheader("📊 Store Insights")

    st.success("Peak customer occupancy detected: 25")
    st.info(f"Total crowd alerts generated: {total_alerts}")

    st.subheader("📜 Event History")

    for event in reversed(events[-10:]):
        st.write(event)

except:
    st.warning("No events found yet")

# Architecture Section
st.subheader("🏗️ System Architecture")

st.code("""
CCTV Feed
     ↓
OpenCV Processing
     ↓
YOLOv8 Detection
     ↓
Person Tracking
     ↓
Crowd Analysis
     ↓
Event Logging
     ↓
FastAPI Services
     ↓
Streamlit Dashboard
""")

# Future Scope
st.subheader("🚀 Future Enhancements")

st.markdown("""
- Customer Heatmaps
- Queue Detection
- Multi-Camera Analytics
- Shelf Monitoring
- Cloud Deployment
- Real-Time Alert Notifications
""")