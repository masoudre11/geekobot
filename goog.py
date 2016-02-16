import urllib.request
import urllib.parse
import re
from pyquery import PyQuery as pq

imgpat = re.compile('imgurl=([^>]+)&amp;imgrefurl')

def get_images(q):
    url     = "https://www.google.com/search?site=&tbm=isch&q=%s#q=%s&tbm=isch"%(
            urllib.parse.quote_plus(q), urllib.parse.quote_plus(q))
    agent   = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    headers = {'User-Agent':agent,}
    request = urllib.request.Request(url,None,headers)
    results = urllib.request.urlopen(request)
    images  = imgpat.findall(results.readall().decode())
    return images

def get_search(q):
    url     = "https://www.google.com/search?q=%s&ie=UTF-8#q=%s"%(
                urllib.parse.quote_plus(q), urllib.parse.quote_plus(q))
    agent   = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    headers = {'User-Agent':agent,}
    request = urllib.request.Request(url,None,headers)
    results = pq(urllib.request.urlopen(request).readall().decode())
    links   = []
    for x in results('.rc'):
        x = pq(x)
        links += [(x('h3').text(), x('.st').text(), x('a').attr('href'))]
    return links

#print(get_images('banana')[0])
