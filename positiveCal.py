yp = [0.17, 0.99, 0.77, 1.08, 0.68, 1.85, 1.12]
h = [1.7, 2.3, 1.6, 2.3, 1.4, 3.9, 2.3]

for i in range(0, 7):
    sum = 0
    j = 0
    while (j <= i):
        sum += h[j]
        j+=1
    print(round(sum - yp[i],2))
