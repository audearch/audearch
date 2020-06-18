import auderch.database as ad
import pytest


@pytest.fixture(scope="module")
def db():
    mongodb = ad.MongodbFactory()
    imongodb = mongodb.create()

    yield imongodb

    mongodb.close()
