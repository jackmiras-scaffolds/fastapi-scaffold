from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.responses import RedirectResponse

from app.exceptions.application_exception import ApplicationException
from app.models.error import Error
from configs.constants import Constants
from configs.database import db
from database.seeds.database_seeder import DatabaseSeeder
from routes.api import api

"""
--------------------------------------------------------------------------
 Routes
--------------------------------------------------------------------------

Here you may specify all your router's bootstrap.

"""


app = FastAPI()
app.include_router(api, prefix=Constants.API_V1)


@app.get("/")
async def read_root():
    return RedirectResponse(url=f"{Constants.API_V1}/health")


"""
--------------------------------------------------------------------------
 Exception Handler
--------------------------------------------------------------------------

Here is defined the exception handler convention for the entire application.
It's important that every exception MUST inherit ApplicationException.

"""


@app.exception_handler(ApplicationException)
async def app_exception_handler(self, app_exception: ApplicationException):
    app_exception.log_message()
    content = app_exception.detail()
    status_code = app_exception.status_code()
    return JSONResponse(status_code=status_code, content=content)


@app.exception_handler(ValidationError)
async def pydantic_exception_handler(self, app_exception: ValidationError):
    helps = []
    messages = []
    validation_errors = app_exception.errors()

    for validation_error in validation_errors:
        field = validation_error["loc"][0]
        field_info = app_exception.model.__fields__[field].field_info

        messages.append(field_info.title or field)
        helps.append(field_info.description or validation_error["msg"])

    error = Error(app_exception.model.__name__, messages, helps)

    return JSONResponse(status_code=400, content=error.__dict__)


"""
--------------------------------------------------------------------------
 Database
--------------------------------------------------------------------------

Here you may define all your database initializers, such as seeders,
migrations or paths.

"""


@app.on_event("startup")
async def startup():
    await DatabaseSeeder().execute()


@app.on_event("shutdown")
async def shutown():
    db.close()
