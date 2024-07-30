import subprocess
import json

def scrape_amazon(query: str):
    result = subprocess.run(['python', 'scraper/app/core1.py', query], capture_output=True, text=True,  check=True)
    return json.loads(result.stdout)
    
