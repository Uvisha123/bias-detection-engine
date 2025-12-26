from fastapi import FastAPI
from app.routes.analyze import router

app = FastAPI(title="Bias Detection Engine")

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(router)