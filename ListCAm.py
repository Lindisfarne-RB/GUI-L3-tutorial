list1 = [34, 56, 12, 67, 22]
# Largest
Largest = 0
for x in list1:
    if x > Largest:
        Largest = x

print(Largest)


# Smallest
small = 100
for x in list1:
    if x < small:
        small = x

print(small)

print("-----------------------------")
# Double the values in a list


newlist=[] # create an empty list
for x in list1:
    x = x * 2
    newlist.append(x) # to add a new value to the list
print(newlist)


