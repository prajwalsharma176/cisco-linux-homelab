from netmiko import ConnectHandler
from pathlib import Path
from getpass import getpass

switch = {
    "device_type": "cisco_ios",
    "host": "192.168.1.2",
    "username": "prajwal",
    "password": getpass("Cisco Password: "),
}

connection = ConnectHandler(**switch)

output = connection.send_command("show version")

output_dir = Path.home() / "cisco-linux-homelab" / "configs" / "switch"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "show-version.txt"

with open(output_file, "w") as f:
    f.write(output)

print(f"Saved output to {output_file}")

connection.disconnect()

