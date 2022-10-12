from http import HTTPStatus
import json
import os
import tempfile
import pytest
import app
from models import Orders


@pytest.fixture
def client():
    db_fd, app.app.config["DATABASE"] = tempfile.mkstemp()
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        with app.app.app_context():
            app.client
    yield client
    
    os.close(db_fd)
    os.unlink(app.app.config["DATABASE"])
    
def test_index_success(client):
    res = json.loads(client.get("/welcome").data)
    assert "Welcome to Pizza House" == res["message"]
    assert HTTPStatus.OK == HTTPStatus(res["status"])
    
def test_insertData_success(client):
    res = client.post("/order",data=json.dumps(
        dict(orders=["pizza", "burger"])
    ))
    res = json.loads(res.data)
    assert HTTPStatus.CREATED == HTTPStatus(res["status"])
    assert type("success") == type(res["id"])
    
def test_insertData_bad_request(client):
    res = client.post("/order",data=json.dumps(
        dict()
    ))
    res = json.loads(res.data)
    assert HTTPStatus.BAD_REQUEST == HTTPStatus(res["status"])
    
def test_getAllOrders_success(client):
    res = json.loads(client.get("/getorders").data)
    assert HTTPStatus.OK == HTTPStatus(res["status"])
    if len(res['all_orders']):
        assert type({}) == type(res['all_orders'][0])
        

    