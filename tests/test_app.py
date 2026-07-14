from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_from_activity():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    original_participants = app.activities[activity_name]["participants"][:]

    try:
        response = client.delete(f"/activities/{activity_name}/participants/{email}")

        assert response.status_code == 200
        assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
        assert email not in app.activities[activity_name]["participants"]
    finally:
        app.activities[activity_name]["participants"] = original_participants
