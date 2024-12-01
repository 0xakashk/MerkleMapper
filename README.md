# MerkleMapper

**MerkleMapper** is a Python-based CLI tool that leverages the MerkleMap API to extract subdomains for a given domain and resolve their respective IP addresses. The tool supports both single domain and batch processing of domains from a file. Results are saved in a structured JSON format for further analysis.

About MerkleMap : MerkleMap offers a comprehensive solution for subdomain enumeration, certificate transparency monitoring, and infrastructure discovery. Uncover hidden assets, investigate suspicious domains, and gain valuable insights with ease. 


## Features

- Fetches **all subdomains** of a given domain using MerkleMap's paginated API.
- Resolves IP addresses of the retrieved subdomains.
- Supports both single domain and bulk domain processing from a file.
- Saves results in a JSON file for easy access and automation.
- Simple, modular, and easy to use.

## Requirements

The tool requires **Python 3.6+** and the following Python package:
- `requests`

## Usage
1. Process a Single Domain : To fetch all subdomains and their IPs for a single domain:
```bash
python MerkleMapper.py -d example.com
```
   
2. Process Multiple Domains from a File ; Create a text file (e.g., domains.txt) with one domain per line, then run:
```bash
python MerkleMapper.py -f domains.txt
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/<your-username>/MerkleMapper.git
cd MerkleMapper
```

2. Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```



