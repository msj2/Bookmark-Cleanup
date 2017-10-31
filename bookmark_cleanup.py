'''	Take FF or Chrome Bookmark htm, remove duplicates, group them....
# any other cleanup
#	Tue Jul 19 10:55:32 IST 2016
'''
# "(should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)"
from sys import argv
import lxml.html
LC_INPUT_FILE = argv
FULL_URL = LC_INPUT_FILE
IMAGE = lxml.html.parse(FULL_URL)
URL_LIST = IMAGE.xpath("//a/@href")
URL_LIST .sort()
URL_LIST = list(set(URL_LIST))
print "Total no. of URL after dup remove= ", len(URL_LIST)
# Your code has been rated at 10.00/10 (
