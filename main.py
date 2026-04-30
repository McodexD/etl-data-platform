import pandas as pd
import csv
import os

def generate_csv(filename="generated_products.csv"):
    """Creates a local CSV file with product data (Criteria F11)"""
    data = [
        {"id": 1, "name": "Laptop", "price": 1200.0, "quantity": 5, "category": "Electronics"},
        {"id": 2, "name": "Desk", "price": 450.0, "quantity": 10, "category": "Furniture"},
        {"id": 3, "name": "Headphones", "price": 150.0, "quantity": 25, "category": "Electronics"},
        {"id": 4, "name": "Coffee Mug", "price": 15.0, "quantity": 100, "category": "Home"},
        {"id": 5, "name": "Monitor", "price": 300.0, "quantity": 12, "category": "Electronics"}
    ]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"--- Step 1: {filename} has been generated successfully. ---")

def ingest_data(filename):
    """Reads the CSV data into a Pandas DataFrame (ETL: Ingest)"""
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        print("--- Step 2: Data has been ingested into Python. ---")
        print(df.head())
        return df
    else:
        print("Error: File not found.")
        return None

if __name__ == "__main__":
    file_name = "generated_products.csv"
    generate_csv(file_name)
    product_df = ingest_data(file_name)