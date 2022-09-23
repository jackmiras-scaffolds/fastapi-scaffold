from typing import Generic, List, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from fastapi.logger import logger
from pydantic import BaseModel

from configs.database import Base, db

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def find(self, id: int) -> Optional[ModelType]:
        try:
            return db.query(self.model).filter(self.model.id == id).first()
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    def save(self, pydantic_model: CreateSchemaType) -> ModelType:
        try:
            pydantic_model_encoded = jsonable_encoder(pydantic_model)
            sqlalchemy_model = self.model(**pydantic_model_encoded)

            model = self.find(sqlalchemy_model.id)

            if model:
                return self.update(model, pydantic_model)

            db.add(sqlalchemy_model)
            db.commit()
            db.refresh(sqlalchemy_model)

            # FIXME: It should return a pydantic model [Sun Aug  2 16:02:56 2020]
            return sqlalchemy_model
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    def save_many(self, pydantic_models: List[CreateSchemaType]) -> List[ModelType]:
        return list(map(lambda model: self.save(model), pydantic_models))

    def update(
        self, sqlalchemy_model: ModelType, pydantic_model: UpdateSchemaType
    ) -> ModelType:
        try:
            db.refresh(sqlalchemy_model)
            sqlalchemy_model_encoded = jsonable_encoder(sqlalchemy_model)
            update_data = pydantic_model.dict(exclude_unset=True)

            for field in sqlalchemy_model_encoded:
                if field in update_data:
                    setattr(sqlalchemy_model, field, update_data[field])

            db.add(sqlalchemy_model)
            db.commit()
            db.refresh(sqlalchemy_model)

            # FIXME: It should return a pydantic model [Sun Aug  2 16:02:29 2020]
            return sqlalchemy_model
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e

    def remove(self, id: int) -> ModelType:
        try:
            sqlalchemy_model = db.query(self.model).get(id)
            db.delete(sqlalchemy_model)
            db.commit()

            # FIXME: It should return a pydantic model [Sun Aug  2 16:02:29 2020]
            return sqlalchemy_model
        except Exception as e:
            logger.exception(e)
            db.rollback()
            raise e
