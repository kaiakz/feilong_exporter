# feilong_exporter
A z/VM Prometheus exporter based on Feilong.

# Metrics
## Version(zvm_sdk)
* zvm_sdk_version: `zvm_sdk_version{api_version="1.0.",max_version="1.0",min_version="1.0",version="1.0.0"} 1.0`
## Host
* memory_mb
* memory_mb_used
* disk_total
* disk_available
* disk_used
* vcpus
* vcpus_used
## Guest
* max_mem_kb
* num_cpu
* cpu_time_us
* power_state
* mem_kb

# For Developer
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install zVMCloudConnector`
4. `pip install prometheus_client`
5. `pip install flask`
## Run zvm-sdk mocking server
1. `source venv/bin/activate`
2. `python ./tests/mock_server.py`

# Architeture

# References
* [z/VM Cloud Connector](https://cloudlib4zvm.readthedocs.io/en/latest/index.html)

The zvm exporter uses these libraries:
* Feilong/zvmconnector client
* Prometheus client_python
* Flask

