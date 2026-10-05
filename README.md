# API Status Checker CLI

A simple Python command-line tool that checks websites and API endpoints, reports their HTTP status, measures response time, and handles network failures without crashing.

## Why It Exists

This project was built to practice working with HTTP requests, APIs, JSON configuration files, response-time measurement, and network error handling in Python.

## Features

- Reads endpoints from a JSON file
- Sends HTTP GET requests
- Displays HTTP status codes
- Measures response time in milliseconds
- Treats HTTP 200–399 as successful
- Identifies failed HTTP responses
- Handles connection errors
- Handles request timeouts
- Continues checking after failures
- Displays a summary of results

## Technologies

- Python
- requests
- JSON

## Installation

Clone the repository and install the dependency:

```bash
pip install -r requirements.txt