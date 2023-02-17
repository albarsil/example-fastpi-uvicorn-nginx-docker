import os
import time

import pytest
import requests

d = '.'
print([os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))])

# curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:80/ping
def test_health_endpoint():
    response = requests.get('http://localhost:80/health')
    assert response.status_code == 200

def test_ping_endpoint():
    response = requests.get('http://localhost:80/ping')
    assert response.status_code == 200

# curl curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X -d '{"text":"testing"}'
@pytest.mark.parametrize("payload", [{'text': 'oi'}])
def test_model_endpoint_with_correct_payload(payload):
    response = requests.post('http://localhost:80/test', json=payload)
    assert response.status_code == 200
    
    expected_output_keys = ['message']
    output_keys = response.json().keys()

    for key in expected_output_keys:
        assert key in output_keys