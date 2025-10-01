# ⚙️ Hardware Directory – StrayMate Robotic Feeder

Welcome to the **Hardware** directory of **StrayMate**, the intelligent stray animal assistance system.  
This folder contains all the physical and electronic components of the robotic feeder, including **firmware, sensor configurations, assembly instructions, and datasheets**.

---

## 📂 Directory Overview

| Folder / File | Type | Description |
|---------------|------|-------------|
| `firmware/` | 💻 Code | Microcontroller (Arduino/Raspberry Pi) code and control scripts for motors, servos, and sensors. |
| `sensors/` | 🧪 Config | Sensor calibration and configuration files (ultrasonic, load cells, etc.) and test scripts. |
| `assembly/` | 🏗️ Guide | Step-by-step assembly instructions, exploded diagrams, and assembly photos. |
| `datasheets/` | 📚 Reference | Datasheets for all electronic components (motors, servos, sensors). |
| `README.md` | 📘 Documentation | You are here — this document explains all hardware components and structure. |

---

## 📁 1. Firmware – `firmware/`

Includes all microcontroller and control code:

**Examples:**
- `feeder_arduino.ino` – main Arduino firmware controlling motors, servos, and sensors  
- `motor_control.py` – Python script to control motor speed via Raspberry Pi  
- `servo_control.py` – Python script to operate servo-driven feeder mechanisms

**Usage Notes:**
- Ensure correct pin mapping according to your assembly.  
- Upload `.ino` files using Arduino IDE (version 1.8+ recommended).  
- Python scripts require libraries: `RPi.GPIO`, `time`, `Adafruit_PCA9685` (for servo control).

---

## 📁 2. Sensors – `sensors/`

Contains sensor calibration data, configuration files, and test scripts:

**Examples:**
- `ultrasonic_config.json` – threshold distances and pins  
- `loadcell_calibration.csv` – weight calibration for dispensing food  
- Optional test scripts to verify sensor readings before integration

---

## 📁 3. Assembly – `assembly/`

Step-by-step instructions and visual guidance for assembling the feeder:

**Contents:**
- `step_by_step.pdf` – textual guide for assembly  
- `photos/` – high-resolution photos of each assembly stage (`step1.jpg`, `step2.jpg`, …)  
- Optional: exploded view diagrams for mechanical understanding

> 🔧 Tip: Take photos from multiple angles to clearly show wiring and component placement.

---

## 📁 4. Datasheets – `datasheets/`

Reference datasheets for all electronic components used:

**Examples:**
- `servo_motor_datasheet.pdf`  
- `ultrasonic_sensor.pdf`  
- `loadcell_datasheet.pdf`  

> 📌 Keep datasheets organized and named clearly for quick reference.

---

## 🧭 Suggested Workflow

1. Assemble mechanical components following `assembly/` instructions.  
2. Upload firmware from `firmware/` to microcontroller.  
3. Configure and calibrate sensors using files from `sensors/`.  
4. Test system in small stages before full deployment.  

---

## 📌 Best Practices

- Keep hardware and software clearly separated.  
- Compress large images but maintain clarity for assembly photos.  
- Version-control your firmware whenever changes are made.  
- Document any modifications in this README for future reference.  

---

## 🏁 Conclusion

This `hardware/` directory contains all the **physical intelligence and control logic** of StrayMate’s robotic feeder.  
Proper organization ensures **easy replication, debugging, and maintenance**, while making the project GitHub-ready and professional for reviewers.

---

✍️ **Author:** Swarnendu Bhattacharjee  
📅 **Last Updated:** October 2025  
🔗 **Project Repository:** [StrayMate – AI & Robotics for Stray Animal Welfare](../)
