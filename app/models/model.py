import importlib
from typing import Any, Dict, List, NoReturn

from configs.database import db
from fastapi.logger import logger
from sqlalchemy import delete, inspect
from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    async def find(self, id: int):
        try:
            # NOTE: [Sat Apr 29 21:34:03 2023] Need to use self.__class__
            # because we query a model class, not an instance.
            return db.query(self.__class__).filter(self.__class__.id == id).first()
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    #  async def find_by(self, column: str, value: Any):
    #      try:
    #          # NOTE: [Sat Apr 29 21:34:03 2023] Need to use self.__class__
    #          # because we query a model class, not an instance.
    #          return db.query(self.__class__).filter(getattr(self.__class__, column) == value).first()
    #      except Exception as e:
    #          logger.exception(e)
    #          db.rollback()
    #          raise e

    async def all(self) -> List:
        try:
            return db.query(self.__class__).all()
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    async def save(self) -> NoReturn:
        try:
            model = await self.find(self.id)

            if model:
                return await self.update()

            db.add(self)
            db.commit()
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    async def save_many(self, models: List) -> List:
        for model in models:
            await model.save()

        return models

    async def update(self) -> NoReturn:
        try:
            db.merge(self)
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    async def delete(self) -> NoReturn:
        try:
            db.delete(self)
            db.commit()
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    async def truncate(self) -> NoReturn:
        try:
            db.execute(delete(self.__class__))
            db.commit()
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    async def column_data(self):
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self).mapper.column_attrs
        }

    async def validate(self, **kwargs):
        # NOTE: [Wed Jun 28 23:51:52 2023] Check if a class with the same name
        # of the model exists into app/validators, if it exists instanciate and
        # call the validate() method if not thrown an exception.

        module_name = f"app.validators.{self.__class__.__name__.lower()}"
        module = importlib.import_module(module_name)

        validator_class = getattr(module, self.__class__.__name__)

        if kwargs:
            validator_class(**kwargs)
        else:
            validator_class(**await self.column_data())

        return self
