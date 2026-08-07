# Cisco/Linux Home Lab

Enterprise-style Cisco and Linux Home Lab built to develop practical skills in Linux administration, Cisco networking, network automation, infrastructure monitoring, and enterprise documentation.

---

## Project Overview

This project documents the design, implementation, automation, and management of my personal enterprise-style networking laboratory.

The lab combines Cisco networking hardware with Linux servers to simulate real-world infrastructure administration tasks including:

- Cisco IOS administration
- Linux server administration
- Secure remote management
- Network troubleshooting
- Infrastructure documentation
- Python network automation
- Configuration backup
- Git/GitHub workflow

The primary goal is to build hands-on infrastructure engineering skills similar to those used in enterprise environments.

---

# Project Status

| Component | Status |
|------------|---------|
| Cisco Switch Installation | ✅ Complete |
| Ubuntu Server | ✅ Complete |
| SSH Management | ✅ Complete |
| VS Code Remote SSH | ✅ Complete |
| GitHub Repository | ✅ Complete |
| NTP Synchronization | ✅ Complete |
| Syslog Configuration | ✅ Complete |
| PortFast | ✅ Complete |
| BPDU Guard | ✅ Complete |
| Python Automation | ✅ Complete |
| Configuration Backup | ✅ Complete |
| VLAN Configuration | 🚧 In Progress |
| SNMP Monitoring | 🚧 Planned |
| LibreNMS | 🚧 Planned |
| Docker | 🚧 Planned |
| Grafana | 🚧 Planned |
| Ansible | 🚧 Planned |

---

# Objectives

The objectives of this project are:

- Learn enterprise Linux administration
- Learn Cisco IOS administration
- Build practical networking skills
- Practice secure remote administration
- Implement infrastructure monitoring
- Learn Python network automation
- Document infrastructure professionally
- Practice Git version control
- Build a professional networking portfolio

---

# Physical Network Topology

![Network Topology](images/network-topology.png)

---

# Logical Network Topology

```text
                    Internet
                        │
                Airtel Home Router
                  192.168.1.1
                        │
                        │
            Cisco Catalyst 2960X Switch
              Management IP
               192.168.1.2
                VLAN 1
        ┌──────────────┴──────────────┐
        │                             │
Ubuntu Server                   Linux Mint
192.168.1.8                  Administration PC
                                   │
                                   │ SSH
                                   │
                            MacBook Air
```

---

# Hardware

| Device | Purpose |
|---------|---------|
| Cisco Catalyst WS-C2960X-24TS-L | Layer-2 Managed Switch |
| HP Notebook 2000 | Ubuntu Server |
| Lenovo Laptop | Linux Mint Administration |
| MacBook Air | Remote Administration |
| Airtel Router | Internet Gateway |

---

# Software

- Ubuntu Server 26.04 LTS
- Cisco IOS
- Python 3
- Netmiko
- OpenSSH
- VS Code Remote SSH
- Git
- GitHub
- Nginx
- Tailscale

---

# Network Addressing

| Device | IP Address |
|---------|------------|
| Airtel Router | 192.168.1.1 |
| Cisco Switch | 192.168.1.2 |
| Ubuntu Server | 192.168.1.8 |
| Linux Mint | DHCP |
| MacBook Air | DHCP |

---

# Cisco Features Configured

Successfully configured:

- SSH Remote Management
- Local User Authentication
- NTP Synchronization
- Syslog
- PortFast
- BPDU Guard
- Interface Descriptions
- VLAN Management Interface
- Default Gateway
- Secure Remote Login

---

# Linux Features Configured

- OpenSSH Server
- VS Code Remote SSH
- Git
- GitHub
- Python Virtual Environment
- Netmiko
- Nginx
- Rsyslog
- Tailscale
- Systemd Services

---

# Python Network Automation

Python automation is used to connect to the Cisco switch through SSH using Netmiko.

Current automation tasks:

- Connect to Cisco Switch
- Execute multiple show commands
- Save command output
- Backup switch information
- Maintain configuration snapshots

Commands collected automatically:

- show version
- show inventory
- show clock
- show interfaces status
- show interfaces description
- show ip interface brief
- show vlan brief
- show running-config
- show startup-config
- show logging
- show ntp status
- show mac address-table
- show spanning-tree summary
- show ip ssh
- show users
- show cdp neighbors

---

# Automation Workflow

```text
Python Script
      │
      ▼
Netmiko SSH
      │
      ▼
Cisco Switch
      │
      ▼
Execute Show Commands
      │
      ▼
Collect Output
      │
      ▼
Save to Files
      │
      ▼
Git Commit
      │
      ▼
GitHub Repository
```

---

# Monitoring

Current monitoring includes:

- SSH connectivity
- Syslog
- NTP status
- Interface status
- Switch logs
- Configuration backup

Planned monitoring:

- SNMP
- LibreNMS
- Grafana
- Prometheus

---

# Repository Structure

```text
cisco-linux-homelab/

├── README.md
├── CHANGELOG.md
├── LICENSE
│
├── configs/
│   ├── switch/
│   └── ubuntu/
│
├── diagrams/
│
├── docs/
│
├── images/
│
├── screenshots/
│   ├── ssh/
│   ├── vscode/
│   ├── nginx/
│   ├── cisco/
│   └── automation/
│
├── monitoring/
│
├── runbooks/
│
└── scripts/
```

---

# Documentation

The repository contains documentation for:

- Cisco Configuration
- Ubuntu Configuration
- Network Topology
- Python Automation
- SSH
- Syslog
- NTP
- Git Workflow
- Troubleshooting Guides

---

# Screenshots

## Cisco SSH

*(Add screenshot)*

---

## VS Code Remote SSH

*(Add screenshot)*

---

## Cisco CLI

*(Add screenshot)*

---

## Python Automation

*(Add screenshot)*

---

## GitHub Repository

*(Add screenshot)*

---

## Nginx

*(Add screenshot)*

---

## Skills Demonstrated

### Networking

- Cisco IOS
- Switching
- VLAN Fundamentals
- PortFast
- BPDU Guard
- NTP
- Syslog
- SSH
- TCP/IP

### Linux

- Ubuntu Server
- OpenSSH
- Systemd
- Nginx
- Bash
- Networking

### Automation

- Python
- Netmiko
- SSH Automation
- Configuration Backup

### DevOps

- Git
- GitHub
- VS Code
- Markdown

---

# Future Roadmap

- VLAN Segmentation
- Inter-VLAN Routing
- Port Security
- EtherChannel
- SNMP
- LibreNMS
- Docker
- Grafana
- Prometheus
- Ansible
- CI/CD
- Multi-device Automation
- Automated Configuration Compliance

---

# Author

**Prajwal R**

Information Science & Engineering Student

### Areas of Interest

- Computer Networking
- Linux System Administration
- Infrastructure Engineering
- Network Automation
- Cloud Infrastructure
- DevOps

---

# License

This project is maintained for educational purposes, continuous learning, and professional portfolio development.