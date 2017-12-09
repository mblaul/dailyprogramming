## author Matt Blaul
## 12/8/2017

## Problem set: https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/

onedigprimes =  [2,3,5,7,13]

test = 0
num = 169

for x in onedigprimes:
    if (num % x == 0):
        print("This is not a prime")
        break
    if (num % x != 0):
        test += 1
        if(test == 5):
            print(str(num) + " is a prime!")
