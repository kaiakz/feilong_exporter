import json
from zvmconnector.connector import ZVMConnector

# collect the infomation from sdk server
class ZVMCollector(ZVMConnector):
    def __init__(self, ip_addr: str=None, port: int=None, timeout: int=3600,
                 connection_type: str=None, ssl_enabled: bool=False, verify: bool=False,
                 token_path: bool=None):
        super().__init__(ip_addr=ip_addr, port=port, timeout=timeout,
                        connection_type=connection_type, ssl_enabled=ssl_enabled,
                        verify=verify, token_path=token_path)
        pass

    def collect(self):
        pass

    # Version
    def collect_api_version(self) -> dict:
        """
        GET /
        "output": {
            "api_version": "1.0.",
            "min_version": "1.0",
            "max_version": "1.0",
            "version": "1.0.0"
        }
        """
        res = self.send_request('version')
        return res['output']


    # Host
    def collect_host_info(self) -> dict:
        """
        GET /host
        "output": {
            "disk_available": 3057,
            "ipl_time": "IPL at 06/02/17 11:07:10 EDT",
            "vcpus_used": 6,
            "hypervisor_type": "zvm",
            "vcpus": 6,
            "zvm_host": "OPNSTK2",
            "memory_mb": 51200.0,
            "cpu_info": {
                "cec_model": "2817",
                "architecture": "s390x"
            },
            "disk_total": 3623,
            "zcc_userid": "ZCCUID",
            "hypervisor_hostname": "OPNSTK2",
            "hypervisor_version": 640,
            "disk_used": 566,
            "memory_mb_used": 0.0
        }
        """
        res = self.send_request('host_get_info')
        return res['output']

    def collect_host_disk_info(self) -> dict:
        """
        GET /host/diskpool
        "output": {
         "disk_available": 3060,
         "disk_total": 3623,
         "disk_used": 563
        },
        """
        res = self.send_request('host_diskpool_get_info')
        return res['output']


    # Image
    def collect_image_list(self) -> dict:
        """
        GET /images
        "output": [{"imagename": "image1",
        "imageosdistro": "rhel7.2",
        "md5sum": "52014cd658cea6ed4005fb25885e30e2",
        "disk_size_units": "0:CYL",
        "image_size_in_bytes": "55",
        "type": "netboot",
        "comments": null}]
        """
        res = self.send_request('image_query')
        return res['output']

    # Guest
    def collect_guest_list(self) -> dict:
        """
        GET /guests
        "output": ["v1", "v2"]
        """
        res = self.send_request('guest_list')
        return res['output']

    # def collect_guest_definition_info(self) -> dict:
    #     pass


    def collect_guest_stats(self, userids) -> dict:
        """
        GET /guests/stats
        output dict cpu and memory statics of guest
        """
        res = self.send_request('guest_inspect_stats', userids)
        return res['output']

    def collect_guest_vnics(self, userids):
        """
        GET /guests/interfacestats
        output dict vNICs statistics of one guest.
        """
        res = self.send_request('guest_inspect_vnics', userids)


    def collect_guest_info(self, userid: str) -> dict:
        """
        GET /guests/{userid}/info
        "output": {
            "max_mem_kb": 1,
            "num_cpu": 1,
            "cpu_time_us": 0,
            "power_state": "off",
            "mem_kb": 0
        }
        """
        res = self.send_request('guest_get_info', (userid))
        return res['output']

    # VSwitch
    def collect_vswitch_list(self) -> dict:
        """
        GET /vswitches
        "output": ["v1", "v2"]
        """
        res = self.send_request('vswitch_get_list')
        return res['output']

    def collect_vswitch_info(self, name: str) -> dict:
        """
        GET /vswitches/{name}
            "output": {
              "switch_name": "TESTVSW",
              "lag_group": "(NOGRP)",
              "port_type": "NONE",
              "vlan_id": "0000",
              "queue_memory_limit": "8",
              "gvrp_request_attribute": "NOGVRP",
              "MAC_protect": "UNSPECIFIED",
              "mac_address": "02-00-0C-00-00-09",
              "gvrp_enabled_attribute": "NOGVRP",
              "lag_interval": "0",
              "IP_timeout": "5",
              "vlan_awareness": "UNAWARE",
              "isolation_status": "NOISOLATION",
              "native_vlan_id": "0000",
              "user_port_based": "USERBASED",
              "transport_type": "ETHERNET",
              "link_ag": "LAG",
              "switch_type": "QDIO",
              "switch_status": "OSA device ready.",
              "routing_value": "NA",
              "VLAN_counters": "E)",
              "real_devices": {"8070":
                                     {"dev_status": "Device is active.",
                                      "controller": "DTCVSW1",
                                      "port_name": "NONE",
                                      "dev_err": "No error.",
                                      "vdev": "0600"}},
              "authorized_users":
                     {"UB160120":
                             {"vlan_ids": [], "prom_mode": "NOPROM",
                              "port_num": "0000", "osd_sim": "NOOSDSIM",
                              "vlan_count": 0},
                      "OPNCLOUD":
                             {"vlan_ids": [], "prom_mode": "NOPROM",
                              "port_num": "0000", "osd_sim": "NOOSDSIM",
                              "vlan_count": 0}},
              "adapters":
                     {
                      "UB160120_1009": {"mac": "02-00-0C-00-01-2D", "type": "QDIO"},
                      "OPNCLOUD_0700": {"mac": "02-00-0C-00-00-0C", "type": "QDIO"}}
              },
        """
        res = self.send_request('vswitch_query', (name))
        return res['output']
