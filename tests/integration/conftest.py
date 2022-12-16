import pytest
from sqlalchemy.orm import clear_mappers

from app.create_app import create_app
from database import db


@pytest.fixture
def app():
    app = create_app(settings_module="config.TestingConfig")
    yield app
    with app.app_context():
        clear_mappers()
        db.drop_all()
