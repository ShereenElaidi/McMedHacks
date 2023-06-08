"""
Notes from Session 2. None of this is my own, following lessons from https://mcmedhacks.com/program-2023/
Instructor: Hunter Buckhorn
"""

"""
Object Oriented Programming in Python.  
- A way to organize the state of the project -- organizing the code in a specifc way. 
- Along with the state, there are specific functions that you can use to create modifications of the state as the program progresses. 
- Concepts of OOP: 
	- Classes and objects. 
	- Intro to OOP and Class Design for Computer Vision Data
	- Encapsulation 
	- Inheritance
	- Polymorphism 
	- Data Abstraction
	- Data Science -- relating OOP concepts to the Data Science workflow.

- Every object that can be named in the object has equal class. 
- One of the tenents of OOP is data abstraction. 
	- Handling complexity by hiding unnecessary information from the user. 
- Classes/Objects
	- A class is a collection of data and functions -> "attributes" and "methods"

- Functional python
	- core functional programming is common in data processing: map and reduce. Others: 
		- lambda:
			- holy grail: map (apply a function to each element of the data set), filter, reduce (apply function on entire data set)
			- custom functions and pandas
		- itertools
			- module with every kind of iteration imaginable
		- defaultdict
			- defining function IO and APIs
			- enforce what the key values should be (data type)
		- set logic
			- working with data points and the file system.
"""

# DEMO: implementing a data point class
import os 
import numpy 
import shapely 
from shapely import geometry 
import json
import cv2
import matplotlib.pyplot as plt

# first obtain the directory of the data sets
DATA_TITLE = "data"
labelme_dir = os.path.join(os.getcwd(), DATA_TITLE)

# open an image 
img_fname = '2011_000006.jpg'
json_fname = '2011_000006.json'

# open the file ; this syntax will also close the file
with open(os.path.join(labelme_dir, json_fname), 'r') as f:
	test_json = json.load(f)

# read the image 
img = cv2.imread(os.path.join(labelme_dir, img_fname))
print(img.shape)

# window that the image is displayed
window_name = 'image'

# next we will look at the labelme format. 

print(type(test_json))

# test_json is a python dictionary. Let's look at the labelme format

print(test_json.keys())

# we can view some of the keys here:

print(test_json['imageHeight'])
print(test_json['imageWidth'])

# let's now try to see how the labelme format represents polygons

print("Sample test_json['shapes'][0]:")
print(test_json['shapes'][0])


# PLOTTING LINE SEGMENTS - we will do this with matplotlib. 

# storing the label (label) and points (points) as variables, 
# will be a polygon around the person.
label = test_json['shapes'][0]['label']
points = test_json['shapes'][0]['points']

# importing necessary packages
import matplotlib.pyplot as plt 
import matplotlib.patches as patches 
from PIL import Image 

# obtaining the image
im = Image.open(os.path.join(labelme_dir, img_fname))

# creating a figure and axes. 
fig, ax = plt.subplots(figsize=(15, 15))

# display the image
ax.imshow(im)

# create the polygon using the vertices in the points array
poly = patches.Polygon(xy = points, linewidth = 2, edgecolor='r', facecolor = 'none')

# add the polygon to the axes
ax.add_patch(poly)

# add a title
ax.set_title(f'Polygon Label: `{label}`')

# plt.show()
plt.close(fig)

# let's collect all of the labels. they are contained in the 
# test_json['shapes'] array

print(test_json['shapes'])
# python data structure -- it is a list of dictionaries
print(type(test_json['shapes']))
# dimension
print(len(test_json['shapes']))

# let's mke a list of all the possible unique labels

unique_labels = set() 		# python set 

for shape in test_json['shapes']:
	label = shape['label']
	print(label)
	unique_labels.add(label)

# view the unique labels set
print(unique_labels)

# now let's plot them all. Again, create figure and axes 
fig, ax = plt.subplots(figsize=(15, 15))
ax.imshow(im)

# dictionary containing all the colours for each unique label
colormap = {
	'__ignore__': 'none',
	'chair': 'g', 
	'person': 'b', 
	'sofa': 'r', 
}

# for each polygon, make a shape

for shape in test_json['shapes']: 
	# create a polygon 
	poly = patches.Polygon(
		xy = shape['points'],
		linewidth = 2, 
		edgecolor = colormap[shape['label']], 
		facecolor = 'none')
	# add the polygon object to the axes 
	ax.add_patch(poly)
plt.show()

# will deal with OOP later today