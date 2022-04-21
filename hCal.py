Ea = [117.89, 253.05, 67.97, 146.37, 234.03, 220.47, 318.14, 218.13, 955.43, 452.67]
ya = [0.79, 1.75, 0.57, 0.81, 1.11, 0.78, 1.12, 0.69, 1.88, 1.13]
Ep = [25.6, 255.04, 309.66, 621.29, 475.27, 1389.76, 1421.39]
yp = [0.17, 0.99, 0.77, 1.08, 0.68, 1.85, 1.12]
h = [ 3.4, 4.2, 1.2, 1.7, 2.3, 1.6, 2.3, 1.4, 3.9, 2.3, 50]
distanceA = [2.61, 4.25, 6.63, 8.09, 10.09, 12.02, 13.98, 15.81, 18.52]
distanceB = [1.53, 3.01, 4.83, 6.82, 8.62, 11.35, 14.38]
T1 = 125
T2 = 250
T3 = 250
import math

n = 0
bendL = 0
bestDepth = 0
for depth in range(10, 27):
    bendA = 0
    bendB = 0
    for i in range (0, 9):
        if distanceA[i] > depth:
            break
        else:
            bendA += Ea[i] * (depth - distanceA[i])
    for i in range (0, 7):
        if distanceB[i] > depth:
            break
        else:
            bendB += Ep[i] * (depth - 8.8 - distanceB[i])
    bendAns = T1 * (depth - 0.5) + T2 * (depth - 4.5) + T3 * (depth - 8.5) + bendB - bendA
    n +=1
    print(str(depth) + "m: " + str(bendAns))
###    print(bendA)
###    print(bendB)
    print()
    if n == 0 :
        bendL = bendAns
    elif abs(bendL) > abs(bendAns):
        bendL = bendAns
        bestDepth = depth
print(bestDepth)