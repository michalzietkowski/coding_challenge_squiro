import base64


async def demask_and_stream(response_generator, detector):
    buffer = ""
    async for chunk in response_generator:
        buffer += chunk
        while " " in buffer:  # Check for complete words
            word, buffer = buffer.split(" ", 1)
            demasked_word = detector.demask_data(word) + " "
            yield demasked_word
    # Yield any remaining data if no space detected at the end
    if buffer:
        yield detector.demask_data(buffer)


def base_64_encoding(text):
    return str(base64.b64encode(text.encode("utf-8")).decode("utf-8"))
