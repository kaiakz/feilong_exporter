# Requirement
The zvm exporter uses these libraries:
* Feilong/zvmconnector
* Prometheus client_python
* Flask

# For Developer
0. `git clone https://github.com/kaiakz/feilong_exporter.git && cd feilong_exporter`
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install zVMCloudConnector`
4. `pip install prometheus_client`
5. `pip install flask`
6. `python exporter.py` or `./venv/bin/python3.8 ./exporter.py`

**TEST ONLY** If you don't have a zvm-sdk server, use the mock server instead. 
## Run zvm-sdk mocking server
1. `source venv/bin/activate`
2. `python ./tests/mock_server.py`