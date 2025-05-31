from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionInput(BaseModel):
    question: str
    image: str | None = None  # base64 string, optional

@app.post("/search")
async def search_docs(query: QuestionInput):
    # Dummy logic to simulate RAG
    if "token" in query.question.lower():
        return {
            "answer": "0.0017",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                    "text": "Use the model that’s mentioned in the question."
                }
            ]
        }
    return {
        "answer": "This is a placeholder answer.",
        "links": []
    }
