from __future__ import annotations

from io import BytesIO
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from fastapi.testclient import TestClient

import pytest
from pydub import AudioSegment


@pytest.fixture
def valid_mp3_file() -> BytesIO:
    """
    Fixture to create a valid MP3 file.
    
    :return: BytesIO.
    """
    audio = AudioSegment.silent(duration=1000)
    output = BytesIO()
    audio.export(output, format="mp3")
    output.seek(0)
    output.name = "test.mp3"
    return output


@pytest.fixture
def valid_wav_file() -> BytesIO:
    """
    Fixture to create a valid WAV file.

    :return: BytesIO.
    """
    audio = AudioSegment.silent(duration=1000)
    output = BytesIO()
    audio.export(output, format="wav")
    output.seek(0)
    output.name = "test.wav"
    return output


def test_upload_valid_mp3(client: TestClient, valid_mp3_file: BytesIO) -> None:
    """
    Test uploading a valid MP3 file.

    :param client: fixture to test the FastAPI application.
    :param valid_mp3_file: fixture to create a valid MP3 file.
    """
    response = client.post(
        "/upload-audio/",
        files={"file": valid_mp3_file},
    )
    assert response.status_code == 200


def test_upload_valid_wav(client: TestClient, valid_wav_file: BytesIO) -> None:
    """
    Test uploading a valid WAV file.

    :param client: fixture to test the FastAPI application.
    :param valid_wav_file: fixture to create a valid WAV file.
    """
    response = client.post(
        "/upload-audio/",
        files={"file": valid_wav_file},
    )

    assert response.status_code == 200


def test_upload_invalid_file_type(client: TestClient) -> None:
    """
    Test uploading an invalid file type.

    :param client: fixture to test the FastAPI application.
    """
    invalid_file = BytesIO(b"not an audio file")
    invalid_file.name = "test.txt"
    response = client.post(
        "/upload-audio/",
        files={"file": invalid_file},
    )
    assert response.status_code == 200


def test_upload_no_file(client: TestClient) -> None:
    """
    Test uploading no file.

    :param client: fixture to test the FastAPI application.
    """
    response = client.post("/upload-audio/")
    assert response.status_code == 422
