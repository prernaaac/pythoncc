from fastapi import FastAPI
app = FastAPI()

@app.get("/home")
def home():
    return{"success":True,"message":"Hello Beautiful!!"}

@app.get("/about")
def about():
    return{"Name":"Prerna","Location":"Mumbai"}