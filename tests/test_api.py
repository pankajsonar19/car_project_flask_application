import pytest
import warnings
from app import main

warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd
from app.database import db
from app.models.models import Car_db
import os
import io


def setup_module():
    global app, test_client

    app = main.create_app('test')

    test_client = app.test_client()


# Car API testing

def test_read_file():
    # path = '/home/ubuntu/Pyapp/tests/'
    csv_file_path = (os.path.dirname(__file__)) + '/car_data.csv'
    with open(csv_file_path, 'rb') as f:
        data = dict(car_data=(f))

        res = test_client.post('/api/v1/cars/read_file', data=data, content_type='multipart/form-data')

    assert res.status_code < 400


def test_get_details():
    id = 1
    # this token expires after sometime. please use the email-password.html to create access token ( for more details refer readme.md)
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjI4Y2M2MzEyZWVkYjI1MzIwMDQyMjI4MWE4MTQ4N2UyYTkzMjJhOTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY2FycHJvamVjdC1mZTRlZiIsImF1ZCI6ImNhcnByb2plY3QtZmU0ZWYiLCJhdXRoX3RpbWUiOjE1NjQxODE0MDYsInVzZXJfaWQiOiJjWmlFV1ZUZ2ljVDhOTlJ0TGc3dDQwRmxyV0IzIiwic3ViIjoiY1ppRVdWVGdpY1Q4Tk5SdExnN3Q0MEZscldCMyIsImlhdCI6MTU2NDE4MTQwNiwiZXhwIjoxNTY0MTg1MDA2LCJlbWFpbCI6InBhbmthai5zb25hckB1Y2Rjb25uZWN0LmllIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInBhbmthai5zb25hckB1Y2Rjb25uZWN0LmllIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.GxydEow52v3i8B0rocyCp1LqkYz3pqVgRt9mXTtw9oEYJISaKePhgyc-2ni5hrp4BfqpmI8zuqy4XWdjPWoOgqobCAU7rHK46BxTPLECHCzdVm9sYG3b-DPBPMRInDsCZQUcvHnThLCBJo2o6K_nJr33amskKok3_qSFbMzA2qXYRTtfk0HXfEQTMPxDfvnorp333aWch_NnFGHLj74KzSPw60khjzD8r2-wPxlaSaEEizigX6G_5rJ0PtQtzaSkyUTXzOlbD055Oinq94SA21Su6Dv_4U-U1Xc4YuEfIIKFObcwAaYnc3eIvqO_xVUqEntfmt6RlBolvzWKvisx3w"
    res = test_client.get('/api/v1/cars/%d' % (id),headers={'Authorization': token})
    assert res.status_code == 200


def test_average_price():
    res = test_client.post('/api/v1/cars/avg_price', json={'make': 'Nissan', 'model': 'Micra'})
    assert res.status_code < 400
