import solver
import cube

import re
import json
from bs4 import BeautifulSoup as bs
import requests

# Setup.
site = 'http://127.0.0.1:5555/frontend/rubiks.html'
exp = '^[\n\s]+sessionStorage.setItem\(.*JSON.stringify\((?P<content>{.*})\)\)'

r = requests.get(site)
if r.status_code == 200:
    soup = bs(r.text, features="html.parser")
    # Extract all <script> tags from the full HTML.
    scripts = soup.findAll('script')
    # Loop through all <script> tags until sessionStorage is found.
    script = [s.string for s in scripts if 'sessionStorage' in s.decode()]
    print("script:", scripts)
    # Use regex (with a named capture group) to extract the JSON data.
    m = re.match(exp, script[0])
    if m:
        content = m['content']
        # Convert scraped JSON data to a dict.
        data = json.loads(content)

print(data)
