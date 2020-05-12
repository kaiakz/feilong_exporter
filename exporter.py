import json
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY

from collector import ZVMCollector

fake_token_path = 'tests/faketoken.txt'
mock_server_port = 8909


# Export them to Prometheus
if __name__ == "__main__":
    REGISTRY.register(ZVMCollector(port=mock_server_port, token_path=fake_token_path))     # TODO
    start_http_server(8009)
    while True:
        pass