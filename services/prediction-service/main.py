from fastapi import FastAPI
import threading
from app.consumer.consumer import start_consuming

app = FastAPI()

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=start_consuming, daemon=True)  # Usa daemon para que no bloquee shutdown
    thread.start()

@app.get("/")
def root():
    return {"message": "Prediction service running"}
