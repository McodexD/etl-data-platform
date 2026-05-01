import pandas as pd
import csv
import os
from fastapi import FastAPI


app = FastAPI()

def get_processed_data():
    """ETL Flow: Ingest and Transform using the provided products_100.csv"""
    
    file_name = "products_100.csv" 
    
   
    if not os.path.exists(file_name):
        return {"error": f"File '{file_name}' not found. Please place it in the same folder as main.py"}
    
  
    df = pd.read_csv(file_name)
    
  
    df = df.dropna()
    
    avg_prices = df.groupby('category')['price'].mean().to_dict()
    
    top_5 = df.nlargest(5, 'price').to_dict(orient="records")
    
    return {
        "status": "Success",
        "rows_processed": len(df),
        "avg_prices": avg_prices, 
        "top_5_products": top_5
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product ETL API - Using products_100.csv"}

@app.get("/statistics")
def get_stats():
    """Exposes the transformation results via API (Criteria KOM6/F11)"""
    return get_processed_data()

if __name__ == "__main__":
    import uvicorn
    print("Starting the API server with products_100.csv data...")
    uvicorn.run(app, host="127.0.0.1", port=8000)