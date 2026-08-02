# Home Lab Architecture

## Architecture Overview

The home lab is designed to simulate a small enterprise network environment for learning Cisco switching, Linux infrastructure administration, secure remote management, and network troubleshooting.

The infrastructure consists of a Cisco Catalyst 2960X managed switch, an Ubuntu Server providing network services, Linux and macOS administration workstations, and an Internet gateway.

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

## Device Roles

### Cisco Catalyst 2960X

The Cisco Catalyst 2960X functions as the central Layer 2 managed switch, providing connectivity between network devices and enabling secure switch administration.

Responsibilities include:

- Layer 2 switching
- SSH management
- Console management
- Port administration
- Network connectivity

---

### Ubuntu Server

Ubuntu Server provides centralized Linux services within the lab.

Services include:

- OpenSSH
- Nginx
- User management
- Package management
- System services

---

### Lenovo (Linux Mint)

The Linux Mint workstation is used for:

- Cisco console administration
- Network testing
- Linux administration
- SSH connectivity verification

---

### MacBook Air

The MacBook Air serves as the remote administration workstation.

Responsibilities include:

- SSH administration
- Configuration management
- Documentation
- GitHub repository maintenance

---

## Management Methods

The lab supports two administration methods.

### In-band Management

- SSH
- Network-based administration
- Remote Linux management
- Remote Cisco switch management

---

### Out-of-band Management

- USB Console Cable
- Cisco Console Port
- Initial switch configuration
- Recovery when SSH is unavailable

---

## Network Services

The Ubuntu Server currently provides:

- Secure Shell (OpenSSH)
- Nginx Web Server

Additional services can be added in the future as the lab expands.

---

## Skills Demonstrated

- Cisco IOS Administration
- Linux Administration
- Secure Remote Management
- TCP/IP Networking
- SSH
- Network Troubleshooting
- Enterprise Infrastructure Concepts
