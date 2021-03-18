
def max_of_three_numbers(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

num1 = int(input("\nPlease enter the first number : \n"))
num2 = int(input("Please enter the second number : \n"))
num3 = int(input("Please enter the third number : \n"))

z=max_of_three_numbers(num1,num2,num3)
print("\nThe greatest value is "+str(z)+ ".\n")