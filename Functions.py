#user defined fuctions
def greet():
    print("hello world")
#calling function
greet()

#Function with parameter
def names(name):
    print('hello ' +'muuo '+ name)
names('Mark')   



#positional Argument
def add(a,b):
    result = a+b
    return result 
result=add(5,6)
print(result)

#keyword argument
def add(c,d):
    result1= c+d
    return result1
result1 =add(c=7,d=11)
print(result1)


#Lambda Function(Anonymous) -function that can be defined without a nanme
add = lambda a,b: a+b
result3 = add(7,3)
print(result3)