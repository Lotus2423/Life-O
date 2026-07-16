# 13_API_Design# API Design

Version: 1.0

Status: Planning

Date: 15 July 2026

---

# Objective

Define all APIs required for communication between the IoT devices, backend server, AI engine, Digital Twin, and frontend dashboard.

The API design follows REST principles for standard operations and WebSocket for real-time communication.

---

# API Architecture

ESP32 Sensors
        │
        ▼
Backend API (FastAPI)
        │
 ┌──────┼──────────┐
 ▼      ▼          ▼
Database AI Engine WebSocket
        │
        ▼
Frontend Dashboard
        │
        ▼
Factory Manager

---

# API Standards

Protocol

HTTPS

Data Format

JSON

Authentication

JWT

Version

v1

Base URL

/api/v1/

---

# Authentication APIs

## Login

POST

/api/v1/auth/login

Request

{
  "email": "manager@factory.com",
  "password": "********"
}

Response

{
  "token": "...",
  "user": {
      "name": "Factory Manager",
      "role": "Manager"
  }
}

---

## Logout

POST

/api/v1/auth/logout

---

## Refresh Token

POST

/api/v1/auth/refresh

---

# Machine APIs

## Get All Machines

GET

/api/v1/machines

---

## Get Machine Details

GET

/api/v1/machines/{machine_id}

---

## Register Machine

POST

/api/v1/machines

---

## Update Machine

PUT

/api/v1/machines/{machine_id}

---

## Delete Machine

DELETE

/api/v1/machines/{machine_id}

---

# Sensor APIs

## Get Sensors

GET

/api/v1/machines/{machine_id}/sensors

---

## Register Sensor

POST

/api/v1/sensors

---

## Update Sensor

PUT

/api/v1/sensors/{sensor_id}

---

# Sensor Data APIs

## Upload Sensor Data

POST

/api/v1/sensor-data

Used by ESP32.

Request Example

{
  "machine_id":"M001",
  "temperature":67.2,
  "vibration":2.4,
  "current":4.8,
  "rpm":1450,
  "timestamp":"2026-07-15T15:45:10Z"
}

Response

{
  "status":"received"
}

---

## Get Live Sensor Data

GET

/api/v1/machines/{machine_id}/live

---

## Get Historical Data

GET

/api/v1/machines/{machine_id}/history

Query Parameters

start_date

end_date

sensor_type

---

# AI APIs

## Get Latest Prediction

GET

/api/v1/machines/{machine_id}/prediction

---

## Run AI Analysis

POST

/api/v1/ai/analyze

Purpose

Trigger manual AI analysis.

---

## AI Explanation

GET

/api/v1/machines/{machine_id}/explanation

Response Example

{
 "prediction":"Bearing Wear",
 "confidence":91,
 "reason":"Temperature and vibration increased continuously over the last 7 days."
}

---

# Maintenance APIs

## Get Maintenance History

GET

/api/v1/machines/{machine_id}/maintenance

---

## Create Maintenance Record

POST

/api/v1/maintenance

---

## Update Maintenance Record

PUT

/api/v1/maintenance/{id}

---

# Alert APIs

## Get Active Alerts

GET

/api/v1/alerts

---

## Mark Alert as Resolved

PUT

/api/v1/alerts/{alert_id}

---

# Report APIs

## Generate Report

POST

/api/v1/reports

---

## Download Report

GET

/api/v1/reports/{report_id}

---

# Digital Twin APIs

## Get Twin Status

GET

/api/v1/digital-twin/{machine_id}

---

## Update Twin State

POST

/api/v1/digital-twin/update

Used internally by backend.

---

# WebSocket Events

Purpose

Provide real-time updates without refreshing the dashboard.

Connection

/ws

---

Event

sensor_update

Payload

{
 "machine":"Motor-01",
 "temperature":67,
 "rpm":1450
}

---

Event

prediction_update

Payload

{
 "machine":"Motor-01",
 "prediction":"Bearing Wear",
 "confidence":91
}

---

Event

alert_created

Payload

{
 "machine":"Motor-01",
 "severity":"Critical"
}

---

Event

machine_status_changed

Payload

{
 "machine":"Motor-01",
 "status":"Warning"
}

---

# HTTP Status Codes

200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

500 Internal Server Error

---

# Security

JWT Authentication

Role-Based Access Control

HTTPS Only

Input Validation

Rate Limiting

Audit Logging

---

# API Versioning

Current

v1

Future

v2

Old versions remain available for backward compatibility.

---

# Development Principles

RESTful Design

Stateless APIs

Consistent JSON Structure

Clear Error Messages

Comprehensive Validation

Real-Time Communication

---

# Long-Term Vision

The API layer should enable seamless communication between industrial hardware, AI services, digital twins, and user interfaces while remaining secure, scalable, and easy to integrate with future systems such as mobile applications, ERP platforms, and cloud services.
Paste the detailed content here.
