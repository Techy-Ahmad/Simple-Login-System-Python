username = "Admin"
password = "12345"

attempts = 0

for i in range(1, 4):
    print("Attempt", i, "/ 3")

    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    attempts += 1

    if user_input == username and pass_input == password:
        print("Login Successful")
        break
    else:
        print("Invalid credentials")

if attempts == 3 and user_input != username or pass_input != password:
    print("Account Locked")
