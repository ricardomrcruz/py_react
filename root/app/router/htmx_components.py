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
async def dropdown_feat():
    return """
    <div
    class=" border-b border-neutral-800 p-2"
    hx-trigger="mouseleave from:body"
    hx-target="#dropdown"
    hx-swap="innerHTML"
    hx-get="/empty-dropdown">
        <ul class="w-[70%] flex flex-wrap items-center justify-center gap-8 mx-auto">
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Market Data</a
                >
            </li>
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Upcoming releases</a
                >
            </li>
        </ul>
    </div>
    """


@router.get("/dropdown-about", response_class=HTMLResponse)
async def dropdown_about():
    return """
    <div
    class=" border-b border-neutral-800 p-2"
    hx-trigger="mouseleave from:body"
    hx-target="#dropdown"
    hx-swap="innerHTML"
    hx-get="/empty-dropdown">
        <ul class="w-[70%] flex flex-wrap items-center justify-center gap-8 mx-auto">
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Who are we?</a
                >
            </li>
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Contact Us</a
                >
            </li>
        </ul>
    </div>
    """


@router.get("/empty-dropdown", response_class=HTMLResponse)
async def empty_dropdown():
    return ""