#arithmetic operations
num1=5
num2=3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)
#complex numbers
num1=2+3j
num2=4+5j
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
#strings
str='hello'
print(len(str))
print(str)
str='hello everyone'
print(str)
#indexing and slicing
str='hello everyone'
print(str[2])
print(str[2:])
print(str[:9])
print(str[-2])
print(str[-3:])
print(str[2:5])
#boolean
num= 2 < 3
print(num)
a= 30/2 == 16
print(a)
#sequence
#list
list=[1,2,3,4,['hello','True','False'],5,6]
print(len(list))
list[4][1]='good morning' #mutable
print(list)
list[5]='five'
print(list)
#tuple
tuple=(1,2,3,4,['hii','welcome'],'five','six')
print(tuple)

#range
print(list(range(0, 100)))
print(list(range(0, 100,2)))
print(list(range(0, 100,1)))
