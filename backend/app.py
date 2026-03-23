from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
import traceback
from data_store import uploaded_data

from query_parser import parse_query
from data_processor import process_data
from context_manager import update_context, get_context
from export_utils import generate_csv

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str
    session_id: str

# 🚀 QUERY
@app.post("/query")
def handle_query(request: QueryRequest):
    try:
        context = get_context(request.session_id)
        structured_query = parse_query(request.query, context)
        update_context(request.session_id, structured_query)
        result = process_data(structured_query, request.query)

        return {"structured_query": structured_query, "result": result}

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

# 📥 UPLOAD CSV
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        path = f"sample_data/{file.filename}"

        with open(path, "wb") as f:
            f.write(await file.read())

        dataset_name = file.filename.split(".")[0]
        uploaded_data["current"] = dataset_name

        df = pd.read_csv(path)

        return {
            "message": "Uploaded successfully",
            "dataset": dataset_name,
            "columns": df.columns.tolist()
        }

    except Exception as e:
        return {"error": str(e)}

# 📤 EXPORT CSV
@app.post("/export")
def export_csv(data: dict):
    file = generate_csv(data)
    return {"file": file}

@app.get("/")
def home():
    return {"status": "running"}