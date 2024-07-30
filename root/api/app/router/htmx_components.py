from fastapi import APIRouter, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated

router = APIRouter()

templates = Jinja2Templates(directory="api/app/templates")


@router.get("/test", response_class=HTMLResponse)
async def index2(request: Request, hx_request: Annotated[str | None, Header()] = None):
    films = [
        {"name": "Blade Runner", "director": "Ridley Scott"},
        {"name": "Inception", "director": "Christopher Nolan"},
        {"name": "The Matrix", "director": "Lana Wachowski"},
        {"name": "Pulp Fiction", "director": "Quentin Tarantino"},
    ]
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("components/table.html", context)
    return templates.TemplateResponse("index3.html", context)


@router.get("/dropdown-feat", response_class=HTMLResponse)
async def dropdown_feat(request: Request):
    return templates.TemplateResponse(
        {"request": request}, name="partials/dropdown-feat.html"
    )


@router.get("/dropdown-about", response_class=HTMLResponse)
async def dropdown_about(request: Request):
    return templates.TemplateResponse(
        {"request": request}, name="partials/dropdown-about.html"
    )


@router.get("/empty-dropdown", response_class=HTMLResponse)
async def empty_dropdown():
    return ""

@router.get("/empty", response_class=HTMLResponse)
async def empty():
    return ""


@router.get("/register_form", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse(
        {"request": request}, name="components/register_form.html"
    )


@router.get("/toggle_sidenav", response_class=HTMLResponse)
async def toggle_sidenav(request:Request):
    return templates.TemplateResponse(
        {"request": request}, name="partials/toggle-sidenav.html"
)
    
@router.get("/recent_search", response_class=HTMLResponse)
async def toggle_sidenav(request:Request):
    return templates.TemplateResponse(
        {"request": request}, name="partials/recent-search.html"
)
    
@router.get("/sidenav", response_class=HTMLResponse)
async def sidenav(request: Request):
    return templates.TemplateResponse(
        {"request": request}, name="components/sidenav.html"
    )
