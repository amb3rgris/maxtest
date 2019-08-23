import re
import os

log_dir = "data_dir"
log_file = "log.txt"

log_path = log_dir+"/"+log_file

f = open(log_path,'r')

count = 0
for line in f:
    if re.search("^Aug",line):
        count += 1
print ("lines with string \"Aug\": ",count)
f.close()

f = open(log_path,'r')

count2 = 0
for line in f:
    line_month, line_date, line_time, line_info = line.split(" ",3)
    line_time_hour, line_time_minute, line_time_second = line_time.split(":",2)
    if line_time_hour == "07":
        if int(line_time_minute) >= 0 and int(line_time_minute) <= 15:
            count2 += 1
print ("lines with timestamp between 07:00 and 07:15: ",count2)
f.close()

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
