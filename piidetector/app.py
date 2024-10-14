import uvicorn
from fastapi import FastAPI
from config import config
from routes import router as generate_answer_router

app = FastAPI()
app.include_router(generate_answer_router)


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=config.SERVICE_HOST,
        port=config.PORT,
        reload=config.IS_DEVELOPMENT,
    )
