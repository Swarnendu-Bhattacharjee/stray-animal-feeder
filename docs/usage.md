
# Usage Guide

This guide explains how to run StrayMate using scripts, notebooks, or the web app, along with examples of inputs and outputs.

---

## 1. Running Python Scripts

### Robot Control Script
```bash
python src/robot_control.py
````

* **Purpose:** Controls the robot for feeding and navigation.
* **Example Input:** None (runs based on default configuration in `config.yaml`)
* **Example Output:**

```
[INFO] Robot initialized
[INFO] Navigating to Zone A
[INFO] Dispensed 50g of dry food
[INFO] Feeding complete
```

### Data Logging Script

```bash
python src/log_data.py
```

* **Purpose:** Logs detected animals, feeding times, and alerts.
* **Example Output:**

```
[LOG] 2025-09-29 10:30:00 | Dog | Zone A | Food: 50g | Alert: No
[LOG] 2025-09-29 11:00:00 | Injured Cat | Zone B | Food: 30g | Alert: Yes
```

---

## 2. Running Jupyter Notebooks

### Notebook Launch

```bash
jupyter notebook notebooks/analysis.ipynb
```

* **Purpose:** Analyze data, test algorithms, visualize feeding and detection logs.
* **Example Output:**

  * Plots of animal detections over time.
  * Feeding statistics charts.
  * Heatmap of visited zones.

---

## 3. Using the Web App

1. Start the backend server:

```bash
python src/web_app.py
```

2. Open a browser and go to:

```
http://localhost:5000
```

3. **Features:**

   * Dashboard showing current robot status and feeding logs.
   * Schedule feeding times.
   * Receive alerts for injured animals.
   * Visualize maps and activity logs.

**Example:** Scheduling a feeding

* Input: Zone C, Dry Food, 50g
* Output: Robot navigates to Zone C and dispenses food; logs updated.

---

## 4. Notes

* Ensure the robot hardware or simulator is connected when running control scripts.
* All logs are stored in `data/logs.csv`.
* Sample configurations are in `config.yaml` (adjust zones, quantities, and times as needed).

---