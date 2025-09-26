# src/feeder_robot.py
from utils import log_event

class FeederRobot:
    """
    Core class for the Stray Animal Feeder Robot
    Handles:
    - Food dispensing
    - Status tracking
    - Simulated actuator controls
    """
    def __init__(self):
        self.status = "Idle"
        self.total_food_dispensed = 0
        log_event("FeederRobot initialized and idle.")

    def dispense_food(self, amount: int):
        """
        Dispense the specified amount of food.
        Placeholder for motor control logic.
        """
        log_event(f"Dispensing {amount} units of food.")
        self.total_food_dispensed += amount
        self.status = f"Dispensed {amount} units"
        return self.status

    def get_status(self):
        """
        Returns current robot status.
        """
        log_event(f"Status requested: {self.status}")
        return self.status

    def shutdown(self):
        """
        Simulates robot shutdown.
        """
        self.status = "Offline"
        log_event("FeederRobot has been shutdown.")
        return self.status
