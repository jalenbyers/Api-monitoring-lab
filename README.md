# API Monitoring Lab

A Python-based API monitoring tool that checks REST API endpoints, measures response time, evaluates HTTP status codes, handles API errors, and records health-check results in structured logs.

## Project Overview

This project was built to develop hands-on experience with:

- REST APIs
- Python scripting
- JSON data
- HTTP status codes
- API error handling
- Response-time monitoring
- Structured logging
- Git and GitHub

The monitoring tool currently checks multiple REST API endpoints and reports whether each endpoint is healthy or failed.

## How It Works

The application:

1. Sends a GET request to each configured API endpoint.
2. Measures the API response time.
3. Evaluates the HTTP status code.
4. Parses the JSON response.
5. Identifies successful and failed requests.
6. Records the results in a log file.
7. Displays a health report in the terminal.

### Architecture

```text
API Endpoints
      |
      v
Python Monitoring Script
      |
      +----> HTTP Status Code
      |
      +----> Response Time
      |
      +----> JSON Response
      |
      +----> Error Handling
      |
      v
Health Report + Log File

Technologies Used
Python 3
REST APIs
JSON
HTTP
Git
GitHub
macOS Terminal

Example output

API HEALTH REPORT
=================

Endpoint: /posts/1
Status: 200
Response: 0.22s
STATUS: Healthy

Endpoint: /posts/2
Status: 200
Response: 0.18s
STATUS: Healthy

Endpoint: /posts/3
Status: 200
Response: 0.15s
STATUS: Healthy

Endpoint: /posts/9999
Status: 404
Response: 0.17s
STATUS: Failed
Error: Not Found

-----------------
Healthy: 3
Failed: 1

Logging

The application records API health-check results in:
logs/api_monitor.log

Example:
2026-08-12 23:25:36,005 | INFO | /posts/1 | 200 | 0.21s | HEALTHY
2026-08-12 23:25:36,183 | INFO | /posts/2 | 200 | 0.17s | HEALTHY
2026-08-12 23:25:36,359 | INFO | /posts/3 | 200 | 0.17s | HEALTHY
2026-08-12 23:25:36,522 | ERROR | /posts/9999 | 404 | 0.16s | FAILED

Project structure

api-monitoring-lab/
├── .gitignore
├── README.md
├── src/
│   └── api_monitor.py
├── logs/
│   └── api_monitor.log
└── venv

logs/ and venv/ are excluded from version control using .gitignore.

Running the Project

Create and activate the Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Run the monitoring script:
python src/api_monitor.py

## Current Capabilities

- [x] REST API health checks
- [x] Multiple endpoint monitoring
- [x] HTTP status-code validation
- [x] JSON response parsing
- [x] Response-time measurement
- [x] HTTP error handling
- [x] Structured logging
- [x] Git version control
- [x] GitHub repository

## Planned Improvements

- [ ] Add response-time thresholds
- [ ] Add configurable API endpoints
- [ ] Add automated tests
- [ ] Add API authentication
- [ ] Add environment variables for configuration
- [ ] Add monitoring metrics
- [ ] Add alerting for failed endpoints
- [ ] Add CI/CD with GitHub Actions

## What I Learned

Through this project, I gained hands-on experience building and troubleshooting a Python application that interacts with REST APIs.
Key concepts practiced include HTTP methods, status codes, JSON parsing, exception handling, reusable functions, response-time measurement, structured logging, Git workflows, and GitHub repository management.