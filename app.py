from fastapi import FastAPI, File
from uvicorn import run as app_run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
from helmet.constants import APP_HOST, APP_PORT
from helmet.pipeline.train_pipeline import TrainPipeline
from helmet.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@pp.get("/train")
async def training():
    try:
        train_pipeleine = TrainPipeline()
        train_pipeleine.run_pipeline()

        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred!{e}")
