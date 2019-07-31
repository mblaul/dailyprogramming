## author Matt Blaul
## 12/7/2017
## Problem set: https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/
## Script to find find recurring character in a given string
## Resources used: https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3

def ffrc(stringtosearch):
    print("Entered module")
    print(stringtosearch)
    for x in stringtosearch:
        check = []
        if x in check:
            print("Match found: " + x)
        else:
            check.append(x)
