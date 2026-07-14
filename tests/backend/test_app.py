import src.app as app_module


def test_unregister_participant_from_activity(app_client):
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = app_client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in app_module.activities[activity_name]["participants"]
