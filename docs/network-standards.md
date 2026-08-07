# Network Standards

## Purpose

This document defines the standards followed throughout the Cisco & Linux Homelab to ensure consistency, maintainability, security, and scalability.

---

# Device Naming Standard

Devices should follow a consistent naming convention.

| Device Type | Naming Convention | Example |
|------------|-------------------|---------|
| Cisco Switch | SW-<Location>-<Number> | SW-HOMELAB-01 |
| Ubuntu Server | SRV-<Role>-<Number> | SRV-UBUNTU-01 |
| Linux Laptop | ADMIN-<Number> | ADMIN-01 |
| Router | RTR-<Location>-<Number> | RTR-HOME-01 |

---

# Interface Naming Standard

Documentation should always include interface names.

Examples:

| Interface | Description |
|-----------|-------------|
| GigabitEthernet0/1 | Uplink |
| GigabitEthernet0/2 | Ubuntu Server |
| GigabitEthernet0/3 | Administration Laptop |

---

# IP Addressing Standard

Private IPv4 addressing is used.

| Network | Purpose |
|---------|----------|
| Management Network | Switch and Server Management |
| Client Network | Administration Devices |

Actual IP addresses are documented separately and sensitive information is removed before publication.

---

# VLAN Standard

Current implementation:

| VLAN | Purpose |
|------|---------|
| Default VLAN | Management and Lab Devices |

Future implementation:

| VLAN | Purpose |
|------|---------|
| Management VLAN | Device Management |
| User VLAN | Client Devices |
| Server VLAN | Infrastructure Services |
| Guest VLAN | Guest Access |

---

# Documentation Standard

Every implementation document should contain:

- Purpose
- Prerequisites
- Configuration
- Verification
- Evidence
- Troubleshooting
- Security Considerations
- References

---

# Verification Standard

Every configuration must include verification commands.

Examples:

Cisco

```cisco
show running-config
show version
show interfaces status
show vlan brief
show logging
show ntp status
```

Linux

```bash
systemctl status nginx
systemctl status ssh
docker ps
hostnamectl
```

---

# Backup Standard

Configuration backups should be performed before major changes.

Backups include:

- Cisco running configuration
- Cisco startup configuration
- Important Linux configuration files

Automation should be used whenever possible.

---

# Security Standard

The following practices are followed:

- SSH Version 2 only
- Local authentication enabled
- Passwords never stored in plaintext
- Secrets removed before publishing
- Private keys excluded from Git
- Sensitive information redacted

---

# Automation Standard

Automation scripts should:

- Be written in Python or Bash
- Include comments
- Handle errors gracefully
- Avoid hardcoded credentials
- Use secure authentication methods

---

# Git Standards

Commit messages should clearly describe the change.

Examples:

```
Add SSH runbook

Implement Docker monitoring

Update NTP documentation

Improve Python automation

Fix backup script
```

---

# Repository Structure

```
automation/
configs/
diagrams/
docs/
images/
monitoring/
runbooks/
screenshots/
scripts/
```

Every new file should be placed in the appropriate directory.

---

# Future Standards

As the homelab grows, the following standards will be adopted:

- Ansible automation
- Infrastructure as Code
- GitHub Actions
- Configuration compliance
- Monitoring dashboards
- Change management documentation

---

# Conclusion

Following consistent standards improves maintainability, simplifies troubleshooting, and prepares the homelab to resemble enterprise infrastructure environments.