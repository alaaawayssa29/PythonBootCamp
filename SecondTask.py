username = input("Enter username:").lower().replace(" ", "_")
password = input("Enter password:")
password_length = len(password)
print("Your username is:", username,", and your password is:", password,", with length equals to:", password_length)
check_password_length = len(password) >= 8
print(check_password_length)
check_username = username == "admin"
print(check_username)
check_password = password == "1234"
print(check_password)
check_defaul_account = (check_username and check_password)
print(check_defaul_account)
print(f"Welcome to your account with username: {username}, and the lenght of password is: {password_length}")