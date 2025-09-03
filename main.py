from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
import os
import sys  
# Add the parent directory (i.e., the root directory of your project) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

# Enable frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or "*" during dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
