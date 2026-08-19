
#Step 1: get input from user and create variables
var1 = str(input())              #RLE original
var2 = int(input())              #position of character
list1 = [ ]                      #list of repeated letters
list2 = [ ]                      #list of numbers
var3 = ""                       #current number
var4 = 0                         #length of uncompressed var1
var5 = 0                       #character at position

#Step 2: get length of var1 (as if it wasnt RLE)

for i in var1:
    if i.isalpha():
        list1.append(i)
        if var3 != "":
            var4 = int(var3) + var4
            list2.append(var3)
            var3 = ""
    else:
        var3 += i
list2.append(var3)
var4 += int(var3)

#step 3: check if var2 is greater than length of var1. If so, skip step 3.5

if  var2 < var4:
    pass
else:
    var2 = var2 % var4


#Step 3.5: get modulo of var2


#Step 4: check if var2 is smaller than first item in list1. If so, assign var3 to the character at position 1 in list1. 
#If not, remove the first item in list1 and subtract that number from var2. Repeat step 4 until var2 is smaller than 
#the first item in list1. Then assign var3 to the character at position 1 in list1.

while var2 >= int(list2[0]):
    var2 -= int(list2[0])
    list1.pop(0)
var5 = list1[0]

#Step 5:print the character at position
print(var5)
