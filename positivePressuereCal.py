fai = [11.6,20.6,23,9.8,22.3,28]
c = [35.9,15,5,32.2,14.8,21.5]
gama = [ 19.3, 19.7,21.5,19.1,19.8,21.5]
h = [ 1,5.9,1.7,9.8,1.7,50]
flag = [ 0, 0, 1, 0,0,1]

import math

q = 0
for i in range(0,6):
    K = round(pow(math.tan(math.radians(45 + fai[i]/2)), 2), 2)
    if(flag[i]):
        u= 10*h[i]
        p_up = q*K + 2*c[i]*pow(K,0.5)
        q = q + gama[i]*h[i]
        p_low = (q-u)*K + 2*c[i]*pow(K,0.5) + u

        print("（" + str(i+1) +"）第" + str(i+1) + "层被动土压力（水土分算）")
        print("地下水压力：")
        print("u = " + str(u) + "kPa")
    else:
        print("（" + str(i+1) +"）第" + str(i+1) + "层被动土压力（水土合算）")
        p_up = q*K + 2*c[i]*pow(K,0.5)
        q = q + gama[i]*h[i]
        p_low = q*K + 2*c[i]*pow(K,0.5)

    E = 0.5 * ( p_up + p_low ) * h[i]
    y = h[i]/3 * (2*p_up + p_low)/(p_up + p_low)

    print("被动土压力系数：")
    print("Kp" + str(i+1) + " = tan2(45 + " + str(fai[i]) + "/2) = " + str(K))
    print("被动土压力强度为：")
    print('Pp%d上 = %.2f * %.2f + 2 * %.2f * √%.2f = %0.2f kPa' %(i+1,q-gama[i]*h[i],K, c[i], K, p_up))
    print('Pp%d下 = %.2f * %.2f + 2 * %.2f * √%.2f = %0.2f kPa' %(i+1,q,K, c[i], K, p_low))
    print("被动土压力合力为：")
    print('Ep%d = 1/2 * (%.2f + %.2f) * %.2f = %.2f kPa'%(i+1, p_up, p_low, h[i], E))
    print('Ep%d作用点至第%d层土地面的距离:'%(i+1, i+1))
    print('yp%d = %.2f m'%(i+1, y))
    print()

