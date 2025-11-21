from sys import getsizeof
x= 101
y=12345678901234567890
print("Value of x:",x)
print("Type of x:",type(x))  # Output: <class 'int'>
print("Value of y:",y)
print("Type of y:",type(y))  # Output: <class 'int'>
print(sizeof_x:=x.__sizeof__())  # Output: Size in bytes of integer x
print(sizeof_y:=y.__sizeof__())  # Output: Size in bytes of integer y 
print("Size of x using getsizeof:",getsizeof(x))  # Output: Size in bytes of integer x
print("Size of y using getsizeof:",getsizeof(y))  # Output: Size in bytes of integer y

print(id(x))
print(id(y))

x=205
print(id(x))