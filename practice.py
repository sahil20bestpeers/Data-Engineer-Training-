# Variables, Data Types (int, float, string, bool)
x = 5
y = "John"
print(x)  
print(y)

x = "John"
# is the same as
x = 'John'

print(x==x)


a = 4
A = "Sally"
print(a)
print(A)


name = "Jane Doe"
age = 19
subjects = ["Math", "English", "Physics", "Chemistry"]

print(type(name))
print(type(age))
print(type(subjects))


# Rules for the variable declaration 
# 1) start with a letter or underscore 
# 2) allowed characters 
# 3) case sensetive 
# 4) No reversed keyword 
# 5) No spaces 



# python data types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


lst = [20,30,40,80]
x = 30.2
y = int(x)
print(y)
z = frozenset({"apple","banana","cheery"})
print(type(z))

my_frozenset = frozenset([1, 2, 3, 2, 4])
print(my_frozenset)  

# mylist = ['apple', 'banana', 'cherry']
# x = frozenset(mylist)
# x[1] = "strawberry" does not support change 



num_str = "1234"
num_int_ = int(num_str)
print(type(num_int_))


num_float = float(num_str)
print(num_float)
print(type(num_float))  

# List functions and  methods 

# List Methods
# Let's look at different list methods in Python:

# append(): Adds an element to the end of the list.
# copy(): Returns a shallow copy of the list.
# clear(): Removes all elements from the list.
# count(): Returns the number of times a specified element appears in the list.
# extend(): Adds elements from another list to the end of the current list.
# index(): Returns the index of the first occurrence of a specified element.
# insert(): Inserts an element at a specified position.
# pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
# remove(): Removes the first occurrence of a specified element.
# reverse(): Reverses the order of the elements in the list.
# sort(): Sorts the list in ascending order (by default).

lst = [1,2,3,4,5,6]
lst.append(9)
print(lst)


print(lst.copy())
lst.copy()

lst2 = [2,3,"sahil", "Harsh"]
lst2.clear()
print(lst2)


lst3 = [5,9,7,7,8,8,8]
print(lst3.count(8))

lst3.extend(lst)
print(lst3)


print(lst3.index(8))


lst3.insert(5,76)
print(lst3)

lst3.pop(5)
print(lst3)


lst3.remove(5)
print(lst3)


lst3.reverse()
print(lst3)


lst3.sort()
print(lst3)


# Tuple 

l = (2,3,4,5)
print(type(l))


print(tuple(lst3))

tuple1 = tuple()
print(tuple1)

string1 = "geeksforgeeks"
tuple4 = tuple(string1)
print(tuple4)



my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])


my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
my_tuple = tuple(my_dict.items())
print(my_tuple)


my_tuple = tuple((1, 2, 3))
print(len(my_tuple))

my_tuple = tuple((1, 2, 3))
print(max(my_tuple))

my_tuple = tuple((3, 2, 1))
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)



x = 0, 1, 2, 3
y = ("WsCube", "Tech")

result = x + y
print(result)


tup = ("WsCube", "Tech", "Learning", "Platform")
for item in tup:
    print(item)
    

s1= {2,3,4,9,8,6}
s2 = {2,3,7,8,5,9}
print(s1)
print(s2)

s1.add(10)
print(s1)

s1.discard(10)
print(s1)

print(s1.union(s2))


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using the intersection() method
print(a.intersection(b))

# Using the & operator
print(a & b)




print(s1.difference(s2))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using the symmetric_difference() method
print(a.symmetric_difference(b))

# Using the ^ operator
print(a ^ b)


print(s1.issuperset(s2))

print(s1.intersection_update(s2))


print(s1.difference_update(s2))


# Dictionary 

dst = {"name" : "sahil" , "surname": "chourasiya", "address" : "Bhawani Nagar Nepanagar"}
print(dst.copy())

print(dst.fromkeys)

print(dst.get("name"))

print(dst.items())

print(dst.keys())

print(dst.values())

# print(dst.setdefault())

# print(dst.setdefault("c",3))



# Strings Manipulations

s = "SAhil Chourasiya"
print(s.lower())

print(s.upper())

print(s.strip())    

print(s.split())


words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence) 

print(s.find("s"))


text = "Hello, world!"
print(text.startswith("Hello"))
print(text.startswith("hello"))  



# Mini Project: Parse and clean a CSV-like string input

string_input = "Lorem Ipsum is simply dummy text of the printing , typesetting industry. Lorem Ipsum has been the industr."
for i in string_input:
        string_input = string_input.replace(".","").replace("," , "")
        print(string_input)
        break
    
# Parse a string like "name:John, age:30, role:engineer" into a dictionary.

string_dict = "name:John, age:30, role:engineer"
dictionary = {}

for pair in string_dict.split(","):
    key, value = pair.split(":")
    dictionary[key] = value

print(dictionary)


#Convert list of such strings into a list of dictionaries. 
l = ["('name':'sahil', 'age':'22', 'role':'engineer')",
 "('name':'pankaj', 'age':'30', 'role':'Data Engineer')",
 "('name':'Kushal', 'age':'26', 'role':'cloud enginner')"]
result = [dict(item.replace("'", '').split(':')
               for item in s[1:-1].split(', '))for s in l]
print(result)




# Create a function to extract domains from a list of emails.

string_input = input("enter a string")
if "@" not in string_input:
    print("enter a valid email address")
else:
    split_input = string_input.split("@")
print(split_input[-1])







    
