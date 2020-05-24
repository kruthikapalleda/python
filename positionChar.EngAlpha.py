#Given a string of lower and uppercase characters, the task is to find that how many characters are at same position as in English alphabet.
def s(str):
    res = 0

    for i in range (len(str)):
        if((i == ord(str[i]) - ord('a')) or
           (i == ord(str[i]) - ord('A'))):
            res += 1
    return res
str ='AbgdeF'
print(s(str))