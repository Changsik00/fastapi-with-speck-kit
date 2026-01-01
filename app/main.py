from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.items import router as items_router
from app.core.errors.http_error_handlers import http_404_handler

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="An example of a FastAPI application following clean architecture principles.",
    version="0.1.0",
)

app.include_router(items_router)
app.add_exception_handler(404, http_404_handler)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Clean Architecture example!"}
