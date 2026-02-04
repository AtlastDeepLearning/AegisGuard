from fastapi import APIRouter
from .endpoints import phishing, ids

# This is the main router that collects all the smaller routers from diffrent modules below
api_app_router = APIRouter()

# Phishing module
api_app_router.include_router(phishing.phishing_router, prefix = "/phishing", tags = ["Phishing Email detection"])

# IDS module
api_app_router.include_router(ids.ids_router, prefix = "/ids", tags = ["Intrusion Detection system"])