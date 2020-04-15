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

    # Version
    def collect_api_version(self) -> dict:
        # GET /
        res = self.send_request('version')
        return res['output']


    # Host
    def collect_host_info(self) -> dict:
        # GET /host
        res = self.send_request('host_get_info')
        return res['output']

    def collect_host_disk_info(self) -> dict:
        # GET /host/diskpool
        res = self.send_request('host_diskpool_get_info')
        return res['output']


    # Image
    def collect_image_list(self) -> dict:
        # GET /images
        res = self.send_request('image_query')
        return res['output']

    # Guest
    def collect_guest_list(self) -> dict:
        # GET /guests
        res = self.send_request('guest_list')
        return res['output']

    # def collect_guest_definition_info(self) -> dict:
    #     pass


    def collect_guest_stats(self, userids) -> dict:
        # GET /guests/stats
        res = self.send_request('guest_inspect_stats', userids)
        return res['output']

    def collect_guest_info(self, userid: str) -> dict:
        # GET /guests/{userid}/info
        res = self.send_request('guest_get_info', (userid))
        return res['output']

    # VSwitch
    def collect_vswitch_list(self) -> dict:
        # GET /vswitches
        res = self.send_request('vswitch_get_list')
        return res['output']

    def collect_vswitch_info(self, name: str) -> dict:
        # GET /vswitches/{name}
        res = self.send_request('host_get_info', (name))
        return res['output']
