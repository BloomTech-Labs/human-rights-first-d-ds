from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, us_map, us_bar, us_demo_pie, us_pie_vic

app = FastAPI(
    title='HRF-TEAM-D-Lab28 DS API',
    description='The ultimate api for Data Visualization',
    version='0.1',
    docs_url='/',
)
app.include_router(us_demo_pie.router)
app.include_router(us_map.router)
app.include_router(us_bar.router)
app.include_router(us_pie_vic.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
