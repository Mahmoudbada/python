import os
import time
os.system('cls')
print("wellcome to ITI shop")

product = ["apple","orange","banana"]
cost = [3,5,2]
unit = [30,20,50]
value =[]
costt = 0
n =len(product)
print (n)
while(True):
	user=input("for press owner = 1 , for press customer = 2   :")
	print (user)

	if (user == '1' ):
			print ("to see the products press: 1")
			print ("to add product press     : 2")
			print ("to modifie product press : 3")
			x=input()
			if (x=='1'):
				 print (" prooduct : cost : Avilable")
				 for i in range(n):
				  print(product[i],cost[i],unit[i])
			elif(x=='2'):
				 product.append(input("enter new product"))
				 cost.append(input("enter the cost"))
				 unit.append(input("enter the quantity"))
				 n=n+1
				 for i in range(n):
				  print(product[i],cost[i],unit[i])
			elif (x=='3'):
				 for i in range(n):
				  print(product[i],cost[i],unit[i])
				 print("choose the product to modifie")
				 num=product.index(input(""))
				 print(num)
				 product.insert(num,input("change the product name: "))
				 cost.insert(num,input("change the product cost: "))
				 unit.insert(num,input("change the product quantity: "))
				 for i in range(n):
				  print(product[i],cost[i],unit[i])
				 
	 
	elif (user == '2'):
			print ("to see the products press: 1")
			print ("to buy product press      : 2")
			x=input()
			if (x=='1'):
				 print (" prooduct : cost : Avilable")
				 for i in range(n):
				  print(product[i],cost[i],unit[i])
			elif(x=='2'):
				 print (" prooduct : cost : Avilable")
				 for i in range(n):
				  print(product[i],cost[i],unit[i])
				 num=product.index(input("choose your product:"))
				 q=input("choose the quantity : ")
				 costt = int(costt) + (int(q) * cost[num])
				 print (costt)	 
	else :
		break
	 