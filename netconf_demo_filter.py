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
filter = "<get-interface-information><terse/></get-interface-information>"
for switch in switches:
    with manager.connect(host=switch["host"], port=switch["port"], username=switch["username"], password=switch["password"], hostkey_verify=False, device_params={'name': 'junos'}) as m:
        response = m.rpc(filter)
        interfaces = response.xpath("//*[local-name()='physical-interface']")
        print(f"{'Interface':<20} {'Admin status':<12}")
        print("-" * 32)
        for phy in interfaces:
            name_el = phy.xpath("*[local-name()='name']")
            admin_el = phy.xpath("*[local-name()='admin-status']")
            name = (name_el[0].text or "").strip()
            admin = (admin_el[0].text or "").strip() if admin_el else "?"
            print(f"{name:<20} {admin:<12}")
