set = {10, 20, 30, 40, 50, 20, 30, "AAA", "BBB",43.23, None,None}
#print(set)
#print(type(set))
fs = frozenset(set)
print(fs)
print(type(fs))
for x in fs :
    print(x,end="\t")