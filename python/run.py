# Standard libraries
from contextlib import asynccontextmanager

# Third-party libraries
from accelerate import Accelerator
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware

# Local application imports
from app.routes import downloads_router, pipelines_router


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
    description="AI text-to-image generation API for Animge",
)


# API Router
api_router = APIRouter(prefix="/api/v1")


# CORS
origins = [
    "http://localhost:5123",  # frontend dev server
    "http://127.0.0.1:5123",
    "http://localhost:8000",  # allow same-origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Endpoints
@api_router.get("/")
def root(api: Request):
    return {"detail": "Welcome to Animge API v1"}


# Include routers
api_router.include_router(downloads_router)
api_router.include_router(pipelines_router)
app.include_router(api_router)
