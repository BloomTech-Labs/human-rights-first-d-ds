import pandas as pd 
import numpy as np 

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
