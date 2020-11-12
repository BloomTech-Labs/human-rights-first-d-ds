from fastapi import APIRouter, HTTPException
import plotly.graph_objects as go
import datetime
import pandas as pd
import json
import requests
from pydantic import BaseModel, Field, validator
import plotly.graph_objects as go
import plotly.express as px
import random
import os

def line_chart():
    link = 'https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/events.csv'
    df = pd.read_csv(link)
    fig = px.line(df,
                x="date",
                y="events",
                title='Events of police violence',
                color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"])
    return fig.to_json()
router = APIRouter()

@router.get("/us_non_lethal_line")
async def us_non_lethal_line():
    """
    Return map of PoliceViolence
    """
    return line_chart()