from datetime import datetime

print("Collecting network switch info...")

# string
switch_hostname = input("Enter switch hostname: ")
switch_ip = input("Enter switch IP address: ")
switch_model = input("Enter switch model: ")
switch_location = input("Enter switch location: ")

# integer
port_count = int(input("Enter number of ports: "))

# # float
# uptime_days = float(input("Enter uptime in days (e.g. 45.5): "))

# # boolean (y/n -> True/False)
# is_managed_raw = input("Is the switch managed? (y/n): ").strip().lower()
# is_managed = is_managed_raw in ("y", "yes", "true", "1")

# # datetime (expect YYYY-MM-DD)
# last_maintenance_str = input("Last maintenance date (YYYY-MM-DD): ")
# last_maintenance = datetime.strptime(last_maintenance_str, "%Y-%m-%d")

print("\n--- Network switch info (multiple data types) ---")
print("Hostname (str):", switch_hostname)
print("IP address (str):", switch_ip)
print("Model (str):", switch_model)
print("Location (str):", switch_location)
print("Port count (int):", port_count, "| type:", type(port_count).__name__)
# print("Uptime days (float):", uptime_days, "| type:", type(uptime_days).__name__)
# print("Is managed (bool):", is_managed, "| type:", type(is_managed).__name__)
# print("Last maintenance (datetime):", last_maintenance, "| type:", type(last_maintenance).__name__)
print("-------------------------------------------------")

# conditional: classify switch by port count
if port_count >= 48:
    print("Switch is large (48+ ports)")
    switch_size = "large (48+ ports)"
elif port_count >= 24:
    print("Switch is medium (24-47 ports)")
    switch_size = "medium (24-47 ports)"
else:
    print("Switch is small (under 24 ports)")
    switch_size = "small (under 24 ports)"

print(f"\nSwitch size classification: {switch_size}")

# list: VLANs configured on the switch
vlan_ids = [10, 20, 30, 100, 200]
print("\n--- Configured VLANs (list + loop) ---")
for vlan_id in vlan_ids:
    print(f"  VLAN {vlan_id}")
print("-------------------------------------")
