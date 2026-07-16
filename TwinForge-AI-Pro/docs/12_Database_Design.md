# 12_Database_Design
# Database Design

Version: 1.0

Status: Planning

Date: 15 July 2026

---

# Objective

Design a scalable and efficient database for the TwinForge AI platform.

The database stores machine information, sensor readings, AI predictions, maintenance history, alerts, users, and system logs.

It acts as the central source of truth for the entire platform.

---

# Database Technologies

Prototype

SQLite

Production

PostgreSQL

Future

TimescaleDB (Time-Series Data)

Redis (Caching)

---

# Database Architecture

Factory

↓

Machines

↓

Sensors

↓

Sensor Data

↓

AI Predictions

↓

Maintenance Records

↓

Reports

---

# Entity Relationship Overview

Factory (1)

↓

Machines (Many)

↓

Sensors (Many)

↓

Sensor Readings (Many)

↓

AI Predictions (Many)

↓

Maintenance Records (Many)

---

# Tables

## 1. Users

Purpose

Store platform users.

Columns

- user_id (Primary Key)
- full_name
- email
- password_hash
- role
- created_at
- last_login

Roles

- Administrator
- Factory Manager
- Maintenance Engineer

---

## 2. Factories

Purpose

Store factory information.

Columns

- factory_id
- factory_name
- location
- contact_person
- created_at

---

## 3. Machines

Purpose

Store machine details.

Columns

- machine_id
- factory_id
- machine_name
- machine_type
- manufacturer
- installation_date
- status
- health_score

Status

- Healthy
- Warning
- Critical
- Offline

---

## 4. Sensors

Purpose

Store sensor information.

Columns

- sensor_id
- machine_id
- sensor_type
- model
- unit
- installation_date
- calibration_date
- status

Sensor Types

- Temperature
- Vibration
- Current
- RPM

---

## 5. Sensor Readings

Purpose

Store live IoT data.

Columns

- reading_id
- sensor_id
- timestamp
- value
- quality_flag

Example

Temperature

67°C

Time

2026-07-15 15:20:45

---

## 6. AI Predictions

Purpose

Store AI analysis results.

Columns

- prediction_id
- machine_id
- prediction_type
- confidence_score
- remaining_useful_life
- recommendation
- generated_at

Example

Prediction

Bearing Wear

Confidence

91%

RUL

5 Days

---

## 7. Maintenance Records

Purpose

Store maintenance activities.

Columns

- maintenance_id
- machine_id
- maintenance_type
- issue_found
- action_taken
- engineer_name
- maintenance_date
- next_due_date

---

## 8. Alerts

Purpose

Store system alerts.

Columns

- alert_id
- machine_id
- alert_type
- severity
- message
- created_at
- resolved_at
- status

Severity

Information

Warning

Critical

Emergency

---

## 9. Reports

Purpose

Store generated reports.

Columns

- report_id
- report_type
- generated_by
- generated_at
- file_path

---

## 10. System Logs

Purpose

Track important system events.

Columns

- log_id
- event_type
- description
- user_id
- timestamp

---

# Database Relationships

Factory

↓

Machines

↓

Sensors

↓

Sensor Readings

↓

AI Predictions

↓

Maintenance Records

↓

Alerts

Each machine may have multiple sensors.

Each sensor generates thousands of readings.

Each machine may have multiple AI predictions over time.

Maintenance records are linked directly to machines.

---

# Data Flow

ESP32

↓

Backend API

↓

Sensor Readings

↓

AI Prediction Engine

↓

Predictions Table

↓

Digital Twin

↓

Dashboard

---

# Indexing Strategy

Indexes should be created on:

- machine_id
- sensor_id
- timestamp
- prediction_id
- alert_status

Purpose

Improve query performance for real-time dashboards.

---

# Data Retention Policy

Live Sensor Data

1 Year

AI Predictions

5 Years

Maintenance Records

10 Years

System Logs

6 Months

Reports

Permanent

---

# Security

Passwords stored as hashes.

Role-Based Access Control (RBAC).

JWT authentication.

Encrypted database connections.

Regular database backups.

Audit logs for important actions.

---

# Scalability

Current Version

Single Factory

Future Versions

Multiple Factories

Cloud Deployment

Distributed Database

High Availability

---

# Future Database Enhancements

- TimescaleDB for time-series optimization
- Redis cache for live dashboards
- Data compression
- Automatic backups
- Data archiving
- AI training dataset generation

---

# Design Principles

- Normalized schema
- Scalable structure
- High performance
- Secure by design
- Easy maintenance
- Real-time support

---

# Long-Term Vision

The TwinForge AI database is designed to become the foundation of an Industry 4.0 platform capable of managing multiple factories, millions of sensor readings, and intelligent AI-driven maintenance insights while maintaining reliability, scalability, and security.
Paste the detailed content here.
