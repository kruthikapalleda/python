#Find total number of non-empty substrings of a string with N characters. Here we use the word proper because we do not consider string itself as part of output.

def a(str):
    #print(a)
    n = len(str)
    return int(n * (n+1) /2)
s="abcde"
print(a(s))