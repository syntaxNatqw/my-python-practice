
print(15)
print(147.0)
print(3+4j)


base_input = (float(input('Enter base:')))
height_input = (float(input('Enter height:')))
area_of_triangle = 0.5 * base_input * height_input
print('Area of triangle is:' + ' '+ str(area_of_triangle))

side_a = (float(input('Enter side a:')))
side_b = (float(input('Enter side b:')))
side_c = (float(input('Enter side c:')))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is' + ' ' + str(perimeter))

length_input = (float(input('Enter length:')))
width_input = (float(input('Enter width:')))
area_rectangle = length_input * width_input
perimeter_of_rec = 2 * (length_input + width_input)
print('The area of the rectangle:' + str(area_rectangle))
print('The perimeter of the rectangle:' + str(perimeter_of_rec))

radius_input = (float(input('Enter radius:')))
pi = 3.14
area_cir = pi * radius_input * radius_input
cir_cir = 2 * pi * radius_input
print('The area of the circle:' + str(area_cir))
print('The circumference of the circle:' + str(cir_cir))

# -----------------------------------------
# ôi vcl tôi ko có hiểu bài 8 tới bài 11 luôn má ơi ;-;;; gemini giải dùm á, mong mthu tương lai đừng dí mình

slope1 = 2
y_intercept = -2
x_intercept = 1
print("Task 8 -> Slope:", slope1, "y-int:", y_intercept, "x-int:", x_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Task 9 -> Slope:", slope2, "Distance:", distance)

print("Are the slopes equal?", slope1 == slope2)  # Spoiler: True (both are 2)

x = -3
y = x**2 + 6*x + 9
print("When x =", x, "y is:", y)  # Prints 0

# --------------------------------------------

print(len('python'))
print(len('dragon'))
print(len('python') > len('dragon'))

print(len('python') and len('dragon')) # whoops wrong answerr
# correct one:
print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')


# câu 15 là cái chó jz?? bt là nó sai nhma t thấy nó kì
# cảm ơn a gemini

# Option 1: Using 'not in' with 'and'
print('on' not in 'python' and 'on' not in 'dragon')

# Option 2: Checking the whole condition with 'not'
print(not ('on' in 'python' and 'on' in 'dragon'))


length_py = len('python') # this shit is an int
length_py_float = float(length_py)
length_py_str = str(length_py)
print(length_py)

# ??? ưtf câu 17
print(10 % 2 == 0) # 10 % 2 là để ktra nó chia hết cho 2 ko, ==0 là xem nó có số dư bằng 0 k
# nếu muốn ktra số:
number = 7
print(number % 2 == 0)


print(7//3 == int(2.7))
print(type('10') == type(10))
print(int(float('9.8')) == 10)

user_hours = (float(input('enter hours:')))
rate_per_hour = (float(input('Enter rate per hour:')))
earning = user_hours * rate_per_hour
print('Your weekly earning is' + str(earning))

years = float(input('Enter number of years you have lived.. or dont:'))
secon = 365 * 24 * 60 * 60 * years
print('You wont live long, but you have lived for' + str(secon) + 'seconds, yey')

# are you fucking kidding me
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')