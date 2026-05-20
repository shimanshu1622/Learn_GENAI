x=55
print(x,type(x)) # int

y=3.14
print(y,type(y)) # float

name = "Himanshu"
print(name,type(name)) # str

is_adult = True
print(is_adult,type(is_adult)) # bool

complex_num = 2 + 3j
print(complex_num,type(complex_num)) # complex

marks = [90, 85, 92]
print(marks,type(marks)) # list

roll_number = (1, 2, 3)
print(roll_number,type(roll_number)) # tuple

person = {"name": "Himanshu", "age": 99}
print(person,type(person)) # dict

unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers,type(unique_numbers)) # set

# type casting 

x="100"
y="200"

a=int(x)
b=int(y)
c=a+b
print(c,type(c))
