from ActivePressure import ActivePressure
from PositivePressure import PositivePressure

class InputStatics(ActivePressure, PositivePressure):
    def __init__(self):
        arr = input('请输入内摩擦角（注意将输入法调为英文，数字间以空格分隔，回车表示结束）\n')
        self.fai = [float(i) for i in arr.split( )]
        print("内摩擦角输入成功\n")
        ###self.fai = fai

        arr = input('请输入粘聚力\n')
        self.c = [float(i) for i in arr.split( )]
        print("粘聚力输入成功\n")

        arr = input('请输入重度\n')
        self.gama = [float(i) for i in arr.split( )]
        print("重度输入成功\n")

        arr = input('请输入层厚\n')
        self.h = [float(i) for i in arr.split( )]
        print("层厚输入成功\n")

        arr = input('请确定水土分算还是合算（1表示分算，0表示合算）\n')
        self.flag = [int(i) for i in arr.split( )]
        print("土层情况定义成功\n")

        self.q = float(input('请输入附加荷载大小\n'))
        print("附加荷载输入成功\n")

        self.n = int(input('请输入土层数\n'))
        print("土层数目输入成功\n")

    def getAns(self, n):
        if n == 1:
            ActivePressure.__init__(self,self.fai, self.c, self.gama, self.h, self.flag, self.n)
            ActivePressure.calculation(self, self.q)
        elif n == 2:
            PositivePressure.__init__(self,self.fai, self.c, self.gama, self.h, self.flag, self.n)
            PositivePressure.calculation(self, self.q)
        else:
            print("出错")