# NTP Configuration

## Purpose

Network Time Protocol (NTP) synchronizes the Cisco Catalyst switch clock with a reliable time source, ensuring accurate timestamps for logs, monitoring, and network operations.

---

## Prerequisites

Before configuring NTP, ensure:

- Switch has IP connectivity
- DNS is configured (if using hostname)
- Internet access is available (or an internal NTP server exists)

---

## Configuration

Configure the NTP server.

```cisco
configure terminal

ntp server pool.ntp.org

end

write memory
```

---

## Verification

### Verify NTP Status

Run:

```cisco
show ntp status
```

Expected Result

- Clock synchronized
- NTP server reachable
- Synchronization successful

Evidence

```
configs/switch/show-ntp-status.txt
```

---

### Verify System Clock

Run:

```cisco
show clock
```

Expected Result

- Correct date and time displayed
- Time matches the configured NTP source

Evidence

```
configs/switch/show-clock.txt
```

---

### Verify Running Configuration

Run:

```cisco
show running-config | include ntp
```

Expected Result

- Configured NTP server displayed

Evidence

```
configs/switch/show-running-config.txt
```

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| Clock not synchronized | NTP server unreachable | Verify Internet connectivity |
| Incorrect time | Wrong timezone | Configure timezone |
| No NTP association | Incorrect server | Verify NTP server address |
| Time drifts | Server unavailable | Use another NTP server |

---

## Security Considerations

- Use trusted NTP servers.
- Synchronize all network devices to the same time source.
- Regularly verify clock synchronization.

---

## Files

```
configs/switch/show-ntp-status.txt
configs/switch/show-clock.txt
configs/switch/show-running-config.txt
```

---

## References

- Cisco IOS NTP Configuration Guide
- RFC 5905 – Network Time Protocol Version 4