#password
password="fifty four"
user_password=input("enter your password")
while password!=user_password:
    print ("Incorrect")
    user_password = input("enter your password")
print("access granted")