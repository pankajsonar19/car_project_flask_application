import pytest
from app import main,init

@pytest.fixture
def app():
    app = main.create_app('test')
    init.init()
    return app