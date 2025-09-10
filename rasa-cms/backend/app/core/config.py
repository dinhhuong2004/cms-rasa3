import os

class Settings:
    PROJECT_NAME: str = "Rasa CMS"
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB: str = "rasa_cms"
    # JWT_SECRET: str = os.getenv("JWT_SECRET", "supersecret")
    JWT_ALGORITHM: str = "HS256"

settings = Settings()
