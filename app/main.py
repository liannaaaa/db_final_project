from fastapi import FastAPI
from .routers import athletes, sport_types, results

app = FastAPI()

app.include_router(athletes.router)
app.include_router(sport_types.router)
app.include_router(results.router)
