import re
import os

log_dir = "data_dir"
log_file = "log.txt"
log_path = log_dir+"/"+log_file
print (log_path)

f = open(log_path,'r')
count = 0

for line in f:
    if re.search("^Aug",line):
        count += 1

print (count)


for count in range(1,16):
    if count % 3 == 0:
        print ("fizz", end=' ')
        if count % 5 == 0:
            print ("buzz", end=' ')
    elif count % 5 == 0:
            print ("buzz", end=' ')
    else:
        print (count, end=' ')
    print ()
