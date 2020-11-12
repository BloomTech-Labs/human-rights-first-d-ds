from fastapi import APIRouter, HTTPException
import plotly.graph_objects as go
import datetime
import pandas as pd
import json
import requests
from pydantic import BaseModel, Field, validator
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import geopy.geocoders
import plotly.graph_objects as go
import plotly.express as px
import random
import os
def PoliceViolence_map():
  link = 'https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/PoliceViolence.csv'
  df = pd.read_csv(link)
  mapbox_access_token = 'pk.eyJ1IjoicG9wa2RvZGdlIiwiYSI6ImNrZDdvZDFtbDAwNmwycW9xazQycWpldTYifQ.33ELrqLko1a0dHHEkSsxNw'
  px.set_mapbox_access_token(mapbox_access_token)
  fig = px.scatter_mapbox(df,
                          lat=df.lon,
                          lon=df.lat,
                          zoom=1,
                          hover_name= "name",
                          hover_data = ['Link1',],
                          animation_frame="date", animation_group="name",
                          color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"],
                          title="Recent Acts of Police Force",
                        )
  fig.update_yaxes(automargin=True)
  fig.update_xaxes(automargin=True))
  fig.update_layout(mapbox_style="open-street-map",
                    mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
  return fig.to_json()
router = APIRouter()

@router.get("/us_non_lethal")
async def us_non_lethal():
    """
    Return map of PoliceViolence
    """
    return PoliceViolence_map()