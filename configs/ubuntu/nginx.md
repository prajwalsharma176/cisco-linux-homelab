# Nginx Configuration

## Purpose

Nginx is used to host a web server within the home lab.

## Installation

```bash
sudo apt install nginx
```

## Service Management

```bash
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

## Features

- Static web hosting
- HTTP service
- Systemd service management

## Verification

Verified successful deployment by accessing the default Nginx web page from another device within the lab.