# Port Scanner

A Python script that scans common ports on a list of hosts and reports which ones are open.

## How it works

Reads hosts from `targets.txt` and attempts to connect to the most common ports using TCP sockets. Reports open ports for each host.

## Scanned portsgit

21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 80 (HTTP), 110 (POP3), 143 (IMAP), 443 (HTTPS), 3306 (MySQL), 5432 (PostgreSQL), 8080 (HTTP Alt), 8443 (HTTPS Alt)

## Usage

Add the hosts you want to scan to `targets.txt`, one per line:

google.com
github.com
192.168.1.1


Then run:

python main.py


## Example output
==================================================
Port Scanner — 2026-10-04 22:00:00

Scanning host: google.com
Open ports on google.com: 80, 443

Scanning host: github.com
Open ports on github.com: 22, 443


## Technologies

- Python 3
- socket (TCP port scanning)
- datetime (timestamp)

## Disclaimer

This tool is intended for educational purposes and authorized testing only. Never scan hosts without permission.