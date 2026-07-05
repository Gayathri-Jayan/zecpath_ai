# Zecpath AI – Intelligent AI Hiring Platform

## Overview

Zecpath AI is an AI-powered recruitment platform that automates the complete hiring workflow using Artificial Intelligence and Natural Language Processing.

The system is designed to assist recruiters by screening resumes, conducting AI-driven interviews, evaluating communication and behavioral skills, assessing logical reasoning, and generating recruiter-ready hiring reports.

---

## Features

### ATS Resume Screening
- Resume parsing (PDF & DOCX)
- Skill extraction
- Education & experience parsing
- ATS score calculation
- Resume ranking
- Role similarity matching
- Eligibility checking
- Fairness-aware scoring

### AI Screening System
- AI screening question engine
- Speech-to-text pipeline
- Answer understanding engine
- Intent classification
- Confidence & sentiment analysis
- Screening score generation
- Edge-case handling
- Error recovery
- Conversation state management

### HR Interview AI
- Dynamic HR question generation
- Role-based interviews
- Experience-based questions
- Adaptive follow-up questions
- Conversation flow management
- Interview state tracking
- Decision tree logic

### Communication Evaluation
- Fluency analysis
- Grammar evaluation
- Vocabulary assessment
- Explanation clarity
- Answer structure detection
- Filler word detection
- Communication score normalization

### Behavioral Analysis
- Confidence detection
- Stress indicator analysis
- Hesitation detection
- Repeated word detection
- Contradiction detection
- Sentiment analysis
- Behavioral confidence scoring

### Aptitude Evaluation
- Logical reasoning assessment
- Situational judgment evaluation
- Problem-solving analysis
- Scenario-based scoring
- Decision quality evaluation

### HR Interview Evaluation
- HR interview scoring engine
- Explainable score breakdown
- Weight configuration
- Candidate HR report generation
- Interview summary generation
- Recruiter-friendly recommendations

### End-to-End Simulation
- Multiple candidate simulations
- AI vs Manual evaluation comparison
- Hiring recommendation generation
- Accuracy evaluation
- System testing framework

---

# Project Structure

```
ZECPATH_AI/
│
├── api/                          # FastAPI endpoints
├── ats_engine/                   # ATS resume screening engine
├── data/                         # Resumes, transcripts, JSON outputs
├── interview_ai/                 # HR Interview AI modules
├── logs/                         # System logs
├── parsers/                      # Resume parsing utilities
├── resume_section_classifier/    # Resume section detection
├── scoring/                      # Scoring engines
├── screening_ai/                 # AI screening system
├── tests/                        # Unit tests
├── utils/                        # Helper utilities
│
├── main.py
├── main_jd.py
├── requirements.txt
└── README.md
```

---

# Technology Stack

- Python 3.10+
- FastAPI
- JSON
- Regular Expressions
- NLP (Rule-Based)
- Speech-to-Text Pipeline
- AI Interview Logic
- Git & GitHub

---

# Modules Implemented

## Resume Processing
- Resume Parsing
- Resume Cleaning
- Skill Extraction
- Section Classification

## ATS Engine
- ATS Score Engine
- Ranking Engine
- Eligibility Engine
- Fairness Engine
- Semantic Matching
- Role Detection

## AI Screening
- Question Dataset
- Conversation Flow
- Intent Classification
- Confidence Analysis
- Sentiment Analysis
- Screening Scoring
- Edge Case Handling

## HR Interview AI
- Question Bank
- Adaptive Questioning
- Follow-up Engine
- Interview Flow
- State Tracking

## Candidate Evaluation
- Communication Scoring
- Behavioral Signals
- Confidence Analysis
- Aptitude Evaluation
- HR Interview Scoring

## Reporting
- HR Score Report
- Interview Summary Generator
- Candidate Recommendation
- Recruiter Summary

---

# Installation

Clone the repository

```bash
git clone https://github.com/Gayathri-Jayan/zecpath_ai.git
```

Go into the project

```bash
cd zecpath_ai
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the main application

```bash
python main.py
```

Run Job Description parser

```bash
python main_jd.py
```

---

# Running Tests

Run all tests

```bash
pytest
```

Run an individual test

```bash
python -m tests.test_screening_system
```

Example:

```bash
python -m tests.test_hr_scoring
python -m tests.test_hr_simulation
python -m tests.test_interview_summary
```

---

# Current Project Status

**Completed (Days 1–40)**

- Resume Parsing Engine
- ATS Engine
- AI Screening System
- Speech-to-Text Processing
- Communication Evaluation
- Behavioral Analysis
- HR Interview AI
- Adaptive Follow-up Logic
- Aptitude Evaluation
- Interview Summary Generator
- HR Interview Simulation

---

# Future Roadmap

- Technical Interview AI
- Coding Assessment Engine
- AI Proctoring
- Video Interview Analysis
- LLM-powered Answer Evaluation
- Recruiter Dashboard
- Candidate Portal
- Deployment on Cloud

---

# Author

**Gayathri Jayan**

B.Tech Computer Science Engineering

AI | Python | NLP | Recruitment Automation

---

# License

This project is developed for educational and research purposes.
