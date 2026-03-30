import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import settings
from app.database import engine
from app.models.lead import Lead  # noqa: F401  (needed for metadata.create_all)
from app.database import Base
from app.routers import leads, enrich, geo, export, db_leads

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Apollo Lead Extraction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads.router)
app.include_router(enrich.router)
app.include_router(geo.router)
app.include_router(export.router)
app.include_router(db_leads.router)

# Determine the frontend directory (sibling to backend/)
# Main project root is two levels up from this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# Mount frontend directory to /static
# This handles files like /static/src/App.jsx
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def serve_frontend():
    """Serve the main index.html for the frontend root."""
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
