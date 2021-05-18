from vconnector.core import VConnector
client = VConnector(user='root',pwd='Mke11anP',host='10.3.0.101')
vms = client.get_host_view()
print(vms.view)