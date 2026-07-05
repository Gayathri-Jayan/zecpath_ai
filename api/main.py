from fastapi import FastAPI
from fastapi import FastAPI

from api.routes.resume_routes import router as resume_router

from api.routes.ats_routes import router as ats_router

app = FastAPI()

app.include_router(resume_router)

app.include_router(ats_router)

app = FastAPI(
    title="Zecpath ATS API"
)

@app.get("/")
def home():

    return {
        "message": "Zecpath ATS API Running"
    }