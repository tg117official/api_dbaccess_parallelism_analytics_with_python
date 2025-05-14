
import sys
# age| remaining tenure, prev_org_name
script, name, email, cno  = sys.argv # (path, ABC, abc@xyz.com)

prev_sal = int(input("Enter your Salary : "))
age = int(input("Enter your age : "))
prev_org = input("Enter your previous Org name : ")

employment_status = "employed"

print(f"Name : {name}")
print(f"Email : {email}")
print(f"Previous Salary : {prev_sal} | Current Salary : {prev_sal * 1.30}")
print(f"Cno : {cno}")
print(f"Status : {employment_status}")
print(f"Your age : {age} | remaining_tenure : {60 - age}")