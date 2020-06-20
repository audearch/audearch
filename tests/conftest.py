import pytest
import audearch.database as ad


@pytest.fixture(scope="session")
def db_connection():
    mongodb = ad.MongodbFactory()
    imongodb = mongodb.create()

    return imongodb
