list =[20,2.34,9,250,29,46,21,999]
print(list[2])
print(list[0])
print(list[1])
print(list[3])

# slicing(extract specific or range of items)
result = list[1:3]
print(result)

#adding items in list insert(any position) append(end)
list.append('false')
print(list)

list.insert(2,'orange')
print(list)

#removing item  pop(removes and returns),remove(name of the item)
list.pop(2)
print(list)

list.remove('false')
print(list)

#sorting items  sort()  sorted(returns item sorted)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#combining list  concatenation
l1 =[6,3,9]
l2 =[21,11,76]
print(l1 + l2)

#list comprehension ---creating new list from existing one
l3 =[num *5 for num in l1 ]
print(l3)

#nested  lists
l4 =[num *5 for num in l2 if num%2==0 ]
print(l4)

#zip() combines items of different list with the same index

l5 =zip(l1,l3)
print(l5)



