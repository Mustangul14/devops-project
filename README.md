# 🧭 DevOps System Monitoring Automation Project

## 📘 Project Overview

This project is a DevOps automation pipeline designed to demonstrate end-to-end deployment and orchestration of multiple services using Linux, Docker, Docker Compose, and Ansible.


It consists of two lightweight system monitoring applications — one written in Bash and the other in Python — that collect and display system information (CPU, memory, disk, and network usage) in real time.


Each application is containerized with Docker and managed through Docker Compose.
The entire environment can be automatically deployed on a remote server (e.g., AWS EC2) using Ansible, achieving full infrastructure automation.

## 🏗 Project Architecture

devops-project/

├── bash-script/

│   ├── sysinfo.sh          # Bash monitoring script

│   └── Dockerfile          # Dockerfile for Bash service

├── python-script/

│   ├── sysinfo.py          # Python monitoring script

│   └── Dockerfile          # Dockerfile for Python service

├── docker-compose.yml       # Orchestration for both containers

└── ansible/

    ├── inventory.ini        # Defines target host (e.g., EC2)
    ├── site.yml             # Main playbook
    └── roles/
        ├── docker/          # Role: installs Docker & Compose
        └── deploy/          # Role: copies and runs the project

## 🚀 How the Project Was Implemented

# 1️⃣ System Monitoring Applications

Two applications were built to monitor system performance:
sysinfo.sh (Bash): Uses uname, lscpu, free, df, and ip commands to display CPU, memory, and network info every few seconds.
sysinfo.py (Python): Uses the psutil library to collect metrics in a structured, platform-independent way.
Both scripts were made configurable using the environment variable INTERVAL, allowing dynamic refresh intervals.

# 2️⃣ Containerization with Docker

Each script was packaged in a dedicated Docker image using a custom Dockerfile.
The Bash container is based on Ubuntu 22.04, and the Python one on python:3.11-slim.
Dependencies such as psutil (for Python) and iproute2, procps, net-tools (for Bash) were installed at build time.
Example commands:
docker build -t sysinfo-bash:local ./bash-script
docker build -t sysinfo-py:local ./python-script
docker run sysinfo-bash:local

# 3️⃣ Orchestration with Docker Compose

A docker-compose.yml file was created to manage both containers together.
It defines build contexts, environment variables, and restart policies.
docker compose up --build -d
docker ps
docker compose logs -f
✅ Both containers run simultaneously, printing live system stats to their logs.

# 4️⃣ Infrastructure Automation with Ansible

The Ansible automation handles deployment to remote Linux servers.
The docker role installs Docker and Docker Compose.
The deploy role copies the entire project to /opt/devops-project on the target host and runs docker compose up -d --build.
Steps:
ansible -i inventory.ini -m ping servers
ansible-playbook -i inventory.ini site.yml
After execution:
ssh ubuntu@<EC2_IP>
docker ps
✅ Both containers are deployed and running on AWS EC2.


# 5️⃣ Version Control and Documentation
The project is version-controlled with Git and hosted on GitHub.
A .gitignore file was added to exclude temporary, cache, and log files.
All steps, code, and configurations are documented to enable full reproducibility.