import requests


class WaybackMachine:
    def __init__(self, domain):
        self.domain = domain

    def fetch_urls(self):
        response = requests.get(
            f"https://web.archive.org/cdx/search/cdx?url=*.{self.domain}/*&output=json&collapse=urlkey",
            timeout=30,
        )
        if response.status_code == 200:
            return [entry[2] for entry in response.json()[1:]]
        return []


class URLSaver:
    def __init__(self, filename):
        self.filename = filename

    def save(self, urls):
        with open(self.filename, "w") as file:
            for url in urls:
                file.write(f"{url}\n")


if __name__ == "__main__":
    domain = input("Enter the domain (example.com): ")
    save_name = input("Enter the name for the output (please add .txt at the end): ")

    wayback_machine = WaybackMachine(domain)
    urls = wayback_machine.fetch_urls()

    print("Collected URLs:")
    for url in urls:
        print(url)

    url_saver = URLSaver(save_name)
    url_saver.save(urls)

    print(f"Finished saving URLs to '{save_name}'")
