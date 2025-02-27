# test_calculator.py

import pytest
from fastapi.testclient import TestClient
from calculator import app

client = TestClient(app)


def test_square_root():
    response = client.get("/sqrt/9")
    assert response.status_code == 200
    assert response.json()["result"] == 3.0


def test_factorial():
    response = client.get("/factorial/5")
    assert response.status_code == 200
    assert response.json()["result"] == 120


def test_natural_log():
    response = client.get("/ln/1")
    assert response.status_code == 200
    assert response.json()["result"] == 0.0


def test_power():
    response = client.get("/power/2/3")
    assert response.status_code == 200
    assert response.json()["result"] == 8.0
