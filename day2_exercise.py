# --- LEVEL 1 ---
 
first_name = 'Nathan'
last_name = 'Riley'
full_name = first_name + ' ' + last_name
country = 'Vietnam'
city = 'Ho Chi Minh City'
age = 15
year = 2026
is_married = False
is_tired = True
is_lights_on = False
skills = ['Drawing', 'Sleeping', 'Coding']

x,y= 5,10

# --- LEVEL 2 ---

print(type(first_name))
print(type(last_name))

print('Length of first name' , len(first_name))
print('Length of last name' , len(last_name))

print('Name is longer than last name', len(first_name) > len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two #cộng
diff = num_one - num_two #trừ
mul = num_one * num_two #nhân
div = num_one / num_two #chia
mod = num_one % num_two #chia lấy dư
exp = num_one ** num_two #lũy thừa
floor_division = num_one // num_two #chia lấy phần nguyên


# tìm chu vi hình tròn (ưtf quên rồi)
# công thức chu vi hình tròn = 2 * π * r

p = 3.14
r = 30

area_of_circle = p * r ** 2
circum_of_circle = 2 * p * r

user_input = input('Nhập bán kính hình tròn:')
r = float(user_input)
area_of_circle = p * r ** 2

name_user = input('Sủa tên mày ra?')
print('Ai sợ thì đi về, nhất là mày ấy' + ' ' + name_user)

age_user = input('Mày tuổi gì?')
print('Bày đặt' + ' ' + age_user + ' ' + 'hê')

help('keywords')