from fastapi import APIRouter, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


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


@router.get("/register_form", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse(
        {"request": request}, name="components/register_form.html"
    )


@router.get("/toggle_sidenav", response_class=HTMLResponse)
async def toggle_sidenav():
    return """
    <div id="toggle_sidenav" class="ml-24 py-5 w-full absolute">
      <button
            hx-get="/sidenav"
            hx-trigger="click "
            hx-target="#toggle_sidenav"
            hx-swap="outerHTML"
            >
        <svg
          class="h-8 w-8 text-gray-400"
          xmlns="http://www.w3.org/2000/svg"
          height="24px"
          viewBox="0 -960 960 960"
          width="24px"
          fill="#9ca3af"
        >
          <path
            d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm280-80h280v-560H480v560Z"
          />
        </svg>
      </button>
    </div>
    
    """
    
@router.get("/sidenav", response_class=HTMLResponse)
async def sidenav(request: Request):
    return templates.TemplateResponse(
        {"request": request}, name="components/sidenav.html"
    )
