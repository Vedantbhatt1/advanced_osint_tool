import whois
import dns.resolver

def perform_domain_recon(domain):
    results = {"domain": domain, "whois": "", "dns": {}}
    try:
        results["whois"] = str(whois.whois(domain))
    except Exception as e:
        results["whois"] = f"WHOIS lookup failed: {e}"

    for record in ['A', 'MX', 'NS']:
        try:
            answers = dns.resolver.resolve(domain, record)
            results["dns"][record] = [str(rdata) for rdata in answers]
        except Exception as e:
            results["dns"][record] = [f"{record} lookup failed: {e}"]

    return results