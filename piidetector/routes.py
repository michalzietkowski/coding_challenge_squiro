from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from piidetector.chat_handler import chat_handler
from piidetector.detector import Detector
from piidetector.helpers import demask_and_stream
from piidetector.models import InputData

router = APIRouter()


@router.post("/generate-answer")
async def generate_answer(input_data: InputData) -> StreamingResponse:
    detector = Detector()
    masked_prompt, masked_context = detector.process(input_data)

    generator = chat_handler.ask_question(masked_prompt, masked_context)

    return StreamingResponse(
        demask_and_stream(generator, detector), media_type="text/plain"
    )
