
# StrayMate Architecture

This document explains the overall system design, folder structure, module breakdown, and data flow of the StrayMate project.

---

## 1. Folder Structure

```

stray-animal-feeder/
│
├── src/             # Python source code for robot control, data logging, and web app
├── notebooks/       # Jupyter notebooks for analysis and experimentation
├── data/            # Stores logs, feeding schedules, and animal images
├── assets/          # Images, diagrams, screenshots for documentation
├── docs/            # Project documentation (overview, installation, usage, architecture, etc.)
├── requirements.txt # Python dependencies
├── config.yaml      # Configuration file for robot settings and schedules
└── README.md        # Project overview and quick links

````

---

## 2. Module Breakdown

| Module                | Description |
|----------------------|-------------|
| **Computer Vision**   | Detects animals and identifies injuries using OpenCV and ML models. |
| **Navigation**        | Plans routes and maps the environment using GPS and sensors. |
| **Feeding System**    | Controls motors and dispensers to provide food and water. |
| **Web Dashboard**     | Displays robot status, logs, and allows scheduling via a web interface. |
| **Logging & Alerts**  | Stores feeding events and sends notifications for injured animals. |

---

## 3. Data Flow

1. **Input:**  
   - Sensors on the robot (camera, GPS, etc.)  
   - User inputs from web dashboard or configuration file  

2. **Processing:**  
   - Computer vision detects animals  
   - Navigation module calculates paths  
   - Feeding module executes commands  
   - Logs generated and stored  

3. **Output:**  
   - Updated web dashboard  
   - CSV logs in `data/logs.csv`  
   - Visualizations in notebooks  
   - Alerts for injured animals  



![StrayMate Data Flow]
````
          +-----------------+
          |   User Input /   |
          |  Web Dashboard  |
          +--------+--------+
                   |
                   v
        +---------------------+
        |  Robot Sensors:     |
        |  Camera, GPS, etc.  |
        +---------+-----------+
                  |
                  v
  +----------------+----------------+
  | Computer Vision Module          |
  | Detects animals, injuries      |
  +----------------+----------------+
                  |
                  v
  +----------------+----------------+
  | Navigation Module               |
  | Path planning & movement        |
  +----------------+----------------+
                  |
                  v
  +----------------+----------------+
  | Feeding System                  |
  | Dispenses food & water          |
  +----------------+----------------+
                  |
                  v
  +----------------+----------------+
  | Logging & Alerts                |
  | Logs events, sends notifications|
  +----------------+----------------+
                  |
                  v
       +---------------------+
       | Outputs: Dashboard, |
       | Logs, Visualizations|
       +---------------------+


---

## 4. Notes

* All modules are designed to be **modular and independent** for easier testing and upgrades.
* The `src/` folder contains separate Python files for each module (e.g., `vision.py`, `navigation.py`, `feeding.py`, `web_app.py`).
* Logs and configuration are separated from code for maintainability.

```

---
