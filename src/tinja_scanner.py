import subprocess


class SSTIScanner:
    @staticmethod
    def execute_tinja_scan(urls, cookies=None, rate_limit=None):
        command = ["tinja", "url"]

        if urls:
            for url in urls:
                command.extend(["-u", url])
        else:
            print("No unique URLs found. Exiting scan.")
            return

        if cookies:
            command.extend(["-c", cookies])

        if rate_limit:
            command.extend(["--ratelimit", str(rate_limit)])

        print(f"Running: {' '.join(command)}")

        subprocess.run(command, stderr=subprocess.STDOUT)
