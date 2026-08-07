# Network Design

## Overview

This document describes the design of the Cisco & Linux Homelab network. The lab is built to simulate an enterprise infrastructure environment for learning networking, Linux system administration, automation, and infrastructure management.

---

# Objectives

The primary objectives of this homelab are:

- Learn Cisco Enterprise Switching
- Learn Linux System Administration
- Practice Network Automation using Python
- Develop Infrastructure Documentation
- Practice Troubleshooting
- Prepare for Networking and Infrastructure Engineering roles

---

# Network Topology

```
                    Internet
                        │
                Airtel Broadband Router
                        │
        ┌───────────────┴───────────────┐
        │
Cisco Catalyst 2960X Switch
        │
 ┌──────┴─────────────┐
 │                    │
Ubuntu Server      Linux Mint Laptop
(Homelab Server)   (Administration)
        │
    SSH / Python
        │
   Remote Management
        │
     MacBook Air
```

---

# Physical Components

| Device | Role |
|---------|------|
| Cisco Catalyst WS-C2960X-24TS-L | Enterprise Layer 2 Switch |
| Ubuntu Server | Linux Infrastructure Server |
| Linux Mint Laptop | Administration Workstation |
| MacBook Air | Remote Administration |
| Airtel Router | Internet Gateway |
| USB Console Cable | Out-of-band Management |

---

# Network Services

The following infrastructure services are implemented.

| Service | Status |
|----------|--------|
| SSH | ✅ |
| NTP | ✅ |
| Syslog | ✅ |
| Nginx | ✅ |
| Docker | ✅ |
| Tailscale | ✅ |
| Python Automation | ✅ |

---

# Network Management

The network devices are managed using:

- SSH
- Cisco IOS CLI
- Linux Terminal
- Python Netmiko Automation

---

# Infrastructure Automation

Automation is implemented using:

- Python
- Netmiko
- Bash Scripts

Current automation includes:

- Switch Backup
- Show Version Collection

Future automation will include:

- Inventory Collection
- Health Monitoring
- Configuration Validation

---

# Security Features

Current security configurations include:

- SSH Version 2
- Local User Authentication
- PortFast
- BPDU Guard
- Secure Remote Access
- Password Redaction in Repository

Future enhancements:

- Port Security
- DHCP Snooping
- Dynamic ARP Inspection
- SNMPv3

---

# Monitoring

Monitoring currently includes:

- System Health Checks
- Service Monitoring
- Docker Status
- SSH Status
- Tailscale Status

Future monitoring:

- Grafana
- Prometheus
- Alertmanager

---

# Repository Mapping

| Directory | Description |
|-----------|-------------|
| automation/ | Python automation scripts |
| configs/ | Device configurations |
| docs/ | Project documentation |
| runbooks/ | Operational procedures |
| monitoring/ | Monitoring documentation |
| scripts/ | Linux administration scripts |
| diagrams/ | Network diagrams |
| screenshots/ | Verification screenshots |

---

# Skills Demonstrated

This project demonstrates practical experience with:

- Cisco Enterprise Switching
- Linux Administration
- Infrastructure Documentation
- Network Automation
- Git Version Control
- Bash Scripting
- Python Programming
- SSH Administration
- Nginx Administration
- Docker Administration
- Infrastructure Troubleshooting

---

# Future Roadmap

Networking

- VLAN Implementation
- Management VLAN
- Port Security
- DHCP Snooping
- SNMP
- EtherChannel

Linux

- Firewall Management
- Log Rotation
- Cron Automation
- Backup Automation

Automation

- Ansible
- Configuration Compliance
- Health Reporting
- Automated Inventory

Monitoring

- Prometheus
- Grafana
- Uptime Kuma

CI/CD

- GitHub Actions
- Markdown Validation
- Python Testing

---

# Conclusion

This homelab is an ongoing enterprise-style infrastructure project designed to develop practical skills in networking, Linux administration, infrastructure automation, monitoring, and documentation. The project will continue to evolve with additional enterprise networking features and automation capabilities.