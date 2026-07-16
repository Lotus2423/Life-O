from fastapi import FastAPI
app=FastAPI(title='TwinForge AI')

@app.get('/')
def root():
    return {'status':'running'}
