#!/usr/bin
#lsblk 
dd if="./filename.iso" of="/dev/sdb" status="progress" conv="fsync"
