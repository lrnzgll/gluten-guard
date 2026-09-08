from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
       return {"status": "ok"}

@app.get("/items")
def list_items():
       return [
           {"id": 1, "name": "Beispiel A", "preis": 9.99},
           {"id": 2, "name": "Beispiel B", "preis": 19.99},
       ]
