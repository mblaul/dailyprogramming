## author Matt Blaul
## 12/16/2017

#### Problem set: https://www.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/
## Help from: https://stackoverflow.com/questions/699866/python-int-to-binary << Convert int to binary

num = 20


print("{0:b}".format(num))

for x in range (0,num+1):
    binx = "{0:b}".format(x)
    
