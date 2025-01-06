"""
Area Sum
Complete the area_sum() function. It accepts a list of rectangles,
 where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

The function will calculate the area of each rectangle, 
then sum them all up and return the result.
"""

def area_sum(*rectangles):
    sum = 0
    for x in rectangles:
        sum += 2 * (x.get("height") + x.get("width"))
    return sum
rectangle1 = {
  "height": 5,
  "width": 2,
}

rectangle2 = {
  "height": 5,
  "width": 2,
}

rectangle3 = {
  "height": 5,
  "width": 2,
}

print(area_sum(rectangle1,rectangle2,rectangle3))