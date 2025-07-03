from aiohttp import ClientSession

from config import settings


class TelegramAPI:
    def __init__(self):
        self.token = settings.TG_BOT_TOKEN
        self.chat_id = settings.TG_LOG_CHAT_ID

    async def send_message(self, message: str) -> None:
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
        }

        async with ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if not response.ok:
                    raise Exception(f"Telegram API error: {await response.text()}")
