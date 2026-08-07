# Nginx Installation and Configuration

## Purpose

Nginx is deployed as a lightweight, high-performance web server to host web content and provide HTTP services on the Ubuntu Server within the homelab.

---

## Prerequisites

Before installing Nginx, ensure the following requirements are met:

- Ubuntu Server installed
- Internet connectivity available
- User has sudo privileges
- System packages updated

---

## Installation

Update the package repository.

```bash
sudo apt update
```

Install Nginx.

```bash
sudo apt install nginx -y
```

Enable the Nginx service.

```bash
sudo systemctl enable nginx
```

Start the service.

```bash
sudo systemctl start nginx
```

---

## Configuration

Verify that the service is enabled.

```bash
sudo systemctl enable nginx
```

Verify that the service is running.

```bash
sudo systemctl start nginx
```

(Optional)

Place your website inside:

```text
/var/www/html/
```

---

## Verification

### Verify Service Status

Run:

```bash
sudo systemctl status nginx
```

Expected Result

- Service status is **active (running)**

Evidence

```
configs/ubuntu/nginx-status.txt
```

---

### Verify Installed Version

Run:

```bash
nginx -v
```

Expected Result

- Installed Nginx version displayed.

Evidence

```
configs/ubuntu/nginx-status.txt
```

---

### Verify HTTP Service

Run:

```bash
curl http://localhost
```

Expected Result

- Default HTML page is returned.

---

### Verify Browser Access

Open:

```
http://<ubuntu-server-ip>
```

Expected Result

- Nginx welcome page or custom homepage is displayed.

Evidence

```
screenshots/nginx/nginx-homepage.png
```

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| Nginx service not running | Service stopped | `sudo systemctl start nginx` |
| Port 80 unavailable | Another application is using the port | Check `sudo ss -tulpn` |
| Browser cannot connect | Firewall or incorrect IP | Verify server IP and firewall rules |
| Configuration error | Invalid configuration | Run `sudo nginx -t` |
| Changes not visible | Service not reloaded | Run `sudo systemctl reload nginx` |

---

## Security Considerations

- Keep Ubuntu packages updated.
- Use HTTPS for production deployments.
- Restrict unnecessary firewall ports.
- Review Nginx logs regularly.
- Avoid exposing sensitive files through the web server.

---

## Files

```
configs/ubuntu/nginx-status.txt
configs/ubuntu/nginx.md
screenshots/nginx/nginx-homepage.png
```

---

## References

- Official Nginx Documentation
- Ubuntu Server Documentation