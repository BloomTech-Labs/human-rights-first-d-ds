from fastapi import APIRouter, HTTPException
import random
from pydantic import BaseModel, Field, validator
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 
import json 

#loading csv in to Dataframes
df = pd.read_csv("https://raw.githubusercontent.com/popkdodge/Dataset-Holder/main/final.csv" ,index_col=[0])
asc= True
## Helper functions:
def pie_charts_vic(df, start_date:str, end_date:str, groupby, sort_by, asc):
    # Selection of timeframes
    df = df.copy()
    mask =  (df['Date of Incident (month/day/year)'] > start_date) & ( df['Date of Incident (month/day/year)'] <= end_date)
    df = df.loc[mask]
    
    if "National" in groupby:
        df = df[sort_by].value_counts(10).sort_values(ascending=asc).rename_axis(sort_by).reset_index(name='Percentage')
        labels = df[sort_by]
        values = df["Percentage"]
        try:
            fig = px.pie(df, values=values, names= labels, color=labels,
                         color_discrete_map={
                "Black": "#636EFA",
                "Hispanic": "#EF553B",
                "Native American": "#00CC96",
                "Asian": "#AB63FA",
                "Pacific Islander": "#FFA15A",
                "White":"#19D3F3",
                "Other": "#FF6692"})
            fig.update_yaxes(automargin=True)
            fig.update_xaxes(automargin=True)
            fig.update_layout(
                title=f"Percent of {sort_by}",
                xaxis_title="X Axis Title",
                yaxis_title="X Axis Title",
                font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="RebeccaPurple"))
        except:
            {"Error": "invalid User inputs"}
        return fig.to_json()
    if "States" in groupby:
        df = df.loc[df['State'].isin(groupby["States"])]
        df = df[sort_by].value_counts(10).sort_values(ascending=asc).rename_axis(sort_by).reset_index(name='Percentage')
        labels = df[sort_by]
        values = df["Percentage"]
        try:
            fig = px.pie(df, values=values, names= labels, color=labels,
                         color_discrete_map={
                "Black": "#636EFA",
                "Hispanic": "#EF553B",
                "Native American": "#00CC96",
                "Asian": "#AB63FA",
                "Pacific Islander": "#FFA15A",
                "White":"#19D3F3",
                "Other": "#FF6692"})
            fig.update_yaxes(automargin=True)
            fig.update_xaxes(automargin=True)
            fig.update_layout(
                title=f"Percent of {sort_by}",
                xaxis_title="X Axis Title",
                yaxis_title="X Axis Title",
                font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="RebeccaPurple"))
        except:
            return {"Error":"Invalid States Inputs"}
        return fig.to_json()         
    if "City" in groupby:
        df = df.loc[df['City_State'].isin(groupby["City"])]
        df = df[sort_by].value_counts(10).sort_values(ascending=asc).rename_axis(sort_by).reset_index(name='Percentage')
        labels = df[sort_by]
        values = df["Percentage"]
        try:
            fig = px.pie(df, values=values, names= labels, color=labels,
                         color_discrete_map={
                "Black": "#636EFA",
                "Hispanic": "#EF553B",
                "Native American": "#00CC96",
                "Asian": "#AB63FA",
                "Pacific Islander": "#FFA15A",
                "White":"#19D3F3",
                "Other": "#FF6692"})
            fig.update_yaxes(automargin=True)
            fig.update_xaxes(automargin=True)
            fig.update_layout(
                title=f"Percent of {sort_by}",
                xaxis_title="X Axis Title",
                yaxis_title="X Axis Title",
                font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="RebeccaPurple"))
        except:
            return {"Error":"Invalid States Inputs"}
        return fig.to_json()
    return "No Selection or invalid inputs"

router = APIRouter()

class Input(BaseModel):
    "Use this to pair request body JSOn"
    start_date: str
    end_date: str
    group_by: dict
    sort_by: str

@router.post("/us_pie_vic")
async def us_pie_vic(item: Input):
    """
start_date : string 'yyyy-mm-dd' format.
end_date : string 'yyyy-mm-dd' format.
group_by: string
{"States":["GA","FL","SC","CA","PA"]}
{'National':None}
{"Zipcode": [77414.0, 34614.0]}
{"City": ["Atlanta,GA"]}
sort_by: string
    
    
    """
    start_date = item.start_date
    end_date = item.end_date
    group_by = item.group_by
    sort_by = item.sort_by
    asc=True
    return pie_charts_vic(df, start_date, end_date, group_by, sort_by, asc)
