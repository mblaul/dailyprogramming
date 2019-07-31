## author Matt Blaul
## 12/8/2017

## Problem set: https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/
## Help from: https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python << Getting last item in list in Python

flag = False
num = 468
numList = []
primeList = []

def findLowerPrime(num):
    print("Find lower prime ...")
    for i in range(2,num+1):
        if (i==2):
            numList.append(i)
            primeList.append(i)
        else:
            for x in numList:
                if(x == numList[-1]):
                    primeList.append(i)
                else:
                    if(i % x == 0):
                        break
            numList.append(i)

def findUpperPrime(flag):
    print("Finding upper prime ...")
    while (flag == False):
        numList.append(numList[-1]+1)
        for x in numList:
            if(x == numList[-1]):
                primeList.append(numList[-1])
                flag = True
                break
            else:
                if (numList[-1] % x == 0):
                    break

findLowerPrime(num)
findUpperPrime(flag)
if(num in primeList):
    print(str(num) + " is a prime number!")
else:
    print(str(primeList[-2]) + " < " + str(num) + " < " + str(primeList[-1]))
