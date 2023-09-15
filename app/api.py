from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config.mongo_collection import ADMIN
from controllers.admin.init import init_admin
from controllers.util.crud import find_on_db
from models.util.errors import BadRequestException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*", "*"],
    allow_methods=["*", "*"],
    allow_headers=["*", "*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/init_first_admin")
async def init_first_admin():
    # await TESTS.insert_one({"test": "work"})
    admin = await find_on_db(collection=ADMIN, criteria={})
    if admin:
        raise HTTPException(
            status_code=400, detail=BadRequestException.ADMIN_ALREADY_EXIST
        )
    await init_admin()
