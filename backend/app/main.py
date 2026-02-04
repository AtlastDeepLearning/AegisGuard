from fastapi import FastAPI

app = FastAPI(title="AegisGuard API", description="AegisGuard API", version="1.0.0")

@app.get("/")
def read_root(): 
    return {"System Status": "Online"}
