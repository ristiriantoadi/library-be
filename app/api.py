from fastapi import FastAPI

from config.mongo_collection import TESTS

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/test_insert")
async def read_root():
    await TESTS.insert_one({"test": "work"})
