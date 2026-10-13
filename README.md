<div align="center">

# ▲ ANTIGRAVITY ▲
### Autonomous Linux Zero-Bloat, Deep Telemetry & FinOps Engine ⚡

> **Defy System Gravity • Slay Cloud Waste • Reclaim Host Resources**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux%20Native-orange.svg)](https://kernel.org)
[![FinOps: Enabled](https://img.shields.io/badge/FinOps-Cloud%20Cost%20Audit-yellow.svg)](#-the-finops-engine)
[![Terminal UI: Rich](https://img.shields.io/badge/UI-Modern%20Rich%20TUI-9cf.svg)](https://github.com/Textualize/rich)
[![Safety: Sandboxed](https://img.shields.io/badge/Safety-SRE%20Verified-success.svg)](#-safety--reliability-policy)

<br/>

<p align="center">
  <img src="assets/demo.png" alt="Antigravity Live Telemetry & FinOps Engine" width="850" style="border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);"/>
</p>

*Figure 1.0: Real-time telemetry audit inspecting APT cache, log pressure, Docker layers, and projecting cloud financial waste.*

</div>

---

## 📑 Table of Contents
- [Overview & The Problem](#-overview--the-problem)
- [Key Specifications & Features](#-key-specifications--features)
- [System Architecture](#-system-architecture)
- [FinOps Economic Engine](#-finops-economic-engine)
- [Prerequisites & Requirements](#-prerequisites--requirements)
- [Complete Installation & Setup Guide](#-complete-installation--setup-guide)
- [Usage & Command Reference](#-usage--command-reference)
  - [1. Deep System & Cost Audit (`scan`)](#1-deep-system--cost-audit-scan)
  - [2. Safe Zero-Gravity Purge (`purge`)](#2-safe-zero-gravity-purge-purge)
- [Understanding the Output Metrics](#-understanding-the-output-metrics)
- [Vanilla Linux vs. Antigravity](#-vanilla-linux-vs-antigravity)
- [Safety & Enterprise Reliability Policy](#-safety--enterprise-reliability-policy)
- [Roadmap](#-roadmap)
- [Author & Systems Suite](#-author--systems-suite)
- [License](#-license)

---

## 🌌 Overview & The Problem

In high-performance Linux servers, container clusters, and developer workstations, systems silently accumulate **host deadweight**. Over weeks of continuous operation:

- **Unbounded Journal Logs:** `systemd-journald` fills fast SSD/NVMe drives with gigabytes of stale diagnostic events.
- **Docker Layer Atrophy:** Dangling container layers, dead volumes, and untracked builder cache persist silently.
- **Resource Pressure:** Memory leaks and orphaned zombie processes lock operating system Process IDs (PIDs) and exhaust host buffers.
- **The FinOps Blindspot:** Engineering organizations unknowingly pay thousands of dollars every month for oversized cloud block storage (AWS EBS gp3, GCP Persistent Disks, Hetzner volumes) solely to house abandoned caches and stale logs.

**Antigravity** is built to solve this. It provides sub-second host inspection, translates raw wasted gigabytes into actual boardroom financial metrics (USD), and executes sandboxed, non-destructive cleanups to restore **Zero-G system performance**.

---

## ⚡ Key Specifications & Features

| Capability | Specification | Internal Mechanism |
| :--- | :--- | :--- |
| **Deadweight Detection** | Sub-second directory tree & cache scan | Direct non-blocking POSIX filesystem traversal |
| **Log Pressure Audit** | Exact log retention calculation | Native `journalctl --disk-usage` parser |
| **Docker Storage Reclaim** | Reclaimable container layer calculation | Integration with Docker daemon storage engine |
| **Process Telemetry** | Zombie PIDs & memory leak hunter | Cross-platform `/proc` inspection via `psutil` |
| **FinOps Valuation** | Real-time USD waste projection | AWS EBS gp3 provisioned storage pricing model |
| **Execution UI** | Modern terminal visualization | Zero-dependency Rich console with ASCII box framing |
| **Execution Safety** | 100% Non-destructive sandbox | Zero access to user `/home`, codebases, or databases |

---

## 🏗️ System Architecture
code
Code
┌───────────────────────────────┐
                  │     ▲ ANTIGRAVITY CORE ▲      │
                  │       Autonomous CLI          │
                  └───────────────┬───────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
[ 🛰️ Telemetry Audit ] [ 💰 FinOps Engine ] [ 🧹 Zero-G Purge ]
├── APT Archive Scraper ├── Storage Waste ($) ├── 3-Day Journal Vacuum
├── Journalctl Inspector ├── Annual Projection ├── Package Cache Flush
├── Docker Layer Scanner └── Cloud EBS Benchmarks └── Process Leak Warnings
└── Zombie Process Hunter
│ │ │
└─────────────────────────┼─────────────────────────┘
▼
┌───────────────────────────────┐
│ Rich High-Def Terminal UI │
│ (Double-Boxed Status Panels) │
└───────────────────────────────┘
code
Code
---

## 💰 FinOps Economic Engine

Antigravity does not just report gigabytes; it connects systems engineering directly with **cloud financial management (FinOps)**:

$$\text{Monthly Waste (USD)} = \max\left(0.40, \; \text{Total Wasted GB} \times \$0.12/\text{GB-month}\right)$$

$$\text{Annual Infrastructure Savings} = \text{Monthly Waste} \times 12$$

- **Pricing Baseline:** Built against **AWS EBS gp3** and cloud provider retained volume tiers ($0.10 - $0.12 per provisioned GB/month).
- **Executive Visibility:** Gives DevOps leads and engineering managers immediate justification for storage volume right-sizing and cloud cost elimination.

---

## 💻 Prerequisites & Requirements

Antigravity is engineered to be extremely lightweight and portable:
- **Operating System:** Any modern Linux distribution (Ubuntu, Debian, Linux Mint, Arch Linux, Fedora, CentOS, Rocky Linux).
- **Python Runtime:** Python **3.10** or higher.
- **Permissions:** Standard user permissions for scanning. Root (`sudo`) is requested only during the optional cache purge.

---

## 🚀 Complete Installation & Setup Guide

### Method 1: Instant Quickstart (Recommended)

Run Antigravity in under 30 seconds using the pre-configured runner script:

```bash
# 1. Clone the repository
git clone https://github.com/EngJoDev/antigravity.git

# 2. Enter directory
cd antigravity

# 3. Grant execution permissions
chmod +x run.sh

# 4. Launch your first system audit
./run.sh scan
Method 2: Manual Environment Setup
If you prefer full control over your Python virtual environment:
code
Bash
# 1. Clone the project
git clone https://github.com/EngJoDev/antigravity.git
cd antigravity

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install core dependencies
pip install -r requirements.txt

# 4. Execute directly via Python
python3 main.py scan
📖 Usage & Command Reference
1. Deep System & Cost Audit (scan)
Performs a non-destructive audit of system bloat, zombie PIDs, and financial waste:
code
Bash
./run.sh scan
What it does:
Scans /var/cache/apt/archives for residual .deb installer packages.
Reads journalctl to calculate active journal log pressure on disk.
Audits running Docker daemons for reclaimable container caches.
Traverses process trees to spot zombie states and runaway memory consumers.
Outputs the FinOps Economic Impact Report.
2. Safe Zero-Gravity Purge (purge)
Reclaims host storage and eliminates accumulated system deadweight:
code
Bash
./run.sh purge
What it does:
Safely vacuums system journal logs down to the last 3 days (preserving forensic logs for security and troubleshooting).
Cleans APT package cache archives without removing any installed applications.
Leaves user personal files, configurations, and running databases 100% untouched.
🔍 Understanding the Output Metrics
When you run scan, Antigravity presents a clean telemetry breakdown:
APT Package Cache: Residual package files downloaded during past updates. Safe to purge.
System Logs (Journal): Aggregated system logs. Antigravity trims these safely while preserving the last 72 hours.
Docker Cache / Images: Reclaimable layers identified from the Docker engine.
Zombie Processes: Processes that have completed execution but remain in the OS process table.
High-Memory Processes: Active processes consuming more than 15% of total system RAM.
FinOps Economic Waste: Real-time projected dollar savings upon executing cleanup.
📊 Vanilla Linux vs. Antigravity
Feature	Standard Linux	With Antigravity
Deadweight Visibility	Manual du, df, find, htop	Single-command instant audit
FinOps Dollar Projection	❌ None (Surprise AWS bills)	Live monthly/annual cost analysis
Journalctl Maintenance	Complex syntax & manual flags	One-click safe 3-day retention
Container Waste Scraper	Buried in verbose Docker commands	Calculated and reported upfront
Architecture Overhead	Heavy agents (Datadog/Prometheus)	Zero-overhead, local Python CLI
🛡️ Safety & Enterprise Reliability Policy
Antigravity follows strict Site Reliability Engineering (SRE) safety standards:
Zero Data Loss Guarantee: It strictly operates on system caches and logs. It will never alter or delete files in /home, source code directories, or application databases.
Forensic Log Preservation: Log vacuuming explicitly preserves the last 3 days of system events to ensure operational transparency is maintained.
Fault-Tolerant Execution: If Docker is not running or system permissions are restricted, Antigravity degrades gracefully and logs findings safely without crashing.
🗺️ Roadmap

v0.1.0: Core deadweight audit, FinOps economic calculator, and sandboxed purge.

v0.2.0: Automated cron daemon for scheduled weekly zero-bloat maintenance.

v0.3.0: Cloud provider telemetry sync (AWS CloudWatch, GCP Monitoring).

v0.4.0: Webhook alerting support for Slack and Discord DevOps channels.
👤 Author & Systems Suite
Crafted by Youssef (@EngJoDev) — Systems & DevOps Engineer.
🌐 The Open-Source Infrastructure Suite
⚡ Antigravity — Autonomous Linux Zero-Bloat & FinOps Engine.
🛠️ GhostOps — Autonomous Terminal SRE & DevOps Copilot for Linux Systems.
