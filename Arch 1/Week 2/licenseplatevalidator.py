import re

license=input("Enter license plate:").upper()

valid_licenses= [r'^[A-Z]{1,2}-[0-9]{1,2}-[0-9]{1,2}$',
                r'^[0-9]{1,2}-[0-9]{1,2}-[A-Z]{1,2}$',
                r'^[0-9]{1,2}-[A-Z]{1,2}-[0-9]{1,2}$',
                r'^[A-Z]{1,2}-[0-9]{1,2}-[A-Z]{1,2}$',
                r'^[A-Z]{1,2}-[A-Z]{1,2}-[0-9]{1,2}$',
                r'^[0-9]{1,2}-[A-Z]{1,2}-[A-Z]{1,2}$',
                r'^[0-9]{1,2}-[A-Z]{1,3}-[0-9]{1}$',
                r'^[0-9]{1}-[A-Z]{1,3}-[0-9]{1,2}$',
                r'^[A-Z]{1,2}-[0-9]{1,3}-[A-Z]{1}$',
                r'^[A-Z]{1}-[0-9]{1,3}-[A-Z]{1,2}$',
                r'^[A-Z]{1,3}-[0-9]{1,2}-[A-Z]{1}$',
                r'^[0-9]{1}-[A-Z]{1,2}-[0-9]{1,3}$'
                ]

valid=False

for pattern in valid_licenses: 
    if re.match(pattern, license):
        valid = True 
        break

if valid: print("valid")

else: print("invalid")