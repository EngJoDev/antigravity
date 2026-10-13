# ▲ ANTIGRAVITY ▲
### Autonomous Linux Zero-Bloat, Telemetry & FinOps Engine ⚡

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Linux](https://img.shields.io/badge/platform-Linux-green.svg)](https://www.linux.org/)

**Antigravity** is a lightweight, zero-dependency CLI engine designed to eliminate host deadweight, diagnose resource leaks, and calculate real cloud infrastructure cost waste (FinOps) directly from the terminal.

---

## 🌟 Why Antigravity?
Modern cloud servers and Linux systems silently accumulate deadweight:
- Stale Docker image layers and dangling container volumes.
- Bloated `systemd` journal logs filling NVMe/SSD disks.
- Zombie processes and runaway memory-leak loops.
- **Uncontrolled cloud spending:** Companies pay thousands of dollars monthly on oversized cloud storage and idle compute.

Antigravity audits system telemetry, estimates monthly financial waste in USD, and safely purges deadweight to achieve **Zero-G**.

---

## 🚀 Key Features
- 🛰️ **System Deadweight Telemetry:** Instant audit of APT caches, journal logs, and container bloat.
- 💰 **FinOps Economic Waste Calculator:** Computes estimated monthly and annual dollar waste based on AWS EBS & cloud storage pricing.
- 🧹 **Zero-G Purge:** Safe, verified cleanup of accumulated system deadweight without touching personal files or packages.
- ⚡ **Pure Terminal Performance:** Zero heavy web servers, written natively in Python with modern Rich terminal styling.

---

## 🛠️ Quick Start

```bash
# Clone the repository
git clone https://github.com/EngJoDev/antigravity.git
cd antigravity

# Run instant system & FinOps audit
./run.sh scan

# Safely purge deadweight
./run.sh purge
