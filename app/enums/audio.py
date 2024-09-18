from enum import Enum


class Audio(str, Enum):
    """
    An enumeration of audio file formats.
    """

    MP3 = "audio/mpeg"
    WAV = "audio/vnd.wave"
