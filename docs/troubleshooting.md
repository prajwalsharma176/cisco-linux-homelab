# Troubleshooting Guide

## Overview

This document records real troubleshooting scenarios encountered while building and administering the Cisco/Linux Home Lab.

Documenting problems, root causes, and resolutions helps build systematic troubleshooting skills commonly required in enterprise networking and Linux administration.

---

# Issue 1: SSH Connection Failed

## Problem

Unable to establish an SSH connection to the Ubuntu Server.

## Investigation

- Verified network connectivity.
- Checked the SSH service status.
- Reviewed firewall configuration.
- Confirmed server IP address.

## Root Cause

SSH service was unavailable or network connectivity was interrupted.

## Resolution

- Started the OpenSSH service.
- Verified network connectivity.
- Successfully established an SSH session.

---

# Issue 2: GitHub Connectivity Issue

## Problem

GitHub was inaccessible while connected through the home network.

## Investigation

- Tested general Internet connectivity.
- Compared connectivity using a mobile hotspot.
- Verified DNS resolution.
- Tested network routing.

## Root Cause

Network path or ISP-related connectivity issue.

## Resolution

Verified the issue using an alternate network and continued troubleshooting until GitHub became reachable.

---

# Issue 3: Cisco Console Connection

## Problem

Unable to access the Cisco Catalyst 2960X console.

## Investigation

- Verified USB console cable connection.
- Confirmed USB serial device detection.
- Checked terminal settings.

## Root Cause

Incorrect serial interface or terminal configuration.

## Resolution

Used the correct USB serial interface and verified successful console access.

---

# Issue 4: Nginx Service Validation

## Problem

Needed to verify that the Nginx web server was operating correctly.

## Investigation

- Checked service status.
- Verified server accessibility.
- Tested web page availability from another device.

## Resolution

Confirmed successful web server deployment and client accessibility.

---

# Troubleshooting Methodology

The following approach is used when diagnosing issues.

1. Identify the problem.
2. Verify the current configuration.
3. Isolate the affected component.
4. Identify the root cause.
5. Apply corrective action.
6. Validate the solution.
7. Document the outcome.

