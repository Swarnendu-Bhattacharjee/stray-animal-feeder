# src/cv_module.py
import cv2
from utils import log_event

class CVModule:
    """
    Computer Vision module for detecting stray/injured animals.
    - Can connect to live CCTV or camera feed.
    - Currently simulates detection.
    """
    def __init__(self, model_path=None):
        self.model_path = model_path
        self.detected_animals = []
        log_event(f"CVModule initialized with model_path: {self.model_path}")

    def analyze_frame(self, frame):
        """
        Analyze a single video frame.
        Placeholder for integrating object detection models like YOLO or Faster R-CNN.
        """
        log_event("Analyzing frame for stray animals.")
        # Dummy detection
        detected = ["Stray Dog"] if frame is not None else []
        self.detected_animals.extend(detected)
        return detected

    def get_detected_animals(self):
        """
        Returns list of all detected animals in session.
        """
        return self.detected_animals
