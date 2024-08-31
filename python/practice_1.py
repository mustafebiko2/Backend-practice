#1 strings
# price = 10
# print(price)

# name = input('whats your name')
# fav_color = input('my fv color is')
# print(name + 'likes' + fav_color )

# birth_year = input('birth_year:')
# age = 2019 - int(birth_year)
# print(age)

# 2 strings methods
# course = 'python for beginners'
# print(len(course)) = tan waxaa lagu eegah dhararka 
# erayada aad isticmallidi doontid sida username ama password

# course = 'python for beginners'
# print(course.find('p'))
# find waxaa loo isticmalaa markaa eray raadinaysid

# course = 'python for beginners'
# print(course.upper())
# ereyadaa waxaa looga dhigaah waaweyn

# course = 'python for beginners'
# print(course.lower())
# erayadaa looga dhigaah mid yar yar

# course = 'python for beginners'
# print(course.replace('beginners', 'totally beginners'))
# replace waxaa loo isticmaala inaad qoraal jirey ku badashid mid cusub

# course = 'python for beginners'
# print('Python' in course )
# # sidaan waa markaa isticmalysid booleen run ama been 
# # hada waa been mada aan isticmaalay 'p'ah capitaal letter
# print('python' in course )
# markan waa run madama aan isticmaalay 'p' yar 

# 3 arithmetic operation
# waxaan haysana la qabayd oo xisab ah midna wa intger ah tiro siman like '12345'
# midna wa float wa tiro dhafan sida '12.12,133.33' 
# marki intaa laga soo tago waxan haysana kudhufo oo ah sida ' '*' u qaybi / iyo ku dar +'
                # tusaale

# print(10 + 3) = 13
# print(10 * 3) = 30
# print(10 / 3) = 3.33333333335
# print(10 // 3) = 3
# print(10 % 3) = 1
# print(10 ** 3) = 1000
# x = 10
# x = x + 4
# print(x)
# x = 10
# x *=4
# print(x),
# 4 operator precedence
# x = 10 +3 * 2
# print(x)
# x = (10 +3) * 2 * 2
# print(x)
# exponentiantion 2 ** 3, multiplication,
# division, addition, subtraction, parenthesis

# math function
# x = 2.9
# print(round(x))
# x = 2.9
# print(abs(-2.9))
# abs always wuxuu soo celiyaah tiro possitiv ah
# x = 2.9
# print(round(x))
# NOTE moduls waa system ay ku kaydsan yihin waxliba sida store u leh qayboh fastfood, vegetable, and more 
# tusaale math fuction oo kale markaad rabtid store kaliyah inaad wax
# badan ka isticmaashid just IMPORT math waxliba si easy ah bad u isticmaalin 
 
# IF statement
# its_hot = False
# its_cold = False

# if its_hot:
#     print('its a hot day')
#     print("wear soft cloth")
# elif its_cold:
#      print("its cold day")
#      print("wear warm cloth")
# else:
#     print("its lovely day")
# print("enjoy your day")

# price = 1000000
# has_good_credit = False
# if has_good_credit:
#   down_payment = 0.1 * price
# else:
#    down_payment = 0.2 * price

# print(f"down payment: ${down_payment}")

# Explanation:
# Assigning Values:

# price = 1000000: This sets the price of the item to 1,000,000.
# has_good_credit = True: This variable is a boolean that indicates whether the customer has good credit.
# Conditional Statement:

# if has_good_credit:: Checks if the has_good_credit variable is True.
# If True, the down payment is calculated as 10% of the price.
# If False, the down payment is calculated as 20% of the price.
# Printing the Result:

# print(f"Down payment: ${down_payment}"): This line prints the calculated down payment using an f-string to format the output.
# Summary:
# Error: The use of price instead of print led to a NameError.
# Fix: Replace price with print to display the result correctly.

#logical operators

# has_high_income = False
# has_good_credit = True

# if has_high_income and has_good_credit:
#  print('eligable for loon')

# has_good_credit = True
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#  print('eligable for loon')