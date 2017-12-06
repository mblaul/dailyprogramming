## author Matt Blaul
## 12/5/2017

## Script to divide polynomials

from numpy.polynomial import polynomial as P

## Enter polynomial coefficients starting with lowest e.g. (c,x^1,x^2,...)
q = (3,-6,2,4)
d = (-3,1)

###NumPy is used to perform the dirty work. Output is 2 arrays: [0] is the quotient, [1] is the remainder
sol = P.polydiv(q,d)

coeff = 0
for x in sol[0]:
        if (coeff < 1):
            readablepoly = str(x)
            coeff += 1
        elif (coeff == 1):
            readablepoly = str(x) + "x" + " + " + readablepoly
            coeff += 1
        else:
            readablepoly = str(x) + "x^" + str(coeff) + " + " + readablepoly
            coeff += 1

print("Quotient: " + readablepoly + "  |  Remainder: " + str(int(sol[1])))
