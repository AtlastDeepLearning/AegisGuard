from fastapi import APIRouter

ids_router = APIRouter()

@ids_router.get("/")
def read_ids_status():
    return {"module": "Sentinet", "status": "Monitoring Traffic"}