from fastapi import APIRouter, HTTPException
import random
from pydantic import BaseModel, Field, validator
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 
import json 

# Helper's Functions 
def top_x_func(dataset, filters, count=10):
    # Choose a datasets:
    if dataset == "Killings":
        df = pd.read_csv("https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/final.csv" ,index_col=[0])
        # Choose filters:
        if filters == "State":
            df = df.groupby("State").count().sort_values(by=["City"],ascending =False)['City'].head(count).reset_index()
            df.columns = ['State', 'Counts']
            df.index +=1
            return df.to_json(orient="index")
        if filters == "City":
            df = df.groupby("City").count().sort_values(by=["State"],ascending =False)['State'].head(count).reset_index()
            df.columns = ['City', 'Counts']
            df.index +=1
            return df.to_json(orient="index")       
    if dataset == "PViolence":
        df = pd.read_csv("https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/PoliceViolence.csv", index_col=[0])
        if filters == "State":
            df = df.groupby("state").count().sort_values(by=["city"], ascending=False).head(count)["city"].reset_index()
            df.columns = ['State', 'Counts']
            df.index +=1
            return df.to_json(orient="index")
        if filters == "City":
            df = df.groupby("city").count().sort_values(by=["state"], ascending=False).head(10)["state"].reset_index()
            df.columns = ['City', 'Counts']
            df.index +=1
            return df.to_json(orient="index")       
    return {"Error": "Invalid Inputs"}

router = APIRouter()

class Input(BaseModel):
    "Use this to pair request body JSOn"
    dataset: str
    filter: str
    count: int

@router.post("/top_x_list")
async def top_x_list(item: Input):
    """
    `dataset`: choose either "PViolence" or "Killings"
    `filter` : choose either "State" or "City"
    `count` : the top X ammount fiter.
    
    """
    return top_x_func(item.dataset, item.filter, item.count)