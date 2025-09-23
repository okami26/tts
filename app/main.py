from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from fastapi import FastAPI, Request
from loguru import logger

from app.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Бот запущен...")
    yield
    logger.info("Бот остановлен...")
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router=router)
