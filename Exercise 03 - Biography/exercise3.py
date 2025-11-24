First_name = input("Enter your first name: ")
Last_name = input("Enter your last name:")

Hometown = input("Enter your hometown:")
age = input("Enter your age:")
biography = ("My name is {First_name} {Last_name}. I am {age} years old and I come from {Hometown}.")
print (biography.format(First_name=First_name, Last_name=Last_name, age=age, Hometown=Hometown))