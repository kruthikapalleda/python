l = [1,2,3,4,5] #checking is it mutable or immutable
b = bytes (l)
print(b)
b[2] = 10
print(b)


#l = [253, 254, 255, 256]  #"Status : ValueError "
#b = bytes(l)
#print(b)
