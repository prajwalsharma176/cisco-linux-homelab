# Change Management

## Purpose

This document defines the change management process followed within the Cisco & Linux Homelab. The objective is to ensure that all infrastructure changes are planned, documented, verified, and recoverable.

---

# Objectives

The change management process aims to:

- Reduce configuration errors
- Minimize service interruptions
- Maintain configuration consistency
- Provide rollback procedures
- Maintain accurate documentation

---

# Change Categories

| Type | Description |
|------|-------------|
| Standard Change | Low-risk, repeatable changes (e.g., updating documentation) |
| Normal Change | Planned configuration changes requiring verification |
| Emergency Change | Immediate changes required to restore service |

---

# Change Workflow

```
Request
   │
   ▼
Planning
   │
   ▼
Backup
   │
   ▼
Implementation
   │
   ▼
Verification
   │
   ▼
Documentation
   │
   ▼
Completion
```

---

# Pre-Change Checklist

Before making any configuration changes:

- Backup current configuration
- Review implementation plan
- Verify console or SSH access
- Confirm maintenance window (if applicable)
- Verify rollback procedure
- Notify affected users (if applicable)

---

# Implementation Checklist

During implementation:

- Apply configuration changes
- Record commands executed
- Save configuration
- Monitor device status
- Verify expected behavior

---

# Verification Checklist

After implementing changes, verify:

Cisco Switch

```cisco
show running-config
show version
show logging
show interfaces status
show spanning-tree summary
show vlan brief
show ip ssh
show ntp status
```

Ubuntu Server

```bash
hostnamectl

systemctl status ssh

systemctl status nginx

docker ps

tailscale status
```

Expected Result

- Services operational
- Configuration applied successfully
- No unexpected errors
- Network connectivity maintained

---

# Rollback Procedure

If verification fails:

1. Restore previous configuration.
2. Reboot service if necessary.
3. Verify connectivity.
4. Review logs.
5. Investigate root cause.
6. Document the issue.

---

# Backup Policy

Before any major configuration change:

- Backup Cisco running configuration
- Backup Cisco startup configuration
- Backup important Linux configuration files

Automation should be used whenever possible.

---

# Documentation Requirements

Every completed change should include:

- Date
- Engineer
- Purpose
- Devices affected
- Commands executed
- Verification performed
- Outcome
- Rollback required (Yes/No)

---

# Example Change Record

| Field | Value |
|--------|-------|
| Date | 2026-08-07 |
| Engineer | Prajwal R |
| Device | Cisco Catalyst 2960X |
| Change | Enabled BPDU Guard |
| Verification | Successful |
| Rollback Required | No |

---

# Best Practices

- Test changes in the homelab before production.
- Make one significant change at a time.
- Verify every configuration immediately after implementation.
- Keep documentation updated.
- Never publish credentials or sensitive information.

---

# Related Documents

- docs/network-design.md
- docs/network-standards.md
- docs/security.md
- runbooks/
- configs/

---

# Conclusion

A structured change management process improves reliability, simplifies troubleshooting, and ensures that every infrastructure modification is documented and verifiable. Following these practices helps prepare for real-world enterprise networking and infrastructure engineering environments.