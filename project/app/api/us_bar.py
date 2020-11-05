from fastapi import APIRouter, HTTPException
import random
from pydantic import BaseModel, Field, validator
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('https://raw.githubusercontent.com/Lambda-School-Labs/human-rights-first-d-ds/beta/project/app/api/final.csv', index_col=[0])
state_pop

## Functions
def bar_incident(state_pop, df, start_date:str, end_date:str, groupby:str="National",asc=True):
    """
    This function serves to generate bar graphs that represent rate of deadly police shooting
    with filter that is determined by user inputs.
    
    The function can take in certian start and end_date and limit the data representation to those
    stated timeframes.
    
    This funcation can group the data set to show the graph represending user specific Zipcodes and States.
    """
    state = state_pop.copy()
    df = df.copy()
    mask =  (df['Date of Incident (month/day/year)'] > start_date) & ( df['Date of Incident (month/day/year)'] <= end_date)
    df = df.loc[mask]
    if groupby == "National":
        test_df = df['State'].value_counts().sort_values(ascending=asc).rename_axis('State').reset_index(name='counts')
        fin = pd.merge(state_pop, test_df, how="inner", on="State")
        fin['count/popPermillions'] = round(fin["counts"]/fin["Pop. Millions"])
        fin = fin.sort_values(by="count/popPermillions")
        fig = px.bar(fin, x="State", y="count/popPermillions", title="Number of People killed by police in the Selected States", color="State")
        return fig.show()
    if "States" in groupby:
        test_df = df.loc[df["State"].isin(groupby["States"])]
        test_df = test_df['State'].value_counts().sort_values(ascending=asc).rename_axis('State').reset_index(name='counts')
        fin = pd.merge(state_pop, test_df, how="inner", on="State")
        fin['count/popPermillions'] = round(fin["counts"]/fin["Pop. Millions"])
        fin = fin.sort_values(by="count/popPermillions")
        fig = px.bar(fin, x="State", y="count/popPermillions", title="Number of People killed by police in the Selected States", color="State")
        return fig.show()          
    if "Zipcode" in groupby:
        test_df = df.loc[df["Zipcode"].isin(groupby["Zipcode"])]
        test_df = test_df['Zipcode'].value_counts().sort_values(ascending=asc).rename_axis('Zipcode').reset_index(name='counts')
        test_df['Zipcode'] = test_df["Zipcode"].astype(int)
        test_df['Zipcode'] = test_df["Zipcode"].astype(str)
        fig = px.bar(test_df, x="Zipcode", y="counts", title="Number of People killed by police in the Zipcode", color="Zipcode")
        return fig.show()  
    if "City" in groupby:
        test_df = df.loc[df["CityState"].isin(groupby["City"])]
        test_df = test_df['CityState'].value_counts().sort_values(ascending=asc).rename_axis('CityState').reset_index(name='counts')
        fig = px.bar(test_df, x="CityState", y="counts", title="Number of People killed by police in the selected City", color="CityState")
        return fig.show()    
    
    return "No Selection or invalid inputs"


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