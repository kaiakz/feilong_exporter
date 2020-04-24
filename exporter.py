import json
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY

from collector import ZVMCollector

# Export them to Prometheus
if __name__ == "__main__":
    REGISTRY.register(ZVMCollector())   # TODO
    start_http_server(8009)
    while True:
        pass