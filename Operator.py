"""
fai = 10 8.10 13.2 11.6 20.6 11.6 20.6 23 9.8 22.3 28
c = 8 24.2 39 35.9 15 35.9 15 5 32.2 14.8 5
gama =  18.5 19.2 19.4 19.3 19.7 19.3 19.7 21.5 19.1 19.8 21.5
h = 1.7 4.2 1.2 1.7 2.3 1.6 2.3 1.4 3.9 2.3 50
flag =  0 0 0 0 0 0 0 1 0 0 1
n = 11
q = 64.45
"""

from InputStatics import InputStatics

while 1:
    print("选择功能：")
    choose = int(input('输入1进行主动土压力计算，输入2进行被动土压力计算，输入其他数字结束程序：\n'))

    if choose == 1 or choose == 2:
        operator = InputStatics()
        operator.getAns(choose)
    else:
        print("程序结束")
        break
