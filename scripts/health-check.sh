#!/bin/bash

echo "==== Home Lab Health Check ===="

systemctl is-active ssh
systemctl is-active nginx
systemctl is-active tailscaled

echo
echo "Disk Usage"
df -h /

echo
echo "Memory Usage"
free -h

echo
echo "CPU Load"
uptime