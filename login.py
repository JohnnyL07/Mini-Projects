import time 

username = 'thisusername'
password ='thispassword'

u1 = input("Username: ")
p1 = input("Password: ")

if u1 == username and p1 == password:
    time.sleep(5)
    print("Access granted ")
elif u1 == username and p1 != password:
    time.sleep(2)
    print("Password is incorrect. Try again")
elif u1 != username and password == p1:
    time.sleep(2)
    print("Username is incorrect. Try again")
else: 
    time.sleep(2)
    print("Check both fields and try again. ")


  
