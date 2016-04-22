#!/usr/bin/python

# Open a file
from datetime import datetime

# define a timestamp format you like
FORMAT = '%Y%m%d%H%M%S'
path = 'foo.txt'
data = 'data to be written to the file\n'
new_path = '%s_%s' % (datetime.now().strftime(FORMAT), path)
fo = open("foo.txt", "wb")
print(new_path)
fo.write( "Python is a great language.\nYeah its great!!\n");
fo.write("%s \r\n" %new_path)
# Close opend file
fo.close()
