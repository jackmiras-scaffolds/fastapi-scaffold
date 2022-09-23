from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse

from app.exceptions.application_exeception import ApplicationException
from app.helpers.constants import Constants
from database.seeds.database_seeder import DatabaseSeeder
from routes.api import api

"""
|--------------------------------------------------------------------------
| Routes
|--------------------------------------------------------------------------
|
| Here you may specify all your router's bootstrap.
|
"""


app = FastAPI()
app.include_router(api, prefix=Constants.API_V1)


@app.get("/")
async def read_root():
    return RedirectResponse(url=Constants.API_V1)


"""
|--------------------------------------------------------------------------
| Exception Handler
|--------------------------------------------------------------------------
|
| Here is defined the exception handler convention for the entire application.
| It's important that every exception MUST derive ApplicationException.
|
"""


@app.exception_handler(ApplicationException)
async def app_exception_handler(self, app_exeception: ApplicationException):
    app_exeception.log_message()
    content = app_exeception.detail()
    status_code = app_exeception.status_code()
    return JSONResponse(status_code=status_code, content=content)


"""
|--------------------------------------------------------------------------
| Database Seeders
|--------------------------------------------------------------------------
|
| Here you may call all your database seeders classes.
|
"""


@app.on_event("startup")
async def startup():
    # NOTE: [Thu Mar 17 17:46:10 2022] Integration with the database is not good
    # try to use something more like ActiveRecord or Eloquent
    # await DatabaseSeeder().execute()
