# MerkleMapper

**MerkleMapper** is a Python-based CLI tool that leverages the MerkleMap API to extract subdomains for a given domain and resolve their respective IP addresses. The tool supports both single domain and batch processing of domains from a file. Results are saved in a structured JSON format for further analysis.

## Features

- Fetches **all subdomains** of a given domain using MerkleMap's paginated API.
- Resolves IP addresses of the retrieved subdomains.
- Supports both single domain and bulk domain processing from a file.
- Saves results in a JSON file for easy access and automation.
- Simple, modular, and easy to use.

## Requirements

The tool requires **Python 3.6+** and the following Python package:
- `requests`

Install the dependencies using the following command:
```bash
pip install -r requirements.txt
