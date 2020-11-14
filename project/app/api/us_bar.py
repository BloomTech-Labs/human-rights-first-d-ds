from fastapi import APIRouter, HTTPException
import random
from pydantic import BaseModel, Field, validator
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json



df = pd.read_csv('https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/final.csv', index_col=[0])
state_pop = pd.read_csv("https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/state_pop.csv", index_col=[0])

## Functions
def bar_incident(state_pop, df, start_date:str, end_date:str, groupby,asc=True):
    """
    This function serves to generate bar graphs that represent rate of deadly police shooting
    with filter that is determined by user inputs.
    
    The function can take in certian start and end_date and limit the data representation to those
    stated timeframes.
    
    This funcation can group the data set to show the graph represending user specific Zipcodes and States.
    """
    groupby = groupby
    state = state_pop.copy()
    df = df.copy()
    mask =  (df['Date of Incident (month/day/year)'] > start_date) & ( df['Date of Incident (month/day/year)'] <= end_date)
    df = df.loc[mask]
    if "National" in groupby:
        test_df = df['State'].value_counts().sort_values(ascending=asc).rename_axis('State').reset_index(name='counts')
        fin = pd.merge(state_pop, test_df, how="inner", on="State")
        fin['count/popPermillions'] = round(fin["counts"]/fin["Pop. Millions"])
        fin = fin.sort_values(by="count/popPermillions")
        try:
            fig = px.bar(fin, x="State", y="count/popPermillions", title="Number of People killed by police in the Selected States", color="State")
            fig.update_yaxes(automargin=True)
            fig.update_xaxes(automargin=True)
        except:
            return {"Error": "Invalid inputs."}
        return fig.to_json()
    if "States" in groupby:
        test_df = df.loc[df["State"].isin(groupby["States"])]
        if test_df.to_json() == "{}":
            return {"Error":"Invalid user inputs"}
        test_df = test_df['State'].value_counts().sort_values(ascending=asc).rename_axis('State').reset_index(name='counts')
        fin = pd.merge(state_pop, test_df, how="inner", on="State")
        fin['count/popPermillions'] = round(fin["counts"]/fin["Pop. Millions"])
        fin = fin.sort_values(by="count/popPermillions")
        try:
            fig = px.bar(fin, x="State", y="count/popPermillions", title="Number of People killed by police in the Selected States", color="State")
            fig.update_yaxes(automargin=True)
            fig.update_xaxes(automargin=True)
        except:
            return {"Error": "No incident for the selected states"}
        return fig.to_json()          
    if "Zipcode" in groupby:
        test_df = df.loc[df["Zipcode"].isin(groupby["Zipcode"])]
        test_df = test_df['Zipcode'].value_counts().sort_values(ascending=asc).rename_axis('Zipcode').reset_index(name='counts')
        test_df['Zipcode'] = test_df["Zipcode"].astype(int)
        test_df['Zipcode'] = test_df["Zipcode"].astype(str)
        try:
            fig = px.bar(test_df, x="Zipcode", y="counts", title="Number of People killed by police in the Zipcode", color="Zipcode")
            fig.update_yaxes(automargin=True)
            fig.update_xaxes(automargin=True)
        except:
            return {"Error": "No incident for the selected zipcode"}
        return fig.to_json()  
    if "City" in groupby:
        test_df = df.loc[df["City_State"].isin(groupby["City"])]
        test_df = test_df['City_State'].value_counts().sort_values(ascending=asc).rename_axis('CityState').reset_index(name='counts')
        try:
            fig = px.bar(test_df, x="CityState", y="counts", title="Number of People killed by police in the selected City", color="CityState")
            fig.update_yaxes(automargin=True)
            fig.update_xaxes(automargin=True)
        except:
            return {"Error": "No incident for the selected City"}
        return fig.to_json()    
    
    return "No Selection or invalid inputs"


router = APIRouter()

class Input(BaseModel):
    """Use this to mode pare request body JSON."""
    start_date: str
    end_date: str
    group_by: dict
    asc: bool

@router.post('/us_bar')
async def us_bar(item: Input):
    """
    ### Request Body
    ---
    - `start_date` : string 'yyyy-mm-dd' format.
    - `end_date` : string 'yyyy-mm-dd' format.
    - `group_by`: string
       - {"States":["GA","FL","SC","CA","PA"]}
       - {'National':None}
       - {"Zipcode": [77414.0, 34614.0]}
       - {"City": ["Atlanta, GA"]}
    - `asc` : True/False
    ### Response
    ---
    Should return JSON to be converted in to Plotly graph_objects.
    """
    start_date = item.start_date
    end_date = item.end_date
    group_by = item.group_by
    asc = item.asc
    #                                   **item  
    return bar_incident(state_pop, df, start_date, end_date, group_by,asc)