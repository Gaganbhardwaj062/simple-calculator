print("simple calculator")

num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))

print("1. Addition")
print("2. subtraction")
print("3. Divison")
print("4. multiplication")

choice = (input("enter the choice(1-4): "))

if choice == "1":
    print("resut=", num1 + num2)
elif choice == "2":
        print("result=", num1 - num2) 
elif choice == "4":
       print("resut=", num1 * num2)
elif choice == "3":
      if num2 !=0:
            print("result =", num1/num2)
      else:
            print("cannot divide by zero")

else:
      print("invalid choice")                         