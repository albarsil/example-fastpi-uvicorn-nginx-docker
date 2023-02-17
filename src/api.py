# This is the file that implements a flask server to do inferences

import logging
import os
import sys
from fastapi import FastAPI
import dto

# Create logger
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
logger = logging.getLogger()

# The flask app for serving predictions
app = FastAPI()
prefix = "/opt/app/"

@app.get("/")
async def root():
    return {"message": "Hello world!"}

@app.get("/ping")
async def health():
    return {"message": "Hello world!"}

@app.post("/test")
async def test(req: dto.ModelTestRequest):
    return {"message": req.text}
