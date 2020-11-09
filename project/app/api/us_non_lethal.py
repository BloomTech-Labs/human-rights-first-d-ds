from sqlalchemy import create_engine, Table, Text, Column, String, MetaData, DateTime
import psycopg2
from fastapi import APIRouter, HTTPException
import plotly.graph_objects as go
import datetime
import pandas as pd
import json
import requests
from pydantic import BaseModel, Field, validator

link = 'https://raw.githubusercontent.com/2020PB/police-brutality/data_build/all-locations.csv'

def recent_pb(link, num_o_events):
  df = pd.read_csv(link)
  df = df.sort_values(by='date', ascending=False).head(num_o_events)
  df.columns = ['state', 'edit_at', 'city', 'name', 'date', 'date_text', 
                'id', 'Link1', 'Link2', 'Link3', 'Link4', 'Link5', 
                'Link6', 'Link7', 'Link8', 'Link9', 'Link10', 'Link11', 
                'Link12', 'Link13', 'Link14', 'Link15', 'Link16', 'Link17', 
                'Link18', 'Link19', 'Link20', 'Link21', 'Link22', 'Link23', 
                'Link24']
  df = df[['state', 'edit_at', 'city', 'name', 'date', 'date_text', 
           'id', 'Link1', 'Link2', 'Link3']]
  fig = go.Figure(data=[go.Table(header= dict(values=list(df.columns), 
                                              fill_color='paleturquoise', 
                                              align='left'),
                                 cells = dict(values=[df.state, df.edit_at, 
                                                      df.city, df.name, df.date, 
                                                      df.date_text, df.id, df.Link1,
                                                      df.Link2, df.Link3],
                                              fill_color='lavender',
                                              align='left'))
  ])
  result = df.to_json()
  parsed = json.loads(result)
  answers = json.dumps(parsed)
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
