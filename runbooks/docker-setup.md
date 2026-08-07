# Docker Installation and Configuration

## Purpose

Docker is installed on the Ubuntu Server to provide lightweight containerization for running applications and services in isolated environments.

---

## Prerequisites

Before installing Docker, ensure the following requirements are met:

- Ubuntu Server installed
- Internet connectivity available
- User has sudo privileges
- System packages updated

---

## Installation

Update package information.

```bash
sudo apt update
```

Install Docker.

```bash
sudo apt install docker.io -y
```

Enable Docker at boot.

```bash
sudo systemctl enable docker
```

Start Docker.

```bash
sudo systemctl start docker
```

(Optional)

Allow the current user to run Docker without sudo.

```bash
sudo usermod -aG docker $USER
```

Log out and back in for the group change to take effect.

---

## Configuration

Verify Docker service.

```bash
sudo systemctl status docker
```

Verify Docker version.

```bash
docker --version
```

---

## Verification

### Verify Docker Service

Run:

```bash
sudo systemctl status docker
```

Expected Result

- Service status is **active (running)**

Evidence

```
configs/docker/docker-info.txt
```

---

### Verify Docker Version

Run:

```bash
docker --version
```

Expected Result

- Docker version displayed successfully.

Evidence

```
configs/docker/docker-version.txt
```

---

### Verify Docker Information

Run:

```bash
docker info
```

Expected Result

- Docker engine information displayed.

Evidence

```
configs/docker/docker-info.txt
```

---

### Verify Installed Images

Run:

```bash
docker images
```

Expected Result

- Available Docker images listed.

Evidence

```
configs/docker/docker-images.txt
```

---

### Verify Running Containers

Run:

```bash
docker ps
```

Expected Result

- Running containers displayed.
- If no containers are running, the command should complete without errors.

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| Docker service not running | Service stopped | `sudo systemctl start docker` |
| Permission denied | User not in docker group | `sudo usermod -aG docker $USER` |
| Docker command not found | Docker not installed | Install Docker package |
| Cannot connect to Docker daemon | Daemon stopped | Restart Docker service |
| Image download failed | Internet connectivity issue | Verify network connectivity |

---

## Security Considerations

- Keep Docker updated.
- Avoid running containers as root when possible.
- Use trusted container images.
- Remove unused images and containers regularly.
- Limit exposed container ports.

---

## Files

```
configs/docker/docker-version.txt
configs/docker/docker-info.txt
configs/docker/docker-images.txt
```

---

## References

- Docker Official Documentation
- Ubuntu Server Documentation