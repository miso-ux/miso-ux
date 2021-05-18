from __future__ import print_function
import pyVmomi
from vconnector.core import VConnector
client = VConnector(
    user='root',
    pwd='Mke11anP',
    host='10.3.0.101')
client.connect()
host = client.get_object_by_property(
    property_name='name',
    property_value='esxi01.example.org',
    obj_type=pyVmomi.vim.HostSystem
)
print(host.name)
client.disconnect()