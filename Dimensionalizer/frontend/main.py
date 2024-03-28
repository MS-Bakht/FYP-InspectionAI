from fastapi import FastAPI, WebSocket
import cv2
import numpy as np
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    cap = cv2.VideoCapture(0)  # Open the default camera (usually the built-in webcam)

    while True:
        ret, frame = cap.read()  # Read a frame from the camera

        if not ret:
            break

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_data = buffer.tobytes()

        await websocket.send_bytes(frame_data)  # Send the frame to the client

    cap.release()  # Release the camera when done

@app.get("/")
async def read_upload(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
