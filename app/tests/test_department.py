from app.tests.setup.test_main import client


def test_get_all_department():
    response = client.get('/department/get')
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    if data:
        department = data[0]

        assert "id" in department
        assert "name" in department
        assert "email" in department
        assert "head_of_department" in department


def test_get_department_by_id():
    response = client.get(
        '/department/specific',
        params={'department_id': 2}
        )
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 2
    assert "name" in data
    assert "email" in data
    assert "head_of_department" in data


def test_get_department_by_id_not_found():
    response = client.get(
        '/department/specific',
        params={'department_id': 999}
    )
    assert response.status_code == 404
    data = response.json()
    assert data['detail'] == "Invalid department id"


def test_create_department():
    payload = {
        'id': 4,
        'name': "Cloud AI",
        'email': 'ca@college.com',
        'head_of_department':'Rahul Mukund'
    }

    response = client.post(
        '/department/create',
        json=payload
    )

    assert response.status_code == 201
    data = response.json()
    assert data['message'] == 'successfully inserted data'


