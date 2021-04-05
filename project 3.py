# ........ and shoot for the Sky in you getting a big promotion & opportunity
# Enter Full Names
print("Enter First and Last Name:")
fname = input("First Name: ") #First Name
lname = input("Last Name: ")#last Name
fullnames = fname + " " + lname

# Enter phone, email
print("Enter Customer's Phone Number")
phone = input()
print("Enter Customer's email address")
email = input()

# price of a used car
price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print('Feedback'.center(50, "="))
print("Full Names: ", fullnames)
print("Phone: " +phone)
print("Email: " + email)
print(f"Down Payment: {'{:.2f}'.format(down_payment)}")
print("Thank You".center(50, "="))
