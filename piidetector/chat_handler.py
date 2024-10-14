import asyncio
import os
from typing import AsyncIterator

from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


class ChatHandler:
    def __init__(self):
        self.open_ai_key: str = os.environ.get("OPENAI_API_KEY")
        self.callback = AsyncIteratorCallbackHandler()
        self.llm = ChatOpenAI(
            model_name="gpt-4",
            temperature=0.0,
            streaming=True,
            callbacks=[self.callback],
        )

    async def ask_question(self, query: str, context: str) -> AsyncIterator[str]:
        messages = []

        if context:
            messages.append(SystemMessage(content=f"Context: {context}"))

        messages.append(HumanMessage(content=query))

        task = asyncio.create_task(self.llm.agenerate(messages=[messages]))
        try:
            async for token in self.callback.aiter():
                yield token
        except Exception as e:
            print(f"Caught exception: {e}")
        finally:
            self.callback.done.set()
        await task


chat_handler = ChatHandler()
