def generate_report(domain_data, emails, social_results):
    with open("report.txt", "w") as f:
        f.write("=== OSINT REPORT ===\n\n")
        f.write(f"Domain: {domain_data['domain']}\n")
        f.write("\n--- WHOIS Data ---\n")
        f.write(domain_data['whois'] + "\n")

        f.write("\n--- DNS Records ---\n")
        for record_type, values in domain_data['dns'].items():
            f.write(f"{record_type} Records:\n")
            for value in values:
                f.write(f"  - {value}\n")

        f.write("\n--- Emails Found ---\n")
        for email in emails:
            f.write(f"  - {email}\n")

        f.write("\n--- Social Media Results ---\n")
        for line in social_results:
            f.write(f"{line}\n")