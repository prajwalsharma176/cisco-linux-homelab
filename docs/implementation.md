# Home Lab Implementation

## Overview

This document describes the implementation of the Cisco/Linux home lab and the configuration performed on the network infrastructure and Ubuntu Server.

---

## Cisco Catalyst 2960X

The Cisco Catalyst 2960X serves as the central Layer 2 managed switch within the lab.

### Implemented Features

- Basic switch configuration
- Secure SSH management
- USB console administration
- Interface configuration
- Switch management
- Configuration backup and restore

---

## Ubuntu Server

Ubuntu Server provides centralized services within the lab.

### Implemented Services

- OpenSSH Server
- Nginx Web Server
- Linux user and group management
- File and directory permissions
- Package management
- System service management

---

## Remote Administration

Two administration methods are used.

### In-band Management

- SSH from the MacBook Air
- SSH from the Linux Mint workstation

### Out-of-band Management

- USB console cable connected to the Cisco Catalyst 2960X
- Console access for initial configuration and recovery

---

## Network Validation

The following checks were performed after configuration:

- Verified SSH connectivity
- Verified Nginx accessibility from another workstation
- Verified network connectivity between devices
- Verified Linux services were running correctly

---

## Skills Applied

- Cisco IOS Administration
- Linux Administration
- OpenSSH Configuration
- Nginx Deployment
- Secure Remote Administration
- Network Troubleshooting
- TCP/IP Networking
