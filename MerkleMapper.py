import argparse
import requests
import os
import json
import socket
import time  # Added for delay between API requests

# Fetch subdomains using MerkleMap API
def fetch_subdomains(domain):
    api_url = "https://api.merklemap.com/search"
    all_subdomains = []
    page = 0  # Start with the first page

    try:
        while True:
            params = {"query": domain, "page": page}
            response = requests.get(api_url, params=params, timeout=15)

            if response.status_code == 200:
                data = response.json()

                # Debugging: Log page results
                print(f"Page {page}: {len(data.get('results', []))} subdomains fetched.")

                results = data.get("results", [])
                if not results:  # Break if no more results
                    break
                subdomains = [item["domain"] for item in results]
                all_subdomains.extend(subdomains)
                page += 1  # Move to the next page

                # Add delay to avoid rate limiting
                time.sleep(1)
            else:
                print(f"Failed to fetch subdomains for {domain} (Status code: {response.status_code})")
                break
    except requests.RequestException as e:
        print(f"Failed to fetch subdomains for {domain}: {e}")
    
    # Remove duplicates
    return sorted(set(all_subdomains))  # Sort results for clarity

# Resolve IP address for a given subdomain
def resolve_ip(subdomain):
    try:
        return socket.gethostbyname(subdomain)
    except socket.gaierror:
        return "N/A"

# Save results to a file
def save_results(domain, subdomains_info):
    if not os.path.exists("results"):
        os.makedirs("results")
    json_file_path = os.path.join("results", f"{domain}_results.json")
    with open(json_file_path, "w") as json_file:
        json.dump({"domain": domain, "subdomains": subdomains_info}, json_file, indent=4)
    print(f"Results saved to {json_file_path}")

# Process a single domain and display results
def process_single_domain(domain):
    print(f"\nProcessing Domain: {domain}")
    subdomains = fetch_subdomains(domain)
    if subdomains:
        subdomains_info = []
        print("-------------------------------------------------")
        print(f"Subdomains and IPs for {domain}:")
        for subdomain in subdomains:
            ip_address = resolve_ip(subdomain)
            print(f"  - Subdomain: {subdomain}, IP: {ip_address}")
            subdomains_info.append({"subdomain": subdomain, "ip_address": ip_address})
        save_results(domain, subdomains_info)
        print("-------------------------------------------------")
    else:
        print(f"No subdomains found for {domain}.")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Extract subdomains and IP addresses using MerkleMap API.")
    parser.add_argument("-d", "--domain", help="Single domain to process.")
    parser.add_argument("-f", "--file", help="File containing a list of domains to process.")
    args = parser.parse_args()

    if args.domain:
        process_single_domain(args.domain)
    elif args.file:
        with open(args.file, "r") as file:
            domains = [line.strip() for line in file if line.strip()]
            for domain in domains:
                process_single_domain(domain)
    else:
        print("Please specify either a domain (-d) or a file (-f).")

if __name__ == "__main__":
    main()
