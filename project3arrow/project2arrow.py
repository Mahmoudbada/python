import os
import time

num = input('enter a number\n')
num=int(num)
while(1):
    os.system('cls')
    for i in range(((num*2)+1)):
        print()
		######################## for the right arrow
    for i in range(num):
	#prints middle line 
	# for the fisrt part spaces
	# for the second part print (* )
	# for the final part print  (* ) as it is the longest line 
        if i==(num-1):
		# for the fisrt part spaces
            print(" "*((num*6)-1),end="");
		# for the second part print (* )
            print("* "*(2*num),end="");
		# for the final part print (* ) as it is the longest line 
            print("* "*(i+1))
        else:
        #prints first part be4 the line
            print(" "*((num*6)-1),end="");
            print("  "*(2*num),end="")
            print((i+1)*"* ")
            
    for j in range(num-1,0,-1):
        #prints second part
        print(" "*((num*6)-1),end="");
        print("  "*(2*num),end="")
        print((j)*"* ")
    time.sleep(.5)
    os.system('cls')
    for i in range(num*3):
        print()
		##############################for the down arrow
    for i in range(0,num*2,1):
        print(" "*(num*5),end="")
        print(" "*(num-1),end="")
        print("*")
    for i in range(num):
        print((num*5)*" ",end="");
        for j in range(i):
            print(" ",end="")
        for j in range(i,num-1):
            print("*",end="")
        for j in range(i,num):
            print("*",end="")
        print()
    time.sleep(.5)
    os.system('cls')
    for i in range(((num*2)+1)):
        print()
		########################for left arrow
    for i in range(num):
        if i== (num-1):
        #prints middle line
            print(" *"*(2*num),end="");
            print(" *"*(i+1))
        else:
        #prints first part be4 the line
            
            print("  "*(num-i-1),end="")
            print((i+1)*" *")
        
    for j in range(1,num,1):
        #prints second part
        print("  ",end="")
        print((num-j)*" *")
        print((j)*"  ",end="")
    time.sleep(.5)
    os.system('cls')
	############################## for up arrow
    print()
    for i in range(num):
        print(" "*(num*5),end="")
        for j in range(i+1,num):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(0,num*2,1):
        print(" "*(num*5),end="")
        print(" "*(num-1),end="")
        print("*")
    time.sleep(.5)