## API Endpoints

### GET /

Returns API status and service availability.

### GET /analytics

Returns real-time people count, crowd alerts, and peak occupancy metrics.

### GET /health

Returns system health and operational status.

## Business Insights

* Occupancy Monitoring
* Crowd Alert Detection
* Peak Crowd Analysis
* Store Traffic Analytics

## Production Readiness

* Modular Architecture
* REST API Support
* Event Logging
* Scalable Design

## Engineering Decisions

* YOLOv8 selected for accurate real-time person detection.
* OpenCV used for efficient video frame processing.
* FastAPI implemented for lightweight and scalable REST APIs.
* Streamlit chosen for rapid dashboard development and visualization.

## Event Schema

```json
{
  "timestamp": "2026-06-04T19:30:00",
  "event_type": "crowd_alert",
  "people_count": 12,
  "camera_id": "cam_01"
}
```

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

* Customer Heatmaps
* Queue Detection
* Multi-Camera Analytics
* Shelf Monitoring
* Cloud Deployment
* Real-Time Notifications
