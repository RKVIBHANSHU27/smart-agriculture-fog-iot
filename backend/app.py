from fastapi import FastAPI
from backend.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="Smart Agriculture API",
    version="1.0"
)

app.include_router(router)

app.mount(
    "/assets",
    StaticFiles(directory="backend/dist/assets"),
    name="assets"
)


@app.get("/")
def serve_dashboard():
    return FileResponse(
        "backend/dist/index.html"
    )