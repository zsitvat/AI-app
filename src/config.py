import os


class Config:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    PORT = os.getenv("PORT", 5000)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
