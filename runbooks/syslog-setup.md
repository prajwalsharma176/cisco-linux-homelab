# Syslog Configuration

## Purpose

Syslog enables the Cisco Catalyst switch to send system logs and events to a centralized Syslog server for monitoring, troubleshooting, and auditing.

---

## Prerequisites

Before configuring Syslog, ensure:

- Switch has IP connectivity
- Syslog server is reachable
- Correct management IP configured
- Time synchronized using NTP

---

## Configuration

Configure the Syslog server.

```cisco
configure terminal

logging host <SYSLOG_SERVER_IP>

logging trap informational

service timestamps log datetime msec

end

write memory
```

---

## Verification

### Verify Logging Configuration

Run:

```cisco
show logging
```

Expected Result

- Remote logging enabled
- Syslog server IP displayed
- Logging level configured
- Log messages being generated

Evidence

```
configs/switch/show-logging.txt
```

---

### Verify Running Configuration

Run:

```cisco
show running-config | include logging
```

Expected Result

- logging host configured
- logging trap configured

Evidence

```
configs/switch/show-running-config.txt
```

---

### Verify Timestamp Configuration

Run:

```cisco
show running-config | include service timestamps
```

Expected Result

- Log timestamps enabled

Evidence

```
configs/switch/show-running-config.txt
```

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| No logs received | Incorrect Syslog server IP | Verify server address |
| Logs missing timestamps | Timestamp service disabled | Configure `service timestamps` |
| Cannot reach Syslog server | Network connectivity issue | Verify routing and connectivity |
| Only local logs available | Remote logging disabled | Configure `logging host` |

---

## Security Considerations

- Use a trusted Syslog server.
- Synchronize device time using NTP.
- Restrict access to log files.
- Regularly review logs for security events.

---

## Files

```
configs/switch/show-logging.txt
configs/switch/show-running-config.txt
```

---

## References

- Cisco IOS System Message Logging Configuration Guide
- RFC 5424 – The Syslog Protocol