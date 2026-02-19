def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_dashboard(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Dashboard" in response.text
    assert "Birchwood" in response.text


def test_properties_list(client):
    response = client.get("/properties")
    assert response.status_code == 200
    assert "Properties" in response.text
    assert "Birchwood" in response.text
    assert "Fairview" in response.text


def test_property_detail(client):
    response = client.get("/properties/1")
    assert response.status_code == 200
    assert "Birchwood" in response.text
    assert "Rebuild" in response.text


def test_contractors_list(client):
    response = client.get("/contractors")
    assert response.status_code == 200
    assert "Apex General Contracting" in response.text
    assert "Volta Electric" in response.text


def test_contractor_detail(client):
    response = client.get("/contractors/1")
    assert response.status_code == 200
    assert "Apex General Contracting" in response.text
    assert "Marcus Webb" in response.text


def test_schedule(client):
    response = client.get("/schedule")
    assert response.status_code == 200
    assert "Schedule" in response.text


def test_payments(client):
    response = client.get("/payments")
    assert response.status_code == 200
    assert "Payments" in response.text
    assert "INV-" in response.text
