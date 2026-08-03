# Cisco/Linux Home Lab

![Ubuntu](https://img.shields.io/badge/Ubuntu-26.04-E95420?logo=ubuntu&logoColor=white)
![Cisco](https://img.shields.io/badge/Cisco-Catalyst%202960X-1BA0D7?logo=cisco)
![Nginx](https://img.shields.io/badge/Nginx-Web%20Server-009639?logo=nginx)
![OpenSSH](https://img.shields.io/badge/OpenSSH-Remote%20Access-black)
![Tailscale](https://img.shields.io/badge/Tailscale-Remote%20Networking-242424?logo=tailscale)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-yellow?logo=linux)

---

# Overview

This repository documents my **Cisco/Linux Home Lab**, built to gain practical experience in Linux system administration, Cisco networking, secure remote administration, infrastructure documentation, and network troubleshooting.

The lab simulates common enterprise infrastructure workflows using both **in-band (SSH)** and **out-of-band (USB Console)** device management.

---

# Quick Facts

| Item | Value |
|------|-------|
| Operating System | Ubuntu 26.04 LTS |
| Switch | Cisco Catalyst 2960X (WS-C2960X-24TS-L) |
| Remote Access | OpenSSH, Tailscale |
| Web Server | Nginx |
| Version Control | Git & GitHub |
| Development | VS Code Remote SSH |
| Documentation | Markdown |

---

# Objectives

- Build enterprise Linux administration skills
- Practice Cisco IOS administration
- Configure secure SSH remote management
- Deploy and manage an Nginx web server
- Document infrastructure professionally
- Troubleshoot networking issues
- Learn Git and GitHub workflows
- Build a professional infrastructure portfolio

---

# Physical Network Topology

![Physical Network Topology](diagrams/physical-topology.png)

---

# Lab Architecture

```text
                    Internet
                        │
                 Airtel Home Router
                 (Default Gateway)
                        │
                Cisco Catalyst 2960X
              WS-C2960X-24TS-L
                 │              │
                 │              │
          Ubuntu Server     Lenovo (Linux Mint)
          (HP Notebook)            │
                 ▲                 │
                 │                 │
                 └──── SSH ────────┘
                       ▲
                       │
             MacBook Air (Remote Administration)

Lenovo ───── USB Console Cable ───── Cisco Console Port
```

---

# Hardware

| Device | Purpose |
|---------|---------|
| Cisco Catalyst 2960X | Layer-2 Managed Switch |
| HP 2000 Notebook PC | Ubuntu Server |
| Lenovo Laptop | Linux Mint Administration Workstation |
| MacBook Air | Remote Administration |
| Airtel Home Router | Internet Gateway |

---

# Software Stack

- Ubuntu 26.04 LTS
- Cisco IOS
- OpenSSH
- Nginx
- Docker
- Tailscale
- Git
- GitHub
- VS Code Remote SSH

---

# Features

- Cisco IOS Administration
- Ubuntu Server Administration
- Secure SSH Remote Access
- Tailscale Remote Connectivity
- Nginx Web Hosting
- Linux User & Group Management
- Linux Service Management
- Git Version Control
- Infrastructure Documentation
- Network Troubleshooting
- In-band Device Management
- Out-of-band Console Management

---

# Network Services

| Service | Status | Purpose |
|---------|--------|---------|
| OpenSSH | Running | Secure Remote Administration |
| Nginx | Running | Web Hosting |
| Docker | Running | Container Runtime |
| Tailscale | Running | Secure Remote Networking |

---

# Skills Demonstrated

- Linux System Administration
- Cisco IOS Administration
- TCP/IP Networking
- SSH
- Nginx
- Docker
- Git & GitHub
- Infrastructure Documentation
- Remote Administration
- Network Troubleshooting

---

# Repository Structure

```text
cisco-linux-homelab/
│
├── .github/
├── CHANGELOG.md
├── LICENSE
├── README.md
│
├── configs/
│   ├── docker/
│   ├── nginx/
│   ├── switch/
│   └── ubuntu/
│
├── diagrams/
├── docs/
├── monitoring/
├── runbooks/
├── screenshots/
│   ├── nginx/
│   ├── ssh/
│   ├── tailscale/
│   ├── terminal/
│   └── vscode/
│
└── scripts/
```

---

# Documentation

This repository includes documentation covering:

- Architecture
- Implementation
- Security
- Troubleshooting
- Ubuntu Configuration
- Cisco Configuration
- Docker Configuration
- Network Topology
- Linux Administration Scripts

---

# Verification Screenshots

## SSH Login

![SSH Login](screenshots/ssh/ssh-login.png)

---

## VS Code Remote SSH

![VS Code Remote SSH](screenshots/vscode/vscode-remote.png)

---

## Ubuntu System Information

![System Information](screenshots/terminal/system-info.png)

---

## Tailscale Service

![Tailscale](screenshots/tailscale/tailscale-status.png)

---

## Nginx Web Server

![Nginx Homepage](screenshots/nginx/nginx-homepage.png)

---

# Automation Scripts

The repository contains administration scripts for common operational tasks.

| Script | Purpose |
|---------|---------|
| system-info.sh | Display system information |
| health-check.sh | Verify important services |
| nginx-restart.sh | Restart Nginx |
| update-server.sh | Update Ubuntu packages |
| backup-config.sh | Backup project configuration |

---

# Technologies Used

- Cisco Catalyst 2960X
- Cisco IOS
- Ubuntu Server
- Linux
- OpenSSH
- Nginx
- Docker
- Git
- GitHub
- Tailscale
- VS Code Remote SSH
- Bash
- TCP/IP

---

# Future Improvements

- VLAN Configuration
- Inter-VLAN Routing
- Port Security
- Cisco SSH Management
- Python Network Automation
- Configuration Backup Automation
- Infrastructure Monitoring
- Centralized Logging
- SNMP Monitoring
- Ansible Automation
- Prometheus
- Grafana
- Kubernetes Home Lab

---

# Author

**Prajwal R**

Information Science & Engineering Student

### Areas of Interest

- Linux System Administration
- Computer Networking
- Infrastructure Engineering
- Network Automation
- Cloud Infrastructure

---

# License

This project is maintained for educational, portfolio, and professional development purposes.
