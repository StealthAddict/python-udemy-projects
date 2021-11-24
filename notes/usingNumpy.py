# LECTURE 121

import numpy #base library for other libraries

# create array
n = numpy.arange(27) #one dimensional 
n = n.reshape(3,9) #two dimensional
n = n.reshape(3,3,3) #three dimensional

m = numpy.asarray([[123,12,123,12,33],[],[]])


# LECTURE 123

import cv2

# read image file
# (imread) pass file, then pass 0 for black & white, pass 1 for RBG
img_grey = cv2.imread("/Users/Of The Crow/Desktop/original.png", 0)

#print(img_grey)

#create new image file
cv2.imwrite("/Users/Of The Crow/Desktop/newsmallgrey.png", n)


# LECTURE 124

# indexing
"""
print(img_grey[0:2, 2:4])

print(img_grey.shape)

print (img_grey[2,4])
"""

# iterating
"""
for i in img_grey:
    print(i)

for i in img_grey.flat:
    print(i)
"""

# LECTURE 125

# concatinating arrays
ims = numpy.hstack((img_grey,img_grey)) #hstack = horizontal stack

ims = numpy.vstack((img_grey,img_grey)) #vstack = vertical stack

lst = numpy.vsplit(ims, 3) #split into lists
