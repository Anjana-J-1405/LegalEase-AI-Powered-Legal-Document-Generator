from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

app = FastAPI()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    doc_type: str
    parties: str
    terms: str
    dates: str

@app.post("/generate")
def generate_doc(req: DocumentRequest):
    try:
        content = generator.generate_document(
            doc_type=req.doc_type,
            parties=req.parties,
            terms=req.terms,
            dates=req.dates
        )
        return {"status": "success", "content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
