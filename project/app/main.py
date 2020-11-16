from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, us_map, us_bar, us_demo_pie, us_pie_vic, us_non_lethal, us_non_lethat_line, top_x_list

app = FastAPI(
    title='HRF-TEAM-D-Lab28 DS API',
    description='The ultimate api for Data Visualization',
    version='0.5',
    docs_url='/',
)
app.include_router(us_demo_pie.router)
app.include_router(us_map.router)
app.include_router(us_bar.router)
app.include_router(us_pie_vic.router)
app.include_router(us_non_lethal.router)
app.include_router(us_non_lethat_line.router)
app.include_router(top_x_list.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
