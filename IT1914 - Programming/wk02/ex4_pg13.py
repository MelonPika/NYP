name = input("Enter name: ")
admin_number = input("Enter admin number: ")
age = float(input("Enter age: "))
gender = input("Enter gender (Male/Female): ")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / height**2        # **  -> exponential (power of) operator
bmi = weight / (height * height)
bmi = weight / height / height

print("\nHello!", name )
print("Your admin no is ", admin_number, " and age is ", age )
print(f"Your gender is {gender} and bmi is {bmi:.2f} ")


'''
precedence of operators
()
* /
+ -

'''

'''
a = 1 + 2
a += 1 + 2

"="  --> assignment operator, right associative'''