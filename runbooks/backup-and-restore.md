# Cisco Switch Backup and Restore

## Purpose

Regular backups of the Cisco switch configuration help protect against hardware failures, accidental configuration changes, and data loss. This runbook documents the backup and restoration process used in the homelab.

---

## Prerequisites

Before performing a backup, ensure:

- SSH is configured on the switch.
- Python and Netmiko are installed.
- Network connectivity to the switch is available.
- Backup directory exists.

---

## Backup Process

Run the backup automation script.

```bash
python automation/backup_switch.py
```

The script will:

- Prompt for Cisco username.
- Prompt for Cisco password securely.
- Connect to the switch using SSH.
- Download the running configuration.
- Save the configuration to a local backup file.

---

## Verification

### Verify Backup File

Run:

```bash
ls backups/
```

Expected Result

- Backup file is created successfully.

---

### Verify Backup Contents

Run:

```bash
cat backups/<backup-file>
```

Expected Result

- Running configuration is displayed.

---

### Verify Script Execution

Run:

```bash
python automation/backup_switch.py
```

Expected Result

- SSH connection established.
- Configuration downloaded.
- Backup completed successfully.

---

## Restore Procedure

If configuration needs to be restored:

1. Connect to the switch using the console cable.
2. Enter privileged EXEC mode.

```cisco
enable
```

3. Enter global configuration mode.

```cisco
configure terminal
```

4. Apply the saved configuration manually or copy it from a TFTP/SCP server if available.

5. Save the configuration.

```cisco
write memory
```

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| SSH connection failed | Incorrect IP or credentials | Verify management IP and credentials |
| Authentication failed | Wrong username/password | Check local user configuration |
| Backup file not created | Directory missing | Create the backup directory |
| Permission denied | File permissions | Verify write permissions |

---

## Security Considerations

- Never store plaintext passwords in scripts.
- Use `getpass()` for password input.
- Protect backup files from unauthorized access.
- Remove sensitive information before publishing backups.

---

## Related Files

```
automation/backup_switch.py
configs/switch/show-running-config.txt
```

---

## References

- Cisco IOS Configuration Fundamentals
- Netmiko Documentation