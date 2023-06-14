def test_create_job(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA, NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/", json=data)
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


def test_read_job(client):
    data = {
        "title": "SDE user",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA, NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/", json=data)

    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE user"


def test_read_all_jobs(client):
    data = {
        "title": "SDE user",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA, NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/", json=data)
    response = client.post("/jobs/create-job/", json=data)
    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA, NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post("/jobs/create-job/", json=data)
    data["title"] = "test new title"
    response = client.put("/jobs/update/1", json=data)
    assert response.json()["msg"] == "Successfully updated data."
