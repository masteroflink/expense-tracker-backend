from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World peen!"}
