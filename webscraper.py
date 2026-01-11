import requests

from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('a')
    print("Links found on the page:")
    for link in links:
        print(link.get('href'))

scrape_website('https://www.google.com/')