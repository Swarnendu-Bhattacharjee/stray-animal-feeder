# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import csv
import os

app = FastAPI()

DATA_FOLDER = "data"
LOG_FILE = os.path.join(DATA_FOLDER, "logs.csv")
SCHEDULE_FILE = os.path.join(DATA_FOLDER, "feeding_schedule.csv")

os.makedirs(DATA_FOLDER, exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp","animal_type","location","food_dispensed","alert_sent"])
if not os.path.exists(SCHEDULE_FILE):
    with open(SCHEDULE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["schedule_id","time","location","food_type","quantity"])

# Models
class FeedRequest(BaseModel):
    location: str
    food_type: str
    quantity: int

class ScheduleRequest(BaseModel):
    time: str
    location: str
    food_type: str
    quantity: int

# Dummy robot status
robot_status = {
    "robot_status": "idle",
    "battery_level": 87,
    "location": "Zone A"
}

@app.get("/status")
def get_status():
    return robot_status

@app.post("/feed")
def feed_animal(request: FeedRequest):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # For demo: random alert if animal_type == 'Injured Cat'
    alert_sent = request.location == "Zone B"  # dummy condition
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, "Dog", request.location, request.quantity, alert_sent])
    return {"status": "success", "message": f"Feeding initiated at {request.location}"}

@app.get("/logs")
def get_logs():
    with open(LOG_FILE, "r") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

@app.post("/schedule")
def add_schedule(request: ScheduleRequest):
    schedule_id = 1
    with open(SCHEDULE_FILE, "r") as f:
        lines = f.readlines()
        if len(lines) > 1:
            schedule_id = int(lines[-1].split(",")[0]) + 1
    with open(SCHEDULE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([schedule_id, request.time, request.location, request.food_type, request.quantity])
    return {"status": "success", "message": f"Schedule added successfully with id {schedule_id}"}
