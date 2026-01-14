# IP Reputation Checker

This project simulates a basic IP reputation and IOC enrichment workflow commonly used in Threat Intelligence and SOC environments.

## Overview
The tool accepts an IP address as input and performs basic enrichment by:
- Validating the IP format
- Determining whether the IP is private or public
- Checking the IP against a simulated malicious indicator feed

## Why This Matters
Threat Intelligence analysts regularly enrich IP indicators to:
- Assess potential risk
- Prioritize alerts
- Support incident response investigations

This project demonstrates how simple automation can assist in early-stage threat analysis.

## How It Works
1. The user provides an IP address
2. The script validates the IP
3. The IP is checked against a local JSON-based indicator feed
4. The result is displayed in a clear, analyst-friendly format

## Files
- `ip_reputation.py` – Core logic for IP validation and reputation checks  
- `indicators.json` – Simulated malicious IP feed  
- `README.md` – Project documentation  

## Usage
```bash
python ip_reputation.py


