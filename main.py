from fastapi import FastAPI
app = FastAPI(title="ENAGA Pay")
@app.get("/health")
def health():
    return {"status": "ok", "service": "enaga-pay"}

