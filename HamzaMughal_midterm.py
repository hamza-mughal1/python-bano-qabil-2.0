#               Hamza Mughal
#               Mid term Examination


"""     Q1 - Write a Python program to do arithmetical operations addition and division.        """

num1 = int(input("enter the number 1 : "))
num2 = int(input("enter the number 2 : "))
sum = num1 + num2
divide = num1/num2
print(f"sum is {sum}")
print(f"divide is {divide}")


"""     Q2 - Write a Python program to find the area of a triangle      """

base = int(input("enter the base : "))
perp = int(input("enter the perpendicular : "))
area = base*perp*0.5
print(f"The area of triangle is {area}")

"""     Q3 - Write a Python program to convert Celsius to Fahrenheit.       """

celsius = int(input("enter the degree in celsius to convert into fahrenheit : "))
fahrenheit = (celsius*9/5)+32
print(f"{celsius} degree of celsius in fahrenheit is {fahrenheit}")


"""         Q4 - Write a Python program that return all datatypes that we discussed in the class.       """
num = 17
fl = 17.5
name  = "hamza"
bol = True
print(f"data type of {num} is {type(num)}")
print(f"data type of {fl} is {type(fl)}")
print(f"data type of {name} is {type(name)}")
print(f"data type of {bol} is {type(bol)}")