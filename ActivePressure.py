'''
fai = [10, 8.10, 13.2, 11.6, 20.6, 11.6, 20.6, 23, 9.8, 22.3, 28]
c = [8, 24.2, 39, 35.9, 15, 35.9, 15, 5, 32.2, 14.8, 5]
gama = [ 18.5, 19.2, 19.4, 19.3, 19.7, 19.3, 19.7, 21.5, 19.1, 19.8, 21.5]
h = [ 1.7, 4.2, 1.2, 1.7, 2.3, 1.6, 2.3, 1.4, 3.9, 2.3, 50]
flag = [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
'''
import math

class ActivePressure:
    def __init__(self, new_fai, new_c, new_gama, new_h, new_flag, new_n):

        self.fai = new_fai
        self.c = new_c
        self.gama = new_gama
        self.h = new_h
        self.flag = new_flag
        self.n = new_n

        print("#####数据载入成功#####\n\n")

    def calculation(self, new_q):                                        ###计算及打印输出
        q = new_q
        for i in range(0,self.n):
            K = round(pow(math.tan(math.radians(45 - self.fai[i]/2)), 2), 2)
            if(self.flag[i]):
                u= 10*self.h[i]
                p_up = q*K - 2*self.c[i]*pow(K,0.5)
                q = q + self.gama[i]*self.h[i]
                p_low = (q-u)*K - 2*self.c[i]*pow(K,0.5) + u

                print("（" + str(i+1) +"）第" + str(i+1) + "层主动土压力（水土分算）")
                print("地下水压力：")
                print("u = " + str(u) + "kPa")
            else:
                print("（" + str(i+1) +"）第" + str(i+1) + "层主动土压力（水土合算）")
                p_up = q*K - 2*self.c[i]*pow(K,0.5)                                                     ###上层界面主动土压力
                q = q + self.gama[i]*self.h[i]                                                              ###累加土层重
                p_low = q*K - 2*self.c[i]*pow(K,0.5)                                                   ###下层界面主动土压力

            E = 0.5 * ( p_up + p_low ) * self.h[i]                                                 ###土压力合力
            y = self.h[i]/3 * (2*p_up + p_low)/(p_up + p_low)                                      ###合力作用点距土层底面距离

            print("主动土压力系数：")
            print("Ka" + str(i+1) + " = tan2(45 - " + str(self.fai[i]) + "/2) = " + str(K))
            print("主动土压力强度为：")
            print('Pa%d上 = %.2f * %.2f - 2 * %.2f * √%.2f = %0.2f kPa' %(i+1,q-self.gama[i]*self.h[i],K, self.c[i], K, p_up))
            print('Pa%d下 = %.2f * %.2f - 2 * %.2f * √%.2f = %0.2f kPa' %(i+1, q, K, self.c[i], K, p_low))
            print("主动土压力合力为：")
            print('Ea%d = 1/2 * (%.2f + %.2f) * %.2f = %.2f kPa'%(i+1, p_up, p_low, self.h[i], E))
            print('Ea%d作用点至第%d层土地面的距离:'%(i+1, i+1))
            print('ya%d = %.2f m'%(i+1, y))
            print()
'''
ap = ActivePressure(fai, c, gama, h, flag, 11)
ap.calculation(64.45)
'''