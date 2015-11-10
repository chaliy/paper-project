from math import *

# Body

R = 20
D = R*2
C = pi * D
C2 = C/4
C3 = C2/2

print("Body: width: %(C)d, C2: %(C2)f, C3: %(C3)f" % locals())

# Nose
H = 50
L = sqrt(H**2 + R**2)
A = (pi * L * (C)) / 180
A2 = (pi * L * (C + 25)) / 180

print("Nose: radious(L): %(L)d, angle(A): %(A)d, angle with white(A2): %(A2)d" % locals())

A3 = A/3
A4 = A3/2
L2 = L + 15

print("Node handles: angle(A3): %(A3)d, angle side(A4): %(A4)d, (L2): %(L2)d" % locals())
