from url_scraper import URLScraper
from tinja_scanner import SSTIScanner


def main():
    domain = input("Domain (e.g., example.com): ").strip()
    scraper = URLScraper(domain)

    wayback_urls = scraper.fetch_wayback_urls()
    common_crawl_urls = scraper.fetch_common_crawl_urls()
    all_urls = wayback_urls + common_crawl_urls

    unique_urls = scraper.filter_urls(all_urls)

    cookies = input("Cookies (or Enter to skip): ").strip() or None
    rate_limit = input("Max requests per second (or Enter to skip): ").strip() or None

    SSTIScanner.execute_tinja_scan(unique_urls, cookies, rate_limit)


if __name__ == "__main__":
    main()
