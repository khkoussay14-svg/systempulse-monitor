from pathlib import Path
import platform
import socket

import psutil
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="SystemPulse", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def network_addresses() -> list[dict[str, str]]:
    result = []
    for interface, addresses in psutil.net_if_addrs().items():
        for address in addresses:
            if address.family == socket.AF_INET:
                result.append({"interface": interface, "address": address.address})
    return result


def system_snapshot() -> dict:
    disk_root = "C:\\" if platform.system() == "Windows" else "/"
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "platform_release": platform.release(),
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "cpu_count": psutil.cpu_count(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage(disk_root).percent,
        "network": network_addresses(),
    }


@app.get("/api/system")
def api_system() -> dict:
    return system_snapshot()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
