# OpenSSH Configuration

## Purpose

OpenSSH provides secure remote administration of the Ubuntu Server.

## Configuration

- Installed OpenSSH Server
- Enabled SSH service
- Configured SSH for remote administration
- Disabled direct root login
- Configured SSH key-based authentication
- Verified SSH connectivity from Linux and macOS administration workstations

## Service Management

```bash
sudo systemctl status ssh
sudo systemctl enable ssh
sudo systemctl restart ssh
```

## Security

- SSH protocol version 2
- Key-based authentication
- Root login disabled
- Secure remote administration