# 05_Sensor_Selection

# Sensor Selection

Version: 0.1
Status: Planning
Date: 15 July 2026

---

# Objective

Select suitable sensors for monitoring the health of a Three Phase Induction Motor.

The selected sensors should:

- Be compatible with ESP32
- Be affordable for a student prototype
- Provide reliable real-time data
- Be scalable for future industrial deployment

---

# Sensor Requirements

The system should monitor:

- Temperature
- Vibration
- Current
- RPM

These parameters provide sufficient information to detect common motor failures.

---

# Selected Sensors

## 1. Temperature Sensor

Purpose

Monitor motor body temperature.

Failure Detection

- Bearing overheating
- Cooling fan failure
- Stator overheating
- Overload condition

Recommended Sensor

DS18B20 Waterproof Temperature Sensor

Advantages

- Easy to connect
- Digital output
- Accurate
- Waterproof
- Low cost

ESP32 Interface

GPIO (OneWire)

---

## 2. Vibration Sensor

Purpose

Detect abnormal machine vibration.

Failure Detection

- Bearing wear
- Shaft misalignment
- Rotor imbalance
- Loose mounting

Recommended Sensor

SW-420 (Prototype)

Future Upgrade

Industrial MEMS Accelerometer
(ADXL345 / MPU6050 / Industrial IEPE sensor)

ESP32 Interface

Digital / I2C

---

## 3. Current Sensor

Purpose

Measure motor current.

Failure Detection

- Overload
- Rotor problems
- Electrical faults
- Stator faults

Recommended Sensor

ACS712

Future Upgrade

SCT-013 Current Transformer

ESP32 Interface

Analog

---

## 4. RPM Sensor

Purpose

Measure motor rotational speed.

Failure Detection

- Speed drop
- Shaft problems
- Mechanical load changes

Recommended Sensor

Hall Effect Sensor

Alternative

Optical Encoder

ESP32 Interface

Digital

---

# Sensor Summary

| Parameter | Sensor | ESP32 Compatible | Prototype | Industrial |
|------------|---------|-----------------|------------|------------|
| Temperature | DS18B20 
| Vibration | SW-420 
| Current | ACS712 
| RPM | Hall Effect 

---

# Future Sensors

Version 2.0

- Voltage Sensor
- Humidity Sensor
- Oil Quality Sensor
- Pressure Sensor
- Noise Sensor
- Thermal Camera
- Infrared Temperature Sensor

---

# Why These Sensors?

These four sensors are enough to detect most common failures in an induction motor while keeping the prototype affordable and easy to build.

Future versions of TwinForge AI can include additional sensors for higher diagnostic accuracy.
Paste the detailed content here.
