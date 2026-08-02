# Security

## Overview

Security is an important aspect of enterprise network and Linux administration. This home lab follows basic security practices to provide secure remote administration while minimizing unnecessary access.

---

## SSH

OpenSSH is used as the primary method for remote administration.

Implemented practices include:

- Secure remote administration
- Encrypted communication
- Remote management of Linux systems

---

## SSH Key Authentication

SSH key-based authentication is used to improve security over password-only authentication.

Benefits include:

- Stronger authentication
- Reduced risk of password attacks
- Secure administrative access

---

## Root Login

Direct root login is disabled.

Administrative tasks are performed using a standard user account with elevated privileges when required.

This follows the principle of least privilege.

---

## In-band Management

Normal administration is performed using SSH over the network.

Examples include:

- Ubuntu Server administration
- Cisco switch administration
- Configuration management

---

## Out-of-band Management

USB console connectivity provides an alternative management path.

Benefits include:

- Initial device configuration
- Recovery when network access is unavailable
- Troubleshooting management connectivity issues

---

## Future Security Improvements

Planned improvements include:

- VLAN segmentation
- Firewall configuration
- Configuration backup
- Infrastructure monitoring

