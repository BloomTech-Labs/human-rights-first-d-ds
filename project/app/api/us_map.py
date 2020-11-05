from fastapi import APIRouter, HTTPException
import random
from pydantic import BaseModel, Field, validator
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('https://raw.githubusercontent.com/Lambda-School-Labs/human-rights-first-d-ds/beta/project/app/api/final.csv', index_col=[0])

## Functions
def map_function(df, start_date, end_date, sort_by:str= "Armed/Unarmed"):
    # Selection of timeframes
    df = df.copy()
    mask =  (df['Date of Incident (month/day/year)'] > start_date) & ( df['Date of Incident (month/day/year)'] <= end_date)
    df = df.loc[mask]
    mapbox_access_token = 'pk.eyJ1IjoicG9wa2RvZGdlIiwiYSI6ImNrZDdvZDFtbDAwNmwycW9xazQycWpldTYifQ.33ELrqLko1a0dHHEkSsxNw'
    if sort_by == "Armed/Unarmed":
        color="Unarmed/Did Not Have an Actual Weapon"
    if sort_by == "Demographic":
        color="Victim's race"
    if sort_by == "Gender":
        color="Victim's gender"
    px.set_mapbox_access_token(mapbox_access_token)
    fig = px.scatter_mapbox(df,
                            lat=df.lon,
                            lon=df.lat,
                            zoom=1,
                            hover_name= "Victim's name",
                            hover_data= ['Victim\'s age','Victim\'s gender','Victim\'s race',"State","City"],
                            color = color,
                            title=f"Police Shooting Between {start_date} and {end_date}"
                           )
    fig.update_layout(mapbox_style="open-street-map",
                      mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
    return fig.to_json()


router = APIRouter()

class Input(BaseModel):
    """Use this to mode pare request body JSON."""
    start_date: str
    end_date: str
    sort_by: str

@router.post('/us_map')
async def us_map(item: Input):
    """
    ### Request Body
    ---
    - `start_date` : string 'yy-mm-dd' format.
    - `end_date` : string 'yy-mm-dd' format.
    - `sort_by`: string
       - "Armed/Unarmed"
       - "Demographic",
       - "Victim's gender",
       - "Armed/Unarmed"

    ### Response
    ---
    Should return JSON to be converted in to Plotly graph_objects.
    """
    start_date = item.start_date
    end_date = item.end_date
    sort_by = item.sort_by
    return map_function(df, start_date, end_date, sort_by)