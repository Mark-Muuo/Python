#like lists but cannot be modified
a,b,c =1,2,3
print(a)
#unpacking tuples
num1,*num2=4,5,6
print(num1)
print(num2)

#dummy variables
_,w,e =7,8,9
print(w)

#operation on tuples
T = 1,2,3,4,5,6,7,1,2,1,1,8,23,1,12,32,67,89
print(len(T))#no. of items

print(T.count(1))
print(T.count(2))

min_value =min(T)
max_value =max(T)
print(min_value)
print(max_value)

print(tuple(T))

T1 =(1, 2, 3, 4, 5, 6, 7, 1, 2, 1, 1, 8, 23, 1, 12, 32, 67, 89)
print(T1.index(4))
print(T1.index(12))
print(T1.index(67))