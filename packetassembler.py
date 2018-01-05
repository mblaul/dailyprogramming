## author Matt Blaul
## 1/3/2018

## Problem set: https://www.reddit.com/r/dailyprogrammer/comments/72ivih/20170926_challenge_333_easy_packet_assembler/

import re

handle = open("packetassembler/datastream.txt")

lst = list()


for line in handle:
    line = re.split(r'\s*',line)
    lst.append(line)
sorted_list = sorted(lst)
for x in sorted_list:
