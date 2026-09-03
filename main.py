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

"""

#Step 1, get input from user and create variables and lists
input1 = str(input())              #input string
numofpens = 0                      #number of pens
numofcolors = 0                    #number of colors
numofpaintings = 0                 #number of paintings
penlist = {}                       #list of pens
colorlist = []                     #list of colors
paintingprettyness = []            #list of painting prettyness
prettynessoptions = []             #list of prettyness options
temporarypainting = []             #temporary painting prettyness
doublecheck = []                   #double check variable
currentpen = ""                    #current pen
paintings = []                     #list of paintings
penchanges = []                    #list of pen changes

#Step 2, read input1 and distribute the values to the variables and lists
var1  = input1.split()
numofpens = int(var1[0])
numofcolors = int(var1[1])
numofpaintings = int(var1[2]) + 1
for i in range(numofpens):
    currentpen = str(input())
    var2 = currentpen.split()
    #var2[0] = pen color, var2[1] = pen prettyness, i = pen number
    penlist.setdefault(int(var2[0]), {}) [i + 1] = int(var2[1]) #Stores the pens, setdefault checks if the nested list exist or not
    var2.clear()
for i in range(numofpaintings - 1):
    penchanges.append(str(input()))
for i in range(1, numofcolors + 1):
    colorlist.append(i)
for p in range(numofpaintings):
    temporarypainting.clear()
    #print(penlist , "Penlist")
    for i in penlist:
    #Step 3, figure out which pen combination is the prettiest
        #print(i , "Current Color")
        temporarypainting.append(max(penlist[i].values())) # gets the prettiest pen of each color
        #print(temporarypainting , "Temporary Painting")
        #print(max(penlist[i].values()) , "Prittiest pen")
    #Step 4, check if the second prettyest pen can be replaced with one of the other pens
    for i in penlist:
        doublecheck = temporarypainting.copy() # copies the original best colors
        if len(penlist[i]) > 1: # checks if there is more than one pen of the current color
            doublecheck[doublecheck.index(min(doublecheck))] = sorted(penlist[i].values())[0] # replaces the least pretty pen with the second prettiest pen of the current color
        prettynessoptions.append(doublecheck) # adds it to the list of painting options
        #print(doublecheck , "Double Check")
    for i in prettynessoptions:
        #print(i, "current check")
        if sum(int(x) for x in i) > sum(int(x) for x in temporarypainting): # checks if the new painting is prettier than the original
            temporarypainting = i.copy() # if it is, it becomes the new best painting
            #print(temporarypainting , "New Best Painting")
    prettynessoptions.clear() # clears the list of painting options for the next round
    paintings.append(temporarypainting.copy()) # adds the best painting to the list of paintings
    #print(temporarypainting , "Best painting")
    #print(paintings , "Paintings")
    if len(penchanges) > p:
        penchanges[p] = penchanges[p].split() # 0 = operation 1 = pen number 2 = change number
        if int(penchanges[p][0]) == 1:
            for i in list(penlist):
                for key in list(penlist[i]):
                    if key == int(penchanges[p][1]):
                        value = penlist[i].pop(key)
                        penlist[int(penchanges[p][2])][int(penchanges[p][1])] = value
        elif int(penchanges[p][0]) == 2:
            for i in penlist:
                for key in penlist[i]:
                    if key == int(penchanges[p][1]):
                        penlist[i][key] = int(penchanges[p][2])
    #print("change" , p , penlist , "Penlist")
#print(paintings)
for painting in paintings:
    print(sum(int(x) for x in painting)) # prints the prettyness of each painting
