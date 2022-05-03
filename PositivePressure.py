"""
fai = [11.6,20.6,23,9.8,22.3,28]
c = [35.9,15,5,32.2,14.8,21.5]
gama = [ 19.3, 19.7,21.5,19.1,19.8,21.5]
h = [ 1,5.9,1.7,9.8,1.7,50]
flag = [ 0, 0, 1, 0,0,1]
"""
import math

class PositivePressure:
    def __init__(self, new_fai, new_c, new_gama, new_h, new_flag, new_n):

        self.fai = new_fai
        self.c = new_c
        self.gama = new_gama
        self.h = new_h
        self.flag = new_flag
        self.n = new_n

        print("#####数据载入成功#####\n\n")

    def calculation(self, new_q):
        q = new_q
        for i in range(0,self.n):
            K = round(pow(math.tan(math.radians(45 + self.fai[i]/2)), 2), 2)
            if(self.flag[i]):
                u= 10*self.h[i]
                p_up = q*K + 2*self.c[i]*pow(K,0.5)
                q = q + self.gama[i]*self.h[i]
                p_low = (q-u)*K + 2*self.c[i]*pow(K,0.5) + u

                print("（" + str(i+1) +"）第" + str(i+1) + "层被动土压力（水土分算）")
                print("地下水压力：")
                print("u = " + str(u) + "kPa")
            else:
                print("（" + str(i+1) +"）第" + str(i+1) + "层被动土压力（水土合算）")
                p_up = q*K + 2*self.c[i]*pow(K,0.5)                                                     ###上层界面主动土压力
                q = q + self.gama[i]*self.h[i]                                                              ###累加土层重
                p_low = q*K + 2*self.c[i]*pow(K,0.5)                                                   ###下层界面主动土压力

            E = 0.5 * ( p_up + p_low ) * self.h[i]                                                 ###土压力合力
            y = self.h[i]/3 * (2*p_up + p_low)/(p_up + p_low)                                      ###合力作用点距土层底面距离
            print("被动土压力系数：")
            print("Kp" + str(i+1) + " = tan2(45 + " + str(self.fai[i]) + "/2) = " + str(K))
            print("被动土压力强度为：")
            print('Pp%d上 = %.2f * %.2f + 2 * %.2f * √%.2f = %0.2f kPa' %(i+1,q-self.gama[i]*self.h[i],K, self.c[i], K, p_up))
            print('Pp%d下 = %.2f * %.2f + 2 * %.2f * √%.2f = %0.2f kPa' %(i+1,q,K, self.c[i], K, p_low))
            print("被动土压力合力为：")
            print('Ep%d = 1/2 * (%.2f + %.2f) * %.2f = %.2f kPa'%(i+1, p_up, p_low, self.h[i], E))
            print('Ep%d作用点至第%d层土地面的距离:'%(i+1, i+1))
            print('yp%d = %.2f m'%(i+1, y))
            print()

'''
pp = PositivePressure(fai, c, gama, h, flag, 6)
pp.calculation(0)
'''