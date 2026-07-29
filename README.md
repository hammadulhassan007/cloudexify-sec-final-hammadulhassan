# CloudExify Cybersecurity Month 1 Final Project: Cryptography & Network Security

This repository contains the complete implementation of Applied Cryptography, Secure Authentication Systems, Web Integration, and Network Reconnaissance Labs for the **CloudExify Cybersecurity Summer Internship 2026**.

---

## 📌 Project Overview

This project delivers a multi-layered security implementation covering both **Application Security** (Password Hashing, Web UI, Symmetric Encryption) and **Network Security** (Active Port Scanning & Packet Capture Analysis).

### Key Features & Architecture:

1. **Secure Authentication Engine (`secure_auth.py`)**:
   * **Bcrypt Salted Hashing**: Replaces plain-text password storage with cryptographic bcrypt hashes, preventing rainbow table attacks.
   * **Password Policy Enforcement**: Validates user passwords against strength requirements (minimum 8 characters, uppercase, lowercase, numbers, and special symbols).
   * **Brute-Force Protection**: Implements dynamic rate-limiting and account lockout after 3 consecutive failed login attempts.
   * **Data Persistence**: Stores hashed credentials securely inside `users.json`.

2. **Web Portal Demo Interface (`app.py`)**:
   * Flask-based web server providing a dynamic UI for live authentication testing.
   * Features interactive flash notifications for security policy violations, successful registrations, and locked accounts.

3. **Data Protection & Key Management (`encryption_examples.py`)**:
   * Uses **Fernet (AES-128 Symmetric Encryption)** to encrypt sensitive data at rest/in transit.
   * **Persistent Key Management**: Automatically generates, saves, and reloads encryption keys via `secret.key`.
   * Formatted terminal output for verification and cryptographic integrity checks.

4. **Network Reconnaissance & Traffic Labs (`nmap_and_wireshark_labs/`)**:
   * **Nmap Scanning**: Local host port discovery and active service enumeration (`nmap_scan.png`).
   * **Wireshark Analysis**: Packet sniffing artifacts (`wireshark_http_capture.png`) demonstrating plain-text HTTP vulnerabilities and highlighting the critical need for HTTPS/TLS encryption (`wireshark_findings.txt`).

---

## 📁 Repository Structure

```text
├── secure_auth.py                 # Core Password Hashing, Validation & Lockout Logic
├── app.py                         # Flask Web Application Interface
├── encryption_examples.py         # Symmetric Encryption (Fernet AES) Engine
├── README.md                      # Technical Project Documentation
├── penetration_test_report.pdf    # Vulnerability Assessment Report
└── nmap_and_wireshark_labs/       # Network Scanning & Sniffing Artifacts
    ├── nmap_scan.png              # Local Port Scan Screenshot
    ├── wireshark_http_capture.png # Wireshark HTTP Packet Capture Proof
    └── wireshark_findings.txt     # Traffic Analysis & Audit Findings
