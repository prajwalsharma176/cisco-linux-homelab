# Tailscale Installation and Configuration

## Purpose

Tailscale provides secure remote access to the homelab over a private mesh VPN, allowing administrators to manage the Ubuntu Server from anywhere without exposing SSH directly to the Internet.

---

## Prerequisites

Before installing Tailscale, ensure:

- Ubuntu Server installed
- Internet connectivity available
- User has sudo privileges
- Tailscale account created

---

## Installation

Install Tailscale.

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Enable the service.

```bash
sudo systemctl enable tailscaled
```

Start the service.

```bash
sudo systemctl start tailscaled
```

Authenticate the server.

```bash
sudo tailscale up
```

Follow the authentication URL in your browser.

---

## Configuration

Check the service status.

```bash
sudo systemctl status tailscaled
```

Check Tailscale status.

```bash
tailscale status
```

Display the assigned Tailscale IP.

```bash
tailscale ip
```

---

## Verification

### Verify Service Status

Run:

```bash
sudo systemctl status tailscaled
```

Expected Result

- Service status is **active (running)**

Evidence

```
configs/ubuntu/tailscale-status.txt
```

---

### Verify VPN Connection

Run:

```bash
tailscale status
```

Expected Result

- Device appears in the Tailnet.
- Status shows **Connected**.

Evidence

```
configs/ubuntu/tailscale-status.txt
```

---

### Verify Assigned IP Address

Run:

```bash
tailscale ip
```

Expected Result

- IPv4 and/or IPv6 Tailscale addresses displayed.

---

### Verify Remote SSH

From another authorized device:

```bash
ssh username@<tailscale-ip>
```

Expected Result

- SSH connection established successfully.

Evidence

```
screenshots/tailscale/tailscale-status.png
```

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| Service inactive | Service not started | `sudo systemctl start tailscaled` |
| Device offline | Authentication expired | Run `sudo tailscale up` |
| Cannot SSH | SSH service not running | Verify `systemctl status ssh` |
| No Internet | Network connectivity issue | Verify Internet access |
| Device not visible | Login issue | Reauthenticate using `tailscale up` |

---

## Security Considerations

- Keep Tailscale updated.
- Enable SSH only for authorized users.
- Remove unused devices from the Tailnet.
- Do not expose SSH directly to the Internet.
- Protect your Tailscale account with MFA.

---

## Files

```
configs/ubuntu/tailscale-status.txt
screenshots/tailscale/tailscale-status.png
```

---

## References

- Tailscale Documentation
- Ubuntu Server Documentation