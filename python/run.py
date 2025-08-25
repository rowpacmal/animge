# Third-party libraries
from fastapi import FastAPI, APIRouter

# Local application imports
from app.routes import models_router


# Initialize FastAPI
app = FastAPI(
    title="Animge API",
    version="1.0",
    description="AI text2img/img2img generation API for Animge",
)

# API Router
api_router = APIRouter(prefix="/api/v1")


# API Endpoints
@api_router.get("/")
async def root():
    return {"message": "Welcome to Animge API v1"}


# Include routers
api_router.include_router(models_router)
app.include_router(api_router)
