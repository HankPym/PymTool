# Calculate the area of a circle based on its radius.
# This calculation will be done by slicing the circle into tiny rings, adding the lengths
# of each ring together to get a combined length, and then calculating the area as a triangle
# using 1/2 base * height (with base being the radius and height being the combined slice length).

import math

radius = 17
precision = 100000 # Defines how many 'rings' the circle will be sliced into
slicesum = 0 
 
for slice in range(0,radius*precision,1):
	slicesum =+ 2 * math.pi * (slice)  # circumference = 2*Pi*r

print("The sum of each slice length is " + str(slicesum/precision) + ".")

area = ((radius*slicesum)/2)/precision # Area = (ab)/2, or (radius*slicesum)/2
print("The resulting area would then be " + str(area) + ".")
