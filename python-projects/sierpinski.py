import math
import stddraw

# return the height of an equilateral triangle with sides of length ‘length’
def height(length):
  h = length*math.sqrt(3)/2
  return h

# draws a filled, inverted triangle at point x, y with sides of length ‘length’
def filledTriangle(x, y, length):
  xf = [x, x - length/2, x + length/2]
  yf = [y, y + height(length), y + height(length)]
  stddraw.filledPolygon(xf, yf)

# draws an empty equilateral triangle of length = 1, with a bottom-left vertex of (0, 1)
# draws the order N Sierpinski triangle inside the outline from the step above (recurse n times)
def sierpinski(n, x, y, length):
  if n == 1:
    stddraw.polygon([0, 1, 1/2], [0, 0, math.sqrt(3)/2])
    return filledTriangle(x, y, length)
  else:
    filledTriangle(x, y, length)
    return sierpinski(n-1, x - (length/2), y, length/2), sierpinski(n-1, x + (length/2), y, length/2), sierpinski(n-1, x, y + height(length), length/2)


if __name__ == "__main__":
  # you will provide values for n, x, y, and length
  sierpinski(5, 0.5, 0, 0.5)
  stddraw._showAndWaitForever()
 
