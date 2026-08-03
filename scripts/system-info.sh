#!/bin/bash

echo "==============================="
echo " System Information"
echo "==============================="

hostnamectl

echo
echo "==============================="
echo " Disk Usage"
echo "==============================="
df -h

echo
echo "==============================="
echo " Memory Usage"
echo "==============================="
free -h

echo
echo "==============================="
echo " CPU Load"
echo "==============================="
uptime

echo
echo "==============================="
echo " Network Interfaces"
echo "==============================="

ip -br link | awk '{print $1, $2}'

echo
echo "==============================="
echo " Important Services"
echo "==============================="

echo -n "SSH: "
systemctl is-active ssh

echo -n "Nginx: "
systemctl is-active nginx

echo -n "Docker: "
systemctl is-active docker

echo -n "Tailscale: "
systemctl is-active tailscaled