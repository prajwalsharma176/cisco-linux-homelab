# SSH Configuration

## Purpose

Secure Shell (SSH) provides encrypted remote access to the Cisco Catalyst switch, allowing administrators to securely manage the device without using Telnet.

---

## Prerequisites

Before configuring SSH, ensure the following requirements are met:

- Hostname configured
- IP domain name configured
- Management IP address configured
- Local administrator account created
- RSA keys generated
- SSH Version 2 enabled

---

## Configuration

The following configuration was applied on the Cisco Catalyst switch.

```cisco
hostname SW1

ip domain-name homelab.local

username admin privilege 15 secret <REDACTED>

crypto key generate rsa modulus 2048

ip ssh version 2

line vty 0 15
 login local
 transport input ssh
```

---

## Verification

### Verify SSH Status

Run:

```cisco
show ip ssh
```

Expected Result

- SSH Version 2 enabled
- Authentication timeout displayed
- SSH server enabled

Evidence

```
configs/switch/show-ip-ssh.txt
```

---

### Verify Active Users

Run:

```cisco
show users
```

Expected Result

- Active SSH session displayed
- Logged-in administrator shown

Evidence

```
configs/switch/show-users.txt
```

---

### Verify VTY Configuration

Run:

```cisco
show running-config | section line vty
```

Expected Result

- login local
- transport input ssh

Evidence

```
configs/switch/show-running-config.txt
```

---

### Verify SSH Connectivity

From the Linux administration laptop:

```bash
ssh admin@<switch-management-ip>
```

Expected Result

- Password prompt displayed
- Successful login
- Cisco IOS prompt displayed

Evidence

```
screenshots/ssh/ssh-login.png
```

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| Connection refused | SSH not enabled | Verify `ip ssh version 2` |
| Connection timeout | Wrong management IP | Verify VLAN interface and IP configuration |
| Authentication failed | Incorrect username/password | Verify local user configuration |
| Permission denied | VTY misconfiguration | Verify `login local` and `transport input ssh` |
| SSH Version 1 displayed | SSH Version 2 not configured | Configure `ip ssh version 2` |
| RSA key error | RSA keys missing | Generate RSA keys again |

---

## Security Considerations

- Telnet is disabled.
- SSH Version 2 is used.
- Local authentication is enabled.
- Passwords are not stored in this repository.
- Sensitive information has been redacted.

---

## Files

```
configs/switch/show-ip-ssh.txt
configs/switch/show-users.txt
configs/switch/show-running-config.txt
screenshots/ssh/ssh-login.png
```

---

## References

- Cisco IOS Security Configuration Guide
- Cisco Secure Shell Configuration Guide