# 🌊 Underwater Drone – Aqua Pi Project

## 📌 Project Overview
This project focuses on developing a Raspberry Pi–based underwater drone capable of monitoring water conditions, capturing live underwater video, and performing object manipulation using a robotic gripper.

The drone integrates multiple sensors, camera streaming, motor control, and a web-based monitoring dashboard.

---

## 🎯 Objectives
- Monitor water quality parameters (pH, temperature, depth)
- Capture live underwater video feed
- Control thrusters and robotic gripper
- Real-time environmental monitoring
- Expandable underwater robotics platform

---

## ⚙️ Hardware Components

### Core Components
- Raspberry Pi 4 Model B
- USB Camera Module
- L298N Motor Driver
- DC Motors (prototype thrusters)
- External battery power supply

---

## 💻 Software Stack

- Python 3
- Flask Web Framework
- OpenCV (camera streaming)
- RPi.GPIO library
- Adafruit ADS1115 library

---

## 📂 Project Structure
### Sensors Used
- Depth Sensor
- Waterproof Temperature Sensor (DS18B20)

### Additional Components
- Servo motor gripper
- Waterproof drone body
- Flask web dashboard

---

## ▶️ How to Run

Install required libraries:
pip install -r requirements.txt


Run sensor example:
python sensors/ph_sensor.py


Run camera streaming:
python camera/webcam_stream.py


---

## 🚀 Future Improvements
- Waterproof thrusters
- AI-based object detection
- Autonomous navigation
- Deep-water pressure-resistant body
- Improved battery system

---

## 👨‍💻 Author
**Souvagya Karmakar**  
Engineering Underwater Drone Project

---

## 📜 License
This project is intended for academic and research purposes.

---

## 📄 Project Report
The complete project documentation is available in the `docs` folder.


