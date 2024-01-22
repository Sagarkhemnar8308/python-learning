#capitalize
str="sagar"
print(str.capitalize())     # make a first letter capitalize

#caseFold
str1="SamiR"
print(str1.casefold())     # make all word in lower case 

#center
str2="banana"
print(str2.center(100))

#count
str3="i\t am and\t i am sagar iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
print(str3.count("i"))
print(str3.count("i",0,10))

#encode
str4="encode in a pytho å n"
print(str4.encode())

#endswith
str5="sagar khemnar ."
print(str5.endswith('r'))

#expandtabs
str6 = "H\te\tl\tl\to"
print(str6.expandtabs(5))

#find
str7="hello, welcome i am sagar khemnar"
print(str7.find('w'))  #PRINT INDEX if search or written -1

#format
str8="my name is {name}.age is {age}"
print(str8.format(name="sagar" ,age=33))

#index
str9="saga dlkf fkr"
print(str9.index("fkr"))

#isalnum
str10="samirvarpeisdeveloper"
print(str10.isalnum())  #return true-false it check alphanumeric and number.

#isalpha
str11="stringnumbere leven" 
print(str11.isalpha())  #return true-false it check alphanumeric and number.

#isascii
str12 = "/?"
print(str12.isascii())

#join
str13="sagar"
print(str12.join(str13))

#zfill
str14="sagar khemnar 81"
print(str14.zfill(50))

#upper
str15="to upper case"
print(str15.upper())

#lower
str16="TO LOWER CASE"
print(str16.lower())

#rfind
str17="str12 is a string defined"
print(str17.rfind("defined"))




