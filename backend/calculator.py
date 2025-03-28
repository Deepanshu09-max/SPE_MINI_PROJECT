# calculator.py

import math

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           
    allow_credentials=True,          
    allow_methods=["*"],            
    allow_headers=["*"],            
)

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/sqrt/{x}")
def square_root(x: float):
    return {"result": math.sqrt(x)}

@app.get("/factorial/{x}")
def factorial(x: int):
    return {"result": math.factorial(x)}

@app.get("/ln/{x}")
def natural_log(x: float):
    return {"result": math.log(x)}

@app.get("/power/{x}/{b}")
def power(x: float, b: float):
    return {"result": math.pow(x, b)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
