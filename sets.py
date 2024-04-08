#creating sets
nums ={1,2,3,4,5,6}
  #alt
L = [1,2,2,2,3,3,4,5,6]
num=set(L)
print(num)

#adding item 
nums.add(7)
nums.add(8)
print(nums)
 
 #removing items
nums.remove(8)
nums.remove(7)
print(nums)

#operation in sets
#Union
S1 ={1,2,3,4,5}
S2 ={3,4,5,6,7,8}

result =S1.union(S2)
print(result)

#intersection
result2 =S1.intersection(S2)
print(result2)

#Difference
result3 =S1.difference(S2)
print(result3)

result4 =S2.difference(S1)
print(result4)

#symetric difference
result5 =S1.symmetric_difference(S2)
print(result5)

#cartesian product

P=[]
for x in S1: 
   for y in S2:
    P.append((x,y))
    print(P)
    