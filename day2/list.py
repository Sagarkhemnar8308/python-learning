list1=["sagar",1,2,3,44,"samir"]

print(list1[0])


list1[3:4]=["watermellon"]
print(list1)

#insert
list1.insert(1,'shghfgh')
print(list1)

#append
list1.append('dsfsdfsrtgertg')
print(list1)

#extends
list2=["sagar"]
list1.extend(list2)

#remove
print(list1.remove(2))
print(list1)

#pop
print(list1.pop(2))
print(list1)


# #clear
# list1.clear()
# print(list1)


# print all list
for x in list1:
    print("array is "+str(x))


len=range(len(list1))

for x in len:
    print(list1[x]) 



if "sagr" in list1:
    print("found........")
else:
    print("not found")    
