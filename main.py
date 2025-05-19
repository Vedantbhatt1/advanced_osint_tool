from modules.domain_recon import perform_domain_recon
from modules.email_scraper import scrape_emails
from modules.social_scraper import search_social_media
from modules.report import generate_report

def main():
    domain = input("Enter domain to analyze: ")
    domain_data = perform_domain_recon(domain)

    url = input("Enter URL for email scraping: ")
    emails = scrape_emails(url)

    keyword = input("Enter keyword for social media search: ")
    social_results = search_social_media(keyword)

    generate_report(domain_data, emails, social_results)
    print("[*] Report saved to report.txt")

if __name__ == "__main__":
    main()