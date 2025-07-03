import asyncio
import json

from loguru import logger

from config import settings
from extentions.redis_connector.client import RedisConnector
from extentions.redis_connector.enums import TaskEvent
from extentions.redis_connector.schemas import TaskMessage
from extentions.telegram_api.client import TelegramAPI


async def process_message(message: dict) -> None:
    if not message["type"] == "message":
        return

    data = message["data"]
    try:
        data = TaskMessage(**json.loads(data))
        if data.event == TaskEvent.created:
            logger.info(f"New Task created: {data.task.id}:{data.task.title}:{data.task.description}")
        elif data.event == TaskEvent.updated:
            await TelegramAPI().send_message(f"Task ID{data.task.id} is DONE")

    except (ValueError, TypeError):
        logger.error("Invalid message")


async def start_worker() -> None:
    client = RedisConnector(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        channel=settings.REDIS_CHANNEL,
    )
    await client.connect()

    try:
        pubsub = await client.subscribe(settings.REDIS_CHANNEL)

        async for message in pubsub.listen():
            await process_message(message)
    finally:
        await client.disconnect()


if __name__ == "__main__":
    try:
        logger.info("Start worker.")
        asyncio.run(start_worker())
    except KeyboardInterrupt:
        logger.info("Worker interrupted.")
