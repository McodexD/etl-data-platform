# Product ETL Data Platform

## Description
This project is a Python-based ETL (Extract, Transform, Load) pipeline built for the Data Platform 26 course. It demonstrates how to generate raw product data, process it for statistical insights, and expose the results via a web API.

## Features
* **Ingest**: Generates a CSV file and reads it using Pandas.
* **Transform**: Cleans data and calculates average prices and top products.
* **Load**: Serves data through a FastAPI endpoint.

## How to Run
1. Install dependencies: `pip install pandas fastapi uvicorn`
2. Run the application: `python main.py`
3. View statistics at: `http://127.0.0.1:8000/statistics`

## Agile Workflow
This project followed an agile methodology using:
* User Stories
* GitHub Project Board
* Feature Branching and Pull Requests