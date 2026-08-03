# OpenSSH Server Configuration

## Purpose

OpenSSH provides secure remote administration for the Ubuntu Server. It allows authorized users to securely access and manage the server over the network using the SSH protocol.

---

## Configuration File

The primary OpenSSH server configuration file is located at:

```text
/etc/ssh/sshd_config
```

Ubuntu also supports additional configuration snippets located in:

```text
/ etc/ssh/sshd_config.d/
```

---

## Current Configuration

| Setting | Value |
|----------|-------|
| SSH Port | 22 (Default) |
| Keyboard Interactive Authentication | Disabled (`KbdInteractiveAuthentication no`) |
| PAM Authentication | Enabled (`UsePAM yes`) |
| X11 Forwarding | Enabled (`X11Forwarding yes`) |
| Print MOTD | Disabled (`PrintMotd no`) |
| Environment Variables | `LANG`, `LC_*`, `COLORTERM`, `NO_COLOR` |
| SFTP Subsystem | Enabled (`/usr/lib/openssh/sftp-server`) |

---

## SSH Service Status

The OpenSSH server is managed using **systemd**.

| Property | Value |
|----------|-------|
| Service Name | `ssh.service` |
| Status | Active (running) |
| Startup | Enabled at boot |
| Triggered By | `ssh.socket` |
| Documentation | `man:sshd(8)`, `man:sshd_config(5)` |

The service was verified using:

```bash
systemctl status ssh
```

Example output:

```text
● ssh.service - OpenBSD Secure Shell server
Loaded: loaded (/usr/lib/systemd/system/ssh.service; enabled; preset: enabled)
Active: active (running)
TriggeredBy: ssh.socket
Docs: man:sshd(8)
      man:sshd_config(5)
```

---

## Service Management

### Check SSH Status

```bash
sudo systemctl status ssh
```

### Restart SSH

```bash
sudo systemctl restart ssh
```

### Reload SSH Configuration

```bash
sudo systemctl reload ssh
```

### Enable SSH at Boot

```bash
sudo systemctl enable ssh
```

### Disable SSH at Boot

```bash
sudo systemctl disable ssh
```

---

## Verification Commands

```bash
systemctl status ssh
ss -tlnp | grep :22
sudo journalctl -u ssh
sudo systemctl is-enabled ssh
```

---

## Remote Administration

The Ubuntu Server is administered remotely using:

- SSH
- VS Code Remote SSH
- Tailscale for secure remote access outside the local network
- macOS administration workstation
- Linux administration workstation

---

## Security Notes

Current security-related settings include:

- Secure Shell (SSH) is used for encrypted remote administration.
- Keyboard Interactive Authentication is disabled.
- PAM authentication is enabled.
- SSH listens on the default TCP port (22).
- Root login follows the Ubuntu default (`prohibit-password`).
- Secure File Transfer Protocol (SFTP) is enabled through the OpenSSH subsystem.
- Configuration is managed using `/etc/ssh/sshd_config` and optional configuration snippets.

---

## References

```text
man sshd
man sshd_config
man ssh
https://man.openbsd.org/sshd_config
```