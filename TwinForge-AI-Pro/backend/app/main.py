from fastapi import FastAPI

app = FastAPI(title="TwinForge AI")

@app.get("/")
def root():
    return {"message": "TwinForge AI Backend Running"}
