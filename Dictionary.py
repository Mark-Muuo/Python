#iTs a collection of itmescomprising key_value separated bby commas
subject = {1:'chemestry',2:'Biology',3:'Geography',4:'Mathematics',5:'History'}

#accesing dictionary(we use keys(1,2,3,4))

chem = subject[1]
print(chem)
#ALt
chem2 =subject.get(1)
print(chem2)


#updating dict
subject[1]= 'Agriculture'
print(subject)

#Adding items
subject[6]='Chemestry'
print(subject)

#deleting items
del subject[6]
print(subject)
   #alt
subjects = subject.pop(5)
print(subjects)
   #alt
subjec= subject.popitem()
print(subjec)
print(subject)

#looping dictionary
for items in subject.items():
        print(items)
