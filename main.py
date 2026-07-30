from fastapi import Body, FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World!!"}

@app.get("/posts")
async def  get_posts():
    return {"post" : 5}

@app.post("/createposts")
async def create_posts(payload: dict = Body(...)):
    return {"new post" : f"title is {payload["title"]} {payload["content"]}" }

