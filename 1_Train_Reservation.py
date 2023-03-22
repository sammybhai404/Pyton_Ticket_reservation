#importing Modules
import datetime
import random
import os
from tabulate import tabulate


#Gives Differnt Values 
def PNR():
	x = datetime.datetime.now()
	return x.strftime("%f")
	
	
#Data Storing Array
Train_seat= []
Ticket_Info=[]

#seats Add
Total_Seat = 40
for i in range(0,Total_Seat):
	Train_seat.append(0)
	


	
#Seat Avalible with Seat Number
def Seat_Position():
	#Av_Seat = 0;
	Store = []
	for i in range(len(Train_seat)):
		if Train_seat[i] == 0:
			#Av_Seat +=1
			Store.append(i+1)
		
	print("\nAvaible Seat Numbers\n")
	for i in range(len(Store)):
		if i%5 == 0:
			print(end="\n")
		print(Store[i],end=" ")
		
#Train Seat Available Or Not Check Section 
def Train_Seat():
	print("\n************SEATS************\n")
	Seat_A = 0;
	Seat_NA = 0;
	print("0 For Seat Available")
	print("1 For Seat Not Available")
			
	for i in range(len(Train_seat)):
		if(i%8 == 0):
			print(end="\n")
			
		if(Train_seat[i] == 0):
			Seat_A += 1
		if(Train_seat[i] == 1):
			Seat_NA += 1
		
		print(Train_seat[i],end=" ")
	print("\n")
	print("Total ",Seat_A,"Seats Available in train ")	
	print("Total ",Seat_NA,"Seats Are Booked ")
	print("\n")	
	
	
	aseat = input("Enter Y For Check Seat Available Seat Number : ")
	if(aseat == 'y' or aseat == 'Y'):
		Seat_Position()
	else:
		print("Thanks For Visit")	
	print("\n")
	
		
		
#Ticket Booking Function
#Empty Error 
def Err(a):
	if a == "":
		print("\n")
		print("Please Fill The Field")
		raise Exception("Train Seat Number Is exceed")
#Gender Error 
def Gender_Err(gender):
	if(gender != 'M' and gender != 'm' and gender != 'F'
           and gender != 'f' and gender != 'O' and gender != 'o'):
		print("\n")
		print("Gender Error : Gender is wrong " )
		raise Exception("Gender Error!!!!!")
			
#Ticket Book
def Ticket_Book():
	print("\n")
	Total_Ticket = int(input("Enter How Many Tickets You Want : "))
	obj={}
	array=[]
	for i in range(Total_Ticket):
		
		newar=[]
		name = input("Enter Passenger Name :")
		Err(name)
		newar.append(name)
		
		age = input("Enter Passenger Age : ")
		Err(age)
		newar.append(age)
		
		print("Gender \nM , m : Male  \nF , f : Female\nO , o : Others")
		gender = input("Enter Passenger Gender  : ")
		Gender_Err(gender)
		Err(gender)
		Upper = gender.upper()
		newar.append(Upper)
		
		
		print("\nBefore Selecting Seat please check Seat Availability ")
		print("Enter 'Y or y' for check Seat Press any key For No")
		Scheck = input()
		if Scheck == 'Y' or Scheck =='y':
			Train_Seat()
			
		seat = int(input("Please Select Your Seat : "))
		Err(seat)
		
		if(seat > 0 and seat <= Total_Seat):
			if Train_seat[seat-1] == 0:
				Train_seat[seat-1] = 1
				Seat_Add = "S",seat
				st = ''.join(map(str, Seat_Add))
				newar.append(st)
				array.append(newar)
				print("\n")
			else:
				print("Train Seat Is Already Book")
				raise Exception("Train Seat Already Booked")
				
		else:
			print("Train Seat Number Is exceed")
			raise Exception("Train Seat Number Is exceed")
			
						
	new = PNR()
	os.system('cls')
	print("\n###############################")
	print("Your Ticket Successfully Booked")
	print("Your PNR Number is ",new)
	print("Plase Save it ")
	print("###############################\n")
	
	obj['PNR'] = new
	obj['DATA']= array
	Ticket_Info.append(obj)
	print("\n")
	
	
	
#PNR check 
def data(index):
	print("\n")
	T_Info =Ticket_Info[index]['DATA']
	print("PNR Is Match ")
	print("Total ",len(T_Info)," Seat Booked By You \n")
	
	print("Passengers Details :")
	head = ["Name","Age","Gender","Seat NO"]
	print(tabulate(T_Info, headers=head, tablefmt="grid"))

def PNR_Check():
	index =999999;
	flag = False
	print("\n")
	p=input("Enter Your PNR Number : ")
	os.system('cls')
	for i in range(len(Ticket_Info)):
		for key in Ticket_Info[i]:
		
			if(p == Ticket_Info[i]['PNR']):
				index = i
				flag=True 
				break;
	if(flag):
		data(index)
	else:
		print("Please Enter Correct PNR Number")
	
	print("\n")
	


exit = "y"
for i in range(int(Total_Seat/10)):
	Train_seat[random.randint(0, Total_Seat)] = 1
try:
	while exit != 'E':
		print("****************S*********************")
		print("**********TRAIN RESERVATION**********")
		print("1. Book Train Ticket ")
		print("2. Check PNR Status ")
		print("3. Train Seat Availability")
		print("4. Exit ")
		print("\n")
		option = int(input("Enter The Options : "))
		#option 1
		if option == 1:
			Ticket_Book()
		
		if option == 2:
			PNR_Check();
		
		#option 3
		if option == 3:
			Train_Seat()	
		#option 4 
		if option == 4:
			exit = 'E'
			print("\n")
			print("Successufully Exit")
		
		if(option != 1 and option != 2 and option != 3 and option != 4):
			print("Wrong Options")
			break 
		
except :
	print("Some Error Found")
	
