import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(scope="session")
def app_client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(app_module.activities)
    yield
    app_module.activities = original_activities
    app_module.app.activities = original_activities
