import subprocess
import json

def scrape_amazon(query: str):
    try:
        result = subprocess.run(['python', 'scraper/playwright_worker.py', query], capture_output=True, text=True,  check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        raise
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Raw output: {result.stdout}")
        raise
