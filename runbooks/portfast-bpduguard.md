# PortFast and BPDU Guard Configuration

## Purpose

PortFast and BPDU Guard improve Layer 2 network stability and security by reducing switch port startup time for end devices and protecting the network from accidental or unauthorized switches.

---

## Prerequisites

Before configuring PortFast and BPDU Guard, ensure:

- Cisco Catalyst switch is operational
- Spanning Tree Protocol (STP) is enabled
- Access ports have been identified
- Only end devices are connected to access ports

---

## Configuration

Enable PortFast on access interfaces.

```cisco
configure terminal

interface range FastEthernet0/1 - 24

spanning-tree portfast

exit
```

Enable BPDU Guard globally.

```cisco
configure terminal

spanning-tree portfast bpduguard default

end

write memory
```

---

## Verification

### Verify PortFast

Run:

```cisco
show spanning-tree summary
```

Expected Result

- PortFast Default: Enabled
- Number of PortFast ports displayed

Evidence

```
configs/switch/show-spanning-tree-summary.txt
```

---

### Verify Interface Status

Run:

```cisco
show interfaces status
```

Expected Result

- Access ports are operational
- Connected end devices shown

Evidence

```
configs/switch/show-interfaces-status.txt
```

---

### Verify Interface Configuration

Run:

```cisco
show running-config interface FastEthernet0/1
```

Expected Result

- spanning-tree portfast configured

Evidence

```
configs/switch/show-running-config.txt
```

---

### Verify BPDU Guard

Run:

```cisco
show spanning-tree summary
```

Expected Result

- BPDU Guard Default: Enabled

Evidence

```
configs/switch/show-spanning-tree-summary.txt
```

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|----------|
| Port enters err-disabled state | BPDU received on PortFast port | Remove unauthorized switch and recover interface |
| PortFast not enabled | Interface configured as trunk | Configure only on access ports |
| Device cannot connect | Incorrect interface configuration | Verify interface mode and VLAN assignment |
| STP convergence delay | PortFast disabled | Enable PortFast on access ports |

---

## Security Considerations

- Enable PortFast **only** on access ports.
- Never enable PortFast on switch-to-switch links.
- Use BPDU Guard to automatically disable ports that receive unexpected BPDUs.
- Periodically review err-disabled ports.

---

## Files

```
configs/switch/show-spanning-tree-summary.txt
configs/switch/show-interfaces-status.txt
configs/switch/show-running-config.txt
```

---

## References

- Cisco STP Configuration Guide
- Cisco BPDU Guard Best Practices
