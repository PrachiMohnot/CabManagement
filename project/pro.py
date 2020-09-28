import pickle as p

def init():
 n=input('''
	    WELCOME TO MY PROJECT.

	1. Admin Login
	2. User Registration
	3. User Login
	4. Dealer Registration
	5. Dealer login
	6. Exit

     Enter your choice:  ''' )

 if(n=='1'):
  adminlogin()
 elif(n=='2'):
  user_reg()
 elif(n=='3'):
  user_log()
 elif(n=='4'):
  dealr_reg()
 elif(n=='5'):
  dealr_log()
 elif(n=='6'):
  exit()
 else:
  print("\t\tINVALID CHOICE")
  init()

def adminlogin():
 print("\n\tWelcome Admin\n ")
 a_name=input("Enter your Username: ")
 a_pass=input("Enter your password: ")
 
 file=open('admin.txt','rb')
 d=p.load(file)
 file.close()
 flag=0
 for i in d:
  if(d[i][1]==a_name and d[i][2]==a_pass):
   print("\n\tLogin Successful!")
   flag=1
   admin_opt()
 if(flag==0):
  print("\n\tLogin Unsucessful. Lets try Again.")
  init()
 

def admin_opt():
 n=input('''\n\n\tChoose Your Options\n
        1. View User
        2. Delete User
        3. View Cabs
        4. Delete Cabs
        5. View dealer
        6. Delete dealer
        7. View Requests
        8. Change Password
        9. Logout

        Enter your choice: ''')
 print()
    
 if(n=='1'):
  a_viewuser()
 elif(n=='2'):
  a_deleteuser()
 elif(n=='3'):
  a_viewcab()
 elif(n=='4'):
  a_deletecab()
 elif(n=='5'):
  a_viewdealer()
 elif(n=='6'):
  a_deletedealer()
 elif(n=='7'):
  a_viewreq()
 elif(n=='8'):
  a_changepass()
 elif(n=='9'):
  init()
 else:
  print("Invalid choice.Lets try Again.")
  admin_opt()

def a_viewuser():
 file=open('user.txt','rb')
 d=p.load(file)
 file.close()

 print("{0:^10} | {1:^12} | {2:^20} | {3:^12}".format("User id","Name","Email id","Contact")) 
 print()
 if(len(d)==0):
  print("\n\t\t\tNo User Found.")
 else:
  for i in d:
   print("{0:^10} | {1:^12} | {2:^20} |{3:^12}".format(i,d[i][0],d[i][1],d[i][3]))
 admin_opt()

def a_deleteuser():

 file=open('user.txt','rb')
 d=p.load(file)
 file.close()
 file1=open('request.txt','rb')
 d1=p.load(file1)
 file1.close()
 print("{0:^10} | {1:^12} | {2:^20} | {3:^12}".format("User id","Name","Email id","Contact")) 
 print()
 for i in d:
  print("{0:^10} | {1:^12} | {2:^20} | {3:<12}".format(i,d[i][0],d[i][1],d[i][3]))

 print("\n\t Delete User")
 id=input("Enter the User Id: ")
 flag=0
 for i in d:
  if(str(i)==id):
   flag=1
   d.pop(i)
   print("\n\n\tUser Deleted Successfully.")
   break
 if(flag==0):
  print("\n\tError:User not found")
 r=[]
 for i in d1:
  if(str(d1[i][2])==id):
   r.append(i)
 for i in r:
  d1.pop(i)
  print("Request Id %d deleted."%i)
 file=open('user.txt','wb')
 p.dump(d,file)
 file.close()
 file1=open('request.txt','wb')
 p.dump(d1,file1)
 file1.close()

 admin_opt()

def a_viewcab():
 file=open('cab.txt','rb')
 d=p.load(file)
 file.close()
 print("\n\t\tCab Details")
 print("{0:^8}| {1:^10}| {2:^11}| {3:^7}| {4:^12}| {5:^12}| {6:^5}".format("cab id","dealr id","Name","Number","From","To","Stat")) 
 print()
 if(len(d)==0):
  print("\n\t\t\tNo Cabs Found.")
 else:
  for i in d:
   print("{0:^8}| {1:^10}| {2:^11}| {3:^7}| {4:^12}| {5:^12}| {6:^5}".format(i,d[i][0],d[i][1],d[i][4],d[i][5],d[i][6],d[i][7]))
 admin_opt()

def a_deletecab():
 file=open('cab.txt','rb')
 d=p.load(file)
 file.close()
 file1=open('request.txt','rb')
 d1=p.load(file1)
 file1.close()

 print("\tCab Details")
 print("{0:^8}| {1:^10}| {2:^11}| {3:^7}| {4:^12}| {5:^12}| {6:^5}".format("cab id","dealr id","Name","Number","From","To","Stat")) 
 for i in d:
  print("{0:^8}| {1:^10}| {2:^11}| {3:^7}| {4:^12}| {5:^12}| {6:^5}".format(i,d[i][0],d[i][1],d[i][4],d[i][5],d[i][6],d[i][7]))

 print("\n\tDelelte Cab")
 print()
 id=input("Enter the Cab Id: ")

 r=[]
 for i in d1:
  if(str(d1[i][1])==str(d[int(id)][4])):
   r.append(i)
 for i in r:
  d1.pop(i)
  print("Req id %d deleted"%i)

 flag=0
 print()
 for i in d:
  if(str(i)==id):
   flag=1
   d.pop(i)
   print("\nCab Deleted Successfully")
   break
 if(flag==0):
  print("\n\tError:Cab not found")

 file=open('cab.txt','wb')
 p.dump(d,file)
 file.close()
 file1=open('request.txt','wb')
 p.dump(d1,file1)
 file1.close()


 admin_opt()

def a_viewdealer():
 file=open('dealer.txt','rb')
 d=p.load(file)
 file.close()
 print("\n\t\tDealer Details")
 print("{0:^10} | {1:^12} | {2:^20} | {3:^12} | {4:^10}".format("Dealr id","Name","Email id","Contact","Address"))
 print() 
 if(len(d)==0):
  print("\n\t\t\tNo User Found.")
 else:
  for i in d:
   print("{0:^10} | {1:^12} | {2:^20} | {3:^12} | {4:^10}".format(i,d[i][0],d[i][1],d[i][3],d[i][4]))
 admin_opt()

def a_deletedealer():
 file=open('dealer.txt','rb')
 d=p.load(file)
 file.close()
 file1=open('cab.txt','rb')
 d1=p.load(file1)
 file1.close()
 file2=open('request.txt','rb')
 d2=p.load(file2)
 file2.close()

 print("\n\t\tDealer Details")
 print("{0:^10} | {1:^12} | {2:^20} | {3:^12} | {4:^10}".format("Dealr id","Name","Email id","Contact","Address")) 
 print()
 for i in d:
  print("{0:^10} | {1:^12} | {2:^20} | {3:^12} | {4:^10}".format(i,d[i][0],d[i][1],d[i][3],d[i][4]))

 print("\n\t Delete Dealer")
 id=input("Enter the dealer Id: ")
 flag=0
 for i in d:
  if(str(i)==id):
   flag=1
   d.pop(i)
   print("\n\tDealer Deleted Successfully")
   break
 
 if(flag==1):
  c=[]
  flag=0
  for j in d1:
   if(str(d1[j][0])==id):
    c.append(j)
  for j in c:
   d1.pop(j)
   flag=1

  file1=open('cab.txt','wb')
  p.dump(d1,file1)
  file1.close()
  if(flag==1):
   print("\n\tAll Cabs with Dealer",id,"deleted")
  
  r=[]
  flag=0
  for k in d2:
   if(str(d2[k][0])==id):
    r.append(k)
  for k in r:
   d2.pop(k)
   flag=1

  file2=open('request.txt','wb')
  p.dump(d2,file2)
  file2.close()
  if(flag==1):
   print("\n\tAll Requests with Dealer",id,"deleted")

 else:

  if(flag==0):
   print("\n\tError:Dealer not found")

 file=open('dealer.txt','wb')
 p.dump(d,file)
 file.close()
 admin_opt()


def a_viewreq():
 file=open('request.txt','rb')
 d=p.load(file)
 file.close()
 print("\n\tRequest Details")
 print("{0:^7} | {1:^11} | {2:^8} | {3:^12} | {4:^15}".format("Req_id","Cab_Number","User_id","Stat","User Email")) 
 print()

 if(len(d)==0):
  print("{0:^7} | {1:^11} | {2:^8} | {3:^12} | {4:^15}".format("x","x","x","x","x"))
  print("\n\tNo Requests.")
 else: 
  for i in d:
   print("{0:^7} | {1:^11} | {2:^8} | {3:^12} | {4:^15}".format(i,d[i][1],d[i][2],d[i][3],d[i][4]))
 admin_opt()

  
def a_changepass():
 file=open('admin.txt','rb')
 d=p.load(file)
 file.close()
 
 o_pass=input("Enter old password:")
 c=0
 for i in d:
  if(d[i][2]==o_pass):
   c=1
   n_pass=input("Enter new password:")
   d[i][2]=n_pass
   file=open('admin.txt','wb')
   p.dump(d,file)
   file.close()

 if(c==1):  
  print("\nPassword Updated Successfully.\n")
 else:
  print("\nIncorrect password.Lets try again.\n")
  
 admin_opt()
 
def dealr_reg():
 print("\n\tWelcome to Dealer Registration Page.")
 d_name=input("Name: ")
 d_email=input("E_Mail: ")
 d_pass=input("Password: ")
 d_phone=input("Contact: ")
 d_add=input("Address: ")
 print()

 file=open("dealer.txt",'rb')
 d=p.load(file)
 file.close()
 lk=0
 
 for i in d:
  if(len(d)==0):
   lk=1
   break

  elif(d[i][0]==d_name or d[i][1]==d_email or d[i][3]==d_phone):
   print("\n\tOops! Looks like you've already registered.\n")
   init()
  
  else:
   lk=i
 
 
 d[lk+1]=[d_name,d_email,d_pass,d_phone,d_add]

 file=open("dealer.txt",'wb')
 p.dump(d,file)
 print('\nHey There! Your Registration is Successful.\nYour dealer ID is ',lk+1)
 print()
 file.close()
 init()
 

def dealr_log():
 file=open("dealer.txt",'rb')
 d=p.load(file)
 file.close()
 print("\n\tWelcome to Dealer Login Page.")
 print()

 dealr_name=input("Enter your name: ")
 dealr_pass=input("Enter password: ")

 c=0

 for i in d:
  if(d[i][0]==dealr_name and d[i][2]==dealr_pass):
   c=1
   break

 if(c==1):
    print("\n\tHURRAY!! LOGIN SUCCESSFUL")
    print()
    print('Dealer ID is: ',i)
    dealr_opt(i)
 else:
     print("\nOops!LOGIN UNSUCCESSFUL.Please Try Again.\n")
     init()
 

def dealr_opt(id):
 n=input('''\n\n\tWELCOME DEALER\n
        1. Add Cabs
        2. View Cabs
        3. Delete Cabs
        4. Change Cab Status
        5. Change Password
        6. View Requests
        7. Logout

        Enter your choice: ''')
    
 if(n=='1'):
  d_addcab(id)
 elif(n=='2'):
  d_viewcab(id)
 elif(n=='3'):
  deletecab(id)
 elif(n=='4'):
  changestat(id)
 elif(n=='5'):
  changepass(id)
 elif(n=='6'):
  view_req(id)
 elif(n=='7'):
  init()
 else:
  print("\tInvalid choice.Lets try again.")
  dealr_opt(id)

def changestat(d_id):
 file=open('cab.txt','rb')
 d=p.load(file)
 file.close()
 print("{0:^7}| {1:^10}| {2:^8}| {3:^7}| {4:^7}| {5:^11}| {6:^11}| {7:^4}".format("CabId","CabName","Model","Seater","Number","From","Destination","Stat"))
 for i in d:
  if(d[i][0]==d_id):
   print("{0:^7}| {1:^10}| {2:^8}| {3:^7}| {4:^7}| {5:^11}| {6:^11}| {7:^4}".format(i,d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]))
 
 if(len(d)==0):
  print("\n\t\t\tNo Cab Found.")
  dealr_opt(d_id)
 else:
  c_num=input("\nEnter cab number: ")
  c_num=c_num.lower()
  flag=0
  for i in d:
   if(d[i][0]==d_id and d[i][4]==c_num):
    print("Your current cab Status is ",d[i][7])
    stat=input("switch status to[A/NA]: ")
    if(stat=='A' or stat=='NA'):
     d[i][7]=stat
     print("\nStatus updated successfully.")
     file=open('cab.txt','wb')
     p.dump(d,file)
     file.close()
    else:
     print("\n\tInvalid Input.please try again.")
    dealr_opt(d_id)
   else:
    print("\n\tCab Not Found.")
    dealr_opt(d_id)
   
   
   
def d_addcab(d_id):
 print("\n\tEnter New Cab Details  ")
 cab_name=input("Enter cab name: ")
 cab_name=cab_name.lower()
 cab_model=input("Model[top/middle/basic]: ")
 cab_type=cab_type=input("Seater: ")
 cab_num=input("Cab Number: ")
 cab_num=cab_num.lower()
 cab_from=input("Cab From: ")
 cab_from=cab_from.lower()
 cab_to=input("Cab to: ")
 cab_to=cab_to.lower()
 cab_status='a'
 while(cab_status!='A' and cab_status!='NA' ):
  cab_status=input("Enter Status[A/NA]: ")
 
 file=open("cab.txt",'rb')
 d=p.load(file)
 file.close()
 
 lx=0
 for i in d:
  if(len(d)==0):
   lx=0
   break
  elif(d[i][4]==cab_num):
   print("Cab with this number already exists.")
   dealr_opt(d_id)
  else:
   lx=i

 d[lx+1]=[d_id,cab_name,cab_model,cab_type,cab_num,cab_from,cab_to,cab_status]
  
 file=open('cab.txt','wb')
 p.dump(d,file)
 print("Cab Added Successfully.")
 print("your cab id is:",lx+1)
 file.close()
 dealr_opt(d_id)
 
def d_viewcab(d_id):
 file=open('cab.txt','rb')
 d=p.load(file)
 file.close()
 print("{0:^7}| {1:^10}| {2:^8}| {3:^7}| {4:^7}| {5:^11}| {6:^11}| {7:^4}".format("Cab Id","Cab Name","Model","Seater","Number","From","Destination","Stat"))
 for i in d:
  if(d[i][0]==d_id):
   print("{0:^7}| {1:^10}| {2:^8}| {3:^7}| {4:^7}| {5:^11}| {6:^11}| {7:^4}".format(i,d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]))
 dealr_opt(d_id)

def deletecab(d_id):
 file=open('cab.txt','rb')
 d=p.load(file)
 file.close()
 print("{0:^7}| {1:^10}| {2:^8}| {3:^7}| {4:^7}| {5:^11}| {6:^11}| {7:^4}".format("Cab Id","Cab Name","Model","Seater","Number","From","Destination","Stat"))
 for i in d:
  if(d[i][0]==d_id):
   print("{0:^7}| {1:^10}| {2:^8}| {3:^7}| {4:^7}| {5:^11}| {6:^11}| {7:^4}".format(i,d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]))

 print("\nEnter Cab Details:")
 cab_name=input("Enter cab Name: ")
 cab_name=cab_name.lower()
 cab_num=input("Enter cab Number: ")
 cab_num=cab_num.lower()
 flag=0
 for i in d:
  if(d[i][0]==d_id and d[i][1]==cab_name and d[i][4]==cab_num):
   flag=1
   d.pop(i)
   break
 if(flag==0):
  print("\tSorry we could not find your cab.")
 else:
  print("\tCab Deleted Successfully.")


 file=open('cab.txt','wb')
 p.dump(d,file)
 file.close()
 dealr_opt(d_id)
 
def changepass(d_id):
 file=open('dealer.txt','rb')
 d=p.load(file)
 file.close()
 
 o_pass=input("Enter old password:")
 c=0
 for i in d:
  if(i==d_id and d[i][2]==o_pass):
   c=1
   n_pass=input("Enter new password:")
   d[i][2]=n_pass
   file=open('dealer.txt','wb')
   p.dump(d,file)
   file.close()

 if(c==1):  
  print("Password Updated Successfully.\n")
 else:
  print("Incorrect password.\n")
 dealr_opt(d_id)

def view_req(d_id):
 file=open('request.txt','rb')
 d=p.load(file)
 file.close()
 print("{0:^10} | {1:^12} | {2:^10} | {3:^7} | {4:^20}".format("req_num","cab_number","user_id","status","email"))
 c=0
 for i in d:
  if(d[i][0]==d_id):
   c=1
   print("{0:^10} | {1:^12} | {2:^10} | {3:^7} | {4:^20}".format(i,d[i][1],d[i][2],d[i][3],d[i][4]))
 if(c==0):
   print("{0:^10} | {1:^12} | {2:^10} | {3:^7} | {4:^20}".format("X","X","X","X","X"))
   print("\nNo New Requests.\n")

 dealr_opt(d_id)


def user_reg():
 print("\n\tWelcome to User Registration Page.")
 u_name=input("Name: ")
 u_email=input("E_Mail: ")
 u_pass=input("Password: ")
 u_phone=input("Contact: ")

 file=open("user.txt",'rb')
 d=p.load(file)
 file.close()
 
 lk=0
 for i in d:
  if(len(d)==0):
   lk=1
   break

  elif(d[i][0]==u_name or d[i][1]==u_email or d[i][3]==u_phone):
   print("\nYou've already registered.\n")
   init()
  
  else:
   lk=i

     
 d[lk+1]=[u_name,u_email,u_pass,u_phone]

 file=open("user.txt",'wb')
 p.dump(d,file)
 print('Registration successful.')
 file.close()
 print('Your User ID is ',lk+1)
 init()

def user_log():
 file=open("user.txt",'rb')
 d=p.load(file)
 file.close()

 
 print('\n\tWelcome to User Login Page. ')

 user_name=input("Enter your name: ")
 user_pass=input("Enter password: ")
 c=0
 for i in d:
   if(d[i][0]==user_name and d[i][2]== user_pass):
    c=1
    break

 if(c==1):
   print("LOGIN SUCCESSFUL")
   print("your User Id is",i) 
   user_opt(i)
 else:
     print("LOGIN UNSUCCESSFUL.Please Try Again.")
     init()
 

def user_opt(id):
 n=input(''' \n\tWELCOME USER.
        1. View Cabs
        2. Search Cabs
        3. Enquiry Cabs
        4. Change Password
        5. Logout

        Enter your choice: ''')
    
 if(n=='1'):
  viewcab(id)
 elif(n=='2'):
  searchcab(id)
 elif(n=='3'):
  enquirycab(id)
 elif(n=='4'):
  u_changepass(id)
 elif(n=='5'):
  init()
 else:
  print("Invalid choice.Lets try again.")
  user_opt(id)

def viewcab(u_id):
 file=open('cab.txt','rb')
 d=p.load(file)
 file.close()
 print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format("Name","Model","Seater","Number","From","To","Stat","Cab_id"))
 print()
 for i in d:
  if(d[i][7]=='NA'):
   pass
  else:
   print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format(d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7],i))
 user_opt(u_id)

def searchcab(u_id):
 file=open("cab.txt",'rb')
 d=p.load(file)
 file.close()
 print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format("Name","Model","Seater","Number","From","To","Stat","Cab_id"))
 print()
 for i in d:
  if(d[i][7]=='NA'):
   pass
  else:
   print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format(d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7],i))

 beg=input("enter from: ")
 beg=beg.lower()
 dest=input("enter destination: ")
 dest=dest.lower()
 c=0
 print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format("Name","Model","Seater","Number","From","To","Stat","Cab_id"))
 print()
 
 for i in d:
  if(d[i][5]==beg and d[i][6]==dest):
   c=1
   print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format(d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7],i))
 if(c==0):
  print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format("X","X","X","X","X","X","x","X"))
  print("\n\tSorry! We could not find your cab.")
  
  for i in d:
   if((d[i][5]==dest and d[i][6]==beg)):
    print("\nYou may check Related Search\n")
    print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format("Name","Model","Seater","Number","From","To","Stat","Cab_id"))
    print()
    print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format(d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7],i))
  
 user_opt(u_id) 


def enquirycab(user_id):
 file=open('cab.txt','rb')
 c=p.load(file)
 file.close()
 print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format("Name","Model","Seater","Number","From","To","Stat","Cab_id"))
 print()
 for i in c:
  if(d[i][7]=='NA'):
   pass
  else:
   print("{0:^10}| {1:^7}| {2:^7}| {3:^8}| {4:^10}| {5:^10}| {6:^5}| {7:^5}".format(c[i][1],c[i][2],c[i][3],c[i][4],c[i][5],c[i][6],c[i][7],i))

 file1=open('request.txt','rb')
 r=p.load(file1)
 file1.close()

 file2=open('user.txt','rb')
 u=p.load(file2)
 file2.close()
 
 print("\n\tTo Send Enquiry Request")
 cab_name=input("Enter cab name: ")
 cab_name=cab_name.lower()
 cab_num=input("Enter cab number: ")
 cab_num=cab_num.lower()
 flag=0
 lx=0

 for i in c:
  if(c[i][1]==cab_name and c[i][4]==cab_num and c[i][7]=='A'):
   flag=1
   break
  if(c[i][1]==cab_name and c[i][4]==cab_num and c[i][7]=='NA'):
   print("\nCab Not Available at the moment.")
   flag=2
  else:
   pass
   
 if(flag==1):
  for j in r:
   lx=j
  r[lx+1]=[c[i][0],c[i][4],user_id,c[i][7],u[user_id][1]]
  file1=open('request.txt','wb')
  p.dump(r,file1)
  print("Request Send Added Successfully.")
  print("your Request id is:",lx+1)
  file1.close()
 if(flag==0):
  print("\nSorry! Could Not Find Your Match.")
 
 user_opt(user_id)

def u_changepass(u_id):
 file=open('user.txt','rb')
 d=p.load(file)
 file.close()
 
 o_pass=input("Enter old password:")
 c=0
 for i in d:
  if(i==u_id and d[i][2]==o_pass):
   c=1
   n_pass=input("Enter new password:")
   d[i][2]=n_pass
   file=open('user.txt','wb')
   p.dump(d,file)

 if(c==1):  
  print("Password Updated Successfully.\n")
 else:
  print("Incorrect password.\n")
 file.close()
 user_opt(u_id)
 

init()


 
 
