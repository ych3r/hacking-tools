from re import sub
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

def bing_search(site, pages):
    subdomain = []
    headers = {}
    
    for i in range(1, int(pages) + 1):
        url = "https://cn.bing.com/search?q=site%3a" + site + "&go=Search&qs=ds&first=" + str((int(i) - 1) * 10) + "&FORM=PERE"
        conn = requests.session()
        conn.get('http://cn.bing.com', headers=headers)
        html = conn.get(url, stream = True, headers = headers, timeout = 8)
        soup = BeautifulSoup(html.content, 'html.parser')
        job_bt = soup.findAll('h2')
        for i in job_bt:
            link = i.a.get('href')
            domain = str(urlparse(link).scheme + "://" + urlparse(link).netloc)
            if domain in subdomain:
                pass
            else:
                subdomain.append(domain)
                print(domain)

def main():
    if len(sys.argv) == 3:
        site = sys.argv[1]
        page = sys.argv[2]
    else:
        print("usage: %s xx.com 10" % sys.argv[0])
        sys.exit(-1)
    subdomain = bing_search(site, page)

if __name__ == '__main__':
    main()