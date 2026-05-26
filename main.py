from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Lead(BaseModel):
    name: str
    email: str
    cart_total: float
    country: str
    source: str

@app.post("/score-lead")
def score_lead(lead: Lead):
    score = 0
    
    if lead.cart_total >= 500:
        score += 50
    elif lead.cart_total >= 200:
        score += 30

    if lead.country == 'Nigeria':
        score += 20

    if lead.source == 'Paid Ad':
        score += 15
    elif lead.source == 'Organic':
        score += 5

    return {"email": lead.email, "priority_score": score}