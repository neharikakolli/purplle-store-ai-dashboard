import streamlit as st
import cv2

st.set_page_config(page_title="Purplle Dashboard", layout="wide")

st.title("🛍️ Purplle Store Intelligence Dashboard")

video_file = open("video.mp4", "rb")
video_bytes = video_file.read()

st.subheader("CCTV Feed")
st.video(video_bytes)

try:
    with open("events.txt", "r") as f:
        events = f.readlines()

    total_alerts = len(events)
    latest_event = events[-1] if events else "No events"

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Crowd Alerts", total_alerts)

    with col2:
        st.metric("Latest Event", latest_event)

    st.subheader("Event History")

    for event in reversed(events[-10:]):
        st.write(event)

except:
    st.warning("No events found yet")