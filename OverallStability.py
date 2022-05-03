frictionSita = [-58, -45, -36, -28, -21, -14, -7, 0, 7, 14,	21,	28,	36,	45,	55,	81]
h_j= [2.1, 5.3, 7.0, 8.2, 9.1, 9.7, 10.1, 10.2, 10.1, 19.8, 19.2, 18.3, 17.0, 15.3, 12.9, 5.7]
gama = [18.5, 19.2, 19.4, 19.3, 19.7, 19.3, 19.7, 21.5, 19.1]
h = [3.4, 4.2, 1.2, 1.7, 2.3, 1.6, 2.3, 1.4, 3.9]
import math

'''
#输出滑弧段长度Ld
for i in range(-7, 9):
    if i == -7:
        b = 2.7
    elif i == 8:
        b = 2.1
    else:
        b = 2.0

    lenth = b/math.cos(math.radians(frictionSita[i+7]))
    print("l%d = b%d/cosθ%d = %.1f/cos(%d°) = %.2f" %(i, i, i, b, frictionSita[i+7], lenth))
'''

#天然重度∆G=h_j*γ_j*b_j*a
a = 1.6
for i in range(-7, 9):
    print("∆G%d ="%(i), end="")

    if i == -7:
        b = 2.7
    elif i == 8:
        b = 2.1
    else:
        b = 2.0

    if i <= 1:
        G_delta = 0.46 * gama[3]
        h_0 = h_j[i+7] - 0.46
        print("%.2f ×%.2f ×%.2f ×%.2f +" %(0.46, gama[3], b, a), end="")
        n = 4
        while(h_0 > 0 ):
            if h_0 - h[n] > 0:
                h_0 = h_0 - h[n]
                G_delta = G_delta + h[n]*gama[n]*b*a
                print("%.2f ×%.2f ×%.2f ×%.2f +" %(h[n], gama[n], b, a), end="")
            else:
                G_delta = G_delta + h_0*gama[n]*b*a
                print("%.2f ×%.2f ×%.2f ×%.2f" %(h_0, gama[n], b, a), end="")
                h_0 = h_0 - h[n]
            n = n + 1
    else:
        h_0 = h_j[i+7]
        n = 0
        G_delta = 0
        while(h_0 > 0):
            if h_0 - h[n] > 0:
                h_0 = h_0 - h[n]
                G_delta = G_delta + h[n]*gama[n]*b*a
                print("%.2f ×%.2f ×%.2f ×%.2f +" %(h[n], gama[n], b, a), end="")
            else:
                G_delta = G_delta + h_0*gama[n]*b*a
                print("%.2f ×%.2f ×%.2f ×%.2f" %(h_0, gama[n], b, a), end="")
                h_0 = h_0 - h[n]
            n = n + 1

    print(" =%.2fkN" %(G_delta))
