#!/bin/bash

BACKUP_DIR=~/backups
DATE=$(date +%F)

mkdir -p "$BACKUP_DIR"

cp -r ~/cisco-linux-homelab "$BACKUP_DIR/home-lab-$DATE"

echo "Backup completed."