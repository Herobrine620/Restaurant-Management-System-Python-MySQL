#---------------------------- MODULE IMPORT ---------------------------------------------------
import mysql.connector

#------------------------------ MODULE CONNECTOR -----------------------------

x = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="620620", 
    database="Restaurant"
)
crm = x.cursor()

#------------------------------- OWNER ---------------------------------------
def owner():
	print("1. EDIT MENU") 
	print("2. SHOW MENU") 
	print("3. SHOW ORDERS") 
	print("4. SHOW FEEDBACKS")
	v = int(input("WHAT YOU WANT TO DO: "))
	if v == 1: 
		edit_menu()
	elif v == 2:
		sm = "select * from menu".format() 
		crm.execute(sm)
		m = crm.fetchall() 
		for x in m:
			print("# DISH NUMBER:",x[0],'\n',"---}",x[1],"(",'TYPE:',x[3],")",'\n\t\t','Price:',x[2])
	elif v == 3:
		so = "select * from cusdet".format()
		crm.execute(so)
		o = crm.fetchall()
		for x in o:
			print("ID:",x[0],"\n\t","QUANTITY:",x[1],"\n\t","NAME:",x[2],"(",x[3],";",x[4],")","\n\t\t","TOTAL PRICE:",x[5])
	elif v == 4:
		sf = "select * from feedback".format()
		crm.execute(sf)
		f = crm.fetchall() 
		print("NAME","\t","FEEDBACK")
		for x in f:
			print("NAME:",x[0],"\n\t","---}",x[1])

#---------------------------------- CUSTOMER -------------------------------------
def customer(): 
	while True:
		print('\n')
		print('1. VIEW MENU')
		print('2. BOOK ORDER')
		print('3. VIEW ORDER')
		print('4. CANCEL ORDER')
		print('5. FEEDBACK')
		print('6. EXIT')
		ch1 = int(input("ENTER YOUR CHOICE:"))
		if ch1 == 1: 
			view_menu()
		elif ch1 == 2: 
			book_order()
		elif ch1 == 3: 
			view_order()
		elif ch1 == 4: 
			cancel_order()
		elif ch1 == 5: 
			feedback()
		elif ch1 == 6: 
			welcome() 
			break
		else:
			print('\n',"INVALID INPUT",'\n',"TRY AGAIN",'\n')
			customer()

#---------------------------------- FOR EDIT MENU -------------------------------
def edit_menu():
	print("1. YES")
	print("2. NO")
	c = int(input("DO YOU WANT TO EDIT MENU:"))
	if c == 1:
		print("1. ADD A DISH")
		print("2. UPDATE PRICE OF A DISH") 
		d = int(input("DO YOU WANT TO DO:")) 
		if d == 1:
			while True :
				enter = int(input("1/-1")) 
				if enter == 1:
					ID = int(input('Enter item id:')) 
					ITEM_NAME = input('Enter item name:') 
					PRICE = int(input('Enter item price:')) 
					ITEM_TYPE = input('Enter item type:') 
					f="insert into menu values({},'{}',{},'{}')".format(ID,ITEM_NAME,PRICE,ITEM_TYPE)
					x.commit(f) 
				else:
					break
		elif d == 2:
			while True :
				enter = int(input("1/-1")) 
				if enter == 1:
					ID = int(input('Enter item id:'))
					PRICE = int(input('Enter item price:'))
					l="update menu set PRICE = {} where ID ={}".format(PRICE,ID)
					x.commit(l)
				else:
					break

#------------------------------ FOR VIEWNG MENU SECTION ---------------------
def view_menu():
	q = "select * from menu".format() 
	crm.execute(q)
	menu = crm.fetchall() 
	if len(menu)>0:
		print("\n\n <----------- Available Dishes------>")
		for i in menu:
			print("DISH NUMBER",i[0],'\n',"---}",i[1],"(",'TYPE:',i[3],")",'\n\t\t','Price:',i[2])
			print("\n\n") 
	x.commit()
	print("1. YES \n 2. MAIN PAGE")
	yn = int(input("DO YOU WANT TO ORDER AN ITEM? "))
	if yn == 1:
		book_order() 
	else:
		welcome()
		print("THANK YOU ")
		print("!WELCOME BACK TO MAIN PAGE!")

#---------------------------------- FOR BOOKING ORDER ---------------------------
def book_order():
	id = int (input("ENTER DISH NO. OF THE ITEM YOU WANT TO ORDER:"))
	quantity = int(input("ENTER QUANTITY:")) 
	name = input("ENTER YOUR NAME:")
	mobileno = int(input("ENTER YOUR MOBILE NO:")) 
	address = input("ENTER YOUR ADDRESS:")
	a = "select * from menu where id = {}".format(id) 
	crm.execute(a)
	a = crm.fetchall()
	b = a[0][2]
	c = quantity*b
	ins = "insert into cusdet values({},{},'{}',{},'{}',{})".format(id,quantity,name,mobileno,address,c)
	crm.execute(ins)
	print("\n","THANKS FOR ORDER","\n\n","YOUR ORDER HAS BEEN ORDERED SUCCESSFULLY","\n\n")
	print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")
	x.commit()

#---------------------------- FOR VEWING ORDER ------------------------
def view_order():
	c = int(input("ENTER YOUR NUMBER:"))
	d = "select * from cusdet where mobileno = {}".format(c) 
	print('\n',"YOUR RECENT ORDERS",'\n')
	crm.execute(d)
	p = crm.fetchall() 
	for i in p:
		r = "select * from menu,cusdet where mobileno = {} and menu.id = cusdet.id".format(c)
		crm.execute(r)
		e = crm.fetchall()
		for j in e:
			print('Id:',j[0],'\n','Item Name:',j[1],'\n','ItemType:',j[3],'\n','Total Price:',j[9],'\n','MobileNumber:',j[7],'\n','Address:',j[8],'\n')

#---------------------------- FOR CANCELLING PPRDER -----------------
def cancel_order():
	c = int(input("ENTER YOUR NUMBER:"))
	e = "delete from cusdet where mobileno = {}".format(c)
	crm.execute(e)
	print('\n\n',"YOUR ORDER HAS BEEN CANCELLED SUCCESSFULLY")
	print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE",'\n\n')
	x.commit()
#---------------------------- FEEDBACK ------------
def feedback():
	fd = input("ENTER YOUR NAME:")
	print("Write someting about us--")
	fdi = input()
	q = "insert into feedback values('{}','{}')".format(fd,fdi)
	crm.execute(q)
	print('\n')
	print("!THANKS FOR YOUR FEEDBACK!")
	print('\n')
	print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")
	print('\n')
	print('\n')
	x.commit() 

#------------------------- WELCOME PAGE I -----------------
def welcome():
	print('\n')
	print('\n')
	print(' | {{{{-------------------------------------}}}} |')
	print(' | ####################################################### |')
	print(' |:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: |')
	print(' | {------------------ WELCOME TO ----------------} |')
	print(' |:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: |')
	print(' | [::::::::::} STREET RESTAURANT {::::::::::] |')
	print(' |:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: |')
	print(' | ####################################################### |')
	print(' | {{{{-------------------------------------}}}} |')
	print('\n')
	print('\n')
	print("Press assigned keys for going forward")
	print("1.OWNER")
	print("2.CUSTOMER")
	print("3.EXIT")

# ---------------------- WELCOME PAGE II -------------------------
def welcome2():
	while True:
		ch = int(input("ENTER YOUR CHOICE: "))
		if ch == 1:
			con = input("ENTER PASSWORD TO CONFIRM THAT YOU ARE OWNER:")
			if con == "620620":
				owner()
			else:
				print("!INCORRECT PASSWORD TRY CUSTOMER OPTION!")
				break
		elif ch == 2:
			customer()
			break
		elif ch == 3:
			print("!THANK YOU!")
			break
		else :
			print("INVALID INPUT",'\n',"TRY AGAIN")
			welcome()

#-------------------------- START -----------------------
welcome()
welcome2()

#-------------------------- END -----------------------