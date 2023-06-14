def test_create_user(client):
    data = {"username": "testuser", "email": "testuser@noofoobar.com", "password": "testing"}
    response = client.post("/users/", json=data)
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@noofoobar.com"
    assert response.json()["is_active"] is True
