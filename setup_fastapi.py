from fastapi import FastAPI

app = FastAPI() # app is object

@app.get("/")
def hello():
    return { 'message':'Hello world'}


@app.get('/about')
def about():
    return {'message':'Hi there! My name is hasib'}