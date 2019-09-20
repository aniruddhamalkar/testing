from maclookup import ApiClient
import logging
client = ApiClient('at_kmyQbPqQZGvWMGFf3fLYGqdQM11DQ')

logging.basicConfig(filename='myapp.log', level=logging.WARNING)
mac = str(input("Pleas enter the MAC address: "))
print(client.get_vendor(mac))
