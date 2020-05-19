The z/vm exporter querys the information by the xCAT rest api(SMAPI):
```shell
System_Page_Utilization_Query -T ZHCP
System_Spool_Utilization_Query -T ZHCP
System_Performance_Information_Query -T ZHCP -k DETAILED_CPU=SHOW=NO
Image_Volume_Space_Query_DM -T ZHCP -q 1 -e 1
Image_Volume_Space_Query_DM -T ZHCP -q 2 -e 1
```
![xcat](https://wiki.openstack.org/w/images/e/e9/Nova-xCAT.png)

The management node uses a z/VM hardware control point (ZHCP) to communicate with SMAPI to implement changes on a z/VM host. The exporter obtains the information of the ZHCP(z/VM hardware control point) node, such as CPU, Memory, Disk, Paging and Spool, and exports some metircs for the Prometheus. The exporter choose grafana as its monitoring dashboards.
We know that there are many guest systems running on z/vm. How about generating each guest's information(CPU, Memory, Disk, nic, vswitch), and exporting them as part of the metric?