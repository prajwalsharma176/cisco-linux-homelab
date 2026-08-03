# Cisco/Linux Home Lab

## Overview

This repository documents my enterprise-style home lab built using a Cisco Catalyst 2960X switch and Ubuntu Server to develop practical experience in Cisco switch administration, Linux systems administration, secure remote management, and network troubleshooting. The lab simulates common enterprise infrastructure administration workflows using both in-band (SSH) and out-of-band (USB console) device management.

---

## Objectives

- Administer Cisco Catalyst 2960X switches using Cisco IOS
- Deploy and administer Ubuntu Server
- Configure secure remote administration using OpenSSH
- Deploy and manage an Nginx web server
- Practice Linux system administration
- Perform systematic network troubleshooting
- Implement secure infrastructure administration practices
- Understand both in-band and out-of-band device management

---

## Physical Network Topology

![Physical Network Topology](diagrams/physical-topology.png)

---

## Lab Architecture

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

## Components

| Component | Purpose |
|----------|---------|
| Cisco Catalyst 2960X | Layer 2 managed switch |
| Ubuntu Server | Linux server and network services |
| Lenovo (Linux Mint) | Console administration workstation |
| MacBook Air | Remote SSH administration |
| Airtel Home Router | Internet gateway |

---

## Features

- Cisco IOS switch administration
- Ubuntu Server administration
- Secure SSH remote access
- OpenSSH server configuration
- Nginx web server deployment
- Linux user and group management
- Linux file permission management
- Linux package management
- Linux system service management
- Network troubleshooting
- In-band (SSH) administration
- Out-of-band (USB console) administration

---

## Skills Demonstrated

- Cisco IOS Administration
- Linux Systems Administration
- TCP/IP Networking
- Secure Remote Administration
- SSH
- Nginx
- Linux Services
- Network Troubleshooting
- Infrastructure Management

---

## Repository Structure

```text
cisco-linux-homelab/
├── README.md
├── configs/
│   ├── switch/
│   └── ubuntu/
├── diagrams/
├── docs/
├── images/
└── screenshots/
```

---

## Documentation

- Architecture
- Implementation
- Security
- Troubleshooting
- Cisco configurations
- Ubuntu configurations
- Physical network topology

---

## Technologies

- Cisco Catalyst 2960X
- Cisco IOS
- Ubuntu Server
- Linux
- OpenSSH
- Nginx
- Git
- Tailscale
- TCP/IP
- SSH

---

## Future Improvements

- VLAN implementation on the physical switch
- Docker-based services
- Python network automation
- Configuration backup automation
- Infrastructure monitoring
- Centralized logging
- SNMP monitoring

---

## License

This project is maintained for educational, portfolio, and professional development purposes.