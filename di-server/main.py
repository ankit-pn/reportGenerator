from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json
import os
from telegram_bot.send_message import send_file_to_telegram_bot
from dataIndexerReport.generate_report import generate_pdf


app = FastAPI()

class Notification(BaseModel):
    audios: int
    current_date: str
    current_time: str
    images: int
    links: int
    messages: int
    textMessages: int
    total_documents_processed: int
    videos: int

@app.post("/notify")
async def notify(notification: Notification):
    try:
        # Parse the date and time from the notification
        current_date = notification.current_date
        current_time = notification.current_time.split(" ")[-1].replace(":", "-")

        # Create the filename based on the current date and time
        filename = f"json_{current_date}_{current_time}.json"
        directory = "../dataIndexerReport/data"
        filepath = os.path.join(directory, filename)

        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Save the notification data to a JSON file
        with open(filepath, "w") as file:
            json.dump(notification.dict(), file, indent=4)

        response = send_file_to_telegram_bot()
        print(response)
        return {"message": "Notification saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the app, use the following command: uvicorn main:app --host 0.0.0.0 --port 8813 --reload