
<h1 align="center" style="font-family: 'Arial', sans-serif;">
    <span style="color: #4CAF50;">RRT Path Planning</span>
</h1>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.9+-green.svg" alt="Python Version" />
    <img src="https://img.shields.io/badge/Pygame-2.0-blue.svg" alt="Pygame Version" />
    <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License" />
</p>

<p align="center">
    <img src="https://github.com/Hydra-Bolt/LiDARSimulator/blob/ad2e864feb9d65b166b77915d4b2917b7a9542f6/maps/example.png" alt="Project Screenshot" width="600">
</p>

---

<h2>🏁 Overview</h2>

<p style="font-family: 'Arial', sans-serif;">
    This project implements a visualization of a <strong>Rapidly-exploring Random Tree (RRT)</strong> path planning algorithm. It uses a laser sensor to simulate obstacle detection in real-time and updates the environment accordingly. The simulation is rendered using the Pygame library in Python.
</p>

<h2>💡 Features</h2>

<ul style="font-family: 'Arial', sans-serif';">
    <li>Real-time simulation of RRT path planning.</li>
    <li>Laser sensor to detect obstacles.</li>
    <li>Simulates uncertainty in sensor data using Gaussian noise.</li>
    <li>Dynamic rendering of the environment based on sensor input.</li>
</ul>

---

<h2>🔧 Installation</h2>

```bash
# Clone the repository
git clone https://github.com/Hydra-Bolt/LiDARSimulator.git

# Navigate into the directory
cd LiDARSimulator

# Install the required dependencies
pip install -r requirements.txt
```

<h3>💻 Requirements</h3>

<ul style="font-family: 'Arial', sans-serif';">
    <li>Python 3.9+</li>
    <li>Pygame 2.0+</li>
    <li>NumPy</li>
</ul>

---

<h2>🚀 Usage</h2>

```bash
# Run the simulation
python main.py
```

<p style="font-family: 'Arial', sans-serif;">
    Upon running the simulation, you will see a map with a robot's position. Move your mouse to simulate the robot's movement, and the laser sensor will detect obstacles in the environment and update the point cloud in real-time.
</p>

---

<h2>🛠️ Project Structure</h2>

```plaintext
├── env.py         # Environment setup and rendering logic
├── main.py        # Main script to run the simulation
├── sensors.py     # Sensor logic and obstacle detection
├── floor_map.png  # Map used in the environment
├── requirements.txt # Dependencies for the project
```

<h2>📈 Algorithm Details</h2>

<p style="font-family: 'Arial', sans-serif;">
    The RRT (Rapidly-exploring Random Tree) algorithm is designed for path planning in environments with obstacles. The laser sensor in this project senses the environment in 360 degrees, detects obstacles, and adjusts the path dynamically.
</p>

---
