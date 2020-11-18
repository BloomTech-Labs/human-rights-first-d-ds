# Human Rights First D DS

## Description
We were approached to undertake this project by Human Rights First, a non-profit, nonpartisan organization dedicated to fighting for human rights and race equality. They have been working diligently for over 40 years, with a strong presence across the country, from Washington D.C. and Los Angeles. They have been on the forefront of this struggle for a long time, and they are very good at what they do.
The purpose of this app is to better track and report acts of police use of force. There are wild inconsistencies regarding how these acts are reported, and the information is thin no matter where you look. Using various APIs and datasets, we pooled and shaped these sources and rendered them onto an easily navigated map of the US as well as multiple graphs pointing out discrepancies. Each datapoint on the map is clickable and will give the metrics for what it represents. The goal was to have a single source of truth on this matter.
Moving forward, the app could benefit from more social media API data, and possibly an NLP model to assess this data to find relevant incidents.

If we do a video, we should add it here.

## Contributors

| [Rob Bennett](https://github.com/RobDBennett) | [Sasana Kongjareon](https://github.com/popkdodge) | [Royer Adames](https://github.com/royeradames) | [Bikesh Maharjan](https://github.com/bikesh-maharjan) | [Heath Scott](https://github.com/Scotth72) |
| :---: | :---: | :---: | :---: | :---: |
| [<img src="https://avatars1.githubusercontent.com/u/64490045?s=460&u=85f903c0baf6ae8fcab0ae2d1686a434ce90be6b&v=4" width = "200" />](https://github.com/RobDBennett) | [<img src="https://avatars1.githubusercontent.com/u/62583069?s=460&u=2ce19efe9d7d8a39d3c2dc64b7a1b764b6d3c79c&v=4" width = "200" />](https://github.com/popkdodge) | [<img src="https://avatars1.githubusercontent.com/u/16887907?s=460&u=abefba57b8b58084d4df6c8a666873ed0986eea6&v=4" width = "200" />](https://github.com/royeradames) | [<img src="https://avatars2.githubusercontent.com/u/55510668?s=460&u=971839c4635847249a9c6ffc1d3b855f05910041&v=4" width = "200" />](https://github.com/bikesh-maharjan) | [<img src="https://avatars1.githubusercontent.com/u/59752102?s=460&u=bdcb67dfd73148cd7e867bd7d0448f75f45c5d3c&v=4" width = "200" />](https://github.com/Scotth72) |
| Data Scientist | Data Scientist | Back-End Developer | Front-End Developer | Front-End Developer |
|[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/RobDBennett) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/popkdodge) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/royeradames) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/bikesh-maharjan) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Scotth72) |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/robdbennett-tech/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/sasana-kongjareon-2618281a6/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/royer-adames/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/bikeshmaharjan91/) |  [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/heath-l-scott/) |            

<br>

## Deployed Product
- Front-End Deployment- This is the user version for the current product deployment.
https://d-fe.humanrightsfirst.dev/
- Back-End App- This is the back end app that pulls from the DS API and wires into the front-end. However, there isn't a splash page.
https://hrf-d-api.herokuapp.com/
- Data-Science API- This is the API that pulls from the various data sources, cleans/shapes the data, and reports various visualizations.
http://hrf-ds16.eba-fmbjvhg4.us-east-1.elasticbeanstalk.com/#/

## Linked Repos
- Front-End Repo- This repo contains all of the documentation and files for the front end deployment
https://github.com/Lambda-School-Labs/human-rights-first-d-fe
- Back-End Repo- This repo contains all of the documentation and files for the back end deployment
https://github.com/Lambda-School-Labs/human-rights-first-d-be
- Data-Science Repo- This repo contains all of the documentation and files for the data science api deployment
https://github.com/Lambda-School-Labs/human-rights-first-d-ds

## Getting Started (DS)
Our team inherited several notebooks along with a partially functional DS API. While things were wire correctly, some of the data displayed was 'dummy'. There was a NLP model that wasn't properly pickled. The DS API also was theoretically wired with the NLP model, but it wasn't reporting anything beyond the base scaffolding. The primary endpoint that functioned was getdata.py. There were also a few mis-wired APIs- the PRAW Reddit API for instance was buggy so that it could only pull a single instance rather than 100 or 1000. This difficulty was further complicated when the API did nothing with them anyway, so there was no way to have the end user update the data/database.
While there was a fair amount of documentation within the body of the app files, the README and layout was lackluster at best.

All historical documentation and artifacts can be found in the labs27 labeled folders.

With these items in hand, we were instructed to follow the Product Vision Document to create a better product, found [here](https://www.notion.so/Human-Rights-First-Roadmap-Labs-28-4725bc357588498587902fed9d9b78c5)

The layout of this repo is fairly straightforward. Anything labeled with a 28 is the most up-to-date example of the item in question. The labs28_notebooks contains some python notebooks detailing how we expored various APIs, model deployments or soft-coded something before adding it to the app's framework properly. You should familiarize yourself with all of the files within the project folder as this is the functional code for the application we wrote. The Docker files might not be necessary, depending on how you deploy your Docker and AWS. They are left for reference. Within this folder you will find the App folder, and the primary file within that is the Main.py file. 

Main.py is the framework for the endpoints. Take a minute to familiarize yourself with the various endpoints and how they are structured. You will want to change the title to reflect your team and lab cohort. Also bear in mind the various imports; most of these are important to either the FastAPI framework or the various endpoints themselves. You can keep what you need, add new endpoints, and delete what doesn't interest you.

Within the App folder is the API folder that has a variety of files reflecting the various endpoints that main imports. Some of these we didn't use, like viz and can be safely deleted. Not all of these files are pulled into main; some are pulled into other files within this folder. The bulk of the work we did is reflected in this folder and likely will be the case for you as well. It is strongly recommended that you familiarize yourself with the individual components before deleting or altering these files. At present, some of the endpoints that DS produced did not make it into final production, such as the top_x_list. These endpoints operate as intended, the front-end team just got a bit behind towards the end. We have tried to keep the naming convention consistent so that the file represents the visualization and router calls.

In order to get your own files up and running, you will need to clone the repo, make a cosmetic change to the main file (just changing the name is enough at this stage), and try to run the files locally. You may need to debug something, depending on your local enviornment, or install needed libraries. If it runs locally,  you should follow the documentation provided by Ryan Herr regarding local Docker deployment. There is also a step-by-step guide for deploying to AWS. Once you have Docker deploying correctly, and it is uploaded to AWS, doing further updates is trivial. 

Ryan Herr's guide can be found [here](https://docs.labs.lambdaschool.com/data-science/)

## Tech Stack Used (DS)
fastapi==0.61.1
pandas==1.1.3
plotly==4.12.0
pytest==6.1.1
requests==2.24.0
uvicorn==0.12.2
geopy==2.0.0
geopandas==0.8.1

Optional for historical use-
praw==7.1.0
python-dotenv==0.14.0
beautifulsoup4==4.9.1
scikit-learn==0.23.2
spacy==2.3.2
newspaper3k==0.2.8
fastapi-utils==0.2.1

Within the core application, you will need FastAPI, Pandas, Plotly, Uvicorn, Geopy and Geopandas. Depending on how you structure you own API interface, you may require requests as well.

Pandas is used to shape data into dataframes and clean it easily. Ploty is the primary enginge for our visualization generation (the front end will be using Plotly for React). Uvicorn is to run the app locally. Geopy and Geopandas is necessary for the geocoding that we did so that the various graphs could be plotted on a map of the US. 

We have also included the libraries that previous labs used  with their pickled models. We found the data to be woefully small for accurate ML algorithms, but your source may be better. PRAW is used to wire into the Reddit API. Python-dotenv is used to hide passwords within an .env file (this was unncessary for our deployment as none of our material was sensetive in nature). Beautiful Soup, Spacy, and Newspaper3k are all necessary for NLP modeling to tokenize/lemma the data and then scikit-learn and fastapi-utils is needed to create the specific models as well. 

## User Flows 
The user goes to the front-end website. They are greeted with the non-lethal incidents data. There are two graphs. The left-most graph is the progression of incidents over time. The play button should automatically advance time, but you can also drag the slider to a specific date. Each point will populate on the map with details and a clickable link to the stories they are associated with.

The right-most graph is a line graph with the same information, but displayed over time to easy show spikes of activity.
![User1](/screenshots/User-Flow1.JPG)

Along the top of the screen you will have a few tabs. Clicking on the 'Incidents of Killing' tab will give you the second batch of graphs.
On this screen the user should see four graphs. The upper left graph is a map of the US with historical data of police lethal use of force, including off-duty incidents. The default filter is for the full time of the data, but there is a filter tab on the upper right that will allow the user to dial in on the specific timeframe they wish to see displayed. On the US map, each point is a specific instance that can be hovered over for more data. The map can zoom and pan effectively, and each datapoint is represented as close to the address that it occured as possible.

The upper-right graph is a bar graph displaying the different states with their number of incidents. This data has been normalized so that the population of the state is taken into account with the number of incidents. The purpose of this is to illustrate that the general public tends to associate police use of force with big cities, but the extremely troubling trend is that more rural areas like New Mexico have a substantively higher lethal force per capita.

The lower-left graph is a breakdown of the victim's race displayed on a pie-chart.

The lower-right graph is the breakdown of the national racial demographics for the US to illustrate differences in lethal force.
![User2](/screenshots/User-Flow2.JPG)

The final user option is to go to the About page, which has some information regarding the Human Rights First organization.
![User3](/screenshots/User-Flow3.JPG)

## Architecture
The flow for visualizations and descriptions between the user and the back end are detailed below.

![FE-Wire](/screenshots/Front-End-Wire-Frame.JPG)

The base architecture for the Data-Science API is displayed below.
![DS-Wire](/screenshots/DS-Wire-Frame.JPG)

- Describe the file hierarchy and where to find things (BE, FE, or DS specific)

## Updates To Repo in Labs 28 (DS)
A variety of files were added in the project/app/api folder to allow the DS team to generate the graphs rather than the front-end. US_bar, US_Demo_pie, US_map, US_Non_lethal and so forth relate directly to end points we generated for back/front end use. 

The Labs28 notebook has most of our notes and test code to access APIs or test model theory. 

Main.py in the project/app folder was extensively changed to add the 6 additional endpoints we required. 

A folder named 'screenshots' has been added to allow ease of use of this README file. These will need to be altered to reflect whatever team's progress or projection if they differ from ours.

The folder entitled data sources is a historical folder with the previous team's collective data. Most of this was largely unnecessary as we could pull from various APIs in real time. However, it is included here for posterity.

## End Points (DS)
us_demo_pie - This returns racial breakdown by state. Default is 'US' which returns the national breakdowns.

us_map - This returns the US map graph populated with incidents based on filter selection. Can select Armed/Unarmed, Demographic (racial), Gender, as well as date ranges. Default is Demographic with full time range.

us_bar - This shows a bar graph of demographic information by filter. Can select State, National, Zipcode, or City. Normalizes data for incidents to population. Default is National.

us_pie_vic - This shows a pie chart of the demographic information of the victims within a given time range. Can select States, National, Zipcode, City, and sort by Geography, Body Camera, Alleged Threat Level, Symptoms of mental illness, Unarmed/Did Not Have an Actual Weapon, Alleged Weapon, Victim's gender, Victim's race. Defaults to National, full time range, and Victim's Race.

us_non_lethal - This shows a US map of non-lethal incidents drawn from social media sources. There is a 'play' button on the graph that automatically advances time and displays only the incidents on that date. The slider can also be dragged to specific location. Map can zoom; each incident has clickable link to story it relates to. This is a GET request- there is no filter to select.

us_non_lethal_line - This shows a line graph of the non-lethal data over the timerange of the found data. Hovering over the line gives a link to each incident. This is a GET request- there is no filter to select.

top_x_list - This returns the highest frequency of incidents filtered by Police Violence or Killings, State or City, and the top X of the specified filters where X is the value you wish to see. Example- Selecting Killings, State, 5 will give you the 5 states with the highest killings in the given data.


## Issues (BE, FE, or DS specific)
* The Front-End wasn't able to fully deploy the filter functions for the US_Demo_Pie, US_pie_vic, us_map, and US_bar graphs. The DS endpoints have a lot of depth that was never fully utilized. It is possible that these filters could be added in the future to allow for greater graph returns.

## Future Features (DS)
* Twitter API (Tweepy) deployment. Due to time constraints, we weren't able to successfully wire into this API.

* NLP Model to successfully detect posting about police use of force.

* AWS Database to store cleaned data or collected social media postings. This wasn't necessary with our build given the relatively small datasets, but would be necessary for any widespread API useage.

Other Links-
[Police_Shooting_Prediction_APP](https://github.com/RobDBennett/DS-Unit-2-Build-Week)

[Rob's Production Blog](http://robdbennett.com/2020-11-20-Tracking-Police-Use-Of-Force/)

## Support (DS)
For advise understanding this project, questions about the code, or concerns about our approach, please contact the following-
| [Rob Bennett](https://github.com/RobDBennett) | [Sasana Kongjareon](https://github.com/popkdodge) |

All necessary information to send us messages should be included in the Contributor's section of this ReadMe.

