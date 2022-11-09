print ("choose the mood 1: noraml 2: programer")
mood = input()

if mood == '1':
 print("choose your operator")
 print ("1 for +")
 print ("2 for -")
 print ("3 for *")
 print ("4 for /")
 print ("5 for %")
 
 choice = input("Enter choice(1/2/3/4/5): ")
 if choice in ('1', '2', '3', '4','5'):
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))

     if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)

     elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

     elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)

     elif choice == '4':
            print(num1, "/", num2, "=", num1 / num2)
     elif choice == '5':
            print(num1, "%", num2, "=", num1 % num2) 
	 
 
elif mood == '2':
 print ("choose what you want to be done")
 print ("1 for dicimal to binary")
 print ("2 for shift right ")
 print ("3 for shift left")
 print ("4 for &")
 print ("5 for |")
 
 choice = input("Enter choice(1/2/3/4/5): ")
 if choice in ('1', '2', '3', '4','5'):
  
  if choice =='1':
      num = int(input("enter your dicimal number"))
      print(bin(num)[2:])
  elif choice == '2':
		  num=int(input("enter the number to be shifted"))
		  shift=int(input("enter the number of shifts"))
		  num >>= shift
		  print(num)
  elif choice == '3':
		  num=int(input("enter the number to be shifted"))
		  shift=int(input("enter the number of shifts"))
		  num <<= shift
		  print(num)
  elif choice == '4':
		  num1=int(input("enter the first number"))
		  num2=int(input("enter the second number"))
		  num1 &= num2
		  print(num1)
  elif choice == '5':
		  num1=int(input("enter the first number"))
		  num2=int(input("enter the second number"))
		  num1 |= num2
		  print(num1)
 