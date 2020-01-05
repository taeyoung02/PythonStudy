#3-5
A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for i in A:
    sum+=i
print(sum/len(A))

#3-6
numbers = [1, 2, 3, 4, 5]
result = [i*2 for i in numbers if i%2]
print(result)