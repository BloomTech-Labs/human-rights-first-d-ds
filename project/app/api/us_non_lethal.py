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

link = 'https://raw.githubusercontent.com/2020PB/police-brutality/data_build/all-locations.csv'

def recent_pb(link, num_o_events=30):
  df = pd.read_csv(link)
  df = df.sort_values(by='date', ascending=False).head(num_o_events)
  df.columns = ['state', 'edit_at', 'city', 'name', 'date', 'date_text', 
                'id', 'Link1', 'Link2', 'Link3', 'Link4', 'Link5', 
                'Link6', 'Link7', 'Link8', 'Link9', 'Link10', 'Link11', 
                'Link12', 'Link13', 'Link14', 'Link15', 'Link16', 'Link17', 
                'Link18', 'Link19', 'Link20', 'Link21', 'Link22', 'Link23', 
                'Link24']
  df = df[['state', 'edit_at', 'city', 'name', 'date', 'date_text', 
           'id', 'Link1']]
  def anchor_tag(url):
    return f'<a href="{url}">{url}</a'
  df['Link1'] = df['Link1'].apply(anchor_tag)
  df['edit_at'] = df['edit_at'].apply(anchor_tag)
  df['location'] = df['city'] + ", " + df['state']
  geopy.geocoders.options.default_user_agent = "PlaceFinder"
  geolocator = Nominatim()
  geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1/20)
  df['geocode'] = df['location'].apply(geocode)
  df['point'] = df['geocode'].apply(lambda loc: tuple(loc.point) if loc else None)
  df['point'] = df.point.astype(str)
  df.point = df.point.str.rstrip(")")
  df.point = df.point.str.lstrip("(")
  df.point.dropna(inplace=True)
  new = df.point.str.split(",", expand=True)
  df['lon'] = new[0]
  df['lat'] = new[1]
  df['lon'] = df.lon.astype(float)
  df['lat'] = df.lat.astype(float)
  df = df[['location', 'name', 'date', 'id', 'Link1', 'lon', 'lat']]
  def randomize(flt):
    x = flt + (round(0.0001 * random.randrange(0,999), 6))
    return x
  df['lat'] = df['lat'].apply(randomize)
  df['lon'] = df['lon'].apply(randomize)
  mapbox_access_token = 'pk.eyJ1IjoicG9wa2RvZGdlIiwiYSI6ImNrZDdvZDFtbDAwNmwycW9xazQycWpldTYifQ.33ELrqLko1a0dHHEkSsxNw'
  px.set_mapbox_access_token(mapbox_access_token)
  fig = px.scatter_mapbox(df,
                        lat=df.lon,
                        lon=df.lat,
                        zoom=1,
                        hover_name= "name",
                        hover_data = ['Link1'],
                        color="date",
                        title=f"Recent Acts of Police Force"
                       )
  fig.update_layout(mapbox_style="open-street-map",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})

  return fig.to_json()

router = APIRouter()

class Input(BaseModel):
    """Use this to mode pare request body JSON."""
    user_input: int

@router.post("/us_non_lethal")
async def us_non_lethal(item: Input):
    """
    Pulls data from API. Shapes it to an acceptably limited form. 
    Requests number of recent inputs. Default to 20.
    -'user_input': Integer
    """
    user_input = item.user_input
    return recent_pb(link, user_input)