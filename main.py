"""
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
    list2.pop(0)
var5 = list1[0]

#Step 5:print the character at position
print(var5)
#Test results : 141/141 passed
#longest one: 2.2811791s        s2.3-106.in
#total time 32.097953s
"""

# Step 1, get input from user and create variables and lists
var1 = str(input())              #input string
var2 = ""                        #current string
count = 0                        #number of strings
list1 = []                       #list of strings
list2 = set()                    #list of duplicates
list3 = []                       #list of characters
list4 = []                       #list of removed strings
n = 0                            # current string being proccessed
for i in var1:
    if i.isdigit():
        count = count * 10 + int(i)
    else:
        break
for i in range(count):
    var2 = str(input())
    list1.append(var2)

#Step 2, basicly do everything
for i in list1:
    list4.append("")
    o = 0
    l = 0
    n += 1
    for j in i:
        if j in list3:
            list2.add(j)
        else:
            list3.append(j)
    print(list2)
    for j in i:
        o += 1
        print(o)
        if o % 2 == 0:
            list1[n-1] = list1[n-1][:o-1] + " " + list1[n-1][o:]
        print(list1[n-1], "\n list1 string ", n)
        l += 1
        print(l)
        if l % 2 == 0:
            list4[n-1] = list4[n-1][:l-1] + j
        print(list4[n-1], "\n list4 string ", n)
    list1[n-1] = list1[n-1].replace(" ", "")
    list4[n-1] = list4[n-1].replace(" ", "")
    print(list1[n-1], "\nlist1\n", list2, "duplicates\n")
    if set(list4[n-1].strip()).isdisjoint(set(list1[n-1].strip())) and (set(list1[n-1].strip()).issubset(set(list2)) or set(list4[n-1].strip()).issubset(set(list2))):    
        list1[n-1] = "T\n"
    else:
        list1[n-1] = "F\n"
    print(list1[n-1])
    list2.clear()
    list3.clear()
        

#Step 3, print the results
print("".join(list1))
