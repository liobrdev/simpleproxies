import re

from flask.testing import FlaskClient

from utils import ip_address_regex


def test_proxies_api(client: FlaskClient):
    response = client.get('/api/proxies')
    body = response.json
    assert isinstance(body, list)
    
    for ip_address in body:
        assert isinstance(ip_address, str)
        ip_match = re.match(ip_address_regex(), ip_address)
        assert ip_match is not None
        assert ip_match.group(0) == ip_address
