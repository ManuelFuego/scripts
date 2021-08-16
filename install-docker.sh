#!/bin/bash

set -e

# Install dependencies.
sudo apt install -y curl apt-transport-https \
     software-properties-common ca-certificates

# Install docker.
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" | \
  sudo tee /etc/apt/sources.list.d/docker-engine.list

sudo apt-get update -y
sudo apt-get install -y docker-ce

# Run docker.
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo gpasswd -a "${USER}" docker
sudo mkdir  /sys/fs/cgroup/systemd
sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd


# Reboot
sudo reboot
