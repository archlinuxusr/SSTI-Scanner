import requests


class URLScraper:
    def __init__(self, domain):
        self.domain = domain

    def fetch_wayback_urls(self):
        url = f"https://web.archive.org/cdx/search/cdx?url=*.{self.domain}/*&output=json&collapse=urlkey"
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            return [entry[2] for entry in response.json()[1:]]
        return []

    def fetch_common_crawl_urls(self):
        url = f"http://index.commoncrawl.org/CC-MAIN-2023-22-index?url=*.{self.domain}/*&output=json"
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            return [entry["url"] for entry in response.json()]
        return []

    def filter_urls(self, urls):
        return set(url for url in urls if "?" in url)
