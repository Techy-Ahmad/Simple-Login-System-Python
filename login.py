def enter_info(user,pw):
    username="Admin"
    password="12345"
    if user==username and pw==password:
            return True
    else:
            return False
    
attempts = 0
for i in range(1,4):
    print("Attempt",i," / 3")

    user_input=input("Enter your Username: ")
    pass_input=input("Enter your Password: ")

    result=enter_info(user_input,pass_input)
    if result:
      print("login Success")
      break
    else:
      print("Login Denied")
    attempts+=1

if attempts==3:
    print("account locked")
