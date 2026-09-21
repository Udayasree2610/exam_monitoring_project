# PROJECT DOCUMENTATION

## 1. Introduction & Executive Summary

The **Online Exam Monitoring and Integrity Analytics Platform (ExamGuard)** is an advanced, AI-powered virtual proctoring solution designed to uphold academic honesty and integrity during remote examinations. Traditional remote assessments often suffer from unmonitored malpractices, high administrative overhead, and a lack of reliable behavioral tracking. ExamGuard resolves these challenges by integrating **real-time computer vision algorithms**, automated event logging, and robust analytics dashboards into a unified web application.

---

## 2. Problem Statement & Objectives

### Problem Statement
Conducting remote exams securely without physical invigilation leads to critical vulnerabilities, such as:
- Identity impersonation and proxy writing.
- Unauthorized resource browsing and tab-switching.
- Lack of real-time alert mechanisms for examiners to intervene during suspicious behavior.

### Primary Objectives
- **Automated Supervision**: Leverage computer vision to continuously track candidate face presence and detect visual anomalies.
- **Violation Tracking**: Log procedural infractions like browser focus loss, window minimization, and tab switches.
- **Analytics & Scoring**: Generate real-time integrity trust scores and visual data summaries to streamline administrative audits.

---

## 3. System Architecture & Technology Stack

The platform follows a modular web application architecture built using industry-standard tools:

- **Backend Framework (Python & Flask)**: Handles HTTP routing, server-side business logic, and secure user session management.
- **Computer Vision & AI (OpenCV)**: Utilizes Haar Cascade classifiers to execute real-time frame processing and facial feature detection via webcam feeds.
- **Data Management (SQLite)**: Acts as a lightweight relational database ensuring secure storage of candidate profiles, chronological event logs, and session integrity scores.
- **Analytics & Machine Learning (Matplotlib & Scikit-learn)**: Generates graphical performance trends, evaluation reports, and handles automated anomaly pattern processing.
- **Data Simulation Scripts (`synthetic_data_generator.py`)**: Used for stress-testing system telemetry and scaling data pipelines.

---

## 4. Core Functional Modules

- **Authentication & Authorization Module**: Provides secure login and registration portals segregated for students and administrative examiners.
- **Virtual Proctoring & Vision Engine**: Continuously tracks webcam streams during exams, actively flagging instances where a candidate's face is missing or multiple individuals are detected.
- **Violation & Tab-Switch Logger**: Monitors browser-level focus shifts, automatically recording precise timestamps and infraction categories when a candidate navigates away.
- **Integrity Scoring Engine**: Computes a dynamic trust index by aggregating weighted penalties derived from visual anomalies and browser violations.
- **Administrative Dashboard & Analytics**: Empowers examiners with graphical summaries, individual student audit trails, and data visualizations rendered through Matplotlib.

---

## 5. Software Testing & Quality Assurance

To ensure absolute system stability, the project is backed by structured quality assurance artifacts located within the documentation directory:
- **Unit Testing (`Unit_Test_Plan_v0.1.xlsx`)**: Outlines test cases, functional inputs, and expected outcomes to verify core module reliability.
- **Defect Tracking (`Defect_Tracker_Template_v0.1.xlsx`):** Records software bugs, severity ratings, reproduction steps, and resolution statuses identified during testing phases.

---

## 6. Conclusion

ExamGuard successfully bridges the gap between remote learning flexibility and rigorous examination security. By automating proctoring workflows through computer vision and structured logging, the platform ensures a fair, scalable, and transparent evaluation environment.