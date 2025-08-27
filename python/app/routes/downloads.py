# Standard libraries
import asyncio
import threading

# Third-party libraries
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from huggingface_hub import snapshot_download

# Local application imports
from app.constants import CACHE_DIR, MODEL_ID
from app.utils import create_pipeline_text_to_image


downloads_router = APIRouter(prefix="/downloads", tags=["downloads"])
download_model_router = APIRouter(prefix="/model")


@downloads_router.get("/")
def list_downloads():
    return ["model"]


@download_model_router.get("/")
async def download_model(request: Request):
    async def event_stream():
        loop = asyncio.get_running_loop()
        queue: asyncio.Queue = asyncio.Queue()

        def run_download():
            try:
                # Download model
                snapshot_download(repo_id=MODEL_ID, cache_dir=str(CACHE_DIR))

                if request.app.state.pipe is None:
                    request.app.state.pipe = create_pipeline_text_to_image(
                        request.app.state.device
                    )

                loop.call_soon_threadsafe(queue.put_nowait, f"DONE")
            except Exception as e:
                # Report error
                loop.call_soon_threadsafe(queue.put_nowait, f"ERROR: {e}")

        threading.Thread(target=run_download, daemon=True).start()

        # Send initial signal
        await queue.put(f"STARTED")

        # Send progress updates
        while True:
            progress = await queue.get()
            yield f"data: {progress}\n\n"
            if progress.startswith("DONE") or progress.startswith("ERROR"):
                break

    # Return streaming response
    return StreamingResponse(event_stream(), media_type="text/event-stream")


downloads_router.include_router(download_model_router)
