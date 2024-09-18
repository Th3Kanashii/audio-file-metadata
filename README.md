# AudioFile Metadata

This project is a FastAPI-based web application that allows users to upload *.mp3 and *.wav audio files by automatically extracting their metadata. It also provides an interface to display uploaded files and their information, including duration and tags.

## System dependencies

- Python 3.8+
- make
- hatch

## Deployment

**Clone the repository**

    git clone https://github.com/Th3Kanashii/audio-file-metadata.git

**Install dependencies and run application**
    
    make install
    make run

## Development

### Setup environment

    make dev

## Used technologies

- [FastAPI](https://fastapi.tiangolo.com/) (Web framework)
- [Mutagen](https://mutagen.readthedocs.io/en/latest/) (Handle audio metadata)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) (Templating engine)
- [Uvicorn](https://www.uvicorn.org/) (Web server)
