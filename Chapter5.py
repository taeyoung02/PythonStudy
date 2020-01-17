#1
class cal:
    def __init__(self):
        self.value=0

    def add(self, val):
        self.value +=val

class UpgradeCal(cal):
    def __init__(self):
        super().__init__()
        self.value=0
    def minus(self, val):
        self.value -= val
    
c = UpgradeCal()
c.add(10)
c.minus(7)

print(c.value)

#4
#filter(func,iterable) #참인요소만 가져옴
print(list(filter(lambda x:x>0,[1,-2,3,-5,8,-3]))) 

#5
int('0xea',16)


#6
print(list(map(lambda x:x*3,[1,2,3,4])))

#7
li=[-8, 2, 7, 5, -3, 5, 0, 1]
print(max(li)+min(li))

#8
print(round(17/3,4))

#9
import sys #명령창에서 인수 전달
sum=0
for i in sys.argv: #argv = [myargv.py, 1, 2, 3, 4, 5...]
    if i.isnumeric():
        sum+=int(i)
print(sum)

#10
import os
os.chdir("C://doit")

result=os.popen("dir")

print(result.read())

#11
import glob
print(glob.glob(
    "C://doit//*.py"))