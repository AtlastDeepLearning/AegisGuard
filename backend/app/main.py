from fastapi import FastAPI
from backend.app.api.api import api_app_router

# Main application
app = FastAPI(title="AegisGuard API", description="AegisGuard API", version="1.0.0")

# Include the API router
# allows the application to use Modules defined in api.py 
app.include_router(api_app_router, prefix="/api/v1")

@app.get("/")
def read_root(): 
    return {"System Status": "Online"}
