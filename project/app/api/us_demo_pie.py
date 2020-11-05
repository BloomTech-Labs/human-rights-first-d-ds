from fastapi import APIRouter, HTTPException
import random
from pydantic import BaseModel, Field, validator
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json

# loading csv into Dataframes 
df = pd.read_csv('https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/State_Country_Pop.csv', index_col=[0])

## Helper functions:
def demographic_pie(df, user_input):
    fig = px.pie(df, values=user_input, names='Demographics', color_discrete_sequence=px.colors.qualitative.D3, title=f"Demographic of {user_input}")
    return fig.to_json()

router = APIRouter()

class Input(BaseModel):
    """Use this to mode pare request body JSON."""
    user_input: str

@router.post("/us_demo_pie")
async def us_demo_pie(item: Input):
    """
    ### Request body:
    ---
    - `user_input`: string 
        -"{insert state abbreviation}" ex. "AK"
        -use "US" for nationwide demographics.
    """
    user_input = item.user_input

    return demographic_pie(df,user_input)