#4-2
def everage(a):
    sum=0
    for i in a:
        sum+=i
    return sum/len(a)

print(everage([10,20,3,2,1]))

#4-5
f1 = open("test.txt","w")
f1.write("Life is too short")
f1.close()

f2=open("test.txt","r")
print(f2.read())

#4-6
def program():
    f = open("test.txt","a")
    f.write(input()+'\n')
    f.close()

program()
program()

#4-7
with open("Test.txt","w") as f:
    f.write("Life is too short\nyou need java")
with open("Test.txt","r") as f:
    data=f.read()
data=data.replace("java","python")
with open("Test.txt","w") as f:
    f.write(data)
with open("Test.txt","r") as f:
    print(f.readlines())
    