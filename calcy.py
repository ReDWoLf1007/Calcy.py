#A simple calculator that calculates 4 operations on two integers

print("Enter 1st Integer: ")    //Input 1st Integer
k = (int)(input())
print("Enter 2nd Integer: ")    //Input 2nd Integer
l = (int)(input())

print("Enter the operation you want to perform (+,-,*,/): ")    //Enter the Arithmetic Expression/operation you want to perform.
a = input()        //input the 1 of the 4 operations

if a is + :                                //Operation 1: ADDITION
  print("Result: k + l = ", k + l)        //Adding the two integers & returning the result
elif a is - :                              //Operation 2: SUBTRACTION
  print("Result: k - l = ", k - l)        //Subtracting the two integers & returning the result
elif a is * :                              //Operation 3: MULTIPLICATION
  print("Result: k * l = ", k * l)        //Multiplying the two integers & returning the result
elif a is / :                              //Operation 4: DIVISION
  print("Result: k / l = ", k / l)        //Dividing the two integers & returning the result
else
  print("Wrong Choice!!!")                //For different choices
