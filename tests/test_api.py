from app import app

def test_get_workouts():
    client = app.test_client()
    response = client.get("/workouts")

    assert response.status_code == 200

def test_get_missing_workout():
    response = app.test_client().get("/workouts/99999")

    assert response.status_code == 404

