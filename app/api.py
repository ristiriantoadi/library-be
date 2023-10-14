from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config.mongo_collection import ADMIN
from controllers.admin.init import init_admin
from controllers.util.crud import find_on_db
from models.test import TestInput
from models.util.errors import BadRequestException
from routes.account.admin_account import route_admin_account
from routes.book.admin_book import route_admin_book
from routes.borrowing.admin_borrowing import route_admin_borrowing
from routes.fee.admin import route_admin_fee
from routes.member.admin_member import route_admin_member

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


@app.delete("/test_insert_data")
async def test_insert_data(input: TestInput):
    # raise HTTPException(status_code=400, detail="Something else")
    return input


@app.delete("/test_delete_data")
async def test_delete_data():
    return {"something": "deleted"}


app.include_router(route_admin_account)
app.include_router(route_admin_book)
app.include_router(route_admin_member)
app.include_router(route_admin_borrowing)
app.include_router(route_admin_fee)
