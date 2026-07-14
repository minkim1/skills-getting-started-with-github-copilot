import src.app as app_module


def test_get_activities_returns_all_activities(app_client):
    response = app_client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert "Chess Club" in activities
    assert activities["Chess Club"]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"


def test_signup_for_activity_adds_participant(app_client):
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    response = app_client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in app_module.activities[activity_name]["participants"]


def test_signup_for_unknown_activity_returns_404(app_client):
    response = app_client.post("/activities/Unknown Activity/signup", params={"email": "student@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_participant_from_activity(app_client):
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = app_client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in app_module.activities[activity_name]["participants"]


def test_unregister_missing_participant_returns_404(app_client):
    activity_name = "Chess Club"
    email = "missingstudent@mergington.edu"

    response = app_client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
