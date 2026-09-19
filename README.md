# ExamGuard - Online Exam Monitoring and Integrity Analytics Platform

## Description

ExamGuard is a state-of-the-art, AI-powered online exam monitoring and integrity analytics platform engineered to maintain absolute academic fairness during remote assessments. Developed using **Python, Flask, OpenCV, and SQLite**, the application acts as an intelligent virtual proctoring solution capable of autonomously supervising candidates, tracking focus, logging procedural violations, and delivering deep analytical insights to examiners.

Traditional remote testing often suffers from widespread malpractice and high oversight overhead. ExamGuard addresses these challenges by integrating **real-time computer vision algorithms** to detect face presence and anomalies, alongside automated event loggers that capture browser tab-switching or focus loss. Furthermore, the platform features a robust backend architecture equipped with automated data pipelines, synthetic dataset generators, and comprehensive visual dashboards built using Matplotlib. This empowers administrative bodies to efficiently review exam integrity scores, audit candidate behavior, and streamline compliance reporting in a secure environment.

## Key Features & Capabilities

- 🤖 **Real-time Computer Vision Proctoring**: Utilizes OpenCV Haar Cascade classifiers to continuously track student presence and detect visual anomalies during examinations.
- 📊 **Automated Integrity Scoring Engine**: Dynamically calculates trust and integrity indices based on weighted infractions and behavioral patterns.
- 📑 **Violation & Tab-Switch Logger**: Seamlessly monitors browser activity to record and timestamp focus shifts or unauthorized navigation.
- 📈 **Administrative Analytics & Dashboards**: Generates detailed graphical visualizations using Matplotlib to summarize exam performance and suspicious activity trends.
- 🗄️ **Secure Database Management**: Implements lightweight SQLite structures to securely store session metadata, student profiles, and chronological event logs.
- ⚙️ **Synthetic Data Generator**: Includes automated scripts to simulate test telemetry for system scaling, stress testing, and pipeline debugging.
- 🛡️ **Modular Architecture**: Built on robust Flask routing and Python modules ensuring scalability, rapid deployment, and clean separation of concerns.

## Technologies Used

### Backend & Core Logic
- **Python**: Primary programming language for business logic and algorithms.
- **Flask**: Lightweight web framework handling routing, sessions, and HTTP requests.
- **SQLite**: Relational database management for persistent data storage.

### Computer Vision & Data Analytics
- **OpenCV**: Image processing and real-time facial feature tracking.
- **Scikit-learn**: Machine learning utilities for anomaly classification and evaluation.
- **Matplotlib**: Data visualization library generating automated graphical summaries.

### Development & Version Control
- **Visual Studio Code**: Integrated development environment.
- **Git & GitHub**: Version control, repository standardization, and remote collaboration.


## Prerequisites & Installation

To run this project locally, ensure you have Python installed. The required dependencies are listed in `requirements.txt`.

1. Clone the repository:
   ```bash
   git clone [https://github.com/Udayasree2610/exam_monitoring_project.git](https://github.com/Udayasree2610/exam_monitoring_project.git)

2. Navigate to the project directory:
    cd exam_monitoring_projectg

3. Install dependencies:
    pip install -r requirements.txt

4. Run the application:
    python app.py


## Project Directory Structure

```text
exam_monitoring_project/
├── Documentation/
│   ├── Agile_Template_v0.1.xlsx
│   ├── Defect_Tracker_Template_v0.1.xlsx
│   └── Unit_Test_Plan_v0.1.xlsx
├── static/
│   ├── charts/
│   ├── faces/
│   ├── plots/
│   └── uploads/
├── templates/
│   ├── admin.html
│   ├── exam.html
│   ├── instructions.html
│   ├── login.html
│   ├── register.html
│   └── reports.html
├── ai_agent.py
├── analytics.py
├── app.py
├── dashboard.py
├── database.py
├── exam_monitor.db
└── synthetic_data_generator.py

## Documentation

Project management artifacts, structured documentation files, and testing blueprints are systematically organized under distinct directories in compliance with institutional standards:

- **Project Documentation/**: Contains the core technical planning and evaluation artifacts required for quality assurance:
  - **Unit_Test_Plan_v0.1.xlsx**: Outlines test cases, module verification procedures, inputs, and expected outcomes to ensure system reliability.
  - **Defect_Tracker_Template_v0.1.xlsx**: Tracks application bugs, severity levels, and resolution status throughout the testing phase.
- **Agile Documentation/**: Contains agile project management artifacts tracking iterative development:
  - **Agile_Template_v0.1 (1).xlsx**: Tracks sprint cycles, user stories, task backlogs, and milestone progress.s