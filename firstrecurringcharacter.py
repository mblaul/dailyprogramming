## author Matt Blaul
## 12/7/2017
## Problem set: https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/
## Script to find find recurring character in a given string
## Resources used: https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3

import re

input = ["IKEUNFUVFV",
        "PXLJOUDJVZGQHLBHGXIW",
        '*l1J?)yn%R[}9~1"=k7]9;0[$'
        ]

for x in input:
    print(x)
    check = []
    for y in x:
        if y in check:
            print("Match found: " + y)
            break
        else:
            check.append(y)
