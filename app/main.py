from typing import Final

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .routers import routers_list


app: Final[FastAPI] = FastAPI()

for router in routers_list:
    app.include_router(router)

templates: Final[Jinja2Templates] = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> HTMLResponse:
    """
    Root path of the application.

    :param request: Request.
    :return: HTMLResponse.
    """
    return templates.TemplateResponse("index.html", {"request": request})
