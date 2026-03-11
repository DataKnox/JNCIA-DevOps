from ncclient import manager
from ncclient.xml_ import *

switches = [
    {
        "host": "172.20.1.101",
        "port": 830,
        "username": "knox",
        "password": "Juniper"
    }
]

for switch in switches:
    with manager.connect(host=switch["host"], port=switch["port"], username=switch["username"], password=switch["password"], hostkey_verify=False, device_params={'name': 'junos'}) as m:
        print(f"Connected to {switch['host']}")
        print(m.get_configuration(format="xml"))
        response = m.get_configuration(format="xml")
        hostname = response.xpath("//system/host-name")[0].text
        print(f"Hostname: {hostname}")
        interfaces = response.xpath("//interfaces/interface")
        for interface in interfaces:
            name = interface.xpath("name")[0].text
            description = interface.xpath("admin-status")
            print(f"Interface: {name} - {description}")