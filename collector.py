import json
from zvmconnector.connector import ZVMConnector

# collect the infomation from sdk server
class ZVMCollector():
    def __init__(self, ip_addr: str=None, port: int=None, timeout: int=3600, \
                 connection_type: str=None, ssl_enabled: bool=False, verify: bool=False, \
                 token_path: bool=None):
        # Init ZVMConnector here
        pass

    # Version
    def collect_api_version(self):
        # GET /
        pass

    # Host
    def collect_host_info(self):
        # GET /host
        pass

    def collect_host_disk_info(self):
        # GET /host/diskpool
        pass

    # Image
    def collect_image_list(self):
        # GET /images
        pass

    # Guest
    def collect_guest_list(self):
        # GET /guests
        pass

    def collect_guest_definition_info(self):
        pass

    def collect_guests_stats(self):
        # GET /guests/stats
        pass

    def collect_guest_info(self):
        # GET /guests/{userid}/info
        pass

    # VSwitch
    def collect_vswitch_list(self):
        # GET /vswitches
        pass

    def collect_vswitch_info(self):
        # GET /vswitches/{name}
        pass


