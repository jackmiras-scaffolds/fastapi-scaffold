from configs.database import db
from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory
from tests.stubs.model import Model


class ModelFactory(SQLAlchemyModelFactory):
    text = Faker("text", max_nb_chars=50)

    class Meta:
        model = Model
        sqlalchemy_session = db
        sqlalchemy_get_or_create = ("text",)
        sqlalchemy_session_persistence = "commit"
