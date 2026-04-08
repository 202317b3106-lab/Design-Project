
from fastapi import FastAPI

app = FastAPI(title="Smart Release Intelligence Hub")

@app.get("/")
def health_check():
    return {"status": "Backend running"}
