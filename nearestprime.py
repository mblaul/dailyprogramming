## author Matt Blaul
## 12/8/2017

## Problem set: https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/
## Help from: https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python << Getting last item in list in Python

flag = False
num = 169
numList = []
primeList = []

def findLowerPrime(num):
    print("Find lower prime: ")
    for i in range(2,num+1):
        if (i==2):
            numList.append(i)
            primeList.append(i)
        else:
            for x in numList:
                if(i % x == 0):
                    break
                else:
                    if(x == len(numList)+1):
                        print(str(i) + " is a prime")
                        primeList.append(i)
            numList.append(i)

def findUpperPrime(num,flag):
    print("Find upper prime")
    while(flag == False):
        numList.append(num+1)
        for i in range(2,len(numList)+1):
            for x in numList:
                if(i % x != 0):
                    if(x == len(numList)+1):
                        print(str(i) + " is a prime")
                        primeList.append(i)
                        flag = True



findLowerPrime(num)
print(str(primeList[-1]))
findUpperPrime(num,flag)
