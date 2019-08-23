import re
import os

log_dir = "data_dir"
log_file = "log.txt"

print (log_dir, log_file)

def log_format(log_line):
    split_log_line = log_line.split()
    return {
        month : split_log_line[0],
        date : split_log_line[1],
        time : split_log_line[2],
        info : split_log_line[3:],
    }

