"""
Notes from Session 1. None of this is my own, following lessons from https://mcmedhacks.com/program-2023/
"""

"""
Lists and Tuples
----------------
Helpful for when we want to collect a large collection of objects. 

We use lists and tuples for an ordered sequence of values. Lists are dynamic in 
size and mutable (they can be altered), and tuples are fixed size and immutable 
(cannot be altered).
"""

# we can make lists with the [] syntax: 
empty_list = []

list1 = [1, 2, 3, 5]

# we can make lists with mixed data types 

list2 = ['abc', 34, True, 323, "male"]

# we can even make a list of list 

list3 = [1, 'abc', [1, 2, 3]]

# we use list_name[idx] to access entries in the list. 

animals = ['cat', 'bat', 'rat', 'elephant']
print(animals)

# let's use type() to see the type of animals. 

print(type(animals))

# animals[i] will return the (i-1)th element of the list; for 
# python lists, indexing begins at 0. 

print(animals[1])

# SPLICING: 
# animals[1:4] will return the second element to the last element:
print(animals[1:4])

# in general, list[a:b] will return [ list[a], list[b] [. We can 
# also omit the a or b:

print(animals[:1])

# we can access the last element of a list using the -1 index. 

print(animals[-1])

# if we want to know how many elements are in a list, we can use the len() method:

print(len(animals))

# since python lists are mutable, we can add elements. list.append() will append 
# elements to a python list. 

new_animal = 'rabbit'
animals.append(new_animal)
print(animals)

# if we want to add a sequence of new elements, we can use list.extend(). 

new_animals = ['sparrow', 'parrot']
animals.extend(new_animals)
print(animals)

# we can do boolean operations on a list: we can check if something is in a list: 

print('cow' in animals)			 # should be false
print('cow' not in animals)		 # should be true 
print('bat' in animals)          # should be true 
print('bat' not in animals)      # should be false

# we can store them in variables: 

boolean_1 = 'cow' in animals 
print(boolean_1)

# we can change the elements of a list using the index, since lists 
# are mutable 

animals[2] = 'elk'
print(animals)

# we can also insert elements in the middle of a list using the list.insert() syntax. 

animals.insert(2, 'lion')
print(animals)

# we can get the first index a certain element shows up ising the list.index(element). 
# let's add another cat so we can demonstrate how this works.

animals.append('cat')

print(animals.index('cat'))

# what about the next one? We can check the index of cat in the interval 
# [a, b] using the following function: animals.index('cat', a, b)

print(animals.index('cat', 1, len(animals)))

# list.remove(element) will remove the first occurence of an element. 

animals.remove('cat')
print(animals)

# list.pop(idx) will remove the idx-th element of the list 

animals.pop(1)  		# will remove 'lion'
print(animals)

# another way to remove elements is the del list[idx]. 

del animals[2]
print(animals)

# list.sort() will sort a list 
animals.sort()
print(animals)

# list.clear() will erase the whole list. 
animals.clear()
print(animals)

# == will check for equality of lists. 
l1 = ['A', 'B', 'C']
l2 = ['A', 'B', 'C']
print(l1 == l2)
l2.append('D')
print(l1 == l2)

# Expanding: we can assign the values of a list to variables as follows:
l = [185, 185.3, 'John']
height, weight, name = l 
print(f'height: {height}, weight: {weight}, name: {name}')


"""
Tuples. We cannot change these. We'll use () to create them.
"""
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (1, 5, 7, 9)
tuple3 = (True, False, False)

fruits = ("apple", "banana", "cherry", "apple", "cherry")

# tuple.count(el) tells us how many of el are in the tuple. 
print(fruits)
print(fruits.count('apple'))

# tuple.index(el) tells us the index of the first occurence of el. 

print(fruits.index('apple'))
print(fruits.index('banana'))

# we can also expand tuples. We can use the tuple(list) operation to 
# turn a list into a tuple. 

t = (185, 185.3, 25)
l = list(t)
l.append(22)
t = tuple(l)
print(t)

# B.T.W.: you cannot make a tuple of length 1, it will be considered a string.

"""
Sets
----
Sets are immutable collections of data with no repetition and no order (literally like real ones in math).
We'll use the { } notation to make them.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {True, False, False}
set3 = {'abc', 34, True, 40, "male"}

this_set = {"apple", "banana", "cherry", "apple"}
print(this_set)

# We can add items to a set using the set.add() function.

this_set.add('orange')
print(this_set)

# We can use the set.update(another_set) to join a set to set.

tropical = {'pineapple', 'mango', 'papaya'}
this_set.update(tropical)
print(this_set) 

"""
Removing elements from sets. We have two options: 
- set.remove(element) will raise an error if the element is not in the set. 
- set.discard(element) will not raise an error if the element is not in the set. 
"""

this_set.remove("banana")
print(this_set)
this_set.discard("date")

# set.pop() will remove anything in the set, cause sets are not ordered. 
this_set = {"apple", "banana", "cherry"}
x = this_set.pop()
print(x)

# we can do the usual set operations on sets. 

set1 = {1, 2}
set2 = {1, 3}
set3 = {1, 2, 3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.issubset(set3))
print(set1.difference(set2))

# set() will return the empty set. 

s = set()
print(s)

"""
Dictionaries
------------

Dictionaries store data in key-value pairs. Quick facts:
	* They're mutable. 
	* Two items cannot have the same key. 
	* As of Python 3.7, dictionaries are ordered.
The syntax is as follows:

dictionary_name = {
	key1 : value1, 
	key2 : value2, 
	...
	keyN : valueN
}
So, instead of indices to access elements, we have keys. This is 
much more readable, and helpful for data analysis.
"""

this_dict = {
	"brand": "Ford", 
	"model": "Mustang", 
	"year": 1964 
}
print(this_dict)

# we use this_dict[key] to access the value associated to the key.
print(this_dict['brand'])
print(type(this_dict))

# we can set the value associated to a key
this_dict["year"] = 2020
print(this_dict)

# we can add a new key with a new value. 
this_dict['colour'] = 'red'
print(this_dict)

# we can find the length. 
print(len(this_dict))

# we can find all the values using dict.values()
print(this_dict.values())

# we can also find all the items, returned as a list of (keyN, valueN). 

print(this_dict.items())

# we can retrieve the value of a key using .get

x = this_dict.get("model")
print(x)

# and we can get all the key values. 
l = this_dict.keys()
print(l)
print(type(l))

# we can check if a key exists 

if 'model' in this_dict:
	print("Yes, 'model' is one of the keys in the this_dict dictionary.")

# given a key, we can delete the whole (key, value) pair using del. 

del this_dict['model']
print(this_dict)

"""
Activities
----------

1) Print numbers from 1 to 10 --> LOOP
"""

for i in range(1, 11):
	print(i)

# Range is a Python function to start a number and count up to 
# a certain number, increasing by a certain interval. 

# the syntax is: range(start, stop, step). If we omit a start and step, 
# Python will assume it starts at 0.

# 2) sum the numbers in a list
l = [2, 23, -5, 7, 8, -456, 34, 89, -97, 43, 12, -8, 43, -345, 23, 1, 43, 5, 7]

cum_sum = 0 

for num in l:
	cum_sum += num

# check work using the sum() function.
print(cum_sum, sum(l))

# what does this do? According to Google, it will raise an AssertionError if it's not true.
assert cum_sum == sum(l)

# let's test it. 

# cum_sum = 4

# we can display a custom string 
assert cum_sum == sum(l), "Sum not implemented correctly"


# 3) calculate the summation of all non-negative numbers in a list. 

pos_cum_sum = 0

for num in l: 
	# only add if it's positive
	if num >= 0:
		pos_cum_sum += num

print(pos_cum_sum)


"""
Functions
---------

A function to calculate the frequency of elements in a sequence
"""

def frequency(l):
	"""
	Returns a dictionary with the frequency of each element in the sequence. 

	Parameters
	----------
			l : list
				sequence 
	Returns
	-------
			freq : dictionary
				   frequency of each element in the sequence. 
	"""
	# initialize the dictionary of frequencies. 
	freqs = {}
	for el in l:
		# first check of el is already a key in freqs
		if el not in freqs:
			# add it as a key, and increment the value by one. 
			freqs[el] = 1 
		else:
			# otherwise, increment the pre-existing value by one. 
			freqs[el] += 1 
	return freqs 

# their code:
def their_frequency(l):
	"""
	Returns a dictionary with the frequency of each element in the sequence. 

	Parameters
	----------
			l : list
				sequence 
	Returns
	-------
			freq : dictionary
				   frequency of each element in the sequence. 
	"""
	keys = set(l)
	freq = {}     # empty dictionary
	for x in l:

		# list.get(keyname, value) is nicer syntax, since it is a 
		# value to return if the specified key does not exist. 
		# the default value is none.

		freq[x] = freq.get(x, 0) + 1 
	return freq

# checking
l = [1, 2, 3, 2, 1, 1, 3, 4, 1, 4, 3, 1, 2, 3, 4]
assert their_frequency(l) == frequency(l), "Error in coding my version"

"""
Modular Programming
-------------------
Python allows us to put definitions in a file and use them in a script. 
We call the file that contains all the definitions a *module*. 
We can import definitions from a module into another module, or into the main module.
"""

"""
For example, suppose we have two files: myModule.py and main.py. 

FILE: myModule.py

def func1(x):
	return x + 2 

def func2(y):
	return y * 78


FILE: main.py

import myModule

value = myModule.func1(5)
print(value)   #  will print 7
******************************************************
Common modules to know about: 
- math 
- scikit-learn 
- numpy
- pytorch 
- scipy 
- pandas
- matplotlib
- random 
- opencv-python
- itertools
- logging
- json


SUGGESTION: Automate the Boring Stuff with Python
"""

