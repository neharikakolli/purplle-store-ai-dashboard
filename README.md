## API Endpoints

GET /
Returns API status

GET /analytics
Returns current people count, alerts and peak crowd.

GET /health
Returns system health status.

## Business Insights

- Occupancy Monitoring
- Crowd Alerts
- Peak Crowd Detection
- Store Traffic Analytics

## Production Readiness

- Modular Architecture
- REST API Support
- Event Logging
- Scalable Design
## Engineering Decisions

- YOLOv8 chosen for fast and accurate person detection.
- OpenCV used for real-time video processing.
- FastAPI used for lightweight API services.
- Streamlit used for rapid dashboard development.
## Event Schema

{
  "timestamp": "2026-06-04T19:30:00",
  "event_type": "crowd_alert",
  "people_count": 12,
  "camera_id": "cam_01"
}
## System Architecture

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
## Future Enhancements

- Customer Heatmaps
- Queue Detection
- Multi-Camera Analytics
- Shelf Monitoring
- Cloud Deployment
- Real-Time Notifications