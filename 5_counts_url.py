#This code is to reach out into a url and read and parse an xml document to deliver a sum of the occurence of a piece of string data in int form.

import urllib
import xml.etree.ElementTree as ET

def main():
    url = get_user_input()
    xml = read_xml(url)
    count_str_list = count_str_collector(xml) #collect list of comment strings
    count_int_list = convrt_stringlst_2intlist(count_str_list)
    sum_int_list = sum_count_int_list(count_int_list)
    return sum_int_list

def main2():
    # also called "train wreck" or functional style
    return sum_count_int_list(convrt_stringlst_2intlist_2(count_str_collector(read_xml( get_user_input()))))

def get_user_input():
    url = raw_input('Enter URL ')
    if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_178007.xml"
    return url  # 'return' is the binder between the first layer of defintion and the variable receiving the result.

def read_xml(url):
    uh = urllib.urlopen(url)
    data = uh.read()
    uh.close() #free your resources!!
    return data

def count_str_collector(data):
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    return counts

def convrt_stringlst_2intlist(counts):
    convert_list = []
    for i in counts:
        convert_list.append(int(i.text))
    return convert_list

def convrt_stringlst_2intlist_2(counts):
    convert_list = [int(i.text) for i in counts] # this is called list comprehension
    return convert_list

def sum_count_int_list(count_int_list):
    sum = 0
    for i in count_int_list:
        sum = sum + i
    return sum

print main()
