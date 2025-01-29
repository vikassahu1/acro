from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Mount a static directory to serve PDFs
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates for HTML rendering
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint to serve the PDF (in case you need direct access via URL)
@app.get("/pdf/{filename}")
def get_pdf(filename: str):
    pdf_path = os.path.join("static", filename)
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path)
    return {"error": "File not found"}

