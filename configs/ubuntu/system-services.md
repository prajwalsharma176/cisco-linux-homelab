# Linux System Services

## Purpose

Managed Linux services using systemd.

## Services

- ssh
- nginx
- tailscaled

## Common Commands

```bash
sudo systemctl status ssh
sudo systemctl status nginx
sudo systemctl status tailscaled

sudo systemctl restart ssh
sudo systemctl restart nginx

sudo systemctl enable ssh
sudo systemctl enable nginx
```

## Monitoring

Verified service status and reviewed logs using:

```bash
journalctl
systemctl
```

This ensured that services were operational after configuration changes.