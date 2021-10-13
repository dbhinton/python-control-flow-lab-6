# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a messagecs such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

len_1 = int(input('length of a: '))
len_2 = int(input('length of b: '))
len_3 = int(input('length of c: '))

if len_1 == len_2 and len_2 == len_3:
    print('A triangel with side {len_1}, equilateral')
elif len_1 != len_2 and len_2 != len_3 and len_1 != len_3:
    print('scalene')
else:
    print('iscoles')
