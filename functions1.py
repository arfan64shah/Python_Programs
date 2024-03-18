''' write Write a function called calculate_area that takes base and height as an input
 and returns and area of a triangle. Equation of an area of a triangle is '''

# def calculate_area(width, height):
#     area = 1/2*(width*height)
#     return area

# tri_1 = calculate_area(5, 10)

# print("The area of triangle is ", tri_1)

# '''
# Modify above function to take third parameter shape type. It can be either "triangle" or 
# "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is
# '''
# triangle = 'triangle'
# rectangle = 'rectangle'
# def calc_area(width, height, shape):
#     if (shape == 'triangle'):
#         area = 1/2*(width*height)
#     elif (shape == 'rectangle'):
#         area = width * height
#     else:
#         print("Please select a valid shape.")
#     return area
# tri = calc_area(5, 10, triangle)
# rect = calc_area(5, 10, rectangle)

# print(rect)

'''
Write a function called print_pattern that takes integer number as an argument and prints 
following pattern if input number is 3
'''
def pattern(no):
    pattern_str = ''
    for i in range(1, no+1):
        pattern_str = pattern_str + "*"*i + '\n'
    return pattern_str
three = pattern(3)
print(three)
