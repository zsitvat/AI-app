
from fastapi import FastAPI
from dotenv.main import load_dotenv, find_dotenv
import os
import uvicorn

from services.logger.logger import LoggerService
from .config import Config


def create_app():
    load_dotenv(find_dotenv())
    app = FastAPI()

    app.include_router()

    LoggerService().setup_logger(Config.LOG_LEVEL)
    

    return app

app = create_app()

if __name__ == "__main__":
     uvicorn.run("app:app", reload=True, port=Config.PORT, host="0.0.0.0")