# DNS OSINT Recon Tool

## Overview
The DNS OSINT Recon Tool is a Python-based reconnaissance tool that performs passive DNS enumeration using a customizable subdomain wordlist. It discovers publicly accessible subdomains, retrieves their IPv4 (A) records, and performs reverse DNS lookups to gather additional information about the discovered hosts.
This project was developed to strengthen Python programming skills while learning reconnaissance techniques commonly used in cybersecurity.

## Features

- Performs DNS A record lookups for discovered subdomains.
- Conducts reverse DNS lookups on resolved IP addresses.
- Uses a customizable wordlist for subdomain enumeration.
- Handles common DNS exceptions gracefully.
- Measures and displays total scan execution time.
- Presents results in a clean and readable format.

## Technologies Used

- **Python 3**
- **dnspython** – Performs DNS queries.
- **socket** – Performs reverse DNS lookups.
- **time** – Measures scan execution time.
- **Git** – Version control.
- **GitHub** – Project hosting and collaboration.

## Project Structure

```text
dns-osint-tool/
│
├── dns_osint.py        # Main application
├── subdomains.txt      # Wordlist used for subdomain enumeration
├── README.md           # Project documentation
└── .gitignore          # Files ignored by Git
```

## How It Works

1. The user specifies a target domain.
2. The tool reads a list of potential subdomains from `subdomains.txt`.
3. Each subdomain is combined with the target domain.
4. The tool performs DNS A record lookups for each generated subdomain.
5. If a subdomain is successfully resolved, its IP address is recorded.
6. A reverse DNS lookup is performed on each discovered IP address.
7. The discovered information is displayed along with a scan summary and execution time.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.10 or later
- Git
- `dnspython` (installed automatically using `requirements.txt`)

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.10 or later
- Git

## Installation

```bash
git clone https://github.com/AfifaNaser/dns-osint-tool.git

cd dns-osint-tool

pip install -r requirements.txt
```

## Usage

Run the following command from the project directory:

```bash
python dns_osint.py
```

The script performs DNS reconnaissance against the target domain specified in the source code and displays the discovered subdomains, their IP addresses, reverse DNS information, and a scan summary.

## Example Output

```text
============================================================
DNS OSINT RECON TOOL
============================================================
Target Domain : google.com

Discovered Subdomains
============================================================

Domain      : www.google.com
IP Address  : 142.251.154.119
Reverse DNS : None

------------------------------------------------------------

Domain      : mail.google.com
IP Address  : 142.250.187.5
Reverse DNS : lcmcta-ai-in-f5.1e100.net

------------------------------------------------------------

============================================================
SCAN SUMMARY
============================================================
Target Domain : google.com
Results Found : 35
Scan Time     : 2.84 seconds
```

## Future Improvements

- Accept the target domain as a command-line argument.
- Support additional DNS record types (AAAA, MX, NS, TXT, and CNAME).
- Export scan results to CSV.
- Add colored terminal output for improved readability.
- Display scan progress during execution.

## Disclaimer

This project was developed for educational purposes to demonstrate Python programming and DNS reconnaissance techniques. It should only be used to gather information about systems and domains that you own or have explicit permission to assess.
