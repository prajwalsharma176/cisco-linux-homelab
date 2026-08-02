# Cisco/Linux Home Lab

## Overview

This repository documents my enterprise-style home lab built to develop practical skills in Cisco switching, Linux system administration, secure remote management, and network troubleshooting. The lab uses a Cisco Catalyst 2960X switch and Ubuntu Server to simulate common enterprise infrastructure administration workflows.

---

## Objectives

- Build hands-on experience with Cisco IOS administration
- Deploy and administer Ubuntu Server
- Configure secure remote administration using SSH
- Host web services using Nginx
- Practice Linux system administration
- Perform systematic network troubleshooting
- Understand in-band and out-of-band device management

---

## Physical Topology

```
                    Internet
                        │
                 Airtel Router
                        │
                Cisco Catalyst 2960X
                 │              │
                 │              │
          Ubuntu Server    Lenovo (Linux Mint)
                                │
                        USB Console Cable
                                │
                      Cisco Console Port

MacBook Air
     │
     └── SSH → Ubuntu Server
     └── SSH → Cisco Switch
```

---

## Components

| Component | Purpose |
|----------|---------|
| Cisco Catalyst 2960X | Layer 2 managed switch |
| Ubuntu Server | Linux server |
| Lenovo (Linux Mint) | Console management and administration |
| MacBook Air | Remote SSH administration |
| Airtel Router | Internet gateway |

---

## Features

- Cisco IOS switch administration
- Linux system administration
- Secure SSH access
- OpenSSH server
- Nginx web server
- User and group management
- File permission management
- Network troubleshooting
- In-band (SSH) management
- Out-of-band (USB console) management

---

## Skills Demonstrated

- Cisco IOS
- Linux Administration
- TCP/IP Networking
- SSH
- Nginx
- System Services
- Remote Administration
- Network Troubleshooting

---

## Repository Structure

```
cisco-linux-homelab/
├── README.md
├── configs/
├── diagrams/
├── docs/
├── images/
└── screenshots/
```

---

## Future Improvements

- VLAN implementation
- Python network automation
- Infrastructure monitoring
- Configuration backup automation
- Centralized logging
- SNMP monitoring

---

## License

This project is for educational and portfolio purposes.