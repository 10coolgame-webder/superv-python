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