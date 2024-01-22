array=[
    {"name":"sagar","age":18,"city":"Akole","pincode":422601},
    {"name":"pankaj","age":19,"city":"sangamner","pincode":422602},
    {"name":"suraj","age":20,"city":"Akole","pincode":422603},
    {"name":"kcp","age":21,"city":"sangamner","pincode":422604},
]


a=input("Enter Your Name ?")
b=input("Enter Your City ?")

for std in array:
   if(std["name"]==a and std["city"]==b):
       print(f"your pincode is {std['pincode']} ")
       break
   elif(std["name"]==a and std["city"]!=b):
          print("City is Not Correct")
          break
   elif(std["name"]!=a and std["city"]==b):
          print("Name is Not correct")
          break
else:
 print("Not Found User")
      
    