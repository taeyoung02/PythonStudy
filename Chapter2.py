#2-3
address="881120-1068234"
address=address.split('-') #address가 str에서 list로 형변환됨
print(address)

#2-4
print(address[1][0])

#2-5
a="a:b:c:d"
a=a.replace(':','#')
print(a)

#2-7
print(' '.join(['Life','is','too','short']))

#2-7
t=(1,2,3)
t+=(4,) #값 하나 추가시 ,붙여줌
print(t)

#2-9
#3. value와 달리 key안의 값은 변경할수 없는 값이 들어가야하기 떄문이다

#2-11
a=[1,1,1,2,2,3,3,3,4,4,5]
print(list(set(a)))

#2-12
#a와 b의 주소값이 같기때문에 변경된 리스트를 여전히 b가 가르킴
#b=a[:]를 이용하면 별개의 리스트를 갖게 할 수 있다.