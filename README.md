# feilong_exporter
A z/VM Prometheus exporter based on Feilong.

# Metrics
## Version(zvm_sdk)
* zvm_sdk_version: 
    `zvm_sdk_version{api_version="1.0.",max_version="1.0",min_version="1.0",version="1.0.0"} 1.0`
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
0. `git clone https://github.com/kaiakz/feilong_exporter.git && cd feilong_exporter`
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install zVMCloudConnector`
4. `pip install prometheus_client`
5. `pip install flask`
6. `python exporter.py` or `./venv/bin/python3.8 ./exporter.py`

## Run zvm-sdk mocking server
1. `source venv/bin/activate`
2. `python ./tests/mock_server.py`

# Architeture

# References
* [z/VM SDK Document](https://cloudlib4zvm.readthedocs.io/en/latest/index.html)
* [prometheus-openstack-exporter](https://github.com/CanonicalLtd/prometheus-openstack-exporter)
* [nova-zvm's document](https://nova-zvm.readthedocs.io/en/latest/)
* [openstack zvm](https://docs.openstack.org/nova/latest/admin/configuration/hypervisor-zvm.html)
* [zvm-openstack](https://github.com/MaximilianMeister/dirtyhelpers/blob/master/zvm-openstack.md)

The zvm exporter uses these libraries:
* Feilong/zvmconnector
* Prometheus client_python
* Flask

