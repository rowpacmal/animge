# Standard libraries
from contextlib import asynccontextmanager

# Third-party libraries
from accelerate import Accelerator
from fastapi import FastAPI, APIRouter, Request

# Local application imports
from app.routes import downloads_router, models_router


# Initialize FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup
    print("App starting...")
    accelerator = Accelerator()
    app.state.accelerator = accelerator
    app.state.device = accelerator.device
    app.state.pipe = None

    yield

    # On shutdown
    print("App shutting down...")


app = FastAPI(
    lifespan=lifespan,
    title="Animge API",
    version="1.0",
    description="AI text2img/img2img generation API for Animge",
)


# API Router
api_router = APIRouter(prefix="/api/v1")


# API Endpoints
@api_router.get("/")
def root(api: Request):
    return {**vars(api.app.state), "detail": "Welcome to Animge API v1"}


# Include routers
api_router.include_router(downloads_router)
api_router.include_router(models_router)
app.include_router(api_router)
