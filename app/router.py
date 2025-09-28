import asyncio
import base64
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse


from app.tts import tts_generator

router = APIRouter(prefix="/api")

tts_executor = ThreadPoolExecutor(max_workers=1)
tts_lock = asyncio.Lock()

@router.post("/text")
async def generate_message(text: str):
    try:

        loop = asyncio.get_running_loop()

        async with tts_lock:
            audio_bytes = await loop.run_in_executor(
                tts_executor, tts_generator.generate_tts, text
            )

        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')


        logger.info(f"Успешный ответ пользователю")
        return JSONResponse(content={
            "audio_base64": audio_base64
        })
    except Exception as e:
        logger.error(f"Произошла ошибка при ответе пользователю: {e}")
        raise HTTPException(status_code=500, detail="Ошибка генерации аудио")

router.get("/test")
async def test():
    return "Hello"