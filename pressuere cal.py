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
        p_up = q*K + 2*c[i]*pow(K,0.5)                                                     ###上层界面主动土压力
        q = q + gama[i]*h[i]                                                              ###累加土层重
        p_low = q*K + 2*c[i]*pow(K,0.5)                                                   ###下层界面主动土压力

    E = 0.5 * ( p_up + p_low ) * h[i]                                                 ###土压力合力
    y = h[i]/3 * (2*p_up + p_low)/(p_up + p_low)                                      ###合力作用点距土层底面距离

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


'''
class ActiveForce(object):
    q = 64.45
    def __init__(self,fai,c,gama,h,flag):
        ###private###
        self._fai = fai
        self._c = c
        self._gama = gama
        self._h = h
        self._flag = flag

    def cal(self):
        for i in range(0,11):
            K = round(pow(math.tan(math.radians(45 - fai[i]/2)), 2), 2)
            if(flag[i]):
                u= 10*h[i]
                p_up = self.q*K - 2*c[i]*pow(K,0.5)
                q = self.q + gama[i]*h[i]
                p_low = (self.q-u)*K - 2*c[i]*pow(K,0.5) + u
                E = 0.5 * ( p_up + p_low ) * h[i]                                              ###土压力合力
                y = h[i]/3 * (2*p_up + p_low)/(p_up + p_low)
                self.pprint1()

            else:
                print("（" + str(i+1) +"）第" + str(i+1) + "层主动土压力（水土合算）")
                p_up = self.q*K - 2*c[i]*pow(K,0.5)                                              ###上层界面主动土压力
                self.q = self.q + gama[i]*h[i]                                                        ###累加土层重
                p_low = self.q*K - 2*c[i]*pow(K,0.5)                                            ###下层界面主动土压力
                E = 0.5 * ( p_up + p_low ) * h[i]                                              ###土压力合力
                y = h[i]/3 * (2*p_up + p_low)/(p_up + p_low)                                  ###合力作用点距土层底面距离

    def pprint1(cal):
        print("（" + str(super.i+1) +"）第" + str(super.i+1) + "层主动土压力（水土分算）")
        print("地下水压力：")
        print("u = " + str(u) + "kPa")
        print("主动土压力系数：")
        print("Ka" + str(super.i+1) + " = tan2(45 - " + str(fai[super.i]) + "/2) = " + str(K))
        print("主动土压力强度为：")
        print('Pa%d上 = %.2f * %.2f - 2 * %.2f * √%.2f = %0.2f' %(super.i+1,q,K, c[super.i], K, p_up))
        print('Pa%d下 = %.2f * %.2f - 2 * %.2f * √%.2f = %0.2f' %(super.i+1,q,K, c[super.i], K, p_low))
        print("主动土压力合力为：")
        print('Ea%d = 1/2 + (%.2f + %.2f) * %.2f = %.2f'%(super.i+1, p_up, p_low, h[super.i], E))
        print('Ea%d作用点至第%d层土地面的距离:'%(super.i+1, super.i+1))
        print('ya%d = %.2f'%(super.i+1, y))
        print()

    def pprint0(cal):
        print("主动土压力系数：")
        print("Ka" + str(super.i+1) + " = tan2(45 - " + str(fai[super.i]) + "/2) = " + str(K))
        print("主动土压力强度为：")
        print('Pa%d上 = %.2f * %.2f - 2 * %.2f * √%.2f = %0.2f' %(super.i+1,q,K, c[super.i], K, p_up))
        print('Pa%d下 = %.2f * %.2f - 2 * %.2f * √%.2f = %0.2f' %(super.i+1,q,K, c[super.i], K, p_low))
        print("主动土压力合力为：")
        print('Ea%d = 1/2 + (%.2f + %.2f) * %.2f = %.2f'%(super.i+1, p_up, p_low, h[super.i], E))
        print('Ea%d作用点至第%d层土地面的距离:'%(super.i+1, super.i+1))
        print('ya%d = %.2f'%(super.i+1, y))
        print()

act = ActiveForce(fai,c,gama,h,flag)
act.cal()
'''