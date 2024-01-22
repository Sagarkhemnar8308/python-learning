array = {
    "name1": {"name": "sagar", "age": 18, "city": "Akole", "pincode": 422601},
    "name2": {"name": "pankaj", "age": 19, "city": "sangamner", "pincode": 422602},
    "name3": {"name": "suraj", "age": 20, "city": "Akole", "pincode": 422603},
    "name4": {"name": "kcp", "age": 21, "city": "sangamner", "pincode": 422604},
}

a = input("Enter Your Name? ")
b = input("Enter Your City? ")

found = False

for std_name, std_info in array.items():
    if std_info["name"] == a and std_info["city"] == b:
        print(f"Your pincode is {std_info['pincode']}")
        found = True
        break
    elif std_info["name"] == a and std_info["city"] != b:
        print("City is Not Correct")
        found = True
        break
    elif std_info["name"] != a and std_info["city"] == b:
        print("Name is Not Correct")
        found = True
        break

if not found:
    print("Not Found User")
