import io
from typing import Annotated, Any, Final

from fastapi import APIRouter, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

from app.enums import Audio


router: Final[APIRouter] = APIRouter()

templates: Final[Jinja2Templates] = Jinja2Templates(directory="app/templates")


@router.post("/upload-audio/", response_class=HTMLResponse)
async def upload_audio(request: Request, file: Annotated[UploadFile, File(...)]) -> HTMLResponse:
    """
    Upload an audio file.

    :param file: The audio file to upload.
    :return: The uploaded audio file.
    """
    if file.content_type not in {Audio.MP3, Audio.WAV}:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "File must be an MP3 or WAV."},
        )

    file_contents: bytes = await file.read()

    metadata: dict[str, Any] | None = None
    audio_file: MP3 | WAVE | None = None

    if file.content_type == Audio.MP3:
        audio_file = MP3(io.BytesIO(file_contents))

    elif file.content_type == Audio.WAV:
        audio_file = WAVE(io.BytesIO(file_contents))

    if (audio_file is None) or (audio_file.tags is None):
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "Metadata not found."},
        )

    metadata = {tag: str(audio_file.tags[tag]) for tag in audio_file.tags}

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "success": f"File '{file.filename}' uploaded successfully!",
            "duration": f"{audio_file.info.length:.2f}",
            "metadata": metadata,
        },
    )
