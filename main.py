from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from pypdf import PdfReader
import re
from ai_services import summarize, extract_code 
from vector_db import get_vector_store

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# PDF Processor
def process_pdf(file: UploadFile):
    pdf = PdfReader(file.file)
    text = " ".join([page.extract_text() for page in pdf.pages])
    return text

# Web Scraper
def scrape_url(url: str):
    try:
        response = requests.get(url)
        # Add Readability-like parsing here
        return response.text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"URL Error: {str(e)}")
@app.post("/summarize")
async def api_summarize(text: str):
    return {"summary": summarize(text)}

@app.post("/extract-code")
async def api_extract_code(text: str):
    return {"code": extract_code(text)}

@app.post("/process-input")
async def process_input(file: UploadFile = None, url: str = None, text: str = None):
    if file:
        content = process_pdf(file)
    elif url:
        content = scrape_url(url)
    elif text:
        content = text
    else:
        raise HTTPException(status_code=400, detail="No input provided")
    
    return {"content": content[:5000]}  # Return first 5000 chars for demo

vector_store = get_vector_store()

@app.post("/add-document")
async def add_document(text: str):
    vector_store.add_texts([text])
    return {"status": "success"}

@app.post("/search")
async def semantic_search(query: str):
    results = vector_store.similarity_search(query, k=3)
    return {"results": [doc.page_content for doc in results]}