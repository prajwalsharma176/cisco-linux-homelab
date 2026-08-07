from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from pathlib import Path
from getpass import getpass

switch = {
    "device_type": "cisco_ios",
    "host": "192.168.1.2",
    "username": "prajwal",
    "password": getpass("Cisco Password: "),
}

commands = {
    "show-version.txt": "show version",
    "show-inventory.txt": "show inventory",
    "show-clock.txt": "show clock",
    "show-ip-interface-brief.txt": "show ip interface brief",
    "show-interfaces-status.txt": "show interfaces status",
    "show-interfaces-description.txt": "show interfaces description",
    "show-vlan-brief.txt": "show vlan brief",
    "show-mac-address-table.txt": "show mac address-table",
    "show-spanning-tree-summary.txt": "show spanning-tree summary",
    "show-logging.txt": "show logging",
    "show-ntp-status.txt": "show ntp status",
    "show-ip-ssh.txt": "show ip ssh",
    "show-running-config.txt": "show running-config",
    "show-startup-config.txt": "show startup-config",
    "show-users.txt": "show users",
    "show-cdp-neighbors.txt": "show cdp neighbors",
}

output_dir = Path.home() / "cisco-linux-homelab" / "configs" / "switch"
output_dir.mkdir(parents=True, exist_ok=True)

print("=" * 50)
print("Cisco Switch Backup")
print("=" * 50)

try:
    print("Connecting to Cisco switch...")

    connection = ConnectHandler(**switch)

    print("Connected successfully!\n")

    successful = 0

    for filename, command in commands.items():

        print(f"Running: {command}")

        output = connection.send_command(
            command,
            read_timeout=60
        )

        with open(output_dir / filename, "w") as f:
            f.write(output)

        print(f"✓ Saved {filename}\n")

        successful += 1

    connection.disconnect()

    print("=" * 50)
    print("Backup completed successfully!")
    print(f"Commands executed : {successful}")
    print(f"Files saved       : {output_dir}")
    print("=" * 50)

except NetmikoAuthenticationException:
    print("\nAuthentication failed.")
    print("Check your Cisco username/password.")

except NetmikoTimeoutException:
    print("\nConnection timed out.")
    print("Check the switch IP address or network connectivity.")

except Exception as e:
    print(f"\nUnexpected error: {e}")
