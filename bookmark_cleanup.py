#	Take FF or Chrome Bookmark htm, remove duplicates, group them....
# any other cleanup
#	Tue Jul 19 10:55:32 IST 2016

import lxml.html
import string
from sys import argv
from datetime import datetime

start=datetime.now()
script, input_file = argv

full_url = input_file   

image = lxml.html.parse(full_url)
url_list = image.xpath("//a/@href")	

url_list.sort()
#print "*********** All URL's before Duplicate & Sort *********** "
#for each in url_list:
	#print each
print "Total no. of URL = ", len(url_list)

url_list = list(set(url_list))		


print "*********** All URL's after Duplicate & Sort *********** "
#for each in url_list:	print each
print "Total no. of URL after dup remove= ", len(url_list)

end=datetime.now()

run_time = end - start
print "run time = ", run_time
