import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def restore_activity_state():
    original_participants = {
        name: activity["participants"][:]
        for name, activity in app_module.activities.items()
    }

    yield

    for name, participants in original_participants.items():
        app_module.activities[name]["participants"] = participants