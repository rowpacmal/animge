# Standard libraries
from pathlib import Path
import asyncio
import threading

# Third-party libraries
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from huggingface_hub import snapshot_download
from platformdirs import user_documents_dir

from app.schemas import DownloadModelRequest


downloads_router = APIRouter(prefix="/downloads", tags=["downloads"])
download_model_router = APIRouter(prefix="/model")


@downloads_router.get("/")
def list_downloads():
    return ["model"]


@download_model_router.post("/")
async def download_model(req: DownloadModelRequest, api: Request):
    async def event_stream():
        loop = asyncio.get_event_loop()
        queue: asyncio.Queue = asyncio.Queue()

        documents = Path(user_documents_dir())
        cache_dir = documents / "Animge" / "models"
        cache_dir.mkdir(parents=True, exist_ok=True)

        def run_download():
            model_path = snapshot_download(
                repo_id=req.repo_id, cache_dir=str(cache_dir)
            )
            api.app.state.pipelines[req.repo_id] = model_path
            loop.call_soon_threadsafe(queue.put_nowait, f"DONE:{req.repo_id}")

        threading.Thread(target=run_download, daemon=True).start()

        # Send "STARTED" first
        await queue.put(f"STARTED:{req.repo_id}")

        while True:
            progress = await queue.get()
            yield f"data: {progress}\n\n"
            if progress.startswith("DONE"):
                break

    return StreamingResponse(event_stream(), media_type="text/event-stream")


downloads_router.include_router(download_model_router)
