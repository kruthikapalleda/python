str = "Durga Software Solutions"
for x in range(0, len(str)): #forward direction
    print(x,"--->",str[x])
    print()
for x in range(0, len(str)):
        index = -(x+1)
        print(index,"--->",str[(index)]) #backward direction
#print(str)
#print(len(str))
#below is used for each loop but only forward direction can be retrived
#str ="Durga software Solutions"
#for x in str:
 #   print(x)