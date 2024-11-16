import os

class Config:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    PORT = os.getenv("PORT", 5000)

