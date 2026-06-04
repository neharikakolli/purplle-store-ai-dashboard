from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Purplle Store Intelligence API Running"}

@app.get("/analytics")
def analytics():
    return {
        "current_people": 4,
        "total_alerts": 62,
        "peak_crowd": 6,
        "camera_status": "Active"
    }

@app.get("/health")
def health():
    return {"status": "running"}