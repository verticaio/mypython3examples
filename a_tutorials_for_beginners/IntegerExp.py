# Arithmetic operations
# Addition         3 + 2
# Subtraction      3 - 2
# Multiplication   3 * 2
# Division         3 / 2
# Floor Division   3 // 2
# Exponent         3 ** 2
# Modulus          3 %  2              (Bolundukden sonra qaligi gosterir) 
"""
num = 5
float = 34.456456
string = "Hello"
print(type(num))
print(type(float))
print(type(string))

print( 17 % 10)
print(3 * (2 + 5 + 5))

num = 1
num += 1  # Or num = num + 1
print(num)
print(abs(-5))  # 5
print(round(5.3)) #5
print(round(5.6))  #6
print(round(5.5))  #6
print(round(6.75, 1 ))

num1 = 5
num2 = 6
print(num1 == num2)



i = -9
print(-i)
"""

# abs() for absolute value
# divmod() to find a quotient and remainder simultaneously
# pow() to raise a number to a certain power
# round() to round a number to a certain decimal point
# sum() to calculate the sum of the items in an iterable data type

#for x in range(0, 7):
#    x *= 2
#install agent oem12c on oracle linux    print(x)

a = 5 
b = 2
print(a // b)
print(a % b)
words = 80000       # How many words in our book
per_page_A = 300    # Option A, 300 words per page
per_page_B = 250    # Option B, 25- words per page
print(divmod(words,per_page_A))
print(divmod(words,per_page_B))


print(pow(2,5))
print(pow(5,2))

i = 17.34989436516001
print(round(i,4))

some_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print(sum(some_floats))
print(sum((8,16,64,512)))   # Calculate sum of numbers in tuple
print(sum({-10: 'x', -20: 'y', -30: 'z'}))  # Calculate sum of numbers in dictionary 