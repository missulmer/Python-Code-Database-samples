import ssl
import urllib
from BeautifulSoup import *


def get_last_name(in_url, link_position, count):
    name = None
    arg_url = in_url
    for i in xrange(count):
        (name, out_url) = get_name_url_by_pos(arg_url, link_position)
        print arg_url, name
        arg_url = out_url
    return name

def get_name_url_by_pos(in_url, link_position):
    name = None
    out_url = None
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(in_url, context=scontext)
    html = uh.read()
    soup = BeautifulSoup(html)
    a_tag_list = soup('a')
    a_tag_nth = get_nth_a_href(a_tag_list, link_position)
    name = a_tag_nth.contents[0]
    out_url = a_tag_nth['href']
    return (name, out_url)

def get_nth_a_href(a_tag_list, link_position):
    href_list = []
    for tag in a_tag_list:
        if tag['href']:
            href_list.append(tag)
    return href_list[link_position]


url = raw_input('Enter URL ')
if len(url) < 1 : url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Elis.html "

position =  raw_input('Enter Position ')
if len(position) < 1 :
    position = 18
else:
    position = int(position)

count = raw_input('Enter Count')
if len(count) < 1 :
    count = 7
else:
    count = int(count)


print get_last_name(url, position - 1, count)

# retrieve all href tags
# a_tag = soup('a')


#html = urllib.urlopen(url).read()
#