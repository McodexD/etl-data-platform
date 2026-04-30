import pandas as pd
import csv
import os
from fastapi import FastAPI


app = FastAPI()

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

def get_processed_data():
    """ETL Flow: Ingest and Transform (Criteria KOM6)"""
    file_name = "generated_products.csv"
    if not os.path.exists(file_name):
        generate_csv(file_name)
    
    df = pd.read_csv(file_name)
    avg_prices = df.groupby('category')['price'].mean().to_dict()
    top_5 = df.nlargest(5, 'price').to_dict(orient="records")
    return {"avg_prices": avg_prices, "top_5_products": top_5}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product ETL API"}

@app.get("/statistics")
def get_stats():
    """Exposes the transformation results via API"""
    return get_processed_data()

if __name__ == "__main__":
    import uvicorn
    print("Starting the API server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)