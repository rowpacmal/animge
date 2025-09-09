# Standard
from contextlib import asynccontextmanager
import asyncio
import sys

# Third-party
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_200_OK
import uvicorn

# Local
from app.routes import images_router, models_router
from app.schemas import ApiResponse


# Initialize FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup
    print("Starting Animge API...")
    app.state.api_lock = asyncio.Lock()
    app.state.pipeline = None

    yield

    # On shutdown
    print("Shutting down Animge API...")
    del app.state.api_lock
    del app.state.pipeline


app = FastAPI(
    lifespan=lifespan,
    title="Animge API",
    version="1.0",
    description="AI text-to-image generation API for Animge",
)


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


# API Router
api_router = APIRouter(prefix="/api/v1")


# API Endpoints
@api_router.get("/", response_model=ApiResponse, status_code=HTTP_200_OK)
def root(request: Request):
    return ApiResponse(
        message="Welcome to Animge API v1",
        data=None,
    )


# Include routers
api_router.include_router(images_router)
api_router.include_router(models_router)
app.include_router(api_router)


def main():
    port = 8000

    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8000.")

    uvicorn.run("run:app", host="127.0.0.1", port=port)


if __name__ == "__main__":
    main()
