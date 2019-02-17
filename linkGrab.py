import urllib.request
import re
import wikipedia

mp = 'http://en.wikipedia.org/wiki/Main_Page'  #Main page url
def get_links(source_url):

    link_exp = re.compile('(?:a href=("\/wiki\/[^:]*?"))')
    page = urllib.request.urlopen(source_url)
    page_html = str(page.read())

    links = set()

    for link in link_exp.findall(page_html):
        links.add(link[7:-1])
    links.discard(mp)               
    
    return links    #returns a set of all links from a page except the link to the main page


