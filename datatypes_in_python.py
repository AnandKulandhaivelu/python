print("This is all about the data types in python")
# Number data type:

# integer type:
a=5
print(type(a))
# output : <class 'int'>

# floating type:
b=1.5
print(type(b))
# output : <class 'float'>

# complex type:
c=5+10j
print(type(c))
# output : <class 'complex'>

# String data type:

s1="welcome"
s2="admin"

print(s1)
print(type(s1))
# output : <class 'str'>

# string concatination:

print(s1+s2)
# output : welcomeadmin
# string slicing:
print(s1[0:3])
print(s1[-1:])
# output : wel,e
# string repetation:
print(s1*4)
# output : welcomewelcomewelcomewelcome
# Multiline string:
s3="""
    python is high level programming language
    python is general purpose programming language
"""
print(s3)

# output:     python is high level programming language
#             python is general purpose programming language


# List data type:

l1=[1,2,3,4,5]

print(l1)
print(type(l1))

print(l1[2:5])

l1[2]='Hi'
print(l1)

# Tuple data type:

t1=(10,20,30,40)

print(type(t1))

print(t1[0:2])

# set data type:

s1={1,3,5,7,9}
s2={5,7,2,6}
print(type(s1))

s3=s1|s2
print(s3)

s4=s1&s2
print(s4)

# Dictionary data type:

d1={1:'hi',2:'hello',3:'welcome',4:'python'}

print(type(d1))

print(d1[2])

d1[3]='java'
print(d1)

print("This is all about the data types in python")
