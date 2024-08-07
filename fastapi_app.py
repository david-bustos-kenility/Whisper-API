from tempfile import NamedTemporaryFile
from typing import List

import torch
import whisper
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse

DEVICE= "cuda" if torch.cuda.is_available() else "cpu";
model = whisper.load_model("base", device= DEVICE); 

app= FastAPI();


@app.post("/whisper")
async def transcribe_audio(files: List[UploadFile]= File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="At least one file is required");
    
    results=[];
    for file in files:
        with NamedTemporaryFile(delete=True) as temp:
            temp.write(file.file.read());
            result = model.transcribe(temp.name);
            results.append(
                {
                    "filename": file.filename,
                    "transcript": result["text"]
                    }
            );
    return JSONResponse(content={'results':results})

@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"