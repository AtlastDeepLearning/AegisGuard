from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Routes input data to phishing.py then gives out output data to api.py
phishing_router = APIRouter()

class EmailRequest(BaseModel):
    subject: str
    sender: str
    body: str
    urls: Optional[List[str]] = []
    attachments: Optional[List[str]] = []

class PhishingDetectionResult(BaseModel):
    risk_level: str 
    confidence: float
    reason: str
    

@phishing_router.get("/")
def phishing_status():
    return {"module": "Phishguard", "status": "Online, ready to detect phishing emails"} 

@phishing_router.post("/analyze")
def detect_phishing(email: EmailRequest):
    # Placeholder for ML model (To be implemented)
    risk = "safe"
    confidence = 0.0
    reason = "Email is safe to open"
    # Simple keyword check 
    suspicious_keywords = ["urgent", "verify account", "password cxpiration", "bank"]
    if any(keyword in email.body.lower() for keyword in suspicious_keywords):
        risk = "Suspicious"
        confidence = 0.75
        reason = "Detected urgency language typical of phishing."
    return PhishingDetectionResult(
        risk_level=risk,
        confidence=confidence,
        reason=reason
    )
    
