# Nginx Web Server Configuration

## Purpose

Nginx is deployed on the Ubuntu Server to provide web hosting services within the home lab environment. It is managed using `systemd` and serves as the primary HTTP web server for testing and administration.

---

## Installation

Nginx was installed using the Ubuntu package manager.

```bash
sudo apt update
sudo apt install nginx
```

---

## Configuration Files

Main configuration file:

```text
/etc/nginx/nginx.conf
```

Default site configuration:

```text
/etc/nginx/sites-available/default
```

Enabled site configurations:

```text
/etc/nginx/sites-enabled/
```

---

## Current Configuration

| Setting | Value |
|----------|-------|
| Web Server | Nginx |
| Version | 1.28.3 (Ubuntu) |
| Service | `nginx.service` |
| Startup | Enabled at boot |
| Status | Active (running) |
| Worker Processes | Auto |
| Worker Connections | 768 |
| Default Document Root | `/var/www/html` |
| Access Log | `/var/log/nginx/access.log` |
| Error Log | `/var/log/nginx/error.log` |
| Supported TLS Versions | TLS 1.2, TLS 1.3 |

---

## Service Status

The Nginx service is managed using **systemd**.

| Property | Value |
|----------|-------|
| Service Name | `nginx.service` |
| Status | Active (running) |
| Startup | Enabled |
| Documentation | `man:nginx(8)` |

The service was verified using:

```bash
systemctl status nginx
```

Example output:

```text
● nginx.service - A high performance web server and a reverse proxy server
Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
Active: active (running)
Docs: man:nginx(8)
```

---

## Website Files

The default web root is:

```text
/var/www/html
```

Current files:

```text
index.html
index.nginx-debian.html
```

---

## Configuration Validation

Before restarting the service, the configuration syntax is validated.

```bash
sudo nginx -t
```

Example output:

```text
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

---

## Service Management

Check service status:

```bash
sudo systemctl status nginx
```

Start the service:

```bash
sudo systemctl start nginx
```

Restart the service:

```bash
sudo systemctl restart nginx
```

Reload configuration:

```bash
sudo systemctl reload nginx
```

Enable service at boot:

```bash
sudo systemctl enable nginx
```

Stop the service:

```bash
sudo systemctl stop nginx
```

---

## Verification Commands

```bash
systemctl status nginx
nginx -v
sudo nginx -t
curl http://localhost
```

---

## Deployment Summary

The Ubuntu Server hosts Nginx as the primary web server within the home lab. Service availability was verified using `systemctl`, configuration syntax was validated using `nginx -t`, and the default web content is served from `/var/www/html`.

---

## References

```text
man nginx
https://nginx.org/
```