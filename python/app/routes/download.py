# Standard libraries
import asyncio
import threading

# Third-party libraries
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from huggingface_hub import snapshot_download

# Local application imports
from app.constants import CACHE_DIR, MODEL_ID


downloads_router = APIRouter(prefix="/downloads", tags=["downloads"])
download_model_router = APIRouter(prefix="/model")


@downloads_router.get("/")
def list_downloads():
    return ["model"]


@download_model_router.post("/")
async def download_model(api: Request):
    async def event_stream():
        loop = asyncio.get_event_loop()
        queue: asyncio.Queue = asyncio.Queue()

        def run_download():
            model_path = snapshot_download(repo_id=MODEL_ID, cache_dir=str(CACHE_DIR))
            api.app.state.model_path = model_path
            loop.call_soon_threadsafe(queue.put_nowait, f"DONE:{MODEL_ID}")

        threading.Thread(target=run_download, daemon=True).start()

        # Send "STARTED" first
        await queue.put(f"STARTED:{MODEL_ID}")

        while True:
            progress = await queue.get()
            yield f"data: {progress}\n\n"
            if progress.startswith("DONE"):
                break

    return StreamingResponse(event_stream(), media_type="text/event-stream")


downloads_router.include_router(download_model_router)
