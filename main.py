import pandas as pd
import csv
import os

def generate_csv(filename="generated_products.csv"):
    """Creates a local CSV file (Criteria F11)"""
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
    print(f"--- Step 1: {filename} generated. ---")

def ingest_data(filename):
    """Reads the CSV (ETL: Ingest)"""
    return pd.read_csv(filename)

def transform_data(df):
    """Clean data and calculate stats (ETL: Transform / KOM6)"""
  
    df = df.dropna()
    
  
    avg_prices = df.groupby('category')['price'].mean().to_dict()
    
  
    top_5 = df.nlargest(5, 'price')
    
    print("--- Step 2: Data Transformed (Statistics calculated) ---")
    return avg_prices, top_5

if __name__ == "__main__":
    file_name = "generated_products.csv"
    generate_csv(file_name)
    product_df = ingest_data(file_name)
    

    stats, top_products = transform_data(product_df)
    
    print("\nAverage Price per Category:")
    print(stats)
    print("\nTop 5 Most Expensive Products:")
    print(top_products)