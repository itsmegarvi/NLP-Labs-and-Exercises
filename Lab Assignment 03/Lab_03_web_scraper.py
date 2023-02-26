import requests
import string
import math
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.wired.com/2017/02/life-death-spring-disorder/'

# Send a GET request to the website
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

# Extract the text from the HTML content
blacklist = ['[document]', 'noscript', 'header',
             'html', 'meta', 'head', 'input', 'script', 'style']

output = ''

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)
# Save the text to a file
with open('Lab_03_data1.txt', 'w', encoding='utf-8') as file:
    file.write(output)

# psmag.comPlease enable JS and disable any ad blocker error comes in the text file
# This web scraping attempt was a failure

# Nope Got it working Ps - Took a different blog to scrape (How life(and death) spring from diorder)

# Removed extra text from above and below the blog manually