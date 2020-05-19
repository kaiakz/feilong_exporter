## Python Implementation
z/VM Cloud Connector provides a python development sdk to manage z/VM. The new exporter will integrate the `python-zvm-sdk/zvmconnector`, and performs the following steps:
1. Initialization
2. Authentication: [token](https://cloudlib4zvm.readthedocs.io/en/latest/restapi.html#token), the new exporter needs to get a valid token by the Admin-Token.
3. Querying. It should use these API:
```python
# REST methods
req_version    #check the API version
req_host_get_info   #host's cpu, memory, disk
req_host_diskpool_get_info
req_guest_list  #guest list
req_guest_inspect_stats #guest's status
req_guest_inspect_vnics

# SOCKET methods
send_request(self, api_name, *api_args, **api_kwargs)
# api_name can be:
guest_inspect_stats
guest_inspect_vnics
vswitch_query
guests_get_nic_info
# etc
```
4. Processing:
After quering the information, the exporter will receive some requests formated by json:
```json
{
    'overallRC': x, // The overall return code for API request.
    'modID': x, // The module ID that causes the error to occur.
    'rc': x,    // The return code for API request.
    'rs': x,    // The reason code for API request.  
    'errmsg': 'msg',    // The error message returned for API request. It can be empty if no error occur.
    'output': 'out' // The return data from API request.
}
```
The new z/vm export would parse them, and collect the metrics.
5. Exporting
With the help of Prometheus [client_python](https://github.com/prometheus/client_python), it's not difficult to do this. All metrics will be saved in a folder, and sent to Prometheus server.
6. Testing
There are some tests in the zvm Prometheus exporter. I would use those tests in the new exporter.