# q.1 difference between java and python. 
# q.2 difference between c and python. 
# installation

print("hello world")

a=10.2
b=10

c=10<6
d="sagar"

print(a+b)
print(type(a))
print(type(c))
print(type(d))


#for loop
if a<b:
    print(str(b)+" is greater")
elif b>a:
    print(str(a)+" is greater")
else:
    print("is equal")
    
    
#declare a function in python    
def fun(name):
    print("my name is  "+str(name))
    
fun("sagar")

#casting

print(int(a))
print(float(b))
print(type(b))

#declare a multiline string   '''          '''          """                 """

a='''sddasf
sdfsdf
sdfs
fsdfsf
fsdfsdf
sfsdf
sdfsd
fsdfs'''


#string sliceing !
sag=" sagar khemnar"

print(sag[:6])
print(sag[6:])


#upper()  lower()
print(sag.upper() +""+ sag.lower())

#strip The strip() method removes any whitespace from the beginning or the end:
print(sag.strip())

#replace
print(sag.replace('a','j'))

#split
print(sag.split())

#concatination
str1="hello"
str2=" world"

print(str1+str2)

#formatination

str="sagar khemnar"

txt= "my name is {}"

print(txt.format(str))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."    #by index
print(myorder.format(quantity, itemno, price))

