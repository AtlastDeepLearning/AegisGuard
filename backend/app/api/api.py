from fastapi import APIRouter
from app.api.endpoints import phishing, ids

# This is the main router that collects all the smaller routers from diffrent modules below
api_app_router = APIRouter()

# Phishing module
api_app_router.include_router(phishing.router, prefix = "/phishing", tags = ["Phishing Email detection"])

# IDS module
api_app_router.include_router(ids.router, prefix = "/ids", tags = ["Intrusion Detection system"])
