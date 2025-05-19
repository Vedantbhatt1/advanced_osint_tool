import subprocess

def search_social_media(keyword):
    results = []
    try:
        output = subprocess.check_output(["snscrape", "--max-results", "5", f"twitter-search:{keyword}"], text=True)
        results = output.strip().split('\n')
    except Exception as e:
        results = [f"Social media scraping failed: {e}"]
    return results