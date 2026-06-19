# Check the strength of a Password
def check_password(password):
    if len(password)<8:
        raise Exception("Error! Password must be >= 8 characters")
    print("Password is Strong")
try:
    password = input("Enter a Password: ")
    check_password(password)
except Exception as e:
    print(e)
    