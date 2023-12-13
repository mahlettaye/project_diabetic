from fastapi import FastAPI
from .routers import model_router

app = FastAPI()

# Include router from routers directory
app.include_router(model_router.router)