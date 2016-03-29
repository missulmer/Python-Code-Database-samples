import urllib
from BeautifulSoup import *

url = raw_input('Enter ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_178010.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# retrieve all span tags
span_tag = soup('span')

tsum = 0
for span in span_tag:
    content_list = span.contents
    str_numb = content_list[0]
    numb = int(str_numb)
    tsum = tsum + numb

print tsum

""" What is happening in this code.  I am importing urllib
which gives me the ability to create a socket with a server and mimik a web browser. I provide the URL I am interested in connecting to.
From there I create variables to handle the socket creation and reading using urllib as well
as creating a variable to call the class I need, then I calling the  class BeautifulSoup(html)
which contains the code I need to parse HTML.  I am retreaving all the span tags.By creating a variable
content_list = span.contents, I am parsing out just the section of the tag which contains the data
I am interested in and stuffing in it str_numb.  From there I convert the unicode string to an int and then
sum my ints.  Lastly I print and taa daaa!"""