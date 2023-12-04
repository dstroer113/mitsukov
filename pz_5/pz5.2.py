import math

def TrianglePS(a):
    P, S = (3 * a), (a**2 * math.sqrt(3/4))
    print(P,S)

a, b, c = float(input()), float(input()), float(input())
TrianglePS(a),  TrianglePS(b), TrianglePS(c)



