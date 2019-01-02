from bs4 import BeautifulSoup
import urllib3
import re

links = []
site = "https://alextech18.blogspot.com"
pattern = "://alextech18.blogspot.com"
 
def getLinks(url, pattern, html_only=True):

    http = urllib3.PoolManager()
    html_page = http.request('GET', url)

    soup = BeautifulSoup(html_page.data, features="html.parser")

    # Use separate pattern, because, blogspot for example, can use links leading with http and https
    for link in soup.findAll('a', attrs={'href': re.compile(pattern)}):
      if link.get('href') not in links:
        if html_only:
            if ".html" == link.get('href')[-5:]:
              links.append(link.get('href'))
        else:
            links.append(link.get('href'))

    print(len(links))
 
    return links

def main():
    getLinks(site, pattern)
    print("----------Links from main page-----------")
    print(links)

    for link in links:
        print("----------LINK-----------")
        print(link)
        getLinks(link, pattern)

    print(links)

if __name__ == "__main__":
    main()
