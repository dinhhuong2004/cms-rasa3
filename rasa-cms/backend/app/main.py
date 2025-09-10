from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import intents, auth

app = FastAPI(title="Rasa CMS API")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(intents.router, prefix="/api/v1/intents", tags=["Intents"])
