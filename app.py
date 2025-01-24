import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional, List
from main import run



app = FastAPI()

class InputModel(BaseModel):
    data: Dict[str, Any]

@app.post("/run")
async def run_main_fuct(input_data: InputModel):
    try:
        result = run(input_data.data)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }
