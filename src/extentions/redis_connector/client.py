from typing import AsyncGenerator

from redis.asyncio import Redis
from redis.client import PubSub

from config import settings
from database.schemas.task import TaskSchema
from extentions.redis_connector.enums import TaskEvent
from extentions.redis_connector.schemas import TaskMessage


class RedisConnector:
    def __init__(self, host: str, port: int, db: int, channel: str) -> None:
        self.host = host
        self.port = port
        self.db = db
        self.channel = channel
        self._redis_client: Redis | None = None

    async def connect(self) -> Redis:
        if not self._redis_client:
            self._redis_client = Redis(host=self.host, port=self.port, db=self.db, decode_responses=True)

        return self._redis_client

    async def disconnect(self) -> None:
        if self._redis_client:
            await self._redis_client.close()

    async def publish(self, message: str) -> None:
        if not self._redis_client:
            raise ValueError("Redis connection is not initialized")
        await self._redis_client.publish(channel=self.channel, message=message)

    async def subscribe(self, channel: str) -> AsyncGenerator[PubSub, None]:
        if not self._redis_client:
            raise ValueError("Redis connection is not initialized")

        pubsub = self._redis_client.pubsub()
        await pubsub.subscribe(channel)
        try:
            yield pubsub
        finally:
            await pubsub.unsubscribe(channel)
            await pubsub.close()

    @staticmethod
    def build_message(event: TaskEvent, task: TaskSchema) -> str:
        message = TaskMessage(event=event, task=task)
        return message.model_dump_json()


async def redis_client() -> AsyncGenerator[RedisConnector, None]:
    client = RedisConnector(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        channel=settings.REDIS_CHANNEL,
    )
    await client.connect()

    try:
        yield client
    finally:
        await client.disconnect()
