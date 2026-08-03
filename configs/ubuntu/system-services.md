# Linux System Services

## Purpose

Ubuntu Server uses **systemd** to manage system services. Core infrastructure services are configured to start automatically during system boot and provide secure remote administration, web hosting, and remote connectivity for the home lab.

---

## Host Information

| Property | Value |
|----------|-------|
| Hostname | `homelab-srv01` |
| Operating System | Ubuntu 26.04 LTS |
| Kernel | Linux 7.0.0-28-generic |
| Architecture | x86-64 |
| Hardware | HP 2000 Notebook PC |

Verification:

```bash
hostnamectl
```

---

## Core Services

| Service | Purpose | Status | Startup |
|----------|---------|--------|---------|
| SSH | Secure remote administration | Active (running) | Enabled |
| Nginx | Web server | Active (running) | Enabled |
| Tailscale | Secure remote networking | Active (running) | Enabled |

---

## SSH Service

Verification:

```bash
systemctl status ssh
```

Summary:

```text
Service: ssh.service
Status: Active (running)
Startup: Enabled
Triggered By: ssh.socket
Documentation:
  man:sshd(8)
  man:sshd_config(5)
```

---

## Nginx Service

Verification:

```bash
systemctl status nginx
```

Summary:

```text
Service: nginx.service
Status: Active (running)
Startup: Enabled
Documentation:
  man:nginx(8)
```

---

## Tailscale Service

Verification:

```bash
systemctl status tailscaled
```

Summary:

```text
Service: tailscaled.service
Status: Active (running)
Startup: Enabled
Purpose:
  Secure remote connectivity to the home lab
```

> The Tailscale status output contains device-specific information (such as account email and assigned Tailscale IP address). These details are omitted from this repository for privacy.

---

## Service Management

Check service status:

```bash
sudo systemctl status <service>
```

Start a service:

```bash
sudo systemctl start <service>
```

Restart a service:

```bash
sudo systemctl restart <service>
```

Reload a service:

```bash
sudo systemctl reload <service>
```

Enable a service at boot:

```bash
sudo systemctl enable <service>
```

Disable a service:

```bash
sudo systemctl disable <service>
```

---

## Log Management

View service logs:

```bash
journalctl -u ssh
journalctl -u nginx
journalctl -u tailscaled
```

---

## Monitoring

List running services:

```bash
systemctl --type=service --state=running
```

List enabled services:

```bash
systemctl list-unit-files --type=service --state=enabled
```

---

## Home Lab Services

The following services form the core infrastructure of the home lab:

- OpenSSH Server
- Nginx
- Tailscale
- systemd

These services provide secure remote administration, web hosting, and remote access to the lab environment.

---

## References

```text
man systemctl
man systemd
man journalctl
https://www.freedesktop.org/wiki/Software/systemd/
```