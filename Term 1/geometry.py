#benjamin vielstich 
#9/11/2019
#geometry homework

#Errors: Format in the first square, circle and triangle-logic error.
#Forgot the input() at the end-runtime error.
#Able to break the program by inputting a letter and special characters- runtime error.
#Didn't double the amount of backslashes-syntax error.
#Mispelled perimeter- logic error.
#Improper punctuation- logic error.
#Can't input units- runtime error.
#Able to have negative answers - logic error.
#Found by April Fuentes, Rachel Thomas, Bryan Morris, Daniel Embley

#perimeter and area of square
print("preimeter and area of a square")

#gets the length of the square
sqr_side = input("what is the length of the square?")

#calculates the perimeter
perimeter = int(sqr_side)*4

#calculates the area
sqr_area = int(sqr_side)*int(sqr_side)

#prints the perimeter and area
sqr = str.format("""                            {}
                       +--------+
                       |           |
                   {}   |           |  {}
                       |           |
                       +--------+
                             {}
    perimeter {} units
    area       {} square units""",sqr_side,sqr_side,sqr_side,sqr_side,perimeter,sqr_area)
print(sqr)

#circumference of a circle
print("circumference of a circle")

#gets the radius
rad = input("what is the radius")

#sets pi
pi = 3.14

#calculates the circumference
circ = pi*int(rad)**2

#prints the circumference
crcl = str.format("""
                        *  *
                     *      {} *
                    *      ----*
                     *          *
                         *  *
    circumference {} units""",rad,circ)
print(crcl)

#area of a triangle
print("area of a triangle")

#gets the base and height
base = input("what is the base")
height = input("what is the height")

#calculates the area
tri_area = 0.5*int(base)*int(height)

#prints the area
tri = str.format("""
              /\
            /  | \
          /  {}|  \
         /     |   \
         ---------
               {}
 area {} square units""",height,base,tri_area)
print(tri)

#volume of a cube
print("volume of a cube")

#gets the length of the side
side = input("what is the length of a side")

#calculates the volume
vol = int(side)**3

#prints the volume
cube = str.format("""
          +----+
         /      /|
        +----+  |  all sides are {} units long
        |      |  +
        |      | /
        +----+

  volume {} units cubed""",side,vol)
print(cube)
input()
