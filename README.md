# feilong_exporter
A z/VM Prometheus exporter based on Feilong.

# Metrics
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

# Architeture

# References
* [z/VM Cloud Connector](https://cloudlib4zvm.readthedocs.io/en/latest/index.html)

The zvm exporter uses these libraries:
* Feilong/zvmconnector client
* Prometheus client_python

