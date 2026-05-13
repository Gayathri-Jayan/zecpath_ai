# zecpath_ai
# Zecpath AI System

## Overview
Zecpath is an AI-powered hiring platform that automates:
- ATS resume screening
- AI interviews
- Behavior analysis
- Technical assessments
- Offer generation

## Project Structure

### data/
Stores resumes, transcripts, and interview records.

### parsers/
Handles resume parsing and data extraction.

### ats_engine/
Implements ATS scoring and ranking logic.

### screening_ai/
Handles AI voice screening workflows.

### interview_ai/
Contains HR and technical interview AI modules.

### scoring/
Aggregates evaluation scores and hiring decisions.

### utils/
Shared utilities including logging and database configuration.

### tests/
Contains unit test scripts for AI modules.

## Setup

Install dependencies:

pip install -r requirements.txt

Run project:

python main.py

Run tests:

pytest tests/
