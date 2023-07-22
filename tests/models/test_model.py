import pytest
from configs.database import db
from database.factories.model_factory import ModelFactory
from sqlalchemy import delete
from tests.stubs.model import Model


@pytest.fixture(autouse=True, scope="function")
async def after_each():
    yield
    # NOTE: [Tue May  2 19:39:00 2023] Delete all data from table
    db.execute(delete(Model))
    db.commit()


async def test_find():
    user = ModelFactory.build()
    db.add(user)
    db.commit()

    result = await Model().find(id=user.id)

    assert user.id == result.id


async def test_all():
    users = ModelFactory.build_batch(size=2)
    for user in users:
        db.add(user)
        db.commit()

    result = await Model().all()

    assert len(result) == 2


async def test_save(faker):
    model = ModelFactory.build()

    await model.save()

    assert len((await model.all())) == 1


async def test_save_2_records(faker):
    model = Model()
    models = ModelFactory.build_batch(size=2)

    for model in models:
        await model.save()

    assert len((await model.all())) == 2


async def test_save_many(faker):
    model = Model()
    models = ModelFactory.build_batch(size=2)

    await model.save_many(models)

    assert len((await model.all())) == 2


async def test_update(faker):
    model = ModelFactory.create()
    new_text = faker.text(max_nb_chars=10)

    model.text = new_text
    await model.update()

    founded_model = await Model().find(id=model.id)
    assert founded_model.text == new_text


async def test_delete():
    model = ModelFactory()

    await model.delete()

    assert len((await Model().all())) == 0


async def test_truncate():
    ModelFactory.create_batch(size=5)

    await Model().truncate()

    assert len(await Model().all()) == 0
