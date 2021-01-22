# Name of exercise: Faulty calculator
# TO make a calculator that gives wrong answers for following calculations:
#1. 45 * 3 = 555
#2. 56 + 9 = 77
#3. 56/6 = 4

#code start from line 10

#Code words for operators
#additions means plus
#substraction means minus
#divide means division

#Instructions on hou to use
#To multiply any 2 numbers use keyword multiplication
#To add any 2 numbers use keyword addition
#To divide any 2 numbers use keyword division


print("Enter you first number here")#ask for the user for first number
userNumber_1 = int(input())

print("Enter you second number here")#ask for the user for second number
userNumber_2 = int(input())

print("Enter you operator name here")#ask for the user for operator
operator = input()

#The three lines below is the code for wrong calculation
if(userNumber_1==45) and (userNumber_2==3) and (operator == "multiplication"):
    print("The answer is 555")

elif(userNumber_1==56) and (userNumber_2==9) and (operator=="addition"):
    print("The answer is 77")

elif(userNumber_1==56) and (userNumber_2==6) and (operator=="Division"):
    print("The answer is 4")


#Conditins if the number is not equal to 45 and 3
if (userNumber_1 != 45) and (userNumber_2 != 3) and (operator == "multiplication"):
        print(userNumber_1 * userNumber_2)

elif (userNumber_1 != 45) and (userNumber_2 != 3) and (operator == "addition"):
        print(userNumber_1 + userNumber_2)

elif (userNumber_1 != 45) and (userNumber_2 != 3) and (operator == "Division"):
        print(userNumber_1/userNumber_2)

else:
    print()

